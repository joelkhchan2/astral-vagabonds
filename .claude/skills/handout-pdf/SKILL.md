---
name: handout-pdf
description: Build an in-world document PDF (a recovered letter, a log page, a printed program or poster) for the campaign, using the shared reportlab helper rather than writing page-drawing code from scratch each time. Use whenever a new prop handout is needed as a real printable/shareable PDF. Companion to `handout-prop-split` (what belongs in it) and `props-pdf/generators/` (where existing generator scripts live).
---

# Building a handout PDF

`props-pdf/generators/handout_pdf_helpers.py` is the shared page-building module, built from two scripts that each independently reinvented the same wrap/header/section/para/footer functions (one for the derelict's recovered documents, one for the Dog Show program) and hit the same em-dash bug twice doing it. Use the shared module instead of writing canvas calls from scratch.

`props-pdf/generators/make_derelict_handouts.py` (short single-page in-world notes, "parchment" theme) and `props-pdf/generators/make_dogshow_program.py` (a multi-page formal program, "festive" theme) are the two worked examples. `props-pdf/generators/make_crew_pdf.py` and `make_ship_pdf.py` are a different design language (fillable D&D-style stat cards) and don't use this helper, they're their own thing.

## Setup

`pip install reportlab` if it's not already available (check with `python3 -c "import reportlab"` first, it may already be installed). This is not preinstalled by default.

## Using the shared helper

```python
import sys, os
sys.path.insert(0, "props-pdf/generators")  # or wherever the script lives relative to it
from handout_pdf_helpers import Page, THEMES

page = Page("/path/to/out.pdf", THEMES["parchment"])  # or THEMES["festive"]
y = page.header("A Formal Multi-Page Title")           # centered, for programs/posters
# or: y = page.note_header("A Short Note's Title", header_note="Found: wherever.")  # left-aligned, for a single-page note/log
y = page.section(y, "A Sub-Heading")                    # left-aligned rule under it
y = page.para(y, "Body text that wraps automatically to the page width.")
page.footer("A small italic closing line, centered.")
page.show_page()                                         # next page
page.save()
```

Two built-in themes: `parchment` (aged single-border, for recovered documents and in-world notes) and `festive` (double gold border with an accent color, for formal printed programs). Add a new theme by extending the `THEMES` dict with the same keys (`paper`, `ink`, `faint`, `accent`, `border`), nothing else needs to change.

For raw canvas access beyond what the helpers cover (custom tables, mixed-column layouts, as in the past-champions table in `make_dogshow_program.py`), reach for `page.c` (the underlying reportlab canvas) and `page.theme` directly, the helper doesn't need to cover every layout, just the common document shape.

## Where output goes

- **Session-specific props** (a recovered log, a job posting, a prop tied to one session or arc): `sessions/handouts/`.
- **Standing reference cards** (crew stat cards, ship cards, anything reused across sessions): `props-pdf/`.
Match the existing convention in whichever folder the new prop belongs to.

## The known pitfall: literal em-dash escapes

Typing the Unicode escape for the em-dash character (U+2014) as a literal escape sequence inside a Python string, meaning to produce that character in the PDF, actually renders as a real em-dash character when the Write tool writes the script file itself, which then violates the campaign's no-em-dash house rule (`CLAUDE.md`, `dnd-writing` skill) the moment the script's own source is read back or copied elsewhere. This bit twice in the same session before being caught. Use a plain double hyphen (`--`), a colon, or parentheses instead, exactly the same substitutions the house rule already calls for in prose. After generating any handout with cut-off or interrupted text, grep the source script itself for the em-dash character directly, not just the rendered output.

## Verification

Render pages to PNG and actually look at them before calling a handout done, text wrapping and layout errors are easy to miss by reading the script alone:

```bash
pip install reportlab   # if needed
python3 your_script.py
pdftoppm -png -r 100 "path/to/output.pdf" "$SCRATCHPAD_DIR/preview"
```

Then `Read` the resulting PNG(s). Do this for every page on a first build, and at minimum the pages that changed on a revision.
