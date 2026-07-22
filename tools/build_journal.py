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

    Returns the mapping, or {} when the local cache is absent — e.g. in CI,
    where the published journal falls back to readable ids.
    """
    path = ROOT / "tools/journal-text/quest_text.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_by_steps(steps, objective, quest_text):
    """Pick the prototype QuestID that owns these unlocked steps.

    The save's ObjectiveID does not reliably prefix a prototype QuestID, so
    match on step-id membership (the reliable key) and use the objective's
    prefix only to break ties.
    """
    best, best_score = None, 0
    for qid, q in quest_text.items():
        proto_steps = q.get("steps", {})
        score = sum(1 for s in steps if s in proto_steps)
        if score > best_score or (
            score == best_score and score > 0 and best and objective.startswith(qid)
            and not objective.startswith(best)
        ):
            best, best_score = qid, score
    return best if best_score > 0 else None


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
        # Skip the first-person origin ("Avatar") companion tracks; for a custom
        # player character the party-perspective ORI_COM tracks are the correct
        # ones, and keeping both mixes "I..." and "we..." in the same quest.
        if objective.startswith("ORI_Avatar"):
            continue
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


def merge(quests, quest_text):
    """Turn raw save quest nodes into render-ready units.

    Without the text cache, each node passes through as a fallback unit. With
    it, nodes are resolved to their prototype quest and grouped by display
    title, so a quest that appears as several save nodes becomes a single entry.

    A companion quest exists twice in the save: the `ORI_COM_*` track, written
    from the party's perspective ("we..."), and the `ORI_Avatar_*` track,
    written first-person ("I...") for when that companion is the player's origin
    character. For a custom player character only the `ORI_COM_*` "we" track is
    correct, so within a title group we keep the non-Avatar contributions and
    drop the first-person ones (falling back to Avatar only if it is the sole
    source). Entries are collected in unlock order and de-duplicated by text.
    A merged quest is "completed" only if every contributing node was.
    """
    if not quest_text:
        return [
            {"id": q["id"], "completed": q["completed"], "steps": q["steps"], "real": False}
            for q in quests
        ]
    groups = {}
    order = []
    passthrough = []
    for q in quests:
        base = resolve_by_steps(q["steps"], q["objective"], quest_text)
        if not base:
            passthrough.append(
                {"id": q["id"], "completed": q["completed"], "steps": q["steps"], "real": False}
            )
            continue
        proto = quest_text[base]
        title = (proto.get("title") or "").strip()
        key = title if title and not title.startswith("%%%") else base
        g = groups.get(key)
        if g is None:
            g = groups[key] = {"title": proto.get("title"), "completed": True, "contribs": []}
            order.append(g)
        entries = [proto["steps"][s] for s in q["steps"] if proto["steps"].get(s)]
        g["contribs"].append({"base": base, "entries": entries})
        if not q["completed"]:
            g["completed"] = False

    result = []
    for g in order:
        preferred = [c for c in g["contribs"] if not c["base"].startswith("ORI_Avatar")]
        use = preferred or g["contribs"]
        entries, seen = [], set()
        for c in use:
            for e in c["entries"]:
                if e not in seen:
                    seen.add(e)
                    entries.append(e)
        result.append({
            "id": use[0]["base"], "title": g["title"],
            "completed": g["completed"], "entries": entries, "real": True,
        })
    return result + passthrough


def render(quests, meta, quest_text):
    real = bool(quest_text)
    quests = merge(quests, quest_text)
    open_q = sorted(
        (q for q in quests if not q["completed"]),
        key=lambda q: (region_order(q["id"]), q["id"]),
    )
    done_q = sorted(
        (q for q in quests if q["completed"]),
        key=lambda q: (region_order(q["id"]), q["id"]),
    )

    lines = [
        "# Quest Journal",
        "",
        "> ⚠️ **Spoiler:** contains this save's full story progress.",
        "> Auto-generated from the savegame; do not edit by hand (rebuild with `tools/build_journal.py`).",
    ]
    if real:
        lines.append(
            "> Quest and journal text © Larian Studios, from *Baldur's Gate 3* — "
            "reproduced here for personal reference."
        )
    lines += [
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

    def clean_title(raw, rid):
        # Some prototype titles are untranslated placeholders (e.g. "%%% EMPTY").
        if not raw or raw.strip().startswith("%%%"):
            return humanize_quest(rid)
        return raw

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

            detail = []
            if q["real"]:
                for entry in q["entries"]:
                    detail.append(f"<li>{esc(entry)}</li>")
                shown = len(q["entries"])
                count = f"{shown} " + ("entry" if shown == 1 else "entries")
                quest_title = clean_title(q["title"], q["id"])
            else:
                if q["steps"]:
                    trail = " → ".join(esc(humanize(s)) for s in q["steps"])
                    detail.append(f'<li>Trail: <span class="q-trail">{trail}</span></li>')
                shown = len(q["steps"])
                count = f"{shown} " + ("step" if shown == 1 else "steps")
                quest_title = humanize_quest(q["id"])
            detail.append(f'<li class="q-raw">ID: <code>{esc(q["id"])}</code></li>')

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
    quest_text = load_quest_text()

    # Use the real in-game journal text when the local cache is present
    # (see tools/extract_journal_text.py); otherwise fall back to readable
    # titles derived from the ids — so CI, which has no game files, still builds.
    units = merge(quests, quest_text)
    n_open = sum(1 for q in units if not q["completed"])
    n_done = sum(1 for q in units if q["completed"])
    out = Path(args.out)
    out.write_text(render(quests, meta, quest_text), encoding="utf-8")
    mode = "real in-game text" if quest_text else "readable ids (no text cache)"
    print(f"Wrote {out.relative_to(ROOT)}: {n_open} open, {n_done} completed [{mode}].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
