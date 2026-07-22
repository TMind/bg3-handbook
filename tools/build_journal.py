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

    Match on step-id membership (the reliable key). Step ids are not unique
    across quests (e.g. `GroveChanged` exists in five grove quests, and the
    COM/Avatar companion tracks share most step ids), so on a score tie prefer
    the prototype whose id prefixes the node's ObjectiveID — that is the quest
    this save node actually belongs to.
    """
    scored = {}
    for qid, q in quest_text.items():
        score = sum(1 for s in steps if s in q.get("steps", {}))
        if score > 0:
            scored[qid] = score
    if not scored:
        return None
    top = max(scored.values())
    tied = [qid for qid, sc in scored.items() if sc == top]
    if len(tied) > 1:
        for qid in sorted(tied, key=len, reverse=True):
            if objective and objective.startswith(qid):
                return qid
    return tied[0]


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


# Keyed by lowercased id token so ORI_COM_Shadowheart and ORI_Avatar_ShadowHeart
# normalize to one character.
_COMPANION_NAMES = {
    "laezel": "Lae'zel", "shadowheart": "Shadowheart", "astarion": "Astarion",
    "gale": "Gale", "wyll": "Wyll", "karlach": "Karlach", "halsin": "Halsin",
    "minthara": "Minthara", "jaheira": "Jaheira", "minsc": "Minsc",
}


def companion_of(qid):
    """(character, form) for an ORI companion quest, else (None, None).

    form is 'party' for the ORI_COM_* track (told as "we...") and 'origin' for
    the first-person ORI_Avatar_* track (told as "I...").
    """
    m = re.match(r"ORI_(COM|Avatar)_([A-Za-z]+)", qid or "")
    if not m:
        return None, None
    token = m.group(2)
    char = _COMPANION_NAMES.get(token.lower(), token)
    return char, ("party" if m.group(1) == "COM" else "origin")


def merge(quests, quest_text):
    """Turn raw save quest nodes into render-ready units.

    Without the text cache, each node passes through as a fallback unit. With
    it, nodes are resolved to their prototype quest and grouped by prototype id,
    so several save nodes of one quest (e.g. one node per objective) become a
    single entry, while distinct quests stay separate.

    A companion quest exists twice: the `ORI_COM_*` party-perspective track
    ("we...") and the first-person `ORI_Avatar_*` origin track ("I..."). These
    have different ids, so they are kept as separate units and tagged with their
    character and form; the renderer groups them under the companion's name.
    Entries are collected in unlock order and de-duplicated by text. A merged
    quest is "completed" only if every contributing node was.
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
        g = groups.get(base)
        if g is None:
            g = groups[base] = {
                "id": base, "title": quest_text[base].get("title"),
                "completed": True, "entries": [], "_seen": set(), "real": True,
            }
            order.append(g)
        for s in q["steps"]:
            txt = quest_text[base]["steps"].get(s)
            if txt and txt not in g["_seen"]:
                g["_seen"].add(txt)
                g["entries"].append(txt)
        if not q["completed"]:
            g["completed"] = False

    for g in order:
        g.pop("_seen", None)
        g["character"], g["form"] = companion_of(g["id"])
    return order + passthrough


COMPANION_REGION = "Companion questlines"
FORM_LABEL = {"party": "party view", "origin": "origin view"}


def render(quests, meta, quest_text):
    real = bool(quest_text)
    quests = merge(quests, quest_text)

    def sort_key(q):
        # Within the companion region, cluster by character and put the
        # party-perspective ("we") track before the first-person origin track.
        return (
            region_order(q["id"]),
            q.get("character") or "",
            0 if q.get("form") == "party" else 1,
            q["id"],
        )

    open_q = sorted((q for q in quests if not q["completed"]), key=sort_key)
    done_q = sorted((q for q in quests if q["completed"]), key=sort_key)

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
        cur_char = None
        for q in items:
            reg = region_label(q["id"])
            if reg != cur_region:
                out += [f"### {reg}", ""]
                cur_region = reg
                cur_char = None
            # Under the companion region, add a per-character sub-heading so the
            # party ("we") and origin ("I") tracks sit together under the name.
            char = q.get("character") if reg == COMPANION_REGION else None
            if char and char != cur_char:
                out += [f"#### {char}", ""]
                cur_char = char

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

            form_html = (
                f'<span class="q-form">{FORM_LABEL[q["form"]]}</span>' if q.get("form") else ""
            )
            out.append(
                f'<details class="quest-entry"><summary><span class="q-title">{esc(quest_title)}</span>'
                f'{form_html}<span class="q-count">{count}</span></summary>'
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
