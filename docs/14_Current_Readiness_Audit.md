---
title: "Current Readiness Audit"
aliases:
  - Readiness Audit
  - Current Party Readiness
  - Hard Fight Readiness
tags:
  - bg3
  - handbook
  - save
  - readiness
  - preparation
---

# Current Readiness Audit

This note summarizes whether the current save is ready for a hard fight. It is based on the latest synced save and stays spoiler-light: no quest-state analysis, map coordinates, or story flags.

> [!info] Navigation
> Previous: [Current Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) | Home: [Baldur's Gate 3 Practical Handbook](../README.md) | Next: [Appendix](15_Appendix.md)

## Contents

| Need | Jump to |
|---|---|
| See the current result | [[14_Current_Readiness_Audit#^readiness-verdict\|Verdict]] |
| Compare current character buffs | [[#Active Buff Coverage\|Active Buff Coverage]] |
| Finish the camp routine | [[14_Current_Readiness_Audit#^before-leaving-camp\|Before Leaving Camp]] |
| Prepare the next serious encounter | [[14_Current_Readiness_Audit#^before-hard-fight\|Before a Hard Fight]] |
| Assign buff casters | [[14_Current_Readiness_Audit#^available-buff-casters\|Available Casters]] · [[14_Current_Readiness_Audit#^optimal-buff-assignment\|Optimal Assignment]] |
| Check supplies and equipment | [[14_Current_Readiness_Audit#^consumable-readiness\|Consumables]] · [[14_Current_Readiness_Audit#^gear-synergies\|Gear and Synergies]] |
| Verify save provenance | [[14_Current_Readiness_Audit#^readiness-source\|Source]] |
| Understand extraction limits | [[#Parser Notes\|Parser Notes]] |

## Verdict ^readiness-verdict

**Markers:** ⭐⭐⭐ ⚠️ ⚔️

The party is **mostly prepared and close to hard-fight ready**.

| Area | Status | Reason |
|---|---|---|
| Core party | ✅ Good | TMind, Lae'zel, Kao, and Astarion are grouped in `WYR_Fortress_SUB` (Wyrm's Rock Fortress); a Flying Ghoul summon and a quasit are also nearby. |
| Daily movement | ✅ Good | Longstrider is active on TMind, Lae'zel, Kao, and Astarion. |
| Maximum HP | ⚠️ Minor gap | Aid level 3 is active on TMind, Kao, and Astarion, but still not detected on Lae'zel. |
| Death protection | ✅ Good | Death Ward is active on TMind, Lae'zel, Kao, and Astarion. |
| Control protection | ✅ Good | Freedom of Movement is active on TMind, Lae'zel, Kao, and Astarion. |
| Burst resources | ✅ Good | **Elixir of Bloodlust is now active on Lae'zel** (previous gap resolved). |
| Stealth aura | ⚠️ Changed | Pass Without Trace is no longer active on the party; re-apply before stealth approaches if wanted. |
| Healing synergy | ✅ Good | Blood of Lathander and Shield of Devotion effects are active on TMind. |

## Active Buff Coverage

**Markers:** ⭐⭐⭐ ✨

| Character | Confirmed useful buffs | Missing before hard fights |
|---|---|---|
| TMind | Longstrider, Aid level 3, Death Ward, Freedom of Movement, Warding Bond, Darkvision, Shield of Devotion spell slot, Blood of Lathander light | No major daily-buff gap detected |
| Lae'zel | Longstrider, Death Ward, Freedom of Movement, Darkvision, **Elixir of Bloodlust (active)**, critical-execution ring, Astral Knowledge (CHA) | Aid |
| Kao | Longstrider, Aid level 3, Death Ward, Freedom of Movement, Mage Armor, Warding Bond, Darkvision, Absorb Elements resource, Detect Thoughts, Animal Speaking, Shovel flag | No major daily-buff gap detected |
| Astarion | Longstrider, Aid level 3, Death Ward, Freedom of Movement, Darkvision, Cat's Grace, Cloak of Displacement, happy status | No major daily-buff gap detected |

> [!note] Pass Without Trace is no longer active on the party in this save (it covered everyone previously). Re-cast it before a stealth-sensitive approach if you want the bonus back.

## Available Camp-Buff Casters ^available-buff-casters

**Markers:** ⭐⭐⭐ ✨ 🎯

This table is about **spell access**, not currently active buffs. It answers who can provide useful pre-combat or camp-cast buffs before the party leaves camp.

| Character | Current role | Camp-buff spells or features they can provide | Practical note |
|---|---|---|---|
| TMind | Death Cleric 10 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement; Divine Intervention: Arm Thy Servant if unused | Strong Cleric buffer, but using him as the active cleric means these spell slots come from the adventuring party. Heroes' Feast requires Cleric 11. |
| Shadowheart | Camp Light Cleric 10 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement; Divine Intervention: Arm Thy Servant if unused | Best current camp source for Cleric buffs because she can spend camp spell slots and then leave the active party. Heroes' Feast requires Cleric 11. |
| Kao | Human Wizard 10 | Longstrider, Mage Armor, Darkvision, See Invisibility; short utility such as Feather Fall, Enhance Leap, Invisibility if known and prepared | Excellent Wizard utility buffer. Does not naturally cover Aid, Warding Bond, Death Ward, Freedom of Movement, or Heroes' Feast. |
| Gale | Camp Wizard, if used | Longstrider, Mage Armor, Darkvision, See Invisibility; short utility if known and prepared | Same practical job as Kao: free the active Wizard from routine utility casting. |
| Bard hireling | Bard support | Longstrider; Freedom of Movement at Bard 7; Death Ward only if selected through Magical Secrets at Bard 10; Song of Rest as a day-extension feature | Good support hireling, but not a full camp buffer unless multiclassed into Cleric/Wizard. |
| Lae'zel | Battle Master Fighter | None from the current build | Receives buffs; does not provide spell-based camp buffs. |
| Astarion | Thief Rogue | None from the current build | Receives buffs; does not provide spell-based camp buffs unless rebuilt into a caster subclass or multiclass. |

For exact spellbook state, verify prepared spells in game before relying on a caster. Clerics can usually prepare the listed Cleric buffs from their class list, while Wizards must have learned the spell and prepared it, and Bards must have chosen the spell as a known spell or Magical Secrets pick.

## Optimal Buff-Spell Assignment ^optimal-buff-assignment

**Markers:** ⭐⭐⭐ ⏱️ ✨ 🎯

Default principle: let camp characters pay for daily utility first, then keep the active party's spell slots for combat, reactions, and emergencies.

| Buff or setup | Best caster | Main targets | Why this assignment is best |
|---|---|---|---|
| Longstrider | Bard hireling first; Gale or Kao as backup | TMind, Lae'zel, Kao, Astarion, summons | Ritual casting makes this cheap. A camp Bard or camp Wizard keeps Kao's active resources cleaner. |
| Mage Armor | Gale if available; Kao as backup | Kao if unarmored; eligible summons or unarmored allies | Wizard utility job. Skip armored characters because the spell does nothing for them. |
| Darkvision | Gale or Kao | Anyone without natural or item-based Darkvision | Useful exploration comfort. Prioritize the party member who actually lacks Darkvision. |
| See Invisibility | Gale or Kao | Kao or the character expected to reveal invisible enemies | Keep this on the scout/caster who is most likely to notice or expose targets. |
| Aid | Shadowheart first; TMind only as backup | All four active characters, then summons if included | Shadowheart can spend camp slots while TMind keeps his Cleric slots for the active day. Upcast when practical. |
| Protection from Poison | Shadowheart first; TMind only if poison risk is high and she is unavailable | Frontline and anyone likely to fail poison saves | Situational daily buff. Do not spend time on it every day unless the area calls for it. |
| Warding Bond | Shadowheart, selectively | Lae'zel first; optionally TMind or Astarion for a hard fight | Strong but risky because Shadowheart receives shared damage. Use on one key target unless her HP and healing setup are managed. |
| Death Ward | Shadowheart first; Bard 10 Magical Secrets or TMind as backup | Lae'zel, TMind, Kao, then Astarion | Best insurance on characters who must not drop early. Use TMind only if camp sources are exhausted. |
| Freedom of Movement | Bard hireling if Bard 7+; Shadowheart second; TMind backup | Lae'zel and Astarion first, then TMind/Kao if control is expected | Bard is a clean source if available. Prioritize melee and mobility-dependent characters. |
| Heroes' Feast | Future Shadowheart or TMind at Cleric 11 | Whole party and summons | Not available from current Cleric 10 setup. Make this the next major daily-buff upgrade. |
| Song of Rest | Bard hireling | Whole party after short-rest resources are spent | Not a buff spell, but it extends the adventuring day and should be used after meaningful short-rest value is missing. |

### Recommended Daily Caster Roles

| Character | Daily job |
|---|---|
| Shadowheart | Primary Cleric camp buffer: Aid, Death Ward, Freedom of Movement, Warding Bond only when worth the risk. |
| Bard hireling | Longstrider routine, Freedom of Movement at Bard 7+, Death Ward only if Bard 10 Magical Secrets selected it, Song of Rest for day extension. |
| Gale | Camp Wizard utility: Longstrider backup, Mage Armor, Darkvision, See Invisibility. |
| Kao | Active Wizard utility backup only; avoid spending his slots if Gale or Bard can cover the same setup. |
| TMind | Active Cleric fallback; use his slots only when Shadowheart cannot cover the buff or the fight needs immediate recasting. |
| Lae'zel | Main recipient for movement, Aid, Death Ward, Freedom of Movement, and selective Warding Bond. |
| Astarion | Recipient for Longstrider, Aid, Death Ward, Freedom of Movement when control or restraint is expected. |

## Consumable Readiness ^consumable-readiness

**Markers:** ⭐⭐⭐ 🍷 ⚔️

Counts refreshed from the current `Wyrms Rock Fortress - 100h 29m` save (see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) for the full audit).

| Resource | Save count | Current holder pattern | Readiness call |
|---|---:|---|---|
| Scroll of Revivify | 10 | Kao 1, storage 9 | Strong stock; put one on at least two active characters |
| Potion of Speed | 6 | Lae'zel 2, TMind 1, storage 3 | Enough for a decisive Haste opener or two |
| Elixir of Bloodlust | 3 | Lae'zel 1 (active), TMind 1, storage 1 | Already active on Lae'zel |
| Potion of Invisibility | 10 | Kao 2, storage 8 | Move a couple to Astarion |
| Scroll of Globe of Invulnerability | 2 | Kao 2 | Excellent boss-defense stock |
| Scroll of Conjure Elemental | 3 | Kao 1, storage 2 | Good summon stock |
| Healing potions | 43 | Astarion 7, TMind 6, Lae'zel 4, Kao 3, storage 23 | Well distributed; nobody under-supplied |

## Gear and Synergy Checks ^gear-synergies

**Markers:** ⭐⭐ ✨ 🎯

| Check | Status | Note |
|---|---|---|
| Shadowheart weapon trick | ✅ Done | Devotee's Mace is now with TMind. |
| Blood of Lathander | ✅ With TMind | Keep as the default cleric weapon unless the healing-aura plan is needed. |
| Devotee's Mace | ✅ With TMind | Use as a swap for Healing Incense Aura and on-heal item synergies. |
| Hellrider's Pride | ✅ With TMind | Works well with multi-target healing and rescue turns. |
| Cloak of Protection | ✅ With TMind | Good defensive pickup already consolidated. |
| Spell Slot Restoration Amulet | ✅ With TMind | Strong day-extension tool; consider whether Kao needs it more before a caster-heavy fight. |
| Whispering Promise style ring | ⚠️ Not confirmed in this pass | If available in game, pair it with Devotee's Mace aura for concentration-free Bless-style value. |

## Before Leaving Camp ^before-leaving-camp

**Markers:** ⭐⭐⭐ ⏱️ ⚔️

1. Use Shadowheart or TMind to cast or refresh **Aid** so Lae'zel is included (still the one gap).
2. Move one Revivify scroll to TMind, Lae'zel, and Astarion; do not leave all emergency recovery on Kao.
3. Move one or two Potion of Invisibility items to Astarion.
4. Give Lae'zel a small healing-potion stack.
5. Bloodlust is already active on Lae'zel this save — no action needed unless it is consumed before the fight.
6. Re-apply **Pass Without Trace** before a stealth approach if wanted (not active this save).
7. Decide whether TMind starts with Blood of Lathander or swaps to Devotee's Mace for the healing-aura plan.

## Before a Hard Fight ^before-hard-fight

**Markers:** ⭐⭐⭐ ⚔️ 🎯

| Step | Action |
|---|---|
| 1 | Confirm everyone who should fight is actually grouped and nearby. |
| 2 | Put turn-based mode on before throwing short-duration potions. |
| 3 | If using Potion of Speed on multiple characters, throw it only immediately before combat. |
| 4 | Put Globe of Invulnerability and Conjure Elemental scrolls on Kao's hotbar. |
| 5 | Put invisibility tools, anti-caster arrows, and poisons on Astarion. |
| 6 | Put Bloodlust / Colossus elixir choice on Lae'zel before initiative matters. |
| 7 | Keep TMind's Divine Intervention unused unless the fight collapses. |

## Source ^readiness-source

**Markers:** ⭐⭐ ⏱️

| Field | Current value |
|---|---|
| Save name | Wyrms Rock Fortress - 100h 29m |
| Save modified | 2026-07-21 01:26:37 +02:00 |
| Synced into handbook | 2026-07-22 00:29:42 +02:00 |
| Game version | 4.1.1.7209685 |
| Difficulty | DifficultyMedium / RulesetLarian |
| Source record | `tools/save-extract/source_manifest.json` |

## Parser Notes

**Markers:** ⭐ ⚠️

- This audit used the current `.lsf` index, not a refreshed `Globals.lsx` text export.
- Active buff detection is reliable for the four named party members because it reads their current status managers.
- The broader save contains many `DYING` statuses on old or non-active entities; the active-party status managers for the four named characters do not show `DYING` in this save.
- Item counts are reliable for practical stock checks, but exact equipped slots still need in-game confirmation.
- Camp storage and world/storage-like inventories are summarized as “elsewhere” rather than by raw container or position.
