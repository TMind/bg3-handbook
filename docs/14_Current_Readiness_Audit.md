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

**Two characters are sitting on an unclaimed level-up, and the party split flipped direction.** Kao and Astarion are already Level 12 and together at Baldur's Mouth Basement; TMind and Lae'zel have the XP for Level 12 too but the save still shows them at 11 in Lower City — the level-up screen just hasn't been used yet for those two. Buff coverage now splits by location rather than by character: the Baldur's Mouth pair kept Death Ward, the Lower City pair lost it. Elixir of Bloodlust is now fully and confirmedly out of stock.

| Area | Status | Reason |
|---|---|---|
| Core party | ⚠️ Split | TMind and Lae'zel are at `LOW_City_SUB`; Kao and Astarion are at `LOW_BaldursMouth_Basement_SUB`. Regroup before any hard fight. |
| Pending level-ups | ⚠️ Action needed | TMind and Lae'zel both have enough XP for Level 12 but the save still shows Level 11 — go through the level-up screen for both. |
| Death protection | ⚠️ Split by location | Kao and Astarion (Baldur's Mouth) still have Death Ward; TMind and Lae'zel (Lower City) both lost it this pass. |
| Control protection | ✅ Good | Freedom of Movement is active on all four, still universal. |
| Maximum HP (Aid) | ⚠️ Split by location | Kao and TMind have it; Astarion and Lae'zel don't. Not a clean party-wide gap or resolution — recast for whoever's missing it before regrouping. |
| Daily movement | ⚠️ Mostly good | Longstrider covers TMind, Kao, and Astarion; **Lae'zel lost it** this pass. |
| Mage Armor (Kao) | ✅ Good | Still holding, unchanged. |
| Stealth aura | ⚠️ Unchanged gap | Pass Without Trace is still not active on the party. |
| Burst resources | 🚨 Depleted | Elixir of Bloodlust remains at zero anywhere in the save — Lae'zel's active buff has now actually expired (confirmed missing from her status list this pass), not just low on spares. |
| New status | ℹ️ Low pressure | Astarion's Tharchiate Codex curse is still present (status ID renamed internally, likely the same curse) — reversible with Remove Curse/Greater Restoration whenever wanted. |
| Coverage catch-up | ℹ️ Informational | This pass surfaced several TMind and Kao items (Circle of Bones, Adamantine Scale Mail, The Spectator Eyes, Strange Tendril Amulet, and others) that were apparently already owned but never rated in past audits — not new gear, just newly documented. See [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md). |

## Active Buff Coverage

**Markers:** ⭐⭐⭐ ✨

| Character | Confirmed useful buffs | Missing before hard fights |
|---|---|---|
| TMind | Heroes' Feast, **Aid**, Freedom of Movement, Longstrider, Shield of Devotion spell slot | **Death Ward** — lost this pass |
| Lae'zel | Heroes' Feast, Freedom of Movement, critical-execution ring, a Bane-style weapon oil | **Death Ward, Longstrider, and Aid** — the most gaps of the four this pass; also her Elixir of Bloodlust has fully expired |
| Kao | Heroes' Feast, Death Ward, Freedom of Movement, Mage Armor, **Aid**, Warding Bond, Absorb Elements, Counterspell resource | No major gap — best-covered character this pass |
| Astarion | Heroes' Feast, Death Ward, Freedom of Movement, Longstrider, Cat's Grace, Cloak of Displacement | **Aid**; still carries the Tharchiate Codex curse (reversible whenever wanted) |

> [!note] Pass Without Trace is still not active on the party in this save. Re-cast it before a stealth-sensitive approach if wanted.

## Available Camp-Buff Casters ^available-buff-casters

**Markers:** ⭐⭐⭐ ✨ 🎯

This table is about **spell access**, not currently active buffs. It answers who can provide useful pre-combat or camp-cast buffs before the party leaves camp.

| Character | Current role | Camp-buff spells or features they can provide | Practical note |
|---|---|---|---|
| TMind | Death Cleric 11 (eligible for 12) | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement, Heroes' Feast; Divine Intervention: Arm Thy Servant if unused | Strong Cleric buffer, but using him as the active cleric means these spell slots come from the adventuring party. |
| Shadowheart | Camp Light Cleric 10 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement | Best current camp source for Cleric buffs because she can spend camp slots and then leave the active party. With TMind's own Death Ward now missing, she's a good source to recast it before he leaves camp again. |
| Kao | Human Wizard 12 | Longstrider, Mage Armor, Darkvision, See Invisibility, Counterspell (Staff of Interruption item charge); short utility if known and prepared | Excellent Wizard utility buffer. Does not naturally cover Aid, Warding Bond, Death Ward, Freedom of Movement, or Heroes' Feast. |
| Gale | Camp Wizard, if used | Longstrider, Mage Armor, Darkvision, See Invisibility; short utility if known and prepared | Same practical job as Kao: free the active Wizard from routine utility casting. |
| Bard hireling | Bard support | Longstrider; Freedom of Movement at Bard 7; Death Ward only if selected through Magical Secrets at Bard 10; Song of Rest as a day-extension feature | Good support hireling, but not a full camp buffer unless multiclassed into Cleric/Wizard. Worth using for Lae'zel's dropped Longstrider specifically. |
| Lae'zel | Battle Master Fighter | None from the current build | Receives buffs; does not provide spell-based camp buffs. |
| Astarion | Thief Rogue | None from the current build | Receives buffs; does not provide spell-based camp buffs unless rebuilt into a caster subclass or multiclass. |

For exact spellbook state, verify prepared spells in game before relying on a caster. Clerics can usually prepare the listed Cleric buffs from their class list, while Wizards must have learned the spell and prepared it, and Bards must have chosen the spell as a known spell or Magical Secrets pick.

## Optimal Buff-Spell Assignment ^optimal-buff-assignment

**Markers:** ⭐⭐⭐ ⏱️ ✨ 🎯

Default principle: let camp characters pay for daily utility first, then keep the active party's spell slots for combat, reactions, and emergencies.

| Buff or setup | Best caster | Main targets | Why this assignment is best |
|---|---|---|---|
| Death Ward | Shadowheart first; TMind or Kao as backup | TMind and Lae'zel (both currently missing it) | **Top priority for the Lower City pair** — they lost it this pass while the Baldur's Mouth pair kept it. |
| Aid | Shadowheart first; TMind or Kao as backup | Astarion and Lae'zel (both currently missing it) | Kao and TMind already have it; fill the other two before a hard fight. |
| Longstrider | Bard hireling first; Gale or Kao as backup | Lae'zel specifically (the only one currently missing it) | Ritual casting makes this cheap — a quick fix for a single-character gap. |
| Mage Armor | Gale if available; Kao as backup | Kao if unarmored; eligible summons or unarmored allies | Wizard utility job. Skip armored characters because the spell does nothing for them. |
| Darkvision | Gale or Kao | Anyone without natural or item-based Darkvision | Useful exploration comfort. |
| See Invisibility | Gale or Kao | Kao or the character expected to reveal invisible enemies | Keep this on the scout/caster who is most likely to notice or expose targets. |
| Protection from Poison | Shadowheart first; TMind only if poison risk is high and she is unavailable | Frontline and anyone likely to fail poison saves | Situational daily buff. Do not spend time on it every day unless the area calls for it. |
| Warding Bond | Shadowheart, selectively | Lae'zel first; optionally TMind or Astarion for a hard fight | Strong but risky because Shadowheart receives shared damage. Use on one key target unless her HP and healing setup are managed. |
| Freedom of Movement | Already covering all four | — | No action needed — still universal after this pass. Just recast before the *next* long rest so the streak holds. |
| Heroes' Feast | TMind (Cleric 11) | Whole party and summons | Cast it at camp before a big fight — the party's best pre-fight investment, especially before regrouping for something hard. |
| Song of Rest | Bard hireling | Whole party after short-rest resources are spent | Not a buff spell, but it extends the adventuring day and should be used after meaningful short-rest value is missing. |

### Recommended Daily Caster Roles

| Character | Daily job |
|---|---|
| Shadowheart | Primary Cleric camp buffer: Death Ward and Aid for whichever pair is missing them, Warding Bond only when worth the risk. |
| Bard hireling | Longstrider routine (especially for Lae'zel right now), Freedom of Movement at Bard 7+, Death Ward only if Bard 10 Magical Secrets selected it, Song of Rest for day extension. |
| Gale | Camp Wizard utility: Longstrider backup, Mage Armor, Darkvision, See Invisibility. |
| Kao | Active Wizard utility backup only; avoid spending his slots if Gale or Bard can cover the same setup. |
| TMind | Active Cleric fallback; use his slots only when Shadowheart cannot cover the buff or the fight needs immediate recasting. |
| Lae'zel | Main recipient for movement, Death Ward, Aid, and selective Warding Bond — currently the most gap-heavy of the four. |
| Astarion | Recipient for Aid when control or restraint is expected; otherwise well-covered this pass. |

## Consumable Readiness ^consumable-readiness

**Markers:** ⭐⭐⭐ 🍷 ⚔️

Counts refreshed from the current `Lower City - 118h 27m` save (see [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) for the full audit).

| Resource | Save count | Current holder pattern | Readiness call |
|---|---:|---|---|
| Scroll of Revivify | 11 | TMind 2, Lae'zel 1, Kao 1, Astarion 1, storage 6 | Best distribution yet — spread across all four plus storage, no action needed |
| Potion of Speed | 4 | TMind 1, Astarion 1, storage 2 | Enough for one decisive Haste opener |
| Elixir of Bloodlust | 0 | none | 🚨 **Still gone from the save entirely**, and Lae'zel's active buff has now actually expired — this is a real gap now, not just "no spares" |
| Potion of Invisibility | 7 | Lae'zel 2, Kao 1, Astarion 1, storage 3 | Healthy stock |
| Scroll of Globe of Invulnerability | 2 | TMind 2 | Down from 4 (Astarion's copies used or lost); still not with Kao, who casts it |
| Scroll of Conjure Elemental | 3 | TMind 1, Astarion 1, storage 1 | Unchanged |
| Scroll of Bestow Curse | 2 | Astarion 2 | Swung back to Astarion after coming home to Kao last pass — fifth snapshot of this back-and-forth |
| Healing potions (basic/greater/superior/supreme) | 36 | spread across all four plus storage | Well-supplied, no action needed |

## Gear and Synergy Checks ^gear-synergies

**Markers:** ⭐⭐ ✨ 🎯

| Check | Status | Note |
|---|---|---|
| Circle of Bones (TMind) | 🆕 Equip it | Rare circlet — Animate Dead + Undead Ward, near-perfect fit for a Death Domain necromancer. Only surfaced in this audit this pass; likely already owned. |
| Adamantine Scale Mail (TMind) | 🆕 Equip it | Very Rare medium armour — damage reduction, no crits, Reeling rider. One of the strongest defensive pieces available; only surfaced this pass. |
| TMind's five competing amulets | ⚠️ Pick one | The Spectator Eyes, Amulet of Restoration, Amulet of Misty Step, Spellcrux Amulet, Pearl of Power all want the same slot — see [[13_Item_Inventory_Snapshot#^inventory-tmind\|TMind's section]] for the comparison. |
| Reaper's Embrace (Lae'zel) | ✅ Resolved | No longer a mystery-companion item — confirmed genuinely in her own inventory this pass. Now a real third armour option alongside Adamantine Splint Armour and Cerebral Citadel Armour. |
| Markoheshkir / Robe of the Weave (Kao) | ✅ Equipped | Legendary staff + Very Rare robe, both confirmed rated and recommended equipped. |
| Duellist's Prerogative (Astarion) | ✅ Equip it (empty off-hand) | Legendary rapier — verified mechanics show Thief's bonus-action economy and Sneak Attack are unaffected (Dueller's Enthusiasm replaces the off-hand attack). See [[11_Main_Character_Builds#^astarion-build\|Astarion's build]]. |
| Salty Scimitar(rrr) | ⚠️ Off-build wherever it lands | Moved from Astarion to TMind this pass — doesn't fit either build (rapier-and-empty-off-hand Astarion, mace-and-shield TMind). Sell it instead of letting it keep drifting. |
| Kao's three competing amulets | ⚠️ Pick one | Strange Tendril Amulet, Fey Semblance Amulet, and Spineshudder Amulet all want the same slot — Spineshudder is the weakest fit (rewards spell attacks, not the saves Kao mostly forces). |
| Sword of the Emperor / Boots of Psionic Movement / Chancer's Carcanet (Lae'zel) | ✅ Rated ⭐⭐⭐ | All three keep, unchanged. |
| Shadow of Menzoberranzan / Disintegrating Night Walkers / Shade-Slayer Cloak (Astarion) | ✅ Rated ⭐⭐⭐ | Keep equipped, unchanged. |
| The Joltshooter / Gleamdance Dagger (Astarion) | ⚠️ Still missing | Neither found anywhere in the save across two syncs now — worth checking in game. |
| *(boss-dropped shield, name withheld)* (Kao) | ⭐ Off-build | A shield doesn't fit a two-handed staff caster — carry for sale, don't equip. |
| Ring of Salving cluster (Ring of Salving, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb ×2, Cerebral Citadel Gloves) | ⚠️ Method exhausted | The "unidentified companion" holding these has moved ~23 units away from the items this pass while they stayed put — evidence they were never in that companion's personal inventory, just near a fixed container. Two prior re-labels plus this new twist means position data alone can't resolve this: **check in game directly** rather than expect another audit correction. |
| Murderous Cut / Whispering Mask ×3 | ✅ Resolved | Both stay resolved — storage-only, not carried by anyone. |
| The Tharchiate Codex (×3: TMind ×2, Astarion ×1 read) | ℹ️ Reversible | Astarion's copy is already read and cursed, but curable with Remove Curse/Greater Restoration if unwanted. Decide whether TMind reads either of his. |

Full effect text and sourcing for every item above is in [[13_Item_Inventory_Snapshot#^inventory-new-finds\|Item and Storage Snapshot § Item Ratings and Redistribution]].

## Before Leaving Camp ^before-leaving-camp

**Markers:** ⭐⭐⭐ ⏱️ ⚔️

The party is split between Lower City and Baldur's Mouth Basement. Regroup first — everything else follows from that.

1. **Regroup TMind/Lae'zel with Kao/Astarion** before treating the party as fight-ready. Top priority.
2. **Level up TMind and Lae'zel to 12** — both already have the XP, just need the level-up screen.
3. **Recast Death Ward on TMind and Lae'zel** — lost this pass, while Kao/Astarion kept it.
4. **Recast Aid on Astarion and Lae'zel** — Kao and TMind already have it.
5. **Recast Longstrider on Lae'zel** — the only one missing it now.
6. Equip **Circle of Bones** and **Adamantine Scale Mail** on TMind if not already active — both newly surfaced this pass and rate highly.
7. Pick one of TMind's five competing amulets rather than leaving it to chance — see Gear and Synergy Checks.
8. Replace the **Elixir of Bloodlust** supply — still zero anywhere in the save, and the active buff has now actually run out.
9. The Tharchiate Codex curse on Astarion is reversible (Remove Curse/Greater Restoration) — cure it if the trade-off isn't wanted, and decide whether TMind should read either of his two copies.
10. Re-apply **Pass Without Trace** before a stealth approach if wanted (still not active this save).
11. The Ring of Salving cluster needs an in-game check, not another position-based guess — see Gear and Synergy Checks for why.

## Before a Hard Fight ^before-hard-fight

**Markers:** ⭐⭐⭐ ⚔️ 🎯

| Step | Action |
|---|---|
| 1 | Confirm everyone who should fight is actually grouped and nearby — the party is currently split across two locations. |
| 2 | Put turn-based mode on before throwing short-duration potions. |
| 3 | If using Potion of Speed on multiple characters, throw it only immediately before combat. |
| 4 | Put Globe of Invulnerability and Conjure Elemental scrolls on whichever caster is present at the fight. |
| 5 | Put invisibility tools, anti-caster arrows, and poisons on Astarion. |
| 6 | Line up a Bloodlust/Colossus elixir alternative for Lae'zel before initiative matters — Bloodlust is out of stock and her buff has expired. |
| 7 | Keep TMind's Divine Intervention unused unless the fight collapses. |
| 8 | Cast Heroes' Feast at camp before committing to the fight, if it hasn't been used yet this rest cycle. |
| 9 | With Astarion on Duellist's Prerogative (two reactions/turn), have Lae'zel spend Commander's Strike on him deliberately — see [[11_Main_Character_Builds#^laezel-build\|Lae'zel's build § Commander's Strike → Astarion Reaction Combo]] for the full sequence. |

## Source ^readiness-source

**Markers:** ⭐⭐ ⏱️

| Field | Current value |
|---|---|
| Save name | Lower City - 118h 27m |
| Save modified | 2026-08-31 01:13:19 +02:00 |
| Synced into handbook | 2026-08-31 08:42:08 +02:00 |
| Game version | 4.1.1.7398727 |
| Difficulty | DifficultyMedium / RulesetLarian |
| Source record | `tools/save-extract/source_manifest.json` |

## Parser Notes

**Markers:** ⭐ ⚠️

- This audit used the current `.lsf` index, not a refreshed `Globals.lsx` text export.
- Active buff detection is reliable for the four named party members because it reads their current status managers.
- Character identity was confirmed by matching each `Character` node's exact `Translate` position against the position reported for that character in `SaveInfo.json`; no decoy/duplicate nodes were found at any of the four positions this pass.
- The party split across two *different* locations than last pass (Lower City proper and Baldur's Mouth Basement, not camp and the tower), so position-matching was re-derived from this save's own `SaveInfo.json`, not reused from the prior snapshot's coordinates.
- **TMind and Lae'zel's `Level: 11` despite XP over the Level 12 threshold is read as a pending level-up, not an extraction bug** — Kao and Astarion, with less total XP, already show Level 12, which only makes sense if they've already used the level-up screen and TMind/Lae'zel haven't.
- Astarion's curse status changed internal ID from `CURSEDTOME_THARCHIATE_CODEX` to `CURSEDTOME_THARCHIATE_TECHNICAL` between snapshots — treated as the same curse (a common BG3 pattern: a display status paired with an internal `_TECHNICAL` marker) but not independently re-confirmed against bg3.wiki this pass.
- **Lae'zel's known maneuvers (e.g. Commander's Strike) are not verifiable from this save index** — known spells/maneuvers for player characters aren't captured by the `Globals.lsf` extraction this handbook uses, only items, positions, and active statuses. Anything about her maneuver picks is player-reported, not save-confirmed.
- The Ring of Salving cluster's position-based inference has now been corrected twice and contradicted a third time (the nearby companion moved away from the stationary items) — flagged in Gear and Synergy Checks as a case where this audit method has reached its limit; needs in-game confirmation instead of another position-based guess.
- The broader save contains many `DYING` statuses on old or non-active entities; the active-party status managers for the four named characters do not show `DYING` in this save.
- Item counts are reliable for practical stock checks, but exact equipped slots still need in-game confirmation. This pass surfaced several previously-uncatalogued TMind and Kao items that were apparently already owned — a coverage gap in past audits, now corrected.
- Camp storage and world/storage-like inventories are summarized as "elsewhere" rather than by raw container or position.
