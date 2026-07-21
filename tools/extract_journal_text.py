#!/usr/bin/env python3
"""Extract real in-game quest/journal text from the installed BG3 game files.

Builds a local cache `tools/journal-text/quest_text.json` mapping each quest to
its localized title and per-step journal entries, by joining two game files:

  * `Gustav.pak` → `Mods/GustavDev/Story/Journal/quest_prototypes.lsx`
    (QuestID → QuestTitle handle, and each QuestStep ID → Description handle)
  * `English.pak` → `Localization/English/english.loca`
    (localization handle → display text)

The resulting text is Larian's copyrighted game content, so the cache is
gitignored and generated locally from the user's own installation. This script
contains no game text — only the extraction logic.

No external tools (Divine/LSLib) required: it reads the LSPK v18 package format
and the LOCA localization format directly, seeking so the 12 GB `Gustav.pak` is
never loaded whole.

Usage:
    python3 tools/extract_journal_text.py [--game-data DIR] [--out PATH]
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/private/tmp/bg3-py-libs")
import lz4.block  # noqa: E402
import zstandard as zstd  # noqa: E402
import zlib  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GAME_DATA = Path(
    "/Users/tmind/Library/Application Support/Steam/steamapps/common/"
    "Baldurs Gate 3/Baldur's Gate 3.app/Contents/Data"
)
QUEST_LSX = "Mods/GustavDev/Story/Journal/quest_prototypes.lsx"
LOCA_NAME = "Localization/English/english.loca"
ENTRY_SIZE = 256 + 16


# ---------- LSPK (.pak) selective reader ----------

def lspk_index(pak: Path):
    """Return (open file, {name: (offset, flags, size_on_disk, uncompressed)})."""
    f = open(pak, "rb")
    head = f.read(64)
    if head[:4] != b"LSPK":
        raise ValueError(f"{pak} is not an LSPK package")
    _v2, file_list_offset, _fls, _flags, _prio = struct.unpack_from("<IQIBB", head, 4)
    f.seek(file_list_offset)
    num_files = struct.unpack("<I", f.read(4))[0]
    comp_size = struct.unpack("<I", f.read(4))[0]
    file_list = lz4.block.decompress(f.read(comp_size), uncompressed_size=ENTRY_SIZE * num_files)
    index = {}
    for i in range(num_files):
        o = i * ENTRY_SIZE
        name = file_list[o : o + 256].split(b"\x00", 1)[0].decode("ascii", "replace")
        o1, o2, _part, flags, sod, unc = struct.unpack_from("<IHBBII", file_list, o + 256)
        index[name] = (o1 | (o2 << 32), flags, sod, unc)
    return f, index


def lspk_read(f, index, name: bytes) -> bytes:
    offset, flags, sod, unc = index[name]
    f.seek(offset)
    raw = f.read(sod)
    method = flags & 0x0F
    if method == 0:
        return raw
    if method == 1:
        return zlib.decompress(raw)
    if method == 2:
        return lz4.block.decompress(raw, uncompressed_size=unc)
    if method == 3:
        return zstd.ZstdDecompressor().decompress(raw, max_output_size=unc)
    raise ValueError(f"unsupported compression flag 0x{flags:02x} for {name}")


# ---------- LOCA (localization) parser ----------

def parse_loca(data: bytes) -> dict[str, str]:
    if data[:4] != b"LOCA":
        raise ValueError("not a LOCA file")
    _magic, num, texts_offset = struct.unpack_from("<4sII", data, 0)
    entry_size = 64 + 2 + 4
    headers = []
    off = 12
    for _ in range(num):
        key = data[off : off + 64].split(b"\x00", 1)[0].decode("ascii", "replace")
        _version, length = struct.unpack_from("<HI", data, off + 64)
        headers.append((key, length))
        off += entry_size
    loca = {}
    t = texts_offset
    for key, length in headers:
        loca[key] = data[t : t + length].split(b"\x00", 1)[0].decode("utf-8", "replace")
        t += length
    return loca


# ---------- quest_prototypes.lsx parser ----------

def parse_quest_prototypes(xml: bytes):
    """QuestID -> {'title_handle': str|None, 'steps': {stepID: desc_handle}}."""
    root = ET.fromstring(xml)
    quests = {}
    for node in root.iter("node"):
        attrs = {}
        for a in node.findall("attribute"):
            attrs[a.get("id")] = a.get("handle") or a.get("value")
        qid = attrs.get("QuestID")
        if not qid:
            continue
        steps = {}
        children = node.find("children")
        if children is not None:
            for step in children.findall("node"):
                sa = {a.get("id"): (a.get("handle") or a.get("value")) for a in step.findall("attribute")}
                sid = sa.get("ID")
                if sid:
                    steps[sid] = sa.get("Description")
        quests[qid] = {"title_handle": attrs.get("QuestTitle"), "steps": steps}
    return quests


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--game-data", default=str(DEFAULT_GAME_DATA), help="BG3 .../Contents/Data dir")
    ap.add_argument("--out", default=str(ROOT / "tools/journal-text/quest_text.json"))
    args = ap.parse_args()

    data_dir = Path(args.game_data)
    gustav = data_dir / "Gustav.pak"
    english = data_dir / "Localization/English.pak"
    for p in (gustav, english):
        if not p.exists():
            raise SystemExit(f"game file not found: {p}\nPass --game-data with your BG3 Data dir.")

    gf, gidx = lspk_index(gustav)
    quests = parse_quest_prototypes(lspk_read(gf, gidx, QUEST_LSX))
    ef, eidx = lspk_index(english)
    loca = parse_loca(lspk_read(ef, eidx, LOCA_NAME))

    result = {}
    for qid, q in quests.items():
        title = loca.get(q["title_handle"] or "", "")
        steps = {}
        for sid, handle in q["steps"].items():
            txt = loca.get(handle or "", "")
            if txt:
                steps[sid] = txt
        result[qid] = {"title": title, "steps": steps}

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=0), encoding="utf-8")
    n_steps = sum(len(q["steps"]) for q in result.values())
    print(f"Wrote {out.relative_to(ROOT)}: {len(result)} quests, {n_steps} step texts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
