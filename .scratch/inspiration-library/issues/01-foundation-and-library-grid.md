# 01 — Foundation & Library Grid

**What to build:** Visiting the app shows a responsive card grid rendering the 3 real starter inspirations (Halo-Lab, MaximaTherapy, logistics) sourced from `Medias/`. Each card shows the image, name, style stack, tags, and theme, styled per `DESIGN.md`'s Emerald & Cream system (light Cream page background, uniform cream card frame with thin border, image-forward — no dark/gold background rotation between cards). This ticket establishes the shared `Inspiration` type and mock-data file that every later ticket builds on.

**Blocked by:** None — can start immediately

**Status:** ready-for-agent

- [ ] `Inspiration` type defined per PRD.md section 4 (`id`, `name`, `source`, `thumbnail`, `mediaType`, `theme`, `styles[]` max 3, `tags[]`, `visualVocabulary[]`, `designExplanation`, `imageGenerationPrompt`, `uiRecreationBrief`)
- [ ] Mock data file with 3 hand-analyzed entries: `Halo-Lab - Hero.PNG`, `MaximaTherapy - Hero.PNG`, `logistics - Hero.png` — real per-image analysis, not placeholder text; theme names invented to fit each image, not forced into any external taxonomy; `source` is plain-text brand name (no URL)
- [ ] `InspirationCard` component: image, name, style stack, tags, theme, subtle metadata — uniform frame treatment across all cards
- [ ] `InspirationGrid` component renders all mock inspirations
- [ ] Layout uses Archivo Black (display), Fraunces (sparing accent), Lato (body) per updated `DESIGN.md`
- [ ] Responsive across desktop and mobile
- [ ] Verified running in browser (not just type-checked)