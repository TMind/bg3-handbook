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

- Save name: `The Blushing Mermaid - 109h 15m`
- Save modified: `2026-08-16 22:29:04 +02:00`
- Synced into handbook: `2026-08-16 22:34:51 +02:00`
- Game version: `4.1.1.7398727` (unchanged since the last sync)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | **Level 11** Cleric / Death Domain | 82,511 total; 6,511 into level | `LOW_BlushingMermaid_SUB` | Real fight happened (+3,506 XP). **Death Ward has newly dropped in addition to Freedom of Movement** — he's now the only one missing either. A partial-ceremorphosis status is also present on him — see Extraction Notes. |
| Lae'zel | **Level 11** Fighter / Battle Master | 82,511 total; 6,511 into level | `LOW_BlushingMermaid_SUB` | **Death Ward, Freedom of Movement, Elixir of Bloodlust, and a fresh temp-HP buff all active** — fully buffed. |
| Kao | **Level 11** Wizard / Conjuration School | 82,111 total; 6,111 into level | `LOW_BlushingMermaid_SUB` | **All three standing gaps resolved**: Death Ward, Freedom of Movement, and Mage Armor are all active for the first time in four snapshots. |
| Astarion | **Level 11** Rogue / Thief | 81,941 total; 5,941 into level | `LOW_BlushingMermaid_SUB` | **Death Ward is back** (was missing for three snapshots) — Cat's Grace and Cloak of Displacement still active too. |

The party fought something — XP is up ~3,500-4,000 each — and moved to **The Blushing Mermaid** (a Lower City location). Buff coverage flipped: Kao's three standing gaps (Death Ward, Freedom of Movement, Mage Armor) and Astarion's Death Ward gap are all resolved, but **TMind picked up two new gaps of his own** — Death Ward and Freedom of Movement both dropped off him. Net effect: he's now the only party member missing either. Summons changed: the Cambion (Planar Ally) is gone, replaced by a **Djinni (Planar Ally)**; TMind also has a new **Flying Ghoul** (Animate Dead) summon, and Kao's air elemental summon leveled up to a **level 11 Myrmidon**.

## Active Practical Buffs

### TMind

- Heroes' Feast
- Aid
- Longstrider
- Darkvision
- Blood of Lathander light aura (item)
- Lathander's Blessing resurrection resource (class feature, unused)
- Shield of Devotion extra spell slot (item)
- Undead-presence effect (item)
- **Partial ceremorphosis status** (new — see Extraction Notes)
- **Missing both Death Ward and Freedom of Movement** — both newly dropped this pass; recast before the next hard fight
- Speak with Dead recast flag no longer showing
- Still no Warding Bond — see Kao

### Lae'zel

- Heroes' Feast
- **Elixir of Bloodlust** (active)
- **Fresh temp-HP buff** (new, likely from the fight)
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
- **Death Ward** (new — first time active since his resurrection)
- **Freedom of Movement** (new — same)
- **Mage Armor** (new — same; all three standing gaps are now resolved)
- Longstrider
- Darkvision
- Absorb Elements cloak resource
- No longer shows the Warding Bond or Shovel-flag statuses from last snapshot

### Astarion

- Heroes' Feast
- Aid
- **Death Ward** (back — was missing for three snapshots)
- Freedom of Movement
- Longstrider
- Darkvision
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- No longer shows See Invisibility, Detect Thoughts, Potion of Animal Speaking, happy status, or Poison Resistance from last snapshot — likely just expired between passes

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support, Blood of Lathander light, and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active.
- Kao has the Absorb Elements cloak resource active.
- Astarion has Cat's Grace / Graceful Cloth and the Cloak of Displacement support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Kao's Death Ward, Freedom of Movement, and Mage Armor gaps are resolved** after persisting across four snapshots since his resurrection — all three are confirmed active now.
- **TMind now shows a partial-ceremorphosis status** (`TAD_PARTIAL_CEREMORPH`), the same status Lae'zel has carried since early in this campaign. This is a real, spoiler-sensitive story development, not an extraction artifact — noted here factually without narrative detail, consistent with how Lae'zel's has always been handled.
- TMind's Death Ward and Freedom of Movement are both genuinely absent from his status manager this pass (confirmed by direct re-check, not an extraction glitch) — he's now the only party member missing either.
- Astarion's several minor buffs from last snapshot (See Invisibility, Detect Thoughts, Potion of Animal Speaking, happy status, Poison Resistance) are gone — consistent with short-duration effects simply expiring over ~3 hours of play, not a readiness concern.
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
