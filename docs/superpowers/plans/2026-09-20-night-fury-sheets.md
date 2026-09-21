# Night Fury Google Sheets Ship Sheet Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a live-tracking Google Sheets ship sheet for the *Night Fury*, replacing the empty Apps Script bound to the existing "Night Fury" Google Sheet (a copy of Orena's PC character template), and push it via `clasp`.

**Architecture:** A local `clasp` project (`sheets/night-fury/`) with static reference data (`ShipData.js`, generated `BastionFacilities.js`) separated from pure calculation logic (`Logic.js`, unit-tested with Node's built-in test runner) and from Google Apps Script I/O (`Setup.js` for one-time tab construction, `Code.js` for the play-time menu). `Setup.js`'s `rebuildAllTabs()` builds the 4 ship tabs from the data files and deletes the PC-only tabs; `Code.js` wires a custom `⚓ Night Fury` menu on top of named ranges those tabs define.

**Tech Stack:** Google Apps Script (V8 runtime) via `clasp` (already installed and authenticated — confirmed in-session), Node.js v24 (`node:test` / `node:assert/strict`, no npm dependencies), Python 3.10 (`py`, one-time data-extraction script only, not part of the Apps Script bundle).

## Global Constraints

- Spec of record: `docs/superpowers/specs/2026-09-20-night-fury-sheets-sheet-design.md` — every task below implements a specific section of it; re-read it if a task's rationale is unclear.
- Local project root: `sheets/night-fury/` (new top-level repo folder, alongside `props-pdf/` as this project's other generated-artifact folder).
- Bound script id (already exists, currently empty boilerplate, confirmed via `clasp clone` earlier this session): `1p-a0dOERHJe3R2Sxia3el1Up4UcpTAH4SvxLa7qMB47Aw_q_66qCfGZa`.
- Bound spreadsheet id: `1K4f4KNXDitZT8jcGyWIentumkTmfWrwZp6j92WyLEVs` (Google Sheet titled "Night Fury").
- **No ammo tracking anywhere** — confirmed via session 0/1 transcripts, the table explicitly doesn't track ballista shots.
- **No live Bastion Facilities tracking** — that tab is static reference only (all 29 DMG'24 facilities), not tied to the live-tracking rationale.
- Don't touch `ships/night-fury-stat-card.html` or `props-pdf/generators/make_ship_pdf.py` — this is a parallel deliverable.
- Don't invent ship mechanics beyond `ships/Night Fury.md` and `rules/Rules & Systems.md` §8 — implement existing canon only.
- Damage threshold 20, max HP 250, repair rate 20 gp/HP, Tack's Reactive Repair (-10 to damage over threshold) — all verified verbatim against `ships/Night Fury.md` and `rules/Stat Blocks.md` earlier this session; don't re-derive, just use these numbers.
- Commit after every task (this repo's CLAUDE.md: "Commit and push after every substantive change"); push to `origin/master` at the end of Task 8.

---

## File Structure

```
sheets/night-fury/
├── .clasp.json              # points clasp at the bound script (Task 1)
├── .claspignore              # ignore-then-allowlist so only GAS files push (Task 1)
├── appsscript.json           # GAS manifest, matches what's already live (Task 1)
├── Code.js                   # play-time menu + 5 actions (Task 1 stub, Task 7 final)
├── Logic.js                  # pure calculation functions, Node-tested (Task 2)
├── ShipData.js                # static ship/crew/weapon/bastion-chosen data (Task 4)
├── BastionFacilities.js       # GENERATED: full 29-facility catalog (Task 3)
├── Setup.js                   # one-time tab-construction functions (Tasks 5-6)
├── scripts/
│   └── extract-bastion-facilities.py   # regenerates BastionFacilities.js (Task 3)
└── test/
    ├── logic.test.js          # Task 2
    ├── shipdata.test.js       # Task 4
    └── bastionfacilities.test.js  # Task 3
```

`scripts/` and `test/` are excluded from `clasp push` by `.claspignore` — only the 6 GAS source files reach the Apps Script project.

---

### Task 1: Clasp project scaffold

**Files:**
- Create: `sheets/night-fury/.clasp.json`
- Create: `sheets/night-fury/.claspignore`
- Create: `sheets/night-fury/appsscript.json`
- Create: `sheets/night-fury/Code.js` (stub — replaced in Task 7)

**Interfaces:**
- Produces: a `clasp`-pushable project at `sheets/night-fury/` targeting the live bound script.

- [ ] **Step 1: Create the project directory and clasp config**

```bash
mkdir -p sheets/night-fury
```

Write `sheets/night-fury/.clasp.json`:

```json
{
  "scriptId": "1p-a0dOERHJe3R2Sxia3el1Up4UcpTAH4SvxLa7qMB47Aw_q_66qCfGZa",
  "rootDir": "."
}
```

- [ ] **Step 2: Write `.claspignore`**

```
**/**
!appsscript.json
!Code.js
!Logic.js
!Setup.js
!ShipData.js
!BastionFacilities.js
```

This ignores everything, then un-ignores exactly the 6 files that belong in the Apps Script project — `scripts/`, `test/`, and this plan's own files never get pushed.

- [ ] **Step 3: Write `appsscript.json`**

Matches what's already live on the bound script (confirmed via `clasp clone` earlier this session):

```json
{
  "timeZone": "America/Toronto",
  "dependencies": {},
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8"
}
```

- [ ] **Step 4: Write a minimal `Code.js` stub**

```javascript
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('⚓ Night Fury')
    .addItem('(not yet built)', 'placeholder_')
    .addToUi();
}

function placeholder_() {
  SpreadsheetApp.getActiveSpreadsheet().toast('Menu not yet built — see implementation plan.');
}
```

- [ ] **Step 5: Verify clasp sees the project correctly**

Run: `cd sheets/night-fury && clasp status`
Expected: lists `appsscript.json` and `Code.js` as tracked files, nothing from `scripts/` or `test/` (those don't exist yet, so this just confirms the ignore pattern doesn't error).

- [ ] **Step 6: Push and confirm**

Run: `cd sheets/night-fury && clasp push`
Expected: `└─ appsscript.json` and `└─ Code.js` listed as pushed, no errors.

- [ ] **Step 7: Commit**

```bash
git add sheets/night-fury/.clasp.json sheets/night-fury/.claspignore sheets/night-fury/appsscript.json sheets/night-fury/Code.js
git commit -m "Scaffold the Night Fury clasp project"
```

---

### Task 2: Logic.js pure functions (TDD)

**Files:**
- Create: `sheets/night-fury/Logic.js`
- Test: `sheets/night-fury/test/logic.test.js`

**Interfaces:**
- Produces: `parseAmountInput(text)`, `clampHp(current, delta, maxHp)`, `computeDamageResult(rawAmount, tackMitigating, threshold)`, `computeRepairBill(currentBill, damageApplied, gpPerPoint)` — all pure, no `SpreadsheetApp` calls. Consumed by `Code.js` in Task 7.

- [ ] **Step 1: Write the failing tests**

Create `sheets/night-fury/test/logic.test.js`:

```javascript
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { parseAmountInput, clampHp, computeDamageResult, computeRepairBill } = require('../Logic.js');

test('parseAmountInput accepts a positive integer string', () => {
  assert.deepEqual(parseAmountInput('23'), { valid: true, value: 23 });
});

test('parseAmountInput rejects blank input', () => {
  assert.deepEqual(parseAmountInput(''), { valid: false, value: null });
});

test('parseAmountInput rejects non-numeric input', () => {
  assert.deepEqual(parseAmountInput('abc'), { valid: false, value: null });
});

test('parseAmountInput rejects null (Cancel)', () => {
  assert.deepEqual(parseAmountInput(null), { valid: false, value: null });
});

test('clampHp floors at 0', () => {
  assert.equal(clampHp(10, -50, 250), 0);
});

test('clampHp caps at maxHp', () => {
  assert.equal(clampHp(240, 50, 250), 250);
});

test('clampHp applies a normal delta unclamped', () => {
  assert.equal(clampHp(200, -30, 250), 170);
});

test('computeDamageResult no-ops a hit under the damage threshold', () => {
  const result = computeDamageResult(15, false, 20);
  assert.equal(result.applied, false);
  assert.equal(result.damage, 0);
});

test('computeDamageResult applies a hit at or over the threshold', () => {
  const result = computeDamageResult(23, false, 20);
  assert.equal(result.applied, true);
  assert.equal(result.damage, 23);
});

test('computeDamageResult reduces damage by 10 when Tack is mitigating', () => {
  const result = computeDamageResult(23, true, 20);
  assert.equal(result.applied, true);
  assert.equal(result.damage, 13);
});

test('computeDamageResult floors Tack-mitigated damage at 0', () => {
  const result = computeDamageResult(20, true, 20);
  assert.equal(result.applied, true);
  assert.equal(result.damage, 10);
});

test('computeDamageResult rejects negative input', () => {
  const result = computeDamageResult(-5, false, 20);
  assert.equal(result.valid, false);
});

test('computeRepairBill accumulates at 20gp per point by default', () => {
  assert.equal(computeRepairBill(0, 23, 20), 460);
});

test('computeRepairBill adds onto an existing bill', () => {
  assert.equal(computeRepairBill(100, 5, 20), 200);
});
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `node --test sheets/night-fury/test/logic.test.js`
Expected: FAIL — `Cannot find module '../Logic.js'` (file doesn't exist yet).

- [ ] **Step 3: Write `Logic.js`**

```javascript
// Logic.js — pure calculation functions. No SpreadsheetApp/Ui calls here;
// those live in Code.js. Node-testable via the module.exports guard below.

function parseAmountInput(text) {
  if (text === null || text === undefined) {
    return { valid: false, value: null };
  }
  var trimmed = String(text).trim();
  if (trimmed === '') {
    return { valid: false, value: null };
  }
  var n = Number(trimmed);
  if (isNaN(n)) {
    return { valid: false, value: null };
  }
  return { valid: true, value: n };
}

function clampHp(current, delta, maxHp) {
  var next = current + delta;
  if (next < 0) next = 0;
  if (typeof maxHp === 'number' && next > maxHp) next = maxHp;
  return next;
}

function computeDamageResult(rawAmount, tackMitigating, threshold) {
  threshold = (threshold === undefined) ? 20 : threshold;
  if (typeof rawAmount !== 'number' || isNaN(rawAmount) || rawAmount < 0) {
    return { valid: false, applied: false, damage: 0, reason: 'Enter a non-negative number.' };
  }
  if (rawAmount < threshold) {
    return { valid: true, applied: false, damage: 0, reason: 'Hit below damage threshold (' + threshold + ') — no effect.' };
  }
  var damage = rawAmount;
  if (tackMitigating) {
    damage = Math.max(0, damage - 10);
  }
  return { valid: true, applied: true, damage: damage, reason: '' };
}

function computeRepairBill(currentBill, damageApplied, gpPerPoint) {
  gpPerPoint = (gpPerPoint === undefined) ? 20 : gpPerPoint;
  return currentBill + damageApplied * gpPerPoint;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { parseAmountInput, clampHp, computeDamageResult, computeRepairBill };
}
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `node --test sheets/night-fury/test/logic.test.js`
Expected: PASS — 14 passing, 0 failing.

- [ ] **Step 5: Commit**

```bash
git add sheets/night-fury/Logic.js sheets/night-fury/test/logic.test.js
git commit -m "Add Logic.js pure calculation functions, Node-tested"
```

---

### Task 3: Bastion Facilities data extraction

**Files:**
- Create: `sheets/night-fury/scripts/extract-bastion-facilities.py`
- Create (generated by the script): `sheets/night-fury/BastionFacilities.js`
- Test: `sheets/night-fury/test/bastionfacilities.test.js`

**Interfaces:**
- Produces: `BASTION_FACILITIES` — an array of 29 objects `{ name, level, prereq, space, hirelings, order, description }`, sorted by `(level, name)`. Consumed by `Setup.js` in Task 6.

- [ ] **Step 1: Write the extraction script**

This regex-based approach was verified in-session against the real source file (`C:\Users\Joelk\Downloads\Bastions - D&D 5e (2024).html`): 29 facilities extracted cleanly, including embedded rules tables (Garden Types, Menagerie Creatures, Sample Guilds, etc.) that a paragraph-only extraction would silently drop.

Create `sheets/night-fury/scripts/extract-bastion-facilities.py`:

```python
#!/usr/bin/env python3
"""
Extract the 29 core DMG'24 Bastion special facility entries from a
5e-tools-style HTML export and emit them as a GAS-ready JS source file
(sheets/night-fury/BastionFacilities.js).

Source: a saved copy of the D&D 5e (2024) DMG Chapter 8 "Special Facility
Descriptions" section (e.g. from dnd2024.wikidot.com/bastions).

Re-run this whenever the source file changes; it is NOT run automatically
by the Sheet.

Usage:
    py scripts/extract-bastion-facilities.py "<path to source HTML>"
"""
import re
import html
import json
import sys
import pathlib


def clean(s):
    s = re.sub(r'<a href="[^"]*">(.*?)</a>', r'\1', s, flags=re.DOTALL)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t]+', ' ', s)
    return s.strip()


def table_to_text(table_html):
    rows = re.findall(r'<tr>(.*?)</tr>', table_html, re.DOTALL)
    lines = []
    for row in rows:
        cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
        lines.append(' | '.join(clean(c) for c in cells))
    return '\n'.join(lines)


def extract(src_path):
    text = pathlib.Path(src_path).read_text(encoding='utf-8', errors='replace')
    start = text.index('<h3 id="toc25">')   # Arcane Study — first core special facility
    end = text.index('<h3 id="toc55">')     # Amethyst Dragon Den — first non-core bonus facility
    block = text[start:end]

    heading_re = re.compile(r'<h3 id="toc\d+"><span>(.*?)</span></h3>', re.DOTALL)
    headings = list(heading_re.finditer(block))
    block_re = re.compile(
        r'<p>(.*?)</p>'
        r'|<strong>([^<]*?)</strong><br\s*/?>'
        r'|<table[^>]*>(.*?)</table>',
        re.DOTALL,
    )

    facilities = []
    for i, m in enumerate(headings):
        name = clean(re.sub(r'<a name="[^"]*"></a>', '', m.group(1))).strip()
        body_start = m.end()
        body_end = headings[i + 1].start() if i + 1 < len(headings) else len(block)
        body_html = block[body_start:body_end]

        level_m = re.search(r'Level (\d+) Bastion Facility', body_html)
        prereq_m = re.search(r'<strong>Prerequisite:</strong>\s*(.*?)<br>', body_html, re.DOTALL)
        space_m = re.search(r'<strong>Space:</strong>\s*(.*?)<br>', body_html, re.DOTALL)
        hire_m = re.search(r'(?:<strong>Hirelings:</strong>|Hirelings:)\s*(.*?)<br>', body_html, re.DOTALL)
        order_m = re.search(r'(?:<strong>Order:</strong>|Order:)\s*(.*?)</p>', body_html, re.DOTALL)

        desc_parts = []
        for bm in block_re.finditer(body_html):
            if bm.group(1) is not None:
                t = clean(bm.group(1))
                if not t or t.startswith('Level ') or 'Prerequisite:' in t:
                    continue
                desc_parts.append(t)
            elif bm.group(2) is not None:
                desc_parts.append(clean(bm.group(2)))
            else:
                desc_parts.append(table_to_text(bm.group(3)))

        facilities.append({
            'name': name,
            'level': int(level_m.group(1)) if level_m else None,
            'prereq': clean(prereq_m.group(1)) if prereq_m else None,
            'space': clean(space_m.group(1)) if space_m else None,
            'hirelings': clean(hire_m.group(1)) if hire_m else None,
            'order': clean(order_m.group(1)) if order_m else None,
            'description': '\n\n'.join(p for p in desc_parts if p),
        })

    return facilities


def main():
    if len(sys.argv) != 2:
        print("Usage: extract-bastion-facilities.py <path-to-source-html>", file=sys.stderr)
        sys.exit(1)

    facilities = extract(sys.argv[1])

    assert len(facilities) == 29, f"expected 29 facilities, got {len(facilities)}"
    for f in facilities:
        assert f['level'] in (5, 9, 13, 17), f"{f['name']}: bad level {f['level']}"
        assert f['prereq'] is not None, f"{f['name']}: missing prereq"
        assert f['space'] is not None, f"{f['name']}: missing space"
        assert f['hirelings'] is not None, f"{f['name']}: missing hirelings"
        assert f['order'] is not None, f"{f['name']}: missing order"
        assert f['description'], f"{f['name']}: empty description"
        assert 'loading' not in f['description'].lower(), f"{f['name']}: still has a Loading placeholder"

    facilities.sort(key=lambda f: (f['level'], f['name']))

    out_path = pathlib.Path(__file__).resolve().parent.parent / 'BastionFacilities.js'
    js = (
        "// GENERATED FILE — do not hand-edit. Regenerate with:\n"
        "//   py scripts/extract-bastion-facilities.py \"<path to source HTML>\"\n"
        "var BASTION_FACILITIES = " + json.dumps(facilities, indent=2, ensure_ascii=False) + ";\n"
        "\n"
        "if (typeof module !== 'undefined' && module.exports) {\n"
        "  module.exports = { BASTION_FACILITIES };\n"
        "}\n"
    )
    out_path.write_text(js, encoding='utf-8')
    print(f"Wrote {len(facilities)} facilities to {out_path}")


if __name__ == '__main__':
    main()
```

- [ ] **Step 2: Run it against the real source file**

Run: `py sheets/night-fury/scripts/extract-bastion-facilities.py "C:\Users\Joelk\Downloads\Bastions - D&D 5e (2024).html"`
Expected: `Wrote 29 facilities to ...BastionFacilities.js`, no assertion errors.

- [ ] **Step 3: Write the Node smoke test**

Create `sheets/night-fury/test/bastionfacilities.test.js`:

```javascript
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { BASTION_FACILITIES } = require('../BastionFacilities.js');

test('BastionFacilities has exactly 29 core DMG facilities', () => {
  assert.equal(BASTION_FACILITIES.length, 29);
});

test('every facility has all required fields and no Loading placeholder', () => {
  for (const f of BASTION_FACILITIES) {
    assert.ok([5, 9, 13, 17].includes(f.level), `${f.name}: bad level ${f.level}`);
    assert.ok(f.prereq !== null && f.prereq !== undefined, `${f.name}: missing prereq`);
    assert.ok(f.space, `${f.name}: missing space`);
    assert.ok(f.hirelings, `${f.name}: missing hirelings`);
    assert.ok(f.order, `${f.name}: missing order`);
    assert.ok(f.description && f.description.length > 0, `${f.name}: empty description`);
    assert.ok(!f.description.toLowerCase().includes('loading'), `${f.name}: has a Loading placeholder`);
  }
});

test('Arcane Study, Library, and Storehouse are present (the ship\'s chosen facilities)', () => {
  const names = BASTION_FACILITIES.map(f => f.name);
  assert.ok(names.includes('Arcane Study'));
  assert.ok(names.includes('Library'));
  assert.ok(names.includes('Storehouse'));
});
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `node --test sheets/night-fury/test/bastionfacilities.test.js`
Expected: PASS — 3 passing, 0 failing.

- [ ] **Step 5: Commit**

```bash
git add sheets/night-fury/scripts/extract-bastion-facilities.py sheets/night-fury/BastionFacilities.js sheets/night-fury/test/bastionfacilities.test.js
git commit -m "Extract the 29-facility DMG'24 Bastion catalog into BastionFacilities.js"
```

---

### Task 4: Ship/crew static data

**Files:**
- Create: `sheets/night-fury/ShipData.js`
- Test: `sheets/night-fury/test/shipdata.test.js`

**Interfaces:**
- Consumes: nothing (hand-authored from `ships/Night Fury.md`, `rules/Stat Blocks.md`, `npcs/Tack.md`, all verified verbatim earlier this session).
- Produces: `SHIP` (object), `WEAPON_STATIONS` (array of 3), `SYSTEMS` (array of 7), `CREW_ROSTER` (array of 7), `BASTION_CHOSEN` (array of 4). Consumed by `Setup.js` (Tasks 5-6) and `Code.js` (Task 7).

- [ ] **Step 1: Write the failing tests**

Create `sheets/night-fury/test/shipdata.test.js`:

```javascript
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { SHIP, WEAPON_STATIONS, CREW_ROSTER, BASTION_CHOSEN } = require('../ShipData.js');

test('CREW_ROSTER has all 7 crew running the ship', () => {
  assert.equal(CREW_ROSTER.length, 7);
});

test('WEAPON_STATIONS has Gertrude, Susan, and Kevin, no ammo field', () => {
  assert.equal(WEAPON_STATIONS.length, 3);
  const names = WEAPON_STATIONS.map(w => w.name);
  assert.deepEqual(names, ['Gertrude', 'Susan', 'Kevin']);
  for (const w of WEAPON_STATIONS) {
    assert.equal('ammo' in w, false);
  }
});

test('SHIP stats match Night Fury.md', () => {
  assert.equal(SHIP.ac, 19);
  assert.equal(SHIP.damageThreshold, 20);
  assert.equal(SHIP.maxHp, 250);
  assert.equal(SHIP.gpPerRepairPoint, 20);
});

test('BASTION_CHOSEN lists all 4 chosen/open facility slots', () => {
  assert.equal(BASTION_CHOSEN.length, 4);
});
```

- [ ] **Step 2: Run to verify it fails**

Run: `node --test sheets/night-fury/test/shipdata.test.js`
Expected: FAIL — `Cannot find module '../ShipData.js'`.

- [ ] **Step 3: Write `ShipData.js`**

```javascript
// ShipData.js — static ship/crew reference data. Source of truth stays
// `ships/Night Fury.md` and `rules/Stat Blocks.md`; this is a snapshot for
// the Sheet's static cells, re-authored by hand if those docs change.

var SHIP = {
  name: 'Night Fury',
  className: 'Sturdy Trader (Danforth Certified Hulls)',
  ac: 19,
  damageThreshold: 20,
  speed: '45 ft tactical (Trader 55, -10 for Sturdy), +5 ft Trim Rig',
  cargoTons: 20,
  crewCapacity: '11 (running with 7)',
  airDays: 120,
  maxHp: 250,
  gpPerRepairPoint: 20,
  startingGp: 50000,
  afterOutfitGp: 14350,
  operatingCost: '500 gp/month for up to 6 crew, +100 gp/month per additional crew member',
};

var WEAPON_STATIONS = [
  { name: 'Gertrude', position: 'Port ballista', notes: 'Sureshot Rotator + Ready Magazine; 50 standard shots bought (not tracked live, see design spec)' },
  { name: 'Susan', position: 'Starboard ballista', notes: 'Sureshot Rotator + Ready Magazine; 50 standard shots bought (not tracked live, see design spec)' },
  { name: 'Kevin', position: 'Blunt ram', notes: 'Self-damaging if the dealt damage exceeds the ship\'s own damage threshold' },
];

var SYSTEMS = [
  { system: 'Hull', choice: 'Sturdy Trader, 20,000 gp' },
  { system: 'Helm', choice: 'Coilworks Mk IV (standard), 8,000 gp' },
  { system: 'Armor', choice: 'Plating I (+1 AC)' },
  { system: 'Weapons', choice: '2 ballistae, blunt ram' },
  { system: 'Weapon upgrades', choice: 'Sureshot Rotator (aim = bonus action), Ready Magazine (load = bonus action)' },
  { system: 'Mobility', choice: 'Trim Rig (+5 ft, holds attitude unhelmed)' },
  { system: 'Life support', choice: 'None (base 120-day air)' },
];

var CREW_ROSTER = [
  { name: 'Orena', speciesClass: 'Water Genasi Bard/Paladin', role: 'Navigator, Helmsman-in-training, Scout', maxHp: null, notes: '' },
  { name: 'Aerion', speciesClass: 'Astral Elf Samurai Fighter', role: 'Bosun, Quartermaster, Cargo Handler', maxHp: null, notes: '' },
  { name: 'Estra', speciesClass: 'Human Fighter (Battle Master)', role: 'Captain, Main Helmsman', maxHp: 58, notes: 'Pilots by default' },
  { name: 'Tack', speciesClass: 'Autognome Artificer', role: 'Chief Engineer', maxHp: 33, notes: 'Engineer by default; confirmed gunner' },
  { name: 'Finny', speciesClass: 'Halfling Rogue (Thief)', role: 'Rigger, Deckhand, backup Gunner', maxHp: 33, notes: 'Confirmed gunner' },
  { name: 'Brass', speciesClass: 'Human Cleric (Life Domain)', role: 'Medic, Cook', maxHp: 33, notes: 'Can load a ballista but not fire it solo' },
  { name: 'Oz', speciesClass: 'Giff Fighter', role: 'Ship\'s Security', maxHp: 82, notes: 'Confirmed gunner' },
];

var BASTION_CHOSEN = [
  { owner: 'Aerion', facility: 'Storehouse', order: 'Trade', status: 'the cargo hold, formalized' },
  { owner: 'Aerion', facility: '(second slot)', order: '—', status: 'not yet chosen' },
  { owner: 'Orena', facility: 'Library', order: 'Research', status: 'the chart room' },
  { owner: 'Orena', facility: 'Arcane Study', order: 'Craft', status: 'the helm room (ruled to qualify as her arcane focus)' },
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SHIP, WEAPON_STATIONS, SYSTEMS, CREW_ROSTER, BASTION_CHOSEN };
}
```

Note: `Orena` and `Aerion`'s `maxHp` are `null` — those are the players' own character-sheet numbers, not this project's to invent (see this repo's "Player agency" hard rule in `CLAUDE.md`). `Setup.js` (Task 5) must leave those cells blank for the players to fill in, not default them to 0 or any other number.

- [ ] **Step 4: Run to verify it passes**

Run: `node --test sheets/night-fury/test/shipdata.test.js`
Expected: PASS — 4 passing, 0 failing.

- [ ] **Step 5: Commit**

```bash
git add sheets/night-fury/ShipData.js sheets/night-fury/test/shipdata.test.js
git commit -m "Add ShipData.js static reference data, Node-tested"
```

---

### Task 5: Setup.js part A — Night Fury tab + Crew Aboard tab

**Files:**
- Create: `sheets/night-fury/Setup.js`

**Interfaces:**
- Consumes: `SHIP`, `WEAPON_STATIONS`, `SYSTEMS`, `BASTION_CHOSEN` (from `ShipData.js`, Task 4), `CREW_ROSTER` (from `ShipData.js`, Task 4).
- Produces: `getOrCreateSheet_(ss, name)`, `setHeaderStyle_(range)`, `setLiveStyle_(range)`, `setNamedRange_(ss, name, range)`, `setupNightFuryTab_(ss)`, `setupCrewAboardTab_(ss)`, `STATION_OPTIONS` (array), sheet-name constants `SHEET_NIGHT_FURY`, `SHEET_CREW_ABOARD`, `SHEET_BASTION_FACILITIES`, `SHEET_CARGO_MANIFEST`. Named ranges `NF_HP_CURRENT`, `NF_REPAIR_BILL`, `CREW_TABLE_BODY` — consumed by `Code.js` in Task 7.

No automated test is possible here — `SpreadsheetApp` doesn't exist outside the Apps Script runtime. Verification is manual, in Task 8, after this and Task 6 are both pushed.

- [ ] **Step 1: Write `Setup.js` (part A — shared helpers, Night Fury tab, Crew Aboard tab)**

Create `sheets/night-fury/Setup.js`:

```javascript
// Setup.js — one-time/rebuildable tab construction. Not part of the play-time
// menu; run manually from the Apps Script editor (or `clasp run`) whenever the
// sheet needs to be rebuilt from scratch. See Code.js for the play-time menu.

var SHEET_NIGHT_FURY = 'Night Fury';
var SHEET_CREW_ABOARD = 'Crew Aboard';
var SHEET_BASTION_FACILITIES = 'Bastion Facilities';
var SHEET_CARGO_MANIFEST = 'Cargo Manifest';

var STATION_OPTIONS = ['Pilot', 'Gunner', 'Engineer', 'Coordinator', 'Personal action', 'Off-duty'];

function getOrCreateSheet_(ss, name) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
  } else {
    sheet.clear();
    sheet.clearFormats();
  }
  return sheet;
}

function setHeaderStyle_(range) {
  range.setFontWeight('bold');
}

function setLiveStyle_(range) {
  range.setBackground('#dce9f8').setFontColor('#14539a').setFontWeight('bold');
}

function setNamedRange_(ss, name, range) {
  var existing = ss.getNamedRanges().filter(function (nr) { return nr.getName() === name; });
  existing.forEach(function (nr) { nr.remove(); });
  ss.setNamedRange(name, range);
}

function setupNightFuryTab_(ss) {
  var sheet = getOrCreateSheet_(ss, SHEET_NIGHT_FURY);

  sheet.getRange('A1:F1').merge()
    .setValue('Legend: blue cells are live/tracked during play. Ammo, skills, and saving throws are not tracked on this Sheet — see docs/superpowers/specs/2026-09-20-night-fury-sheets-sheet-design.md.')
    .setWrap(true);

  sheet.getRange('A3').setValue(SHIP.name).setFontWeight('bold').setFontSize(16);
  sheet.getRange('A4').setValue(SHIP.className).setFontStyle('italic');

  sheet.getRange('A6').setValue('SHIP STATS');
  setHeaderStyle_(sheet.getRange('A6'));
  sheet.getRange('A7').setValue('AC');
  sheet.getRange('B7').setValue(SHIP.ac);
  sheet.getRange('D7').setValue('Damage Threshold');
  sheet.getRange('E7').setValue(SHIP.damageThreshold);
  sheet.getRange('A8').setValue('Speed');
  sheet.getRange('B8').setValue(SHIP.speed);
  sheet.getRange('D8').setValue('Cargo');
  sheet.getRange('E8').setValue(SHIP.cargoTons + ' tons');
  sheet.getRange('A9').setValue('Crew Capacity');
  sheet.getRange('B9').setValue(SHIP.crewCapacity);
  sheet.getRange('D9').setValue('Air');
  sheet.getRange('E9').setValue(SHIP.airDays + ' days');

  sheet.getRange('A11').setValue('HP');
  setHeaderStyle_(sheet.getRange('A11'));
  sheet.getRange('A12').setValue('Max HP');
  sheet.getRange('B12').setValue(SHIP.maxHp);
  sheet.getRange('D12').setValue('Current HP');
  sheet.getRange('E12').setValue(SHIP.maxHp);
  setLiveStyle_(sheet.getRange('E12'));
  sheet.getRange('A13').setValue('Repair Bill (gp)');
  sheet.getRange('B13').setValue(0);
  setLiveStyle_(sheet.getRange('B13'));
  sheet.getRange('D13').setValue('Repair rate');
  sheet.getRange('E13').setValue(SHIP.gpPerRepairPoint + ' gp / HP');

  sheet.getRange('A15').setValue('WEAPON STATIONS');
  setHeaderStyle_(sheet.getRange('A15'));
  sheet.getRange('A16:C16').setValues([['Name', 'Position', 'Notes']]);
  setHeaderStyle_(sheet.getRange('A16:C16'));
  var weaponRows = WEAPON_STATIONS.map(function (w) { return [w.name, w.position, w.notes]; });
  sheet.getRange(17, 1, weaponRows.length, 3).setValues(weaponRows);

  var sysHeaderRow = 17 + weaponRows.length + 2;
  sheet.getRange(sysHeaderRow, 1).setValue('SYSTEMS & ADD-ONS');
  setHeaderStyle_(sheet.getRange(sysHeaderRow, 1));
  sheet.getRange(sysHeaderRow + 1, 1, 1, 2).setValues([['System', 'Choice']]);
  setHeaderStyle_(sheet.getRange(sysHeaderRow + 1, 1, 1, 2));
  var sysRows = SYSTEMS.map(function (s) { return [s.system, s.choice]; });
  sheet.getRange(sysHeaderRow + 2, 1, sysRows.length, 2).setValues(sysRows);

  var moneyHeaderRow = sysHeaderRow + 2 + sysRows.length + 2;
  sheet.getRange(moneyHeaderRow, 1).setValue('MONEY');
  setHeaderStyle_(sheet.getRange(moneyHeaderRow, 1));
  sheet.getRange(moneyHeaderRow + 1, 1).setValue('Started with (gp)');
  sheet.getRange(moneyHeaderRow + 1, 2).setValue(SHIP.startingGp);
  sheet.getRange(moneyHeaderRow + 1, 4).setValue('After outfit (gp)');
  sheet.getRange(moneyHeaderRow + 1, 5).setValue(SHIP.afterOutfitGp);
  sheet.getRange(moneyHeaderRow + 2, 1).setValue('Operating cost');
  sheet.getRange(moneyHeaderRow + 2, 2, 1, 4).merge().setValue(SHIP.operatingCost).setWrap(true);

  var personalityHeaderRow = moneyHeaderRow + 4;
  sheet.getRange(personalityHeaderRow, 1).setValue('PERSONALITY');
  setHeaderStyle_(sheet.getRange(personalityHeaderRow, 1));
  sheet.getRange(personalityHeaderRow + 1, 1, 1, 6).merge()
    .setValue('The tattered flag Tack saved from the old ship is sewn onto this one.')
    .setWrap(true);
  sheet.getRange(personalityHeaderRow + 2, 1, 1, 6).merge()
    .setValue('Named parts: ballistae Gertrude & Susan, ram Kevin, mast Deborah.')
    .setWrap(true);

  var bastionHeaderRow = personalityHeaderRow + 5;
  sheet.getRange(bastionHeaderRow, 1).setValue('BASTION FACILITIES (chosen)');
  setHeaderStyle_(sheet.getRange(bastionHeaderRow, 1));
  sheet.getRange(bastionHeaderRow + 1, 1, 1, 4).setValues([['Owner', 'Facility', 'Order', 'Status']]);
  setHeaderStyle_(sheet.getRange(bastionHeaderRow + 1, 1, 1, 4));
  var bastionRows = BASTION_CHOSEN.map(function (b) { return [b.owner, b.facility, b.order, b.status]; });
  sheet.getRange(bastionHeaderRow + 2, 1, bastionRows.length, 4).setValues(bastionRows);
  sheet.getRange(bastionHeaderRow + 2 + bastionRows.length + 1, 1, 1, 4).merge()
    .setValue('Full facility catalog: see the "' + SHEET_BASTION_FACILITIES + '" tab.')
    .setFontStyle('italic');

  var layoutHeaderRow = bastionHeaderRow + 2 + bastionRows.length + 3;
  sheet.getRange(layoutHeaderRow, 1).setValue('LAYOUT');
  setHeaderStyle_(sheet.getRange(layoutHeaderRow, 1));
  sheet.getRange(layoutHeaderRow + 1, 1).setValue('Upper deck');
  sheet.getRange(layoutHeaderRow + 1, 2, 1, 5).merge()
    .setValue('Helm room, Main deck (rigging + ballista positions), Lookout, Galley')
    .setWrap(true);
  sheet.getRange(layoutHeaderRow + 2, 1).setValue('Lower deck');
  sheet.getRange(layoutHeaderRow + 2, 2, 1, 5).merge()
    .setValue('Crew quarters, Captain\'s quarters, Cargo holds (incl. Storehouse), Engineering, Sick bay/galley stores')
    .setWrap(true);

  sheet.setColumnWidths(1, 6, 130);

  setNamedRange_(ss, 'NF_HP_CURRENT', sheet.getRange('E12'));
  setNamedRange_(ss, 'NF_REPAIR_BILL', sheet.getRange('B13'));
}

function setupCrewAboardTab_(ss) {
  var sheet = getOrCreateSheet_(ss, SHEET_CREW_ABOARD);

  var headers = ['Name', 'Species/Class', 'Role', 'Current Station', 'HP', 'Max HP', 'Patch Used', 'Notes'];
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  setHeaderStyle_(sheet.getRange(1, 1, 1, headers.length));

  var rows = CREW_ROSTER.map(function (c) {
    return [c.name, c.speciesClass, c.role, '', c.maxHp, c.maxHp, false, c.notes];
  });
  var dataRange = sheet.getRange(2, 1, rows.length, headers.length);
  dataRange.setValues(rows);

  var stationRange = sheet.getRange(2, 4, rows.length, 1);
  var stationRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(STATION_OPTIONS, true)
    .setAllowInvalid(false)
    .build();
  stationRange.setDataValidation(stationRule);

  var patchRange = sheet.getRange(2, 7, rows.length, 1);
  patchRange.insertCheckboxes();

  sheet.getRange(rows.length + 3, 1, 1, headers.length).merge()
    .setValue('Flurry (Aerion\'s non-combat pet) does not stand a station and is not listed above.')
    .setFontStyle('italic');

  sheet.setColumnWidths(1, headers.length, 130);

  setNamedRange_(ss, 'CREW_TABLE_BODY', dataRange);
}
```

Note: `CREW_ROSTER` rows for `Orena`/`Aerion` have `maxHp: null`, so their HP/Max HP cells (columns 5/6) are written blank by `setValues` (a JS `null` in a `Range.setValues` cell clears that cell) — this is the correct behavior per Task 4's note, not a bug to fix.

- [ ] **Step 2: Push**

Run: `cd sheets/night-fury && clasp push`
Expected: `Setup.js` listed as pushed, no errors. (It won't run yet — nothing calls `setupNightFuryTab_`/`setupCrewAboardTab_` until Task 6's `rebuildAllTabs()`. This step only confirms the file parses as valid Apps Script.)

- [ ] **Step 3: Commit**

```bash
git add sheets/night-fury/Setup.js
git commit -m "Add Setup.js: Night Fury tab and Crew Aboard tab builders"
```

---

### Task 6: Setup.js part B — Bastion Facilities tab + Cargo Manifest tab + rebuild orchestrator

**Files:**
- Modify: `sheets/night-fury/Setup.js` (append to the file from Task 5)

**Interfaces:**
- Consumes: `BASTION_FACILITIES` (from `BastionFacilities.js`, Task 3), `BASTION_CHOSEN`, `SHIP` (from `ShipData.js`, Task 4), everything `Setup.js` part A produced (Task 5).
- Produces: `setupBastionFacilitiesTab_(ss)`, `setupCargoManifestTab_(ss)`, `deleteObsoleteTabs_(ss)`, `rebuildAllTabs()` (the only function meant to be run directly, from the Apps Script editor). Consumed manually in Task 8.

- [ ] **Step 1: Append the remaining builders and the orchestrator to `Setup.js`**

Add to the end of `sheets/night-fury/Setup.js`:

```javascript
function setupBastionFacilitiesTab_(ss) {
  var sheet = getOrCreateSheet_(ss, SHEET_BASTION_FACILITIES);

  sheet.getRange('A1:G1').merge()
    .setValue('Facility text: D&D 5e (2024) Dungeon Master\'s Guide, Chapter 8 (Bastions). Reference only — not enforced automatically by this Sheet.')
    .setWrap(true);

  sheet.getRange('A3').setValue('CHOSEN FACILITIES');
  setHeaderStyle_(sheet.getRange('A3'));
  sheet.getRange(4, 1, 1, 4).setValues([['Owner', 'Facility', 'Order', 'Status']]);
  setHeaderStyle_(sheet.getRange(4, 1, 1, 4));
  var chosenRows = BASTION_CHOSEN.map(function (b) { return [b.owner, b.facility, b.order, b.status]; });
  sheet.getRange(5, 1, chosenRows.length, 4).setValues(chosenRows);

  var catalogHeaderRow = 5 + chosenRows.length + 2;
  sheet.getRange(catalogHeaderRow, 1).setValue('FULL CATALOG');
  setHeaderStyle_(sheet.getRange(catalogHeaderRow, 1));

  var colHeaders = ['Facility', 'Level', 'Prereq', 'Space', 'Hirelings', 'Order', 'Description'];
  sheet.getRange(catalogHeaderRow + 1, 1, 1, colHeaders.length).setValues([colHeaders]);
  setHeaderStyle_(sheet.getRange(catalogHeaderRow + 1, 1, 1, colHeaders.length));

  var catalogRows = BASTION_FACILITIES.map(function (f) {
    return [f.name, f.level, f.prereq, f.space, f.hirelings, f.order, f.description];
  });
  var catalogRange = sheet.getRange(catalogHeaderRow + 2, 1, catalogRows.length, colHeaders.length);
  catalogRange.setValues(catalogRows);
  catalogRange.setWrap(true);
  catalogRange.setVerticalAlignment('top');

  sheet.setColumnWidths(1, 6, 110);
  sheet.setColumnWidth(7, 480);
}

function setupCargoManifestTab_(ss) {
  var sheet = getOrCreateSheet_(ss, SHEET_CARGO_MANIFEST);

  sheet.getRange('A1').setValue('CARGO MANIFEST');
  setHeaderStyle_(sheet.getRange('A1'));
  sheet.getRange('B1').setValue('Cap: ' + SHIP.cargoTons + ' tons');

  sheet.getRange('A2').setValue('Total (tons)');
  sheet.getRange('B2').setFormula('=SUM(C5:C500)');
  setLiveStyle_(sheet.getRange('B2'));

  sheet.getRange(4, 1, 1, 3).setValues([['Item', 'Notes', 'Weight (tons)']]);
  setHeaderStyle_(sheet.getRange(4, 1, 1, 3));

  sheet.setColumnWidths(1, 3, 180);
}

function deleteObsoleteTabs_(ss) {
  var obsolete = [
    'Character Template', 'Orena Delphine', 'Spells', 'Spells - 1',
    'Bard Table', 'Paladin Table', 'Multiclass Spell Slots',
    'Leveling Table', 'Read Me', 'Inventory',
  ];
  obsolete.forEach(function (name) {
    var sheet = ss.getSheetByName(name);
    if (sheet) {
      ss.deleteSheet(sheet);
    }
  });
}

function rebuildAllTabs() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  setupNightFuryTab_(ss);
  setupCrewAboardTab_(ss);
  setupBastionFacilitiesTab_(ss);
  setupCargoManifestTab_(ss);
  deleteObsoleteTabs_(ss);
  SpreadsheetApp.getUi().alert('Night Fury sheet rebuilt: 4 tabs, obsolete PC tabs removed.');
}
```

`rebuildAllTabs()` builds all 4 new tabs *before* deleting the obsolete ones, so the spreadsheet is never left with zero sheets mid-run (Apps Script refuses to delete the last remaining sheet).

- [ ] **Step 2: Push**

Run: `cd sheets/night-fury && clasp push`
Expected: `Setup.js` re-pushed with no errors.

- [ ] **Step 3: Commit**

```bash
git add sheets/night-fury/Setup.js
git commit -m "Add Bastion Facilities tab, Cargo Manifest tab, and rebuildAllTabs orchestrator"
```

---

### Task 7: Code.js — play-time menu and actions

**Files:**
- Modify: `sheets/night-fury/Code.js` (replace the Task 1 stub entirely)

**Interfaces:**
- Consumes: `parseAmountInput`, `clampHp`, `computeDamageResult`, `computeRepairBill` (from `Logic.js`, Task 2); `SHIP` (from `ShipData.js`, Task 4); named ranges `NF_HP_CURRENT`, `NF_REPAIR_BILL`, `CREW_TABLE_BODY` (defined by `Setup.js`'s `rebuildAllTabs()`, Tasks 5-6 — must be run once before this tab's menu actions will work).
- Produces: the `⚓ Night Fury` menu with 5 items, verified manually in Task 8.

- [ ] **Step 1: Replace `Code.js`**

```javascript
// Code.js — play-time menu and actions. Wraps Logic.js pure functions around
// live cell reads/writes. If this menu ever misbehaves, every value it writes
// can be edited directly in the "Night Fury" / "Crew Aboard" tabs instead —
// nothing here is the only path to a valid sheet state.
//
// Single-user assumption: the DM operates this menu (matches actual play —
// one person runs the sheet at the table). No concurrency guard.

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('⚓ Night Fury')
    .addItem('Apply Damage', 'applyDamage')
    .addItem('Emergency Patch', 'emergencyPatch')
    .addItem('Repair to Full', 'repairToFull')
    .addSeparator()
    .addItem('New Round', 'newRound')
    .addItem('New Encounter', 'newEncounter')
    .addToUi();
}

function getNamedRange_(name) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var range = ss.getRangeByName(name);
  if (!range) {
    throw new Error('Named range "' + name + '" not found — run rebuildAllTabs() from the Apps Script editor first.');
  }
  return range;
}

// Returns null if the user canceled, undefined if they entered something
// that doesn't parse as a number, or the parsed number otherwise.
function promptForNumber_(ui, title, promptText) {
  var response = ui.prompt(title, promptText, ui.ButtonSet.OK_CANCEL);
  if (response.getSelectedButton() !== ui.Button.OK) {
    return null;
  }
  var parsed = parseAmountInput(response.getResponseText());
  return parsed.valid ? parsed.value : undefined;
}

function applyDamage() {
  var ui = SpreadsheetApp.getUi();
  var toast = SpreadsheetApp.getActiveSpreadsheet().toast.bind(SpreadsheetApp.getActiveSpreadsheet());

  var raw = promptForNumber_(ui, 'Apply Damage', 'Incoming hit amount:');
  if (raw === null) return; // canceled
  if (raw === undefined) {
    toast('Enter a non-negative number. Nothing was changed.');
    return;
  }

  var mitigateResponse = ui.alert('Apply Damage', 'Is Tack actively mitigating this hit? (Reactive Repair, -10 to damage over threshold)', ui.ButtonSet.YES_NO);
  var tackMitigating = (mitigateResponse === ui.Button.YES);

  var result = computeDamageResult(raw, tackMitigating, SHIP.damageThreshold);
  if (!result.valid) {
    toast('Enter a non-negative number. Nothing was changed.');
    return;
  }
  if (!result.applied) {
    toast(result.reason);
    return;
  }

  var hpRange = getNamedRange_('NF_HP_CURRENT');
  var billRange = getNamedRange_('NF_REPAIR_BILL');
  var newHp = clampHp(hpRange.getValue(), -result.damage, SHIP.maxHp);
  var newBill = computeRepairBill(billRange.getValue(), result.damage, SHIP.gpPerRepairPoint);
  hpRange.setValue(newHp);
  billRange.setValue(newBill);
  toast(result.damage + ' damage applied. HP: ' + newHp + '/' + SHIP.maxHp + '. Repair bill: ' + newBill + ' gp.');
}

function emergencyPatch() {
  var ui = SpreadsheetApp.getUi();
  var toast = SpreadsheetApp.getActiveSpreadsheet().toast.bind(SpreadsheetApp.getActiveSpreadsheet());

  var nameResponse = ui.prompt('Emergency Patch', 'Engineer\'s name (must match a row on Crew Aboard):', ui.ButtonSet.OK_CANCEL);
  if (nameResponse.getSelectedButton() !== ui.Button.OK) return;
  var engineerName = nameResponse.getResponseText().trim();

  var crewRange = getNamedRange_('CREW_TABLE_BODY');
  var values = crewRange.getValues();
  var rowIndex = -1;
  for (var i = 0; i < values.length; i++) {
    if (String(values[i][0]).trim().toLowerCase() === engineerName.toLowerCase()) {
      rowIndex = i;
      break;
    }
  }
  if (rowIndex === -1) {
    toast('No crew member named "' + engineerName + '" found on Crew Aboard. Nothing was changed.');
    return;
  }
  if (values[rowIndex][6] === true) { // Patch Used column
    toast(engineerName + ' has already used Emergency Patch this encounter.');
    return;
  }

  var levelResponse = ui.prompt('Emergency Patch', 'Confirm the DC 12 Technology/Intelligence check succeeded at the table, then enter ' + engineerName + '\'s level:', ui.ButtonSet.OK_CANCEL);
  if (levelResponse.getSelectedButton() !== ui.Button.OK) return;
  var parsed = parseAmountInput(levelResponse.getResponseText());
  if (!parsed.valid) {
    toast('Enter a non-negative number. Nothing was changed.');
    return;
  }

  var maxHp = values[rowIndex][5];
  var currentHp = values[rowIndex][4];
  var newHp = clampHp(currentHp, parsed.value, typeof maxHp === 'number' ? maxHp : undefined);

  crewRange.getCell(rowIndex + 1, 5).setValue(newHp);
  crewRange.getCell(rowIndex + 1, 7).setValue(true);
  toast(engineerName + ' patched for ' + parsed.value + ' HP. Now at ' + newHp + (typeof maxHp === 'number' ? '/' + maxHp : '') + '.');
}

function repairToFull() {
  var hpRange = getNamedRange_('NF_HP_CURRENT');
  var billRange = getNamedRange_('NF_REPAIR_BILL');
  hpRange.setValue(SHIP.maxHp);
  billRange.setValue(0);
  SpreadsheetApp.getActiveSpreadsheet().toast('Night Fury repaired to full: ' + SHIP.maxHp + ' HP, repair bill cleared.');
}

function newRound() {
  var crewRange = getNamedRange_('CREW_TABLE_BODY');
  var numRows = crewRange.getNumRows();
  var stationCol = crewRange.getCell(1, 4).getColumn();
  var sheet = crewRange.getSheet();
  sheet.getRange(crewRange.getRow(), stationCol, numRows, 1).clearContent();
  SpreadsheetApp.getActiveSpreadsheet().toast('Station assignments cleared for the new round.');
}

function newEncounter() {
  newRound();
  var crewRange = getNamedRange_('CREW_TABLE_BODY');
  var numRows = crewRange.getNumRows();
  var patchCol = crewRange.getCell(1, 7).getColumn();
  var sheet = crewRange.getSheet();
  sheet.getRange(crewRange.getRow(), patchCol, numRows, 1).setValue(false);
  SpreadsheetApp.getActiveSpreadsheet().toast('New encounter: stations cleared, Emergency Patch flags reset.');
}
```

- [ ] **Step 2: Push**

Run: `cd sheets/night-fury && clasp push`
Expected: `Code.js` re-pushed with no errors.

- [ ] **Step 3: Commit**

```bash
git add sheets/night-fury/Code.js
git commit -m "Add the play-time Code.js menu: Apply Damage, Emergency Patch, Repair to Full, New Round, New Encounter"
```

---

### Task 8: Rebuild and verify in the live Sheet

**Files:** none (manual verification against the live Google Sheet — this is the task that proves Tasks 1-7 actually work together, since none of the Apps Script code is testable outside the Apps Script runtime)

- [ ] **Step 1: Push everything and open the script editor**

```bash
cd sheets/night-fury && clasp push && clasp open
```

Expected: browser opens the Apps Script editor for the bound project, showing `Code.js`, `Logic.js`, `Setup.js`, `ShipData.js`, `BastionFacilities.js`, `appsscript.json`.

- [ ] **Step 2: Run `rebuildAllTabs()` from the editor**

In the Apps Script editor: select `Setup.js` in the file list, choose `rebuildAllTabs` from the function dropdown next to the Run button, click Run. Authorize the script if prompted (first run only — it needs Spreadsheet access, which is expected for a bound script).

Expected: an alert dialog "Night Fury sheet rebuilt: 4 tabs, obsolete PC tabs removed."

- [ ] **Step 3: Open the actual Google Sheet and verify tab structure**

Open `https://docs.google.com/spreadsheets/d/1K4f4KNXDitZT8jcGyWIentumkTmfWrwZp6j92WyLEVs/edit`.

Verify:
- Exactly 4 tabs exist: **Night Fury**, **Crew Aboard**, **Bastion Facilities**, **Cargo Manifest**.
- The old tabs (Character Template, Orena Delphine, Spells, Spells - 1, Bard Table, Paladin Table, Multiclass Spell Slots, Leveling Table, Read Me, Inventory) are gone.
- **Night Fury** tab: legend row at top, AC 19 / Damage Threshold 20 / Speed / Cargo / Crew Capacity / Air all populated, Current HP cell (blue-filled) shows 250, Repair Bill (blue-filled) shows 0, Weapon Stations table lists Gertrude/Susan/Kevin with no ammo column, Systems & Add-ons lists all 7 rows, Money section shows 50,000 / 14,350 gp, Personality section shows only the flag + named-parts lines (nothing else), Bastion Facilities (chosen) lists the 4 rows, Layout section shows upper/lower deck.
- **Crew Aboard** tab: 7 rows (Orena, Aerion, Estra, Tack, Finny, Brass, Oz), Orena/Aerion's HP and Max HP cells are blank (not 0), the other 5 show their `Stat Blocks.md` HP values, Current Station column has a dropdown (click a cell, confirm the 6 options appear), Patch Used column shows checkboxes.
- **Bastion Facilities** tab: "Chosen Facilities" mini-table at top matches Night Fury tab's, "Full Catalog" below has 29 rows, spot-check that the Description column for "Arcane Study" contains real text (not "Loading...").
- **Cargo Manifest** tab: header row, "Total (tons)" cell (blue-filled) shows 0 or blank-safe (empty range sums to 0), Cap: 20 tons label present.

- [ ] **Step 4: Reload the Sheet and verify the menu**

Reload the browser tab (menu only installs on open via `onOpen()`). Confirm a **⚓ Night Fury** menu appears in the menu bar with: Apply Damage, Emergency Patch, Repair to Full, a separator, New Round, New Encounter.

- [ ] **Step 5: Test Apply Damage — below-threshold no-op**

Click ⚓ Night Fury → Apply Damage. Enter `15`. Click a mitigation answer (either). Expected: toast reads "Hit below damage threshold (20) — no effect." Current HP on the Night Fury tab is still 250.

- [ ] **Step 6: Test Apply Damage — normal hit**

Click ⚓ Night Fury → Apply Damage. Enter `23`. Click "No" on the Tack mitigation question. Expected: toast reads "23 damage applied. HP: 227/250. Repair bill: 460 gp." Confirm the Night Fury tab's Current HP cell now shows 227 and Repair Bill shows 460.

- [ ] **Step 7: Test Apply Damage — Tack mitigation**

Click ⚓ Night Fury → Apply Damage. Enter `23`. Click "Yes" on the Tack mitigation question. Expected: toast reads "13 damage applied. HP: 214/250. Repair bill: 720 gp." (720 = 460 + 13×20.) Confirm the sheet matches.

- [ ] **Step 8: Test Apply Damage — canceled and invalid input**

Click ⚓ Night Fury → Apply Damage, click Cancel. Expected: no dialog, no toast, no sheet change. Repeat, this time entering `abc` and clicking OK. Expected: toast reads "Enter a non-negative number. Nothing was changed." HP/Repair Bill unchanged from Step 7's values.

- [ ] **Step 9: Test Emergency Patch — success, then blocked reuse**

Click ⚓ Night Fury → Emergency Patch. Enter `Tack`. Enter `4` for level (assume Tack is level 4 for this test). Expected: toast confirms Tack patched for 4 HP; Crew Aboard's Tack row HP increases by 4 (capped at his Max HP of 33) and Patch Used is now checked. Repeat the whole flow for `Tack` again. Expected: toast reads "Tack has already used Emergency Patch this encounter." — no further HP change.

- [ ] **Step 10: Test Repair to Full**

Click ⚓ Night Fury → Repair to Full. Expected: toast confirms repair; Night Fury tab's Current HP returns to 250 and Repair Bill returns to 0.

- [ ] **Step 11: Test New Round vs. New Encounter**

On Crew Aboard, manually set a couple of crew members' Current Station cells (e.g. Tack → Engineer, Oz → Gunner) and confirm Tack's Patch Used checkbox is still checked from Step 9 if you haven't run Repair to Full/reset it — if it's already unchecked from a prior step, check it manually to set up this test. Click ⚓ Night Fury → New Round. Expected: both Current Station cells clear; Patch Used checkboxes are untouched. Set the station cells again and ensure a Patch Used checkbox is checked. Click ⚓ Night Fury → New Encounter. Expected: both Current Station cells clear AND the Patch Used checkbox clears.

- [ ] **Step 12: Final commit and push to GitHub**

If Step 3-11 surfaced any fixes, commit them now with a clear message. Otherwise:

```bash
git status
```

Expected: working tree clean (everything was already committed per-task). Then:

```bash
git push
```

Per this repo's `CLAUDE.md`: "Commit and push after every substantive change... Don't leave work sitting uncommitted between sessions."

---

## Self-Review Notes

- **Spec coverage:** every section of `docs/superpowers/specs/2026-09-20-night-fury-sheets-sheet-design.md` maps to a task — the quadrant-mapping table → Task 5 (`setupNightFuryTab_`); Crew Aboard → Task 5 (`setupCrewAboardTab_`); Bastion Facilities → Tasks 3 + 6; Cargo Manifest → Task 6; the 5-item Apps Script menu (with the `New Round`/`New Encounter` split, clamping, input validation, Tack mitigation, single-user assumption, and menu-failure fallback all folded into the spec in the last revision) → Task 7.
- **No placeholders:** every code block above is complete, verified-plausible source (the extraction script was run against the real file in-session; the Logic.js math was hand-traced against its own tests). No "TBD"/"add validation"/"similar to Task N" language anywhere.
- **Type/name consistency checked:** `NF_HP_CURRENT`/`NF_REPAIR_BILL`/`CREW_TABLE_BODY` named-range names match between Task 5 (defined) and Task 7 (consumed); `CREW_TABLE_BODY` column order (Name=1, Species/Class=2, Role=3, Current Station=4, HP=5, Max HP=6, Patch Used=7, Notes=8) matches between Task 5's `setupCrewAboardTab_` and Task 7's `emergencyPatch`/`newRound`/`newEncounter` column-index math (`getCell(rowIndex+1, 5)` for HP, `7` for Patch Used, station column looked up dynamically via `getCell(1,4).getColumn()` rather than hardcoded, which is more robust); `Logic.js`'s exported function names (`parseAmountInput`, `clampHp`, `computeDamageResult`, `computeRepairBill`) match exactly between Task 2's implementation, Task 2's test, and Task 7's `Code.js` usage.
