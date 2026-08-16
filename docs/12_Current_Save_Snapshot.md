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

- Save name: `AutoSave_127`
- Save modified: `2026-08-10 00:27:55 +02:00`
- Synced into handbook: `2026-08-13 12:36:47 +02:00`
- Game version: `4.1.1.7398727` (unchanged since the last sync)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | Level 10 Cleric / Death Domain | 74,808 total; 18,808 into level | `LOW_UndercityRuins_SUB` | Grouped with the main party; Blood of Lathander and Shield of Devotion effects active, Speak with Dead recast available. |
| Lae'zel | Level 10 Fighter / Battle Master | 74,638 total; 18,638 into level | `LOW_UndercityRuins_SUB` | Grouped with the main party; **Elixir of Bloodlust active** (temp-HP rider has worn off, base buff remains). Partial ceremorphosis ongoing. |
| Kao | Level 10 Wizard / Conjuration School | 74,408 total; 18,408 into level | `LOW_UndercityRuins_SUB` | Grouped with the main party; drank an **Elixir of Arcane Acuity**. Still missing Death Ward, Freedom of Movement, and Mage Armor since his resurrection — none of the three have been recast yet. |
| Astarion | Level 10 Rogue / Thief | 74,238 total; 18,238 into level | `LOW_UndercityRuins_SUB` | Grouped with the main party; Cloak of Displacement and Cat's Grace active, drank a Potion of Fire Resistance. |

The party has moved a short distance on from the Lower City sewers into the **Undercity Ruins** (Act 3), about an hour of play after the previous snapshot. Current save still has the **Conjure Elemental (Air)** summon (level 9) grouped with the party.

## Active Practical Buffs

### TMind

- Aid
- Death Ward
- Longstrider
- Darkvision
- Blood of Lathander light aura (item)
- Lathander's Blessing resurrection resource (class feature, unused)
- Shield of Devotion extra spell slot (item)
- Undead-presence effect (item)
- Speak with Dead (recast available)
- No longer has Warding Bond — see Kao
- No longer has the Fox's Cunning elixir effect (worn off)

### Lae'zel

- **Elixir of Bloodlust** (temp-HP rider has worn off; base buff remains)
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Killer's Sweetheart / critical-execution ring effect
- Partial ceremorphosis status
- Aid

### Kao

- Aid
- Warding Bond (received — moved over from TMind since the previous snapshot)
- Longstrider
- Darkvision
- Absorb Elements cloak resource
- Can summon Shovel / familiar flag
- **Elixir of Arcane Acuity** (new this snapshot)
- **Still missing Death Ward, Freedom of Movement, and Mage Armor** since his resurrection — unchanged from the previous snapshot, none have been recast yet

### Astarion

- Aid
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- Detect Thoughts
- Potion of Animal Speaking
- Astarion happy status
- **Potion of Fire Resistance** (new this snapshot)

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support, Blood of Lathander light, and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active.
- Kao has the Absorb Elements cloak resource active.
- Astarion has Cat's Grace / Graceful Cloth and the Cloak of Displacement support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Kao's Death Ward, Freedom of Movement, and Mage Armor gaps persist from the previous snapshot** (he was resurrected shortly before that pass, `IsResurrected` flag on the character node) — none have been recast across an hour of further play, so this is worth doing proactively rather than waiting for it to matter mid-fight.
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
