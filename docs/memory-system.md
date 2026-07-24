# The Memory System (portable spec) — v2

A layered, file-based memory system that gives a stateless AI agent real continuity
across sessions, machines, and environments. Written to be handed to another project
to review and implement. This document describes the system as used in the `ocho-frames`
workspace, and calls out clearly what is portable vs project-specific.

**v2 (2026-07-24)** hardens the base system for scale: extractable client-tagged registries
(`DECISIONS.md`, `OPEN-QUESTIONS.md`), a session index + full-text search, a close-out
`check` with a git pre-push hook (enforcement), and a `reconcile` staleness pass — all via
one stdlib tool, `scripts/memory_tools.py`. The additions target the two things that break a
prose-log system as it grows: **retrieval decay** and **compliance drift**.

---

## 1. Philosophy

**Never start a session cold.** Continuity does not come from the model "remembering."
It comes from a small set of disciplined files that every session *reads first* and
*writes last*. The files are the memory; the agent is stateless between sessions.

Three principles hold the system together:

1. **The file is the memory.** If it is not written down, it did not happen. The value
   of a session is only captured when it is logged.
2. **Source of truth over artifacts.** Commit the prompts, scripts, and specs that
   *reproduce* outputs. Treat generated binaries (images, video, renders, audio) as
   disposable and gitignore them. This keeps the repo small and the intent legible.
3. **A dashboard, not just a diary.** One tiny always-current block answers "where are
   we right now?" so a new session is productive in seconds, without reading history.

---

## 2. The layers (tiered, like human memory)

The system is deliberately tiered so that hot, frequently-read state stays small while
nothing is ever lost.

| Layer | Where it lives | Role | Human-memory analogy |
|---|---|---|---|
| **0. Hot state** | `CURRENT STATE` block at the top of `memory.md` (~12 lines) | The single most important artifact: where we are *now*, what is blocked, what is next. Rewritten every session. | Working memory |
| **1. Episodic log** | `memory.md` session entries (newest at top) | Dated narrative: what we did, learned, decided, and left open. One entry per session. | Episodic memory |
| **2. Cold storage** | `memory-archive.md` | Oldest session entries, moved here automatically when the log grows past a size threshold, so working memory stays lean. | Long-term recall |
| **3. Reference / procedural** | Structured docs: brand/voice guides, process docs, prompt logs, per-artifact `design.md`, architecture docs | Durable "what X is" and "how we do X", kept *separate* from the running narrative so it is not buried in the log. | Semantic / procedural memory |
| **3b. Extractable registries** | `DECISIONS.md`, `OPEN-QUESTIONS.md` (one-line schema, client-tagged) | The two things you re-query most, pulled *out* of prose so they are listable, filterable by client, and age-trackable. | Structured recall |
| **3c. Derived index** | `memory-index.md` (auto-generated TOC of every session) | A scannable map of all sessions (hot + archived) so retrieval does not decay as history grows. | Table of contents |
| **4. Cross-session facts** | Agent-native memory (e.g. Claude Code auto-memory): a `MEMORY.md` index + one fact per file, frontmatter-tagged | Facts the harness auto-surfaces into context: user preferences, standing constraints, reference pointers. | Priming / recognition |

**Version control (git) ties it all together and doubles as the sync layer.** A commit
is what makes one machine's or one environment's work visible to another. In a
single-environment project, git is still the durable spine; in a multi-environment
project it is the handoff channel (see §6).

---

## 3. The two rituals (the entire discipline)

Everything else is detail. If a project does only these two things, it has the system.

### Session start — read-first
1. Read the `CURRENT STATE` block, then the top few session entries of `memory.md`.
2. Read the active context docs (brand/voice/status notes for whatever is in flight).
3. Run `git log --oneline -5` to see what the last session (possibly on another machine)
   did. If the working tree is dirty with changes you did not make, a prior session did
   not close out, reconcile before working.

### Session end — close-out
1. **Update `CURRENT STATE`** (including the one-line handoff header: last-updated date,
   last session number, environment, working-tree status, git status, next action).
2. **Add a session entry to the top of the log** (see format in §4), tagged with
   environment, `Client:`, and `Tags:`.
3. **Update the registries:** record settled decisions in `DECISIONS.md`, new/resolved
   open loops in `OPEN-QUESTIONS.md`.
4. **Run the maintenance tools:** the archiver (no-op unless over threshold), then
   `memory_tools.py index` to regenerate the session index, then `memory_tools.py check`
   (must pass) to verify the close-out is complete.
5. **`git commit && git push`.** The commit is the handoff; nothing is "saved" until it
   is committed. (A pre-push hook re-runs `check` as a safety net.)

These rituals must be written into the project's agent-instructions file
(`CLAUDE.md` / `AGENTS.md` / equivalent) as **mandatory, override-default** steps, not
suggestions. The agent should treat them as non-negotiable, and the `check` tool +
pre-push hook exist precisely because "mandatory" is not self-enforcing (see §5).

---

## 4. Formats (copy these)

### CURRENT STATE header line
A single italic line at the very top of the block, so status is scannable at a glance:

```
*Last updated: YYYY-MM-DD | Last session: NNN (Environment, CLOSED) |
Working tree: committed clean | Git: pushed | Next: <the one next action>*
```

Then ~12 bullet lines max. Newest/most-important context first. Prefix genuinely new
items with **NEW (Session NNN):** so a returning session sees what changed. Ruthlessly
delete or compress stale bullets, this block is a dashboard, not an archive.

### Session log entry
Reverse-chronological (newest at top of the log), continuously numbered across *all*
environments so the sequence is never ambiguous:

```
## Session NNN (YYYY-MM-DD, Environment): short title

What we did, what we learned, what we decided, what is still open.
Call out durable lessons explicitly so they can be lifted into reference docs later.
Cross-link related memory with [[wikilinks]] where the agent memory supports it.
```

### Reference doc header (for derived/synced docs)
When a source doc drives a condensed or client-facing derivative, stamp the derivative:

```
> Source of truth: <path to the internal source doc>
> Synced: YYYY-MM-DD
```

---

## 5. The tooling layer (all stdlib, no dependencies)

Two small Python scripts keep the system bounded, queryable, and self-checking. Both are
plain-stdlib and operate on the markdown files, so the system stays legible.

### 5.1 The archiver — bounded hot memory
`scripts/archive_memory.py` keeps the always-loaded memory from bloating the context window:
- **No-op** until `memory.md` exceeds a size threshold (this project uses 90 KB).
- When exceeded, it **moves the oldest session entries** into `memory-archive.md`, bringing
  the working file back under a lower watermark (~75 KB). Nothing is lost; only the *hot*
  file shrinks. Safe to run unconditionally.

### 5.2 `memory_tools.py` — retrieval, structure, and enforcement
One tool with subcommands, addressing the two things that otherwise break at scale
(retrieval decay and compliance drift):

| Subcommand | What it does | Fixes |
|---|---|---|
| `check` | Verifies the close-out ritual: CURRENT STATE dated today, a session entry for today, registries well-formed. Exit 1 on failure. | **Compliance** (the ritual can no longer silently be skipped) |
| `index` | Regenerates `memory-index.md`, a TOC of every session (hot + archived). | **Retrieval** (a scannable map that does not decay with size) |
| `search QUERY` | Case-insensitive search across memory + registries + docs. | **Retrieval** |
| `decisions [--client X]` | Lists decisions from `DECISIONS.md`, filterable by client. | **Structure / scale** |
| `open [--client X] [--stale N]` | Lists open questions, flags any open ≥ N sessions. | **Structure / scale** |
| `reconcile` | Flags CURRENT STATE staleness: dead file references, an out-of-date "Last updated", and aged open questions. | **Staleness** |
| `install-hooks` | Installs a git **pre-push** hook that runs `check`. Warn-only by default; `MEMORY_ENFORCE=1` makes it block. | **Compliance** |

### 5.3 The registries (schema)
`DECISIONS.md` and `OPEN-QUESTIONS.md` are human-editable but machine-parseable, so they are
the *authoritative* source for those two query-types (no auto-generation, no overwrite risk):
```
DECISIONS.md      - [D-NNN] YYYY-MM-DD | Client | decision text (Sxxx)
OPEN-QUESTIONS.md - [ ] [Q-NNN] YYYY-MM-DD | Client | question (opened Sxxx)   # open
                  - [x] [Q-NNN] YYYY-MM-DD | Client | ... RESOLVED Sxxx: outcome  # done
```
Aging is computed from the `opened Sxxx` tag against the latest session number, so a loop
that has been open too long surfaces itself instead of quietly persisting.

**Why enforcement matters:** "mandatory" instructions are not self-enforcing — a single
skipped close-out leaves a permanent gap (this project lost a key meeting's outcomes exactly
once that way). `check` + the pre-push hook turn the discipline into a gate.

---

## 6. Multi-environment sync (project-specific, but instructive)

This workspace is edited from two environments (a local machine and a sandboxed cloud
app). The memory system doubles as the sync protocol:

- **git commit = the handoff.** The commit message is how the other environment learns
  what happened.
- **Continuous session numbers across environments.** Check the top of the log for the
  last number before starting a new entry, regardless of which environment you are in.
- **Tag every session entry with its environment** (e.g. `(Claude Code)` vs `(Cowork)`),
  so environment-specific gotchas are attributable.
- **Never write from both environments at once.** If both are open, one is the builder
  and the other reads but does not write.
- **Environment-specific learnings** live in a labelled "Tools and gotchas" section of
  the instructions file, so the next session in that environment inherits them.

If your project has only one environment, keep the commit discipline and the numbering;
drop the rest.

---

## 7. Agent-native memory (layer 4) — optional but powerful

If your agent/harness offers a persistent memory store (Claude Code's auto-memory does),
use it for **facts that outlive any single session and should be primed automatically**:

- **One fact per file**, with frontmatter: a short `name` (kebab-case slug), a one-line
  `description` used for recall relevance, and a `type` (`user` | `feedback` | `project`
  | `reference`).
- **An index file** (`MEMORY.md`) with one pointer line per fact, this is what loads into
  context each session.
- **Cross-link with `[[slug]]` wikilinks.** A link to a not-yet-created fact is fine; it
  marks something worth writing later.
- **Store what is non-obvious and durable:** user preferences and working style, standing
  project constraints, hard-won process lessons, pointers to external resources. Do *not*
  store what the repo already records (code structure, git history, one-off task state).
- **Recalled memory reflects when it was written.** If a fact names a file or flag, verify
  it still exists before acting on it.

This layer is harness-specific. Layers 0–3 (the repo files) work with any agent or tool
and are the portable core.

---

## 8. What is portable vs project-specific

**Portable — implement anywhere:**
- The tiered files (hot state / episodic log / cold archive / reference docs).
- The two rituals (read-first, close-out) written as mandatory instructions.
- The `CURRENT STATE` dashboard with a handoff header line.
- Continuous, newest-first session numbering.
- The size-triggered archiver + archive file.
- The `memory_tools.py` tooling: `check` + pre-push hook (enforcement), `index` + `search`
  (retrieval), `decisions` / `open` registries (structure), `reconcile` (staleness).
- The client-tagged registries (`DECISIONS.md`, `OPEN-QUESTIONS.md`) and per-client tagging.
- Source-of-truth-over-binaries (`.gitignore` the generated, commit the reproducible).

**Project-specific — adapt to your context:**
- Multi-environment sync (§6). Keep only if you actually have >1 environment.
- The two-doc drift rule and synced-date headers (§4). Keep if you maintain derived docs.
- The exact reference docs (brand, voice, prompt logs), these depend on the domain.

**Optional — depends on your harness:**
- Agent-native memory (§7).

---

## 9. Implement from scratch — checklist

1. Create `memory.md` with a `CURRENT STATE` block at the top and a reverse-chronological
   session log beneath it. Seed CURRENT STATE with the project's current status and next
   action.
2. Write the **two rituals** into the agent-instructions file as mandatory,
   override-default steps. State plainly that continuity depends on them.
3. Add a **size-triggered archiver** script and an empty `memory-archive.md`. Pick
   thresholds that fit your model's context budget.
4. Add **`memory_tools.py`** (or equivalent) with `check` / `index` / `search` /
   `decisions` / `open` / `reconcile` / `install-hooks`, and run `install-hooks` once.
5. Create the client-tagged **registries** `DECISIONS.md` and `OPEN-QUESTIONS.md` with the
   one-line schema; seed them from your current known decisions and open loops.
6. Set **`.gitignore`** to exclude generated binaries; keep the scripts/prompts that
   reproduce them. Add a one-line note in each generator that "the prompt/script is the
   source of truth."
7. Create the **reference docs** your domain needs (brand, process, prompt log) and give
   each derived doc a "Source of truth / Synced" header if it is downstream of another.
8. (Optional) Stand up **agent-native memory**: a `MEMORY.md` index plus typed one-fact
   files, cross-linked with wikilinks.
9. (If multi-environment) Adopt the **sync protocol** in §6: commit-as-handoff, continuous
   numbering, environment tags, single-writer rule.
10. (When a second client goes active) Split `CURRENT STATE` into per-client mini-blocks
    under a shared workspace header; the registries and tooling already filter by client.

---

## 10. Why it works (the short version)

- **Bounded hot memory** (CURRENT STATE + a lean log, kept small by the archiver) means the
  agent reloads *only* what matters, fast, without context bloat.
- **Full history is never lost** (archive + git), so you can always dig deeper.
- **Retrieval does not decay with size** — the session index, full-text `search`, and the
  extractable decision/open-loop registries mean growth does not bury the past.
- **Compliance is enforced, not hoped for** — `check` plus the pre-push hook turn the
  close-out ritual from a good intention into a gate, closing the one failure mode that
  actually bit this project.
- **Scales by client** — one chronological log for cross-client learning, with per-client
  tagging and filtering so no single client's context drowns the others.
- **Source-of-truth-over-binaries** keeps the repo legible and reproducible, and keeps the
  memory about *intent*, not output.
- **Git as the spine** gives durable, syncable, attributable history for free.

The whole thing is intentionally low-tech: plain markdown files, one small script, and two
rituals. That is the point, it is legible to both humans and agents, portable across tools,
and cheap to maintain.
