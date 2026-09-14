---
name: session-structure
description: The standing beat skeleton for Astral Vagabonds session prep docs (cold open, main content, social, battle, ending hook), how to interrogate what a session actually needs before drafting it, and how a session usually ends up as a comprehensive run-ready HTML companion. Use whenever building a new `sessions/Session N Prep.md` or `sessions/session-N-companion.html`, planning "what happens next session" in chat, or checking whether a prep doc is missing a beat. Companion to `dnd-writing` (voice) and `rules/DMing Craft.md` (scene craft); this skill is about session-level shape and process, not sentence-level style.
---

# Session structure for Astral Vagabonds

`sessions/Session 2 Prep.md` is the clearest worked example of this shape (cold open, Orena/Estra scene, Aerion's beats, bastion actions, the Bral homecoming, numbered 1 through 5, no battle section because that session didn't have one). This skill names that shape so it's a deliberate starting point going forward, not something re-derived from scratch each time. `sessions/Session 3 Prep.md` is a different kind of doc, three parallel job-branch writeups for whichever contract gets picked, not an example of the beat skeleton itself.

**This skeleton is calibrated for Tier 1's job-of-the-week rhythm** (`campaign/Tier 1.md`, `rules/Contracts.md`): one contract, one voyage, one clean loop back to port. Revisit it once multi-session arcs start (`campaign/Arc Map.md`), a session inside a longer arc may not have a discrete job, a port return, or even a cold open in the usual sense, and forcing this shape onto that kind of session would hurt it more than help.

## The skeleton

1. **Where things stand, going in.** A short recap block at the top of the prep doc: open threads, last session's fallout, current rank/money/ship state. For the DM's own orientation, not for the players.
2. **Cold open.** Comedic or warm by default (per the 70/20/10 tone compass), short, and it's what actually kicks the session into motion. A real scene with a landing beat, not a recap. Applies when the session opens on a job or voyage beat; an arc session picking up mid-crisis may not need one.
3. **Main content.** The job, the voyage, the location, or the arc beat, whatever the session is actually about. Usually the longest section, and the one with the most branch points.
4. **Social beats, one per PC.** Both PCs need a real scene, not just a mention. Look first for a way to fold both into one joint scene (his numbers, her instinct, both reading the same wrongness) before defaulting to two solo beats in the same session, per the standing design principle in `CLAUDE.md`. NPC crew B-plot material lives here too.
5. **Battle, if the job calls for it.** Not mandatory. Combat is the second pillar, behind social, per `campaign/Campaign Overview.md`'s pillar priority. When it's in, calibrate it so it's survivable and give it real stakes, not a token scuffle. When it's out, the section simply doesn't exist in the prep doc, don't stub it just to show it was considered.
6. **Bastion actions / downtime**, when the voyage loop calls for a leg with nothing else going on.
7. **Return to port / fallout.** Rumors, Manifest Board movement, consequences catching up. Only when the session actually closes at a berth, a session that ends mid-arc, mid-transit, or on a cliffhanger skips this by design, not by omission.
8. **Ending: a hook, a mystery, or a cliffhanger.** Every session ends on something that carries forward, named explicitly so it doesn't get lost between sessions. Check `sessions/Session Ideas.md` for anything ready to seed here, and add anything new that surfaces but doesn't get used.

## Before you build: clarify first

Don't start writing a full prep doc from a one-line request. Interrogate the session the way a real planning conversation would, the same spirit as a brainstorming pass, ask before assuming, surface the decision points, don't silently pick for the DM. At minimum, get clear on:

- **What kind of session is this?** A Tier 1 job-of-the-week (this skeleton applies cleanly), an arc set piece or location crawl (skeleton mostly doesn't apply, see above), a bottle episode, a one-off social session, something else.
- **What's already in the DM's head?** Which contract got picked, which NPC or thread he wants to spotlight, any beat he already knows he wants. Don't invent a premise he's already decided; ask before drafting one.
- **Which skeleton parts actually make sense here?** Walk the list (cold open, main content, social beats, battle, bastion, port fallout, ending hook) out loud and ask which apply, rather than defaulting to all of them. A battle-free session or a session with no port return is a legitimate answer, confirm it rather than assume it.
- **What's the tone target relative to the last session?** Check whether the prior session ran hot or cold against the 70/20/10 compass before deciding how this one should counterweight.
- **Is there anything on `sessions/Session Ideas.md` he wants seeded in**, or anything from `Live threads after session 1` (`CLAUDE.md`) that needs to surface.

Work through these before committing to a structure, the same way session 2's bastion mechanics, lockbox contents, and fallout beats all went through a discuss-first pass rather than getting written straight to file. Match the depth of interrogation to the size of the ask, a small tweak doesn't need the full list, a from-scratch session does.

## The typical deliverable: the HTML companion

For a session that's actually going to be run at the table, the finished artifact is usually a **comprehensive, self-contained HTML companion** (`sessions/session-N-companion.html`), not just the markdown prep doc. `sessions/session-1-companion.html` and `sessions/session-2-companion.html` are the model: everything needed to run the session without opening another file, run sheet, cold open, full scene scripts, stat blocks, NPC voice cards, ship stats, current money, Manifest Board snapshot, and any handout props, in one page, matching that design system (Fraunces/IBM Plex Sans/IBM Plex Mono, light/dark theme, `.card`/`.beat`/`.call`/`.read`/`.crew`/`.tile`/`.spec` components).

The markdown prep doc (from `sessions/Session Prep Template.md`) comes first, it's where the beats get discussed, revised, and confirmed with the DM. The HTML companion comes after, once the content is settled, as the run-ready version. Don't jump straight to HTML before the prep doc's content has actually been agreed on, the discuss-first clarification above still applies to what goes into the companion.

## How to use it

- **This is a menu, not a form.** Number the sections you actually use, sequentially, when you write the prep doc, the way `Session 2 Prep.md` does. Don't pre-number a template and then leave gaps or stubs where a beat doesn't apply.
- **Reorder or merge freely.** A social beat can come before the main content if the job's shape wants it that way. A cold open and the ending hook can be the same scene bookending a single tense session. Fit the shape to the session, not the other way around.
- **Start a new prep doc from `sessions/Session Prep Template.md`.** It has these sections as bracketed prompts, meant to be cut down, not filled in wholesale.
- **Player agency still applies inside every beat.** The social-beats section especially: describe the situation and the spotlight opportunity, never script what Orena or Aerion choose, feel, or do. See the hard rule in `CLAUDE.md`.
- **Follow the tone compass through the whole skeleton, not just the cold open.** A hot ending (real danger, a genuine cliffhanger) is fine occasionally, but if the last session already ran hot, counterweight toward warmth in this one, per the DM-style notes in `CLAUDE.md`.
- **When a session doesn't fit this shape at all** (a full arc set piece, a multi-session location crawl), say so explicitly in the prep doc's opening line rather than forcing sections that don't serve it. The skeleton exists to save re-deriving the common case, not to constrain the uncommon one.
