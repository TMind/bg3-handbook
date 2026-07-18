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

## 2026-07-18

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
- Mirrored the save into `saves/Stefan-25121262363__Wyrms Crossing - 98h 15m/`.
- Rebuilt the local `.lsf` index for the refreshed snapshot.

## 2026-07-12

### Changed

- Updated the save sync workflow so the selected latest save folder is also copied into `saves/`.
- Refreshed the `characters/` notes from the latest local save, `Rivington - 96h 28m`.
- Replaced old Act 2 / level-planning character notes with current active-party summaries for Stefan, Lae'zel, Kao, and Astarion.
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
