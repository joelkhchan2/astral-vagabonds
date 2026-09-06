#!/usr/bin/env python3
"""Generate a fillable D&D 5e-style stat block PDF for the Night Fury crew."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase.pdfmetrics import stringWidth

PAGE_W, PAGE_H = letter
MARGIN = 50
CONTENT_W = PAGE_W - 2 * MARGIN

RED = HexColor("#7a1f1a")
RED_DEEP = HexColor("#58150f")
INK = HexColor("#1c1608")
INK_SOFT = HexColor("#4b3f2a")
PAPER_EDGE = HexColor("#e6d2ae")
FIELD_BG = HexColor("#fffdf7")

FONT_TITLE = "Helvetica-Bold"
FONT_BODY = "Times-Roman"
FONT_BODY_B = "Times-Bold"
FONT_BODY_I = "Times-Italic"
FONT_LABEL = "Helvetica"
FONT_LABEL_B = "Helvetica-Bold"


def wrap_text(text, font, size, max_width):
    words = text.split(" ")
    lines = []
    cur = ""
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
    c.setStrokeColor(RED)
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


def draw_traits(c, x, y, w, traits, size=9.3, leading=11.6):
    """traits: list of (name_or_None, body). Returns new y."""
    for name, body in traits:
        text = (f"{name} " if name else "") + body
        # measure name in italic-bold, rest in roman: wrap whole line in roman width for simplicity
        lines = wrap_text(text, FONT_BODY, size, w)
        for i, line in enumerate(lines):
            c.setFont(FONT_BODY, size)
            if i == 0 and name:
                # redraw first line with bold-italic name prefix
                c.setFont(FONT_BODY_I, size)
                c.drawString(x, y, name + " ")
                name_w = stringWidth(name + " ", FONT_BODY_I, size)
                rest = line[len(name) + 1:]
                c.setFont(FONT_BODY, size)
                c.drawString(x + name_w, y, rest)
            else:
                c.drawString(x, y, line)
            y -= leading
        y -= 2
    return y


def draw_card(c, data):
    x0 = MARGIN
    y = PAGE_H - MARGIN

    c.setFillColor(RED_DEEP)
    c.setFont(FONT_TITLE, 20)
    c.drawString(x0, y, data["name"])
    y -= 16
    c.setFillColor(INK_SOFT)
    c.setFont(FONT_BODY_I, 10.5)
    c.drawString(x0, y, data["subtitle"])
    y -= 10
    taper_rule(c, x0, y, CONTENT_W)
    y -= 14

    c.setFillColor(INK)
    c.setFont(FONT_BODY, 10.5)
    c.drawString(x0, y, f"Armor Class {data['ac']}")
    y -= 15
    c.drawString(x0, y, f"Hit Points {data['hp']}")
    draw_field(c, f"{data['id']}_hp_current", x0 + stringWidth(f"Hit Points {data['hp']}   Current: ", FONT_BODY, 10.5), y - 4, 55, 16, tooltip="Current HP")
    c.setFont(FONT_BODY, 10.5)
    c.drawString(x0 + stringWidth(f"Hit Points {data['hp']}   ", FONT_BODY, 10.5), y, "Current:")
    y -= 15
    c.drawString(x0, y, f"Speed {data['speed']}")
    y -= 10
    taper_rule(c, x0, y, CONTENT_W)
    y -= 16

    # ability score table
    abbrs = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    col_w = CONTENT_W / 6
    c.setFont(FONT_LABEL_B, 8.5)
    c.setFillColor(RED_DEEP)
    for i, ab in enumerate(abbrs):
        cx = x0 + i * col_w + col_w / 2
        c.drawCentredString(cx, y, ab)
    y -= 12
    c.setFont(FONT_BODY, 9.5)
    c.setFillColor(INK)
    for i, val in enumerate(data["abilities"]):
        cx = x0 + i * col_w + col_w / 2
        c.drawCentredString(cx, y, val)
    y -= 10
    taper_rule(c, x0, y, CONTENT_W)
    y -= 14

    c.setFont(FONT_BODY, 9.5)
    for line in data["props"]:
        c.setFillColor(INK)
        lines = wrap_text(line, FONT_BODY, 9.5, CONTENT_W)
        for ln in lines:
            c.drawString(x0, y, ln)
            y -= 12
    y -= 2
    taper_rule(c, x0, y, CONTENT_W)
    y -= 16

    if data.get("traits"):
        y = draw_traits(c, x0, y, CONTENT_W, data["traits"])

    if data.get("actions"):
        y -= 4
        c.setFillColor(RED_DEEP)
        c.setFont(FONT_TITLE, 11)
        c.drawString(x0, y, "Actions")
        c.setStrokeColor(RED_DEEP)
        c.line(x0, y - 3, x0 + CONTENT_W, y - 3)
        y -= 16
        y = draw_traits(c, x0, y, CONTENT_W, data["actions"])

    if data.get("reactions"):
        y -= 4
        c.setFillColor(RED_DEEP)
        c.setFont(FONT_TITLE, 11)
        c.drawString(x0, y, "Reactions")
        c.setStrokeColor(RED_DEEP)
        c.line(x0, y - 3, x0 + CONTENT_W, y - 3)
        y -= 16
        y = draw_traits(c, x0, y, CONTENT_W, data["reactions"])

    # notes box, right after content, with a floor so it never sits too high on a short card
    notes_label_y = min(y - 14, PAGE_H - MARGIN - 470)
    notes_y = notes_label_y - 38
    c.setFillColor(INK_SOFT)
    c.setFont(FONT_LABEL, 8)
    c.drawString(x0, notes_label_y, "CONDITIONS / NOTES")
    draw_field(c, f"{data['id']}_notes", x0, notes_y, CONTENT_W, 34, multiline=True, tooltip="Conditions and notes")

    c.showPage()


CREW = [
    dict(id="estra", name='Captain Estra Vane', subtitle="Medium humanoid (human), Captain / Main Helmsman · CR 2 (450 XP)",
         ac="15 (studded leather)", hp="58 (9d8 + 18)", speed="30 ft.",
         abilities=["12 (+1)", "14 (+2)", "14 (+2)", "16 (+3)", "15 (+2)", "13 (+1)"],
         props=["Saving Throws Int +6, Wis +5",
                "Skills Insight +5, Investigation +6, Persuasion +4, Piloting +6",
                "Senses passive Perception 12",
                "Languages Common, Elvish, Draconic",
                "Challenge 2 (450 XP)"],
         traits=[("Fifteen Years at the Bottom.", "Advantage on saving throws against being frightened or charmed."),
                 ("Once a Commodore (Recharges after a Short Rest).", "Bonus action: an ally within 30 ft. who can see or hear her gains advantage on their next attack roll, save, or ability check.")],
         actions=[("Rapier.", "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage."),
                  ("Command the Deck (1/Combat).", "Directs one crew station to act immediately, out of the normal order.")],
         reactions=[("Steady Hand.", "When the ship's pilot would lose concentration from damage, Estra grants them advantage on the concentration save.")]),

    dict(id="tack", name="Tack", subtitle="Small construct (autognome), Chief Engineer · CR 1 (200 XP)",
         ac="15 (armored casing)", hp="33 (6d6 + 12)", speed="25 ft.",
         abilities=["10 (+0)", "14 (+2)", "14 (+2)", "16 (+3)", "12 (+1)", "10 (+0)"],
         props=["Skills Arcana +5, Investigation +5, Perception +3; tinker's tools +7",
                "Damage Immunities poison",
                "Condition Immunities charmed, exhaustion, paralyzed, poisoned",
                "Senses darkvision 60 ft., passive Perception 13",
                "Languages Common, Gnomish",
                "Challenge 1 (200 XP)"],
         traits=[("Construct Nature.", "Doesn't eat, drink, breathe, or sleep, and does not count against the ship's air envelope."),
                 ("Built for Something Larger.", "Advantage on all checks made to repair or diagnose a ship.")],
         actions=[("Wrench.", "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage."),
                  ("Field Repair (Recharges after a Short Rest).", "Restores 2d10 hit points to the ship, or fully repairs one disabled ship weapon.")],
         reactions=[("Reactive Repair.", "When the ship takes damage exceeding its damage threshold, reduces that damage by 10.")]),

    dict(id="brass", name='Brassica "Brass" Thorngage', subtitle="Small ooze (plasmoid), Medic / Cook · CR 1 (200 XP)",
         ac="14 (leather, fitted oddly)", hp="32 (7d6 + 7)", speed="25 ft.",
         abilities=["8 (−1)", "18 (+4)", "12 (+1)", "14 (+2)", "12 (+1)", "16 (+3)"],
         props=["Skills Deception +5, Insight +3, Persuasion +5, Sleight of Hand +6; thieves' tools +6",
                "Damage Resistances poison",
                "Condition Immunities poisoned",
                "Senses passive Perception 11",
                "Languages Common, Halfling, Thieves' Cant",
                "Challenge 1 (200 XP)"],
         traits=[("Amorphous.", "Can move through a space as narrow as 1 inch wide without squeezing."),
                 ("Spongy.", "Advantage on saves against poison, and resistance to poison damage."),
                 ("No License, All Instinct.", "Expertise on Medicine checks made to diagnose a creature.")],
         actions=[("Dagger.", "Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 6 (1d4 + 4) piercing damage."),
                  ("Sneak Attack (1/Turn).", "+7 (2d6) damage on an attack with advantage, or when an ally is adjacent to the target."),
                  ("Field Patch (3/Day).", "One creature within 5 ft. regains 2d8 + 2 hit points, or a dying creature becomes stable.")]),

    dict(id="finny", name='Finnick "Finny" Groles', subtitle="Small humanoid (halfling), Rigger / Deckhand · CR 1/2 (100 XP)",
         ac="13", hp="27 (5d8 + 5)", speed="25 ft., climb 20 ft.",
         abilities=["12 (+1)", "16 (+3)", "12 (+1)", "10 (+0)", "12 (+1)", "16 (+3)"],
         props=["Skills Acrobatics +5, Athletics +3, Insight +3, Perception +3, Persuasion +5",
                "Senses passive Perception 13",
                "Languages Common, Halfling, and gossip in four more",
                "Challenge 1/2 (100 XP)"],
         traits=[("Lucky.", "When Finny rolls a 1 on the d20 for an attack roll, ability check, or saving throw, he can reroll and must use the new roll."),
                 ("Brave.", "Advantage on saving throws against being frightened."),
                 ("Sure Hands Aloft.", "Advantage on checks made to rig sails, secure cargo, or crew a ship weapon in a hurry.")],
         actions=[("Boarding Knife.", "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 3) piercing damage.")],
         reactions=[('"HEY!" (Recharges after a Short Rest).', "When an ally within 30 ft. is attacked, the attacker has disadvantage on the roll.")]),

    dict(id="oz", name='Ozgood "Oz" Hammerfall', subtitle="Medium humanoid (giff), Ship's Security · CR 3 (700 XP)",
         ac="16 (breastplate)", hp="82 (11d10 + 22)", speed="30 ft.",
         abilities=["18 (+4)", "12 (+1)", "15 (+2)", "10 (+0)", "12 (+1)", "14 (+2)"],
         props=["Skills Athletics +6, Persuasion +4",
                "Senses passive Perception 11",
                "Languages Common, Giff",
                "Challenge 3 (700 XP)"],
         traits=[("Astral Spark.", "Once per turn, when Oz hits with a weapon attack, he deals an extra 4 (1d8) force damage."),
                 ("Impeccable.", "Advantage on Charisma checks made to be polite to someone who does not expect it.")],
         actions=[("Multiattack.", "Oz makes two attacks."),
                  ("Great Gun.", "Ranged Weapon Attack: +5 to hit, range 100/400 ft., one target. Hit: 12 (2d10 + 1) piercing damage. Must be reloaded (one action) after two shots."),
                  ("Headbutt.", "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage, and the target must succeed on a DC 14 Strength saving throw or be knocked prone.")],
         reactions=[("After You.", "When an ally within 5 ft. is hit by an attack, Oz swaps places with them and takes the damage instead.")]),

    dict(id="flurry", name="Flurry (Rhee)", subtitle="Medium dragon (silver wyrmling), Ship's Dragon · CR 2 (450 XP)",
         ac="17 (natural armor)", hp="45 (6d8 + 18)", speed="30 ft., fly 60 ft.",
         abilities=["18 (+4)", "10 (+0)", "17 (+3)", "12 (+1)", "11 (+0)", "15 (+2)"],
         props=["Saving Throws Dex +2, Con +5, Wis +2, Cha +4",
                "Skills Perception +4, Stealth +2",
                "Damage Immunities cold",
                "Senses blindsight 10 ft., darkvision 60 ft., passive Perception 14",
                "Languages Draconic, understands Common",
                "Challenge 2 (450 XP)"],
         traits=[("Two Years Old.", "Flurry is a puppy with a breath weapon."),
                 ("Lunar Blood (latent).", "An uncanny sensitivity to the astral. No combat effect. See npcs/Flurry.md."),
                 ("Devoted.", "Flurry will not fight unless Aerion is below half his hit points, she is cornered with no escape, or someone she has decided is hers is about to die.")],
         actions=[("Bite.", "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage."),
                  ("Breath Weapon (Recharge 6).", "Flurry uses one option below."),
                  ("Cold Breath.", "15-ft. cone, each creature makes a DC 13 Constitution save, taking 18 (4d8) cold damage on a failure, half as much on a success."),
                  ("Paralyzing Breath.", "15-ft. cone, DC 13 Constitution save or paralyzed for 1 minute, repeating the save at the end of each of its turns.")]),
]


def main():
    import os
    out = os.path.join(os.path.dirname(__file__), "..", "Crew-Stat-Blocks.pdf")
    c = canvas.Canvas(out, pagesize=letter)
    c.setTitle("Night Fury Crew Stat Blocks")
    for data in CREW:
        draw_card(c, data)
    c.save()
    print("done")


if __name__ == "__main__":
    main()
