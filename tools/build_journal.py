#!/usr/bin/env python3
"""Build a personal quest journal (journal.md) from an indexed save.

Reads the JSONL produced by `index_lsf.py` (default
`tools/save-index/globals.jsonl`) and writes a readable diary of open and
completed quests, each with its step trail. The output is spoiler-heavy by
nature, so `journal.md` is gitignored and never published — this script is
not; it contains no save content.

Prereq: sync + index a save first, e.g.
    python3 tools/sync_latest_save.py
    PYTHONPATH=/private/tmp/bg3-py-libs python3 tools/index_lsf.py \
        tools/save-extract/Globals.lsf --jsonl tools/save-index/globals.jsonl

Usage:
    python3 tools/build_journal.py [--jsonl PATH] [--out PATH]
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Region/prefix → human label, roughly in play order.
REGIONS = [
    ("TUT", "Prolog — Nautiloid"),
    ("INT", "Prolog — Zwischenspiel"),
    ("SYS", "System"),
    ("CHA", "Akt 1 — Rekrutierung & Kapelle"),
    ("DEN", "Akt 1 — Hain & Goblins"),
    ("HAG", "Akt 1 — Sumpf / Hexe"),
    ("UND", "Akt 1 — Unterreich"),
    ("FOR", "Akt 1 — Grymschmiede"),
    ("CRE", "Akt 1 — Githyanki-Crèche"),
    ("COL", "Akt 2 — Schattenland"),
    ("SHA", "Akt 2 — Shar-Questreihe"),
    ("MOO", "Akt 2 — Mondtürme"),
    ("WYR", "Akt 3 — Rivington / Wyrm's Crossing"),
    ("LOW", "Akt 3 — Untere Stadt"),
    ("SCL", "Akt 3 — Obere Stadt"),
    ("CTY", "Akt 3 — Stadt"),
    ("PLA", "Akt 3 — Stadt (Verschiedenes)"),
    ("WLD", "Sonstiges — Wildnis"),
    ("GLO", "Hauptquest (übergreifend)"),
    ("ORI", "Begleiter-Questreihen"),
    ("HIDDEN", "Versteckte Ziele"),
]


def region_label(qid: str) -> str:
    for prefix, label in REGIONS:
        if qid.startswith(prefix):
            return label
    return "Sonstiges"


def region_order(qid: str) -> int:
    for i, (prefix, _) in enumerate(REGIONS):
        if qid.startswith(prefix):
            return i
    return len(REGIONS)


def load(jsonl: Path):
    recs = []
    with jsonl.open(encoding="utf-8") as fh:
        for line in fh:
            recs.append(json.loads(line))
    return recs


def val(rec, key):
    a = rec.get("attrs", {}).get(key)
    return a.get("value") if isinstance(a, dict) else None


def build(recs):
    children = defaultdict(list)
    for r in recs:
        children[r["parent"]].append(r)

    # quest id -> category
    cat = {}
    for r in recs:
        if r["name"] == "QuestCategory":
            cat[val(r, "QuestID")] = val(r, "CategoryID")
    qids = sorted(cat.keys(), key=len, reverse=True)

    def match_cat(objective):
        for q in qids:
            if objective and objective.startswith(q):
                return cat[q], q
        return None, objective

    quests = []
    for r in recs:
        if r["name"] != "Quest":
            continue
        objective = val(r, "ObjectiveID") or ""
        category, qid = match_cat(objective)
        steps = [
            val(c, "QuestUnlockedSteps")
            for c in children[r["idx"]]
            if c["name"] == "QuestUnlockedSteps"
        ]
        quests.append(
            {
                "id": qid or objective,
                "objective": objective,
                "completed": category == "CompletedQuests",
                "disabled": bool(val(r, "QuestDisabled")),
                "steps": [s for s in steps if s],
            }
        )
    # de-duplicate by id (keep the one with most steps)
    best = {}
    for q in quests:
        cur = best.get(q["id"])
        if cur is None or len(q["steps"]) > len(cur["steps"]):
            best[q["id"]] = q
    return list(best.values())


def render(quests, meta):
    open_q = sorted(
        (q for q in quests if not q["completed"]),
        key=lambda q: (region_order(q["id"]), q["id"]),
    )
    done_q = sorted(
        (q for q in quests if q["completed"]),
        key=lambda q: (region_order(q["id"]), q["id"]),
    )

    lines = [
        "# Quest-Tagebuch",
        "",
        "> ⚠️ Lokale, spoilerhaltige Datei — bewusst **gitignored**, wird nicht veröffentlicht.",
        "> Automatisch erzeugt aus dem Savegame; nicht von Hand editieren (mit `tools/build_journal.py` neu bauen).",
        "",
        f"- **Save:** {meta.get('save','?')}",
        f"- **Spielzeit (intern):** {meta.get('gametime','?')}",
        f"- **Offen/in Arbeit:** {len(open_q)}  ·  **Abgeschlossen:** {len(done_q)}",
        "",
    ]

    def block(title, items):
        out = [f"## {title}", ""]
        cur_region = None
        for q in items:
            reg = region_label(q["id"])
            if reg != cur_region:
                out += [f"### {reg}", ""]
                cur_region = reg
            out.append(f"- **{q['id']}**")
            if not q["completed"] and q["objective"]:
                out.append(f"  - Aktuelles Ziel: `{q['objective']}`")
            if q["steps"]:
                out.append("  - Verlauf: " + " → ".join(f"`{s}`" for s in q["steps"]))
            out.append("")
        return out

    lines += block("🟡 Offene / laufende Quests", open_q)
    lines += block("✅ Abgeschlossene Quests", done_q)
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--jsonl", default=str(ROOT / "tools/save-index/globals.jsonl"))
    ap.add_argument("--out", default=str(ROOT / "journal.md"))
    args = ap.parse_args()

    jsonl = Path(args.jsonl)
    if not jsonl.exists():
        raise SystemExit(f"index not found: {jsonl}\nRun index_lsf.py first (see module docstring).")

    recs = load(jsonl)
    # save meta, if the manifest is available
    meta = {}
    manifest = ROOT / "tools/save-extract/source_manifest.json"
    if manifest.exists():
        m = json.loads(manifest.read_text())
        meta["save"] = m.get("source_save", {}).get("folder", "?")
    for r in recs:
        if r["name"] == "Journal":
            meta["gametime"] = val(r, "CurrentGameTime")
            break

    quests = build(recs)
    out = Path(args.out)
    out.write_text(render(quests, meta), encoding="utf-8")
    n_open = sum(1 for q in quests if not q["completed"])
    n_done = sum(1 for q in quests if q["completed"])
    print(f"Wrote {out.relative_to(ROOT)}: {n_open} open, {n_done} completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
