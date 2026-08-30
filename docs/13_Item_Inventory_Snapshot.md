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

- Source: `Campsite - 115h 34m`, modified `2026-08-30 01:29:40 +02:00`, synced into the handbook at `2026-08-30 01:34:23 +02:00`. A huge stretch of play happened (+10,500 XP each) and the party is split: Lae'zel and TMind at camp, Astarion and Kao at Ramazith's Tower (Sorcerous Sundries). Kao and Astarion each picked up a Legendary weapon this pass — see [[13_Item_Inventory_Snapshot#^inventory-new-finds|Item Ratings]] below.
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
| TMind | 324 | 29 | 19 | 26 | 25 | 30 | 195 |
| Lae'zel | 65 | 18 | 6 | 1 | 3 | 1 | 36 |
| Kao | 137 | 37 | 13 | 13 | 10 | 0 | 64 |
| Astarion | 199 | 49 | 17 | 36 | 23 | 3 | 71 |

Everyone's totals moved a lot this pass (a long shopping/looting stretch). Notably: TMind's Scrolls jumped 15 → 26 and Combat consumables 4 → 25 — worth a look in game since this is a big unexplained gain. Kao's Scrolls partially recovered (6 → 13), consistent with some of the long-standing hand-back from Astarion finally happening — see the resource spot check below. Murderous Cut is fully gone from both TMind and Astarion's carried lists (now only in storage) — the "wrong owner" issue resolved itself, one way or another.

## Current Resource Spot Check

| Resource | Latest visible count | Current holder(s) | Practical note |
|---|---:|---|---|
| Scroll of Revivify | 10 | Kao 1; storage 9 | Unchanged across five snapshots — still strong emergency stock; put one on at least two active characters. |
| Potion of Speed | 5 | Lae'zel 1; TMind 1; storage 3 | Up from 4. Still enough for a Haste opener. |
| Elixir of Bloodlust | 0 | — | **All spare bottles are gone** — Lae'zel's active buff is running on her last dose with no backup left. Restock before the next hard fight. |
| Potion of Invisibility | 6 | Kao 1; TMind 1; storage 4 | Up from 5. Workable for scouting/escapes. |
| Scroll of Globe of Invulnerability | 4 | TMind 2; Astarion 2 | Up from 2 and partially recovered — 2 are now with TMind instead of all on Astarion. Still worth consolidating onto Kao, who casts it. |
| Scroll of Conjure Elemental | 3 | TMind 1; Astarion 1; storage 1 | Up from 2, same partial-recovery pattern as above. |
| Healing potions | 42 | TMind 7; Astarion 8; Lae'zel 4; Kao 5; storage 18 | Up slightly from 39; nobody under-supplied. |

## Best Immediate Uses ^inventory-best-uses

| Use | Item | Current holder | Best fit | Note |
|---|---|---|---|---|
| ⭐⭐⭐ | **Markoheshkir** | Kao | Kao | Legendary staff: +1 spell DC/attack, a free spell 1/long rest with no slot cost, elemental buff, Topple. Should be his main weapon now. |
| ⭐⭐⭐ | Robe of the Weave | Kao | Kao | +2 AC, +1 spell DC/attack, heals on a successful spell save — upgrade over Infernal Robe |
| ⭐⭐⭐ | **Duellist's Prerogative** | Astarion | Astarion | Legendary rapier: crits on 19, extra reaction, bonus-action taunt+bleed, bonus-action extra attack — but a build fork away from dual daggers, decide deliberately |
| ⭐⭐⭐ | Devotee's Mace | TMind | TMind | healing-aura weapon |
| ⭐⭐⭐ | Shield of Devotion | TMind | TMind | spell slot + shield |
| ⭐⭐⭐ | The Whispering Promise | TMind | TMind | Bless on heal, concentration-free |
| ⭐⭐⭐ | Amulet of Restoration | TMind | TMind | healing support amulet |
| ⭐⭐⭐ | Moonlight Glaive | Lae'zel | Lae'zel | martial weapon |
| ⭐⭐⭐ | Killer's Sweetheart | Lae'zel | Lae'zel | frontline crit |
| ⭐⭐⭐ | Boots of Psionic Movement | Lae'zel | Lae'zel | Githyanki-only Fly + psychic damage |
| ⭐⭐⭐ | Cloak of Elemental Absorption | Kao | Kao | caster defense |
| ⭐⭐⭐ | Spineshudder Amulet | Kao | Kao | Reverberation rider |
| ⭐⭐⭐ | Cloak of Displacement | Astarion | Astarion | miss-chance survival |
| ⭐⭐⭐ | The Graceful Cloth | Astarion | Astarion | DEX / Cat's Grace |
| ⭐⭐⭐ | Scroll of Revivify | Kao | Any | emergency revive |
| ⭐⭐⭐ | Sword of the Emperor | Lae'zel | Lae'zel | +2 longsword, +2 to all saves vs spells — strong vs Act 3's caster-heavy fights |
| ⭐⭐⭐ | Chancer's Carcanet | Lae'zel | Lae'zel | reaction Advantage on an attack or save, 1/long rest |
| ⭐⭐⭐ | Shadow of Menzoberranzan | Astarion | Astarion | on-demand Invisibility — ideal for a Hide → Sneak Attack loop |
| ⭐⭐⭐ | Disintegrating Night Walkers | Astarion | Astarion | terrain immunity + free Misty Step every short rest |

The Incandescent Staff and The Joltshooter have dropped off this list — not because they got worse, but because Markoheshkir and Duellist's Prerogative are straightforwardly better weapons for Kao and Astarion respectively. Both old items are still fine backups (see their character sections).

## Item Ratings and Redistribution — this pass's new finds ^inventory-new-finds

Every named item picked up since the last full item audit is now verified against bg3.wiki and rated below. Effects are summarized in the table; **current holder** is where the save shows it right now, **recommended** is where it should go.

| Character | Item | Rating | Effect | Note |
|---|---|---|---|---|
| Kao | **Markoheshkir** | ⭐⭐⭐ | Legendary +2 Quarterstaff. +1 Spell Save DC/Attack, **Arcane Battery** (cast one spell 1/long rest for free, no slot spent), Kereska's Favour (elemental self-buff, short rest), Topple weapon action | **Equip as main weapon** — this is a top-tier staff |
| Kao | Robe of the Weave | ⭐⭐⭐ | Very Rare. +2 AC, +1 Spell Save DC/Attack, heals 1d6 HP when you succeed a spell saving throw | Upgrade over Infernal Robe |
| Kao | Staff of Interruption | ⭐⭐ | Rare +2 Quarterstaff. Cast Counterspell 1/long rest, Topple action | Competes with Markoheshkir for his hands — situational swap vs caster-heavy fights, can't use both at once |
| Kao | Fey Semblance Amulet | ⭐⭐ | Very Rare. Advantage on Intelligence, Wisdom, and Charisma saving throws | Solid defensive amulet, competes with Spineshudder/Strange Tendril for the slot |
| Kao | *(boss-dropped shield, name withheld)* | ⭐ (off-build) | Rare. +2 AC, Advantage on DEX saves, +1 Spell Save DC/Attack — matches a flagged spoiler-sensitive term so the name is omitted here | A shield doesn't fit a two-handed staff caster — carry for sale/swap, not equip |
| Astarion | **Duellist's Prerogative** | ⭐⭐⭐ (build fork) | Legendary +3 Rapier. Crits on 19 when not dual-wielding, an extra reaction/turn, bonus-action Challenge to Duel (taunt + Bleed), reaction Withering Cut (necrotic on hit), bonus-action extra attack | **Decide deliberately**: this is a one-handed rapier, not a dagger — it pulls him away from dual-dagger Thief toward a single-weapon duelist build. Very strong either way, but a real playstyle change. |
| Astarion | Salty Scimitar(rrr) | ⭐⭐ | Looted from Captain Grisly at The Blushing Mermaid. Command spell 1/long rest, Flourish/Lacerate actions if proficient | Decent, but outclassed by the rapier as a main-hand pick |
| Astarion | Ring Of Blink | ⭐⭐ | Rare. Cast Blink 1/long rest | Good escape/repositioning tool |
| Astarion | Winter's Clutches (gloves) | ⭐⭐ | Uncommon. Inflicts Encrusted with Frost on cold-damage hits | Minor rider, keep if he has cold sources |
| Astarion | Coldbrim Hat | ⭐ | Uncommon. Applies Encrusted with Frost when inflicting any condition | Minor, situational |
| Astarion | Gold Wyrmling Staff | ⭐ (off-build) | Rare +1 Quarterstaff, Fire Bolt cantrip | Not useful for a Rogue — sell |
| TMind | Scroll of Dethrone | ⭐⭐⭐ (situational) | Very Rare single-use scroll (or spellbook-transcribable, Level 5 slot, 1/long rest) | Save for a genuinely hard boss fight — verify its exact effect in game before relying on it, not fully confirmed here |
| Lae'zel | Amulet of Windrider | ⭐⭐ | Very Rare. Ride the Winds (Level 3, 1/long rest) + Gust of Wind (Level 2, 1/short rest) | Good mobility/control utility pickup |
| Lae'zel | Keepsake Ring | ⭐⭐ | Cast Dominate Beast, 1/long rest | Moved to her from TMind — decent flex control option for a frontliner |
| Kao / TMind | The Tharchiate Codex (×4 copies total: 2 with TMind, 1 with Astarion, plus its curse status) | Legendary book | Necromancy of Thay: a Constitution penalty, 20 temp HP after long rest, and Danse Macabre (summon 4 ghouls 1/long rest) once read | **Astarion has already read a copy and carries the curse.** TMind's two copies are unread — reading one applies the same trade-off to him too. Not permanent: **Remove Curse or Greater Restoration cures it** (bg3.wiki-confirmed) — TMind can likely self-cast Remove Curse as a Cleric. Decide who (if anyone else) should read it. |

**Confirmed done from last time**: the Hellfire Hand Crossbow, Shade-Slayer Cloak, and Vivacious Cloak moves all happened as recommended. The Ring of Salving / Cloak of Protection / Helmet of Arcane Acuity / Bloodguzzler Garb situation is unchanged — still with the same unidentified companion-type character near camp (same exact position both times checked now), not lost, not recoverable through this audit method. Murderous Cut is no longer carried by anyone (now only in storage) — the wrong-owner issue resolved itself.

**Redistribution to make**: Astarion still holds part of Kao's old scroll library, though some has come back — see the resource spot check above; Kao should still end up with the rest.

## TMind ^inventory-tmind

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Devotee's Mace | TMind | healing-aura weapon |
| ⭐⭐⭐ | Blood of Lathander | TMind | light aura / safety (effect active) |
| ⭐⭐⭐ | Shield of Devotion | TMind | spell slot + shield (active) |
| ⭐⭐⭐ | The Whispering Promise | TMind | Bless-on-heal ring, concentration-free |
| ⭐⭐⭐ | Amulet of Restoration | TMind | healing-support amulet |
| ⭐⭐ | Luminous Gloves | TMind | radiant / Radiating Orb synergy |
| ⭐⭐ | Pearl of Power Amulet | TMind / Kao | slot recovery |
| ⭐⭐ | Spellcrux Amulet | TMind / Kao | slot recovery |
| ⭐⭐ | Amulet of Misty Step | TMind | free repositioning |
| ⭐⭐ | Nymph Cloak | Kao / TMind | control utility |
| ⭐⭐ | The Spectator Eyes | TMind / Kao | spell utility |
| ⭐⭐ | Circle of Bones | TMind | defensive amulet |
| ⭐⭐ | Adamantine Scale Mail | TMind | no-crit heavy armour |
| ⭐⭐ | Boots of Speed | TMind | frontline mobility — he has no other boots, keep these rather than pass them along |
| — (×2, unread) | The Tharchiate Codex | TMind | Legendary necromancy book — see Item Ratings above; reading it applies the same curse Astarion now carries, curable with Remove Curse/Greater Restoration |

No longer carried: Murderous Cut and all 3 copies of the Whispering Mask are gone from TMind (now only in storage) — both resolved without needing manual intervention. Ring of Salving, Keepsake Ring (now with Lae'zel), Cloak of Protection, Helmet of Arcane Acuity, and Bloodguzzler Garb remain with the same unidentified companion-type character near camp, unchanged from last pass.

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Dethrone | 1 | TMind | Save for a genuinely hard boss fight — see Item Ratings above |
| ⭐⭐⭐ | Scroll of Globe of Invulnerability | 2 | Kao | New this pass — worth handing to Kao, who casts it |
| ⭐⭐ | Scroll of Conjure Elemental | 1 | Kao | New this pass, same reasoning |
| ⭐⭐⭐ | Potion of Speed | 1 | Lae'zel / group | decisive Haste — back after being gone a snapshot |
| ⭐⭐ | Potion of Invisibility | 1 | Astarion / scout | New this pass |
| ⭐⭐ | Elixir of Heroism | 1 | Any | temp HP + fear immunity opener — unchanged |
| ⭐ | Potion of Superior Healing | 2 | Any | situational — unchanged |
| ⭐ | Potion of Greater Healing | 1 | Any | situational — unchanged |
| ⭐ | Potion of Healing | 4 | Any | situational — up from 3 |

TMind's alchemy stock is holding at ≈30 records, still well below the ≈116 it was several snapshots ago. His Scrolls (15 → 26) and Combat consumables (4 → 25) both jumped a lot this pass — worth a look in game to see what specifically came in, beyond what's itemized above.

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
| ⭐⭐ | Cerebral Citadel Armour | Lae'zel | compare its AC to Adamantine Splint Armour before swapping |
| ⭐⭐ (bench) | Cindermoth Cloak | Lae'zel | unreliable retaliation burn |
| ⭐ | Vivacious Cloak | Lae'zel | guaranteed temp HP on initiative, the better default cloak over Cindermoth |
| ⭐⭐ | Amulet of Windrider | Lae'zel | new this pass — Ride the Winds + Gust of Wind, see Item Ratings above |
| ⭐⭐ | Keepsake Ring | Lae'zel | new this pass, moved from TMind — Dominate Beast 1/long rest |

No longer carried: Cerebral Citadel Gloves is gone from her position (not found elsewhere either) — possibly sold or otherwise removed.

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Potion of Speed | 1 | Lae'zel / group | unchanged |
| ⭐ | Potion of Superior Healing | 1 | Any | situational — unchanged |
| ⭐ | Potion of Greater Healing | 1 | Any | situational — unchanged |

No longer carried: her **Elixir of Bloodlust spare bottle is gone** — this was the last one in the entire party's inventory (see the resource spot check above). The active buff is running on borrowed time with no backup left.

## Kao ^inventory-kao

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ | Markoheshkir | Kao | Legendary staff — see Item Ratings above, equip as main weapon |
| ⭐⭐⭐ | Robe of the Weave | Kao | +2 AC, +1 spell DC/attack, heals on spell-save success |
| ⭐⭐⭐ | Cloak of Elemental Absorption | Kao | caster defense (Absorb Elements, active) |
| ⭐⭐⭐ | Spineshudder Amulet | Kao | Reverberation on spell hit |
| ⭐⭐ | Staff of Interruption | Kao | Counterspell 1/long rest — situational swap-in, see Item Ratings above |
| ⭐⭐ | Fey Semblance Amulet | Kao | Advantage on INT/WIS/CHA saves |
| ⭐⭐ | Circlet of Mental Anguish | Kao | psychic control rider |
| ⭐⭐ | Ring of Mental Inhibition | Kao | psychic support |
| ⭐⭐ | Hr'a'cknir Bracers | Kao | telekinesis / utility |
| ⭐⭐ | Strange Tendril Amulet | Kao | control amulet |
| ⭐ | Incandescent Staff | Kao | now a backup weapon, outclassed by Markoheshkir |
| ⭐ | Infernal Robe | Kao | now a backup robe, outclassed by Robe of the Weave |
| ⭐ | Bonespike Boots | Kao | situational boots |
| ⭐ | True Love's Caress | Kao | confirmed dead weight for now — the matching True Love's Embrace ring is on an NPC, not in storage |
| ⭐ | Swiresy Shoes | Kao | +5ft jump, +1 Acrobatics — exploration convenience only |
| ⭐ (off-build) | *(boss-dropped shield, name withheld)* | Kao | doesn't fit a two-handed staff caster — carry for sale, not equip |

No longer carried: Necklace of Elemental Augmentation has moved to Astarion's position — an odd fit for a Rogue, worth moving back to Kao if it was accidental.

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Revivify | 1 | Any | emergency revive — unchanged |
| ⭐⭐ | Scroll of Bestow Curse | 2 | Kao | back with Kao this pass |
| ⭐⭐ | Scroll of Crown of Madness | 1 | Kao | back with Kao this pass |
| ⭐ | Antitoxin | 2 | Any | unchanged |
| ⭐ | Potion of Superior / Greater Healing | 3 | Any | situational — up from 2 |

Kao's scroll library has partially recovered (≈6 → 13) — some of what Astarion was holding has come back, though the Globe of Invulnerability and Conjure Elemental scrolls specifically are still split between TMind and Astarion (see the resource spot check above). No longer carried: his Elixir of Universal Resistance is still gone, unchanged from before.

## Astarion ^inventory-astarion

### Equipment and Build Fit

| Use | Item | Best fit | Note |
|---|---|---|---|
| ⭐⭐⭐ (build fork) | Duellist's Prerogative | Astarion | Legendary rapier — see Item Ratings above, a deliberate build decision |
| ⭐⭐⭐ | Cloak of Displacement | Astarion | miss-chance survival (active) |
| ⭐⭐⭐ | The Graceful Cloth | Astarion | DEX / Cat's Grace (active) |
| ⭐⭐⭐ | Shadow of Menzoberranzan | Astarion | on-demand Invisibility — ideal for a Hide → Sneak Attack loop |
| ⭐⭐⭐ | Disintegrating Night Walkers | Astarion | terrain immunity + free Misty Step every short rest |
| ⭐⭐ | Salty Scimitar(rrr) | Astarion | looted from Captain Grisly at The Blushing Mermaid — good but outclassed by the rapier as main-hand |
| ⭐⭐ | Ring Of Blink | Astarion | cast Blink 1/long rest |
| ⭐⭐ | Stillmaker | Astarion | poison dagger option |
| ⭐⭐ | Ring of Shadows | Astarion | stealth / shadow utility |
| ⭐⭐ | Stalker Gloves | Astarion | on-hit sneak-attack support |
| ⭐⭐ | Periapt of Wound Closure | Astarion | scout survival |
| ⭐⭐ | Shifting Corpus Ring | Astarion | miss-chance defensive ring |
| ⭐⭐ | Winter's Clutches | Astarion | frost-rider gloves, new this pass |
| ⭐⭐ | Hellfire Hand Crossbow | Astarion | burn chance while Hiding/Invisible |
| ⭐⭐⭐ | Shade-Slayer Cloak | Astarion | lower crit threshold while Hiding |
| ⭐ | King's Knife | Astarion | dagger option |
| ⭐ | Coldbrim Hat | Astarion | minor frost rider, new this pass |
| ⭐ | *(radiant-themed ring, name withheld)* | Astarion | Light cantrip on demand — utility only, matches a flagged spoiler-sensitive term so the name is omitted here |
| ⭐ (off-build) | Gold Wyrmling Staff | Astarion | a caster weapon, no use for a Rogue — sell |
| ⭐⭐ (misplaced) | Necklace of Elemental Augmentation | Kao | landed on Astarion this pass — elemental cantrip boost belongs on Kao, not a Rogue |

No longer carried: **The Joltshooter and Gleamdance Dagger are both gone** from his position — not found elsewhere in the save either. Worth checking in game whether these were sold, given away, or are just equipped in a way this extraction doesn't catch.

### Consumables and Scrolls

| Use | Item | Qty | Best fit | Note |
|---|---|---:|---|---|
| ⭐⭐ | Scroll of Invisibility | 1 | Kao / Astarion | escape or setup — unchanged |
| ⭐⭐ | Elixir of Fire / Psychic Resistance | 2 | Any | elemental prep — unchanged (1 Fire, 1 Psychic) |
| ⭐⭐ | Scroll of Protection from Energy | 1 | Any | elemental defense — unchanged |
| ⭐⭐ | Full elemental arrow set | 9 (1 each) | Astarion | fire, ice, acid, darkness, detonation, teleportation, antimagic, smokepowder, construct- and monstrosity-slaying — unchanged |
| ⭐ | Potion of Superior / Greater Healing | 6 | Any | unchanged |
| ⭐ | Antitoxin | 1 | Any | unchanged |

Good news: the Globe of Invulnerability, Conjure Elemental, Bestow Curse, and Crown of Madness scrolls he'd been holding are **no longer all stuck here** — most have moved back toward Kao/TMind this pass (see the resource spot check above and Kao's section). No longer carried: Murderous Cut is gone (now only in storage) — the earlier wrong-owner issue resolved itself.

## Camp Storage ^camp-storage

Storage holds the overflow (2,860 item records, up from ~2,650) — most of it is generic gear and crafting stock. Pull only what supports the next fight, the current build, or the camp-buff routine.

### Priority Pulls from Storage

| Use | Item | Qty seen | Best fit | Why pull it |
|---|---|---:|---|---|
| ⭐⭐⭐ | Scroll of Revivify | 9 | Any | Unchanged. Emergency revive stock; spread across active characters. |
| ⭐⭐⭐ | Potion of Speed | 3 | Lae'zel / group | Up from 2 — TMind's carried copy landed here. Extra decisive-Haste openers. |
| ⭐⭐ | Potion of Invisibility | 4 | Astarion / scout | Down from 8 (half used). Scouting, resets, and escapes. |
| ⭐⭐ | Scroll of Conjure Elemental | 1 | Kao | Down from 2. Extra action economy for hard fights. |
| ⭐⭐ | Potion of Supreme Healing | 2 | Any | Unchanged. Highest-tier emergency heal. |
| ⭐⭐ | Scroll of Speak with Dead | 4 | Any | Unchanged. Investigation utility. |
| ⭐ | Healing potions (basic/greater/superior) | 15 | Split across party | Top up anyone before leaving camp. |
| ⭐ | Assorted caster scrolls | many | Kao | Blur, Mirror Image, Hold Person, Fireball, Misty Step, etc. — browse before a caster fight. |

No longer in storage: the spare Elixir of Bloodlust that was here is gone — the only remaining bottle is the one Lae'zel is now carrying herself (see her Consumables and Scrolls above).

### Notable Gear Sitting in Storage ^storage-notable-gear

**Re-checked this pass** against the new save with the same `Level`-field-plus-`Character`-node method used to catch the earlier mistake. Two changes since last audit:

- **The Tharchiate Codex is resolved** — it's no longer sitting uncollected. Two copies are now confirmed in inventory: one with TMind (unread), one that Astarion picked up and read (source of his new curse — see his Equipment section above).
- **Reaper's Embrace is no longer genuinely free storage.** It now sits at a camp position with a co-located, resurrected `Character` node that is none of the four tracked party members — most likely a benched companion. That means it's probably sitting in *that companion's* personal inventory, not shared camp storage, and needs checking at their portrait in game before assuming it can just be pulled.

**Genuinely in storage**: none confirmed this pass — the one item that qualified last time (Reaper's Embrace) no longer does, per above.

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
| Reaper's Embrace | Very Rare | **New this pass**: moved from "storage" to sitting with a resurrected, unidentified companion-type character at camp — check that companion's own inventory in game rather than the shared storage container |

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
