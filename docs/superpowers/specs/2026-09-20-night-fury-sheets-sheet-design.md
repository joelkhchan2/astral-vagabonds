# Night Fury Google Sheets ship sheet + Apps Script — Design

## Context

`ships/night-fury-stat-card.html` (published via GitHub Pages) is the static reference card for the *Night Fury*. This spec covers a separate deliverable: a **Google Sheets** version that adds **live session tracking** the static card can't do — current HP, ammo remaining, cargo manifest line items, and per-round station assignments that change during play.

The Sheet already exists as a copy of Orena's PC character sheet template (`fileId: 1K4f4KNXDitZT8jcGyWIentumkTmfWrwZp6j92WyLEVs`, titled "Night Fury"), unmodified. It has a bound Apps Script project (`scriptId: 1p-a0dOERHJe3R2Sxia3el1Up4UcpTAH4SvxLa7qMB47Aw_q_66qCfGZa`) that is currently empty boilerplate (`function myFunction() {}` and default `appsscript.json`) — confirmed via `clasp clone`, nothing to preserve.

Source of truth for stats: `ships/Night Fury.md` (ship) and `rules/Stat Blocks.md` (crew). The Sheet's live fields are the only things that change during play; these docs are not touched by the script.

## Tabs

1. **Night Fury** — main sheet, ship-scale stats in Orena template's visual style:
   - Static block: AC 19 (+Plating I), Damage Threshold 20, Speed (~45 ft tactical + Trim Rig), Cargo 20 tons, Crew capacity 11 (running with 7), Air (120 days base).
   - Live block: current HP (of 250), repair bill accrued.
   - Weapon Stations table: 2 ballistae (port/starboard) + blunt ram, each with a live ammo-remaining field (of 50 standard shots) and the Sureshot/Ready Magazine upgrade notes.
   - Systems & Add-ons: Hull, Helm, Armor, Weapon upgrades, Mobility, Life support — from the Build table in `Night Fury.md`.
   - Layout: upper deck / lower deck room list, static flavor text.
   - History / personality blocks: static flavor text, ported as-is.

2. **Crew Aboard** — the 7 running the ship: the 2 PCs (Orena, Aerion) plus the 5 NPCs from `rules/Stat Blocks.md` (Estra, Tack, Finny, Brass, Oz). Columns: Name, Species/Class, Role, Current Station (dropdown: Pilot/Gunner/Engineer/Coordinator/Personal action/Off-duty), HP (live, of their max), Notes. Flurry (Aerion's non-combat pet) gets a separate note, not a station-crewing row — he doesn't stand a station.

3. **Bastion Facilities** — full catalog, all 4 DMG'24 levels (5/9/13/17), 29 facilities total. Columns: Facility, Level, Prereq, Space, Hirelings, Order, Description (full text, not paraphrased — sourced from the DMG'24 text the user supplied). A pinned/highlighted section calls out the ship's actual chosen facilities (Aerion: Storehouse + one open slot; Orena: Library + Arcane Study) at the top, with the rest as reference below.

4. **Cargo Manifest** — repurposed from the old xlsx template's Inventory tab: live line-item cargo tracking against the 20-ton cap.

Dropped entirely (not ship-applicable): Spells, Spells - 1, Bard Table, Paladin Table, Multiclass Spell Slots, Leveling Table, Read Me.

## Apps Script (`Code.js`, replacing the empty boilerplate)

Custom `⚓ Night Fury` menu:
- **Apply Damage** — prompt for amount; if < 20 (damage threshold), no-op with a toast explaining why; otherwise subtract from live HP and add to the repair-bill tracker (20 gp/point, per `Night Fury.md` §Money).
- **Emergency Patch** — restores HP equal to a prompted engineer level, once per encounter per engineer (tracked via a per-session checkbox/flag on the sheet, reset by "Reset Round").
- **Fire Ballista** — prompts which gun (port/starboard) and decrements that gun's ammo field by 1.
- **Repair to Full** — resets HP to 250 and clears the repair-bill tracker (for use after downtime repairs are paid off narratively).
- **Reset Round** — clears per-round station assignments and Emergency Patch flags for a new encounter.

No dice roller, no PDF export, no proficiency-dot dropdown machinery — that was Orena's PC-sheet plumbing (skill checks driven by a shared proficiency-bonus cell), not applicable to a ship with no ability scores.

## Data flow

`Night Fury.md` / `Stat Blocks.md` stay canonical for base stats (max HP, AC, crew roster). The Sheet's live fields (current HP, ammo, cargo, station assignments, repair bill) are session state that only changes through play or the Apps Script menu — the script never writes back to the markdown docs.

## Out of scope

- Editing `ships/night-fury-stat-card.html` or the PDF generator — those stay as-is, this is a parallel deliverable.
- Verbatim DMG text beyond the Bastion Facilities catalog (no other WotC book text goes on the sheet).
- Any mechanic not already established in `Night Fury.md` or `rules/Rules & Systems.md` §8 (gunnery math, station rules) — the Sheet implements existing canon, it doesn't invent new ship rules.
