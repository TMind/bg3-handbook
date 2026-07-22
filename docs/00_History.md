---
title: "Handbook History"
aliases:
  - History
  - Changelog
  - What's New
tags:
  - bg3
  - handbook
  - maintenance
  - history
---

# 🕰️ Handbook History

This note records meaningful handbook changes so it is clear what was added, refreshed, or reorganized.

Use newest entries first. Keep entries practical: what changed, why it matters, and which notes were touched.

## 2026-07-22

### Added

- Added `chronicle.md`, a narrative party chronicle: the characters' story so far (prologue, an act-by-act shared arc, per-character arcs, and a save-waypoint timeline), grounded in the current save's quest journal and the campaign notes (handles only). Story beats are anchored to real saves by playtime (the run has 136 named location-saves from the crash at 1h to Wyrm's Rock at 100h). Added to the site build and sidebar (Current Campaign → Party Chronicle), browsable and searchable alongside the journal.
- Added `tools/extract_item_names.py`, which builds a local `tools/item-names/item_names.json` cache mapping item stat names to their real display names (RootTemplates `_merged.lsf` with ParentTemplateId inheritance, joined to `english.loca`). It reuses the LSPK reader from `extract_journal_text.py` and the LSF parser from `index_lsf.py`, so future item re-audits are one command instead of an ad-hoc rebuild. The cache is gitignored (copyrighted names).

### Changed

- Rewrote the [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) as a full item re-audit of the `Wyrms Rock Fortress - 100h 29m` save. Item display names are now resolved from the game's own root templates and localization (a stat/template → DisplayName → loca join, same approach as the journal text), so names match in game; per-character gear, consumable counts, and storage highlights are refreshed (e.g. TMind now has The Whispering Promise, Astarion has Cloak of Displacement + The Joltshooter, Kao's Absorb Elements is the Cloak of Elemental Absorption). Readiness consumable counts were refreshed to match.
- Refreshed the save-derived snapshots from the `Wyrms Rock Fortress - 100h 29m` save: rewrote the party, buff, and item-source sections of [Current Save Snapshot](12_Current_Save_Snapshot.md) (party now in `WYR_Fortress_SUB`, XP ~63.7k, Flying Ghoul summon, Elixir of Bloodlust now active on Lae'zel, Pass Without Trace no longer active, new item effects), and updated the verdict, buff coverage, and source in [Current Readiness Audit](14_Current_Readiness_Audit.md). The item snapshot (`docs/13`) got the new source reference and a note that its detailed tables still reflect the prior inventory pass pending a full item re-audit. Also updated the current location in `CLAUDE.md` and `session-notes.md`.

### Fixed

- Ran a systematic flag audit over all quest nodes (lone fallback closures, contradictory step pairs, ambiguous prototype resolution). Findings: confirmed the Halsin and Minthara fallback-text cases; discovered that **Karlach was killed in Act 1** (head delivered for the bounty; permanently dead) and that **Wyll was recruited** — added his arc and Karlach's fate to the chronicle and session notes. Fixed the journal's quest resolution to break step-membership ties via the node's ObjectiveID prefix, which had mis-titled `DEN_RobbedAdventurer` (shared `GroveChanged` step) and could mix the Astarion COM/Avatar tracks.
- Fixed companion quests mixing first-person and party-perspective text. The save records each companion quest twice — the `ORI_COM_*` party track ("we...") and the first-person `ORI_Avatar_*` origin track ("I...") — and merging them by title interleaved the two voices. The journal now groups quests by prototype id (so the two tracks stay separate), sub-groups the companion section under each character's name with a `####` heading, and tags every entry `party view` / `origin view`. Both perspectives are preserved, side by side, without mixing.
- Corrected the quest journal to show only genuine journal entries. The save's `QuestUnlockedSteps` were resolved to prototype quests by step-membership (the reliable key) rather than by objective-id prefix, which had mis-mapped several quests and rendered internal/empty steps as bogus humanized lines. Quest nodes that share a title (a companion's ORI_COM and ORI_Avatar tracks, or one node per objective) are now merged into a single entry with de-duplicated text, and untranslated placeholder titles (`%%% EMPTY`) fall back to a readable id.

## 2026-07-21

### Added

- Added `tools/extract_journal_text.py`, which reads the player's own installed game files (`Gustav.pak` → `quest_prototypes.lsx`, `English.pak` → `english.loca`) directly — no LSLib/Divine needed — to build a `tools/journal-text/quest_text.json` cache mapping quests and steps to their real localized journal text. When that cache is present, `build_journal.py` fills `journal.md` with the verbatim in-game entries (with a Larian attribution line); without it, it falls back to readable titles derived from the ids so CI still builds. The intermediate cache is gitignored.

- Added `tools/build_journal.py`, which generates a quest journal (open and completed quests with their step trails) from an indexed save, and published the generated `journal.md`. It is spoiler-heavy (full story progress). It lives at the repo root, so `check_vault.py` does not scan it — same as `session-notes.md`.
- Added `journal.md` to the generated site (`scripts/build_site.py`) and the sidebar (Current Campaign → Quest Journal), so it is browsable and searchable alongside the handbook chapters.
- Made each quest a collapsible `<details>` entry (generator emits the HTML; the site renderer passes `<details>` blocks through and styles them). Keeps the long list scannable and works on the site, on GitHub, and in Obsidian.

## 2026-07-19

### Added

- Added a client-side search box to the generated site (`scripts/site_template.html`): indexes every chapter section in the browser, ranks results, shows highlighted snippets, and jumps to the matching heading. No backend — all content is already embedded in the page. Press `/` to focus it, `Esc` to clear.

## 2026-07-18

### Changed

- Standardized all player references to handles (`Kao`, `tmind`/`TMind`) across the handbook, notes, character files, and map, and renamed the cleric's character notes to `characters/tmind.md`. Anchor ids and the save tooling's default focus pattern were updated to match.

### Added

- Added `scripts/build_site.py` and `scripts/site_template.html`, which build a single self-contained `site/index.html` from the vault — a navigable web version of the handbook with a chapter sidebar and working internal links (Obsidian Wikilinks and Markdown links both resolve). `site/` is gitignored as a generated artifact.
- Added `.github/workflows/pages.yml` to rebuild and deploy the site to GitHub Pages on every push to `main` (requires enabling Pages with the GitHub Actions source).

### Changed

- Resolved the stale Sussur Bark open question in `session-notes.md`: the bark was crafted into the Sussur Dagger, currently held by Astarion.
- Removed the outdated Lae'zel level 7 feat decision from `session-notes.md` and `11_Main_Character_Builds.md` — she is now Fighter 10, so the decision point has passed. Noted that exact feat/maneuver picks aren't reliably readable from the save extract and should be verified in game.

## 2026-07-13

### Changed

- Refreshed the current save snapshot, item snapshot, and readiness audit from `Wyrms Crossing - 98h 15m`.
- Updated active-party buff coverage: the main party is grouped in `WYR_Bridge_SUB`, Death Ward and Freedom of Movement are active on all four main characters, and Aid is still missing from Lae'zel.
- Updated visible inventory/resource counts for the latest extracted save, including Bloodlust, Viciousness, Revivify, Potion of Speed, Globe, Conjure Elemental, and healing-potion stock.
- Added current-holder information to the item snapshot's resource and best-use tables.

### Verified

- Synced and extracted `Wyrms Crossing - 98h 15m`, modified 2026-07-13 01:25:09 +02:00.
- Mirrored the save into `saves/TMind-25121262363__Wyrms Crossing - 98h 15m/`.
- Rebuilt the local `.lsf` index for the refreshed snapshot.

## 2026-07-12

### Changed

- Updated the save sync workflow so the selected latest save folder is also copied into `saves/`.
- Refreshed the `characters/` notes from the latest local save, `Rivington - 96h 28m`.
- Replaced old Act 2 / level-planning character notes with current active-party summaries for TMind, Lae'zel, Kao, and Astarion.
- Updated camp notes for Shadowheart, Gale, the active summons, and current before-fight checks.

### Verified

- Ran the save sync workflow against the current latest save, `Rivington - 96h 28m`, modified 2026-07-12 23:37:38 +02:00.
- Mirrored `Rivington - 96h 28m` into `saves/`.
- Character notes in this entry were refreshed from `Rivington - 96h 28m`, modified 2026-07-12 23:37:38 +02:00.
- Rebuilt the local save index during the `Rivington - 96h 28m` character refresh.

### Added

- Created the first Git-backed handbook snapshot.
- Added this history note so future updates can record what is new.

### Tracked Content

- Handbook chapters from [Basics and User Interface](01_Basics_and_User_Interface.md) through [Appendix](15_Appendix.md).
- Current campaign notes: [Current Save Snapshot](12_Current_Save_Snapshot.md), [Current Item and Storage Snapshot](13_Item_Inventory_Snapshot.md), and [Current Readiness Audit](14_Current_Readiness_Audit.md).
- Maintenance tools and source transcripts used by the handbook.

### Ignored Local Files

- Savegame extracts, generated save indexes, bundled external tools, Python caches, local trash, local Obsidian workspace state, and volatile YouTube metadata.

## Entry Template

```md
## YYYY-MM-DD

### Added

- New note, section, mechanic, source, or workflow.

### Changed

- Existing content that was rewritten, reorganized, corrected, or expanded.

### Verified

- Checks run, source reviewed, save refreshed, or Git commit made.
```
