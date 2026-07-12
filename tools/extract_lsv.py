#!/usr/bin/env python3
"""Extract Baldur's Gate 3 .lsv save packages without Divine/ExportTool.

This is a small, read-only extractor for BG3 package version 18. It writes the
unpacked files to a destination folder and never modifies the source save.
"""

from __future__ import annotations

import argparse
import shutil
import struct
import sys
import zlib
from pathlib import Path

try:
    import lz4.block
    import zstandard as zstd
except ImportError as exc:
    raise SystemExit(
        "Missing dependency. Install with:\n"
        "  python3 -m pip install --target /private/tmp/bg3-py-libs -r tools/requirements-save-tools.txt\n"
        "Then run with:\n"
        "  PYTHONPATH=/private/tmp/bg3-py-libs python3 tools/extract_lsv.py ..."
    ) from exc


ENTRY_SIZE_V18 = 272
SIGNATURE = b"LSPK"


def decompress_payload(raw: bytes, flags: int, uncompressed_size: int) -> bytes:
    method = flags & 0x0F
    if method == 0:
        return raw
    if method == 1:
        return zlib.decompress(raw)
    if method == 2:
        return lz4.block.decompress(raw, uncompressed_size=uncompressed_size)
    if method == 3:
        return zstd.ZstdDecompressor().decompress(raw, max_output_size=uncompressed_size)
    raise ValueError(f"unsupported compression flag 0x{flags:02x}")


def c_string(buf: bytes) -> str:
    return buf.split(b"\x00", 1)[0].decode("utf-8", "replace")


def safe_target(root: Path, package_name: str) -> Path:
    relative = Path(package_name.replace("\\", "/"))
    target = (root / relative).resolve()
    root_resolved = root.resolve()
    if root_resolved not in target.parents and target != root_resolved:
        raise ValueError(f"unsafe package path: {package_name}")
    return target


def extract_lsv(source: Path, destination: Path, overwrite: bool = False) -> list[tuple[str, int]]:
    data = source.read_bytes()
    if data[:4] != SIGNATURE:
        raise ValueError(f"{source} is not an LSPK/LSV package")

    version = struct.unpack_from("<I", data, 4)[0]
    if version != 18:
        raise ValueError(f"unsupported package version {version}; this tool handles BG3 v18 saves")

    header_offset = 4
    version2, file_list_offset, file_list_size, package_flags, _priority = struct.unpack_from(
        "<IQIBB", data, header_offset
    )
    num_parts = struct.unpack_from("<H", data, header_offset + 34)[0]

    if version2 != 18:
        raise ValueError(f"unexpected header version {version2}")
    if num_parts != 1:
        raise ValueError(f"multipart saves are not supported yet; package has {num_parts} parts")
    if package_flags & 0x04:
        raise ValueError("solid archives are not supported by this quick extractor")

    num_files = struct.unpack_from("<I", data, file_list_offset)[0]
    compressed_size = struct.unpack_from("<I", data, file_list_offset + 4)[0]
    compressed = data[file_list_offset + 8 : file_list_offset + 8 + compressed_size]
    file_list = lz4.block.decompress(compressed, uncompressed_size=ENTRY_SIZE_V18 * num_files)

    if destination.exists():
        if not overwrite:
            raise FileExistsError(f"destination already exists: {destination}")
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    extracted: list[tuple[str, int]] = []
    for index in range(num_files):
        offset = index * ENTRY_SIZE_V18
        name = c_string(file_list[offset : offset + 256])
        offset1, offset2, archive_part, flags, size_on_disk, uncompressed_size = struct.unpack_from(
            "<IHBBII", file_list, offset + 256
        )
        if archive_part != 0:
            raise ValueError(f"multipart entry is not supported: {name}")

        payload_offset = offset1 | (offset2 << 32)
        if (payload_offset & 0x0000FFFFFFFFFFFF) == 0xBEEFDEADBEEF:
            continue

        raw = data[payload_offset : payload_offset + size_on_disk]
        body = decompress_payload(raw, flags, uncompressed_size)
        target = safe_target(destination, name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
        extracted.append((name, len(body)))

    return extracted


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract a BG3 .lsv save package.")
    parser.add_argument("source", type=Path, help="Path to the .lsv save")
    parser.add_argument("destination", type=Path, help="Output folder")
    parser.add_argument("--overwrite", action="store_true", help="Replace destination folder if it exists")
    args = parser.parse_args()

    extracted = extract_lsv(args.source, args.destination, args.overwrite)
    print(f"Extracted {len(extracted)} files to {args.destination}")
    for name, size in extracted:
        print(f"{name}\t{size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
