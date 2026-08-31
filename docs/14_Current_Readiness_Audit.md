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

**Both pending level-ups are done, and Lae'zel came out of a respec with no buffs at all.** All four are now Level 12; the save's own class list confirms Lae'zel is now Fighter (Battle Master) / Cleric (War Domain), matching the newly-decided build. That respec seems to have wiped every buff she had — Death Ward, Freedom of Movement, Longstrider, Heroes' Feast, and Aid are all gone, though her Elixir of Bloodlust is somehow active again. TMind and Lae'zel moved from Lower City back to camp; Kao and Astarion are still at Baldur's Mouth Basement — the party remains split.

| Area | Status | Reason |
|---|---|---|
| Core party | ⚠️ Still split | TMind and Lae'zel are at camp; Kao and Astarion are at `LOW_BaldursMouth_Basement_SUB`. Regroup before any hard fight. |
| Level-ups | ✅ Done | TMind and Lae'zel are both confirmed Level 12. |
| Lae'zel's buffs | 🚨 Full wipe | Death Ward, Freedom of Movement, Longstrider, Heroes' Feast, and Aid are all gone at once — almost certainly tied to the respec. Needs a full rebuff before she's fight-ready. |
| Death protection (others) | ⚠️ Unchanged | TMind still missing Death Ward; Kao and Astarion still have it. |
| Control protection (others) | ✅ Good | Freedom of Movement still covers TMind, Kao, and Astarion. |
| Maximum HP (Aid, others) | ⚠️ Unchanged | Kao and TMind have it; Astarion still doesn't. |
| Mage Armor (Kao) | ✅ Good | Still holding, unchanged. |
| Stealth aura | ⚠️ Unchanged gap | Pass Without Trace is still not active on the party. |
| Burst resources | ℹ️ Puzzling | Lae'zel's Elixir of Bloodlust is active again despite zero bottles anywhere in the save — likely recast from a dose that was already running, not a new purchase. Worth confirming there's actually a backup before relying on it. |
| New status | ℹ️ Low pressure | Astarion's Tharchiate Codex curse is unchanged — reversible with Remove Curse/Greater Restoration whenever wanted. |
| Coverage correction | ✅ Resolved | The Joltshooter and Gleamdance Dagger were wrongly flagged as missing last pass — both are confirmed present (a vendor and camp storage respectively). See [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md). |

## Active Buff Coverage

**Markers:** ⭐⭐⭐ ✨

| Character | Confirmed useful buffs | Missing before hard fights |
|---|---|---|
| TMind | Heroes' Feast, Aid, Freedom of Movement, Longstrider, Shield of Devotion spell slot | **Death Ward** — unchanged gap |
| Lae'zel | Critical-execution ring, a Bane-style weapon oil, Elixir of Bloodlust | **Everything else**: Death Ward, Freedom of Movement, Longstrider, Heroes' Feast, Aid — a full rebuff is needed, likely a respec side-effect |
| Kao | Heroes' Feast, Death Ward, Freedom of Movement, Mage Armor, Aid, Absorb Elements, Counterspell resource | No major gap — best-covered character this pass |
| Astarion | Heroes' Feast, Death Ward, Freedom of Movement, Longstrider, Cat's Grace, Cloak of Displacement | **Aid**; still carries the Tharchiate Codex curse (reversible whenever wanted) |

> [!note] Pass Without Trace is still not active on the party in this save. Re-cast it before a stealth-sensitive approach if wanted.

## Available Camp-Buff Casters ^available-buff-casters

**Markers:** ⭐⭐⭐ ✨ 🎯

This table is about **spell access**, not currently active buffs. It answers who can provide useful pre-combat or camp-cast buffs before the party leaves camp.

| Character | Current role | Camp-buff spells or features they can provide | Practical note |
|---|---|---|---|
| TMind | Death Cleric 12 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement, Heroes' Feast; Divine Intervention: Arm Thy Servant if unused | Strong Cleric buffer, but using him as the active cleric means these spell slots come from the adventuring party. |
| Shadowheart | Camp Light Cleric 10 | Aid, Protection from Poison, Warding Bond, Death Ward, Freedom of Movement | Best current camp source for Cleric buffs. With Lae'zel needing a full rebuff, she's the efficient way to cover Death Ward, Freedom of Movement, and Aid on her in one stop. |
| Lae'zel (Cleric 1, War Domain) | New this pass | Cantrips (Resistance, Guidance, Light); Create Water, Sanctuary, Command as prepared spells | Not a buff caster in practice — her one Cleric level is for War Priest's bonus-action attacks, not spell support. |
| Kao | Human Wizard 12 | Longstrider, Mage Armor, Darkvision, See Invisibility, Counterspell (Staff of Interruption item charge); short utility if known and prepared | Excellent Wizard utility buffer. Does not naturally cover Aid, Warding Bond, Death Ward, Freedom of Movement, or Heroes' Feast. |
| Gale | Camp Wizard, if used | Longstrider, Mage Armor, Darkvision, See Invisibility; short utility if known and prepared | Same practical job as Kao: free the active Wizard from routine utility casting. |
| Bard hireling | Bard support | Longstrider; Freedom of Movement at Bard 7; Death Ward only if selected through Magical Secrets at Bard 10; Song of Rest as a day-extension feature | Good support hireling, but not a full camp buffer unless multiclassed into Cleric/Wizard. Useful for Lae'zel's Longstrider specifically. |
| Astarion | Thief Rogue | None from the current build | Receives buffs; does not provide spell-based camp buffs. |

For exact spellbook state, verify prepared spells in game before relying on a caster. Clerics can usually prepare the listed Cleric buffs from their class list, while Wizards must have learned the spell and prepared it, and Bards must have chosen the spell as a known spell or Magical Secrets pick.

## Optimal Buff-Spell Assignment ^optimal-buff-assignment

**Markers:** ⭐⭐⭐ ⏱️ ✨ 🎯

Default principle: let camp characters pay for daily utility first, then keep the active party's spell slots for combat, reactions, and emergencies.

| Buff or setup | Best caster | Main targets | Why this assignment is best |
|---|---|---|---|
| Death Ward, Freedom of Movement, Longstrider, Aid, Heroes' Feast | Shadowheart, all at once if possible | **Lae'zel** | **Top priority** — she lost every one of these in the respec. A full camp rebuff before she leaves is the single most important pre-fight step this pass. |
| Death Ward | TMind or Kao as backup | TMind (unchanged gap) | Second priority once Lae'zel is covered. |
| Aid | Shadowheart first; TMind or Kao as backup | Astarion (unchanged gap) | Kao and TMind already have it. |
| Mage Armor | Gale if available; Kao as backup | Kao if unarmored; eligible summons or unarmored allies | Wizard utility job. Skip armored characters because the spell does nothing for them. |
| Darkvision | Gale or Kao | Anyone without natural or item-based Darkvision | Useful exploration comfort. |
| See Invisibility | Gale or Kao | Kao or the character expected to reveal invisible enemies | Keep this on the scout/caster who is most likely to notice or expose targets. |
| Protection from Poison | Shadowheart first; TMind only if poison risk is high and she is unavailable | Frontline and anyone likely to fail poison saves | Situational daily buff. |
| Warding Bond | Shadowheart, selectively | Lae'zel first; optionally TMind or Astarion for a hard fight | Strong but risky because Shadowheart receives shared damage. |
| Heroes' Feast | TMind (Cleric 12) | Whole party and summons | Cast it at camp before a big fight, once Lae'zel's rebuff is also handled. |
| Song of Rest | Bard hireling | Whole party after short-rest resources are spent | Extends the adventuring day. |

### Recommended Daily Caster Roles

| Character | Daily job |
|---|---|
| Shadowheart | Primary Cleric camp buffer: Lae'zel's full rebuff is the priority, then Death Ward/Aid for whoever else is missing them. |
| Bard hireling | Longstrider routine (especially for Lae'zel), Freedom of Movement at Bard 7+, Death Ward only if Bard 10 Magical Secrets selected it, Song of Rest for day extension. |
| Gale | Camp Wizard utility: Longstrider backup, Mage Armor, Darkvision, See Invisibility. |
| Kao | Active Wizard utility backup only; avoid spending his slots if Gale or Bard can cover the same setup. |
| TMind | Active Cleric fallback; use his slots only when Shadowheart cannot cover the buff or the fight needs immediate recasting. |
| Lae'zel | Now the main recipient for nearly everything — Death Ward, Freedom of Movement, Longstrider, Aid, Heroes' Feast, all lost in the respec. |
| Astarion | Recipient for Aid when control or restraint is expected; otherwise well-covered this pass. |

## Consumable Readiness ^consumable-readiness

**Markers:** ⭐⭐⭐ 🍷 ⚔️

No inventory changes anywhere in the save this pass (verified item-by-item against the last sync) — counts below are unchanged from the previous audit. See [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) for the full breakdown.

| Resource | Save count | Current holder pattern | Readiness call |
|---|---:|---|---|
| Scroll of Revivify | 11 | TMind 2, Lae'zel 1, Kao 1, Astarion 1, storage 6 | Best distribution yet — spread across all four plus storage, no action needed |
| Potion of Speed | 4 | TMind 1, Astarion 1, storage 2 | Enough for one decisive Haste opener |
| Elixir of Bloodlust | 0 | none in inventory | Lae'zel's buff is active again despite zero bottles found — confirm in game where the dose actually came from before assuming there's a backup |
| Potion of Invisibility | 7 | Lae'zel 2, Kao 1, Astarion 1, storage 3 | Healthy stock |
| Scroll of Globe of Invulnerability | 2 | TMind 2 | Still not with Kao, who casts it |
| Scroll of Conjure Elemental | 3 | TMind 1, Astarion 1, storage 1 | Unchanged |
| Scroll of Bestow Curse | 2 | Astarion 2 | Unchanged |
| Healing potions (basic/greater/superior/supreme) | 36 | spread across all four plus storage | Well-supplied, no action needed |

## Gear and Synergy Checks ^gear-synergies

**Markers:** ⭐⭐ ✨ 🎯

No inventory changes this pass — this table is unchanged from the last audit except the Joltshooter/Gleamdance correction below.

| Check | Status | Note |
|---|---|---|
| Circle of Bones (TMind) | 🆕 Equip it | Rare circlet — Animate Dead + Undead Ward, near-perfect fit for a Death Domain necromancer. |
| Adamantine Scale Mail (TMind) | ✅ Confirmed equipped | Very Rare medium armour — damage reduction, no crits, Reeling rider. Player-confirmed equipped. |
| TMind's five competing amulets | ⚠️ Pick one | The Spectator Eyes, Amulet of Restoration, Amulet of Misty Step, Spellcrux Amulet, Pearl of Power all want the same slot — see [[13_Item_Inventory_Snapshot#^inventory-tmind\|TMind's section]]. |
| Reaper's Embrace (Lae'zel) | ✅ Resolved | Confirmed genuinely in her own inventory — a real third armour option alongside Adamantine Splint Armour and Cerebral Citadel Armour. |
| Markoheshkir / Robe of the Weave (Kao) | ✅ Equipped | Legendary staff + Very Rare robe, both confirmed rated and recommended equipped. |
| Duellist's Prerogative (Astarion) | ✅ Equip it (empty off-hand) | Legendary rapier — Thief's bonus-action economy and Sneak Attack are unaffected. See [[11_Main_Character_Builds#^astarion-build\|Astarion's build]]. |
| Salty Scimitar(rrr) | ⚠️ Off-build wherever it lands | Doesn't fit either TMind or Astarion's build — sell it. |
| Kao's three competing amulets | ⚠️ Pick one | Strange Tendril Amulet, Fey Semblance Amulet, and Spineshudder Amulet all want the same slot. |
| Sword of the Emperor / Boots of Psionic Movement / Chancer's Carcanet (Lae'zel) | ✅ Rated ⭐⭐⭐ | All three keep, unchanged. |
| Shadow of Menzoberranzan / Disintegrating Night Walkers / Shade-Slayer Cloak (Astarion) | ✅ Rated ⭐⭐⭐ | Keep equipped, unchanged. |
| The Joltshooter / Gleamdance Dagger (Astarion) | ✅ Resolved (correction) | An earlier "not found anywhere" claim was wrong — The Joltshooter is with a vendor NPC (likely sold), Gleamdance Dagger is genuinely in camp storage. Neither is missing. |
| *(boss-dropped shield, name withheld)* (Kao) | ⭐ Off-build | Carry for sale, don't equip. |
| Ring of Salving cluster (Ring of Salving, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb ×2, Cerebral Citadel Gloves) | ⚠️ Method exhausted | Position data can't resolve this further — check in game directly. |
| Murderous Cut / Whispering Mask ×3 | ✅ Resolved | Both stay resolved — storage-only. |
| The Tharchiate Codex (×3: TMind ×2, Astarion ×1 read) | ℹ️ Reversible | Curable with Remove Curse/Greater Restoration if unwanted. |

Full effect text and sourcing for every item above is in [[13_Item_Inventory_Snapshot#^inventory-new-finds\|Item and Storage Snapshot § Item Ratings and Redistribution]].

## Before Leaving Camp ^before-leaving-camp

**Markers:** ⭐⭐⭐ ⏱️ ⚔️

The party is split between camp and Baldur's Mouth Basement. Regroup first — everything else follows from that.

1. **Regroup TMind/Lae'zel with Kao/Astarion** before treating the party as fight-ready. Top priority.
2. **Give Lae'zel a full rebuff**: Death Ward, Freedom of Movement, Longstrider, Aid, Heroes' Feast — all lost in the respec. Shadowheart at camp is the efficient source.
3. **Recast Death Ward on TMind** — unchanged gap.
4. **Recast Aid on Astarion** — unchanged gap.
5. Equip **Circle of Bones** on TMind if not already active.
6. Pick one of TMind's five competing amulets rather than leaving it to chance.
7. Confirm the source of Lae'zel's active Elixir of Bloodlust dose in game — no bottles exist in the tracked inventory, so it's worth knowing whether there's really a backup.
8. The Tharchiate Codex curse on Astarion is reversible — cure it if the trade-off isn't wanted, and decide whether TMind should read either of his two copies.
9. Re-apply **Pass Without Trace** before a stealth approach if wanted.
10. The Ring of Salving cluster needs an in-game check, not another position-based guess.

## Before a Hard Fight ^before-hard-fight

**Markers:** ⭐⭐⭐ ⚔️ 🎯

| Step | Action |
|---|---|
| 1 | Confirm everyone who should fight is actually grouped and nearby — the party is currently split across two locations. |
| 2 | Put turn-based mode on before throwing short-duration potions. |
| 3 | If using Potion of Speed on multiple characters, throw it only immediately before combat. |
| 4 | Put Globe of Invulnerability and Conjure Elemental scrolls on whichever caster is present at the fight. |
| 5 | Put invisibility tools, anti-caster arrows, and poisons on Astarion. |
| 6 | Confirm Lae'zel's Elixir of Bloodlust dose is real and has backup before counting on it. |
| 7 | Keep TMind's Divine Intervention unused unless the fight collapses. |
| 8 | Cast Heroes' Feast at camp before committing to the fight, once Lae'zel is rebuffed too. |
| 9 | With Astarion on Duellist's Prerogative (two reactions/turn), have Lae'zel spend Commander's Strike on him deliberately — see [[11_Main_Character_Builds#^laezel-build\|Lae'zel's build § Commander's Strike → Astarion Reaction Combo]]. Note the real cost: one of her own attacks plus her bonus action, not a freebie. |

## Source ^readiness-source

**Markers:** ⭐⭐ ⏱️

| Field | Current value |
|---|---|
| Save name | Campsite - 119h 03m |
| Save modified | 2026-08-31 19:40:51 +02:00 |
| Synced into handbook | 2026-08-31 21:39:47 +02:00 |
| Game version | 4.1.1.7398727 |
| Difficulty | DifficultyMedium / RulesetLarian |
| Source record | `tools/save-extract/source_manifest.json` |

## Parser Notes

**Markers:** ⭐ ⚠️

- This audit used the current `.lsf` index, not a refreshed `Globals.lsx` text export.
- Active buff detection is reliable for the four named party members because it reads their current status managers.
- Character identity was confirmed by matching each `Character` node's exact `Translate` position against the position reported for that character in `SaveInfo.json`; no decoy/duplicate nodes were found at any of the four positions this pass.
- **Lae'zel's multiclass is now save-confirmed**, not just player-reported — her `Classes` list shows Fighter (BattleMaster) and Cleric (WarDomain). The save format doesn't expose a per-class level split, so Fighter 11/Cleric 1 specifically is inferred, not directly read.
- **Known spells and maneuvers remain completely unreadable from this save index**, re-confirmed this pass by searching the full index for "maneuver" and "Rally" — zero matches. Only items, positions, and active statuses are extractable.
- **No inventory changes were found anywhere in the save this pass** — every item record was compared against the previous sync and matched exactly. This let two prior "not found anywhere" claims (The Joltshooter, Gleamdance Dagger) get corrected — both were simply missed before, not newly discovered.
- The broader save contains many `DYING` statuses on old or non-active entities; the active-party status managers for the four named characters do not show `DYING` in this save.
- Item counts are reliable for practical stock checks, but exact equipped slots still need in-game confirmation.
- Camp storage and world/storage-like inventories are summarized as "elsewhere" rather than by raw container or position.
