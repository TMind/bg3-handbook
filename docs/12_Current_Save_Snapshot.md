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

- Save name: `Arm Thy Ally`
- Save modified: `2026-07-07 11:51:01 +02:00`
- Game version: `4.1.1.7209685`
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `BGO_Main_A`

## Active Party

- Stefan: Level 10 Cleric / Death Domain (Drow Cleric)
- Lae'zel: Level 10 Fighter / Battle Master (frontline fighter)
- Kao: Level 10 Wizard / Conjuration School (human mage)
- Astarion: Level 10 Rogue / Thief (scout / lockpicker)
- Current save also has a skeleton summon and Scratch active.
- Stefan and Lae'zel are currently in camp; Kao and Astarion are outside camp. Regroup before a serious fight.

## Active Practical Buffs

### Stefan

- Blood of Lathander light aura
- Blood of Lathander self-revive resource
- Shield of Devotion extra spell slot
- Warding Bond
- Darkvision
- Longstrider
- Aid, level 3
- Freedom of Movement

### Lae'zel

- Killer's Sweetheart / critical execution ring effect
- Freedom of Movement
- Death Ward
- Darkvision
- Longstrider

### Kao

- Absorb Elements resource
- Darkvision
- Death Ward
- Freedom of Movement
- Longstrider
- Mage Armor
- Warding Bond
- Aid, level 3
- Can summon Shovel / familiar flag
- Potion of Animal Speaking

### Astarion

- Cat's Grace / Graceful Cloth effect
- Darkvision
- Longstrider
- Aid, level 3

## Confirmed Item-Sourced Buffs

- Stefan has Blood of Lathander and Devotee's Mace available.
- Stefan has Shield of Devotion spell-slot support active.
- Lae'zel has Killer's Sweetheart / critical execution ring support active.
- Astarion has Cat's Grace / Graceful Cloth support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
