# Bastions — DM Reference

The 2024 Bastion system, adapted for *Astral Vagabonds*. **In this campaign the ship is the bastion** — the crew's two PCs pool their facilities into one hull (see "Combining Bastions"). This doc is the full rules reference; the table-facing handout is `Bastions — Player Guide.md`.

> **This complements, and defers to, `Rules & Systems.md` §6 ("The Ship as Bastion").** That section is the short campaign house-ruling — where its two deliberate deviations from RAW (below) differ from the DMG defaults, **§6 wins**. `Rules & Systems.md` §8 covers ship *combat* (crew stations & maneuvers); this doc doesn't touch that. §6 also carries the fuller facilities-as-ship-rooms mapping — see "Adapting to the ship."

> **Sourcing note.** The framework rules and the facility **index** (level, prerequisite, order) are transcribed from *Dungeon Master's Guide (2024), Ch. 8: Bastions* (attached at `fa7bd825-Dungeon_Masters_Guide_2024__Ch._8_Bastions.md`). The per-facility **Space, hireling counts, and effect summaries** are reconstructed from the 2024 DMG — the attachment's individual facility stat blocks were lazy-loaded placeholders that didn't render, and 5e.tools is blocked by the network proxy — so **verify the exact craftable lists, gp values, and boon wording against the book before they matter at the table.** Levels, prerequisites, and order types are authoritative; effect blurbs are directional.

---

## The basics

- **You gain a bastion at level 5.** Work has been happening "off-screen" during early adventuring, so it's ready when the PC hits 5. Here, that's the ship they bought at Session Zero.
- **Bastion turns.** RAW is one every 7 days of in-game time. **This campaign house-rules it to one bastion turn per voyage leg** (`Rules & Systems.md` §6), so a transit is a single procedure regardless of length. On a bastion turn a PC issues **orders** to their special facilities, or issues **Maintain** to the whole bastion.
- A bastion has **basic facilities** (flavor rooms) and **special facilities** (rooms with mechanical benefits).
- **Facility space** caps a room's size:

  | Space | Max area |
  |---|---|
  | Cramped | 4 squares (5-ft) |
  | Roomy | 16 squares |
  | Vast | 36 squares |

- **Free structure features:** closets/washrooms (inside a facility), corridors/ramps/stairs, and one or more doors + shuttered windows per facility. **Defensive walls:** 20 ft high, **250 GP and 10 days per 5-ft square**; a fully walled bastion loses 2 fewer Defender-dice when attacked.

### Combining bastions (this campaign)
Two PCs can merge their bastions into one structure — **the ship**. Merging doesn't change how many special facilities each PC has or how they work.

- **RAW:** each PC still owns and orders their own facilities, and hirelings stay with their owner (can't be shared); the one shared perk is that Defender losses from an event can be absorbed onto either combined bastion.
- **Campaign house rule (`Rules & Systems.md` §6):** the ship is **fully pooled** — facilities are chosen jointly and **either PC can issue any order**. Use this; it keeps transit to one shared procedure. (The Defender-absorption perk still applies.)

---

## Basic facilities

Every bastion starts with **two free basic facilities** — one **Cramped**, one **Roomy** — chosen from: **Bedroom, Dining Room, Parlor, Courtyard, Kitchen, Storage.** They have no mechanical effect; they're roleplaying space. You can have more than one of each.

**Adding / enlarging basic facilities** (money + time; any number at once, PC need not be present):

| Add a facility | Cost | Time |
|---|---|---|
| Cramped | 500 GP | 20 days |
| Roomy | 1,000 GP | 45 days |
| Vast | 3,000 GP | 125 days |

| Enlarge | Cost | Time |
|---|---|---|
| Cramped → Roomy | 500 GP | 25 days |
| Roomy → Vast | 2,000 GP | 80 days |

---

## Special facilities

Special facilities can't be bought — they come with **level advancement**. Each can be chosen only once (unless its text says otherwise), and each has a level requirement and sometimes a prerequisite.

| Level | Special facilities total |
|:---:|:---:|
| 5 | 2 |
| 9 | 4 |
| 13 | 5 |
| 17 | 6 |

Each level-up, a PC may **replace** one special facility with another they qualify for. Each special facility comes with **hirelings** (the facility generates enough income to pay them) who execute orders and are loyal to the owner.

### Orders (issued on a bastion turn)
- **Craft** — hirelings craft an item the facility can make (facility is busy for the craft time).
- **Empower** — the facility confers a temporary boon to the PC or someone else.
- **Harvest** — hirelings gather a resource the facility produces (busy for the harvest time).
- **Maintain** — issued to the **whole bastion**, not one room; blocks all other orders that turn and triggers **one roll on the Bastion Events table**. (A bastion with no orders issued acts as if Maintained.)
- **Recruit** — hirelings recruit creatures, often **Bastion Defenders** (who defend against Attack events; the bastion covers their upkeep).
- **Research** — hirelings gather information/lore.
- **Trade** — hirelings buy and sell goods/services the facility handles.

---

## Facility catalog

Columns **Level / Prereq / Order** are authoritative (from the DMG index). **Space** and **What it does** are reconstructed — treat as directional, verify specifics against the book.

### Level 5

| Facility | Prereq | Space | Order | What it does |
|---|---|---|---|---|
| **Arcane Study** | Arcane Focus / tool as focus | Roomy | Craft | Craft an Arcane Focus, a Book, or a Spell Scroll. The wizardly workroom. |
| **Armory** | — | Roomy | Trade | Stockpile weapons & armor; a stocked armory equips your **Bastion Defenders** when the bastion is attacked. |
| **Barrack** | — | Roomy | Recruit | Houses your Bastion Defenders; Recruit adds more (up to the space cap). The crew's muscle. |
| **Garden** | — | Cramped | Harvest | Grow a chosen garden type (herb / food / poison / decorative) and harvest usable materials. |
| **Library** | — | Roomy | Research | Answer lore questions and dig up information; the reference stacks. |
| **Sanctuary** | Holy Symbol / Druidic Focus | Roomy | Craft | Craft a Holy Symbol, a Druidic Focus, or minor blessed consumables. |
| **Smithy** | — | Roomy | Craft | Forge nonmagical weapons/armor, or a Magic Item (Armaments). |
| **Storehouse** | — | Roomy | Trade | Buy low / sell high on bulk goods; turns cargo space into income. |
| **Workshop** | — | Roomy | Craft | Craft adventuring gear, tools, and tool-dependent items. |

### Level 9

| Facility | Prereq | Space | Order | What it does |
|---|---|---|---|---|
| **Gaming Hall** | — | Vast | Trade | Runs games of chance; generates gold (and rumors, and feuds). |
| **Greenhouse** | — | Roomy | Harvest | Cultivate potent/rare plants; harvest healing or alchemical ingredients. |
| **Laboratory** | — * | Roomy | Craft | Brew alchemical items and poisons (Alchemist's supplies); can craft potions. |
| **Sacristy** | Holy Symbol / Druidic Focus | Roomy | Craft | Craft Holy Water, healing consumables, or a Magic Item (Relics). |
| **Scriptorium** | — * | Roomy | Craft | Produce Books, documents (in bulk), and Spell Scrolls cheaply. |
| **Stable** | — | Roomy | Trade | Houses and trades mounts/beasts; provides a mount or draft animal. |
| **Teleportation Circle** | — | Roomy | Recruit | A permanent circle for fast travel; Recruit staffs it with casters. |
| **Theater** | — | Vast | Empower | Stage a performance that grants allies a temporary boon. |
| **Training Area** | — | Vast | Empower | Drill someone for a temporary edge, or retrain a proficiency. |
| **Trophy Room** | — | Roomy | Research | Read clues from trophies; recover a lost item or a lead. |

\* Certain orders for the Laboratory and Scriptorium have **additional prerequisites** — check the facility text.

### Level 13

| Facility | Prereq | Space | Order | What it does |
|---|---|---|---|---|
| **Archive** | — | Roomy | Research | Deep, hard-to-find lore — the Library's serious older sibling. |
| **Meditation Chamber** | — | Roomy | Empower | Grants a calming boon (e.g., resilience vs. fear/charm, or recovery). |
| **Menagerie** | — | Vast | Recruit | Houses captured creatures; a beast can serve as a Defender. |
| **Observatory** | Spellcasting Focus | Roomy | Empower | A divinatory/astral boon — thematically perfect for a spelljammer. |
| **Pub** | — | Roomy | Research | Gather rumors over drinks; a social intelligence-gathering room. |
| **Reliquary** | Holy Symbol / Druidic Focus | Roomy | Harvest | Produce limited-use blessed items / relic charges. |

### Level 17

| Facility | Prereq | Space | Order | What it does |
|---|---|---|---|---|
| **Demiplane** | Arcane Focus / tool as focus | Vast | Empower | A pocket dimension — storage, refuge, and a powerful boon. |
| **Guildhall** | Expertise in a skill | Vast | Recruit | Recruit a guild of skilled hirelings who provide services. |
| **Sanctum** | Holy Symbol / Druidic Focus | Roomy | Empower | A potent standing blessing. |
| **War Room** | Fighting Style or Unarmored Defense | Vast | Recruit | Muster soldiers and grant tactical boons. |

---

## Voyage & Downtime Events (DM-only)

> **Campaign rework.** Because the ship travels *with* the crew, this replaces the DMG's static-manor "while you were away" events. It's a **voyage table**: things that happen on the long, isolating hauls between systems (the Maintain weeks when the ship is coasting) or while docked at the Rock of Brawl. Tuned to the campaign's ~70% warmth / ~15% wonder / ~15% danger mix. **Bastion Defenders are the ship's faceless recruited security detail — not the named crew** — so a "lost defender" is never Tack or Finny.

Rolled **once each time a PC issues Maintain** (separately for each PC who Maintains, even though the bastion is one hull). Read the result to the owning player and resolve it together — many of these are best run as cutscenes where players voice the crew.

| 1d100 | Event | Tone |
|:---:|---|:---:|
| 01–33 | **All Is Quiet** — a calm leg. Roll 1d8 for color (see below). | 🟢 |
| 34–41 | **Something in the Drift** — the ship crosses paths with a creature. Roll 1d8. | 🔵🔴 |
| 42–49 | **A Heart-to-Heart** — a wall comes down aboard. Roll/pick on 1d6; grants a lasting **Bond** + one-time **morale** (Inspiration) for those involved. | 🟢 |
| 50–56 | **A Ship Hails You** — another vessel signals mid-void to trade or to borrow a facility (their helm needs your Workshop). They pay **1d6×100 GP**; your orders aren't interrupted. | 🟢 |
| 57–63 | **Salvage & Opportunity** — a find in transit: a derelict to strip, an unlisted current to chart and sell as **nav data**, a beacon with a bounty, a convoy needing escort. Spend a cost (a detour, air, fuel) → payoff + reputation, or pass. | 🟢 |
| 64–70 | **A Wonder** — the ship passes something sublime. Roll 1d8. Charting/logging it → nav data or a lead. | 🔵 |
| 71–76 | **She's Acting Up** — one of the hull's quirks fires. Roll 1d6. Almost always comedy + a minor repair; once in a long while, a warning. | 🟢🔴 |
| 77–81 | **Aboard for the Haul** — a passenger, stowaway, or rescued castaway rides along. Roll 1d4: renowned figure (a useful letter) / someone seeking passage or sanctuary (gift **1d6×100 GP**) / a mercenary (**+1 Defender**) / a friendly astral creature that tags along and defends once (no Defender loss). | 🟢 |
| 82–86 | **Castaways** — survivors adrift: a wrecked crew, a marooned traveler, refugees from a raided station (2d4). They pay **1d6×100 GP** or trade **information / a favor**, and stay until rehomed or attacked. *(Prime hook for Orena's lost crew.)* | 🟢🔴 |
| 87–90 | **Word From the Board** — news catches up at the next beacon: a rival beat your route time, a creditor or Aerion's family sends a pointed message, an off-book contract is dangled, or your Manifest Board ranking moves. | 🟢🔴 |
| 91–93 | **Someone's Having a Week** — a crew member is temporarily out (sick, injured, sulking, deep in a B-plot). Their facility idles one turn, then they're back. *Not* desertion. | 🟢 |
| 94–96 | **A Windfall** — the ship comes into something. Roll 1d6 (see below): valuables, a free potion/scroll, or a genuinely useful minor item / paying lead. | 🟢🔵 |
| 97–98 | **A Face From the Past** — someone's history catches up: a bounty hunter for **Brassica**, a collector about **Finny's** payments, a ghost of the **Captain's** old fleet. Pay them off (**1d6×100 GP** bribe), hide them, or face it. | 🔴 |
|  99   | **Distress Call** — a contact or station needs help. Send Defenders (roll 1d6 each; total ≥10 solves it for **1d6×100 GP** + Manifest Board standing; <10 solves it but halves the reward and costs one Defender). | 🔴 |
|  00   | **Contact!** — a hostile encounter. DM picks **ship-to-ship** (hull takes damage → repair cost) or **boarding** (defenders repel them: roll **6d6**, each **1** loses a security-detail Defender; **zero Defenders → a random ship system goes offline** for the PC's next bastion turn, then repaired free). | 🔴 |

### Sub-tables

**All Is Quiet (1d8)** — Tack names a new bolt and introduces it to the others · Finny's game-night bracket erupts in (friendly) scandal · the Captain wins at solitaire again, alone · Brassica invents a dish nobody asked for · a small repair goes suspiciously well · a lovely, harmless sight slides past the porthole · someone *swears* they saw something in the dark (they didn't) · the ram twitches but holds.

**Something in the Drift (1d8)** — 1–2 **Scavvers** pick at the hull; shoo them (check / warning shot) or lose a fitting or bit of cargo 🔴 · 3–4 **Kindori pod** paces the ship: an omen, an escort, a moment of awe; Orena logs them → nav data 🔵 · 5 **Void-glitter school** swarms the galley porthole, harmless and gorgeous; Finny names them; morale 🟢 · 6 **A lone unclassified creature** — feeds Orena's bestiary; study it → survey payout or clue 🔵 · 7 **A "derelict" that's a sleeping creature**; sneak past or wake it 🔴 · 8 **Something watches and leaves** before you get close; no stat block, just a thread 🔵🔴.

**A Heart-to-Heart (1d6)** — 1 two NPCs who grate on each other reconcile · 2 an NPC finally opens up to a PC · 3 the Captain lets her guard down (rare) · 4 a crew member shares a real piece of their secret (Brassica's deal / Finny's payments / Estravane's fleet / Orena's lost crew) · 5 an Aerion–Orena moment about their shared history · 6 the whole crew, over a meal at the long table.

**A Wonder (1d8)** — a dead titan adrift, big as a moon · an impossible aurora across the marble's edge · a silent derelict cathedral-ship, its lights still lit · a current that runs on old memories (you hear voices that aren't there) · a reef of crystal or a garden of frozen comets · a star or a marble being *born* · a migration of thousands crossing the dark · a place that appears on no chart (chart it → nav data + a lead).

**She's Acting Up (1d6)** — the ram self-deploys at nothing · the creaking changes pitch (usually nothing… usually) · the float bay hiccups and someone's coffee is on the ceiling · a Tack-named component throws a tantrum and Tack takes it personally · a door opens or locks for the wrong person · she runs a few degrees warm / hums one note — comfort, or omen.

**A Windfall (1d6)** — 1–3 an art object or valuables (salvage, an inheritance, an admirer's gift) · 4–5 a free Uncommon **Potion or Scroll** (Tack's tinkering or lucky salvage) · 6 a genuinely useful minor magic item, or a lead worth real gold.

### Fall of a bastion
- **Divestiture** — the PC gives it up; it's vacated and looted.
- **Neglect** — no orders for a number of consecutive bastion turns equal to the PC's level (usually because they're dead/incapacitated) → hirelings abandon it; it's looted. A returning PC can start fresh.
- **Ruination** — drawing the *Ruin* card from a *Deck of Many Things* instantly destroys it.

A PC who loses a bastion can establish a new one (use the Acquisition table for how many special facilities it starts with, plus two basic facilities — one Cramped, one Roomy).

---

## Adapting to the ship

- **The hull is the shared bastion.** Aerion (Priscilla) and Orena (Gabrielle) each own their special facilities but pool them into the one ship; their hirelings are the loyal NPC crew, mapped to facilities.
- **Facility ↔ crew mapping (natural fits):** Engineering/Tack → **Workshop** or **Smithy**; sickbay/Brassica → **Laboratory** or **Greenhouse**; gun bay → **Armory**; crew quarters/Ozzie → **Barrack**; galley + long table → basic **Dining Room/Kitchen**; the helm/charts/Orena → **Observatory** (spelljammer-perfect at L13) or **Library** now; cargo/Aerion → **Storehouse**.
- **Space on a ship is tight.** The Trader is 20 tons of cargo and 11 berths — lean toward **Cramped/Roomy** facilities and use the "both faces of every deck are walkable" gravity-plane trick to justify square counts.
- **The `Ship Construction.md` "Bastion Improvements" table** (enlarge costs, extra hirelings, "Arm the Crew," second facility of a type, specialization) is this campaign's houseruled add-on layer on top of these rules — keep the two consistent when you build the ship's facility list.
- **Two level-5 special facilities are unspent** right now — that's the deferred Session Zero task and the placeholder in `The Ship (unnamed).md`.
</content>
