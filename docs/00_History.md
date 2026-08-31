---
title: "Handbook History"
aliases:
  - History
  - Changelog
  - What's New
tags:
  - bg3
  - handbook
  - maintenance
  - history
---

# 🕰️ Handbook History

This note records meaningful handbook changes so it is clear what was added, refreshed, or reorganized.

Use newest entries first. Keep entries practical: what changed, why it matters, and which notes were touched.

Where the change lives in a specific section, link the exact heading (`[[11_Main_Character_Builds#^astarion-build|Astarion's build]]`) instead of just the file — in Obsidian and on the site, that click jumps straight to the change instead of the top of the file. Use a `^block-id` anchor where one already exists on the heading; a plain heading-text anchor (`[[chronicle#Wyll — The Blade of Frontiers]]`) also resolves if no block-id is set. Link the whole file only when the change isn't tied to one section (e.g. a new tool, a site-wide feature).

Group each date's entries into collapsible topic nodes using a callout, not `### Added`/`### Changed`/`### Fixed` headings: `> [!note]- 🎒 Topic Name` followed by `> `-prefixed bullets. **Don't use raw `<details>` HTML** — the site's renderer passes that through untouched and never resolves the wikilinks/markdown links inside it; only the `> [!note]-` callout form runs the bullets through the real parser. Reuse a topic across dates rather than inventing new ones — the recurring set so far: 🎒 Save Snapshots & Readiness, 🗡️ Gear Ratings & Redistribution, 📖 Handbook Content & Builds, 🛠️ Tooling & Site Infrastructure, 🔒 Corrections & Maintenance.

## 2026-08-31

> [!note]- 🎒 Save Snapshots & Readiness (Lower City - 118h 27m, split flipped, pending level-ups)
> - Synced forward to `Lower City - 118h 27m` and rewrote [Current Save Snapshot](12_Current_Save_Snapshot.md), the [[13_Item_Inventory_Snapshot#^inventory-best-uses|Item and Storage Snapshot]], and [[14_Current_Readiness_Audit#^readiness-verdict|Readiness Audit]] against it.
> - **The party's split flipped location**: TMind and Lae'zel are now together in Lower City proper; Kao and Astarion are together at Baldur's Mouth Basement (a different spot than last pass's Ramazith's Tower).
> - **Kao and Astarion are already Level 12**; TMind and Lae'zel have the XP for it too but the save still shows them at Level 11 — read as a pending, unclaimed level-up rather than an extraction bug, since the two with *more* total XP are the ones still showing the lower level.
> - Buff coverage now splits along **location**, not by character: Death Ward stayed with the Baldur's Mouth pair (Kao, Astarion) and dropped off the Lower City pair (TMind, Lae'zel). Aid split the same way but paired differently (Kao and TMind have it; Astarion and Lae'zel don't). Longstrider dropped off Lae'zel specifically, and her Elixir of Bloodlust has now actually **expired** — not just out of spares, confirmed missing from her status list.
> - Astarion's Tharchiate Codex curse status changed internal ID (`CURSEDTOME_THARCHIATE_CODEX` → `CURSEDTOME_THARCHIATE_TECHNICAL`) — treated as the same curse rather than a new effect, flagged as unconfirmed rather than asserted.

> [!note]- 🗡️ Gear Ratings & Redistribution (a coverage-gap catch-up, not just new finds)
> - **Found a real gap in past audits**: several items on TMind (Circle of Bones, Adamantine Scale Mail, The Spectator Eyes, Amulet of Restoration, Amulet of Misty Step, Eversight Ring, Pearl of Power Amulet, Luminous Gloves, Nymph Cloak) and Kao (Strange Tendril Amulet, Ring of Mental Inhibition, Circlet of Mental Anguish, Hr'a'cknir Bracers, Spineshudder Amulet) turn out to have already been in their inventories in prior snapshots without ever being rated here. All now researched against bg3.wiki and added — most notably **Circle of Bones** and **Adamantine Scale Mail** for TMind, both ⭐⭐⭐ and a near-perfect fit for his Death Domain necromancer build.
> - **Reaper's Embrace is resolved** — no longer a mystery-companion item, confirmed genuinely in Lae'zel's own inventory this pass, giving her a real third armour option alongside Adamantine Splint Armour and Cerebral Citadel Armour.
> - TMind now has **five items competing for one amulet slot** and Kao has **three** — documented as explicit slot competitions rather than listing them as if all equipped simultaneously.
> - Salty Scimitar(rrr) drifted from Astarion to TMind — doesn't fit either build (empty-off-hand rapier Astarion, mace-and-shield TMind), flagged to just sell it. Gold Wyrmling Staff is fully resolved (two copies now in storage, none carried). Scroll of Bestow Curse/Crown of Madness swung back onto Astarion — the fifth reversal of this same back-and-forth with Kao's scroll library.
> - **The Ring of Salving cluster hit the limit of what position data can tell us**: the previously-nearby "unidentified companion" has now moved ~23 units away while the seven items stayed exactly where they were — evidence they were never in that companion's personal inventory, just near a fixed container. That's a second correction on the same fact, so per the standing house rule this wasn't patched a third time from inference alone — the docs now say plainly to check it in game instead of trusting another audit guess.

## 2026-08-30

> [!note]- 🎒 Save Snapshots & Readiness (Campsite - 115h 34m, split party, all buff gaps resolved)
> - Synced a large jump forward — `Campsite - 115h 34m`, ~10,500 XP each — and rewrote [Current Save Snapshot](12_Current_Save_Snapshot.md), the [[13_Item_Inventory_Snapshot#^inventory-best-uses|Item and Storage Snapshot]], and [[14_Current_Readiness_Audit#^readiness-verdict|Readiness Audit]] against it.
> - The whole party is now **Level 11**, but split across two locations: TMind and Lae'zel are back at **camp**, Kao and Astarion are at **Ramazith's Tower** (Sorcerous Sundries, Lower City). Regrouping is now the top readiness item.
> - **Every previous buff gap is resolved**: Death Ward, Freedom of Movement, and Mage Armor are active on all four party members for the first time this campaign. A new gap appeared in their place — **Aid has dropped off everyone** — and **Elixir of Bloodlust is completely out of stock**, not just low.
> - Summons changed: the Cambion/Djinni Planar Ally was replaced by a **Deva (Planar Ally)** at camp; Kao's Conjure Elemental (Air) summon is still with him at the tower.
> - Astarion picked up a real **cursed status from The Tharchiate Codex** after reading a copy — the same Legendary book flagged as "lying uncollected" two audits ago. The save's raw status list confirms it's on him, not TMind (his `MAG_CATS_GRACE` and Cloak of Displacement statuses share the same character node), and per bg3.wiki **the curse is reversible** with Remove Curse or Greater Restoration — softened the "confirm this was intentional" framing accordingly since there's no real downside pressure. TMind now holds two more unread copies; whether to read them is a build decision, not a bug.

> [!note]- 🗡️ Gear Ratings & Redistribution (three Legendary/Very Rare finds, a storage correction)
> - Kao picked up **Markoheshkir** (Legendary staff) and **Robe of the Weave** (Very Rare) at the tower — both rated ⭐⭐⭐ and confirmed against bg3.wiki, not guessed.
> - Astarion picked up **Duellist's Prerogative** (Legendary rapier) — first flagged as a genuine build fork, then checked its exact mechanics against bg3.wiki and corrected that: Dueller's Enthusiasm replaces the usual off-hand attack one-for-one, so Thief's bonus-action economy and Sneak Attack are unaffected. It's a loadout swap (empty off-hand), not a subclass/feat decision — the only real cost is the off-hand dagger's own perk (Stillmaker's Hold Person, if that's the one benched). Full breakdown now lives in [[11_Main_Character_Builds#^astarion-build|Astarion's build]].
> - Caught a real combo the user pointed out: Lae'zel picked up the **Commander's Strike** maneuver, which grants an ally a reaction to make a melee attack (the maneuver's mechanics are bg3.wiki-confirmed; whether she knows it is player-reported, since known maneuvers aren't captured by this handbook's save extraction — corrected an earlier overclaim of "confirmed"). With Astarion's extra reaction from Duellist's Prerogative, he can take that granted attack on his *first* reaction and still have his second free for Withering Cut or a real opportunity attack. Documented as [[11_Main_Character_Builds#^laezel-build|Lae'zel's build § Commander's Strike → Astarion Reaction Combo]] and added to the Readiness Audit's Before a Hard Fight checklist.
> - Re-checked Lae'zel's own position against the fresh save and caught two more drifts: **Corpsegrinder** moved off her into genuine camp storage (`Level`/`Character`-node confirmed, nothing shady), and the earlier claim that **Cerebral Citadel Gloves** was "gone, not found elsewhere" was simply wrong — it's sitting with the same unidentified resurrected companion already flagged for the Ring of Salving cluster. That cluster is now confirmed as **one companion holding seven items** (Ring of Salving, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb ×2, Reaper's Embrace, and now Cerebral Citadel Gloves), all at the identical camp position — consolidated into a single entry in [[13_Item_Inventory_Snapshot#^storage-notable-gear|Notable Gear Sitting in Storage]] instead of being tracked as separate mysteries.
> - Also new this pass: Staff of Interruption, Fey Semblance Amulet, and a boss-dropped shield for Kao (name withheld, spoiler-flagged); Salty Scimitar(rrr) (confirmed looted from Captain Grisly at The Blushing Mermaid), Ring Of Blink, Winter's Clutches, Coldbrim Hat, and Gold Wyrmling Staff (off-build, sell) for Astarion; Amulet of Windrider and Keepsake Ring for Lae'zel; Scroll of Dethrone for TMind (exact effect not fully confirmed — flagged as such rather than asserted).
> - **Storage correction**: re-checked the "Notable Gear Sitting in Storage" list with the same `Level`-field-plus-`Character`-node method that caught last audit's mistake, and found Reaper's Embrace no longer qualifies — it now sits with a different resurrected, unidentified companion-type character at camp, not shared storage. The Tharchiate Codex also moved out of "still uncollected" now that copies are confirmed in TMind's and Astarion's inventories.
> - Noticed but not explained: **The Joltshooter and Gleamdance Dagger are both gone** from Astarion's inventory this pass, with no clear cause — flagged in the Readiness Audit for an in-game check rather than assumed lost.
> - Confirmed the last pass's three gear moves (Hellfire Hand Crossbow, Shade-Slayer Cloak, Vivacious Cloak) all landed, and that Murderous Cut and all three Whispering Mask copies are now fully resolved (storage-only, no longer misplaced on a character).

> [!note]- 🔒 Corrections & Maintenance (CLAUDE.md game-state refresh)
> - Updated the root `CLAUDE.md`'s "Current Game State" summary, which still said party level 10 at Sorcerous Sundries — it now reflects level 11 and the party's current split between camp and Ramazith's Tower.

## 2026-08-16

> [!note]- 🎒 Save Snapshots & Readiness (2 syncs, verdict reworded)
> - Refreshed the save-derived snapshots one save-state further (`AutoSave_127`, an hour of play past the previous sync) — the party moved from the Lower City sewers into the **Undercity Ruins**. Updated [Current Save Snapshot](12_Current_Save_Snapshot.md), the [[13_Item_Inventory_Snapshot#^inventory-best-uses|Item and Storage Snapshot]], and the [[14_Current_Readiness_Audit#^readiness-verdict|Readiness Audit verdict]].
> - Confirmed Kao's Death Ward, Freedom of Movement, and Mage Armor gaps (and TMind's missing Freedom of Movement) are still unresolved a full snapshot later — reworded the verdict from "new gap" to "persistent gap" so it reads as the standing priority it is, not a one-off reading.
> - Refreshed the save-derived snapshots again from a much bigger jump — `Campsite - 106h 12m`, about six hours of play past that pass. The whole party leveled up to 11, is back at **camp**, and picked up a new Cambion (Planar Ally) summon; the earlier Conjure Elemental (Air) summon is gone.
> - **Heroes' Feast is now available** party-wide (TMind reached Cleric 11) — this resolves a gap the previous audit had flagged as "the next major daily-buff upgrade," so the recommendation now points at actually casting it before the next hard fight instead.
> - Death Ward coverage got worse, not better: it's dropped off **Astarion** (who had it earlier that day) on top of the standing gap on Kao, who is still missing it — along with Freedom of Movement and Mage Armor — three snapshots running since his resurrection.
> - Synced one more save (`Campsite - 106h 21m`, only 9 minutes of in-game time later) — buffs are byte-for-byte identical to the last snapshot, so the standing gaps are now **four snapshots** running. The party did act on part of the readiness checklist though: see the gear callout below.
> - Synced again after a real fight (`The Blushing Mermaid - 109h 15m`, ~3,500+ XP each) — buff coverage flipped in an unusual way: Kao's Death Ward/Freedom of Movement/Mage Armor and Astarion's Death Ward are all resolved, but **TMind picked up both of those same gaps himself** and is now the only party member with any daily-buff gap. Also caught (and fixed) an initial mistake where I wrote "Freedom of Movement is the only gap left" for TMind without re-checking whether Death Ward had also dropped — it had.
> - TMind now carries a partial-ceremorphosis status, the same one Lae'zel has had since early on — logged factually in [Current Save Snapshot](12_Current_Save_Snapshot.md) without narrative detail, same spoiler-light treatment as hers.

> [!note]- 🗡️ Gear Ratings & Redistribution (item audit, storage sweep, correction)
> - Caught two more gear moves: Lae'zel's Vivacious Cloak drifted onto TMind (unused there) while she picked up an untested Cindermoth Cloak in its place; Astarion picked up an untested amulet, Chancer's Carcanet. Logged both in [[13_Item_Inventory_Snapshot#^inventory-new-finds|Notable New Finds]] without inventing ratings for the new pieces.
> - Caught a scroll hand-off from Kao to Astarion (Globe of Invulnerability, Conjure Elemental, Bestow Curse, Crown of Madness, Invisibility) that's probably worth reversing since Kao is the one who casts most of them, and confirmed the Boots of Speed / Vivacious Cloak that drifted onto TMind earlier are still sitting there unused.
> - Rated every named item picked up over the last three snapshots against bg3.wiki (not guessed) and replaced the "not yet rated" placeholders across [[13_Item_Inventory_Snapshot#^inventory-new-finds|Item and Storage Snapshot]] and [[14_Current_Readiness_Audit#^gear-synergies|Readiness Audit § Gear and Synergy Checks]] with real ⭐ ratings and a concrete redistribution plan: Hellfire Hand Crossbow and Shade-Slayer Cloak move from TMind to Astarion (both are Hide/stealth-triggered, wasted on a melee cleric), the Vivacious Cloak moves from TMind to Lae'zel in place of the less reliable Cindermoth Cloak, and Kao's scroll library moves back from Astarion. Ring of Salving, Sword of the Emperor, Boots of Psionic Movement, Chancer's Carcanet, Shadow of Menzoberranzan, and Disintegrating Night Walkers all rate ⭐⭐⭐; Bloodguzzler Garb fits nobody in the current build (buffs unarmed strikes) and was left unassigned rather than forced onto a character.
> - Went further and checked all 195 named items in the save's `storage` bucket against bg3.wiki (not just what the four characters carry) and added [[13_Item_Inventory_Snapshot#^storage-notable-gear|Notable Gear Sitting in Storage]]. The other ~175 items checked are cosmetic, outclassed, companion-locked starter gear, or consumables miscategorized as equipment, and were left out of the handbook per the project's practical-not-exhaustive convention.
> - **Corrected a methodology error in [[13_Item_Inventory_Snapshot#^storage-notable-gear|Notable Gear Sitting in Storage]]**, caught by the user asking to double-check it: 11 of the 12 "in storage" items listed were wrong. Position-matching against the four active characters isn't enough to confirm something is in camp storage — the save's `Level` field distinguishes items still lying uncollected in the world (Ring of Evasion, The Tharchiate Codex, Blade of the First Blood, Crimson Mischief) from items genuinely in an inventory, and a matching `Character` node at the same position identifies NPC-held items (Voss' Silver Sword and Silver Sword of the Astral Plane are both on the NPC Voss; Staff of Cherished Necromancy, Robe of Supreme Defences, Woe, Penumbral Armour, and both copies of True Love's Embrace are each on other unidentified NPCs). Only **Reaper's Embrace** held up as genuinely in storage. Also added a caveat to the Scope section: the doc's bulk `storage` counts (Character Summary, resource spot check, Camp Storage) inherit this same imprecision and were never individually re-verified.
> - The player actually acted on the readiness checklist: the Hellfire Hand Crossbow, Shade-Slayer Cloak, and Vivacious Cloak moves from the last audit are all confirmed done in game. Updated [Current Save Snapshot](12_Current_Save_Snapshot.md), [[13_Item_Inventory_Snapshot#^inventory-new-finds|Item and Storage Snapshot]], and the [[14_Current_Readiness_Audit#^gear-synergies|Readiness Audit]] to mark those items resolved instead of recommended. Kao's scroll hand-back still hasn't happened, three snapshots running.
> - The fight brought new gear churn: five TMind items (Ring of Salving, Keepsake Ring, Cloak of Protection, Helmet of Arcane Acuity, Bloodguzzler Garb) moved to an unidentified companion-type character near camp — checked its `Level` field and a nearby `Character` node the same way the earlier storage correction taught, and deliberately logged it as "location uncertain" rather than guessing it's simple camp storage. Murderous Cut also drifted from Astarion (a good fit) to TMind (not), and TMind picked up three identical copies of a new item, Whispering Mask, not yet rated.

> [!note]- 🛠️ Tooling & Site Infrastructure (this file's own structure)
> - Restructured this whole file from flat `### Added`/`### Changed`/`### Fixed` headings under each date into collapsible topic nodes (`> [!note]- 🎒 Topic`), so a date with several unrelated changes can be scanned/folded by subject instead of one long flat list. First tried it with raw `<details>` HTML, which turned out to silently break every wikilink and markdown link inside it — the site's renderer passes raw `<details>` blocks through untouched and never runs its parser on the contents. Switched to Obsidian's native collapsible-callout syntax instead (`> [!note]-`), whose body is recursively parsed like any other block, so links inside actually resolve. Updated the intro guidance and the Entry Template to match.

## 2026-08-10

> [!note]- 🎒 Save Snapshots & Readiness
> - Refreshed the save-derived snapshots from a new sync — the party has moved from Wyrm's Rock Fortress (100h 29m) all the way to the **Lower City sewers** (102h 46m, Act 3), and the game itself patched (`4.1.1.7209685` → `4.1.1.7398727`). Updated [Current Save Snapshot](12_Current_Save_Snapshot.md), the [[13_Item_Inventory_Snapshot#^inventory-best-uses|Item and Storage Snapshot]], and the [[14_Current_Readiness_Audit#^readiness-verdict|Readiness Audit verdict]].
> - The refresh surfaced that **Kao was resurrected** since the last sync (`IsResurrected` flag on his character node) and lost Death Ward, Freedom of Movement, and Mage Armor as a result; TMind is separately missing Freedom of Movement too. Both are flagged as the top priority in [[14_Current_Readiness_Audit#^before-leaving-camp|Before Leaving Camp]]. Aid's previous Lae'zel gap is resolved — it's now active on all four.

> [!note]- 🗡️ Gear Ratings & Redistribution
> - Logged several new named items picked up since the last item audit (most notably a unique longsword for Lae'zel) without inventing ratings for them — see [[13_Item_Inventory_Snapshot#^inventory-new-finds|Notable New Finds]]. Also caught that Lae'zel's Boots of Speed had drifted onto TMind's inventory doing nothing, while she's now carrying Boots of Psionic Movement instead.

## 2026-07-31

> [!note]- 📖 Handbook Content & Builds
> - Downloaded and read the actual transcripts (via `tools/download_youtube_transcript.py`, already in the repo) for all four Fextralife class-guide videos cited in Main Character Builds, after realizing the YouTube transcript API failures reported the previous day were real but solvable — the repo already had a working `yt-dlp`-based tool for this. Corrected several attribution errors the transcripts surfaced: [[11_Main_Character_Builds#^astarion-build|Astarion's]] feat table had substituted unverified picks (Alert, Savage Attacker, Mobile) for what the video actually names (Dual Wielder, Lucky, Sharpshooter) and was missing Rogue's level-10 bonus feat; [[11_Main_Character_Builds#^kao-build|Kao's]] table credited the Wizard video with recommending War Caster, which it never mentions (Alert, confirmed at level 8, was accurate); the Cleric video's War Caster recommendation for [[11_Main_Character_Builds#^tmind-build|TMind]] was initially missed by a keyword search because auto-captions render it as "warcaster" (one word) — now correctly credited, and its reasoning matches TMind's build almost exactly. Also flagged that three subclasses (Death Domain, Bladesinging, Arcane Archer) postdate their respective videos and are sourced from bg3.wiki only, not the transcripts. Transcript files are committed alongside the `.vtt` sources already in `tools/video-transcripts/`.

## 2026-07-30

> [!note]- 📖 Handbook Content & Builds
> - Extended the Fextralife-guide treatment from Astarion to the rest of the active party in Main Character Builds: added a Subclass Reference table (all subclasses of the class, with the current pick's exact features and why the alternatives don't fit) and a Recommended Feats table to [[11_Main_Character_Builds#^tmind-build|TMind]] (Cleric — confirmed Death Domain is genuinely player-selectable, with its real Reaper/Touch of Death/Divine Strike features), [[11_Main_Character_Builds#^kao-build|Kao]] (Wizard — confirmed Conjuration's Focused Conjuration protects Concentration specifically on Web/Grease), and [[11_Main_Character_Builds#^laezel-build|Lae'zel]] (Fighter — enriched the existing Feat Priority table with verified effect wording rather than duplicating it). All mechanics were checked against bg3.wiki rather than assumed from tabletop D&D, continuing the practice from the Advantage/Disadvantage correction earlier the same day.
> - Added a Rogue Subclass Reference (Thief, Assassin, Arcane Trickster) to [[11_Main_Character_Builds#^astarion-build|Astarion's build section]], citing Fextralife's Rogue class guide video. Confirms Thief still fits Astarion's current playstyle and notes why Arcane Trickster does not match his Dexterity-focused build; logged in the Build Sources Reviewed table.
> - Added a missing core-mechanics section, [[02_Combat_System#^advantage-disadvantage|Advantage and Disadvantage Explained]], to Combat System: how the d20-roll-twice mechanic works, and a table of common ways to gain Advantage on an attack. Cross-linked from Astarion's build and the Appendix glossary, which previously only had a one-line description with no real explanation.
> - Added a "Recommended Feats" table to [[11_Main_Character_Builds#^astarion-build|Astarion's build]] (Ability Improvement, Alert, Savage Attacker/Sharpshooter, with Mobile/Lucky as alternates — later corrected against the video's transcript on 2026-07-31).
> - Corrected two mechanical errors in the [[02_Combat_System#^advantage-disadvantage|Advantage table]] added earlier the same day, caught by spot-checking against [bg3.wiki](https://bg3.wiki/wiki/List_of_sources_of_advantage_and_disadvantage_on_attack_rolls) instead of assuming tabletop D&D rules apply unchanged: (1) BG3's Prone condition grants Advantage based on **distance** (within 3 m/10 ft, any attack type), not a melee-advantage/ranged-disadvantage split like tabletop; there is no ranged disadvantage against Prone in BG3. (2) BG3's **Help action does not grant Advantage at all** — unlike tabletop, it only revives downed allies or clears conditions. Also corrected the Paralyzed auto-crit range to 3 m and added Sleeping (auto-crit at 1.5 m) and Entangled/Enwebbed (relevant to Kao's Web) as their own rows. Feat effects in [[11_Main_Character_Builds#^astarion-build|Astarion's build]] were verified the same way (e.g. Sharpshooter ignores High Ground in BG3, not cover as in tabletop).

## 2026-07-23

> [!note]- 🛠️ Tooling & Site Infrastructure
> - Linked the generated `journal.md` and `chronicle.md` from the vault home page: added both to the `README.md` navigation table and root-content list (with a spoiler warning on each), and documented them in `CLAUDE.md`'s repo-layout list.
> - Installed and enabled the Obsidian Git plugin (`obsidian-git` 2.38.6), configured conservatively — auto-pull on vault open, no auto-commit/push — and committed so other clones of the vault get it too.
> - Added a "🌐 Web version" callout to the `README.md` home page linking to the live GitHub Pages site (`https://tmind.github.io/bg3-handbook/`).
> - Fixed quest summary spacing in `journal.md` for renderers without the site's CSS (Obsidian, GitHub), where the title and entry count ran together (e.g. "Help Your Protector4 entries"). `tools/build_journal.py` now separates them with a plain space and parenthesizes the count.

## 2026-07-22

> [!note]- 📖 Handbook Content & Builds
> - Added `chronicle.md`, a narrative party chronicle: the characters' story so far (prologue, an act-by-act shared arc, per-character arcs, and a save-waypoint timeline), grounded in the current save's quest journal and the campaign notes (handles only). Story beats are anchored to real saves by playtime (the run has 136 named location-saves from the crash at 1h to Wyrm's Rock at 100h). Added to the site build and sidebar (Current Campaign → Party Chronicle), browsable and searchable alongside the journal.
> - Ran a systematic flag audit over all quest nodes (lone fallback closures, contradictory step pairs, ambiguous prototype resolution). Findings: confirmed the Halsin and Minthara fallback-text cases; discovered that **Karlach was killed in Act 1** (head delivered for the bounty; permanently dead) and that **Wyll was recruited** — added his arc (see [[chronicle#Wyll — The Blade of Frontiers|Wyll's chronicle section]]) and Karlach's fate to the chronicle and session notes.

> [!note]- 🛠️ Tooling & Site Infrastructure
> - Added `tools/extract_item_names.py`, which builds a local `tools/item-names/item_names.json` cache mapping item stat names to their real display names (RootTemplates `_merged.lsf` with ParentTemplateId inheritance, joined to `english.loca`). It reuses the LSPK reader from `extract_journal_text.py` and the LSF parser from `index_lsf.py`, so future item re-audits are one command instead of an ad-hoc rebuild. The cache is gitignored (copyrighted names).
> - Fixed the journal's quest resolution to break step-membership ties via the node's ObjectiveID prefix, which had mis-titled `DEN_RobbedAdventurer` (shared `GroveChanged` step) and could mix the Astarion COM/Avatar tracks.
> - Fixed companion quests mixing first-person and party-perspective text. The save records each companion quest twice — the `ORI_COM_*` party track ("we...") and the first-person `ORI_Avatar_*` origin track ("I...") — and merging them by title interleaved the two voices. The journal now groups quests by prototype id (so the two tracks stay separate), sub-groups the companion section under each character's name with a `####` heading, and tags every entry `party view` / `origin view`. Both perspectives are preserved, side by side, without mixing.
> - Corrected the quest journal to show only genuine journal entries. The save's `QuestUnlockedSteps` were resolved to prototype quests by step-membership (the reliable key) rather than by objective-id prefix, which had mis-mapped several quests and rendered internal/empty steps as bogus humanized lines. Quest nodes that share a title (a companion's ORI_COM and ORI_Avatar tracks, or one node per objective) are now merged into a single entry with de-duplicated text, and untranslated placeholder titles (`%%% EMPTY`) fall back to a readable id.

> [!note]- 🎒 Save Snapshots & Readiness
> - Rewrote the [Item and Storage Snapshot](13_Item_Inventory_Snapshot.md) as a full item re-audit of the `Wyrms Rock Fortress - 100h 29m` save. Item display names are now resolved from the game's own root templates and localization (a stat/template → DisplayName → loca join, same approach as the journal text), so names match in game; per-character gear, consumable counts, and storage highlights are refreshed (e.g. TMind now has The Whispering Promise, Astarion has Cloak of Displacement + The Joltshooter, Kao's Absorb Elements is the Cloak of Elemental Absorption). Readiness consumable counts were refreshed to match.
> - Refreshed the save-derived snapshots from the `Wyrms Rock Fortress - 100h 29m` save: rewrote the party, buff, and item-source sections of [Current Save Snapshot](12_Current_Save_Snapshot.md) (party now in `WYR_Fortress_SUB`, XP ~63.7k, Flying Ghoul summon, Elixir of Bloodlust now active on Lae'zel, Pass Without Trace no longer active, new item effects), and updated the [[14_Current_Readiness_Audit#^readiness-verdict|verdict]] and [[14_Current_Readiness_Audit#^available-buff-casters|buff coverage]] in Current Readiness Audit. The item snapshot (`docs/13`) got the new source reference and a note that its detailed tables still reflect the prior inventory pass pending a full item re-audit. Also updated the current location in `CLAUDE.md` and `session-notes.md`.

## 2026-07-21

> [!note]- 🛠️ Tooling & Site Infrastructure
> - Added `tools/extract_journal_text.py`, which reads the player's own installed game files (`Gustav.pak` → `quest_prototypes.lsx`, `English.pak` → `english.loca`) directly — no LSLib/Divine needed — to build a `tools/journal-text/quest_text.json` cache mapping quests and steps to their real localized journal text. When that cache is present, `build_journal.py` fills `journal.md` with the verbatim in-game entries (with a Larian attribution line); without it, it falls back to readable titles derived from the ids so CI still builds. The intermediate cache is gitignored.
> - Added `tools/build_journal.py`, which generates a quest journal (open and completed quests with their step trails) from an indexed save, and published the generated `journal.md`. It is spoiler-heavy (full story progress). It lives at the repo root, so `check_vault.py` does not scan it — same as `session-notes.md`.
> - Added `journal.md` to the generated site (`scripts/build_site.py`) and the sidebar (Current Campaign → Quest Journal), so it is browsable and searchable alongside the handbook chapters.
> - Made each quest a collapsible `<details>` entry (generator emits the HTML; the site renderer passes `<details>` blocks through and styles them). Keeps the long list scannable and works on the site, on GitHub, and in Obsidian.

## 2026-07-19

> [!note]- 🛠️ Tooling & Site Infrastructure
> - Added a client-side search box to the generated site (`scripts/site_template.html`): indexes every chapter section in the browser, ranks results, shows highlighted snippets, and jumps to the matching heading. No backend — all content is already embedded in the page. Press `/` to focus it, `Esc` to clear.

## 2026-07-18

> [!note]- 🔒 Corrections & Maintenance
> - Standardized all player references to handles (`Kao`, `tmind`/`TMind`) across the handbook, notes, character files, and map, and renamed the cleric's character notes to `characters/tmind.md`. Anchor ids and the save tooling's default focus pattern were updated to match.

> [!note]- 🛠️ Tooling & Site Infrastructure
> - Added `scripts/build_site.py` and `scripts/site_template.html`, which build a single self-contained `site/index.html` from the vault — a navigable web version of the handbook with a chapter sidebar and working internal links (Obsidian Wikilinks and Markdown links both resolve). `site/` is gitignored as a generated artifact.
> - Added `.github/workflows/pages.yml` to rebuild and deploy the site to GitHub Pages on every push to `main` (requires enabling Pages with the GitHub Actions source).

> [!note]- 📖 Handbook Content & Builds
> - Resolved the stale Sussur Bark open question in `session-notes.md`: the bark was crafted into the Sussur Dagger, currently held by Astarion.
> - Removed the outdated Lae'zel level 7 feat decision from `session-notes.md` and [[11_Main_Character_Builds#^laezel-build|Lae'zel's build]] — she is now Fighter 10, so the decision point has passed. Noted that exact feat/maneuver picks aren't reliably readable from the save extract and should be verified in game.

## 2026-07-13

> [!note]- 🎒 Save Snapshots & Readiness
> - Refreshed the current save snapshot, item snapshot, and readiness audit from `Wyrms Crossing - 98h 15m`.
> - Updated active-party buff coverage: the main party is grouped in `WYR_Bridge_SUB`, Death Ward and Freedom of Movement are active on all four main characters, and Aid is still missing from Lae'zel.
> - Updated visible inventory/resource counts for the latest extracted save, including Bloodlust, Viciousness, Revivify, Potion of Speed, Globe, Conjure Elemental, and healing-potion stock.
> - Added current-holder information to the item snapshot's [[13_Item_Inventory_Snapshot#^inventory-best-uses|resource and best-use tables]].
> - Synced and extracted `Wyrms Crossing - 98h 15m`, modified 2026-07-13 01:25:09 +02:00.
> - Mirrored the save into `saves/TMind-25121262363__Wyrms Crossing - 98h 15m/`.
> - Rebuilt the local `.lsf` index for the refreshed snapshot.

## 2026-07-12

> [!note]- 🎒 Save Snapshots & Readiness
> - Updated the save sync workflow so the selected latest save folder is also copied into `saves/`.
> - Refreshed the `characters/` notes from the latest local save, `Rivington - 96h 28m`.
> - Replaced old Act 2 / level-planning character notes with current active-party summaries for TMind, Lae'zel, Kao, and Astarion.
> - Updated camp notes for Shadowheart, Gale, the active summons, and current before-fight checks.
> - Ran the save sync workflow against the current latest save, `Rivington - 96h 28m`, modified 2026-07-12 23:37:38 +02:00.
> - Mirrored `Rivington - 96h 28m` into `saves/`.
> - Character notes in this entry were refreshed from `Rivington - 96h 28m`, modified 2026-07-12 23:37:38 +02:00.
> - Rebuilt the local save index during the `Rivington - 96h 28m` character refresh.

> [!note]- 🛠️ Tooling & Site Infrastructure (repo setup)
> - Created the first Git-backed handbook snapshot.
> - Added this history note so future updates can record what is new.
> - **Tracked content**: Handbook chapters from [Basics and User Interface](01_Basics_and_User_Interface.md) through [Appendix](15_Appendix.md); current campaign notes ([Current Save Snapshot](12_Current_Save_Snapshot.md), [Current Item and Storage Snapshot](13_Item_Inventory_Snapshot.md), [Current Readiness Audit](14_Current_Readiness_Audit.md)); maintenance tools and source transcripts.
> - **Ignored locally**: savegame extracts, generated save indexes, bundled external tools, Python caches, local trash, local Obsidian workspace state, and volatile YouTube metadata.

## Entry Template

```md
## YYYY-MM-DD

> [!note]- 🎒 Topic Name (reuse an existing topic where it fits)
> - What changed, why it matters, which notes were touched.
> - Another bullet, same topic.

> [!note]- 🗡️ A Different Topic, Same Date
> - Only add a second callout if the day's entries genuinely span more than one topic.
```
