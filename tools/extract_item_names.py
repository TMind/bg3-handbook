#!/usr/bin/env python3
"""Extract real item display names from the installed BG3 game files.

Builds a local cache `tools/item-names/item_names.json` mapping each item's
internal stat name to its localized display name, by joining:

  * `Gustav.pak` / `Shared.pak` → `Public/*/RootTemplates/_merged.lsf`
    (item template → DisplayName handle + Stats, with ParentTemplateId
    inheritance so items that inherit their name from a parent still resolve)
  * `English.pak` → `Localization/English/english.loca`
    (localization handle → display text)

Item display names are Larian's copyrighted content, so the cache is
gitignored and generated locally from the user's own installation. This script
contains no game text — only the extraction logic. It reuses the LSPK reader
from `extract_journal_text.py` and the LSF parser from `index_lsf.py`, so no
LSLib/Divine is required.

Usage:
    python3 tools/extract_item_names.py [--game-data DIR] [--out PATH]
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parents[0]
sys.path.insert(0, str(TOOLS))

from extract_journal_text import DEFAULT_GAME_DATA, lspk_index, lspk_read, parse_loca  # noqa: E402
from index_lsf import LSFIndex  # noqa: E402

# RootTemplates that carry item DisplayName/Stats, by pak. Order matters:
# earlier paks win when the same template id appears more than once.
ROOT_TEMPLATES = [
    ("Shared.pak", "Public/Shared/RootTemplates/_merged.lsf"),
    ("Gustav.pak", "Public/Gustav/RootTemplates/_merged.lsf"),
    ("Gustav.pak", "Public/GustavDev/RootTemplates/_merged.lsf"),
]
LOCA_NAME = "Localization/English/english.loca"


def _val(attr):
    v = attr.get("value") if isinstance(attr, dict) else None
    return v if isinstance(v, str) else None


def _handle(attr):
    v = attr.get("value") if isinstance(attr, dict) else None
    if isinstance(v, dict):
        return (v.get("handle") or "").replace("\x00", "")
    return ""


def collect_templates(data_dir: Path):
    """template_guid -> {'name_handle', 'parent', 'stats'} across the paks."""
    by_guid = {}
    for pak_name, inner in ROOT_TEMPLATES:
        pak = data_dir / pak_name
        if not pak.exists():
            continue
        f, index = lspk_index(pak)
        if inner not in index:
            continue
        raw = lspk_read(f, index, inner)
        # LSFIndex reads from a path, so stage the extracted resource.
        with tempfile.NamedTemporaryFile(suffix=".lsf", delete=False) as tmp:
            tmp.write(raw)
            tmp_path = Path(tmp.name)
        try:
            lsf = LSFIndex(tmp_path)
            lsf.build()
        finally:
            tmp_path.unlink(missing_ok=True)
        for node in lsf.nodes:
            attrs = node.get("attrs", {})
            guid = _val(attrs.get("MapKey"))
            if not guid:
                continue
            entry = by_guid.setdefault(guid, {"name_handle": "", "parent": None, "stats": None})
            if not entry["name_handle"] and "DisplayName" in attrs:
                entry["name_handle"] = _handle(attrs["DisplayName"])
            if entry["parent"] is None:
                entry["parent"] = _val(attrs.get("ParentTemplateId"))
            if entry["stats"] is None:
                entry["stats"] = _val(attrs.get("Stats"))
    return by_guid


def build_stat_names(by_guid, loca):
    def name_for(guid, depth=0):
        entry = by_guid.get(guid)
        if not entry or depth > 12:
            return ""
        handle = entry["name_handle"]
        if handle:
            text = loca.get(handle, "")
            if text and not text.startswith("%%%"):
                return text
        if entry["parent"]:
            return name_for(entry["parent"], depth + 1)
        return ""

    stat_name = {}
    for guid, entry in by_guid.items():
        stat = entry["stats"]
        if stat and stat not in stat_name:
            name = name_for(guid)
            if name:
                stat_name[stat] = name
    return stat_name


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--game-data", default=str(DEFAULT_GAME_DATA), help="BG3 .../Contents/Data dir")
    ap.add_argument("--out", default=str(ROOT / "tools/item-names/item_names.json"))
    args = ap.parse_args()

    data_dir = Path(args.game_data)
    english = data_dir / "Localization/English.pak"
    if not english.exists():
        raise SystemExit(f"game file not found: {english}\nPass --game-data with your BG3 Data dir.")

    ef, eidx = lspk_index(english)
    loca = parse_loca(lspk_read(ef, eidx, LOCA_NAME))
    by_guid = collect_templates(data_dir)
    stat_name = build_stat_names(by_guid, loca)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"stat_name": stat_name}, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}: {len(stat_name)} item names from {len(by_guid)} templates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
