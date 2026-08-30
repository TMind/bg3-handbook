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

**Best buff coverage this campaign, but the party is split, and three Legendary-tier items just landed.** A huge stretch of play happened (~+10,500 XP each) — the whole party is now Level 11, back to full health on daily buffs, and Kao/Astarion each picked up a Legendary-rarity weapon at Ramazith's Tower. The catch: TMind and Lae'zel are at **camp**, while Kao and Astarion are still at the **tower** — they are not grouped, so this is not "ready for a hard fight" as-is, it's "ready once reunited." One new gap appeared (Aid, party-wide), and Astarion picked up a real curse from a book he read.

| Area | Status | Reason |
|---|---|---|
| Core party | ⚠️ Split | TMind and Lae'zel are at `CAMP_SUB`; Kao and Astarion are at `LOW_SorcerousSundries_RamazithsTower_SUB`. Regroup before any hard fight. |
| Daily movement | ✅ Good | Longstrider is active on TMind, Lae'zel, Kao, and Astarion. |
| Death protection | ✅ Resolved | Death Ward is active on **all four** for the first time this campaign. |
| Control protection | ✅ Resolved | Freedom of Movement is active on **all four** for the first time this campaign. |
| Mage Armor (Kao) | ✅ Good | Still holding, unchanged. |
| Maximum HP | ⚠️ New gap | **Aid has dropped off all four characters** — previously always covered, now needs recasting before a hard fight. |
| Stealth aura | ⚠️ Unchanged gap | Pass Without Trace is still not active on the party. |
| Burst resources | 🚨 Depleted | **Elixir of Bloodlust is completely gone from the save** — Lae'zel's active dose has nothing left to refill it with. |
| New status | ⚠️ Needs a decision | Astarion carries a curse from reading a copy of The Tharchiate Codex (Constitution penalty for temp HP + a ghoul-summon feature) — confirm this was intentional; TMind holds two more unread copies. |
| Summons | ℹ️ Changed | The Cambion/Djinni Planar Ally was replaced by a **Deva (Planar Ally)** at camp; Kao's Conjure Elemental (Air) summon is still with him at the tower. |
| New gear | ✅ Big upgrade | Kao: Markoheshkir (Legendary staff) + Robe of the Weave. Astarion: Duellist's Prerogative (Legendary rapier) — a real build-fork decision, not just an upgrade. See [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md). |

## Active Buff Coverage

**Markers:** ⭐⭐⭐ ✨

| Character | Confirmed useful buffs | Missing before hard fights |
|---|---|---|
| TMind | Heroes' Feast, Longstrider, **Death Ward**, **Freedom of Movement**, Shield of Devotion spell slot, Blood of Lathander light | **Aid** — new gap, shared by the whole party |
| Lae'zel | Heroes' Feast, Longstrider, Death Ward, Freedom of Movement, critical-execution ring | **Aid**; also note **Elixir of Bloodlust has no spare bottle left anywhere in the save** |
| Kao | Heroes' Feast, Longstrider, Death Ward, Freedom of Movement, Mage Armor, Absorb Elements resource, new Counterspell resource (Staff of Interruption) | **Aid** |
| Astarion | Heroes' Feast, Longstrider, Death Ward, Freedom of Movement, Cat's Grace, Cloak of Displacement | **Aid**; carries a **new curse status** from The Tharchiate Codex — confirm it was a deliberate read |

> [!note] Pass Without Trace is still not active on the party in this save. Re-cast it before a stealth-sensitive approach if wanted.

## Available Camp-Buff Casters ^available-buff-casters

**Markers:** ⭐⭐⭐ ✨ 🎯

This table is about **spell access**, not currently active buffs. It answers who can provide useful pre-combat or camp-cast buffs before the party leaves camp.

| Character | Current role | Camp-buff spells or features they can provide | Practical note |
|---|---|---|---|
| TMind | Death Cleric 11 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement, Heroes' Feast; Divine Intervention: Arm Thy Servant if unused | Strong Cleric buffer, but using him as the active cleric means these spell slots come from the adventuring party. |
| Shadowheart | Camp Light Cleric 10 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement | Best current camp source for Cleric buffs because she can spend camp spell slots and then leave the active party. She's benched at camp this pass — a good time to have her recast the party-wide **Aid** gap before anyone leaves. |
| Kao | Human Wizard 11 | Longstrider, Mage Armor, Darkvision, See Invisibility, Counterspell (Staff of Interruption item charge); short utility such as Feather Fall, Enhance Leap, Invisibility if known and prepared | Excellent Wizard utility buffer. Does not naturally cover Aid, Warding Bond, Death Ward, Freedom of Movement, or Heroes' Feast. |
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
| Aid | Shadowheart first (she's at camp this pass); TMind only as backup | All four active characters, then summons if included | **Top priority right now** — the gap is party-wide. Shadowheart can spend camp slots while TMind keeps his Cleric slots for the active day. Upcast when practical. |
| Darkvision | Gale or Kao | Anyone without natural or item-based Darkvision | Useful exploration comfort. |
| See Invisibility | Gale or Kao | Kao or the character expected to reveal invisible enemies | Keep this on the scout/caster who is most likely to notice or expose targets. |
| Protection from Poison | Shadowheart first; TMind only if poison risk is high and she is unavailable | Frontline and anyone likely to fail poison saves | Situational daily buff. Do not spend time on it every day unless the area calls for it. |
| Warding Bond | Shadowheart, selectively | Lae'zel first; optionally TMind or Astarion for a hard fight | Strong but risky because Shadowheart receives shared damage. Use on one key target unless her HP and healing setup are managed. |
| Death Ward / Freedom of Movement | Already covering all four | — | No action needed this pass — both are fully resolved for the first time. Just recast before the *next* long rest so the streak holds. |
| Heroes' Feast | TMind (Cleric 11) | Whole party and summons | Cast it at camp before a big fight — the party's best pre-fight investment, especially before regrouping for something hard. |
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

Counts refreshed from the current `Campsite - 115h 34m` save (see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) for the full audit).

| Resource | Save count | Current holder pattern | Readiness call |
|---|---:|---|---|
| Scroll of Revivify | 10 | Kao 1, storage 9 | Unchanged; strong stock, put one on at least two active characters |
| Potion of Speed | 5 | TMind 1, Lae'zel 1, storage 3 | Enough for one decisive Haste opener |
| Elixir of Bloodlust | 0 | none | 🚨 **Gone from the save entirely** — Lae'zel's active buff has no spare bottle behind it; consider crafting or buying a replacement before a hard fight |
| Potion of Invisibility | 6 | Kao 1, TMind 1, storage 4 | Workable but don't over-rely on it |
| Scroll of Globe of Invulnerability | 4 | TMind 2, Astarion 2 | Split evenly between the two locations — fine as-is while the party is split |
| Scroll of Conjure Elemental | 3 | TMind 1, Astarion 1, storage 1 | Reasonable spread; regroup before assuming Kao has quick access |
| Healing potions (basic/greater/superior/supreme) | 42 | spread across all four plus storage | Well-supplied, no action needed |

## Gear and Synergy Checks ^gear-synergies

**Markers:** ⭐⭐ ✨ 🎯

| Check | Status | Note |
|---|---|---|
| Markoheshkir (Kao) | 🆕 Equip it | Legendary staff, free 1/long rest spell + elemental self-buff — best-in-slot, should already be his main weapon. |
| Robe of the Weave (Kao) | 🆕 Equip it | Very Rare, +2 AC/+1 spell save/attack plus a save-triggered heal — upgrade over Infernal Robe. |
| Duellist's Prerogative (Astarion) | 🆕 Build decision needed | Legendary rapier — strong, but pulls him from dual-dagger Thief toward a one-handed duelist build. Decide deliberately before respeccing anything around it. |
| Shadowheart weapon trick | ✅ Done | Devotee's Mace is still with TMind, unchanged. |
| Blood of Lathander | ✅ With TMind | Keep as the default cleric weapon unless the healing-aura plan is needed. |
| Devotee's Mace | ✅ With TMind | Use as a swap for Healing Incense Aura and on-heal item synergies. |
| Hellrider's Pride | ✅ With TMind | Works well with multi-target healing and rescue turns. |
| Spell Slot Restoration Amulet (Spellcrux Amulet) | ✅ With TMind | Strong day-extension tool; consider whether Kao needs it more before a caster-heavy fight. |
| The Whispering Promise | ✅ With TMind | Confirmed present — pairs with Devotee's Mace aura for concentration-free Bless-style value. |
| Sword of the Emperor (Lae'zel) | ✅ Rated ⭐⭐⭐ | +2 longsword, +2 to all saves vs spells — keep, strong vs Act 3's caster-heavy fights. |
| Boots of Psionic Movement (Lae'zel) | ✅ Rated ⭐⭐⭐ | Githyanki-only Fly + psychic damage rider. |
| Chancer's Carcanet (Lae'zel) | ✅ Rated ⭐⭐⭐ | Guaranteed Advantage on a save or attack, 1/long rest — keep. |
| Amulet of Windrider (Lae'zel) | 🆕 Keep | Very Rare mobility/control utility pickup this pass. |
| Shadow of Menzoberranzan / Disintegrating Night Walkers (Astarion) | ✅ Rated ⭐⭐⭐ | On-demand Invisibility and free Misty Step + terrain immunity respectively — both strong, keep equipped. |
| The Joltshooter / Gleamdance Dagger (Astarion) | ⚠️ Missing | Both are no longer found anywhere in the save — worth checking in game whether they were sold or given away. |
| *(boss-dropped shield, name withheld)* (Kao) | ⭐ Off-build | A shield doesn't fit a two-handed staff caster — carry for sale, don't equip. |
| Ring of Salving, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb | ⚠️ Unchanged — location uncertain | Still with the same unidentified companion-type character near camp, confirmed at the exact same position across two syncs now. Not recoverable through this audit method; check in game. |
| Murderous Cut | ✅ Resolved | No longer carried by anyone — only in storage now. |
| Whispering Mask ×3 | ✅ Resolved | No longer carried — moved to storage-only. |
| Reaper's Embrace | ⚠️ New — not free storage | Previously logged as free camp storage; now confirmed sitting with a different resurrected companion-type character, not the shared container. Check that companion's own inventory. |
| The Tharchiate Codex (×3: TMind ×2, Astarion ×1 read) | ⚠️ Decision needed | Astarion's copy is already read and cursed. Decide whether TMind reads either of his — same Constitution-for-temp-HP-and-ghouls trade-off. |

Full effect text and sourcing for every item above is in [[13_Item_Inventory_Snapshot#^inventory-new-finds\|Item and Storage Snapshot § Item Ratings and Redistribution]].

## Before Leaving Camp ^before-leaving-camp

**Markers:** ⭐⭐⭐ ⏱️ ⚔️

The party is split between camp and Ramazith's Tower. Regroup first — everything else follows from that.

1. **Regroup TMind/Lae'zel with Kao/Astarion** before treating the party as fight-ready. Top priority; nothing else here matters until this happens.
2. **Recast Aid on all four characters** — new gap, previously always covered. Shadowheart (at camp with TMind/Lae'zel) is the efficient source.
3. ✅ Resolved: Death Ward, Freedom of Movement, and Mage Armor are all active on everyone — no action needed, just keep the streak going after the next long rest.
4. Decide on **Astarion's Duellist's Prerogative** — dual-dagger Thief vs. one-handed duelist is a real build fork, not a drop-in upgrade.
5. Equip **Markoheshkir** and **Robe of the Weave** on Kao if not already active.
6. Replace the **Elixir of Bloodlust** supply — the save has zero spares left; Lae'zel's active dose has nothing behind it.
7. Confirm whether reading **The Tharchiate Codex** on Astarion was intentional, and decide whether TMind should read either of his two copies.
8. Check on **Ring of Salving / Cloak of Protection / Helmet of Arcane Acuity / Bloodguzzler Garb** and **Reaper's Embrace**, both still sitting with unidentified companion-type characters rather than in shared storage.
9. Re-apply **Pass Without Trace** before a stealth approach if wanted (still not active this save).
10. Investigate **The Joltshooter and Gleamdance Dagger** — both gone from Astarion's inventory with no clear cause.

## Before a Hard Fight ^before-hard-fight

**Markers:** ⭐⭐⭐ ⚔️ 🎯

| Step | Action |
|---|---|
| 1 | Confirm everyone who should fight is actually grouped and nearby — the party is currently split across two locations. |
| 2 | Put turn-based mode on before throwing short-duration potions. |
| 3 | If using Potion of Speed on multiple characters, throw it only immediately before combat. |
| 4 | Put Globe of Invulnerability and Conjure Elemental scrolls on whichever caster is present at the fight. |
| 5 | Put invisibility tools, anti-caster arrows, and poisons on Astarion. |
| 6 | Line up a Bloodlust/Colossus elixir alternative for Lae'zel before initiative matters — Bloodlust is out of stock. |
| 7 | Keep TMind's Divine Intervention unused unless the fight collapses. |
| 8 | Cast Heroes' Feast at camp before committing to the fight, if it hasn't been used yet this rest cycle. |

## Source ^readiness-source

**Markers:** ⭐⭐ ⏱️

| Field | Current value |
|---|---|
| Save name | Campsite - 115h 34m |
| Save modified | 2026-08-30 01:29:40 +02:00 |
| Synced into handbook | 2026-08-30 01:34:23 +02:00 |
| Game version | 4.1.1.7398727 |
| Difficulty | DifficultyMedium / RulesetLarian |
| Source record | `tools/save-extract/source_manifest.json` |

## Parser Notes

**Markers:** ⭐ ⚠️

- This audit used the current `.lsf` index, not a refreshed `Globals.lsx` text export.
- Active buff detection is reliable for the four named party members because it reads their current status managers.
- Character identity was confirmed by matching each `Character` node's exact `Translate` position against the position reported for that character in `SaveInfo.json`; no decoy/duplicate nodes were found at any of the four positions this pass.
- The party split across two locations meant position-matching had to be checked against two distinct coordinate sets (`CAMP_SUB` for TMind/Lae'zel, the tower subregion for Kao/Astarion) rather than one.
- The Tharchiate Codex curse status (`CURSEDTOME_THARCHIATE_CODEX`) and TMind's unchanged partial-ceremorphosis status (`TAD_PARTIAL_CEREMORPH`) were both confirmed directly against the raw status list, not inferred.
- Storage-bucket items were re-verified with the `Level` field plus a nearby-`Character`-node check before being called "genuinely in storage" — this caught Reaper's Embrace moving out of that bucket this pass (see the Item and Storage Snapshot's Camp Storage section for the correction).
- The broader save contains many `DYING` statuses on old or non-active entities; the active-party status managers for the four named characters do not show `DYING` in this save.
- Item counts are reliable for practical stock checks, but exact equipped slots still need in-game confirmation.
- Camp storage and world/storage-like inventories are summarized as "elsewhere" rather than by raw container or position.
