---
name: session-review
description: Completeness and consistency audit for a session prep doc and its companion before calling a session "set" or "ready to run." Use when asked "are we set for session N," "did we cover everything," "any plot holes," or before/after a big prep-doc build to check it against the standing checklist. Companion to `session-structure` (the shape to check against) and `dnd-writing` (voice, not covered here).
---

# Reviewing a session prep doc

This is the checklist used (ad hoc, twice) to review `sessions/Session 5 Prep.md`: once mid-build, which found 5 real gaps (a stale pointer, missing Looking Ahead entries, an identity-less antagonist, an unbalanced PC spotlight, a missing Research pointer), and once as a final pass before calling the session ready. Run it as a deliberate pass, not from memory, the value is in actually checking each item against the doc rather than eyeballing it.

## How to run it

1. **Read the full prep doc top to bottom**, not just the sections that changed recently. Stale content hides in the parts nobody's touched in a while.
2. **Walk the checklist below** against what's actually in the doc, note gaps as you find them rather than trying to hold them all in memory.
3. **Spot-check the companion HTML** against the prep doc's final state, not just its own internal consistency, late edits to the prep doc are the likeliest place for drift (see `session-structure`'s note that the companion comes after the prep doc is settled, this is the check that it actually stayed in sync).
4. **Report gaps as a short list**, then fix the mechanical ones (stale pointers, missing cross-references) directly. Anything that's actually new creative content (a missing NPC motive, a new encounter) goes back through the discuss-before-write rule in `CLAUDE.md`, don't silently invent material to fill a gap.
5. **Only give the "we're set" verdict once the checklist's actually been walked**, not as a reflexive yes to "are we ready."

## The checklist

**Structure and cross-references**
- Every pointer to another doc or an earlier section of this one still resolves (no stale references to a superseded prep doc, an old section number, a cut scene).
- The "Where things stand" recap at the top matches the doc's own final content, not an earlier draft of it.

**Mechanics**
- Every DC follows the campaign's standing ladder (10/13/16+, see `rules/Bastions.md`'s cartography table for the convention) and is actually present where a check is implied, not just gestured at.
- Every creature introduced has a stat block, or a clear pointer to one in `rules/Stat Blocks.md` or the companion's Reference section.
- Loot, pricing, and gp totals are internally consistent (a price quoted twice should match, a total should add up).

**Spotlight and tone**
- Both PCs get a real, active beat, not just a mention, per the standing design principle in `CLAUDE.md`. Check specifically for one PC having mechanical/active material while the other is purely reactive, this is the single most common gap.
- The tone compass (70/20/10) is being counterweighted correctly against how the last session actually ran, per the DM-style notes in `CLAUDE.md`.
- Any antagonist or obstacle has a real identity and motive, not just a stat line, "problem not villain" per the campaign's house style.

**Plot and continuity**
- The session actually advances at least one of the three Spine threads (`campaign/Story Spine.md`), or is deliberately a bottle episode, confirm which rather than assume.
- New threads this session's own content creates are banked in the "Looking Ahead" / ending-hook section, not left implicit. Check specifically for threads the main content itself generates (a new NPC's unstated motive, an item whose origin isn't explained yet).
- Nothing contradicts settled canon, spot-check names, numbers, and established facts against `campaign/Name Index.md` and `campaign/Story Spine.md`.

**Props and handouts**
- Any player-facing handout built for this session has been checked against the `handout-prop-split` skill, no GM-only content leaking into something a player will actually hold.

## What "set" actually means

State the verdict plainly once the pass is done: what's confirmed complete, what's genuinely open by design (a branch point meant to resolve live at the table, not a gap), and what (if anything) still needs a fix. Don't pad a clean result with hedging, and don't give a clean verdict without having actually walked the list this pass.
