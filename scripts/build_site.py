#!/usr/bin/env python3
"""Build a single self-contained HTML site from the handbook vault.

Reads `README.md` and every `docs/*.md`, embeds them (base64) into
`scripts/site_template.html`, and writes `site/index.html` — one portable
file with a chapter sidebar and working internal links. No network, no build
step for the reader: open the file or host it anywhere static.

Usage:
    python3 scripts/build_site.py            # build site/index.html
    python3 scripts/build_site.py --check    # fail if site/index.html is stale
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TEMPLATE = ROOT / "scripts" / "site_template.html"
OUTPUT = ROOT / "site" / "index.html"
PLACEHOLDER = "__DOC_DATA__"


def source_files() -> list[Path]:
    """Vault pages to publish, in a stable order (README, docs, then extras)."""
    pages = [ROOT / "README.md", *sorted(DOCS.glob("*.md"))]
    for extra in ("journal.md", "chronicle.md"):  # root-level narrative pages
        path = ROOT / extra
        if path.exists():
            pages.append(path)
    return pages


def collect_doc_data() -> dict[str, str]:
    """Map each page's repo-relative path to its base64-encoded UTF-8 text."""
    data: dict[str, str] = {}
    for path in source_files():
        rel = path.relative_to(ROOT).as_posix()
        raw = path.read_text(encoding="utf-8").encode("utf-8")
        data[rel] = base64.b64encode(raw).decode("ascii")
    return data


def render_html() -> str:
    template = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        raise SystemExit(f"template is missing {PLACEHOLDER}: {TEMPLATE}")
    payload = json.dumps(collect_doc_data(), ensure_ascii=False)
    return template.replace(PLACEHOLDER, payload, 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify site/index.html is up to date instead of writing it",
    )
    args = parser.parse_args()

    html = render_html()

    if args.check:
        if not OUTPUT.exists():
            print(f"{OUTPUT.relative_to(ROOT)} does not exist; run build_site.py")
            return 1
        if OUTPUT.read_text(encoding="utf-8") != html:
            print(f"{OUTPUT.relative_to(ROOT)} is stale; run build_site.py")
            return 1
        print(f"{OUTPUT.relative_to(ROOT)} is up to date.")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    pages = len(collect_doc_data())
    print(f"Built {OUTPUT.relative_to(ROOT)} from {pages} pages ({len(html):,} bytes).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
