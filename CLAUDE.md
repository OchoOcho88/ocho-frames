# Workspace: ocho-frames

## FIRST THING, EVERY SESSION, BEFORE ANYTHING ELSE

```
python3 scripts/startup.py
```

That command IS the session-start protocol (`/startup` in Claude Code). It is read-only and prints the environment, this session's number, git state, the CURRENT STATE block, one line per open loop, the content gate, the house rules and any flags. Read all of it before replying to Hugo. Then:

1. If the script raised FLAGS or reported a dirty tree, surface it to Hugo in your first message rather than absorbing it.
2. If any client-facing content will be written this session, read `clients/sportif/brand.md` and `clients/sportif/voice-guidelines.md` FIRST. Not a word of content before that.
3. Past detail is on demand, not read by default: `python3 scripts/memory_tools.py search "<term>"` and `... open --client <client>` (full rows).

It is a script because this file is NOT auto-loaded in Cowork (S031) and prose protocols got skipped (S033). Do not start work cold.

## What this workspace is

Hugo's (Ocho's) creative and marketing workspace: a creative-strategy pipeline (competitor analysis, synthesis brief, AI-generated media; `docs/pipeline-architecture.md`, `docs/marketing-fundamentals.md`) and client work under `clients/`. Also a HyperFrames video workspace (video as code, `README.md`).

## Active work

- Client: **Sportif** (founder Lucy Wayne). Affordable-luxury fitnesswear accessories, Australian, launching September 2026. All context lives in `clients/sportif/`. Launch products are accessories (booty bands + vegan ankle strap), not apparel.

## Two environments, one workspace (sync protocol)

Hugo works on this folder from **Claude Code** (terminal on his Mac: full shell, background jobs survive, local fonts, rm works) and **Cowork** (Claude desktop app: sandboxed Linux, 45s per call, no background jobs, rm blocked in the mount), often alternating within a day. Paths under `/sessions/<name>/mnt/hyperframes/` mean Cowork; `/Users/hugobrizuela/...` means Claude Code. Environment and tool gotchas live in `docs/gotchas.md`, which startup names but does not print; read it when a tool misbehaves and add new learnings there, labelled by environment.

**The handoff protocol (both environments, no exceptions):**

1. **Session start** is `startup.py` above. A dirty tree means a session somewhere did not close out; commit or flag before working.
2. **Session end (the close-out ritual, `/close-out` in Claude Code):** write the session entry at the top of `memory.md` with the five-heading template in `docs/memory-system.md` (Done, Learned, Decided, Open, Next; under 500 words; environment tag, `Client:` and `Tags:` lines), refresh CURRENT STATE (handoff line at most three sentences), mirror decisions into `DECISIONS.md` and loops into `OPEN-QUESTIONS.md`, then run:

    ```
    python3 scripts/closeout.py --commit -m "Session NNN: what happened"
    ```

    It clears stale git locks, sweeps changed files for em and en dashes, verifies the entry and CURRENT STATE, runs the archiver, index and `check`, and refuses to commit while anything fails. Drop `--commit` to check only. The commit is the handoff; push from the Mac.
3. **Session numbers are continuous across both environments.** Startup prints the next one.
4. **Do not run both environments on the same files at the same time.** If both are open, one builds and the other only reads.

## Conventions (follow these)

- **Log every session** with real work, as above. Registries are filterable by client (`scripts/memory_tools.py`); the system is documented in `docs/memory-system.md`. Dormant loops are parked with `[p]`, not deleted. A second active client splits CURRENT STATE into per-client mini-blocks.
- **Voice rule: no em dashes and no en dashes** anywhere in written output or files. Use commas, periods, or parentheses instead.
- **Layout rule for anything Hugo ACTS on** (prompts, instructions, checklists, setup steps): heading, then the thing to copy or use as ONE complete self-contained block, then the inputs or file names as bullets. Nothing in between. Analysis and caveats go at the END, a few bullets at most, never woven through the steps (S032).
- **Secrets:** API keys go in `.env` only (gitignored). Never put a real key in `.env.example`, never commit secrets.
- **Work with Hugo:** ask for project context before assuming, and flag trade-offs rather than defaulting to one approach. Background on how he works is in the `hugo-working-style` skill.
- **Generated media** goes in `clients/<client>/generated/images/` or `generated/videos/`, and every keeper's prompt is saved to the client's `image-prompts.md` (the prompt is the source of truth, binaries are gitignored). Iterate at quality low in Cowork, render finals in Claude Code.
- **Images:** the proven engine for the warm-neutral look is **gpt-image-2**; if another engine is used, flag the mismatch to Hugo. Prompt formats are in `docs/platform-prompt-formats.md`.
- **Two-doc drift rule:** an internal source doc drives its condensed client cut and PDF. Change one, sync the other and re-export (details and the Sportif PDF set in `docs/gotchas.md`).
