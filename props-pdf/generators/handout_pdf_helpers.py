#!/usr/bin/env python3
"""Shared reportlab page-building helpers for in-world document PDFs
(letters, logs, programs, posters). Not for the fillable stat-card
layout in make_crew_pdf.py / make_ship_pdf.py, those are a different
design language with their own header/field helpers.

Usage:
    from handout_pdf_helpers import Page, THEMES

    page = Page("/path/to/out.pdf", THEMES["parchment"])
    y = page.header("Cook's Rationing Note")
    y = page.para(y, "Some body text that wraps automatically...")
    page.footer("A closing line, small and centered.")
    page.show_page()
    ...
    page.save()

Two built-in themes:
    "parchment" - aged single-border document look (letters, logs, in-world
                  notes). Used for the derelict's recovered-document handouts.
    "festive"   - double gold border, accent rule, used for printed programs
                  and posters (the Dog Show program).
Add a theme by extending THEMES with the same five keys; nothing else
in Page needs to change.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

THEMES = {
    "parchment": {
        "paper": HexColor("#e8dcc0"),
        "ink": HexColor("#2e2418"),
        "faint": HexColor("#8a7a5c"),
        "accent": HexColor("#8a7a5c"),
        "border": "single",
    },
    "festive": {
        "paper": HexColor("#fbf3dd"),
        "ink": HexColor("#2a2210"),
        "faint": HexColor("#a8761e"),
        "accent": HexColor("#7a2f3a"),
        "border": "double",
    },
}


def wrap(text, font, size, max_width):
    """Word-wrap text to a pixel width for the given font/size. Returns a list of lines.
    Call this with the *canvas's own* stringWidth measurement (imported here), not a guess."""
    words = text.split(" ")
    lines, cur = [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


class Page:
    def __init__(self, out_path, theme):
        self.out_path = out_path
        self.theme = theme
        self.c = canvas.Canvas(out_path, pagesize=letter)
        self.w, self.h = letter

    def bg(self):
        c, w, h, t = self.c, self.w, self.h, self.theme
        c.setFillColor(t["paper"])
        c.rect(0, 0, w, h, fill=1, stroke=0)
        if t["border"] == "double":
            c.setStrokeColor(t["faint"])
            c.setLineWidth(2.5)
            c.rect(0.4 * inch, 0.4 * inch, w - 0.8 * inch, h - 0.8 * inch, fill=0, stroke=1)
            c.setLineWidth(0.75)
            c.rect(0.5 * inch, 0.5 * inch, w - 1.0 * inch, h - 1.0 * inch, fill=0, stroke=1)
        else:
            c.setStrokeColor(t["faint"])
            c.setLineWidth(1)
            c.rect(0.55 * inch, 0.55 * inch, w - 1.1 * inch, h - 1.1 * inch, fill=0, stroke=1)

    def header(self, title, pagenote=None):
        """Draws the background, the title, and an optional italic note under it.
        Returns the y-coordinate to start the body text from."""
        self.bg()
        c, w, h, t = self.c, self.w, self.h, self.theme
        y = h - 1.0 * inch
        c.setFillColor(t["accent"])
        c.setFont("Helvetica-Bold", 15)
        c.drawCentredString(w / 2, y, title)
        y -= 0.12 * inch
        c.setStrokeColor(t["faint"])
        c.line(1.3 * inch, y, w - 1.3 * inch, y)
        y -= 0.3 * inch
        if pagenote:
            c.setFont("Helvetica-Oblique", 8.5)
            c.setFillColor(t["faint"])
            c.drawCentredString(w / 2, y, pagenote)
            y -= 0.22 * inch
        return y

    def note_header(self, title, header_note=None, start_y=None):
        """Left-aligned title with a rule under it, for a short single-page
        in-world note or log (as opposed to header()'s centered style for a
        formal multi-page program). Returns the y to start the body from."""
        self.bg()
        c, w, h, t = self.c, self.w, self.h, self.theme
        c.setFillColor(t["ink"])
        c.setFont("Helvetica-Bold", 15)
        c.drawString(0.85 * inch, h - 1.05 * inch, title)
        c.setLineWidth(0.6)
        c.setStrokeColor(t["faint"])
        c.line(0.85 * inch, h - 1.15 * inch, w - 0.85 * inch, h - 1.15 * inch)
        y = start_y if start_y else h - 1.5 * inch
        if header_note:
            c.setFont("Helvetica-Oblique", 9)
            c.setFillColor(t["faint"])
            c.drawString(0.85 * inch, y, header_note)
            y -= 0.3 * inch
        return y

    def note_para(self, y, lines, font="Helvetica", size=12, leading=17):
        """Body text for note_header's style: a list of paragraphs (plain
        strings), "" between them for a blank line, left margin 0.85in.
        Returns the next y."""
        c, w, t = self.c, self.w, self.theme
        c.setFillColor(t["ink"])
        c.setFont(font, size)
        max_width = w - 1.7 * inch
        for para_text in lines:
            if para_text == "":
                y -= leading * 0.6
                continue
            for line in wrap(para_text, font, size, max_width):
                c.drawString(0.85 * inch, y, line)
                y -= leading
            y -= leading * 0.3
        return y

    def section(self, y, title):
        """A left-aligned sub-heading with a rule under it. Returns the next y."""
        c, w, t = self.c, self.w, self.theme
        c.setFillColor(t["accent"])
        c.setFont("Helvetica-Bold", 13)
        c.drawString(1 * inch, y, title)
        y -= 0.1 * inch
        c.setStrokeColor(t["faint"])
        c.line(1 * inch, y, w - 1 * inch, y)
        return y - 0.24 * inch

    def para(self, y, text, font="Helvetica", size=10, indent=1.1, width=None, leading=0.17):
        """Word-wrapped body text. Returns the next y."""
        c, w, t = self.c, self.w, self.theme
        if width is None:
            width = w - (indent + 1.0) * inch
        c.setFillColor(t["ink"])
        c.setFont(font, size)
        for line in wrap(text, font, size, width):
            c.drawString(indent * inch, y, line)
            y -= leading * inch
        return y

    def footer(self, text):
        """A small italic line centered near the bottom of the page."""
        c, w, h, t = self.c, self.w, self.h, self.theme
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColor(t["faint"])
        c.drawCentredString(w / 2, 0.7 * inch, text)

    def show_page(self):
        self.c.showPage()

    def save(self):
        self.c.save()
        print("wrote", self.out_path)
