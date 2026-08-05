# Design System — Studio Grid Kit (Emerald & Cream)

Palette swap only. Layout, card types, typography treatment, and copy structure are carried over unchanged from the original NOVA / ASTRA reference grid.

---

## 1. Color Tokens

| Token | Hex | Role | Replaces (original) |
|---|---|---|---|
| `--emerald-900` Deep Emerald | `#0F3D34` | Primary dark surface (majority of cards, hero bg) | Black |
| `--emerald-700` Emerald | `#134E43` | Secondary dark surface — layering, alt dark cards | Black (variant) |
| `--mint-100` Mint Mist | `#E6F0E9` | Light neutral — tags, quiet fills | Light grey |
| `--cream-50` Cream | `#F7F6F1` | Base light surface, reversed text on dark | White |
| `--gold-500` Gold | `#C8A96A` | Accent — CTAs, badges, highlight cards | Neon yellow-green |

**Ratio in the grid:** roughly matches the source — 5 dark (emerald) cards, 4 accent (gold) cards, 2 light (cream) cards, out of 12. Keep this ratio if you extend the grid; the dark surface should always be the majority so the gold accent still reads as a highlight, not a base color.

**Contrast notes:**
- Cream text (`#F7F6F1`) on Deep Emerald (`#0F3D34`) — passes AA for body and large text.
- Emerald text on Gold (`#C8A96A`) — passes AA for large/bold text only; keep body copy on gold cards short and bold, not long paragraphs.
- Avoid gold text on cream — too low contrast for anything but decorative marks.

---

## 2. Typography

| Role | Family | Usage |
|---|---|---|
| Display | `Archivo Black` | Card headlines, hero title — always uppercase, tight leading (0.96–1.02) |
| Accent | `Fraunces` (serif, weight 500) | One-off elegant statement lines — used sparingly, echoes the "wellness/elegant" tone of the Emerald & Cream reference |
| Body | `Inter` (400–800) | Captions, tags, buttons, paragraph copy |

**Scale:** 12 (caption/tag) → 16 (body) → 22 (card h3) → 34 (counter numerals) → 46+ (hero display, fluid up to 84px).

Letter-spacing on all-caps display text: `-0.01em` at large sizes to keep Archivo Black from feeling loose; eyebrows/tags use wide tracking (`0.1–0.18em`) instead, for contrast.

---

## 3. Grid & Card System

- **Unit:** single card = `4:5` aspect ratio (Instagram portrait), laid out 4-up on desktop, 2-up on mobile.
- **Radius:** `4px` on cards (sharp, not rounded — keeps the poster/print feel).
- **Padding:** `20px` inside every card, content pinned to top and bottom (eyebrow up top, headline/CTA at the base).
- **Gap:** `14px` between cards.

**Card types (12 total, reusable as a component library):**

1. **Brand mark** — dark surface, logo initial + wordmark, portrait silhouette
2. **Personal/story** — gold surface, portrait + short caption
3. **Statement** — dark surface, bold 2–3 line claim, no image
4. **Stat counter** — gold surface, 3 numerals + labels, headline below
5. **Live badge** — dark surface, pill badge top-left, portrait or object photo
6. **Service label** — cream surface, single bold service name, minimal
7. **Statement (long)** — dark surface, philosophy line + supporting one-liner
8. **Case study intro** — gold surface, brand name + portrait + status line
9. **Before/after** — dark-alt surface, portrait + single descriptive sentence
10. **Quote** — dark surface, large serif quote mark, italic quote, attribution
11. **Episode/media** — gold surface, media badge + portrait
12. **CTA (2-col span)** — cream surface, headline + pill button, always the closing tile

---

## 4. Components

- **Buttons:** pill radius (`999px`), three variants — `primary` (emerald fill), `gold` (gold fill), `ghost` (emerald outline). Uppercase label, 12px, bold, wide tracking.
- **Tags:** pill, mint fill on light backgrounds / emerald fill on dark backgrounds.
- **Dividers:** dashed emerald at low opacity for quiet separation; solid 2px gold when a divider needs to double as an accent line.
- **Photo slots:** every portrait/photo position in the original grid is a placeholder silhouette in this file — swap in real photography at 0.5–0.9 opacity blended into the card, not full-bleed, so the color surface still reads as the dominant layer.

---

## 5. Usage Notes

- Don't let gold become a background majority — it's the accent, same role the neon played in the source grid.
- Keep every headline uppercase and set in Archivo Black; the Fraunces serif is reserved for one accent line per page, not repeated per card.
- The satin/sheen gradient used behind the hero (soft gold + mint glow on deep emerald) is the one signature flourish pulled from the Emerald & Cream reference photo — use it once, on the primary dark hero, not on every dark card.
