#!/usr/bin/env python3
"""Generate the recovered-document handouts for the Quiet Verge derelict
(sessions/Session 5 Prep.md, section 2). Aged single-page notes and logs,
"parchment" theme. Run from the repo root: python3 props-pdf/generators/make_derelict_handouts.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from handout_pdf_helpers import Page, THEMES

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "sessions", "handouts")
OUT_DIR = os.path.abspath(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)


def make_pdf(filename, title, lines, header_note=None, font="Helvetica", size=12, leading=17):
    path = os.path.join(OUT_DIR, filename)
    page = Page(path, THEMES["parchment"])
    y = page.note_header(title, header_note=header_note)
    page.note_para(y, lines, font=font, size=size, leading=leading)
    page.show_page()
    page.save()


# 1. Cook's rationing note
make_pdf(
    "01-cooks-rationing-note.pdf",
    "Ration Tally, Week 9",
    [
        "Flour: 40 lb, holding at half since Thursday, should see us to the",
        "next Verge stop with room to spare.",
        "",
        "Water steady. Dorram says tell the Captain we're fine on stores",
        "either way.",
    ],
    header_note="Found: the galley. A tidy, finished note. Nothing urgent here.",
)

# 2. Bunk roster
make_pdf(
    "02-bunk-roster.pdf",
    "Quiet Verge, Bunk Assignments",
    [
        "1.  Capt. Wren Ashby",
        "2.  Helm  --  Ilsa Marrow",
        "3.  Eng  --  Pell Ostrander",
        "4.  Cook  --  Dorram Keel",
        "5.  Deckhand  --  Fen Caskey",
        "6.  Deckhand  --  (name worn away)",
    ],
    header_note="Found: crew quarters. Confirms the ship's name before her registry was scraped.",
    font="Courier",
)

# 3. Fen's letter home
make_pdf(
    "03-fens-letter-home.pdf",
    "A Letter, Unfinished Business Only in the Sense It Was Never Sent",
    [
        "Dearest Mother,",
        "",
        "Another late crossing, I'm losing count how many in a row now. Toller says it's nothing, just a slow season, but nobody who's run this route longer than me looks like they believe him either. The lane feels thinner than it used to, less to it, somehow, though I couldn't tell you what I mean by that if you asked.",
        "",
        "Don't worry, we're all fine and well fed, Dorram keeps us honest on that front if nothing else.",
        "",
        "I'll write again once we're through to port.",
        "",
        "All my love,",
        "Fen",
    ],
    header_note="Found: crew quarters, DC 20. A finished letter, never sent.",
    font="Helvetica-Oblique",
)

# 4. Cargo jettison log
make_pdf(
    "04-cargo-jettison-log.pdf",
    "Jettison Log, Quiet Verge",
    [
        "Day 1 -- 40 crates dried stores released, 10 crates retained (essential)",
        "Day 1 -- 2 casks water retained",
        "Day 2 -- cargo manifest items 14-30 released, nonessential trade goods",
        "Day 2 -- spare rigging retained",
        "Day 3 -- remaining nonessential cargo released per Captain's order",
        "",
        "Final tally: hold lightened by roughly eleven hundred pounds.",
    ],
    header_note="Found: cargo hold. A controlled, methodical lightening, not a panic dump.",
    font="Courier",
)

# 5. Engineer's maintenance log
make_pdf(
    "05-engineers-maintenance-log.pdf",
    "Maintenance Log -- P. Ostrander",
    [
        "Day 58 -- Helm running hot on every correction. Logged it, nothing conclusive yet.",
        "",
        "Day 60 -- Same as yesterday, worse. Coupling shouldn't need this much coaxing.",
        "",
        "Day 61 -- Helm's been reaching for nothing three days running now. Coupling's hot to the touch even dead. Nothing left to do about it from down here. Reported to the Captain.",
    ],
    header_note="Found: engineering, DC 12.",
)

# 6. Helmsman's logbook
make_pdf(
    "06-helmsmans-logbook.pdf",
    "Helm Logbook -- I. Marrow",
    [
        "Week 6 -- Crossing ran four hours long again. Charts say it shouldn't.",
        "",
        "Week 7 -- Fewer lights in the water tonight. Maybe just overcast.",
        "",
        "Week 8 -- Six hours long now. I don't like how quiet it's gotten out there.",
        "",
        "(final entry, mid-line)",
        "Position holds. Heading holds. We are not mo--",
    ],
    header_note="Found: bridge, DC 13/15/18.",
)

make_pdf(
    "06b-helmsmans-course-scrap.pdf",
    "A Separate Scrap, Tucked Into the Log",
    [
        "Hull course set: dead reckoning for the Rock of Bral.",
        "No power to correct once we're gone.",
        "She'll find it or she won't.",
    ],
    header_note="Found: bridge, DC 15.",
    font="Helvetica-Oblique",
)

# 7. Captain's log
make_pdf(
    "07-captains-log.pdf",
    "Captain's Log -- W. Ashby",
    [
        "(earlier entries, routine, business as usual, omitted here)",
        "",
        "Final entry --",
        "",
        "The water's given out from under us. No getting it back out here, not with anything we have aboard. Hull can't outlast the drift on stores alone, not for six of us. The boats can, if we're fast and don't waste what we're given.",
        "",
        "Jettisoning what we can spare, splitting the crew between both boats, running for the Calder waypoint, the last mark the charts still confirm. Leaving the Verge behind, powered down, heading set for Bral on dead reckoning, in case anyone ever finds her and wonders.",
        "",
        "No one's done anything wrong here. The water just stopped.",
        "",
        "Whoever reads this, I hope it found you well.",
    ],
    header_note="Found: captain's cabin, DC 15. The core reveal.",
    leading=16,
)

make_pdf(
    "07b-captains-private-scrap.pdf",
    "A Second Scrap, Tucked In the Same Log",
    [
        "Wren --",
        "",
        "If we don't make it, don't let them say we panicked.",
        "We did the math. We did it right.",
        "",
        "-- W.",
    ],
    header_note="Found: captain's cabin, DC 20. The one crack in the composure.",
    font="Helvetica-Oblique",
)

print("done")
