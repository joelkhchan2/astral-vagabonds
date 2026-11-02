---
name: npc-creation
description: Shape for writing up a new named NPC with real recurrence (not a one-line mention), especially a crew hire or sidekick, including building their level 6 D&D 5e sidekick stat block when they might show up mechanically. Use whenever a new NPC is getting their own file, or `campaign/Name Index.md`'s "no dedicated file yet" list needs promoting an entry. Companion to `dnd-writing` (voice) and `session-structure` (where NPC beats fit in a session).
---

# Writing up a new NPC

`npcs/Tomlin Underhill.md`, `npcs/Judo.md`, and `npcs/Sable.md` are the worked examples, three crew hires built the same way in one pass. `npcs/Aurel Delverane.md` and `npcs/Wyndham Aldane.md` show the other path in: a guest NPC from a single session, promoted to their own file once they earned real recurrence.

## Before writing: discuss first

A new NPC with real narrative weight (a recurring crew member, a named antagonist, anyone who'll carry a thread) is a creative choice under `CLAUDE.md`'s discuss-before-write rule. Confirm the shape (species, role, the one or two defining facts) in chat before writing the file, even when the direction feels obvious. A minor background NPC who exists for one scene and isn't expected back doesn't need this, use judgment on weight.

## The shape

Per `CLAUDE.md`'s Output Rules ("names, motives, habits, hidden intentions; complexity over alignment") and `rules/DMing Craft.md`'s "every NPC gets one voice tic and one physical tic, and one want":

- **Who they are.** Species, role aboard (or in the world), how they came aboard or into the story.
- **Motive.** What they actually want, stated plainly, not just a job description.
- **Ambition.** Where that want is pointed, the longer arc if they have one.
- **Weakness.** A real one that creates friction or a failure mode, not a quirk.
- **Strength.** What they're actually good at, concretely.
- **Voice tic and physical tic.** One each, enough to play them again without re-deriving who they are.
- **Hidden intention, if any.** What the table doesn't know yet, and how it surfaces.

Write this as scannable prose or bullets, not a form. Match the length to how load-bearing the NPC is, a one-scene guest gets a paragraph, a new crew member gets the full `Tomlin Underhill.md`-length treatment.

## When they need a sidekick stat block

Build one when the NPC might show up mechanically, a ship-combat station, a social encounter needing a roll, a fight. Skip it for NPCs who are purely color.

Approximated from the 2018 Unearthed Arcana Sidekicks playtest (Expert/Warrior/Spellcaster chassis), not the final published text and not exact RAW. The three session 4 hires are built at level 6 from it: HP is the base creature's hit dice plus one hit die per sidekick level, proficiency is +3, and Extra Attack replaces a base Multiattack instead of stacking. Flag it the way this repo already flags reconstructed rules content: **"[Reconstructed sidekick build, verify against the book before it matters at the table.]"**

- **Expert** (skill-based): Expertise (two skills at level 1, two more at level 6; tools only by house rule, as with Tomlin's cook's utensils), Helpful, Cunning Action, Jack of Many Trades, Extra Attack. No Sneak Attack in this chassis.
- **Warrior** (combat-based): Second Wind, Danger Sense, Improved Critical, Extra Attack. No Fighting Style in this chassis, so any "Archery as Gunnery" bonus is homebrew.
- Pick the chassis from what the NPC actually does, a cook-gunner or scout leans Expert with a combat edge or Warrior depending on which half of their role matters more at the table, judgment call, note the reasoning in the file.
- Proficiency bonus +3 at levels 5 to 8. HP and AC scaled to fit the chassis and the NPC's concept (a tortle gets AC from its shell, a hadozee gets Dex-leaning AC), not copied from a template.

## After writing

- **Add them to `npcs/Crew Roster.md`** if they're crew, with a pointer to the new file.
- **Add them to `campaign/Name Index.md`**, either under their matching category (people, factions, locations) or, if they're not yet load-bearing enough for their own file, under "Notable named NPCs with no dedicated file yet." Promote that entry to a real file and a real `Name Index.md` row once they've earned it, the same path Aurel Delverane and Wyndham Aldane took.
- **Check the name isn't already taken** by grepping `campaign/Name Index.md` and the repo before locking it in, especially for a surname or house that might already belong to someone.
