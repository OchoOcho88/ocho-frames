# Workspace: ocho-frames

## Read these first, every session, before doing anything else

1. `memory.md` (the top entries) — the running session log: what we did, what we learned, decisions made, and what is still open.
2. The active client's `brand.md` — currently `clients/sportif/brand.md`.
3. Any status or resume note in the active client's folder, e.g. `clients/sportif/intake/RESEARCH-RUN-STATUS.md`.

Doing this is what gives a new session continuity. Do not start work cold.

## What this workspace is

Hugo's (Ocho's) personal creative and marketing workspace. Two tracks:

1. A creative-strategy pipeline: competitor analysis, then a synthesis brief, then AI-generated production media. See `docs/pipeline-architecture.md` and `docs/marketing-fundamentals.md`.
2. Client work under `clients/`.

It is also a HyperFrames video workspace (video as code). See `README.md`.

## Active work

- Client: **Sportif** (founder Lucy Wayne). Affordable-luxury fitnesswear accessories, Australian, launching September 2026. All context lives in `clients/sportif/`. Launch products are accessories (booty bands + vegan ankle strap), not apparel.

## Conventions (follow these)

- **Log every session.** At the end of any session with real work, add an entry to the TOP of `memory.md` (date, what we did, what we learned, decisions, open questions). Match the existing format.
- **Voice rule: no em dashes and no en dashes** anywhere in written output or files. Use commas, periods, or parentheses instead.
- **Secrets:** API keys go in `.env` only (gitignored). Never put a real key in `.env.example`, never commit secrets.
- **Work with Hugo:** ask for project context before assuming, and flag trade-offs rather than defaulting to one approach. Background on how he works is in the `hugo-working-style` skill.

## Tools and gotchas

- **Research (Perplexity):** `python3 scripts/perplexity_search.py "..." --model <model>`. The `sonar-deep-research` model runs for minutes via async polling, which exceeds the 45 second shell cap. Launch deep jobs in the background (`nohup python3 scripts/perplexity_search.py "..." --model sonar-deep-research --max-tokens 8000 > out.md 2> out.log &`) and poll the output files across calls.
- **Images:** the proven engine for our warm-neutral look is **gpt-image-2** (OpenAI API key in `.env`, or run the prompts in ChatGPT). Pixa is a different engine; if you use it, flag the mismatch to Hugo. gpt-image-2 prompt format is in `docs/platform-prompt-formats.md`.
- **Network egress:** scripts that call the internet need the sandbox Domain allowlist open (Settings, Capabilities, Network Egress). A change only applies to a freshly booted sandbox, so a NEW chat is required after changing it.
