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

The party is **mostly prepared but has two real gaps introduced by Kao's recent death and resurrection** — Death Ward and Freedom of Movement need re-casting on him, and Freedom of Movement is also missing on TMind.

| Area | Status | Reason |
|---|---|---|
| Core party | ✅ Good | TMind, Lae'zel, Kao, and Astarion are grouped in `LOW_Sewers_SUB` (Lower City sewers); a Conjure Elemental (Air) summon is also nearby. |
| Daily movement | ✅ Good | Longstrider is active on TMind, Lae'zel, Kao, and Astarion. |
| Maximum HP | ✅ Good | **Aid is now active on all four** — the Lae'zel gap from the previous snapshot is resolved. |
| Death protection | ⚠️ New gap | Death Ward is active on TMind, Lae'zel, and Astarion, but **not on Kao** — almost certainly because he was recently resurrected (status effects clear on death) and it hasn't been recast. |
| Control protection | ⚠️ New gap | Freedom of Movement is only active on Lae'zel and Astarion — **TMind and Kao are both missing it**. Recast before anything that grapples, paralyzes, or webs. |
| Burst resources | ✅ Good | Elixir of Bloodlust is still active on Lae'zel, with a spare bottle in her inventory. |
| Stealth aura | ⚠️ Unchanged gap | Pass Without Trace is still not active on the party; re-apply before stealth approaches if wanted. |
| Healing synergy | ✅ Good | Blood of Lathander and Shield of Devotion effects are active on TMind. |
| Mage Armor (Kao) | ⚠️ New gap | Not active — another casualty of the resurrection. Recast before relying on his AC. |

## Active Buff Coverage

**Markers:** ⭐⭐⭐ ✨

| Character | Confirmed useful buffs | Missing before hard fights |
|---|---|---|
| TMind | Longstrider, Aid, Death Ward, Darkvision, Shield of Devotion spell slot, Blood of Lathander light, Speak with Dead (recast available) | **Freedom of Movement** (no longer detected) |
| Lae'zel | Longstrider, Aid, Death Ward, Freedom of Movement, Darkvision, **Elixir of Bloodlust (active)**, critical-execution ring | No major daily-buff gap detected |
| Kao | Longstrider, Aid, Warding Bond, Darkvision, Absorb Elements resource, Shovel flag | **Death Ward, Freedom of Movement, and Mage Armor** — all missing since his recent resurrection |
| Astarion | Longstrider, Aid, Death Ward, Freedom of Movement, Darkvision, Cat's Grace, Cloak of Displacement, Detect Thoughts, happy status | No major daily-buff gap detected |

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

Counts refreshed from the current `QuickSave_186` save, Lower City sewers (see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) for the full audit).

| Resource | Save count | Current holder pattern | Readiness call |
|---|---:|---|---|
| Scroll of Revivify | 10 | Kao 1, storage 9 | Unchanged; strong stock, put one on at least two active characters |
| Potion of Speed | 4 | TMind 1, Lae'zel 1, storage 2 | Down from 6; still enough for one decisive Haste opener |
| Elixir of Bloodlust | 1 | Lae'zel 1 | Down from 3; only Lae'zel's spare bottle is left, on top of the active dose |
| Potion of Invisibility | 5 | Kao 1, storage 4 | Down from 10 (half used); still workable but don't over-rely on it |
| Scroll of Globe of Invulnerability | 2 | Kao 2 | Unchanged; excellent boss-defense stock |
| Scroll of Conjure Elemental | 2 | Kao 1, storage 1 | Down from 3; one more summon available |
| Healing potions | 39 | Astarion 7, TMind 6, Lae'zel 4, Kao 4, storage 18 | Down slightly from 43; still well distributed, nobody under-supplied |

## Gear and Synergy Checks ^gear-synergies

**Markers:** ⭐⭐ ✨ 🎯

| Check | Status | Note |
|---|---|---|
| Shadowheart weapon trick | ✅ Done | Devotee's Mace is still with TMind, unchanged. |
| Blood of Lathander | ✅ With TMind | Keep as the default cleric weapon unless the healing-aura plan is needed. |
| Devotee's Mace | ✅ With TMind | Use as a swap for Healing Incense Aura and on-heal item synergies. |
| Hellrider's Pride | ✅ With TMind | Works well with multi-target healing and rescue turns. |
| Cloak of Protection | ✅ With TMind | Good defensive pickup already consolidated. |
| Spell Slot Restoration Amulet (Spellcrux Amulet) | ✅ With TMind | Strong day-extension tool; consider whether Kao needs it more before a caster-heavy fight. |
| The Whispering Promise | ✅ With TMind | Confirmed present — pairs with Devotee's Mace aura for concentration-free Bless-style value. |
| New gear picked up since the last audit | ⚠️ Not evaluated | Sword of the Emperor (Lae'zel), a Cerebral Citadel armour/gloves set (Lae'zel), Boots of Psionic Movement (Lae'zel, replacing Boots of Speed), and several other named items landed on TMind, Kao, and Astarion — see [[13_Item_Inventory_Snapshot#^inventory-new-finds\|Item and Storage Snapshot § Notable New Finds]] for the full list. None of these have confirmed effects or ratings yet. |

## Before Leaving Camp ^before-leaving-camp

**Markers:** ⭐⭐⭐ ⏱️ ⚔️

1. **Recast Death Ward and Freedom of Movement on Kao** — both dropped when he was resurrected and haven't come back yet. This is the top priority this snapshot.
2. **Recast Freedom of Movement on TMind** — also missing, unrelated to Kao's resurrection.
3. Recast **Mage Armor on Kao** before relying on his AC.
4. Aid is now active on all four — no action needed (previous Lae'zel gap is resolved).
5. Move one Revivify scroll to TMind, Lae'zel, and Astarion; do not leave all emergency recovery on Kao.
6. Move the Boots of Speed sitting uselessly on TMind's position to whoever needs the mobility — Lae'zel currently has Boots of Psionic Movement instead; confirm that swap was intentional.
7. Re-apply **Pass Without Trace** before a stealth approach if wanted (still not active this save).
8. Decide whether TMind starts with Blood of Lathander or swaps to Devotee's Mace for the healing-aura plan.

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
| Save name | QuickSave_186 |
| Save modified | 2026-08-09 23:18:49 +02:00 |
| Synced into handbook | 2026-08-10 00:12:00 +02:00 |
| Game version | 4.1.1.7398727 |
| Difficulty | DifficultyMedium / RulesetLarian |
| Source record | `tools/save-extract/source_manifest.json` |

## Parser Notes

**Markers:** ⭐ ⚠️

- This audit used the current `.lsf` index, not a refreshed `Globals.lsx` text export.
- Active buff detection is reliable for the four named party members because it reads their current status managers.
- Character identity was confirmed by matching each `Character` node's exact `Translate` position against the position reported for that character in `SaveInfo.json`; a decoy/duplicate node can share the same coordinates (seen for Kao this pass), so the match was cross-checked against the `Level` field and `IsResurrected`/other distinguishing attributes before trusting it.
- Kao's `IsResurrected` flag is set on his character node — likely the source of the missing Death Ward, Freedom of Movement, and Mage Armor this pass, since status effects clear on death.
- The broader save contains many `DYING` statuses on old or non-active entities; the active-party status managers for the four named characters do not show `DYING` in this save.
- Item counts are reliable for practical stock checks, but exact equipped slots still need in-game confirmation.
- Camp storage and world/storage-like inventories are summarized as “elsewhere” rather than by raw container or position.
