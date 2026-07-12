#!/usr/bin/env python3
"""Mirror and extract the newest BG3 save from the local game save folder.

This tool is read-only against the game save directory. It copies the chosen
.lsv into this handbook workspace, extracts it, and writes a small manifest so
later audits know exactly which save they used.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
DEFAULT_CURRENT_SAVE = TOOLS / "current-save" / "latest.lsv"
DEFAULT_EXTRACT_DIR = TOOLS / "save-extract"
DEFAULT_LIB_DIR = Path("/private/tmp/bg3-py-libs")


def add_dependency_path() -> None:
    if DEFAULT_LIB_DIR.exists():
        sys.path.insert(0, str(DEFAULT_LIB_DIR))
    sys.path.insert(0, str(TOOLS))


def default_source_roots() -> list[Path]:
    home = Path.home()
    return [
        *(
            Path(path)
            for path in home.glob(
                "Library/Application Support/Steam/userdata/*/1086940/remote/_SAVE_Public/Savegames/Story"
            )
        ),
        home / "Documents/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/Savegames/Story",
        home
        / "Library/Application Support/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/Savegames/Story",
    ]


def find_saves(source_roots: list[Path], name_filter: str | None = None) -> list[Path]:
    saves: list[Path] = []
    seen: set[Path] = set()
    for root in source_roots:
        expanded = Path(os.path.expanduser(str(root)))
        if not expanded.exists():
            continue
        for save in expanded.glob("*/*.lsv"):
            resolved = save.resolve()
            if resolved in seen:
                continue
            if name_filter and name_filter.casefold() not in str(save).casefold():
                continue
            seen.add(resolved)
            saves.append(save)
    return sorted(saves, key=lambda path: path.stat().st_mtime, reverse=True)


def save_summary(path: Path) -> dict:
    stat = path.stat()
    return {
        "path": str(path),
        "folder": path.parent.name,
        "file": path.name,
        "size_bytes": stat.st_size,
        "modified_local": datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(timespec="seconds"),
        "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(timespec="seconds"),
    }


def copy_save(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def extract_save(source: Path, destination: Path) -> int:
    add_dependency_path()
    try:
        from extract_lsv import extract_lsv
    except ImportError as exc:
        raise SystemExit(
            "Missing extractor dependencies. Run:\n"
            "  python3 -m pip install --target /private/tmp/bg3-py-libs -r tools/requirements-save-tools.txt"
        ) from exc
    extracted = extract_lsv(source, destination, overwrite=True)
    return len(extracted)


def write_manifest(source: Path, mirrored: Path, extract_dir: Path, extracted_count: int | None) -> None:
    manifest = {
        "synced_at_local": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source_save": save_summary(source),
        "mirrored_save": str(mirrored),
        "extract_dir": str(extract_dir),
        "extracted_file_count": extracted_count,
        "workflow_note": "Run the LSLib/Divine convert-resource step from tools/SAVEGAME_WORKFLOW.md if Globals.lsx needs to be refreshed from Globals.lsf.",
    }
    extract_dir.mkdir(parents=True, exist_ok=True)
    (extract_dir / "source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync the newest local BG3 .lsv save into the handbook tools folder.")
    parser.add_argument("--source-root", action="append", type=Path, help="Savegames/Story folder to scan.")
    parser.add_argument("--name-filter", help="Only consider saves whose path contains this text.")
    parser.add_argument("--list", type=int, default=0, metavar="N", help="List the newest N matching saves and exit.")
    parser.add_argument("--index", type=int, default=0, help="Use save at this zero-based index after sorting by mtime.")
    parser.add_argument("--copy-to", type=Path, default=DEFAULT_CURRENT_SAVE, help="Where to mirror the chosen .lsv.")
    parser.add_argument("--extract-to", type=Path, default=DEFAULT_EXTRACT_DIR, help="Where to extract the mirrored save.")
    parser.add_argument("--no-extract", action="store_true", help="Only copy the save and write a manifest.")
    args = parser.parse_args()

    source_roots = args.source_root if args.source_root else default_source_roots()
    saves = find_saves(source_roots, args.name_filter)
    if not saves:
        print("No matching .lsv saves found.", file=sys.stderr)
        return 2

    if args.list:
        for index, save in enumerate(saves[: args.list]):
            summary = save_summary(save)
            print(f"{index:>2}  {summary['modified_local']}  {summary['folder']}  {summary['file']}")
            print(f"    {summary['path']}")
        return 0

    if args.index < 0 or args.index >= len(saves):
        print(f"Invalid --index {args.index}; found {len(saves)} matching saves.", file=sys.stderr)
        return 2

    source = saves[args.index]
    copy_save(source, args.copy_to)
    extracted_count: int | None = None
    if not args.no_extract:
        extracted_count = extract_save(args.copy_to, args.extract_to)
    write_manifest(source, args.copy_to, args.extract_to, extracted_count)

    summary = save_summary(source)
    print(f"Synced save: {summary['folder']} / {summary['file']}")
    print(f"Source: {source}")
    print(f"Mirrored: {args.copy_to}")
    if extracted_count is not None:
        print(f"Extracted {extracted_count} files to {args.extract_to}")
    print(f"Manifest: {args.extract_to / 'source_manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
