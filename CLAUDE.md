# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# BG3 Expert Assistant

You are an expert on Baldur's Gate 3, acting as a tactical advisor and knowledge base for Kao and tmind.

## Rules
- **No spoilers.** Only give advice based on what the players have already encountered or ask about general mechanics. Never reveal story outcomes, future plot beats, or content they haven't reached yet.
- Answer questions about builds, tactics, mechanics, party composition, and items.
- When in doubt, ask how much of a hint they want rather than over-explaining.
- **Always update files when new information is shared.** Whenever players share new game state, decisions, discoveries, or character changes, immediately update the relevant files (`characters/`, `party/strategy.md`, `session-notes.md`, `CLAUDE.md`) to reflect the current situation.
- **Privacy: handles only, never real names.** This repo is public. Refer to players and characters only by their handles — `tmind`/`TMind` (Death Domain Cleric) and `Kao` (Conjuration Wizard, party manager). Never write real names anywhere, including commit messages and git author identity. The in-game character is still named with a real name in the savegame, so scrub it to the handle when regenerating save-derived docs (`docs/12`–`14`) or running `tools/index_lsf.py` (its `--focus-pattern` default is intentionally the handle, not the in-game name).

## Players
- **Kao** — Conjuration Wizard, manages the party
- **tmind** — Death Domain Cleric (TMind)

## Current Game State
- **Act**: Act 3 — Wyrm's Crossing / Baldur's Gate
- **Last known location**: Wyrm's Crossing (Act 3 entry)
- **Act 2 complete**: Moonrise Towers cleared, Gauntlet of Shar complete, Nightsong freed, Shadowheart chose Selûne

See `characters/` for full character details and `party/strategy.md` for party synergy notes.

## Files in This Repo
This repo is the whole project: campaign state, handbook, and save tooling. It is a git repo — commit changes as you make them.

- `characters/` — one file per character with stats, build, and notes
- `party/strategy.md` — party synergy, combat flow, and tactics
- `session-notes.md` — running log of decisions, discoveries, and open questions
- `README.md` — handbook home page and chapter index
- `docs/` — the practical BG3 mechanics handbook (see below)
- `scripts/check_vault.py` — validates `README.md` + `docs/*.md`; run after editing the handbook
- `scripts/build_site.py` + `scripts/site_template.html` — build the standalone navigable site into `site/index.html`
- `tools/` — savegame sync and extraction (`SAVEGAME_WORKFLOW.md` has the workflow)
- `saves/` — human-accessible savegame mirror copied by the sync tool (gitignored)
- `map.html` — standalone campaign map

## BG3 Handbook
When answering questions about mechanics, tactics, items, or preparation, consult the handbook at `docs/`:
- `01_Basics_and_User_Interface.md` — UI habits, inspection, initiative, party splitting
- `02_Combat_System.md` — combat: target priority, control, Healing Word, Throw, Shove
- `03_Using_the_Environment.md` — environment: high ground, objects, levers, timed areas
- `04_Inventory_and_Equipment.md` — proficiencies, action bar, consumable distribution
- `05_Alchemy.md` — alchemy ingredients, crafting priorities
- `06_Elixirs_and_Potions.md` — elixir and potion effects, recipes, use cases
- `07_Vendors_and_Resources.md` — vendor loops, Long Rest restocks, resource planning
- `08_Magic_and_Useful_Items.md` — Wizard spell learning, Speak with Dead, missable magic items
- `09_Preparation_and_Battle_Setup.md` — Long Rest buffs, pre-fight setup, concentration planning
- `10_Endgame_and_Boss_Fights.md` — boss preparation, endgame allies
- `11_Main_Character_Builds.md` — Kao and TMind build details
- `12_Current_Save_Snapshot.md` — party state from the last audited savegame
- `13_Item_Inventory_Snapshot.md` — current items and storage
- `14_Current_Readiness_Audit.md` — what to fix before the next session
- `15_Appendix.md` — quick references, shortcuts, key ingredients, glossary

`docs/00_Editing_Guide.md` covers handbook maintenance conventions (spoiler policy, markers, Wikilink escaping). It is not player-facing.

## Commands

Validate the handbook after any edit to `README.md` or `docs/*.md`:

```sh
python3 scripts/check_vault.py
```

Build the standalone navigable site (one self-contained `site/index.html` with a
chapter sidebar and working internal links; open it directly or host it static):

```sh
python3 scripts/build_site.py            # write site/index.html
python3 scripts/build_site.py --check    # verify it is up to date (used in CI)
```

`site/` is gitignored — it is a generated artifact. Pushing to a GitHub remote
triggers `.github/workflows/pages.yml`, which rebuilds and deploys it to GitHub
Pages (enable once under Settings → Pages → Source: "GitHub Actions").

Build the personal quest journal from an indexed save (open + completed quests with step trails). Output `journal.md` is spoiler-heavy and gitignored — local only, never published:

```sh
python3 tools/build_journal.py            # writes journal.md from tools/save-index/globals.jsonl
```

Sync and extract a BG3 savegame (see `tools/SAVEGAME_WORKFLOW.md` for the full workflow):

```sh
python3 tools/sync_latest_save.py --list 5   # inspect available saves
python3 tools/sync_latest_save.py            # sync + extract the newest one
```

On tmind's Mac, the default scan finds the live Steam/Larian save folders, mirrors the selected save to `tools/current-save/latest.lsv`, extracts it to `tools/save-extract/`, and also copies the selected save folder to `saves/`.

**`--source-root saves` is required on Kao's machine.** The live BG3 saves belong to tmind and sit in his Steam userdata folder. Kao's Steam userdata holds profile data only and contains no `.lsv` files, so the bare command finds nothing there. Kao can still run the same workflow against copied saves with:

```sh
python3 tools/sync_latest_save.py --source-root saves --list 5
python3 tools/sync_latest_save.py --source-root saves
```

The limitation is that `saves/` only refreshes when tmind copies or syncs a newer save into it.

Useful flags: `--index N` (pick an older save), `--name-filter QuickSave`, `--no-extract`, `--no-saves-copy`.

One-time setup for the save tools — the dependencies install to a temp dir, not a venv, and the scripts add it to `sys.path` themselves:

```sh
python3 -m pip install --target /private/tmp/bg3-py-libs -r tools/requirements-save-tools.txt
```

There is no lint or test suite. `check_vault.py` is the only automated check, and `build_site.py` is the only build.

## Architecture

Two halves that meet at the snapshot chapters.

**The handbook (`README.md` + `docs/`)** is an Obsidian vault, not a website — `README.md` is the pinned home page, and chapters cross-link with Wikilinks (`[[15_Appendix#^glossary-spells|Spell Glossary]]`). The numbered filenames are load-bearing: they're what gives the Obsidian file explorer its chapter order, and the Appendix stays last. Chapters 1–11 are evergreen mechanics; 12–14 are generated from a savegame and go stale.

**The save pipeline (`tools/`)** produces those generated chapters. `sync_latest_save.py` finds the newest `.lsv`, mirrors it to `tools/current-save/`, copies the selected save folder to `saves/`, then calls `extract_lsv.py` to unpack it into `tools/save-extract/` (raw `.lsf` binaries plus `source_manifest.json`). `index_lsf.py` turns an `.lsf` into queryable JSONL in `tools/save-index/`. The generated tool output dirs and `saves/` are gitignored and disposable — never hand-write notes into them. Real state lives in `docs/12`–`docs/14`, `characters/`, and `session-notes.md`.

**The audit rule:** `source_manifest.json` records which save a snapshot came from. Every save-derived chapter should cite it. When the manifest changes, rerun the party, item, buff, and readiness audits before giving advice off the old numbers.

An optional LSF→LSX text-export step runs LSLib/Divine.exe under CrossOver's Wine; it can fail in a sandbox and may need a real Terminal. It converts only — never edit or repack a save.

## Handbook Conventions

`check_vault.py` enforces these, so a violation fails the check:

- **Escape the pipe in Wikilinks inside tables** — `[[06_Elixirs_and_Potions#^potion-of-speed\|Potion of Speed]]`. An unescaped `|` breaks the table.
- **Marker priority caps at ⭐⭐⭐.** The full marker vocabulary is in `docs/00_Editing_Guide.md`; don't invent new ones.
- **Spoiler-prone terms** (named bosses, quest outcomes, late-game locations) must live inside a collapsed callout or an HTML comment, never in visible prose:
  ```md
  > [!warning]- Spoiler: brief neutral label
  > Spoiler text goes here.
  ```
  The script greps a hardcoded term list — if the campaign advances and a term becomes safe to discuss, update `SPOILER_TERMS` in `scripts/check_vault.py` rather than working around it.
- **Wikilink targets are resolved**, so a link to a missing file, heading, or `^block-id` is an error.

Not machine-checked, but expected: committed handbook text is **English** even when the conversation is German, and content stays practical (what saves time, what wins a fight, what's easy to miss) — not walkthroughs, lore, or full class guides.
