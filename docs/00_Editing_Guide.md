---
title: "Editing Guide"
aliases:
  - Handbook Editing Guide
  - Vault Maintenance
tags:
  - bg3
  - handbook
  - maintenance
---

# 🛠️ Editing Guide

This note is for maintaining the handbook. It is not part of the player-facing chapter sequence.

## Contents

- **Standards:** [[#Scope|Scope]] · [[#Language|Language]] · [[#Spoiler Policy|Spoiler Policy]]
- **Formatting:** [[#Wikilinks and Tables|Wikilinks and Tables]] · [[#Marker Scale|Marker Scale]]
- **Maintenance:** [[#Source Policy|Source Policy]] · [[#History Entries|History Entries]] · [[#Validation|Validation]] · [[#Save-Based Audits|Save-Based Audits]]

## Scope

The handbook should stay practical:

- concrete in-game benefit,
- time saved,
- fights made easier,
- common mistakes avoided,
- easy-to-miss mechanics explained.

Avoid complete walkthroughs, full class guides, lore summaries, item catalogs, and patch history without direct gameplay impact.

## Language

- Handbook content: English.
- Filenames: keep the existing numbered chapter order.
- Conversation and maintenance notes can be German when working with the owner, but committed handbook text should stay English.

## Spoiler Policy

The handbook should stay spoiler-light by default. Concrete story locations, late-game enemy names, companion outcomes, and quest-specific tricks should be hidden in collapsed Obsidian callouts:

```md
> [!warning]- Spoiler: brief neutral label
> Spoiler text goes here.
```

General mechanics, interface habits, consumable advice, and non-specific preparation tips can stay visible.

### Spoiler Checklist

Hide these by default:

- named late-game bosses,
- named quest outcomes,
- companion-specific outcomes,
- final-area tactics,
- named exploit examples,
- exact locations for hidden story rewards,
- video titles that reveal late-game content.

Keep these visible:

- general combat mechanics,
- UI habits,
- non-specific preparation advice,
- item categories without story context,
- spoiler-neutral links such as "missable magic item".

## Wikilinks and Tables

Obsidian Wikilinks inside Markdown tables must escape the display-text pipe:

```md
| Item | Use |
|---|---|
| [[06_Elixirs_and_Potions#^potion-of-speed\|Potion of Speed]] | Opening tempo |
```

Prefer direct block links for potions, elixirs, and alchemy resources.

## Marker Scale

Use only this priority scale:

| Marker | Meaning |
|---|---|
| ⭐ | Useful priority |
| ⭐⭐ | Important |
| ⭐⭐⭐ | Very important / read first |

Additional markers:

| Marker | Meaning |
|---|---|
| ⚠️ | Common mistake or easy-to-miss trap |
| 💰 | Saves gold or preserves valuable resources |
| ⏱️ | Saves time |
| ⚔️ | Combat tip |
| 🧪 | Alchemy or ingredient management |
| 🍷 | Potion, elixir, or consumable |
| ✨ | Magic, spell, or buff |
| 🎯 | Advanced trick or high-impact optimization |

## Source Policy

The original practical tip set was based on BG3 videos from **Doms Roundtable**. Other videos are supporting sources and should not be presented as the original source unless that is true.

When adding video references:

- keep source labels spoiler-neutral,
- put spoiler-prone videos in collapsed callouts,
- prefer chapter-level source tables over inline source clutter,
- add central source entries in [Appendix](15_Appendix.md).

## History Entries

Update [Handbook History](00_History.md) after meaningful changes:

- new chapters, sections, source videos, or save-audit outputs,
- major rewrites, reorganizations, or corrections,
- Git setup changes or maintenance workflow changes.

Small typo fixes do not need a history entry unless they correct gameplay advice.

## Validation

Run the local vault check after edits:

```sh
python3 scripts/check_vault.py
```

The script checks:

- unescaped Wikilink pipes inside tables,
- inconsistent Markdown table column counts,
- marker priority above ⭐⭐⭐,
- missing Obsidian target files or block IDs,
- selected spoiler terms outside collapsed callouts.

## Save-Based Audits

Before updating party, inventory, buff, or readiness snapshots from a savegame, sync the latest real save first:

```sh
python3 tools/sync_latest_save.py --list 5
python3 tools/sync_latest_save.py
```

The detailed workflow is in `tools/SAVEGAME_WORKFLOW.md`. Use `tools/save-extract/source_manifest.json` as the source-of-truth record for which save was audited.
