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

- Source: `Campsite - 106h 12m`, modified `2026-08-16 02:02:22 +02:00`, synced into the handbook at `2026-08-16 11:29:07 +02:00`. The whole party leveled up to 11 and is back at camp, about six hours of play after the previous pass.
- Item names were resolved from the game's own root templates and localization, so display names match in game.
- Holder is position-based: an item counts for TMind, Lae'zel, Kao, or Astarion when it sits at that character's active-party position; everything else is bucketed as `storage`. **`storage` is not the same as "in camp storage"** — it also includes items still lying uncollected in the world and items held by NPCs (companions, vendors, enemies) who aren't one of the four tracked characters. The bulk counts in Character Summary, the resource spot check, and Camp Storage below inherit this imprecision; only individually-verified items (like [[13_Item_Inventory_Snapshot#^storage-notable-gear|Notable Gear Sitting in Storage]]) have been checked against the save's `Level` field and nearby `Character` nodes to confirm they're actually sitting in the party's own storage.
- Only build-relevant magic gear is listed per character. Generic default weapons/armour, camp clothes, books, and keys are omitted.
- Exact equipped-vs-carried slots still need in-game confirmation; this is a carried/available snapshot.

## Rating Key

| Marker | Meaning |
|---|---|
| ⭐⭐⭐ | High-impact item for current builds or hard fights |
| ⭐⭐ | Good or situationally strong |
| ⭐ | Low priority, utility, or build-dependent |

## Character Summary

Totals are position-based item records from the current save (approximate category labels).

| Character | Total | Equipment | Potions / elixirs | Scrolls | Combat consumables | Alchemy | Utility / keys |
|---|---:|---:|---:|---:|---:|---:|---:|
| TMind | 270 | 32 | 11 | 22 | 3 | 30 | 172 |
| Lae'zel | 79 | 23 | 7 | 1 | 6 | 1 | 41 |
| Kao | 150 | 38 | 9 | 6 | 11 | 0 | 86 |
| Astarion | 140 | 30 | 12 | 26 | 23 | 0 | 49 |

Kao handed off a chunk of his scroll library this pass — his Scrolls dropped from 33 to 6, while Astarion's rose from 6 to 26. That includes the Scroll of Globe of Invulnerability and Scroll of Conjure Elemental — see the resource spot check below, this is worth reversing since Kao is the one who casts them.

## Current Resource Spot Check

| Resource | Latest visible count | Current holder(s) | Practical note |
|---|---:|---|---|
| Scroll of Revivify | 10 | Kao 1; storage 9 | Unchanged across three snapshots — still strong emergency stock; put one on at least two active characters. |
| Potion of Speed | 4 | TMind 1; Lae'zel 1; storage 2 | Unchanged. Still enough for a Haste opener; throw immediately before combat. |
| Elixir of Bloodlust | 1 | Lae'zel 1 | Unchanged. The buff is still active on Lae'zel from an earlier dose; only one spare bottle left — don't drink it casually. |
| Potion of Invisibility | 5 | Kao 1; storage 4 | Unchanged. Still workable for scouting/escapes, but restock before relying on it for a hard fight. |
| Scroll of Globe of Invulnerability | 2 | Astarion 2 | **Moved from Kao to Astarion this pass.** Kao is the one who casts it — worth moving back unless this was deliberate. |
| Scroll of Conjure Elemental | 2 | Astarion 1; storage 1 | **Moved from Kao to Astarion this pass**, same as above. |
| Healing potions | 39 | Astarion 8; TMind 5; Lae'zel 4; Kao 4; storage 18 | Up slightly. Astarion is now carrying noticeably more than everyone else — still fine, just uneven. |

## Best Immediate Uses ^inventory-best-uses

| Use | Item | Current holder | Best fit | Note |
|---|---|---|---|---|
| ⭐⭐⭐ | Devotee's Mace | TMind | TMind | healing-aura weapon |
| ⭐⭐⭐ | Shield of Devotion | TMind | TMind | spell slot + shield |
| ⭐⭐⭐ | The Whispering Promise | TMind | TMind | Bless on heal, concentration-free |
| ⭐⭐⭐ | Amulet of Restoration | TMind | TMind | healing support amulet |
| ⭐⭐⭐ | Moonlight Glaive | Lae'zel | Lae'zel | martial weapon |
| ⭐⭐⭐ | Killer's Sweetheart | Lae'zel | Lae'zel | frontline crit |
| ⭐⭐⭐ | Boots of Psionic Movement | Lae'zel | Lae'zel | new since last snapshot — replaced Boots of Speed at her position; see note below |
| ⭐⭐⭐ | Incandescent Staff | Kao | Kao | caster damage staff |
| ⭐⭐⭐ | Cloak of Elemental Absorption | Kao | Kao | caster defense |
| ⭐⭐⭐ | Spineshudder Amulet | Kao | Kao | Reverberation rider |
| ⭐⭐⭐ | Cloak of Displacement | Astarion | Astarion | miss-chance survival |
| ⭐⭐⭐ | The Graceful Cloth | Astarion | Astarion | DEX / Cat's Grace |
| ⭐⭐⭐ | The Joltshooter | Astarion | Astarion | ranged option |
| ⭐⭐⭐ | Scroll of Revivify | Kao | Any | emergency revive |
| ⭐⭐⭐ | Scroll of Globe of Invulnerability x2 | Astarion | Kao | boss defense — moved off Kao this pass, see the resource spot check above |
| ⭐⭐⭐ | Elixir of Bloodlust | Lae'zel | Lae'zel | already active |
| ⭐⭐⭐ | Potion of Speed | Lae'zel | Lae'zel / group | decisive Haste |
| ⭐⭐⭐ | Ring of Salving | TMind | TMind | +2 HP on every heal cast — direct upgrade to his core job |
| ⭐⭐⭐ | Sword of the Emperor | Lae'zel | Lae'zel | +2 longsword, +2 to all saves vs spells — strong vs Act 3's caster-heavy fights |
| ⭐⭐⭐ | Chancer's Carcanet | Lae'zel | Lae'zel | reaction Advantage on an attack or save, 1/long rest |
| ⭐⭐⭐ | Shadow of Menzoberranzan | Astarion | Astarion | on-demand Invisibility — ideal for a Hide → Sneak Attack loop |
| ⭐⭐⭐ | Disintegrating Night Walkers | Astarion | Astarion | terrain immunity + free Misty Step every short rest |

## Item Ratings and Redistribution — this pass's new finds ^inventory-new-finds

Every named item picked up since the last full item audit is now verified against bg3.wiki and rated below, replacing the earlier "not yet rated" placeholders. Effects are summarized in the table; **current holder** is where the save shows it right now, **recommended** is where it should actually go.

| Character | Item | Rating | Effect | Current holder | Recommended |
|---|---|---|---|---|---|
| TMind | Ring of Salving | ⭐⭐⭐ | +2 HP restored whenever you heal another creature | TMind | **Keep on TMind** |
| TMind | Keepsake Ring | ⭐⭐ | Cast Dominate Beast, 1/long rest | TMind | Keep as a flex control option |
| TMind | Boots of Speed | ⭐⭐ | Movement-speed boost | TMind (idle) | **Keep on TMind** — he has no dedicated boots, no reason to move these |
| TMind | Hellfire Hand Crossbow | ⭐ (wrong owner) | Chance to set target Burning when attacking from Hide/Invisible | TMind (idle) | **→ Astarion** — TMind isn't a stealth attacker |
| TMind | Shade-Slayer Cloak | ⭐ (wrong owner) | Lower crit threshold while Hiding, stacking | TMind (idle) | **→ Astarion** — wasted on a melee cleric |
| TMind | Bloodguzzler Garb | ⭐ (fits nobody) | Grants Wrath (bonus **unarmed** strikes) when hit | TMind (idle) | Nobody in this party fights unarmed — bench or sell |
| Lae'zel | Sword of the Emperor | ⭐⭐⭐ | +2 Longsword, +1d4 vs shapeshifters/polymorphed, +2 to all saves vs spells | Lae'zel | **Keep** |
| Lae'zel | Boots of Psionic Movement | ⭐⭐⭐ | Githyanki-only: free Fly 1/long rest, +1 DEX save, bonus psychic damage on the melee hit after flying | Lae'zel | **Keep** — she's the party's only Githyanki, this is built for her |
| Lae'zel | Chancer's Carcanet | ⭐⭐⭐ | Reaction: Advantage on an attack roll or save, 1/long rest | Lae'zel | **Keep** |
| Lae'zel | Cerebral Citadel Gloves | ⭐⭐ (conditional) | +1d4 to attack rolls/saves after Charming or Frightening a creature | Lae'zel | Keep only if she has a Frighten-causing Battle Master maneuver (e.g. Menacing Attack) — check in game |
| Lae'zel | Cerebral Citadel Armour | ⭐⭐ (unverified) | Matching illithid-themed set piece, exact AC not confirmed | Lae'zel | Compare its AC in game before swapping off Adamantine Splint Armour — that armour's no-crit protection is hard to beat |
| Lae'zel | Cindermoth Cloak | ⭐⭐ (bench) | Retaliation Burning on nearby melee attackers, but the save is rolled by the *wearer*, not the attacker — unreliable at her level | Lae'zel | Swap for the incoming Vivacious Cloak (see below) |
| Kao | True Love's Caress | ⭐ (situational) | Receive Warding Bond from whoever wears the matching True Love's Embrace ring, 1/long rest | Kao | Only useful if the matching ring turns up (check storage) — otherwise dead weight |
| Kao | Swiresy Shoes | ⭐ | +5ft jump distance, +1 Acrobatics | Kao | Minor exploration convenience only |
| Astarion | Murderous Cut | ⭐⭐ | +1 Dagger, +1d4 piercing vs targets at ≤50% HP | Astarion | **Keep** — good off-hand execute option |
| Astarion | *(radiant-themed ring, name withheld — spoiler-flagged term)* | ⭐ | Casts the Light cantrip on demand; can be unequipped afterward and the light persists | Astarion | Pure utility, no combat value |

**Redistribution to make**: TMind → Astarion (Hellfire Hand Crossbow, Shade-Slayer Cloak); TMind → Lae'zel (Vivacious Cloak, replacing Cindermoth Cloak); Astarion → Kao (Scroll of Globe of Invulnerability ×2, Scroll of Conjure Elemental — already flagged above). Bloodguzzler Garb doesn't fit anyone's current build.

## TMind ^inventory-tmind

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Devotee's Mace | TMind | healing-aura weapon |
| ⭐⭐⭐ | Blood of Lathander | TMind | light aura / safety (effect active) |
| ⭐⭐⭐ | Shield of Devotion | TMind | spell slot + shield (active) |
| ⭐⭐⭐ | The Whispering Promise | TMind | Bless-on-heal ring, concentration-free |
| ⭐⭐⭐ | Amulet of Restoration | TMind | healing-support amulet |
| ⭐⭐ | Cloak of Protection | TMind | general defense |
| ⭐⭐ | Helmet of Arcane Acuity | TMind | weapon-then-cast setups |
| ⭐⭐ | Luminous Gloves | TMind | radiant / Radiating Orb synergy |
| ⭐⭐ | Pearl of Power Amulet | TMind / Kao | slot recovery |
| ⭐⭐ | Spellcrux Amulet | TMind / Kao | slot recovery |
| ⭐⭐ | Amulet of Misty Step | TMind | free repositioning |
| ⭐⭐ | Nymph Cloak | Kao / TMind | control utility |
| ⭐⭐ | The Spectator Eyes | TMind / Kao | spell utility |
| ⭐⭐ | Circle of Bones | TMind | defensive amulet |
| ⭐⭐ | Adamantine Scale Mail | TMind | no-crit heavy armour |
| ⭐⭐⭐ | Ring of Salving | TMind | +2 HP on every heal cast — see Item Ratings above |
| ⭐⭐ | Keepsake Ring | TMind | Dominate Beast 1/long rest, flex control |
| ⭐⭐ | Boots of Speed | TMind | frontline mobility — he has no other boots, keep these rather than pass them along |
| ⭐ (wrong owner) | Vivacious Cloak | Lae'zel | temp HP on initiative — recommend moving to Lae'zel, see Item Ratings above |
| ⭐ (wrong owner) | Hellfire Hand Crossbow | Astarion | Hide/Invisible burn proc — recommend moving to Astarion |
| ⭐ (wrong owner) | Shade-Slayer Cloak | Astarion | crit-while-Hiding — recommend moving to Astarion |
| ⭐ (fits nobody) | Bloodguzzler Garb | — | Wrath on unarmed strikes — nobody in this party fights unarmed; bench or sell |

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Potion of Speed | 1 | Lae'zel / group | decisive Haste — unchanged |
| ⭐⭐ | Elixir of Heroism | 1 | Any | temp HP + fear immunity opener — unchanged |
| ⭐ | Potion of Superior Healing | 2 | Any | situational — unchanged |
| ⭐ | Potion of Greater Healing | 1 | Any | situational — unchanged |
| ⭐ | Potion of Healing | 3 | Any | situational — unchanged |

No longer carried: Elixir of Bloodlust and Elixir of Universal Resistance are both gone from TMind's inventory (and not found anywhere else in the save) — used up since the last snapshot.

TMind's alchemy stock is back down to ≈30 records, still well below the ≈116 it was three snapshots ago.

## Lae'zel ^inventory-laezel

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Moonlight Glaive | Lae'zel | martial weapon |
| ⭐⭐⭐ | Killer's Sweetheart | Lae'zel | frontline crit (active) |
| ⭐⭐⭐ | Adamantine Splint Armour | Lae'zel | no-crit heavy armour |
| ⭐⭐ | Amulet of Branding | Lae'zel | melee debuff |
| ⭐⭐ | Braindrain Gloves | Lae'zel | psychic-rider option |
| ⭐⭐ | Crossbow of Arcane Force | Lae'zel | ranged fallback |
| ⭐⭐ | Corpsegrinder | Lae'zel | martial weapon option |
| ⭐ | Grymskull Helm | Lae'zel | situational helm |
| ⭐⭐⭐ | Sword of the Emperor | Lae'zel | +2 longsword, +2 saves vs spells — see Item Ratings above |
| ⭐⭐⭐ | Boots of Psionic Movement | Lae'zel | Githyanki-only Fly + psychic damage — correctly replaced Boots of Speed |
| ⭐⭐⭐ | Chancer's Carcanet | Lae'zel | guaranteed Advantage on a save or attack, 1/long rest |
| ⭐⭐ | Cerebral Citadel Gloves | Lae'zel | conditional on a Frighten-causing maneuver — see Item Ratings above |
| ⭐⭐ | Cerebral Citadel Armour | Lae'zel | compare its AC to Adamantine Splint Armour before swapping |
| ⭐⭐ (bench) | Cindermoth Cloak | Lae'zel | unreliable retaliation burn — swap for the incoming Vivacious Cloak from TMind |

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Potion of Speed | 1 | Lae'zel / group | down from 2 — one used |
| ⭐⭐⭐ | Elixir of Bloodlust | 1 | Lae'zel | spare, in addition to the dose already active on her |
| ⭐ | Potion of Superior Healing | 1 | Any | situational — unchanged |
| ⭐ | Potion of Greater Healing | 1 | Any | situational — unchanged |

No longer carried: her Elixir of Hill Giant Strength is gone (not found anywhere in the save) — used up.

## Kao ^inventory-kao

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Incandescent Staff | Kao | caster damage staff |
| ⭐⭐⭐ | Cloak of Elemental Absorption | Kao | caster defense (Absorb Elements, active) |
| ⭐⭐⭐ | Spineshudder Amulet | Kao | Reverberation on spell hit |
| ⭐⭐ | Necklace of Elemental Augmentation | Kao | elemental cantrip boost |
| ⭐⭐ | Circlet of Mental Anguish | Kao | psychic control rider |
| ⭐⭐ | Ring of Mental Inhibition | Kao | psychic support |
| ⭐⭐ | Hr'a'cknir Bracers | Kao | telekinesis / utility |
| ⭐⭐ | Strange Tendril Amulet | Kao | control amulet |
| ⭐ | Infernal Robe | Kao | robe option |
| ⭐ | Bonespike Boots | Kao | situational boots |
| ⭐ | True Love's Caress | Kao | needs the matching True Love's Embrace ring elsewhere — check storage, otherwise dead weight |
| ⭐ | Swiresy Shoes | Kao | +5ft jump, +1 Acrobatics — exploration convenience only |

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Revivify | 1 | Any | emergency revive — unchanged |
| ⭐ | Antitoxin | 2 | Any | new this pass |
| ⭐ | Potion of Superior / Greater Healing | 2 | Any | situational — unchanged |

**Handed off since the last snapshot**: Kao's Scroll of Globe of Invulnerability (×2), Scroll of Conjure Elemental, Scroll of Bestow Curse (×2), Scroll of Crown of Madness, and Scroll of Invisibility are all now with Astarion instead — see his Consumables and Scrolls below. Kao's scroll library dropped from ≈31 to just 6 as a result. If that wasn't a deliberate strategy shift (e.g. loading Astarion up before he goes off to scout or sell), it's worth moving the boss-defense and summon scrolls back to Kao, who is the one who casts them.

No longer carried: his Elixir of Universal Resistance is gone (not found anywhere in the save, along with TMind's copy) — used up.

## Astarion ^inventory-astarion

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Cloak of Displacement | Astarion | miss-chance survival (active) |
| ⭐⭐⭐ | The Graceful Cloth | Astarion | DEX / Cat's Grace (active) |
| ⭐⭐⭐ | The Joltshooter | Astarion | ranged / lightning option |
| ⭐⭐ | Gleamdance Dagger | Astarion | main-hand dagger |
| ⭐⭐ | Stillmaker | Astarion | poison dagger option |
| ⭐⭐ | Ring of Shadows | Astarion | stealth / shadow utility |
| ⭐⭐ | Stalker Gloves | Astarion | on-hit sneak-attack support |
| ⭐⭐ | Periapt of Wound Closure | Astarion | scout survival |
| ⭐⭐ | Shifting Corpus Ring | Astarion | miss-chance defensive ring |
| ⭐ | King's Knife | Astarion | dagger option |
| ⭐⭐⭐ | Shadow of Menzoberranzan | Astarion | on-demand Invisibility — ideal for a Hide → Sneak Attack loop |
| ⭐⭐⭐ | Disintegrating Night Walkers | Astarion | terrain immunity + free Misty Step every short rest |
| ⭐⭐ | Murderous Cut | Astarion | +1d4 piercing vs targets at ≤50% HP — good off-hand execute option |
| ⭐ | *(radiant-themed ring, name withheld)* | Astarion | Light cantrip on demand — utility only, matches a flagged spoiler-sensitive term so the name is omitted here |
| ⭐⭐ (incoming) | Hellfire Hand Crossbow | TMind → here | burn chance while Hiding/Invisible — recommended move from TMind |
| ⭐⭐⭐ (incoming) | Shade-Slayer Cloak | TMind → here | lower crit threshold while Hiding — recommended move from TMind |

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Globe of Invulnerability | 2 | Kao | boss defense — **moved from Kao this pass, recommend moving back** |
| ⭐⭐⭐ | Scroll of Conjure Elemental | 1 | Kao | action economy — **moved from Kao this pass, recommend moving back** |
| ⭐⭐ | Scroll of Bestow Curse | 2 | Kao | debuff — moved from Kao this pass |
| ⭐⭐ | Scroll of Crown of Madness | 1 | Kao | control — moved from Kao this pass |
| ⭐⭐ | Scroll of Invisibility | 1 | Kao / Astarion | escape or setup — moved from Kao this pass |
| ⭐⭐ | Elixir of Fire / Psychic Resistance | 2 | Any | elemental prep — unchanged (1 Fire, 1 Psychic) |
| ⭐⭐ | Scroll of Protection from Energy | 1 | Any | elemental defense — unchanged |
| ⭐⭐ | Full elemental arrow set | 9 (1 each) | Astarion | fire, ice, acid, darkness, detonation, teleportation, antimagic, smokepowder, construct- and monstrosity-slaying — unchanged |
| ⭐ | Potion of Superior / Greater Healing | 6 | Any | up from 4 |
| ⭐ | Antitoxin | 1 | Any | unchanged |

Astarion is now carrying most of Kao's old scroll library — see the note in Kao's section above about whether that was intentional. No longer carried: his Elixir of Cloud Giant Strength is gone (used up). His Potion of Animal Speaking is also gone from inventory — matches the still-active Animal Speaking buff on him (he drank it); 3 more copies are sitting in camp storage if he wants it again.

## Camp Storage ^camp-storage

Storage holds the overflow (~2,650 item records) — most of it is generic gear and crafting stock. Pull only what supports the next fight, the current build, or the camp-buff routine.

### Priority Pulls from Storage

| Use | Item | Qty seen | Best fit | Why pull it |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Revivify | 9 | Any | Unchanged. Emergency revive stock; spread across active characters. |
| ⭐⭐⭐ | Potion of Speed | 2 | Lae'zel / group | Down from 3. Extra decisive-Haste openers. |
| ⭐⭐ | Potion of Invisibility | 4 | Astarion / scout | Down from 8 (half used). Scouting, resets, and escapes. |
| ⭐⭐ | Scroll of Conjure Elemental | 1 | Kao | Down from 2. Extra action economy for hard fights. |
| ⭐⭐ | Potion of Supreme Healing | 2 | Any | Unchanged. Highest-tier emergency heal. |
| ⭐⭐ | Scroll of Speak with Dead | 4 | Any | Unchanged. Investigation utility. |
| ⭐ | Healing potions | 18 | Split across party | Down from 23. Top up anyone before leaving camp. |
| ⭐ | Assorted caster scrolls | many | Kao | Blur, Mirror Image, Hold Person, Fireball, Misty Step, etc. — browse before a caster fight. |

No longer in storage: the spare Elixir of Bloodlust that was here is gone — the only remaining bottle is the one Lae'zel is now carrying herself (see her Consumables and Scrolls above).

### Notable Gear Sitting in Storage ^storage-notable-gear

**Correction (this pass)**: an earlier version of this section wrongly claimed 11 of these 12 items were freely available in camp storage. Position-matching alone can't tell storage apart from an NPC's inventory or an item still lying uncollected in the world — the save's `Level` field is the actual signal (empty = genuinely in *some* inventory; set to a map id = still lying in that level, uncollected) and a matching `Character` node at the same position means it's in *that* NPC's inventory, not the party's. Only one of the original twelve holds up under that check.

**Genuinely in storage** — no NPC nearby, position matches camp, previously picked up from the Shadow-Cursed Lands:

| Character | Item | Rarity | Effect | Note |
|---|---|---|---|---|
| Lae'zel | Reaper's Embrace | Very Rare | Heavy armor: immunity to forced movement, fear aura that numbs nearby enemies, flat damage reduction | Alternative to Adamantine Splint Armour's no-crit protection — different defensive profile, not strictly better |

**Still lying uncollected in the world** (never picked up — not accessible from storage or any character):

| Item | Rarity | Where |
|---|---|---|
| Ring of Evasion | Very Rare | Somewhere in `WLD_Main_A` (Act 1 world map) |
| The Tharchiate Codex | Legendary (book) | Somewhere in `CTY_Main_A` (Baldur's Gate) |
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

## Hidden From This Practical List ^inventory-omissions

- Quest keys, most books/notes, camp clothing, plain torches, generic default weapons/armour, and obvious containers are not expanded in the character sections.
- Alchemy ingredients and ⭐ situational scrolls are summarized as counts rather than listed item by item.
- Camp storage is summarized only by practical priority, not by raw save location.
