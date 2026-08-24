# docs/ — the interactive ship sheet

`index.html` is **Ship's Papers**, a self-contained, editable D&D 5e-styled character sheet for the crew's ship. Every stat is a write-over field; edits save to the viewer's own browser (localStorage), and there's Reset and Print/PDF. No build step, no dependencies — one file.

## View it
- **Open locally:** double-click `index.html` (or drag it into a browser).
- **Interactive Artifact (private link):** published from the co-DM session — ask Joel for the claude.ai/code/artifact link.

## Host it on GitHub Pages (free, public URL)
1. Repo **Settings → Pages**.
2. **Source:** "Deploy from a branch". **Branch:** the default branch, **folder:** `/docs`. Save.
3. After a minute it's live at `https://joelkhchan2.github.io/astral-vagabonds/` (this file's folder becomes the site root, so `index.html` is the landing page).

Note: the private repo must allow Pages (GitHub Free serves Pages from public repos; for a private repo, Pages requires a paid plan or making the repo public). If Pages isn't available, the Artifact link and opening the file locally both work.

## Notes
- Edits are **per-browser** — each person who opens it keeps their own copy; nothing syncs between the DM and players. If you later want one shared, synced sheet, that needs a hosted backend (say the word).
- Fan-made; not affiliated with or endorsed by Wizards of the Coast. Uses Google Fonts (Cinzel, Spectral, IBM Plex Mono).
- Source of the stat values: `../ships/The Ship (unnamed).md`.
</content>
