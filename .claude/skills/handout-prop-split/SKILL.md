---
name: handout-prop-split
description: Keep GM-only material out of anything a player will actually hold, a printed program, an in-world letter, a poster, a prop PDF. Use before finalizing any player-facing handout built from richer GM material, or whenever a prop's scope grows past its original size. Companion to `session-review` (checks this as part of the full pass) and `handout-pdf` (the PDF build itself).
---

# Splitting player-facing props from GM material

Built from the International Space Dog Show program's own history: it grew from 2 pages to 13 over several passes, mixing in the full rival roster, the halftime reveal, attendee lists, and a conspiracy menu, before getting caught ("the rest are DM knowledge that players shouldn't see") and trimmed to the 5 pages that actually belong in a player's hands, with everything cut ported into `sessions/Episode - The International Space Dog Show.md` as GM reference. See that episode doc's git history for the worked example.

## The rule

**A player-facing prop shows only what an in-world version of that document would plausibly contain.** A program handed out at the gate lists categories, judges, and past winners. It does not list which rival is secretly favored, what the halftime show's real reveal is, who's planning to cheat, or any DC or mechanics table, because the in-world document wouldn't know those things either.

Apply this test to every section before it goes in a player-facing file: **would the in-world author of this document actually write this down for a stranger to read?** If the answer is "only if they were secretly working for the GM," it doesn't belong.

## Where the cut content goes

Never delete it, move it. GM-only material belongs in the matching session or episode doc (`sessions/Session N Prep.md` or `sessions/Episode - [name].md`) as reference: full rosters, secret motives, DC tables, rigging/conspiracy mechanics, anything that exists to help run the scene rather than to be read by a player. Confirm nothing was lost by checking each removed section has a home in the GM doc before deleting it from the player-facing one, the way the Dog Show trim was verified line by line against the full list of locked decisions.

## Common failure modes to check for

- **Scope creep during a long build.** A prop that started small accretes GM content pass by pass because each individual addition felt justified in the moment. Re-run the test above on the whole doc periodically during a long build, not just at the end.
- **Stale cross-page references after a trim.** Cutting pages changes page numbers and footer pointers ("see page 7" becomes wrong once page 7 is gone). Check every internal reference after any page-count change.
- **Content that's genuinely ambiguous.** Some things (a sponsor's name, a judge's reputation) are fine in-world knowledge; the test is whether a real person in that world would know and casually print it, not whether it's spoiler-adjacent. When genuinely unsure, ask rather than guess which side it falls on.

## Before finalizing

Walk the player-facing file section by section against the test above. Anything that fails goes to the GM doc. Then re-check cross-references (page numbers, "see page N" footers, "continued" notes) since the page count likely changed.
