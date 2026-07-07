# Workspace: ocho-frames

## Read these first, every session, before doing anything else

1. `memory.md`, starting with the CURRENT STATE block at the very top, then the top session entries (the running log: what we did, learned, decided, and what is still open).
2. The active client's `brand.md`, currently `clients/sportif/brand.md`, and `clients/sportif/voice-guidelines.md` before writing any content.
3. Any status or resume note in the active client's folder, e.g. `clients/sportif/intake/RESEARCH-RUN-STATUS.md`.

Doing this is what gives a new session continuity. Do not start work cold.

## What this workspace is

Hugo's (Ocho's) personal creative and marketing workspace. Two tracks:

1. A creative-strategy pipeline: competitor analysis, then a synthesis brief, then AI-generated production media. See `docs/pipeline-architecture.md` and `docs/marketing-fundamentals.md`.
2. Client work under `clients/`.

It is also a HyperFrames video workspace (video as code). See `README.md`.

## Active work

- Client: **Sportif** (founder Lucy Wayne). Affordable-luxury fitnesswear accessories, Australian, launching September 2026. All context lives in `clients/sportif/`. Launch products are accessories (booty bands + vegan ankle strap), not apparel.

## Two environments, one workspace (sync protocol)

Hugo works on this folder from TWO places, often alternating within the same day:

1. **Claude Code** (terminal / VS Code on his Mac): full shell, background processes survive, all local fonts, direct file deletion.
2. **Cowork** (Claude desktop app): sandboxed Linux shell, see the Cowork-specific gotchas below.

Which one am I? If shell paths look like `/sessions/<name>/mnt/hyperframes/`, this is Cowork. If they look like `/Users/hugobrizuela/...`, this is Claude Code.

**The handoff protocol (both environments, no exceptions):**

1. **Session start:** read the CURRENT STATE block, then `git log --oneline -5` to see what the other environment did last. If the working tree is dirty with changes you did not make, a session somewhere did not close out; commit or flag before working.
2. **Session end (the close-out ritual):** update the CURRENT STATE block (including the handoff line), add a session entry to the top of `memory.md` tagged with the environment, e.g. `Session 014 (2026-07-08, Claude Code): ...`, then `git add -A && git commit`. The commit is what makes the work visible to the other side.
3. **Session numbers are continuous across both environments.** Check the top of memory.md for the last number before starting a new entry.
4. **Do not run both environments on the same files at the same time.** If both are open, one is the builder and the other is the sounding board; the sounding board reads but does not write.
5. **Environment-specific learnings** go in "Tools and gotchas" below, labelled with which environment they apply to.

## Conventions (follow these)

- **Log every session.** At the end of any session with real work, add an entry to the TOP of `memory.md` (date, what we did, what we learned, decisions, open questions). Match the existing format.
- **Voice rule: no em dashes and no en dashes** anywhere in written output or files. Use commas, periods, or parentheses instead.
- **Secrets:** API keys go in `.env` only (gitignored). Never put a real key in `.env.example`, never commit secrets.
- **Work with Hugo:** ask for project context before assuming, and flag trade-offs rather than defaulting to one approach. Background on how he works is in the `hugo-working-style` skill.

## Tools and gotchas

- **Research (Perplexity), Cowork version.** In Cowork, background shell processes do NOT survive across tool calls (the sandbox reaps them; each call caps at ~45s), so nohup-and-poll does not work here. Use `scripts/pplx_async.py` instead: it submits async deep-research jobs that run server-side at Perplexity, persists request ids to a registry file on disk, and polls them in later short calls. Perplexity rate-limits async submissions (HTTP 429), so stagger submits (12 to 18s) and resubmit failures. Quick synchronous queries with sonar-pro can still use `python3 scripts/perplexity_search.py "..." --model sonar-pro`. (The old nohup workflow only works on Hugo's Mac via Claude Code, a different environment.)
- **Images:** the proven engine for our warm-neutral look is **gpt-image-2** (OpenAI API key in `.env`, or run the prompts in ChatGPT). Pixa is a different engine; if you use it, flag the mismatch to Hugo. gpt-image-2 prompt format is in `docs/platform-prompt-formats.md`.
- **Network egress:** scripts that call the internet need the sandbox Domain allowlist open (Settings, Capabilities, Network Egress). A change only applies to a freshly booted sandbox, so a NEW chat is required after changing it.
- **PDF generation:** weasyprint must be pip-installed per fresh sandbox (`pip install weasyprint --break-system-packages`). Sandbox fonts are limited to Lora (serif) and Poppins (geometric sans); Glacial Indifference (Sportif's real font) is not installed, so Poppins letter-spaced stands in for the SPORTIF wordmark and Lora carries titles.
- **Showing PDFs to Hugo:** present_files does not reliably preview a PDF in chat. Render pages to PNG and show a combined montage instead.
- **File locations:** keep all deliverables in the mounted hyperframes folder (stable path). Treat the sandbox outputs dir as throwaway; it gets wiped when the sandbox reboots mid-session.
- **File deletion in the mount** requires the `allow_cowork_file_delete` tool first; plain `rm` fails with Operation not permitted.
- **Client PDF set (Sportif):** exactly two Lucy-facing PDFs are current, `Sportif-Brand-Value-Plan.pdf` (strategy) and `Sportif-Launch-Plan.pdf` (operations), regenerated via `build-brand-value-plan.py` and `build-launch-plan.py` from the `-client.md` sources. Everything else lives in `clients/sportif/_archive/`. Do not resurrect archived PDFs.
- **Two-doc drift rule:** internal source docs (e.g. `brand-value-plan.md`) drive condensed client cuts (e.g. `brand-value-plan-client.md`). Any change to an internal doc must be reflected in its client cut and the PDF re-exported. Each client cut carries a "Source of truth" header; update its synced date when you sync.
