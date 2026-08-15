# Inspiration Library — PRD

**Status:** MVP Phase 1 (Frontend + Mock Data)
**Owner:** Cheikh Sambakhe
**Last updated:** 2026-08-13

---

## 1. Summary

The Inspiration Library is a premium, AI-assisted visual reference tool for collecting, organizing, and reverse-engineering design inspirations. It turns images dropped into `Medias/` into a searchable, structured design archive — each entry enriched with metadata, design vocabulary, a written analysis, an image-generation prompt, and a UI recreation brief.

It should feel like a **curated design archive**, not a file manager or admin dashboard.

---

## 2. Primary Goal

For any saved inspiration, answer three questions fast:

1. **What is this design?**
2. **Why does it work?**
3. **How can I recreate or adapt it?**

---

## 3. Phase 1 Scope (this build)

Frontend + mock data only. No backend wiring, no Vision API calls, no `.env` setup in this phase — that's Phase 2.

### In scope
- Inspiration grid (card layout)
- Theme filter chips (derived from mock data)
- Client-side keyword search
- Full-screen inspector view
- Copy Image Prompt / Copy Brief / Close actions
- 3 hand-written mock inspirations, sourced from real images already in `Medias/`
- Responsive layout, keyboard-navigable

### Out of scope (Phase 2+)
- FastAPI scanner wiring (`backend/app/scanner.py` exists but unwired)
- Claude Vision analysis (`backend/app/vision.py` not yet created)
- `.env` / API key setup
- Local metadata caching to disk
- Manual rescan trigger
- SQLite, vector search, auth, cloud storage — explicitly deferred per original brief's upgrade path

---

## 4. Data Model

Single shared type, used identically by mock data now and live API responses later — this is what keeps the frontend independent of the data source.

```ts
type Inspiration = {
  id: string;
  name: string;
  source: string;              // plain-text brand/site name, no URL
  thumbnail: string;           // path to image in Medias/
  mediaType: string;           // e.g. "screenshot"
  theme: string;                // invented per-image, not forced into a fixed taxonomy
  styles: string[];             // max 3
  tags: string[];
  visualVocabulary: string[];
  designExplanation: string;
  imageGenerationPrompt: string;
  uiRecreationBrief: string;
};
```

---

## 5. Starter Content

3 real images from `Medias/`, hand-analyzed (not placeholder text) so this data is genuinely usable and doubles as the seed set once Vision goes live:

| Image | Source (plain text) |
|---|---|
| `Halo-Lab - Hero.PNG` | Halo-Lab |
| `MaximaTherapy - Hero.PNG` | MaximaTherapy |
| `logistics - Hero.png` | (logistics brand) |

Themes are invented to fit what's actually in these 3 images — not reused from any external reference taxonomy. More images added after this batch is validated.

---

## 6. Experience

### 6.1 Library Grid
- Card grid, one consistent frame treatment per card (cream card, thin border, image-forward) — no per-card background color rotation. The screenshot inside each card provides the visual variety, not the card chrome.
- Uniform card shape across the grid (masonry deferred until there's enough volume to evaluate it).
- Each card shows: image, name, style stack, tags, theme, subtle metadata.

### 6.2 Filter Chips
- Auto-derived from theme values present in the data — no hardcoded list.
- Instant client-side filtering, no reload.

### 6.3 Search
- Client-side keyword search across name, theme, styles, tags, visualVocabulary.
- No vector/semantic search in this phase.

### 6.4 Inspector (full-screen takeover)
Reference: user-provided screenshot of a working inspector view.

Layout:
- Overlay panel over a dimmed grid (grid stays visible behind, not a hard navigation away)
- Large image at top
- Serif headline (inspiration name)
- Small-caps category label, top-right (style pairing, e.g. "editorial x voxel 3D")
- Short descriptive line beneath headline
- Tag-pill rows
- Highlighted monospace "IMAGE RECIPE" block containing the image-generation prompt, with the key subject phrase visually highlighted
- Design analysis content covering composition, hierarchy, typography, color, texture, spacing, imagery, mood, visual strategy, and potential use cases — concise, not generic filler
- Bottom action bar: **COPY BRIEF**, **COPY IMAGE PROMPT**, **CLOSE**

---

## 7. Design System

`DESIGN.md` (Emerald & Cream) is the system of record for this build, applied as follows:

- **Page background:** light Cream (`--cream-50`) — matches the "generous whitespace / editorial archive" brief, not the dark-majority treatment `DESIGN.md` originally specified for its source product.
- **Typography:** Archivo Black (display/headlines), Fraunces (sparing accent line), **Lato** (body — updated from Inter).
- **Cards:** single consistent frame (cream surface, thin border), not the original kit's dark/gold/cream rotation — that rotation was designed for a fixed 12-tile brand grid and doesn't map to an open-ended, image-dominant inspiration archive.
- **Buttons/tags/dividers:** per `DESIGN.md` component tokens (pill radius, uppercase wide-tracking labels, mint/emerald tag fills).

---

## 8. Non-Goals (this phase)

- No authentication
- No cloud storage
- No database (JSON/in-memory mock data only)
- No background workers or queues
- No multi-provider AI abstraction
- No real Vision analysis — content is hand-written for the 3 starter images

---

## 9. Definition of Done (Phase 1)

- [ ] Shared `Inspiration` type defined in `src/types/`
- [ ] Mock data file with 3 real, hand-analyzed entries in `src/lib/mock-data/`
- [ ] Grid renders cards from mock data
- [ ] Theme chips auto-derive from data and filter instantly
- [ ] Search filters across name/theme/styles/tags/visualVocabulary
- [ ] Inspector opens full-screen on card click, matches reference screenshot layout
- [ ] Copy Image Prompt / Copy Brief work via clipboard
- [ ] Close returns to grid
- [ ] Responsive on desktop and mobile
- [ ] Verified running in browser (not just type-checked)

---

## 10. Phase 2 Preview (not built now)

Once Phase 1 is validated:
1. Wire `backend/app/scanner.py` to detect new/changed images in `Medias/`
2. Build `backend/app/vision.py` — one Claude Vision call per new image, returns the full metadata object
3. Add `.env` with Anthropic API key (backend-local, gitignored)
4. Cache metadata locally, keyed to image content so unchanged images are never re-analyzed
5. Replace mock data source with live API responses (same shared type, zero frontend changes required)

Upgrade path beyond that (JSON → SQLite → FTS5 → Postgres/pgvector; sync FastAPI → background tasks → queue) stays deferred until real usage demands it, per the original brief.
