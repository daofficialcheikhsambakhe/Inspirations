# 05 — Copy Prompt & Brief Actions

**What to build:** The COPY IMAGE PROMPT and COPY BRIEF buttons in the inspector copy the corresponding text (`imageGenerationPrompt` / `uiRecreationBrief`) to the clipboard, with visible confirmation feedback so the user knows the copy succeeded.

**Blocked by:** 04 — Inspiration Inspector

**Status:** ready-for-agent

- [ ] COPY IMAGE PROMPT copies the exact `imageGenerationPrompt` text for the open inspiration to the clipboard
- [ ] COPY BRIEF copies the exact `uiRecreationBrief` text for the open inspiration to the clipboard
- [ ] Each button shows brief visible confirmation on successful copy (e.g. label swap or toast), then reverts
- [ ] Verified running in browser: copy each field for all 3 starter inspirations and confirm clipboard contents match the source data exactly