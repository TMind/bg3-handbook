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

- Save name: `QuickSave_186`
- Save modified: `2026-08-09 23:18:49 +02:00`
- Synced into handbook: `2026-08-10 00:12:00 +02:00`
- Game version: `4.1.1.7398727` (patched since the last sync, was `4.1.1.7209685`)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | Level 10 Cleric / Death Domain | 73,798 total; 17,798 into level | `LOW_Sewers_SUB` | Grouped with the main party; Blood of Lathander and Shield of Devotion effects active, Speak with Dead recast available. |
| Lae'zel | Level 10 Fighter / Battle Master | 73,628 total; 17,628 into level | `LOW_Sewers_SUB` | Grouped with the main party; **Elixir of Bloodlust active** (with temp-HP rider). Partial ceremorphosis ongoing. |
| Kao | Level 10 Wizard / Conjuration School | 73,398 total; 17,398 into level | `LOW_Sewers_SUB` | Grouped with the main party; **recently resurrected** — Mage Armor has lapsed and needs recasting before the next fight. Now holding Warding Bond instead of TMind. |
| Astarion | Level 10 Rogue / Thief | 73,228 total; 17,228 into level | `LOW_Sewers_SUB` | Grouped with the main party; Cloak of Displacement and Cat's Grace active, Detect Thoughts up. |

The party has moved on from Wyrm's Rock Fortress and is now in the **Lower City sewers** (Act 3). Current save also has a **Conjure Elemental (Air)** summon (level 9) grouped with the party — the earlier Flying Ghoul and quasit summons are gone.

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
- Fox's Cunning elixir effect
- No longer has Warding Bond — see Kao

### Lae'zel

- **Elixir of Bloodlust** (with temp-HP rider)
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Killer's Sweetheart / critical-execution ring effect
- Partial ceremorphosis status
- Aid

### Kao

- Aid
- Warding Bond (received — moved over from TMind since the last snapshot)
- Longstrider
- Darkvision
- Absorb Elements cloak resource
- Can summon Shovel / familiar flag
- **Recently resurrected** (`IsResurrected` flag set) — Mage Armor is not currently active; recast it before the next hard fight

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

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support, Blood of Lathander light, and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active.
- Kao has the Absorb Elements cloak resource active.
- Astarion has Cat's Grace / Graceful Cloth and the Cloak of Displacement support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Kao was resurrected since the last snapshot** (`IsResurrected` flag on the character node) — this likely explains the missing Mage Armor and the Warding Bond having moved from TMind to Kao.
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md) — not yet refreshed for this snapshot.
