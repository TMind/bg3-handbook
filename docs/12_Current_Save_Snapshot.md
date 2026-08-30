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

- Save name: `Campsite - 115h 34m`
- Save modified: `2026-08-30 01:29:40 +02:00`
- Synced into handbook: `2026-08-30 01:34:23 +02:00`
- Game version: `4.1.1.7398727` (unchanged since the last sync)
- Difficulty: `DifficultyMedium / RulesetLarian`
- Current region: `CTY_Main_A`

## Active Party

| Character | Level / build | XP | Current subregion | Practical note |
|---|---|---:|---|---|
| TMind | **Level 11** Cleric / Death Domain | 93,152 total; 17,152 into level | `CAMP_SUB` | +10,641 XP since last sync — a lot happened. **Death Ward and Freedom of Movement are both back** — no gap left on him. |
| Lae'zel | **Level 11** Fighter / Battle Master | 93,152 total; 17,152 into level | `CAMP_SUB` | Death Ward, Freedom of Movement, Heroes' Feast all active. Picked up the **Amulet of Windrider** (very rare) this pass. |
| Kao | **Level 11** Wizard / Conjuration School | 92,677 total; 16,677 into level | `LOW_SorcerousSundries_RamazithsTower_SUB` | Death Ward, Freedom of Movement, Mage Armor all still active. **Picked up Markoheshkir (legendary staff) and Robe of the Weave (very rare)** — see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md). |
| Astarion | **Level 11** Rogue / Thief | 92,507 total; 16,507 into level | `LOW_SorcerousSundries_RamazithsTower_SUB` | Death Ward and Freedom of Movement active. **Picked up Duellist's Prerogative (legendary rapier)** — a potential build fork away from dual daggers. Also now carries a **cursed status from the Tharchiate Codex** he apparently read. |

**The party is split across two locations**: Lae'zel and TMind are at camp, Astarion and Kao are at **Ramazith's Tower** (Sorcerous Sundries, Lower City). A huge amount happened since the last sync (+10,500 XP each) — this looks like a major shopping/looting stretch at the wizard's tower, given the legendary-tier gear that showed up on both Kao and Astarion. **Every previous buff gap is now resolved** — Death Ward, Freedom of Movement, and Mage Armor are active on all four for the first time this campaign. The one new gap: **Aid has dropped off everyone**, not previously a concern. Summons: the Cambion/Djinni Planar Ally is gone, replaced by a **Deva (Planar Ally)** — a different, higher-tier celestial — at camp with Lae'zel and TMind; Kao still has his Conjure Elemental (Air) summon with him at the tower.

## Active Practical Buffs

### TMind

- Heroes' Feast
- **Death Ward** (back)
- **Freedom of Movement** (back)
- Longstrider
- Blood of Lathander light aura (item)
- Lathander's Blessing resurrection resource (class feature, unused)
- Shield of Devotion extra spell slot (item)
- Undead-presence effect (item)
- Partial ceremorphosis status (unchanged from last snapshot)
- Fox's Cunning elixir effect
- **No longer shows Aid or Darkvision** — see Extraction Notes
- Still no Warding Bond

### Lae'zel

- Heroes' Feast
- **Elixir of Bloodlust** (active — note the last spare bottle is gone, see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md))
- Death Ward
- Freedom of Movement
- Killer's Sweetheart / critical-execution ring effect
- Partial ceremorphosis status
- **No longer shows Aid, Longstrider, Darkvision, or the temp-HP buff from last snapshot**

### Kao

- Heroes' Feast
- Death Ward
- Freedom of Movement
- Mage Armor
- Longstrider
- Warding Bond (received, back after being absent last snapshot)
- Absorb Elements cloak resource
- **Counterspell resource** (new — matches picking up the Staff of Interruption)
- An item-effect marker tied to a "Chromatic" item (new — matches picking up Markoheshkir)
- **No longer shows Aid or Darkvision**

### Astarion

- Heroes' Feast
- Death Ward
- Freedom of Movement
- Longstrider
- Cat's Grace / Graceful Cloth effect
- Cloak of Displacement (item)
- **Cursed status from the Tharchiate Codex** (new — see Extraction Notes)
- **No longer shows Aid or Darkvision**

## Confirmed Item-Sourced Buffs

- TMind has Shield of Devotion spell-slot support, Blood of Lathander light, and an undead-presence item effect active.
- Lae'zel has the Killer's Sweetheart / critical-execution ring support active.
- Kao has the Absorb Elements cloak resource active, plus new resources from Markoheshkir and the Staff of Interruption.
- Astarion has Cat's Grace / Graceful Cloth and the Cloak of Displacement support active.

## Extraction Notes

- The source save for generated snapshots is recorded in `tools/save-extract/source_manifest.json`.
- Active buff extraction is reliable because it reads the active character status managers directly.
- **Every previous buff gap is resolved this pass**: Death Ward and Freedom of Movement are active on all four (including TMind, who had newly lost both last snapshot), and Kao's Mage Armor is still holding.
- **New gap: Aid is missing from all four characters**, along with Darkvision. Both are typical "until long rest" utility buffs — likely just expired rather than a readiness concern, but worth recasting before the next hard fight regardless.
- **Astarion carries a cursed status from the Tharchiate Codex** (`CURSEDTOME_THARCHIATE_CODEX`) — this is the same Legendary book flagged as "lying uncollected in the world" two audits ago; he's evidently picked it up and read it since. The book trades a Constitution penalty for temp HP on long rest and a ghoul-summoning ability — a real, deliberate-feeling trade-off worth confirming was intentional.
- TMind's partial-ceremorphosis status (`TAD_PARTIAL_CEREMORPH`) is unchanged from last snapshot, still noted factually without narrative detail, consistent with how Lae'zel's has always been handled.
- An Act 3 story-state status flag (`TAD_PEACE_BREAKER`) is present on the whole party; omitted here as spoiler-sensitive story state rather than a practical buff.
- Inventory extraction works, but exact equipped-slot mapping still needs a separate pass; many carried items share the character position.
- Current hard-fight readiness is summarized in [Current Readiness Audit](14_Current_Readiness_Audit.md).
