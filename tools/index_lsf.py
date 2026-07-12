#!/usr/bin/env python3
"""Create searchable indexes from BG3 .lsf resources.

The JSONL output is intentionally compact: one node per line with parsed,
human-readable attributes where possible. It is meant for investigation, not
for repacking or editing savegames.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import struct
import sys
import zlib
from collections import Counter
from pathlib import Path

try:
    import lz4.block
    import lz4.frame
    import zstandard as zstd
except ImportError as exc:
    raise SystemExit(
        "Missing dependency. Install with:\n"
        "  python3 -m pip install --target /private/tmp/bg3-py-libs -r tools/requirements-save-tools.txt\n"
        "Then run with:\n"
        "  PYTHONPATH=/private/tmp/bg3-py-libs python3 tools/index_lsf.py ..."
    ) from exc


ATTR_TYPES = {
    0: "None",
    1: "Byte",
    2: "Short",
    3: "UShort",
    4: "Int",
    5: "UInt",
    6: "Float",
    7: "Double",
    8: "IVec2",
    9: "IVec3",
    10: "IVec4",
    11: "Vec2",
    12: "Vec3",
    13: "Vec4",
    14: "Mat2",
    15: "Mat3",
    16: "Mat3x4",
    17: "Mat4x3",
    18: "Mat4",
    19: "Bool",
    20: "String",
    21: "Path",
    22: "FixedString",
    23: "LSString",
    24: "ULongLong",
    25: "ScratchBuffer",
    26: "Long",
    27: "Int8",
    28: "TranslatedString",
    29: "WString",
    30: "LSWString",
    31: "UUID",
    32: "Int64",
    33: "TranslatedFSString",
}


class LSFIndex:
    def __init__(self, path: Path):
        self.path = path
        self.data = path.read_bytes()
        self.pos = 0
        self.version = 0
        self.engine_version = 0
        self.compression_flags = 0
        self.metadata_format = 0
        self.names: list[list[str]] = []
        self.values = b""
        self.nodes: list[dict] = []
        self.attributes: list[dict] = []

    def read_section(self, size_on_disk: int, uncompressed_size: int, allow_chunked: bool) -> bytes:
        if size_on_disk == 0 and uncompressed_size != 0:
            raw = self.data[self.pos : self.pos + uncompressed_size]
            self.pos += uncompressed_size
            return raw
        if size_on_disk == 0 and uncompressed_size == 0:
            return b""

        is_compressed = (self.compression_flags & 0x0F) != 0
        read_size = size_on_disk if is_compressed else uncompressed_size
        raw = self.data[self.pos : self.pos + read_size]
        self.pos += read_size
        return self.decompress(raw, uncompressed_size, self.version >= 2 and allow_chunked)

    def decompress(self, raw: bytes, uncompressed_size: int, chunked: bool) -> bytes:
        method = self.compression_flags & 0x0F
        if method == 0:
            return raw
        if method == 1:
            return zlib.decompress(raw)
        if method == 2:
            if chunked:
                return lz4.frame.decompress(raw)
            return lz4.block.decompress(raw, uncompressed_size=uncompressed_size)
        if method == 3:
            return zstd.ZstdDecompressor().decompress(raw, max_output_size=uncompressed_size)
        raise ValueError(f"unsupported compression method 0x{self.compression_flags:02x}")

    def name_from_hash(self, value: int) -> str:
        return self.names[value >> 16][value & 0xFFFF]

    def read_headers(self) -> tuple[bytes, bytes, bytes, bytes, bytes]:
        magic, self.version = struct.unpack_from("<II", self.data, self.pos)
        self.pos += 8
        if magic != 0x464F534C:
            raise ValueError(f"invalid LSF signature 0x{magic:08x}")

        if self.version >= 5:
            self.engine_version = struct.unpack_from("<q", self.data, self.pos)[0]
            self.pos += 8
        else:
            self.engine_version = struct.unpack_from("<i", self.data, self.pos)[0]
            self.pos += 4

        if self.version < 6:
            raise ValueError(f"unsupported LSF version {self.version}; expected BG3 v6+")

        fields = struct.unpack_from("<IIIIIIIIII BBH I", self.data, self.pos)
        self.pos += struct.calcsize("<IIIIIIIIII BBH I")
        (
            strings_u,
            strings_d,
            keys_u,
            keys_d,
            nodes_u,
            nodes_d,
            attrs_u,
            attrs_d,
            values_u,
            values_d,
            self.compression_flags,
            _unknown2,
            _unknown3,
            self.metadata_format,
        ) = fields

        strings = self.read_section(strings_d, strings_u, False)
        nodes = self.read_section(nodes_d, nodes_u, True)
        attributes = self.read_section(attrs_d, attrs_u, True)
        values = self.read_section(values_d, values_u, True)
        keys = self.read_section(keys_d, keys_u, True)
        return strings, nodes, attributes, values, keys

    def read_names(self, blob: bytes) -> None:
        stream = io.BytesIO(blob)
        num_hash_entries = struct.unpack("<I", stream.read(4))[0]
        for _ in range(num_hash_entries):
            chain_len = struct.unpack("<H", stream.read(2))[0]
            chain = []
            for _ in range(chain_len):
                name_len = struct.unpack("<H", stream.read(2))[0]
                chain.append(stream.read(name_len).decode("utf-8", "replace"))
            self.names.append(chain)

    def read_nodes(self, blob: bytes) -> None:
        long_nodes = self.version >= 3 and self.metadata_format == 1
        node_size = 16 if long_nodes else 12
        for offset in range(0, len(blob), node_size):
            if long_nodes:
                name_hash, parent, next_sibling, first_attr = struct.unpack_from("<Iiii", blob, offset)
            else:
                name_hash, first_attr, parent = struct.unpack_from("<Iii", blob, offset)
                next_sibling = -1
            self.nodes.append(
                {
                    "idx": offset // node_size,
                    "name": self.name_from_hash(name_hash),
                    "parent": parent,
                    "first_attr": first_attr,
                    "next_sibling": next_sibling,
                    "children": 0,
                    "attrs": {},
                }
            )

        for node in self.nodes:
            parent = node["parent"]
            if 0 <= parent < len(self.nodes):
                self.nodes[parent]["children"] += 1

    def read_attributes(self, blob: bytes) -> None:
        long_attrs = self.version >= 3 and self.metadata_format == 1
        if long_attrs:
            for offset in range(0, len(blob), 16):
                name_hash, type_length, next_attr, value_offset = struct.unpack_from("<IiiI", blob, offset)
                self.attributes.append(
                    {
                        "idx": offset // 16,
                        "name": self.name_from_hash(name_hash),
                        "type": type_length & 0x3F,
                        "length": type_length >> 6,
                        "offset": value_offset,
                        "next": next_attr,
                    }
                )
            return

        data_offset = 0
        previous_refs: list[int] = []
        for offset in range(0, len(blob), 12):
            name_hash, type_length, node_index = struct.unpack_from("<IIi", blob, offset)
            attr = {
                "idx": offset // 12,
                "name": self.name_from_hash(name_hash),
                "type": type_length & 0x3F,
                "length": type_length >> 6,
                "offset": data_offset,
                "next": -1,
            }
            list_index = node_index + 1
            while len(previous_refs) <= list_index:
                previous_refs.append(-1)
            if previous_refs[list_index] != -1:
                self.attributes[previous_refs[list_index]]["next"] = attr["idx"]
            previous_refs[list_index] = attr["idx"]
            data_offset += attr["length"]
            self.attributes.append(attr)

    def read_string(self, offset: int, length: int) -> str:
        data = self.values[offset : offset + length]
        if length and data.endswith(b"\x00"):
            data = data[:-1]
        return data.rstrip(b"\x00").decode("utf-8", "replace")

    @staticmethod
    def guid_from_dotnet_bytes(data: bytes) -> str:
        if len(data) < 16:
            return data.hex()
        first, second, third = struct.unpack_from("<IHH", data, 0)
        rest = data[8:16]
        return f"{first:08x}-{second:04x}-{third:04x}-{rest[0]:02x}{rest[1]:02x}-{rest[2:].hex()}"

    def read_value(self, attr: dict):
        offset = attr["offset"]
        length = attr["length"]
        attr_type = attr["type"]
        data = self.values[offset : offset + length]

        try:
            if attr_type in (20, 21, 22, 23, 29, 30):
                return self.read_string(offset, length)
            if attr_type == 19:
                return bool(data[0]) if data else False
            if attr_type == 1:
                return data[0] if data else None
            if attr_type == 2:
                return struct.unpack_from("<h", data)[0]
            if attr_type == 3:
                return struct.unpack_from("<H", data)[0]
            if attr_type == 4:
                return struct.unpack_from("<i", data)[0]
            if attr_type == 5:
                return struct.unpack_from("<I", data)[0]
            if attr_type == 6:
                return struct.unpack_from("<f", data)[0]
            if attr_type == 7:
                return struct.unpack_from("<d", data)[0]
            if attr_type == 11:
                return list(struct.unpack_from("<ff", data))
            if attr_type == 12:
                return list(struct.unpack_from("<fff", data))
            if attr_type == 13:
                return list(struct.unpack_from("<ffff", data))
            if attr_type == 24:
                return struct.unpack_from("<Q", data)[0]
            if attr_type in (26, 32):
                return struct.unpack_from("<q", data)[0]
            if attr_type == 27:
                return struct.unpack_from("<b", data)[0]
            if attr_type == 31:
                return self.guid_from_dotnet_bytes(data)
            if attr_type == 25:
                strings = re.findall(rb"[A-Za-z0-9_\.\-]{4,}", data)
                if strings:
                    return {
                        "scratch_strings": [item.decode("utf-8", "replace") for item in strings[:80]],
                        "bytes": length,
                    }
                return {"bytes": length}
            if attr_type == 28 and len(data) >= 6:
                version = struct.unpack_from("<H", data, 0)[0]
                handle_len = struct.unpack_from("<i", data, 2)[0]
                handle = ""
                if 0 <= handle_len <= len(data) - 6:
                    handle = data[6 : 6 + handle_len].decode("utf-8", "replace")
                return {"version": version, "handle": handle}
            return {"raw_hex": data[:32].hex(), "bytes": length}
        except Exception as exc:
            return {"error": str(exc), "raw_hex": data[:32].hex(), "bytes": length}

    def attach_attributes(self) -> None:
        for node in self.nodes:
            attr_idx = node["first_attr"]
            seen = 0
            while attr_idx != -1 and 0 <= attr_idx < len(self.attributes) and seen < 1000:
                attr = self.attributes[attr_idx]
                node["attrs"][attr["name"]] = {
                    "type": ATTR_TYPES.get(attr["type"], str(attr["type"])),
                    "value": self.read_value(attr),
                }
                attr_idx = attr["next"]
                seen += 1

    def build(self) -> None:
        strings, nodes, attributes, values, _keys = self.read_headers()
        self.values = values
        self.read_names(strings)
        self.read_nodes(nodes)
        self.read_attributes(attributes)
        self.attach_attributes()

    def summary(self) -> dict:
        names = Counter(node["name"] for node in self.nodes)
        roots = [
            {
                "idx": node["idx"],
                "name": node["name"],
                "children": node["children"],
                "attrs": list(node["attrs"].keys())[:20],
            }
            for node in self.nodes
            if node["parent"] == -1
        ]
        return {
            "path": str(self.path),
            "version": self.version,
            "engine_version": self.engine_version,
            "compression_flags": f"0x{self.compression_flags:02x}",
            "metadata_format": self.metadata_format,
            "nodes": len(self.nodes),
            "attributes": len(self.attributes),
            "values_bytes": len(self.values),
            "top_node_names": names.most_common(30),
            "roots": roots,
        }

    def write_jsonl(self, path: Path) -> None:
        with path.open("w", encoding="utf-8") as handle:
            for node in self.nodes:
                record = {
                    "idx": node["idx"],
                    "name": node["name"],
                    "parent": node["parent"],
                    "children": node["children"],
                    "attrs": node["attrs"],
                }
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    def write_focus(self, path: Path, pattern: str) -> int:
        regex = re.compile(pattern, re.IGNORECASE)
        count = 0
        with path.open("w", encoding="utf-8") as handle:
            for node in self.nodes:
                record = {
                    "idx": node["idx"],
                    "name": node["name"],
                    "parent": node["parent"],
                    "attrs": node["attrs"],
                }
                text = json.dumps(record, ensure_ascii=False)
                if regex.search(text):
                    handle.write(text + "\n")
                    count += 1
        return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Index a BG3 .lsf resource into searchable JSONL.")
    parser.add_argument("source", type=Path, help="Path to .lsf file")
    parser.add_argument("--jsonl", type=Path, required=True, help="JSONL output path")
    parser.add_argument("--summary", type=Path, help="Optional summary JSON output path")
    parser.add_argument("--focus", type=Path, help="Optional filtered text output path")
    parser.add_argument(
        "--focus-pattern",
        default=(
            "Kao|Stefan|Astarion|Lae'?zel|Shadowheart|Gale|Wizard|Cleric|Fighter|"
            "Rogue|DeathDomain|Conjuration|BattleMaster|Thief|Spell|Passive|Boost|"
            "Longstrider|Aid|Warding|Bond|Elixir|Potion|Feat|Class|Level|Prepared|"
            "Inventory|Item"
        ),
        help="Regex for --focus output",
    )
    args = parser.parse_args()

    index = LSFIndex(args.source)
    index.build()
    args.jsonl.parent.mkdir(parents=True, exist_ok=True)
    index.write_jsonl(args.jsonl)

    summary = index.summary()
    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(summary, ensure_ascii=False, indent=2))

    if args.focus:
        args.focus.parent.mkdir(parents=True, exist_ok=True)
        count = index.write_focus(args.focus, args.focus_pattern)
        print(f"Wrote {count} focused records to {args.focus}")

    print(f"Wrote {len(index.nodes)} records to {args.jsonl}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
