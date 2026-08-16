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

**A real fight happened** (~3,500+ XP each) and buff coverage flipped in an unusual way: Kao's Death Ward, Freedom of Movement, and Mage Armor are **all active for the first time in four snapshots**, and Astarion's Death Ward is back — but **TMind picked up both of those same gaps himself**, newly missing Death Ward and Freedom of Movement. Net effect: TMind is now the only party member with any gap. The location changed to The Blushing Mermaid (Lower City), and the summon roster changed (Djinni Planar Ally, a new Flying Ghoul, and an upgraded level-11 air Myrmidon). One more item to flag: TMind now shows a partial-ceremorphosis status, the same one Lae'zel has carried since early on — noted factually, not narratively.

| Area | Status | Reason |
|---|---|---|
| Core party | ✅ Good | TMind, Lae'zel, Kao, and Astarion are grouped at `LOW_BlushingMermaid_SUB`; summons are a Djinni (Planar Ally), a Flying Ghoul, and a level-11 air Myrmidon. |
| Daily movement | ✅ Good | Longstrider is active on TMind, Lae'zel, Kao, and Astarion. |
| Maximum HP | ✅ Good | Aid and Heroes' Feast are active on all four, unchanged. |
| Death protection | ⚠️ Shifted, not resolved | Death Ward is now active on Lae'zel, Kao, **and Astarion** (all three gaps from last time are gone) — but it's newly missing on **TMind**, who had it every prior snapshot. |
| Control protection | ⚠️ Shifted, not resolved | Freedom of Movement is now active on Lae'zel, Kao, **and Astarion** — same pattern, newly missing only on **TMind**. |
| Burst resources | ✅ Good | Elixir of Bloodlust is still active on Lae'zel, plus a fresh temp-HP buff from the fight. |
| Stealth aura | ⚠️ Unchanged gap | Pass Without Trace is still not active on the party; re-apply before stealth approaches if wanted. |
| Healing synergy | ✅ Good | Blood of Lathander and Shield of Devotion effects are active on TMind. |
| Mage Armor (Kao) | ✅ Resolved | Active for the first time in four snapshots. |
| Gear redistribution | ⚠️ Mixed | The three moves from last time (crossbow/cloak/cloak) are confirmed done. But five *more* TMind items (Ring of Salving, Keepsake Ring, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb) relocated to an unidentified companion near camp this pass, and Murderous Cut drifted from Astarion to TMind — see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md). |

## Active Buff Coverage

**Markers:** ⭐⭐⭐ ✨

| Character | Confirmed useful buffs | Missing before hard fights |
|---|---|---|
| TMind | Heroes' Feast, Longstrider, Aid, Darkvision, Shield of Devotion spell slot, Blood of Lathander light | **Death Ward and Freedom of Movement** — both newly missing this pass; he's now the only party member with any daily-buff gap |
| Lae'zel | Heroes' Feast, Longstrider, Aid, Death Ward, Freedom of Movement, Darkvision, **Elixir of Bloodlust (active)**, fresh temp-HP buff, critical-execution ring | No major daily-buff gap detected |
| Kao | Heroes' Feast, Longstrider, Aid, **Death Ward (new)**, **Freedom of Movement (new)**, **Mage Armor (new)**, Darkvision, Absorb Elements resource | No major daily-buff gap detected — all three standing gaps resolved this pass |
| Astarion | Heroes' Feast, Longstrider, Aid, **Death Ward (back)**, Freedom of Movement, Darkvision, Cat's Grace, Cloak of Displacement | No major daily-buff gap detected |

> [!note] Pass Without Trace is no longer active on the party in this save (it covered everyone previously). Re-cast it before a stealth-sensitive approach if you want the bonus back.

## Available Camp-Buff Casters ^available-buff-casters

**Markers:** ⭐⭐⭐ ✨ 🎯

This table is about **spell access**, not currently active buffs. It answers who can provide useful pre-combat or camp-cast buffs before the party leaves camp.

| Character | Current role | Camp-buff spells or features they can provide | Practical note |
|---|---|---|---|
| TMind | Death Cleric 11 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement, **Heroes' Feast (now available)**; Divine Intervention: Arm Thy Servant if unused | Strong Cleric buffer, but using him as the active cleric means these spell slots come from the adventuring party. |
| Shadowheart | Camp Light Cleric 10 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement; Divine Intervention: Arm Thy Servant if unused | Best current camp source for Cleric buffs because she can spend camp spell slots and then leave the active party. Heroes' Feast requires Cleric 11 — TMind now qualifies, Shadowheart's own level is unconfirmed here. |
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
| Heroes' Feast | TMind (now Cleric 11) | Whole party and summons | **Now available** — TMind reached Cleric 11 this snapshot. Cast it at camp before a big fight; it's the party's new best pre-fight investment. |
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

Counts refreshed from the current `The Blushing Mermaid - 109h 15m` save (see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) for the full audit).

| Resource | Save count | Current holder pattern | Readiness call |
|---|---:|---|---|
| Scroll of Revivify | 10 | Kao 1, storage 9 | Unchanged across five snapshots; strong stock, put one on at least two active characters |
| Potion of Speed | 4 | Lae'zel 1, storage 3 | TMind's copy is no longer with him; still enough for one decisive Haste opener |
| Elixir of Bloodlust | 1 | Lae'zel 1 | Unchanged; only Lae'zel's spare bottle is left, on top of the active dose |
| Potion of Invisibility | 5 | Kao 1, storage 4 | Unchanged; still workable but don't over-rely on it |
| Scroll of Globe of Invulnerability | 2 | **Astarion 2** | Still on Astarion — he's the one who casts it, this hand-back still hasn't happened |
| Scroll of Conjure Elemental | 2 | **Astarion 1, storage 1** | Still on Astarion, same concern |
| Healing potions | 39 | TMind 6, Astarion 8, Lae'zel 4, Kao 4, storage 17 | Roughly steady through a real fight; nobody under-supplied |

## Gear and Synergy Checks ^gear-synergies

**Markers:** ⭐⭐ ✨ 🎯

| Check | Status | Note |
|---|---|---|
| Shadowheart weapon trick | ✅ Done | Devotee's Mace is still with TMind, unchanged. |
| Blood of Lathander | ✅ With TMind | Keep as the default cleric weapon unless the healing-aura plan is needed. |
| Devotee's Mace | ✅ With TMind | Use as a swap for Healing Incense Aura and on-heal item synergies. |
| Hellrider's Pride | ✅ With TMind | Works well with multi-target healing and rescue turns. |
| Spell Slot Restoration Amulet (Spellcrux Amulet) | ✅ With TMind | Strong day-extension tool; consider whether Kao needs it more before a caster-heavy fight. |
| The Whispering Promise | ✅ With TMind | Confirmed present — pairs with Devotee's Mace aura for concentration-free Bless-style value. |
| Sword of the Emperor (Lae'zel) | ✅ Rated ⭐⭐⭐ | +2 longsword, +2 to all saves vs spells — keep, strong vs Act 3's caster-heavy fights. |
| Boots of Psionic Movement (Lae'zel) | ✅ Rated ⭐⭐⭐ | Githyanki-only Fly + psychic damage rider — correctly replaced Boots of Speed on her. |
| Chancer's Carcanet (Lae'zel) | ✅ Rated ⭐⭐⭐ | Guaranteed Advantage on a save or attack, 1/long rest — keep. |
| Shadow of Menzoberranzan / Disintegrating Night Walkers (Astarion) | ✅ Rated ⭐⭐⭐ | On-demand Invisibility and free Misty Step + terrain immunity respectively — both strong, keep equipped. |
| Cerebral Citadel Gloves/Armour (Lae'zel) | ⚠️ Conditional | Gloves need a Frighten-causing maneuver (e.g. Menacing Attack) to matter; Armour's AC vs Adamantine Splint Armour is unconfirmed — verify both in game. |
| Hellfire Hand Crossbow / Shade-Slayer Cloak | ✅ Resolved | Moved to Astarion, as recommended — Hide/stealth-triggered effects fit him, not a melee cleric. |
| Vivacious Cloak | ✅ Resolved | Moved to Lae'zel, as recommended — guaranteed temp HP on initiative, better default than her Cindermoth Cloak. |
| Boots of Speed (TMind) | ✅ Resolved | Kept on TMind — he has no other boots, no reason to move them further. |
| Ring of Salving, Keepsake Ring, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb | ⚠️ New — location uncertain | All five moved off TMind this pass to an unidentified companion-type character near camp — not confirmed as simple camp storage. Ring of Salving especially is worth recovering (direct upgrade to his healing). See [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md). |
| Murderous Cut | ⚠️ New — wrong owner | Drifted from Astarion (a good fit) to TMind (no fit) this pass. Move back if easy. |
| Whispering Mask ×3 | ⚠️ New — unrated | New find, three identical copies on TMind. Not yet checked against bg3.wiki; carrying three is likely unintentional. |
| Kao's scroll library on Astarion | ⚠️ Unresolved | Globe of Invulnerability, Conjure Elemental, Bestow Curse, Crown of Madness, and Invisibility scrolls are still on Astarion, four snapshots after moving off Kao — see the Consumable Readiness table above. This has now survived multiple passes where other checklist items got done, so it may be deliberate rather than an oversight. |

Full effect text and sourcing for every item above is in [[13_Item_Inventory_Snapshot#^inventory-new-finds\|Item and Storage Snapshot § Item Ratings and Redistribution]].

## Before Leaving Camp ^before-leaving-camp

**Markers:** ⭐⭐⭐ ⏱️ ⚔️

The party is out of camp now (mid-fight-cycle, currently at The Blushing Mermaid) — good news is Kao and Astarion's buff gaps are resolved, so the list is much shorter. The bad news: TMind picked up two new gaps of his own.

1. **Recast Death Ward and Freedom of Movement on TMind** — both newly missing this pass, and he's now the only party member with any gap. Top priority.
2. ✅ Resolved: Kao's Death Ward, Freedom of Movement, and Mage Armor are all active — no action needed.
3. ✅ Resolved: Astarion's Death Ward is back — no action needed.
4. Consider casting **Heroes' Feast** before the next hard fight if it hasn't been used yet.
5. Move the Scroll of Globe of Invulnerability and Scroll of Conjure Elemental back to Kao (currently on Astarion) unless the handoff was deliberate — still not done, four snapshots running.
6. Move one Revivify scroll to TMind, Lae'zel, and Astarion; do not leave all emergency recovery on Kao.
7. ✅ Done: Hellfire Hand Crossbow, Shade-Slayer Cloak, and Vivacious Cloak moves from two snapshots ago are all confirmed.
8. Check on the five TMind items (Ring of Salving, Keepsake Ring, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb) that moved to an unidentified companion this pass — Ring of Salving in particular is worth recovering. Also move Murderous Cut back to Astarion.
9. Re-apply **Pass Without Trace** before a stealth approach if wanted (still not active this save).
10. Decide whether TMind starts with Blood of Lathander or swaps to Devotee's Mace for the healing-aura plan.

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
| Save name | The Blushing Mermaid - 109h 15m |
| Save modified | 2026-08-16 22:29:04 +02:00 |
| Synced into handbook | 2026-08-16 22:34:51 +02:00 |
| Game version | 4.1.1.7398727 |
| Difficulty | DifficultyMedium / RulesetLarian |
| Source record | `tools/save-extract/source_manifest.json` |

## Parser Notes

**Markers:** ⭐ ⚠️

- This audit used the current `.lsf` index, not a refreshed `Globals.lsx` text export.
- Active buff detection is reliable for the four named party members because it reads their current status managers.
- Character identity was confirmed by matching each `Character` node's exact `Translate` position against the position reported for that character in `SaveInfo.json`; a decoy/duplicate node can share the same coordinates (seen for Kao this pass), so the match was cross-checked against the `Level` field and `IsResurrected`/other distinguishing attributes before trusting it.
- Kao's `IsResurrected` flag is still set on his character node, but his Death Ward, Freedom of Movement, and Mage Armor are all now confirmed active — the flag staying set doesn't mean the gaps persist forever, just that the resurrection happened at some point.
- TMind's missing Death Ward and Freedom of Movement were double-checked directly against his raw status list (not inferred) — confirmed genuinely absent, not an extraction artifact.
- A distinct `Character` node was found near TMind's items this pass, with `PlayerData` (a companion-roster marker) and its own `IsResurrected` flag — likely a bench companion holding some of TMind's old gear, but not conclusively identified. Treated as "location uncertain" in the item snapshot rather than asserted as camp storage, per the lesson from the earlier storage mislabeling.
- The broader save contains many `DYING` statuses on old or non-active entities; the active-party status managers for the four named characters do not show `DYING` in this save.
- Item counts are reliable for practical stock checks, but exact equipped slots still need in-game confirmation.
- Camp storage and world/storage-like inventories are summarized as “elsewhere” rather than by raw container or position.
