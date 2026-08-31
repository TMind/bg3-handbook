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

- Save name: `Lower City - 118h 27m`
- Save modified: `2026-08-31 01:13:19 +02:00`
- Synced into handbook: `2026-08-31 08:42:08 +02:00`
- Game version: `4.1.1.7398727` (unchanged since the last sync)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | **Level 11** Cleric / Death Domain | 101,877 total; 1,877 into level | `LOW_City_SUB` | **Has enough XP for Level 12 but hasn't leveled up yet** — go through the level-up screen. Lost Death Ward this pass; still has Freedom of Movement. |
| Lae'zel | **Level 11** Fighter / Battle Master | 101,707 total; 1,707 into level | `LOW_City_SUB` | **Also eligible for Level 12, not yet claimed.** Lost Death Ward and Longstrider. **Reaper's Embrace is now confirmed in her own inventory** — no longer a mystery-companion item. |
| Kao | **Level 12** Wizard / Conjuration School | 101,232 total | `LOW_BaldursMouth_Basement_SUB` | Already leveled to 12. Still has Death Ward, Freedom of Movement, Mage Armor, Warding Bond. Used Benign Transposition (level-6 Conjuration feature) at some point this pass. |
| Astarion | **Level 12** Rogue / Thief | 101,062 total | `LOW_BaldursMouth_Basement_SUB` | Already leveled to 12. Still has Death Ward and Freedom of Movement. Tharchiate Codex curse status is still present (internal ID changed from `CURSEDTOME_THARCHIATE_CODEX` to `CURSEDTOME_THARCHIATE_TECHNICAL` — likely just a tracking-marker rename, not a new effect). |

**The party has partly regrouped, but the split flipped**: TMind and Lae'zel are together in **Lower City** proper; Kao and Astarion are together at **Baldur's Mouth Basement**, a different spot than last pass's Ramazith's Tower. Kao and Astarion have already leveled to 12; TMind and Lae'zel have the XP for it but the save still shows them at 11 — the level-up screen just hasn't been used for them yet. **Death Ward split down location lines**: Kao and Astarion (Baldur's Mouth) still have it, TMind and Lae'zel (Lower City) both lost it. **Aid is now split too**: Kao and TMind have it, Astarion and Lae'zel don't. Freedom of Movement and Heroes' Feast remain universal across all four. Longstrider dropped off Lae'zel specifically. Summons: the Deva (Planar Ally) is still with the Lower City pair; Kao's Conjure Elemental (Air) summon is no longer active.

## Active Practical Buffs

### TMind

- Heroes' Feast
- **Aid** (back)
- Freedom of Movement
- Longstrider
- Shield of Devotion extra spell slot (item)
- Undead-presence effect (item)
- Partial ceremorphosis status (unchanged)
- **No longer shows Death Ward** — lost this pass, see Extraction Notes
- No longer shows Blood of Lathander's light aura as an active status (item is still carried — likely just not the equipped weapon right now)

### Lae'zel

- Heroes' Feast
- Freedom of Movement
- Killer's Sweetheart / critical-execution ring effect
- An Oil of Bane-style weapon buff (`ALCH_OIL_BANE`) — applied to her weapon, imposes a save penalty on hit
- Partial ceremorphosis status (unchanged)
- **No longer shows Death Ward, Longstrider, or Elixir of Bloodlust** — the elixir's active dose finally ran out with no spare bottle anywhere in the save (confirmed again this pass)

### Kao

- Heroes' Feast
- Death Ward
- Freedom of Movement
- Mage Armor
- Warding Bond (received)
- **Aid**
- Absorb Elements cloak resource
- Counterspell resource (Staff of Interruption)
- Markoheshkir's item-effect marker
- Benign Transposition used marker (level-6 Conjuration feature — self/ally teleport swap)
- A Greater Elixir of Meditation effect (short-rest-style recovery)
- No longer shows Longstrider as an active status

### Astarion

- Heroes' Feast
- Death Ward
- Freedom of Movement
- Longstrider
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- Tharchiate Codex curse status (still present, ID renamed — see Extraction Notes)
- A weapon-oil damage buff (`ALCH_OIL_DAMAGEATTACKBUFF`) — generic oil name, exact oil unconfirmed
- **No longer shows Aid**

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active, plus a new weapon oil (Bane-style).
- Kao has the Absorb Elements cloak resource, Markoheshkir's resource, and Counterspell (Staff of Interruption) active.
- Astarion has Cat's Grace / Graceful Cloth, the Cloak of Displacement support, and a weapon oil active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **TMind and Lae'zel have enough total XP for Level 12** (both over the 100,000 threshold) but the save's `Level` field still shows 11 for both, while Kao and Astarion — with *less* total XP — already show Level 12. The most likely explanation: Kao and Astarion have already gone through the in-game level-up screen and TMind/Lae'zel haven't yet, not an extraction error. Worth confirming in game.
- **Death Ward and Aid coverage now splits along the party's physical location** rather than by character — worth checking whether this is because different casters are covering each subgroup, or because Death Ward simply wasn't recast before the party split.
- **Astarion's Tharchiate Codex curse status ID changed** from `CURSEDTOME_THARCHIATE_CODEX` to `CURSEDTOME_THARCHIATE_TECHNICAL` between snapshots. Treated as the same underlying curse (BG3 statuses commonly pair a display status with an internal `_TECHNICAL` tracking marker) rather than a new effect, but flagged since it wasn't confirmed against bg3.wiki this pass.
- TMind's partial-ceremorphosis status (`TAD_PARTIAL_CEREMORPH`) is unchanged, still noted factually without narrative detail.
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position. This pass surfaced several TMind and Kao items that were apparently already in their inventories in prior snapshots but hadn't been listed in [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) — a coverage gap in past audits, not new acquisitions, corrected this pass.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
