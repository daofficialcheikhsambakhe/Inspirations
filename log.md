# Decision Log

Meaningful architectural and strategic decisions only — not conversations.

**Format:** date · decision · reasoning · context

---

## 2026-07-29

### Companion files are absolute reference priority

**Decision:** For every task, `AUDIENCE.md`, `CLAUDE.md`, `DESIGN.md`, `SOUL.md`, and `VOICE.md` take absolute priority over all other input.

**Reasoning:** Keeps agent output aligned with identity, voice, audience, and design system instead of drifting toward generic or conflicting sources.

**Context:** Established at the start of the Claude Code Club Phase 2 session as the operating rule for all work in this repo.

---

### Applied Learning section in CLAUDE.md

**Decision:** Add an `Applied Learning` section to root `CLAUDE.md`. One-line bullets only (<15 words), no explanations. Add when something fails repeatedly, gets re-explained, or a tool workaround is found.

**Reasoning:** Captures friction and fixes as durable memory without bloating the file with narrative or one-off session notes.

**Context:** Part of building persistent agent memory that improves across sessions without manual re-briefing.

---

### 95% confidence before making changes

**Decision:** Do not make any changes until 95% confidence in what needs to be built. Ask follow-up questions one at a time until that threshold is reached.

**Reasoning:** Reduces wasted rework from assumptions; matches Cheikh's preference for one question at a time and shipping over guessing.

**Context:** Added to the ALWAYS RULE section in root `CLAUDE.md` alongside the existing "next concrete action" rule.

---

## 2026-07-30

### Markdown-only personal knowledge vault

**Decision:** Personal knowledge base lives in `vault/` — no vector database. Structure: `raw/` (unprocessed sources), `wiki/` (interlinked markdown articles), `index.md` (master index). Ingest trigger: drop file in `raw/`, say "ingest that."

**Reasoning:** Searchable, linkable, human-readable knowledge without embedding infrastructure or cost. Fits zero-capital constraint and Cheikh's learn-by-shipping workflow.

**Context:** Vault rules documented in `vault/CLAUDE.md`. Root `CLAUDE.md` remains live agent memory; vault holds reference and history. Root wins on current priorities if they conflict.

---

### Decisions logged to decisions/log.md

**Decision:** Log meaningful architectural and strategic decisions here — date, decision, reasoning, context. Save decisions, not conversations.

**Reasoning:** Separates durable choices from chat history so future sessions (and Cheikh) can see _why_ the system is shaped the way it is without re-reading threads.

**Context:** Created during Phase 2 memory infrastructure setup alongside the knowledge vault.

---

## 2026-08-04

### Context capacity reminder and summary reset rule

**Decision:** When the conversation context reaches 80% usage, summarize the current state and clear the conversation context, preserving only the durable decision log and memory notes.

**Reasoning:** Prevents the agent from losing the project thread while keeping memory compact and reusable. This protects long-running work without forcing the user to re-explain the same decisions.

**Context:** Added after the inspiration library build and local media-scanner work. This applies to all future sessions in this project and should be enforced during high-context runs.

---

### 2026-08-08

Copy Rules Log
Rule: Avoid AI-Written Copy Tells

Applies to: all copy, emails, and posts (Cheikh + client work).

Before shipping any copy, scan for these patterns. If found, rewrite in plain, specific, human language — no exceptions for "it sounds nice."

Sentence-structure tells
"It's not X. It's Y."
"You don't need another…"
"Whether you're…"
"From X to Y" transformations
"Not only… but also…"
Perfectly balanced / symmetrical sentences ("Think differently. Act intentionally. Live purposefully.")
Tricolon / lists of three used as a crutch ("Clarity, confidence, and freedom.")
Excessive parallelism ("Discover your purpose. Build your offer. Grow your business.")
Too many one-line paragraphs stacked for drama
Excessive rhetorical questions, especially stacked ("What if…" x3)
Artificially dramatic fragments ("No more excuses. No more confusion.")
Excessive em dashes as a crutch for rhythm
Excessive capitalization for emphasis
Emoji-as-structure (✨ → 💰 → 🌱)
Phrase-level tells (cut on sight)

"Here's the thing…" · "The truth is…" · "And that's exactly why…" · "At the end of the day…" · "When it comes to…" · "The key is…" · "The beauty of…" · "Because…" tacked onto every claim · "In today's world…" · "Imagine…" · "You already know…" / "Deep down…" · "There's a reason…" · "Once you…" / "The moment you…" / "Everything changes when…" · "You've been searching…" · "You were meant to…" · "Ready to…" (as a CTA) · "Start your journey" (as a CTA)

Word-level overuse (thesaurus behavior)

Unlock · Step into · Embrace · Harness · Tap into · Cultivate · Navigate · Journey · Landscape · Ecosystem · Powerful · Transformative · Holistic · Aligned · Authentic · Abundance · Purpose · Freedom · Clarity · Potential · Simply / Just / More than just

Substance-level tells (the ones that actually matter most)
Generic emotional labeling — naming a feeling ("stuck, overwhelmed, frustrated") instead of showing the moment that produces it.
Fake specificity — sounds concrete but is actually vague ("countless nights tweaking your offer").
Generic pain points / generic desires — could apply to literally any reader.
Generic enemy creation — "the system was never designed to help you."
No genuine uncertainty, no strong opinions — every claim hedged into mush, or every claim overconfident with zero texture.
Constantly positive resolution — problem always neatly resolved, no mess.
No mundane, sensory, or personal detail — nothing a real specific person would actually say (no imperfect grammar, no quirky aside, no concrete image).
Overly comprehensive benefit lists — "clarity, confidence, purpose, direction, freedom, fulfillment, abundance, momentum."
Repeating the headline's idea throughout the page — same phrase recycled as every section's crutch.
Unsubstantiated social proof — "thousands of people are already…" with nothing behind it.
Artificial urgency — "the time is now" with no real reason why.
The biggest tell of all: it sounds like nobody actually said it out loud.
The fix, in one line

Write the sentence the way you'd actually say it to Marcus over coffee — specific, a little rough, opinionated — then tighten. Never the reverse.
