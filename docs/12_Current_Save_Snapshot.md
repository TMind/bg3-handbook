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

- Save name: `Wyrms Rock Fortress - 100h 29m`
- Save modified: `2026-07-21 01:26:37 +02:00`
- Synced into handbook: `2026-07-22 00:29:42 +02:00`
- Game version: `4.1.1.7209685`
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `BGO_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | Level 10 Cleric / Death Domain | 63,747 total; 7,747 into level | `WYR_Fortress_SUB` | Grouped with the main party; Blood of Lathander and Shield of Devotion effects active. |
| Lae'zel | Level 10 Fighter / Battle Master | 63,747 total; 7,747 into level | `WYR_Fortress_SUB` | Grouped with the main party; **Elixir of Bloodlust now active**. Aid still not detected. |
| Kao | Level 10 Wizard / Conjuration School | 63,347 total; 7,347 into level | `WYR_Fortress_SUB` | Grouped with the main party; Mage Armor and Absorb Elements resource active. |
| Astarion | Level 10 Rogue / Thief | 63,917 total; 7,917 into level | `WYR_Fortress_SUB` | Grouped with the main party; Cloak of Displacement and Cat's Grace active, sneaking. |

Current save also has a **Flying Ghoul** summon (level 6) and a quasit grouped with the party in `WYR_Fortress_SUB`. The party is at Wyrm's Rock Fortress.

## Active Practical Buffs

### TMind

- Aid, level 3
- Warding Bond (received)
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Blood of Lathander light aura (item)
- Undead-presence effect (item)
- Shield of Devotion extra spell slot (item)

### Lae'zel

- **Elixir of Bloodlust** (with temp-HP rider)
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Killer's Sweetheart / critical-execution ring effect
- Astral Knowledge (Charisma)
- Partial ceremorphosis status
- No Aid detected

### Kao

- Aid, level 3
- Warding Bond (received)
- Mage Armor
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Absorb Elements cloak resource
- Detect Thoughts
- Potion of Animal Speaking
- Can summon Shovel / familiar flag

### Astarion

- Aid, level 3
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- Astarion happy status
- Sneaking / lightly obscured

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support, Blood of Lathander light, and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active.
- Kao has the Absorb Elements cloak resource active.
- Astarion has Cat's Grace / Graceful Cloth and the Cloak of Displacement support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Pass Without Trace is no longer active** on the party in this save (it was in the previous snapshot). Re-apply it before stealth-sensitive approaches if wanted.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
