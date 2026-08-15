# 04 — Inspiration Inspector

**What to build:** Clicking a card opens a full-screen takeover overlay (dimmed grid still visible behind, per the reference screenshot) showing the complete inspiration detail: large image, serif headline (name), small-caps category label top-right (style pairing), short description line, tag-pill rows, and the design analysis (composition, hierarchy, typography, color, texture, spacing, imagery, mood, visual strategy, potential use cases — concise, not generic filler). The image-generation prompt is shown in a highlighted monospace "IMAGE RECIPE" block. Close (button + Esc key) returns to the grid.

**Blocked by:** 01 — Foundation & Library Grid

**Status:** ready-for-agent

- [ ] Clicking any `InspirationCard` opens the full-screen inspector for that inspiration
- [ ] Grid remains visible, dimmed, behind the overlay (not a hard route navigation)
- [ ] Layout matches reference screenshot: large image top, serif headline, top-right small-caps category label, short description line, tag-pill rows
- [ ] Design analysis content rendered per PRD.md section 6.4 (composition, hierarchy, typography, color, texture, spacing, imagery, mood, visual strategy, use cases)
- [ ] Image-generation prompt shown in a highlighted monospace "IMAGE RECIPE" block
- [ ] UI recreation brief content is present and readable (scrollable if needed)
- [ ] CLOSE button and Esc key both return to the grid
- [ ] Bottom action bar shows COPY BRIEF, COPY IMAGE PROMPT, CLOSE (button wiring for copy actions is ticket 05 — buttons can be present but non-functional here)
- [ ] Verified running in browser for all 3 starter inspirations