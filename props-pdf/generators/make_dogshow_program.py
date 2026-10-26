#!/usr/bin/env python3
"""Generate the player-facing International Space Dog Show program
(sessions/handouts/dog-show-program.pdf). "Festive" theme, 5 pages:
title/history, categories, judges, past champions, entry & conduct.

GM-only material (full entrant roster, Plume, halftime reveal, attendees,
conspiracies, DC tables) deliberately does NOT belong here -- see
sessions/Episode - The International Space Dog Show.md instead, and the
handout-prop-split skill for why that split exists.

Run from the repo root: python3 props-pdf/generators/make_dogshow_program.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from handout_pdf_helpers import Page, THEMES
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "sessions", "handouts", "dog-show-program.pdf")
OUT = os.path.abspath(OUT)
os.makedirs(os.path.dirname(OUT), exist_ok=True)

page = Page(OUT, THEMES["festive"])
c = page.c
w, h = letter

# ============================================================
# PAGE 1: title
# ============================================================
page.bg()
y = h - 1.1 * inch
c.setFillColor(page.theme["accent"])
c.setFont("Helvetica-Bold", 11)
c.drawCentredString(w / 2, y, "O F F I C I A L   P R O G R A M   &   R U L E S")
y -= 0.42 * inch
c.setFillColor(page.theme["ink"])
c.setFont("Helvetica-Bold", 26)
c.drawCentredString(w / 2, y, "THE INTERNATIONAL")
y -= 0.38 * inch
c.drawCentredString(w / 2, y, "SPACE DOG SHOW")
y -= 0.3 * inch
c.setStrokeColor(page.theme["faint"])
c.setLineWidth(1)
c.line(1.3 * inch, y, w - 1.3 * inch, y)
y -= 0.3 * inch
c.setFont("Helvetica-Oblique", 12)
c.drawCentredString(w / 2, y, "A Travelling Exhibition of Pets, Mascots, and Companion Creatures")
y -= 0.22 * inch
c.drawCentredString(w / 2, y, "from Every Corner of Wildspace")
y -= 0.45 * inch

c.setFont("Helvetica", 10.5)
c.setFillColor(page.theme["ink"])
for line in [
    "Hosted this cycle at the Floating Pavilion, three days' sail coreward of the Rock of Bral.",
    "All chartered crews, independent operators, and persons of quality welcome to enter.",
    "Entrants need not be dogs. Entrants need not, strictly, be animals. The judges have seen worse.",
]:
    c.drawCentredString(w / 2, y, line)
    y -= 0.2 * inch

y -= 0.3 * inch
y = page.section(y, "What This Show Actually Is")
y = page.para(y, "Founded some one hundred and eighty years ago by the astral elf Ophelia Rask, who grew "
    "tired of watching the founding houses turn every gathering into a negotiating table and wanted "
    "one event where that was expressly, formally forbidden. Lady Rask presides still, the Astral "
    "Kennel Concordance having run the Show every cycle since under her own continued eye, and the "
    "no-business rule still holds on the judging floor, by long tradition rather than any enforceable "
    "law, which has somehow made it stick harder than a law would have.", size=9.5, leading=0.165)
y -= 0.08 * inch
y = page.para(y, "It has become, almost by accident, the one place in known space where rival houses, "
    "independent crews, and everyone between them stand shoulder to shoulder and mean it, if only "
    "for the length of a judging round. Attendance is itself a kind of status. Winning, even a minor "
    "category, follows a name for seasons. One hundred and eighty years is long enough that nobody "
    "alive remembers a Wildspace without it.", size=9.5, leading=0.165)
page.show_page()

# ============================================================
# PAGE 2: categories
# ============================================================
y = page.header("This Cycle's Categories")

c.setFillColor(page.theme["ink"])
c.setFont("Helvetica-BoldOblique", 9.5)
c.drawString(1 * inch, y, "Physical Lane, bracketed by size class (Tiny through Huge)")
y -= 0.22 * inch

categories_physical = [
    ("Best Presentation", "House Delverane",
     "Coat, scale, carapace, plumage, whatever the species in question actually has, judged against its own kind's standard, never cross-species."),
    ("The Long Run", "House Stoneward",
     "A timed obstacle course run in full gravity-plane conditions. Speed and composure both count."),
    ("The Proving Round", "House Stoneward",
     "A supervised sparring trial between willing, evenly matched entrants, judged on skill and control. Ends at the first clean hit or clear dominance. No serious harm permitted."),
    ("Strength of Pull", "House Stoneward",
     "A straightforward hauling and towing trial. Raw power, nothing more."),
    ("Fastest in Show", "House Delverane",
     "A straight sprint, no obstacles, no course, just speed."),
    ("The Cargo Run", "House Stoneward",
     "Hauling a sandbag load from one post to another and back. Strength and endurance both, judged on pace held, not a burst of it."),
]
for name, sponsor, desc in categories_physical:
    c.setFillColor(page.theme["ink"])
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1.1 * inch, y, name)
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(page.theme["faint"])
    c.drawRightString(w - 1.1 * inch, y + 0.01 * inch, "sponsored by " + sponsor)
    y -= 0.165 * inch
    y = page.para(y, desc, font="Helvetica-Oblique", size=8.5, indent=1.25, leading=0.145)
    y -= 0.05 * inch

y -= 0.08 * inch
c.setFillColor(page.theme["ink"])
c.setFont("Helvetica-BoldOblique", 9.5)
c.drawString(1 * inch, y, "Open Field, species and size both irrelevant")
y -= 0.22 * inch

categories_open = [
    ("Most Convincing Trick", "House Vellum",
     "A trick is convincing if the record would support that the animal meant to do it."),
    ("Best Costume", "House Nightbreeze",
     "Judged on craft, concept, and the entrant's own evident tolerance for wearing it."),
    ("Best Vocalization", "the Concordance",
     "Song, call, cry, or signal, whatever the entrant actually makes. Judged on control and carrying power."),
]
for name, sponsor, desc in categories_open:
    c.setFillColor(page.theme["ink"])
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1.1 * inch, y, name)
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(page.theme["faint"])
    c.drawRightString(w - 1.1 * inch, y + 0.01 * inch, "sponsored by " + sponsor)
    y -= 0.165 * inch
    y = page.para(y, desc, font="Helvetica-Oblique", size=8.5, indent=1.25, leading=0.145)
    y -= 0.05 * inch

y -= 0.05 * inch
c.setFont("Helvetica-Oblique", 9)
c.setFillColor(page.theme["accent"])
c.drawString(1.1 * inch, y, "Each entrant may be registered for up to three categories, no more.")
y -= 0.3 * inch

y = page.section(y, "Best in Show")
y = page.para(y, "Not a category of its own, Best in Show is chosen by the full judging panel from among "
    "this cycle's category champions. This cycle's purse is sponsored in full by Lord Wendell "
    "Carraway, of his own house's generosity and at considerable personal expense, a gesture the "
    "committee is given to understand he will mention unprompted at every opportunity between now "
    "and the judging.")
y -= 0.05 * inch
c.setFont("Helvetica-Bold", 12)
c.setFillColor(page.theme["accent"])
c.drawString(1.1 * inch, y, "Purse: 20,000 gp")
y -= 0.3 * inch

y = page.section(y, "Honorary, Not Judged")
c.setFillColor(page.theme["ink"])
c.setFont("Helvetica-Bold", 10)
c.drawString(1.1 * inch, y, "Longest Serving Ship's Animal")
y -= 0.17 * inch
y = page.para(y, "Presented, not competed for, to the entrant with the longest verifiable charter-service record. The committee asks only for the paperwork.", font="Helvetica-Oblique", size=9, indent=1.25, leading=0.15)

page.footer("(continued: the judging panel, past champions, and the rules)")
page.show_page()

# ============================================================
# PAGE 3: judges
# ============================================================
y = page.header("This Cycle's Judging Panel", "Two panels of three, by lane. No judge crosses between them.")

y = page.section(y, "Physical Lane")
judges_phys = [
    ("Magistrate Yevelda Thorn", "House Delverane",
     "A silver elf of considerable age and considerably more opinions, fixated on symmetry to the point of personal eccentricity. Known to disqualify an otherwise flawless entrant for one crooked whisker."),
    ("Commodore (Ret.) Ossian Vale", "House Stoneward",
     "A retired Stoneward patrol officer, blunt and unsentimental, respects raw competence over any amount of polish. The panel's hardest mark by a wide margin, and everyone knows it."),
    ("Baroness Isolde Fenmark", "independent",
     "Old money, and proud of it. Cares more for bloodline and lineage than for anything an entrant actually does on the floor, a real source of friction with judges who value raw skill over pedigree."),
]
for name, house, desc in judges_phys:
    c.setFillColor(page.theme["ink"])
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(1.1 * inch, y, name)
    c.setFont("Helvetica-Oblique", 8.5)
    c.setFillColor(page.theme["accent"])
    c.drawRightString(w - 1.1 * inch, y + 0.01 * inch, house)
    y -= 0.19 * inch
    y = page.para(y, desc, size=9, leading=0.155)
    y -= 0.1 * inch

y -= 0.1 * inch
y = page.section(y, "Open Field Lane")
judges_open = [
    ("Madam Quill", "House Nightbreeze",
     "A gnome barely taller than most of the entrants, easily delighted and impossible to win over twice with the same trick. Takes meticulous, illegible notes throughout every round."),
    ("Factor Renshaw Vell", "House Vellum",
     "Aging and exacting, judges every entrant against precedent and the official record. If it hasn't happened before, he wants to know why it's happening now."),
    ("Professor Aldric Wren", "independent",
     "A scholar by training, values originality above all else, and is genuinely hard to impress with anything that reads as derivative of a prior winner."),
]
for name, house, desc in judges_open:
    c.setFillColor(page.theme["ink"])
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(1.1 * inch, y, name)
    c.setFont("Helvetica-Oblique", 8.5)
    c.setFillColor(page.theme["accent"])
    c.drawRightString(w - 1.1 * inch, y + 0.01 * inch, house)
    y -= 0.19 * inch
    y = page.para(y, desc, size=9, leading=0.155)
    y -= 0.1 * inch

page.footer("A fifth chair sits, as ever, at the head of the judging table. It is not filled.")
page.show_page()

# ============================================================
# PAGE 4: past champions
# ============================================================
y = page.header("Ten Years of Best in Show")

champions = [
    ("Last cycle", "Oatmeal", "golden retriever, entirely ordinary, proof the show doesn't only reward the exotic"),
    ("2 cycles back", "Vex", "brass dragon hatchling"),
    ("3 cycles back", "Bramble", "blink dog, a win the judges still privately dispute"),
    ("4 cycles back", "Kitty", "tiny displacer beast kitten"),
    ("5 cycles back", "Bellows", "juvenile hippogriff, won asleep, a program legend"),
    ("6 cycles back", "Anchor", "hauling mastiff, \"the honest work year\""),
    ("7 cycles back", "Needle", "astral hamster"),
    ("8 cycles back", "Marmalade", "orange tabby, didn't seem to notice winning"),
    ("9 cycles back", "Scuttle", "trained giant beetle"),
    ("10 cycles back", "Dot", "a space guppy in a floating bowl, \"the year nobody saw it coming\""),
]
c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(page.theme["accent"])
c.drawString(1.1 * inch, y, "Cycle")
c.drawString(2.6 * inch, y, "Champion")
c.drawString(4.3 * inch, y, "Notes")
y -= 0.08 * inch
c.setStrokeColor(page.theme["faint"])
c.line(1.1 * inch, y, w - 1.1 * inch, y)
y -= 0.22 * inch
from handout_pdf_helpers import wrap as _wrap
for cycle, name, note in champions:
    c.setFillColor(page.theme["ink"])
    c.setFont("Helvetica", 9.5)
    c.drawString(1.1 * inch, y, cycle)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(2.6 * inch, y, name)
    c.setFont("Helvetica-Oblique", 8.5)
    note_lines = _wrap(note, "Helvetica-Oblique", 8.5, w - 5.5 * inch)
    for i, line in enumerate(note_lines):
        c.drawString(4.3 * inch, y - i * 0.14 * inch, line)
    y -= max(0.24 * inch, 0.14 * inch * len(note_lines))

y -= 0.1 * inch
y = page.para(y, "Several past champions are entered again this cycle. A veteran rarely retires "
    "quietly.", size=9)
page.show_page()

# ============================================================
# PAGE 5: entry & conduct
# ============================================================
y = page.header("Entry & Conduct, the Short Version")
c.setFillColor(page.theme["ink"])
c.setFont("Helvetica", 9.5)
rules = [
    "Entry is open to any companion creature accompanied by a sponsoring crew, house, or individual of record.",
    "Entrants must be collected, non-hostile, and under control at all times, judges' own discretion applies.",
    "Each entrant may be registered for up to three categories, no more.",
    "Sabotage, bribery, or interference with another entrant is grounds for immediate disqualification, should the committee ever actually catch anyone at it.",
    "The committee's judging decisions are final, binding, and occasionally inexplicable.",
]
for r in rules:
    r_lines = _wrap(r, "Helvetica", 9.5, w - 2.4 * inch)
    for i, line in enumerate(r_lines):
        prefix = "• " if i == 0 else "   "
        c.drawString(1.1 * inch, y, prefix + line)
        y -= 0.16 * inch
    y -= 0.04 * inch

page.footer("The International Space Dog Show thanks you for your continued, baffling enthusiasm.")
page.show_page()
page.save()
