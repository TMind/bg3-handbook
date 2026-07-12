#!/usr/bin/env python3
"""Validate BG3 handbook Markdown conventions."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SPOILER_TERMS = [
    "Iron Throne",
    "Arcane Tower",
    "Guiding Light",
    "Staff of Arcane",
    "Cazador",
    "Raphael",
    "Orin",
    "Gortash",
    "Netherbrain",
    "Myrkul",
    "Ketheric",
    "Viconia",
    "Sarevok",
    "Ansur",
    "Mystic Carrion",
    "Balthazar",
    "Yurgir",
    "Houndmaster",
    "Victoria",
    "Steel Watch",
    "Mizora",
    "Owlbear",
    "Florrick",
    "Harpers",
    "Gur Hunters",
    "Nightbringer",
    "Final Battle",
    "final battle",
    "Armored Owlbear",
]


def markdown_files() -> list[Path]:
    return [ROOT / "README.md", *sorted(DOCS.glob("*.md"))]


def unescaped_pipe_count(row: str) -> int:
    count = 0
    escaped = False
    for char in row:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "|":
            count += 1
    return count


def table_row_text(line: str) -> str | None:
    stripped = line.lstrip()
    if stripped.startswith("> |"):
        return stripped[2:]
    if stripped.startswith("|"):
        return stripped
    return None


def split_wikilink(link_body: str) -> tuple[str, str | None]:
    escaped_alias = link_body.find("\\|")
    plain_alias = link_body.find("|")
    candidates = [index for index in (escaped_alias, plain_alias) if index != -1]
    if candidates:
        index = min(candidates)
        separator_length = 2 if index == escaped_alias else 1
        return link_body[:index], link_body[index + separator_length :]
    return link_body, None


def collect_targets() -> tuple[
    dict[str, Path], dict[str, set[str]], dict[str, set[str]]
]:
    files = {path.stem: path for path in markdown_files()}
    files["README"] = ROOT / "README.md"
    blocks: dict[str, set[str]] = {}
    headings: dict[str, set[str]] = {}
    for stem, path in files.items():
        text = path.read_text(encoding="utf-8")
        blocks[stem] = set(re.findall(r"\^([A-Za-z0-9_-]+)", text))
        headings[stem] = set()
        for match in re.finditer(r"^#{1,6}\s+(.+)$", text, flags=re.MULTILINE):
            heading = re.sub(r"\s+\^[A-Za-z0-9_-]+\s*$", "", match.group(1)).strip()
            headings[stem].add(heading)
    return files, blocks, headings


def check_tables(path: Path, lines: list[str]) -> list[str]:
    errors: list[str] = []
    index = 0
    while index < len(lines):
        row = table_row_text(lines[index])
        if row is None:
            index += 1
            continue
        start = index + 1
        counts: list[int] = []
        while index < len(lines):
            row = table_row_text(lines[index])
            if row is None:
                break
            counts.append(unescaped_pipe_count(row))
            if re.search(r"\[\[[^\]]*(?<!\\)\|[^\]]*\]\]", row):
                errors.append(f"{path}:{index + 1}: unescaped Wikilink pipe in table")
            index += 1
        if len(set(counts)) > 1:
            errors.append(f"{path}:{start}: inconsistent table pipe counts {counts}")
    return errors


def check_markers(path: Path, lines: list[str]) -> list[str]:
    errors: list[str] = []
    for number, line in enumerate(lines, start=1):
        if "⭐⭐⭐⭐" in line or re.search(r"\*\*Markers:\*\*.*⭐.*⭐.*⭐.*⭐", line):
            errors.append(f"{path}:{number}: marker priority exceeds ⭐⭐⭐")
    return errors


def check_wikilink_targets(
    path: Path,
    lines: list[str],
    files: dict[str, Path],
    blocks: dict[str, set[str]],
    headings: dict[str, set[str]],
) -> list[str]:
    errors: list[str] = []
    for number, line in enumerate(lines, start=1):
        for match in re.finditer(r"\[\[([^\]]+)\]\]", line):
            target_part, _display = split_wikilink(match.group(1))
            target_part = target_part.replace("\\|", "|")
            if "#^" in target_part:
                file_part, block_id = target_part.split("#^", 1)
                heading = None
            elif "#" in target_part:
                file_part, heading = target_part.split("#", 1)
                block_id = None
            else:
                file_part, block_id, heading = target_part, None, None
            file_part = file_part.strip()
            block_id = block_id.strip() if block_id else None
            heading = heading.strip() if heading else None
            if not file_part and (heading or block_id):
                file_part = path.stem
            elif not file_part:
                continue
            if file_part not in files:
                errors.append(f"{path}:{number}: missing Wikilink target file: {match.group(0)}")
                continue
            if block_id and block_id not in blocks.get(file_part, set()):
                errors.append(f"{path}:{number}: missing Wikilink block id: {match.group(0)}")
            if heading and heading not in headings.get(file_part, set()):
                errors.append(f"{path}:{number}: missing Wikilink heading: {match.group(0)}")
    return errors


def check_visible_spoilers(path: Path, lines: list[str]) -> list[str]:
    errors: list[str] = []
    in_comment = False
    for number, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        if "<!--" in stripped:
            in_comment = True
        visible = not in_comment and not stripped.startswith(">")
        if visible:
            for term in SPOILER_TERMS:
                if term in line:
                    errors.append(f"{path}:{number}: visible spoiler-prone term: {term}")
        if "-->" in stripped:
            in_comment = False
    return errors


def main() -> int:
    files, blocks, headings = collect_targets()
    errors: list[str] = []
    for path in markdown_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        errors.extend(check_tables(path, lines))
        errors.extend(check_markers(path, lines))
        errors.extend(check_wikilink_targets(path, lines, files, blocks, headings))
        errors.extend(check_visible_spoilers(path, lines))
    if errors:
        for error in errors:
            print(error)
        print(f"\n{len(errors)} issue(s) found.")
        return 1
    print("Vault checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
