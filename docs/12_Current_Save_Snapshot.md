---
title: "Current Save Snapshot"
aliases:
  - Current Party Snapshot
  - Save Snapshot
tags:
  - bg3
  - handbook
  - party
  - save
  - snapshot
---

# Current Save Snapshot

This note summarizes the current save state extracted from the local save file. It intentionally omits spoiler-sensitive story state.

> [!info] Navigation
> Previous: [Main Character Builds](11_Main_Character_Builds.md) | Home: [Baldur's Gate 3 Practical Handbook](../README.md) | Next: [Current Item and Storage Snapshot](13_Item_Inventory_Snapshot.md)

## Contents

- [[#Save|Save]] · [[#Active Party|Active Party]] · [[#Active Practical Buffs|Active Practical Buffs]] · [[#Confirmed Item-Sourced Buffs|Item-Sourced Buffs]] · [[#Extraction Notes|Extraction Notes]]

## Save

- Save name: `Wyrms Crossing - 98h 15m`
- Save modified: `2026-07-13 01:25:09 +02:00`
- Synced into handbook: `2026-07-13 01:25:41 +02:00`
- Game version: `4.1.1.7209685`
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `BGO_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| Stefan | Level 10 Cleric / Death Domain | 61,597 total; 5,597 into level | `WYR_Bridge_SUB` | Grouped with the main party. |
| Lae'zel | Level 10 Fighter / Battle Master | 61,597 total; 5,597 into level | `WYR_Bridge_SUB` | Grouped with the main party; no active Bloodlust detected. |
| Kao | Level 10 Wizard / Conjuration School | 61,197 total; 5,197 into level | `WYR_Bridge_SUB` | Grouped with the main party; no active `DYING` status detected in the active-party block. |
| Astarion | Level 10 Rogue / Thief | 61,597 total; 5,597 into level | `WYR_Bridge_SUB` | Grouped with the main party and has stealth support active. |

Current save also has a skeleton summon grouped with the party. Scratch and Shovel / quasit are active but currently appear in `WYR_Flophouse_SUB`, away from the bridge group.

## Active Practical Buffs

### Stefan

- Shield of Devotion extra spell slot
- Warding Bond
- Darkvision
- Longstrider
- Aid, level 3
- Freedom of Movement
- Death Ward
- Pass Without Trace

### Lae'zel

- Killer's Sweetheart / critical execution ring effect
- Partial ceremorphosis status
- Freedom of Movement
- Death Ward
- Darkvision
- Longstrider
- Pass Without Trace

### Kao

- Darkvision
- Death Ward
- Freedom of Movement
- Longstrider
- Mage Armor
- Warding Bond
- Aid, level 3
- Can summon Shovel / familiar flag
- Potion of Animal Speaking
- Fox's Cunning
- Pass Without Trace

### Astarion

- Cat's Grace / Graceful Cloth effect
- Darkvision
- Longstrider
- Aid, level 3
- Death Ward
- Freedom of Movement
- Pass Without Trace aura
- Astarion happy status

## Confirmed Item-Sourced Buffs

- Stefan has Shield of Devotion spell-slot support active.
- Lae'zel has Killer's Sweetheart / critical execution ring support active.
- Astarion has Cat's Grace / Graceful Cloth support active.
- Astarion has Pass Without Trace support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- The broader save contains many `DYING` statuses on old or non-active entities. The active-party status managers for Stefan, Lae'zel, Kao, and Astarion do not show `DYING` in this save.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
