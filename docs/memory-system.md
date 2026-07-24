# The Memory System (portable spec)

A layered, file-based memory system that gives a stateless AI agent real continuity
across sessions, machines, and environments. Written to be handed to another project
to review and implement. This document describes the system as used in the `ocho-frames`
workspace, and calls out clearly what is portable vs project-specific.

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
2. **Add a session entry to the top of the log** (see format in §4).
3. **Run the archiver script** (a no-op unless the log crossed its size threshold).
4. **`git commit && git push`.** The commit is the handoff; nothing is "saved" until it
   is committed.

These rituals must be written into the project's agent-instructions file
(`CLAUDE.md` / `AGENTS.md` / equivalent) as **mandatory, override-default** steps, not
suggestions. The agent should treat them as non-negotiable.

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

## 5. The one piece of automation: the archiver

A tiny script (`scripts/archive_memory.py` in this project) keeps the always-loaded
memory bounded so it never bloats the context window:

- It is a **no-op** until `memory.md` exceeds a size threshold (this project uses 90 KB).
- When exceeded, it **moves the oldest session entries** from `memory.md` into
  `memory-archive.md`, bringing the working file back under a lower watermark (~75 KB).
- Nothing is lost, cold history is one file away; only the *hot* file shrinks.

Run it as step 3 of every close-out. Because it is a no-op most of the time, it is safe
to run unconditionally. Tune the thresholds to your model's context budget.

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
4. Set **`.gitignore`** to exclude generated binaries; keep the scripts/prompts that
   reproduce them. Add a one-line note in each generator that "the prompt/script is the
   source of truth."
5. Create the **reference docs** your domain needs (brand, process, prompt log) and give
   each derived doc a "Source of truth / Synced" header if it is downstream of another.
6. (Optional) Stand up **agent-native memory**: a `MEMORY.md` index plus typed one-fact
   files, cross-linked with wikilinks.
7. (If multi-environment) Adopt the **sync protocol** in §6: commit-as-handoff, continuous
   numbering, environment tags, single-writer rule.

---

## 10. Why it works (the short version)

- **Bounded hot memory** (CURRENT STATE + a lean log, kept small by the archiver) means the
  agent reloads *only* what matters, fast, without context bloat.
- **Full history is never lost** (archive + git), so you can always dig deeper.
- **Rituals as mandatory instructions** make the discipline automatic rather than
  aspirational, the agent does it every time.
- **Source-of-truth-over-binaries** keeps the repo legible and reproducible, and keeps the
  memory about *intent*, not output.
- **Git as the spine** gives durable, syncable, attributable history for free.

The whole thing is intentionally low-tech: plain markdown files, one small script, and two
rituals. That is the point, it is legible to both humans and agents, portable across tools,
and cheap to maintain.
