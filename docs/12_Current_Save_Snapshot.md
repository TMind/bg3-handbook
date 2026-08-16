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

- Save name: `Campsite - 106h 12m`
- Save modified: `2026-08-16 02:02:22 +02:00`
- Synced into handbook: `2026-08-16 11:29:07 +02:00`
- Game version: `4.1.1.7398727` (unchanged since the last sync)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | **Level 11** Cleric / Death Domain | 79,005 total; 3,005 into level | `CAMP_SUB` | Leveled up since the last snapshot — **Heroes' Feast is now available**. Blood of Lathander and Shield of Devotion effects active, Speak with Dead recast available. |
| Lae'zel | **Level 11** Fighter / Battle Master | 78,835 total; 2,835 into level | `CAMP_SUB` | **Elixir of Bloodlust active** (temp-HP rider still worn off, base buff remains). Partial ceremorphosis ongoing. |
| Kao | **Level 11** Wizard / Conjuration School | 78,605 total; 2,605 into level | `CAMP_SUB` | Still missing Death Ward, Freedom of Movement, and Mage Armor since his resurrection two snapshots ago — none have been recast yet. |
| Astarion | **Level 11** Rogue / Thief | 78,435 total; 2,435 into level | `CAMP_SUB` | Cat's Grace and Cloak of Displacement still active, but **Death Ward has dropped off him** since the last snapshot. |

The whole party leveled up to 11 and is now back at **camp** (Act 3), about six hours of play after the previous snapshot. The old Conjure Elemental (Air) summon is gone (last seen stranded back in the Lower City sewers, no longer grouped with the party); in its place there's a new **Cambion (Planar Ally) summon**, level 10, at camp with the party — almost certainly from TMind's new Cleric 11 spell access.

## Active Practical Buffs

### TMind

- **Heroes' Feast** (new — unlocked at Cleric 11)
- Aid
- Death Ward
- Longstrider
- Darkvision
- Blood of Lathander light aura (item)
- Lathander's Blessing resurrection resource (class feature, unused)
- Shield of Devotion extra spell slot (item)
- Undead-presence effect (item)
- Speak with Dead (recast available)
- Still no Warding Bond — see Kao

### Lae'zel

- **Heroes' Feast** (new)
- **Elixir of Bloodlust** (temp-HP rider still worn off; base buff remains)
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Killer's Sweetheart / critical-execution ring effect
- Partial ceremorphosis status
- Aid

### Kao

- **Heroes' Feast** (new)
- Aid
- Warding Bond (received, unchanged)
- Longstrider
- Darkvision
- Absorb Elements cloak resource
- Can summon Shovel / familiar flag
- **Elixir of See Invisibility** (new this snapshot; the earlier Elixir of Arcane Acuity has worn off)
- **Still missing Death Ward, Freedom of Movement, and Mage Armor** — unresolved across two full snapshots since his resurrection

### Astarion

- **Heroes' Feast** (new)
- **See Invisibility** (new)
- Aid
- Freedom of Movement
- Longstrider
- Darkvision
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- Detect Thoughts
- Potion of Animal Speaking
- Astarion happy status
- **Potion of Poison Resistance** (new this snapshot; the earlier Fire Resistance potion has worn off)
- **Death Ward has dropped off him** (new gap — he had it last snapshot)

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support, Blood of Lathander light, and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active.
- Kao has the Absorb Elements cloak resource active.
- Astarion has Cat's Grace / Graceful Cloth and the Cloak of Displacement support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Kao's Death Ward, Freedom of Movement, and Mage Armor gaps now span two full snapshots** since his resurrection — worth fixing proactively next time the party leaves camp rather than waiting for it to matter mid-fight.
- **Astarion's Death Ward has newly dropped off** — worth checking in game whether that was a deliberate choice (e.g. a Warding Bond-style trade-off) or just an oversight.
- The whole party reaching **Heroes' Feast** access (Cleric 11) resolves a gap flagged in the previous [Current Readiness Audit](14_Current_Readiness_Audit.md) as "the next major daily-buff upgrade."
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
