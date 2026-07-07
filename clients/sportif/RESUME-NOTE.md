# Resume note: paste this to start the next Sportif session

> Voice rule for this workspace: no em dashes, no en dashes. Updated 2026-07-07 (Session 013).

---

Resuming the Sportif workspace. Before doing anything, follow the session-start protocol in `CLAUDE.md` ("Two environments, one workspace"):

1. Read the CURRENT STATE block at the top of `memory.md`, then the Session 013 entry.
2. Run `git log --oneline -5` to see what the other environment did last. If the tree is dirty with changes you did not make, flag it before working.
3. Before writing any content, read `clients/sportif/brand.md` and `clients/sportif/voice-guidelines.md`.

Quick state:
- Strategy locked, two Lucy-facing PDFs current (Brand Value Plan + Launch Plan), everything else archived.
- The Lucy blocker email is in Hugo's Gmail drafts (Shopify, prices, fabric, who answers customers). May be sent by now; ask Hugo if she replied.
- Image pipeline is live: gpt-image-2 (OpenAI key in .env), prompts and rules in `clients/sportif/image-prompts.md`, output to `clients/sportif/generated/images/`. Production pattern: generate text-free, overlay real Glacial Indifference with `scripts/overlay_wordmark.py` (fonts at `brand/fonts/glacial-indifference/`).
- Lucy is picking between three 4:5 Instagram hero concepts (v5 unboxed, v6 set, v7 flat).

Likely jobs this session (ask Hugo which):
1. Render Lucy's hero pick at quality high (Claude Code only; Cowork's 45s cap only fits quality low), using the logged prompt, text-free, then overlay the wordmark.
2. If in Claude Code: `git push` (local was ~11 commits ahead of GitHub at close-out).
3. If Lucy replied to the blocker email: start the Shopify coming-soon page step-by-step.

End the session with the close-out ritual (in Claude Code: `/close-out`).
