#!/usr/bin/env python3
"""Build a personal quest journal (journal.md) from an indexed save.

Reads the JSONL produced by `index_lsf.py` (default
`tools/save-index/globals.jsonl`) and writes a readable diary of open and
completed quests, each with its step trail. `journal.md` is committed to the
(public) repo by choice; it is spoiler-heavy — it holds the save's full story
progress. Regenerate it after syncing a newer save.

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
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Region/prefix → human label, roughly in play order.
REGIONS = [
    ("TUT", "Prologue — Nautiloid"),
    ("INT", "Prologue — Interlude"),
    ("SYS", "System"),
    ("CHA", "Act 1 — Recruitment & Chapel"),
    ("DEN", "Act 1 — Grove & Goblins"),
    ("HAG", "Act 1 — Swamp / Hag"),
    ("UND", "Act 1 — Underdark"),
    ("FOR", "Act 1 — Grymforge"),
    ("CRE", "Act 1 — Githyanki Crèche"),
    ("COL", "Act 2 — Shadow-Cursed Lands"),
    ("SHA", "Act 2 — Shar questline"),
    ("MOO", "Act 2 — Moonrise Towers"),
    ("WYR", "Act 3 — Rivington / Wyrm's Crossing"),
    ("LOW", "Act 3 — Lower City"),
    ("SCL", "Act 3 — Upper City"),
    ("CTY", "Act 3 — City"),
    ("PLA", "Act 3 — City (misc)"),
    ("WLD", "Other — Wilderness"),
    ("GLO", "Main quest (cross-act)"),
    ("ORI", "Companion questlines"),
    ("HIDDEN", "Hidden objectives"),
]


# Prefixes stripped when turning an internal id into a readable title
# (longest / compound first).
STRIP_PREFIXES = [
    "ORI_COM", "ORI_Avatar", "HIDDEN",
    "TUT", "INT", "SYS", "CHA", "DEN", "HAG", "UND", "FOR", "CRE",
    "COL", "SHA", "MOO", "WYR", "LOW", "SCL", "CTY", "PLA", "WLD", "GLO",
]

_WORD_RE = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z][a-z]+|[A-Z]+|[a-z]+|\d+")


def humanize(token: str) -> str:
    """Split a CamelCase / snake_case token into spaced words."""
    words = []
    for part in token.split("_"):
        words += _WORD_RE.findall(part)
    return " ".join(words) or token


def humanize_quest(qid: str) -> str:
    """Readable English title derived from an internal quest/objective id.

    Heuristic (not the verbatim in-game journal text): strips the region
    prefix and the _COMPLETION marker, then spaces out the remaining
    CamelCase/underscore groups.
    """
    s = re.sub(r"_COMPLETION$", "", qid)
    for p in STRIP_PREFIXES:
        if s == p:
            s = ""
            break
        if s.startswith(p + "_"):
            s = s[len(p) + 1:]
            break
    s = s.replace("_SUB_", "_")
    parts = [humanize(g) for g in s.split("_") if g]
    parts = [p for p in parts if p]
    return " — ".join(parts) if parts else qid


def region_label(qid: str) -> str:
    for prefix, label in REGIONS:
        if qid.startswith(prefix):
            return label
    return "Other"


def load_quest_text():
    """Optional real in-game text cache (see tools/extract_journal_text.py).

    Returns (mapping, sorted_ids) or ({}, []) when the local cache is absent —
    e.g. in CI, where the published journal falls back to readable ids.
    """
    path = ROOT / "tools/journal-text/quest_text.json"
    if not path.exists():
        return {}, []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data, sorted(data.keys(), key=len, reverse=True)


def resolve_quest_id(save_id, objective, known_ids):
    """Map a save's quest id/objective to a base QuestID from the text cache."""
    for candidate in (save_id, objective):
        if not candidate:
            continue
        for qid in known_ids:
            if candidate == qid or candidate.startswith(qid + "_"):
                return qid
    return None


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


def render(quests, meta, quest_text, known_ids):
    open_q = sorted(
        (q for q in quests if not q["completed"]),
        key=lambda q: (region_order(q["id"]), q["id"]),
    )
    done_q = sorted(
        (q for q in quests if q["completed"]),
        key=lambda q: (region_order(q["id"]), q["id"]),
    )
    real = bool(quest_text)

    lines = [
        "# Quest Journal",
        "",
        "> ⚠️ **Spoiler:** contains this save's full story progress.",
        "> Auto-generated from the savegame; do not edit by hand (rebuild with `tools/build_journal.py`).",
        "",
        f"- **Save:** {meta.get('save','?')}",
        f"- **Game time (internal):** {meta.get('gametime','?')}",
        f"- **Open / in progress:** {len(open_q)}  ·  **Completed:** {len(done_q)}",
        (
            "- **Text:** real in-game journal entries"
            if real
            else "- **Text:** readable titles derived from internal ids"
        ),
        "",
    ]

    def esc(s):
        return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def block(title, items):
        # Each quest is a collapsed <details> so the long list stays scannable;
        # raw HTML renders on the site, on GitHub, and in Obsidian alike.
        out = [f"## {title}", ""]
        cur_region = None
        for q in items:
            reg = region_label(q["id"])
            if reg != cur_region:
                out += [f"### {reg}", ""]
                cur_region = reg

            base = resolve_quest_id(q["id"], q["objective"], known_ids) if real else None
            qt = quest_text.get(base) if base else None

            quest_title = (qt and qt.get("title")) or humanize_quest(q["id"])
            step_texts = (qt or {}).get("steps", {})

            detail = []
            if q["steps"]:
                if qt:
                    # Real journal entries, in the order the player unlocked them.
                    for s in q["steps"]:
                        entry = step_texts.get(s) or humanize(s)
                        detail.append(f"<li>{esc(entry)}</li>")
                else:
                    trail = " → ".join(esc(humanize(s)) for s in q["steps"])
                    detail.append(f'<li>Trail: <span class="q-trail">{trail}</span></li>')
            detail.append(f'<li class="q-raw">ID: <code>{esc(q["id"])}</code></li>')

            count = f"{len(q['steps'])} step{'s' if len(q['steps']) != 1 else ''}"
            out.append(
                f'<details class="quest-entry"><summary><span class="q-title">{esc(quest_title)}</span>'
                f'<span class="q-count">{count}</span></summary>'
            )
            out.append("<ul>")
            out += detail
            out.append("</ul>")
            out.append("</details>")
            out.append("")
        return out

    lines += block("🟡 Open / in-progress quests", open_q)
    lines += block("✅ Completed quests", done_q)
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
        folder = m.get("source_save", {}).get("folder", "?")
        # Save folders are "<ProfileName>-<id>__<SaveName>"; keep only the save
        # name so the player's profile (a real name) never lands in the repo.
        meta["save"] = folder.split("__", 1)[1] if "__" in folder else folder
    for r in recs:
        if r["name"] == "Journal":
            meta["gametime"] = val(r, "CurrentGameTime")
            break

    quests = build(recs)
    quest_text, known_ids = load_quest_text()
    n_open = sum(1 for q in quests if not q["completed"])
    n_done = sum(1 for q in quests if q["completed"])

    # Public output: readable titles derived from ids — always safe to publish.
    out = Path(args.out)
    out.write_text(render(quests, meta, {}, []), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}: {n_open} open, {n_done} completed [readable ids].")

    # Local output: real in-game journal text (Larian copyright) — gitignored,
    # only written when the text cache is present.
    if quest_text:
        local = ROOT / "journal.local.md"
        local.write_text(render(quests, meta, quest_text, known_ids), encoding="utf-8")
        print(f"Wrote {local.relative_to(ROOT)}: real in-game text (local only, gitignored).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
