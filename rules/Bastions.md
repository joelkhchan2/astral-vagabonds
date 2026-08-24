# Bastions — DM Reference

The 2024 Bastion system, adapted for *Astral Vagabonds*. **In this campaign the ship is the bastion** — the crew's two PCs pool their facilities into one hull (see "Combining Bastions"). This doc is the rules reference; the table-facing handout is `Bastions — Player Guide.md`.

> **Sourcing note.** The framework rules and the facility **index** (level, prerequisite, order) are transcribed from *Dungeon Master's Guide (2024), Ch. 8: Bastions* (attached at `fa7bd825-Dungeon_Masters_Guide_2024__Ch._8_Bastions.md`). The per-facility **Space, hireling counts, and effect summaries** are reconstructed from the 2024 DMG — the attachment's individual facility stat blocks were lazy-loaded placeholders that didn't render, and 5e.tools is blocked by the network proxy — so **verify the exact craftable lists, gp values, and boon wording against the book before they matter at the table.** Levels, prerequisites, and order types are authoritative; effect blurbs are directional.

---

## The basics

- **You gain a bastion at level 5.** Work has been happening "off-screen" during early adventuring, so it's ready when the PC hits 5. Here, that's the ship they bought at Session Zero.
- **Bastion turns** happen every **7 days of in-game time** by default (slow this to monthly if there are long gaps between adventures). On a bastion turn a PC issues **orders** to their special facilities, or issues **Maintain** to the whole bastion.
- A bastion has **basic facilities** (flavor rooms) and **special facilities** (rooms with mechanical benefits).
- **Facility space** caps a room's size:

  | Space | Max area |
  |---|---|
  | Cramped | 4 squares (5-ft) |
  | Roomy | 16 squares |
  | Vast | 36 squares |

- **Free structure features:** closets/washrooms (inside a facility), corridors/ramps/stairs, and one or more doors + shuttered windows per facility. **Defensive walls:** 20 ft high, **250 GP and 10 days per 5-ft square**; a fully walled bastion loses 2 fewer Defender-dice when attacked.

### Combining bastions (this campaign)
Two PCs can merge their bastions into one structure — **the ship**. Merging does **not** change how many special facilities each PC has, how they work, or who issues their orders. **Each PC's hirelings stay theirs** and can't be shared. Exception: if an event kills one PC's Bastion Defenders, the other PC may absorb some/all of those losses onto their bastion instead (because they're combined).

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

## Bastion Events (DM-only)

Rolled **once each time a PC issues Maintain** (roll separately for each PC who Maintains, even in a combined bastion). Read the result to the owning player; resolve immediately, expanding story together. Great as cutscenes where players voice their hirelings.

| 1d100 | Event |
|:---:|---|
| 01–50 | **All Is Well** — nothing significant (roll 1d8 for color). |
| 51–55 | **Attack** — a hostile force is beaten off. Roll **6d6**; each **1** kills a Bastion Defender. Zero Defenders → a random special facility is damaged and shut down for the PC's next bastion turn (then repaired free). |
| 56–58 | **Criminal Hireling** — a warrant appears; pay a **1d6×100 GP** bribe to keep them, else they're arrested (the facility idles one turn, then a free replacement arrives). |
| 59–63 | **Extraordinary Opportunity** — host a festival / fund a mage / appease a noble. Take it for **500 GP** → roll again on this table (reroll this result); decline → nothing. |
| 64–72 | **Friendly Visitors** — outsiders pay **1d6×100 GP** to briefly use a facility (doesn't interrupt your orders). |
| 73–76 | **Guest** — roll 1d4: renowned guest (letter of recommendation) / fugitive (gift 1d6×100 GP) / mercenary (+1 Defender) / friendly monster (defends once, no Defender loss). |
| 77–79 | **Lost Hirelings** — a random facility loses its hirelings; idle one turn, then replaced free. |
| 80–83 | **Magical Discovery** — gain an Uncommon **Potion or Scroll** of your choice, free. |
| 84–91 | **Refugees** — 2d4 refugees seek shelter; they pay **1d6×100 GP** and stay until rehomed or attacked. |
| 92–98 | **Request for Aid** — send Defenders (roll 1d6 each; total ≥10 solves it for a **1d6×100 GP** reward; <10 solves it but halves the reward and kills one Defender). |
| 99–00 | **Treasure** — gain an art object or magic item (roll on the Treasure sub-table → the referenced Ch. 7 tables). |

### Fall of a bastion
- **Divestiture** — the PC gives it up; it's vacated and looted.
- **Neglect** — no orders for a number of consecutive bastion turns equal to the PC's level (usually because they're dead/incapacitated) → hirelings abandon it; it's looted. A returning PC can start fresh.
- **Ruination** — drawing the *Ruin* card from a *Deck of Many Things* instantly destroys it.

A PC who loses a bastion can establish a new one (use the Acquisition table for how many special facilities it starts with, plus two basic facilities — one Cramped, one Roomy).

---

## Adapting to the ship

- **The hull is the shared bastion.** Aerion (Priscilla) and Orena (Gabrielle) each own their special facilities but pool them into the one ship; their hirelings are the loyal NPC crew, mapped to facilities.
- **Facility ↔ crew mapping (natural fits):** Engineering/Tack → **Workshop** or **Smithy**; sickbay/Brassica → **Laboratory** or **Greenhouse**; gun bay → **Armory**; crew quarters/Aussie → **Barrack**; galley + long table → basic **Dining Room/Kitchen**; the helm/charts/Orena → **Observatory** (spelljammer-perfect at L13) or **Library** now; cargo/Aerion → **Storehouse**.
- **Space on a ship is tight.** The Trader is 20 tons of cargo and 11 berths — lean toward **Cramped/Roomy** facilities and use the "both faces of every deck are walkable" gravity-plane trick to justify square counts.
- **The `Ship Construction.md` "Bastion Improvements" table** (enlarge costs, extra hirelings, "Arm the Crew," second facility of a type, specialization) is this campaign's houseruled add-on layer on top of these rules — keep the two consistent when you build the ship's facility list.
- **Two level-5 special facilities are unspent** right now — that's the deferred Session Zero task and the placeholder in `The Ship (unnamed).md`.
</content>
