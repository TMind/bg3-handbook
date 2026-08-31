# Session Notes

Running log of decisions, discoveries, and open questions.

---

## Act 1 — Underdark (Complete)

### Party at the time
Kao, TMind, Lae'zel, Gale → later swapped Gale for Astarion

### Key decisions
- **Swapped Gale → Astarion**: gained stealth, trapping, lockpicking; lost AoE. Gale remains available in camp.
- **Kept Lae'zel over Shadowheart**: Shadowheart would remove the frontline tank; Lae'zel is essential for the Spirit Guardians strategy.
- **Sussur Bark collected** at the Sussur Tree, later crafted into the **Sussur Dagger** at the Blighted Village forge — currently held by Astarion for caster silence.

### Act 1 outcomes (verified from save quest flags, 2026-07-22)
- **Halsin was never rescued and died in Act 1** (`HalsinDiedEarly`; Act 2 confirms via Art Cullagh: `HalsinAlreadyDead`). No rescue/join step exists anywhere in the save.
- **Sazza was freed from the grove cage and saved again from Minthara** (`DEN_CapturedGoblin`: `Released` → `Escaped` → `Saved`, "we convinced Minthara to spare her life") — and **Sazza then told Minthara where the grove is** (`SazzaToldMinthara`).
- **Grove conflict ended via the goblin assault path** ("Raid the Emerald Grove": `King_SentToMinthara`, `AoD_Started`/`AoD_Ready` — Minthara's warband set out): **Zevlor died**, **Kagha died early**, and the druids were defeated (`Betrayal_DruidDead_Halsin`). The tieflings were **forced out of the grove** before the goblins were dealt with (`Goblin_NoTieflings`: "they'll likely die on the road").
- **Karlach was hunted and killed** despite her claims of innocence (`KarlachKilled`); her head was delivered to Anders for the bounty (`PLA_PaladinsOfTyr: TakeHead` → `DeliverHead` → `KilledKarlach_Reward`), and she is permanently dead (`ORI_COM_Karlach: KarlachPermanentlyDies` — "Karlach is gone forever"). **Wyll was recruited** (`RecruitedWyll`) and rewarded by Mizora for the kill (`MizorasJudgementReward`); in Act 2 the party rescued Mizora from the mind flayer colony, and she promised to release Wyll from his pact (`MizorasRescueHappenedPact`).
- **Minthara was never recruited and never appeared at Moonrise for the party.** No `ORI_*_Minthara` quest exists in the save, and of `MOO_MintharaFate`'s eleven steps only the fallback `MintharaLeftBehind` fired at the Act-2 transition — none of the encounter steps (`KnownMintharaCondemned`, `TalkToMinthara`, `DefeatTorturers`, `MintharaIgnored`, …) are set. The step's journal text ("left Minthara to her grim fate in Moonrise Towers") is the canonical-branch wording; it also fires when she was never met — most likely she died during or after the grove raid in Act 1.

### Lae'zel feat progression (Act 1)
- GWM taken
- STR raised to 19 via ASI (+2 from 17)

---

## Act 2 — Shadow-Cursed Lands (Complete)

### Final location
Moonrise Towers cleared. Act 2 complete.

#### Previously: Gauntlet of Shar (complete)
Silent Library completed. **Nightsong freed.** **Shadowheart spared the Nightsong** — she chose to defy Shar and embrace Selûne. Major Act 2 story decision with lasting consequences for Shadowheart's character arc and abilities.

#### Shadow curse: not lifted
With Halsin dead since Act 1, waking **Art Cullagh** only confirmed that the land-spirit **Thaniel** could not be rescued (`HalsinAlreadyDead`); the party left for Baldur's Gate with the curse intact (`SCL_LiftingTheCurse: OliverNotFound`).

### Active party
Kao (Conjuration Wizard), Astarion (Thief Rogue), Lae'zel (Battle Master Fighter), TMind (Death Domain Cleric)

### Open decisions
- **TMind's Warding Bond**: Currently on Lae'zel. Keep TMind's HP topped off as a result.

### Mechanics learned this session
- Spirit Guardians round timer doesn't tick outside combat — safe to pre-cast before engaging
- Sneak Attack does NOT require Advantage if an ally is within 5ft of the target
- Arrow of Darkness (magical darkness): cuts both ways — don't drop it on your own party
- Greater Invisibility: target stays invisible even after attacking — Advantage all turn, best used on Astarion
- Counterspell must be *prepared* AND reaction must be set to "Ask" or "On" in the reactions menu
- Healing potions can be *thrown* at an ally's feet to splash-heal at range (works on downed allies)
- Lae'zel can Jump over Web/Grease to bypass difficult terrain and reach enemies
- **Bless and Spirit Guardians are both concentration** — cannot run simultaneously. However, certain items (e.g. Hellrider's Pride gloves) apply Blessed to an ally when you heal them, no concentration required. TMind can hold Spirit Guardians and still generate Bless through healing actions.

---

---

## Act 3 — Baldur's Gate (Current)

### Current location
Split across two spots in Lower City — TMind and Lae'zel are in **Lower City proper** (Level 11, both have enough XP for Level 12 but haven't leveled up yet); Kao and Astarion are at **Baldur's Mouth Basement**, already Level 12. (Previously Sorcerous Sundries/Ramazith's Tower, ~118h playtime.)

### In progress
- **Search Tolna's office** (Sorcerous Sundries). Office is on the **second floor, left of the top of the stairs** (~X:12, Y:-79). Door is **DC 15** to pick, and the floor is patrolled by **Animated Armour** that turn hostile on a caught break-in. Plan: Invisibility on the lockpicker (Astarion) and split the party so a failed sneak doesn't pull everyone in; turn-based mode to time the patrol. The objective inside is triggered from the **bookshelf on the immediate right**, not from a desk — one clasped tome on that shelf acts as a lever (Alt-highlight if it doesn't show).
- **Ramazith's Tower arcane barriers.** Two barriers, each opened by an **invisible lever** — need See Invisibility (spell/scroll, or the Elixir of See Invisibility in a backpack on the outer ring) just to see them. Each lever is a **DC 20 Arcana** check, Kao is the interactor. **Failure is punishing:** the two "Aspects of Athkatla" statues are wired to the levers and cast **Disintegrate** on whoever failed. Stack the check first — TMind's **Guidance** (+1d4) plus **Enhance Ability: Fox's Cunning** (advantage on INT) — and save before each pull.

### Active party
Kao (Conjuration Wizard), Astarion (Thief Rogue), Lae'zel (Battle Master Fighter), TMind (Death Domain Cleric). Active summon: Deva (Planar Ally), with the Lower City pair (TMind/Lae'zel). Kao's Conjure Elemental (Air) summon is no longer active.

### Quest outcomes
- **Save Vanra — failed.** Auntie Ethel was killed with Vanra still inside her, so Vanra is permanently dead (no revive, no recovery from the corpse). The two ways to have saved her both had to happen *before* Ethel dropped: (a) craft **Hag's Bane** (Alchemy → Grenades; Ashes of Dried Fey Flower from the safe in Old Garlow's Place + any Essence, recipe book in Ethel's lair) and throw it at her — she goes Nauseous and vomits Vanra out; or (b) toggle **Non-Lethal Attacks** and knock her out in melee, then cut Vanra free. Hag's Bane also works thrown at "Captain Grisly" while she's still in the Blushing Mermaid. Declining her bargain avoids the fight entirely but leaves Vanra inside her.

### Mechanics learned this session
- **Kill-the-boss can kill the hostage.** Some Act 3 rescues are gated on doing something to the enemy *before* the HP bar empties (Hag's Bane / Non-Lethal for Vanra). When a quest says someone is being held *inside* or *by* a boss, check for a non-lethal or item-based route before opening the fight.
- **Pearlspore Bells** (Ethel's Act 3 lair): three fungal bells, 55 HP (Balanced) / 97 HP (Tactician), fungal resistance. All three must be destroyed or Ethel resurrects after death.
- **Impenetrable Slumber cannot be dispelled.** The sleeping tiefling in the Lower City Sewers (Dairow Vin) carries a scripted condition that ignores damage, healing, Shove, and polymorph. The only known way to rouse him is Death Ward → kill him → he stands up at 1 HP on the revive. He has no dialogue afterwards, so it's a curiosity, not a quest step. Speak with Dead works on him normally if left dead.

---

## Open Questions
- Lae'zel is now Fighter 10 — the level 7/8 feat question has passed. Exact feat/maneuver picks aren't reliably readable from the save extract; check her in-game character sheet if it matters for a build recommendation.
