---
title: "Current Item and Storage Snapshot"
aliases:
  - Item Inventory Snapshot
  - Available Items
  - Camp Storage
  - Camp Chest Audit
  - Storage Audit
tags:
  - bg3
  - handbook
  - inventory
  - save
  - snapshot
---

# Current Item and Storage Snapshot

This note summarizes practical active-party and camp-storage items visible in the extracted save. It is spoiler-light: story books, quest keys, and ambiguous world-state objects are intentionally not expanded into a walkthrough list.

> [!info] Navigation
> Previous: [Current Save Snapshot](12_Current_Save_Snapshot.md) | Home: [Baldur's Gate 3 Practical Handbook](../README.md) | Next: [Current Readiness Audit](14_Current_Readiness_Audit.md)

## Contents

| Need | Jump to |
|---|---|
| Understand scope and ratings | [[#Scope\|Scope]] · [[#Rating Key\|Rating Key]] · [[#Character Summary\|Character Summary]] |
| Highest-value actions | [[13_Item_Inventory_Snapshot#^inventory-best-uses\|Best Immediate Uses]] |
| Review a character | [[13_Item_Inventory_Snapshot#^inventory-tmind\|TMind]] · [[13_Item_Inventory_Snapshot#^inventory-laezel\|Lae'zel]] · [[13_Item_Inventory_Snapshot#^inventory-kao\|Kao]] · [[13_Item_Inventory_Snapshot#^inventory-astarion\|Astarion]] |
| Pull or consolidate stored items | [[13_Item_Inventory_Snapshot#^camp-storage\|Camp Storage]] · [[13_Item_Inventory_Snapshot#^storage-notable-gear\|Notable Gear in Storage]] |
| Understand omissions | [[13_Item_Inventory_Snapshot#^inventory-omissions\|Hidden From This Practical List]] |

## Scope

- Source: `Lower City - 118h 27m`, modified `2026-08-31 01:13:19 +02:00`, synced into the handbook at `2026-08-31 08:42:08 +02:00`. The party's split flipped location: TMind and Lae'zel are together in Lower City proper; Kao and Astarion are together at Baldur's Mouth Basement (already Level 12, ahead of TMind/Lae'zel who have the XP but haven't leveled up yet — see [Current Save Snapshot](12_Current_Save_Snapshot.md)).
- Item names were resolved from the game's own root templates and localization, so display names match in game.
- Holder is position-based: an item counts for TMind, Lae'zel, Kao, or Astarion when it sits at that character's active-party position; everything else is bucketed as `storage`. **`storage` is not the same as "in camp storage"** — it also includes items still lying uncollected in the world and items held by NPCs (companions, vendors, enemies) who aren't one of the four tracked characters. The bulk counts in Character Summary, the resource spot check, and Camp Storage below inherit this imprecision; only individually-verified items (like [[13_Item_Inventory_Snapshot#^storage-notable-gear|Notable Gear Sitting in Storage]]) have been checked against the save's `Level` field and nearby `Character` nodes to confirm they're actually sitting in the party's own storage.
- Only build-relevant magic gear is listed per character. Generic default weapons/armour, camp clothes, books, and keys are omitted.
- Exact equipped-vs-carried slots still need in-game confirmation; this is a carried/available snapshot.
- **This pass also caught a coverage gap, not just a state change**: several items on TMind and Kao (Circle of Bones, The Spectator Eyes, Adamantine Scale Mail, Strange Tendril Amulet, and others below) turn out to have already been sitting in their inventories in prior snapshots without ever being listed here. They're written up now as a backlog catch-up, not as new acquisitions — noted per item where relevant.

## Rating Key

| Marker | Meaning |
|---|---|
| ⭐⭐⭐ | High-impact item for current builds or hard fights |
| ⭐⭐ | Good or situationally strong |
| ⭐ | Low priority, utility, or build-dependent |

## Character Summary

Totals are position-based item records from the current save (approximate category labels — recomputed this pass with a slightly different heuristic than before, so treat the sub-category split as directional, not exact).

| Character | Total | Equipment | Potions / elixirs | Scrolls | Combat consumables | Alchemy | Utility / keys |
|---|---:|---:|---:|---:|---:|---:|---:|
| TMind | 194 | 33 | 7 | 28 | 7 | 2 | 117 |
| Lae'zel | 149 | 23 | 36 | 14 | 5 | 1 | 70 |
| Kao | 269 | 27 | 13 | 13 | 5 | 33 | 178 |
| Astarion | 143 | 32 | 19 | 29 | 7 | 1 | 55 |

Big swings across the board this pass: TMind's total dropped 324 → 194 and Astarion's dropped 199 → 143, while Kao's roughly doubled (137 → 269) and Lae'zel's more than doubled (65 → 149). Consistent with a long, active stretch of play across two different locations rather than a single anomaly — a lot moved between characters and into/out of storage. Individual moves worth knowing about are called out per character below.

## Current Resource Spot Check

| Resource | Latest visible count | Current holder(s) | Practical note |
|---|---:|---|---|
| Scroll of Revivify | 11 | TMind 2; Lae'zel 1; Kao 1; Astarion 1; storage 6 | Up from 10 and now spread across **all four** characters plus storage — the best distribution yet, no action needed. |
| Potion of Speed | 4 | TMind 1; Astarion 1; storage 2 | Down slightly from 5, still enough for a Haste opener. |
| Elixir of Bloodlust | 0 | — | **Still zero anywhere in the save.** Lae'zel's active buff finally ran out this pass with nothing to refill it — see her Active Practical Buffs. |
| Potion of Invisibility | 7 | Lae'zel 2; Kao 1; Astarion 1; storage 3 | Up from 6, healthy stock. |
| Scroll of Globe of Invulnerability | 2 | TMind 2 | Down from 4 — Astarion's 2 copies are gone (used or moved, not tracked elsewhere). Still not with Kao, who casts it. |
| Scroll of Conjure Elemental | 3 | TMind 1; Astarion 1; storage 1 | Unchanged. |
| Scroll of Bestow Curse | 2 | Astarion 2 | **Reversed again** — this had moved back to Kao last pass, now it's on Astarion once more. Same long-running back-and-forth as the rest of Kao's scroll library. |
| Healing potions (basic/greater/superior/supreme) | 36 | TMind 5; Lae'zel 4; Kao 5; Astarion 5; storage 17 | Down from 42 but evenly spread; nobody under-supplied. |

## Best Immediate Uses ^inventory-best-uses

| Use | Item | Current holder | Best fit | Note |
|---|---|---|---|---|
| ⭐⭐⭐ | **Markoheshkir** | Kao | Kao | Legendary staff: +1 spell DC/attack, a free spell 1/long rest with no slot cost, elemental buff, Topple. Should be his main weapon now. |
| ⭐⭐⭐ | Robe of the Weave | Kao | Kao | +2 AC, +1 spell DC/attack, heals on a successful spell save — upgrade over Infernal Robe |
| ⭐⭐⭐ | **Duellist's Prerogative** | Astarion | Astarion | Legendary rapier: crits on 19, extra reaction, bonus-action taunt+bleed, bonus-action extra attack — a loadout swap (empty off-hand), not a build fork; see [[11_Main_Character_Builds#^astarion-build\|Astarion's build]] |
| ⭐⭐⭐ | **Circle of Bones** | TMind | TMind | Rare circlet: Animate Dead (1/long rest) + Undead Ward (nearby allied undead resist Bludgeoning/Slashing/Piercing) — a near-perfect fit for a Death Domain necromancer, only surfaced in the audit this pass |
| ⭐⭐⭐ | **Adamantine Scale Mail** | TMind | TMind | Very Rare medium armour: all incoming damage -1, immune to critical hits, attacker gets Reeling for 2 turns — exceptional defensive upgrade, only surfaced this pass |
| ⭐⭐⭐ | Devotee's Mace | TMind | TMind | healing-aura weapon |
| ⭐⭐⭐ | Shield of Devotion | TMind | TMind | spell slot + shield |
| ⭐⭐⭐ | The Whispering Promise | TMind | TMind | Bless on heal, concentration-free |
| ⭐⭐⭐ | Reaper's Embrace | Lae'zel | Lae'zel | Very Rare heavy armour: forced-movement immunity, fear aura, flat damage reduction — now confirmed in her own inventory, no longer a mystery |
| ⭐⭐⭐ | Moonlight Glaive | Lae'zel | Lae'zel | martial weapon |
| ⭐⭐⭐ | Killer's Sweetheart | Lae'zel | Lae'zel | frontline crit |
| ⭐⭐⭐ | Boots of Psionic Movement | Lae'zel | Lae'zel | Githyanki-only Fly + psychic damage |
| ⭐⭐⭐ | Cloak of Elemental Absorption | Kao | Kao | caster defense |
| ⭐⭐⭐ | Cloak of Displacement | Astarion | Astarion | miss-chance survival |
| ⭐⭐⭐ | The Graceful Cloth | Astarion | Astarion | DEX / Cat's Grace |
| ⭐⭐⭐ | Scroll of Revivify | TMind / Lae'zel / Kao / Astarion | Any | emergency revive — now spread across all four, keep it that way |
| ⭐⭐⭐ | Sword of the Emperor | Lae'zel | Lae'zel | +2 longsword, +2 to all saves vs spells — strong vs Act 3's caster-heavy fights |
| ⭐⭐⭐ | Chancer's Carcanet | Lae'zel | Lae'zel | reaction Advantage on an attack or save, 1/long rest |
| ⭐⭐⭐ | Shadow of Menzoberranzan | Astarion | Astarion | on-demand Invisibility — ideal for a Hide → Sneak Attack loop |
| ⭐⭐⭐ | Disintegrating Night Walkers | Astarion | Astarion | terrain immunity + free Misty Step every short rest |

Spineshudder Amulet dropped off this list — it rewards ranged *spell attack* hits, but Kao's core kit (Web, Grease, Hold Person) mostly forces saves rather than rolling attacks, so it's a weaker fit than it first looked. See the Kao section for the full amulet comparison; he now has five competing amulet options.

## Item Ratings and Redistribution — this pass's new finds and coverage catch-up ^inventory-new-finds

Two kinds of rows below: genuinely new acquisitions this pass, and items confirmed against bg3.wiki that turned out to already be in someone's inventory from an earlier snapshot but were never rated (marked **catch-up**).

| Character | Item | Rating | Effect | Note |
|---|---|---|---|---|
| TMind | **Circle of Bones** (catch-up) | ⭐⭐⭐ | Rare Circlet. Animate Dead 1/long rest; nearby allied undead resist Bludgeoning/Slashing/Piercing | Strong direct fit for the Death Domain necromancer identity |
| TMind | **Adamantine Scale Mail** (catch-up) | ⭐⭐⭐ | Very Rare medium armour. All incoming damage -1, immune to Critical Hits, attacker gets Reeling (2 turns) on a melee hit against you | One of the best defensive pieces in the game; needs Medium Armour proficiency |
| TMind | Nymph Cloak (catch-up) | ⭐⭐ | Very Rare. Dominate Person, 1/long rest | Strong control option, competes for cloak slot |
| TMind | The Spectator Eyes (catch-up) | ⭐⭐ | Very Rare Amulet. Ray of Fear and Wounding Ray, each 1/long rest | Competes with Amulet of Restoration / Pearl of Power / Amulet of Misty Step / Spellcrux Amulet — five amulets now, only one slot |
| TMind | Amulet of Restoration (catch-up) | ⭐⭐ | Rare. Healing Word and Mass Healing Word, each 1/long rest, bonus action | Same amulet-slot competition as above |
| TMind | Amulet of Misty Step (catch-up) | ⭐⭐ | Uncommon. Misty Step, 1/short rest | Same amulet-slot competition |
| TMind | Eversight Ring (catch-up; save shows it as `MAG_Shadow_BlindImmunity_Ring`, unresolved display name) | ⭐⭐ | Uncommon. Immune to Blinded; also sees through magical darkness | Solid defensive/utility ring |
| TMind | Pearl of Power Amulet (catch-up) | ⭐ | Uncommon. Restore one spell slot of 3rd level or lower, 1/long rest | Lowest priority of the five competing amulets |
| TMind | Luminous Gloves (catch-up) | ⭐ | Uncommon. +1 Strength save; Radiating Orb on radiant damage dealt | Minor — depends on TMind actually dealing radiant damage |
| TMind | Salty Scimitar(rrr) | ⭐ (off-build) | Moved here from Astarion this pass. Command 1/long rest, Flourish/Lacerate if proficient | Doesn't fit a mace-and-shield Cleric — carry for sale or hand to whoever ends up using a scimitar |
| Lae'zel | **Reaper's Embrace** | ⭐⭐⭐ | Very Rare heavy armour: forced-movement immunity, fear aura, flat damage reduction | Now physically confirmed in her inventory — the "unidentified companion" mystery resolved itself for this one item, see Camp Storage below |
| Kao | Strange Tendril Amulet (catch-up) | ⭐⭐ | Rare. Evard's Black Tentacles, 1/long rest | Good control option, fits his Conjuration identity; competes with Fey Semblance for the amulet slot |
| Kao | Ring of Mental Inhibition (catch-up) | ⭐⭐ | Uncommon. On a target's failed save against your spell/ability, apply Mental Fatigue (2 turns; stacking penalty to INT/WIS/CHA saves, can trigger 1d4 Psychic damage) | Synergizes with a control Wizard forcing saves constantly — bg3.wiki notes it also affects allies, so use with care |
| Kao | Circlet of Mental Anguish (catch-up) | ⭐⭐ | Rare. Heal 1d4 HP when a target fails an INT/WIS/CHA save against your spell/cantrip | Passive sustain that rewards the same save-forcing playstyle |
| Kao | Hr'a'cknir Bracers (catch-up) | ⭐⭐ | Very Rare gloves. Mage Hand as a Bonus Action; Telekinesis 1/short rest | Solid utility, Telekinesis is a genuinely useful control/environment tool |
| Kao | Spineshudder Amulet (catch-up) | ⭐ | Uncommon. Reverberation (2 turns) on a ranged spell *attack* hit | Weaker than it looks — most of Kao's core spells force saves, not attack rolls |
| Astarion | Fetish of Callarduran Smoothhands (save shows it as `UND_DeadInWater_CallarduranTrinket`, unresolved display name) | ⭐ | Rare Ring. Invisibility, 1/long rest | Backup Invisibility source, but ring slots are already crowded (Ring of Shadows, Ring Of Blink, Shifting Corpus Ring) |
| Astarion | Summon Golem Bell, Spider's Lyre, *(a secret-elevator ring, name withheld — spoiler-flagged location)*, Lute of the Merryweather Bard | — | Quest/location-specific or cosmetic items tied to areas or NPCs likely behind the party now (a boss-adjacent summon, a Shadow-Cursed Lands guide item, a secret-passage ring, a cosmetic instrument) | Safe to leave in storage or discard, not rated as active-build equipment |

**Confirmed done from last time**: Duellist's Prerogative and Markoheshkir are both equipped and rated. **Reversed this pass**: Scroll of Bestow Curse and Scroll of Crown of Madness moved back onto Astarion after coming home to Kao last time — the scroll-library hand-off between them keeps flip-flopping (now five snapshots running); worth a deliberate one-time decision instead of letting it keep drifting. **Gold Wyrmling Staff is resolved** — the one copy previously flagged "off-build, sell" on Astarion is gone from him, and two copies now sit in storage (sold or stored, consistent with the earlier recommendation either way).

## TMind ^inventory-tmind

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Circle of Bones | TMind | Animate Dead + Undead Ward — see Item Ratings above, newly surfaced this pass |
| ⭐⭐⭐ | Adamantine Scale Mail | TMind | no-crit medium armour, damage reduction, Reeling rider — see Item Ratings above |
| ⭐⭐⭐ | Devotee's Mace | TMind | healing-aura weapon |
| ⭐⭐⭐ | Blood of Lathander | TMind | light aura / safety (no longer shows as an active status — likely not the currently equipped weapon) |
| ⭐⭐⭐ | Shield of Devotion | TMind | spell slot + shield (active) |
| ⭐⭐⭐ | The Whispering Promise | TMind | Bless-on-heal ring, concentration-free |
| ⭐⭐ | The Spectator Eyes | TMind | Ray of Fear + Wounding Ray — competes for amulet slot, see below |
| ⭐⭐ | Amulet of Restoration | TMind | Healing Word + Mass Healing Word — competes for amulet slot |
| ⭐⭐ | Amulet of Misty Step | TMind | free repositioning — competes for amulet slot |
| ⭐⭐ | Spellcrux Amulet | TMind / Kao | slot recovery — competes for amulet slot |
| ⭐⭐ | Nymph Cloak | TMind / Kao | Dominate Person control |
| ⭐⭐ | Eversight Ring | TMind | Blind immunity, sees through magical darkness |
| ⭐ | Pearl of Power Amulet | TMind | slot recovery, lowest priority of the amulet options |
| ⭐ | Luminous Gloves | TMind | radiant / Radiating Orb synergy |
| ⭐ | Boots of Speed | TMind | frontline mobility — he has no other boots, keep these rather than pass them along |
| ⭐ (off-build) | Salty Scimitar(rrr) | TMind | moved here from Astarion this pass; doesn't fit a mace Cleric, carry for sale |
| — (×2, unread) | The Tharchiate Codex | TMind | Legendary necromancy book — see Item Ratings above; reading it applies the same curse Astarion carries, curable with Remove Curse/Greater Restoration |

**TMind now has five items competing for one amulet slot**: The Spectator Eyes, Amulet of Restoration, Amulet of Misty Step, Spellcrux Amulet, and Pearl of Power. All five are genuinely useful in different ways (utility spells, healing backup, mobility, slot recovery, minor slot recovery) — worth picking one deliberately rather than leaving it to whichever was equipped last. Spellcrux Amulet (spell slot restoration at higher levels) is likely still the strongest pick for a support Cleric, with The Spectator Eyes or Amulet of Restoration as the next-best alternatives depending on whether utility spells or backup healing matters more that day.

No longer carried: Murderous Cut and all 3 copies of the Whispering Mask are gone from TMind (now only in storage) — both resolved without needing manual intervention.

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Dethrone | 1 | TMind | Save for a genuinely hard boss fight — see Item Ratings above |
| ⭐⭐⭐ | Scroll of Revivify | 2 | TMind | Now spread across the whole party, see resource spot check above |
| ⭐⭐ | Scroll of Globe of Invulnerability | 2 | Kao | Still not with Kao, who actually casts it |
| ⭐⭐ | Scroll of Conjure Elemental | 1 | Kao | Same reasoning |
| ⭐⭐⭐ | Potion of Speed | 1 | Lae'zel / group | decisive Haste opener |
| ⭐ | Healing potions (basic/greater/superior) | ~4 | Any | steady, no action needed |

TMind's inventory shrank a lot this pass (324 → 194 total records) even as several previously-uncatalogued equipment pieces surfaced — consistent with a large redistribution/shopping stretch rather than losses. Worth a look in game to confirm nothing important dropped out unintentionally.

## Lae'zel ^inventory-laezel

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | **Reaper's Embrace** | Lae'zel | Very Rare heavy armour — now confirmed in her own inventory, see Item Ratings above |
| ⭐⭐⭐ | Moonlight Glaive | Lae'zel | martial weapon |
| ⭐⭐⭐ | Killer's Sweetheart | Lae'zel | frontline crit (active) |
| ⭐⭐⭐ | Adamantine Splint Armour | Lae'zel | no-crit heavy armour — now has a real alternative in Reaper's Embrace, worth comparing |
| ⭐⭐⭐ | Sword of the Emperor | Lae'zel | +2 longsword, +2 saves vs spells |
| ⭐⭐⭐ | Boots of Psionic Movement | Lae'zel | Githyanki-only Fly + psychic damage |
| ⭐⭐⭐ | Chancer's Carcanet | Lae'zel | guaranteed Advantage on a save or attack, 1/long rest |
| ⭐⭐ | Amulet of Branding | Lae'zel | melee debuff |
| ⭐⭐ | Braindrain Gloves | Lae'zel | psychic-rider option |
| ⭐⭐ | Crossbow of Arcane Force | Lae'zel | ranged fallback |
| ⭐⭐ | Cerebral Citadel Armour | Lae'zel | compare its AC to Adamantine Splint Armour / Reaper's Embrace before swapping |
| ⭐⭐ | Amulet of Windrider | Lae'zel | Ride the Winds + Gust of Wind |
| ⭐⭐ | Keepsake Ring | Lae'zel | Dominate Beast 1/long rest |
| ⭐⭐ (bench) | Cindermoth Cloak | Lae'zel | unreliable retaliation burn |
| ⭐ | Grymskull Helm | Lae'zel | situational helm |
| ⭐ | Vivacious Cloak | Lae'zel | guaranteed temp HP on initiative, the better default cloak over Cindermoth |

**Armour decision now has three options**: Adamantine Splint Armour (no-crit), Reaper's Embrace (forced-movement immunity + fear aura + flat reduction), and Cerebral Citadel Armour — worth comparing all three in game against her current build rather than assuming the no-crit piece is automatically best now that Reaper's Embrace is actually available.

No longer carried: Corpsegrinder is confirmed in genuine camp storage (checked last pass, still true). Cerebral Citadel Gloves' status is unresolved — see [[13_Item_Inventory_Snapshot#^storage-notable-gear|Notable Gear Sitting in Storage]] for a methodology note on that one rather than a repeated claim.

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Potion of Invisibility | 2 | Lae'zel / scout | new this pass |
| ⭐ | Healing potions | 4 | Any | steady |

No longer carried: her **Elixir of Bloodlust spare bottle is gone**, and now the active buff itself has expired too (no longer in her Active Practical Buffs) — the last dose in the entire party's inventory finally ran out. Restock before relying on it again.

## Kao ^inventory-kao

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Markoheshkir | Kao | Legendary staff — see Item Ratings above, equip as main weapon |
| ⭐⭐⭐ | Robe of the Weave | Kao | +2 AC, +1 spell DC/attack, heals on spell-save success |
| ⭐⭐⭐ | Cloak of Elemental Absorption | Kao | caster defense (Absorb Elements, active) |
| ⭐⭐ | Staff of Interruption | Kao | Counterspell 1/long rest — situational swap-in |
| ⭐⭐ | Strange Tendril Amulet | Kao | Evard's Black Tentacles 1/long rest — competes for amulet slot |
| ⭐⭐ | Fey Semblance Amulet | Kao | Advantage on INT/WIS/CHA saves — competes for amulet slot |
| ⭐⭐ | Circlet of Mental Anguish | Kao | psychic control rider |
| ⭐⭐ | Ring of Mental Inhibition | Kao | psychic support, applies to allies too — use carefully |
| ⭐⭐ | Hr'a'cknir Bracers | Kao | Mage Hand bonus action + Telekinesis 1/short rest |
| ⭐ | Spineshudder Amulet | Kao | rewards spell *attacks*, weaker fit than it looks — competes for amulet slot |
| ⭐ | Incandescent Staff | Kao | now a backup weapon, outclassed by Markoheshkir |
| ⭐ | Infernal Robe | Kao | now a backup robe, outclassed by Robe of the Weave |
| ⭐ | Bonespike Boots | Kao | situational boots |
| ⭐ | True Love's Caress | Kao | confirmed dead weight for now — the matching True Love's Embrace ring is on an NPC, not in storage |
| ⭐ | Swiresy Shoes | Kao | +5ft jump, +1 Acrobatics — exploration convenience only |
| ⭐ (off-build) | *(boss-dropped shield, name withheld)* | Kao | doesn't fit a two-handed staff caster — carry for sale, not equip |

**Kao now has three items competing for the amulet slot**: Strange Tendril Amulet (control), Fey Semblance Amulet (defensive saves), and Spineshudder Amulet (weaker fit, low priority). Fey Semblance or Strange Tendril are the two worth actually alternating; Spineshudder can go to storage.

No longer carried: Necklace of Elemental Augmentation is still on Astarion's position, unchanged — an odd fit for a Rogue, still worth moving to Kao if it was accidental (see Astarion's section).

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Revivify | 1 | Any | emergency revive |
| ⭐ | Potion of Superior / Greater Healing | ~2 | Any | situational |

Kao's total item count roughly doubled this pass (137 → 269, mostly alchemy and utility records) — most of the gain is generic stock, not build-relevant. His scroll library is still split with Astarion and TMind (Globe of Invulnerability, Conjure Elemental) and now Bestow Curse/Crown of Madness have swung back to Astorion — see the resource spot check above.

## Astarion ^inventory-astarion

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Duellist's Prerogative | Astarion | Legendary rapier — see Item Ratings above; a loadout swap (empty off-hand), not a build fork |
| ⭐⭐⭐ | Cloak of Displacement | Astarion | miss-chance survival (active) |
| ⭐⭐⭐ | The Graceful Cloth | Astarion | DEX / Cat's Grace (active) |
| ⭐⭐⭐ | Shadow of Menzoberranzan | Astarion | on-demand Invisibility — ideal for a Hide → Sneak Attack loop |
| ⭐⭐⭐ | Disintegrating Night Walkers | Astarion | terrain immunity + free Misty Step every short rest |
| ⭐⭐⭐ | Shade-Slayer Cloak | Astarion | lower crit threshold while Hiding |
| ⭐⭐ | Ring Of Blink | Astarion | cast Blink 1/long rest |
| ⭐⭐ | Stillmaker | Astarion | poison dagger option |
| ⭐⭐ | Ring of Shadows | Astarion | stealth / shadow utility |
| ⭐⭐ | Stalker Gloves | Astarion | on-hit sneak-attack support |
| ⭐⭐ | Periapt of Wound Closure | Astarion | scout survival |
| ⭐⭐ | Shifting Corpus Ring | Astarion | miss-chance defensive ring |
| ⭐⭐ | Winter's Clutches | Astarion | frost-rider gloves |
| ⭐⭐ | Hellfire Hand Crossbow | Astarion | burn chance while Hiding/Invisible |
| ⭐ | King's Knife | Astarion | dagger option |
| ⭐ | Coldbrim Hat | Astarion | minor frost rider |
| ⭐ | Fetish of Callarduran Smoothhands | Astarion | backup Invisibility ring — ring slots already crowded, see Item Ratings above |
| ⭐ | *(radiant-themed ring, name withheld)* | Astarion | Light cantrip on demand — utility only, matches a flagged spoiler-sensitive term so the name is omitted here |
| ⭐⭐ (misplaced) | Necklace of Elemental Augmentation | Kao | still landed on Astarion, unchanged — elemental cantrip boost belongs on Kao, not a Rogue |

No longer carried: **Salty Scimitar(rrr) moved to TMind** this pass — see TMind's section (a genuine downgrade fit-wise; consider moving it to storage instead, since neither current holder can really use it). **The Joltshooter and Gleamdance Dagger are still gone**, unconfirmed elsewhere. **Gold Wyrmling Staff is resolved** — no longer with him, two copies now sit in storage. Also newly present but not rated as build gear: Summon Golem Bell, Spider's Lyre, a secret-elevator ring (name withheld above), and Lute of the Merryweather Bard — see Item Ratings above for why these are quest/cosmetic leftovers rather than active equipment.

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐ | Scroll of Bestow Curse | 2 | Kao | **back on Astarion this pass** — reversed from last snapshot, see the resource spot check above |
| ⭐⭐ | Scroll of Crown of Madness | 1 | Kao | same reversal |
| ⭐⭐ | Elixir of Fire / Psychic Resistance | 2 | Any | elemental prep — unchanged (1 Fire, 1 Psychic) |
| ⭐⭐ | Full elemental arrow set | ~9 | Astarion | fire, ice, acid, darkness, detonation, teleportation, antimagic, smokepowder, construct- and monstrosity-slaying — unchanged |
| ⭐ | Potion of Superior / Greater Healing | ~5 | Any | unchanged |

No longer carried: Murderous Cut is gone (now only in storage) — the earlier wrong-owner issue stays resolved.

## Camp Storage ^camp-storage

Storage holds the overflow (2,968 item records, up from 2,860) — most of it is generic gear and crafting stock. Pull only what supports the next fight, the current build, or the camp-buff routine.

### Priority Pulls from Storage

| Use | Item | Qty seen | Best fit | Why pull it |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Revivify | 6 | Any | Down from 9 (more copies moved into active carry, a good sign). |
| ⭐⭐⭐ | Potion of Speed | 2 | Lae'zel / group | Down from 3. Extra decisive-Haste openers. |
| ⭐⭐ | Potion of Invisibility | 3 | Astarion / scout | Down from 4. Scouting, resets, and escapes. |
| ⭐⭐ | Scroll of Conjure Elemental | 1 | Kao | Unchanged. Extra action economy for hard fights. |
| ⭐⭐ | Scroll of Speak with Dead | 4 | Any | Unchanged. Investigation utility. |
| ⭐⭐ | Gold Wyrmling Staff | 2 | — | Now confirmed in storage (moved off Astarion) — sell, not a fit for anyone in the current party. |
| ⭐ | Healing potions (basic/greater/superior) | 17 | Split across party | Top up anyone before leaving camp. |
| ⭐ | Corpsegrinder | 1 | — | Confirmed genuinely in storage since last pass (drifted off Lae'zel). |
| ⭐ | Assorted caster scrolls | many | Kao | Blur, Mirror Image, Hold Person, Fireball, Misty Step, etc. — browse before a caster fight. |

### Notable Gear Sitting in Storage ^storage-notable-gear

**A methodology note worth reading before trusting this section further**: this cluster of items has now been re-labeled twice — first "genuinely in storage," then corrected to "held by an unidentified companion" after a `Character` node showed up at the exact same coordinates, and now this pass that companion node has moved roughly 23 units away while the items stayed exactly where they were. That's evidence the items were never actually *in the companion's personal inventory* — more likely a stationary container the companion happened to be standing near in an earlier snapshot. Rather than re-label this a third time from position data alone, the honest answer is: **check this cluster directly in game** (both the nearby companion's portrait and the camp storage chest) rather than trust another position-based inference here.

| Item | Rarity | Status |
|---|---|---|
| Ring of Salving, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb ×2, Cerebral Citadel Gloves | Mixed | Still sitting at the same fixed camp coordinates as the last two audits. The previously-nearby companion has since moved away from that spot — check both the companion and camp storage directly in game rather than relying on this audit's location guess. |
| **Reaper's Embrace** | Very Rare | **Resolved** — no longer part of this cluster; confirmed this pass as genuinely in Lae'zel's own inventory. |

**Still lying uncollected in the world** (never picked up — not accessible from storage or any character):

| Item | Rarity | Where |
|---|---|---|
| Ring of Evasion | Very Rare | Somewhere in `WLD_Main_A` (Act 1 world map) |
| Blade of the First Blood ("Bloodthirst") | Legendary | Somewhere in `CTY_Main_A`, two copies |
| Crimson Mischief | Legendary | Somewhere in `CTY_Main_A` |

**Held by an NPC, not the party** — would need to be looted, pickpocketed, or traded for, not just moved from storage:

| Item | Rarity | Held by |
|---|---|---|
| Voss' Silver Sword | Very Rare | **Voss**, a live Githyanki NPC (also carrying a Githyanki Crossbow and Leather Half-Plate) |
| Silver Sword of the Astral Plane | Legendary | Also on Voss |
| Staff of Cherished Necromancy | Very Rare | An unidentified NPC |
| Robe of Supreme Defences | Very Rare | An unidentified NPC |
| Woe | Very Rare | An unidentified NPC — its internal save-data name references a late-game vampire-lord boss |
| Penumbral Armour | Rare | An unidentified NPC |
| True Love's Embrace | Rare | Two separate copies exist, each on a different unidentified NPC — **not** freely available for pairing with TMind's True Love's Caress as previously claimed |

### Storage Handling Routine

1. Before a hard fight, check camp storage for the ⭐⭐⭐ priority pulls.
2. Put Revivify scrolls on at least two different active characters.
3. Move caster scrolls and spell-slot elixirs to Kao.
4. Move invisibility tools, arrows, and scouting consumables to Astarion.
5. Move martial elixirs to Lae'zel.
6. Keep healing-support gear together for TMind (or Shadowheart if she is the active support).
7. Leave books, keys, story objects, and generic containers untouched unless a quest or vendor cleanup needs them.

### Storage Uncertainty

- The save shows storage-like inventories, but exact in-game container labels should be confirmed at camp.
- If an item cannot be found quickly in game, search camp storage by item name instead of by container.
- The Ring of Salving cluster above is a concrete example of this audit method's limits — see the note in Notable Gear Sitting in Storage.

## Hidden From This Practical List ^inventory-omissions

- Quest keys, most books/notes, camp clothing, plain torches, generic default weapons/armour, and obvious containers are not expanded in the character sections.
- Alchemy ingredients and ⭐ situational scrolls are summarized as counts rather than listed item by item.
- Camp storage is summarized only by practical priority, not by raw save location.
