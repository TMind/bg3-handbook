#!/usr/bin/env python3
"""Download YouTube metadata and subtitles for handbook source review.

This script intentionally skips the video file. It only stores metadata and
available subtitles so a guide source can be reviewed without keeping media.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Download YouTube subtitles for source review.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--lang",
        default="en",
        help="Subtitle language code or comma-separated list. Default: en",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tools/video-transcripts"),
        help="Folder for metadata and subtitle files.",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(args.output_dir / "%(id)s.%(ext)s")
    before = set(args.output_dir.glob("*.info.json"))

    run(
        [
            "yt-dlp",
            "--write-info-json",
            "--write-auto-subs",
            "--write-subs",
            "--sub-langs",
            args.lang,
            "--skip-download",
            "--output",
            output_template,
            args.url,
        ]
    )

    after = set(args.output_dir.glob("*.info.json"))
    new_metadata = sorted(after - before, key=lambda path: path.stat().st_mtime, reverse=True)
    metadata_path = new_metadata[0] if new_metadata else None

    if metadata_path and metadata_path.exists():
        info = json.loads(metadata_path.read_text(encoding="utf-8"))
        title = info.get("title", "(unknown title)")
        channel = info.get("channel") or info.get("uploader") or "(unknown channel)"
        print(f"Saved source: {title} - {channel}")
    else:
        print(f"Saved files to {args.output_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
