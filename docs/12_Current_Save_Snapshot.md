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

- Save name: `Campsite - 119h 03m`
- Save modified: `2026-08-31 19:40:51 +02:00`
- Synced into handbook: `2026-08-31 21:39:47 +02:00`
- Game version: `4.1.1.7398727` (unchanged since the last sync)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | **Level 12** Cleric / Death Domain | 101,877 total | `CAMP_SUB` | Leveled up since last sync. Still missing Death Ward — unchanged gap. |
| Lae'zel | **Level 12** Fighter (Battle Master) / Cleric (War Domain) | 101,707 total | `CAMP_SUB` | **Respecced into a multiclass** — the save's own class list now shows Fighter + Cleric (War Domain), confirming [[11_Main_Character_Builds#^laezel-build\|the newly-decided build]]. Lost every buff she had: no Death Ward, Freedom of Movement, Longstrider, Heroes' Feast, or Aid — likely just needs rebuffing after the respec. |
| Kao | **Level 12** Wizard / Conjuration School | 101,232 total | `LOW_BaldursMouth_Basement_SUB` | Unchanged from last sync — still has Death Ward, Freedom of Movement, Mage Armor, Aid. |
| Astarion | **Level 12** Rogue / Thief | 101,062 total | `LOW_BaldursMouth_Basement_SUB` | Unchanged from last sync — still has Death Ward and Freedom of Movement, still missing Aid, still carries the Tharchiate Codex curse. |

**TMind and Lae'zel moved from Lower City back to camp**; Kao and Astarion are unchanged at Baldur's Mouth Basement — the party is still split, just along the same lines as before with the Lower City pair now at camp instead. No inventory changes anywhere in the save this pass — every character's item list is byte-for-byte identical to last sync; only levels, class list, position, and buffs moved. Summons: the Deva (Planar Ally) is still with the camp pair.

## Active Practical Buffs

### TMind

- Heroes' Feast
- Aid
- Freedom of Movement
- Longstrider
- Shield of Devotion extra spell slot (item)
- Undead-presence effect (item)
- Partial ceremorphosis status (unchanged)
- **Still missing Death Ward** — unchanged gap from last sync

### Lae'zel

- Killer's Sweetheart / critical-execution ring effect
- Elixir of Bloodlust (active again — no new bottle found in inventory this pass, likely just recast from an existing dose)
- An Oil of Bane-style weapon buff (`ALCH_OIL_BANE`)
- Partial ceremorphosis status (unchanged)
- **Lost everything else**: Death Ward, Freedom of Movement, Longstrider, Heroes' Feast, and Aid are all gone — a full buff wipe, most likely tied to the respec rather than a readiness failure. Rebuff before the next fight.

### Kao

- Heroes' Feast
- Death Ward
- Freedom of Movement
- Mage Armor
- Aid
- Absorb Elements cloak resource
- Counterspell resource (Staff of Interruption)
- Markoheshkir's item-effect marker
- Benign Transposition used marker (unchanged)
- A Greater Elixir of Meditation effect (unchanged)
- No longer shows Longstrider or Warding Bond as active statuses (both present last sync)

### Astarion

- Heroes' Feast
- Death Ward
- Freedom of Movement
- Longstrider
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- Tharchiate Codex curse status (still present, same renamed ID as last sync)
- A weapon-oil damage buff (unchanged)
- **Still missing Aid**

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support and a weapon oil active; otherwise unbuffed.
- Kao has the Absorb Elements cloak resource, Markoheshkir's resource, and Counterspell (Staff of Interruption) active.
- Astarion has Cat's Grace / Graceful Cloth, the Cloak of Displacement support, and a weapon oil active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Lae'zel's multiclass is now save-confirmed**, not just player-reported: `SaveInfo.json`'s `Classes` list for her shows `[{"Main": "Fighter", "Sub": "BattleMaster"}, {"Main": "Cleric", "Sub": "WarDomain"}]`. This save format doesn't expose a per-class level split, so the exact Fighter 11/Cleric 1 division (versus some other split summing to 12) is inferred from context, not directly read.
- **Known spells and maneuvers remain completely unreadable from this save index** — checked directly again this pass (searched the full `Globals.lsf` index for "maneuver" and "Rally", zero matches). Only items, positions, and active statuses are extractable; anything about which specific maneuvers or spells a character knows is player-reported only.
- **Lae'zel's total buff wipe** (Death Ward, Freedom of Movement, Longstrider, Heroes' Feast, Aid all gone at once) is unusual enough to flag — the most likely explanation is the multiclass respec itself, not four coincidental buff expirations landing on the same character at once.
- No inventory changes were found anywhere in the save this pass (verified by comparing every item record against the previous sync) — worth noting since two previously-flagged "missing" items, The Joltshooter and Gleamdance Dagger, are confirmed to have been sitting in storage the whole time; that earlier "not found anywhere" claim was wrong, not a new development. See [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md).
- TMind's partial-ceremorphosis status (`TAD_PARTIAL_CEREMORPH`) is unchanged, still noted factually without narrative detail.
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
