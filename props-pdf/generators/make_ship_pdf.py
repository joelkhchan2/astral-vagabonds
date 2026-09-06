#!/usr/bin/env python3
"""Generate a fillable D&D 5e vehicle stat block PDF for the Night Fury."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, black
from reportlab.pdfbase.pdfmetrics import stringWidth

PAGE_W, PAGE_H = letter
MARGIN = 50
CONTENT_W = PAGE_W - 2 * MARGIN

RED = HexColor("#7a1f1a")
RED_DEEP = HexColor("#58150f")
INK = HexColor("#1c1608")
INK_SOFT = HexColor("#4b3f2a")
FIELD_BG = HexColor("#fffdf7")

FONT_TITLE = "Helvetica-Bold"
FONT_BODY = "Times-Roman"
FONT_BODY_I = "Times-Italic"
FONT_LABEL = "Helvetica"
FONT_LABEL_B = "Helvetica-Bold"


def wrap_text(text, font, size, max_width):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if stringWidth(trial, font, size) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def taper_rule(c, x, y, w):
    c.setFillColor(RED)
    p = c.beginPath()
    p.moveTo(x, y + 3)
    p.lineTo(x + w, y + 5)
    p.lineTo(x + w, y)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def draw_field(c, name, x, y, w, h, multiline=False, tooltip=""):
    c.saveState()
    c.setStrokeColor(INK_SOFT)
    c.setFillColor(FIELD_BG)
    c.rect(x, y, w, h, fill=1, stroke=1)
    c.restoreState()
    flags = "multiline" if multiline else ""
    c.acroForm.textfield(
        name=name, tooltip=tooltip or name,
        x=x, y=y, width=w, height=h,
        borderStyle="inset", borderColor=INK_SOFT, borderWidth=0.6,
        fillColor=FIELD_BG, textColor=black,
        fontSize=9, fieldFlags=flags, forceBorder=False,
    )


def section_header(c, x, y, w, title):
    c.setFillColor(RED_DEEP)
    c.setFont(FONT_TITLE, 12)
    c.drawString(x, y, title)
    c.setStrokeColor(RED_DEEP)
    c.line(x, y - 3, x + w, y - 3)
    return y - 18


def draw_traits(c, x, y, w, traits, size=9.3, leading=11.8):
    for name, body in traits:
        lines = wrap_text((f"{name} " if name else "") + body, FONT_BODY, size, w)
        for i, line in enumerate(lines):
            if i == 0 and name:
                c.setFont(FONT_BODY_I, size)
                c.drawString(x, y, name + " ")
                name_w = stringWidth(name + " ", FONT_BODY_I, size)
                rest = line[len(name) + 1:]
                c.setFont(FONT_BODY, size)
                c.drawString(x + name_w, y, rest)
            else:
                c.setFont(FONT_BODY, size)
                c.drawString(x, y, line)
            y -= leading
        y -= 2
    return y


def tile(c, x, y, w, h, label, value):
    c.setStrokeColor(HexColor("#e6d2ae"))
    c.setFillColor(FIELD_BG)
    c.roundRect(x, y, w, h, 3, fill=1, stroke=1)
    c.setFillColor(INK_SOFT)
    c.setFont(FONT_LABEL, 6.6)
    c.drawCentredString(x + w / 2, y + h - 12, label.upper())
    c.setFillColor(RED_DEEP)
    c.setFont(FONT_TITLE, 12)
    c.drawCentredString(x + w / 2, y + 7, value)


def main():
    import os
    out = os.path.join(os.path.dirname(__file__), "..", "Night-Fury-Ship-Card.pdf")
    c = canvas.Canvas(out, pagesize=letter)
    c.setTitle("Night Fury - Vehicle Stat Block")
    x0 = MARGIN
    y = PAGE_H - MARGIN

    c.setFillColor(RED_DEEP)
    c.setFont(FONT_TITLE, 24)
    c.drawString(x0, y, "Night Fury")
    y -= 18
    c.setFillColor(INK_SOFT)
    c.setFont(FONT_BODY_I, 11)
    c.drawString(x0, y, "Colossal object (Sturdy Trader), crew capacity 11 · captain of record: Estra Vane")
    y -= 10
    taper_rule(c, x0, y, CONTENT_W)
    y -= 20

    # tiles row: AC, HP, Threshold, Speed, Cargo, Air
    tiles = [("Armor Class", "19 (+Plating I)"), ("Hit Points", "250"), ("Damage Threshold", "20"),
             ("Speed", "~45 ft."), ("Cargo", "20 tons"), ("Air", "120 days")]
    n = len(tiles)
    gap = 8
    tw = (CONTENT_W - gap * (n - 1)) / n
    th = 40
    for i, (label, value) in enumerate(tiles):
        tile(c, x0 + i * (tw + gap), y - th, tw, th, label, value)
    y -= th + 14

    c.setFillColor(INK_SOFT)
    c.setFont(FONT_BODY, 8.6)
    for line in wrap_text(
        "Damage threshold: a single hit under 20 does nothing to the hull. Speed: Trader 55 ft., minus 10 ft. for the "
        "Sturdy hull, plus 5 ft. from the Trim Rig, which also holds attitude when unhelmed. 100 million miles/day in open space.",
        FONT_BODY, 8.6, CONTENT_W):
        c.drawString(x0, y, line)
        y -= 11
    y -= 6

    c.setFillColor(INK)
    c.setFont(FONT_LABEL_B, 9)
    c.drawString(x0, y, "Current HP:")
    draw_field(c, "ship_hp_current", x0 + 62, y - 4, 60, 16, tooltip="Current HP")
    c.setFont(FONT_BODY, 9)
    c.drawString(x0 + 132, y, "/ 250")
    y -= 20
    taper_rule(c, x0, y, CONTENT_W)
    y -= 18

    props = [
        "Crew 11 (running with 7); one seat is always the helm",
        "Hull Sturdy Trader, Danforth Certified Hulls (prior-service)",
        "Helm Coilworks Mk IV (standard); piloting requires an attuned spellcaster holding concentration (Intelligence save to maintain it)",
        "Mobility Trim Rig (+5 ft., holds attitude unhelmed)",
        "Life Support none beyond base air envelope",
    ]
    c.setFont(FONT_BODY, 9.5)
    c.setFillColor(INK)
    for line in props:
        for ln in wrap_text(line, FONT_BODY, 9.5, CONTENT_W):
            c.drawString(x0, y, ln)
            y -= 12.5
    y -= 4
    taper_rule(c, x0, y, CONTENT_W)
    y -= 20

    y = section_header(c, x0, y, CONTENT_W, "Weapons")
    # simple two-row table
    col_x = [x0, x0 + 90, x0 + 260, x0 + 360]
    headers = ["Weapon", "Attack", "Damage", "Crew / Notes"]
    c.setFont(FONT_LABEL_B, 7.5)
    c.setFillColor(RED_DEEP)
    for cx, h in zip(col_x, headers):
        c.drawString(cx, y, h.upper())
    y -= 4
    c.setStrokeColor(RED_DEEP)
    c.line(x0, y, x0 + CONTENT_W, y)
    y -= 12

    rows = [
        ("Ballista x2", "+6 to hit, range 120/480 ft.", "16 (3d10) piercing",
         "Sureshot Rotator + Ready Magazine let 2 gunners fire one, 3 fire both in a round. 50 standard shots."),
        ("Ram (blunt)", "One attack, no weapon crew required", "Hull's listed ram damage",
         "Half the dealt damage comes back to the Night Fury, after her own damage threshold."),
    ]
    c.setFont(FONT_BODY, 8.6)
    c.setFillColor(INK)
    for name, atk, dmg, note in rows:
        note_lines = wrap_text(note, FONT_BODY, 8.6, CONTENT_W - (col_x[3] - x0))
        c.drawString(col_x[0], y, name)
        atk_lines = wrap_text(atk, FONT_BODY, 8.6, col_x[2] - col_x[1] - 6)
        dmg_lines = wrap_text(dmg, FONT_BODY, 8.6, col_x[3] - col_x[2] - 6)
        max_lines = max(len(atk_lines), len(dmg_lines), len(note_lines), 1)
        yy = y
        for i in range(max_lines):
            if i < len(atk_lines):
                c.drawString(col_x[1], yy, atk_lines[i])
            if i < len(dmg_lines):
                c.drawString(col_x[2], yy, dmg_lines[i])
            if i < len(note_lines):
                c.drawString(col_x[3], yy, note_lines[i])
            yy -= 10.5
        y = yy - 4
        c.setStrokeColor(HexColor("#e6d2ae"))
        c.line(x0, y + 8, x0 + CONTENT_W, y + 8)
    y -= 8
    taper_rule(c, x0, y, CONTENT_W)
    y -= 20

    y = section_header(c, x0, y, CONTENT_W, "Crew Stations")
    stations = [
        ("Pilot", "Flying is free. One maneuver per round: Evasive Action, Full Burn, Ram, or Boarding Action."),
        ("Gunner", "Crews a ballista. See the weapons table for the action-economy math."),
        ("Engineer", "Emergency Patch: Technology or Intelligence DC 12, ship regains HP equal to the engineer's level, once per encounter."),
        ("Coordinator", "Once per round: grant advantage, impose disadvantage, or let a station act again out of order."),
    ]
    y = draw_traits(c, x0, y, CONTENT_W, stations)
    y -= 4
    taper_rule(c, x0, y, CONTENT_W)
    y -= 18

    y = draw_traits(c, x0, y, CONTENT_W, [
        ("Reactive Repair (Tack, if aboard).", "When the ship takes damage exceeding its damage threshold, reduces that damage by 10."),
        ("She Talks Back.", "Not a mechanical trait. Tack will insist otherwise."),
    ])

    # tracking row
    y -= 6
    c.setFillColor(INK_SOFT)
    c.setFont(FONT_LABEL, 8)
    c.drawString(x0, y, "SHOTS REMAINING")
    c.drawString(x0 + 180, y, "REPAIRS OWED (GP)")
    draw_field(c, "ship_shots", x0, y - 20, 100, 16, tooltip="Ballista shots remaining")
    draw_field(c, "ship_repairs", x0 + 180, y - 20, 100, 16, tooltip="Repairs owed in gp")
    y -= 34

    c.setFont(FONT_LABEL, 8)
    c.drawString(x0, y, "CONDITIONS / NOTES")
    draw_field(c, "ship_notes", x0, y - 40, CONTENT_W, 34, multiline=True, tooltip="Conditions and notes")

    c.showPage()
    c.save()
    print("done")


if __name__ == "__main__":
    main()
