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

- Save name: `Campsite - 106h 21m`
- Save modified: `2026-08-16 12:55:09 +02:00`
- Synced into handbook: `2026-08-16 17:26:26 +02:00`
- Game version: `4.1.1.7398727` (unchanged since the last sync)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | **Level 11** Cleric / Death Domain | 79,005 total; 3,005 into level | `CAMP_SUB` | Unchanged from last snapshot. Blood of Lathander and Shield of Devotion effects active, Speak with Dead recast available. |
| Lae'zel | **Level 11** Fighter / Battle Master | 78,835 total; 2,835 into level | `CAMP_SUB` | Unchanged. **Elixir of Bloodlust active** (temp-HP rider still worn off). Partial ceremorphosis ongoing. Now also carrying the Vivacious Cloak moved over from TMind (see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md)). |
| Kao | **Level 11** Wizard / Conjuration School | 78,605 total; 2,605 into level | `CAMP_SUB` | Still missing Death Ward, Freedom of Movement, and Mage Armor since his resurrection — **three full snapshots now** with none recast. |
| Astarion | **Level 11** Rogue / Thief | 78,435 total; 2,435 into level | `CAMP_SUB` | Cat's Grace and Cloak of Displacement still active, Death Ward still missing. Now also carrying the Hellfire Hand Crossbow and Shade-Slayer Cloak moved over from TMind. |

Only 9 minutes of in-game time passed since the last snapshot (106h12m → 106h21m) — the party is still at camp, no combat, no XP gained, and buffs are byte-for-byte identical to last time. The one real change: **two of the recommended gear moves from the last audit were actually carried out** — see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) for what moved and what's still outstanding. The Cambion (Planar Ally) summon is still with the party.

## Active Practical Buffs

### TMind

- Heroes' Feast
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

- Heroes' Feast
- **Elixir of Bloodlust** (temp-HP rider still worn off; base buff remains)
- Death Ward
- Freedom of Movement
- Longstrider
- Darkvision
- Killer's Sweetheart / critical-execution ring effect
- Partial ceremorphosis status
- Aid

### Kao

- Heroes' Feast
- Aid
- Warding Bond (received, unchanged)
- Longstrider
- Darkvision
- Absorb Elements cloak resource
- Can summon Shovel / familiar flag
- Elixir of See Invisibility
- **Still missing Death Ward, Freedom of Movement, and Mage Armor** — unresolved across three full snapshots since his resurrection

### Astarion

- Heroes' Feast
- See Invisibility
- Aid
- Freedom of Movement
- Longstrider
- Darkvision
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- Detect Thoughts
- Potion of Animal Speaking
- Astarion happy status
- Potion of Poison Resistance
- **Death Ward still missing** — dropped off two snapshots ago and hasn't been recast

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support, Blood of Lathander light, and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active.
- Kao has the Absorb Elements cloak resource active.
- Astarion has Cat's Grace / Graceful Cloth and the Cloak of Displacement support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Kao's Death Ward, Freedom of Movement, and Mage Armor gaps now span three full snapshots** since his resurrection — the party has been at/near camp for two of those three passes without fixing it, so this is worth doing proactively rather than waiting for it to matter mid-fight.
- **Astarion's Death Ward is still missing**, unresolved since it dropped two snapshots ago.
- The party did act on part of the previous readiness checklist: the Hellfire Hand Crossbow and Shade-Slayer Cloak moved from TMind to Astarion, and the Vivacious Cloak moved from TMind to Lae'zel — all three recommended moves from last time. The buff recasts and Kao's scroll hand-back were not done.
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
