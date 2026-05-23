# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## Session 002 — 2026-05-23 — Framework additions: prompts, recipes, skills, scheduled reflection

### What we did
- Added three new top-level folders to the workspace:
  - `prompts/` — reusable prompt templates with starter content for CSV→chart, PDF→summary, TikTok hook, product intro, and competitor analysis
  - `recipes/` — workflows we've proven and want to repeat, with a `_template.md` to copy from
  - `skills/` — workspace-level custom skills (different from the project-scoped `.agents/skills/`)
- Scheduled a weekly memory reflection task: every Sunday at 6pm, Claude reads `memory.md`, writes a "Weekly Review" section at the top, identifies patterns, and cleans up resolved open questions
- Documented the distinction between project-scoped vs workspace-scoped skills in `skills/README.md`

### What we learned
- **Skills can be scoped two ways:**
  - Project-scoped (`my-projects/<project>/.agents/skills/`) — auto-loaded by AI agents when the project is opened, ideal for project-specific or framework-specific skills (this is where the 15 HyperFrames skills live)
  - Workspace-scoped (`skills/`) — manually referenced, useful for reusable third-party or custom skills like a video-analyzer skill for competitor research
- **Prompts ≠ Recipes ≠ Memory:**
  - Prompts are reusable *starting points* (templates to fill in)
  - Recipes are proven *workflows* (step-by-step sequences that produce known good outputs)
  - Memory is the *historical log* (what we did and why, ordered by time)
- **Competitor analysis is a use case worth investing in early.** Studying what works in the wild is faster than guessing — Hugo has a video-analyzer skill incoming that will plug into the workflow.

### Decisions
- Saved all five starter prompt templates with explicit `[bracket]` placeholders so they're impossible to use without filling in specifics
- Recipes folder starts empty (with template + README) — we only add recipes after a workflow has been proven 2–3 times
- Scheduled reflection runs Sundays at 6pm local time (cron: `0 18 * * 0`) — chosen so the new week starts Monday with clarity
- The reflection task only writes a "Weekly Review" header at the top — never deletes prior session entries (history matters)

### Open questions / next steps
- [ ] Install Hugo's incoming video-analyzer skill into `skills/` and document it
- [ ] First competitor analysis as a real test of the prompt + skill combo
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`) — still from session 001
- [ ] Get OpenAI API key and add to `.env` — still from session 001
- [ ] Get HeyGen API key and add to `.env` — still from session 001

---

## Session 001 — 2026-05-23 — Initial workspace setup

### What we did
- Created `~/Desktop/hyperframes/` as the workspace root
- Upgraded Node from v20.11.0 → v22.22.3 via Homebrew (`brew install node@22`)
  - Needed a manual PATH override in `~/.zshrc` because an older Node install was winning the PATH fight: `export PATH="/opt/homebrew/opt/node@22/bin:$PATH"`
- Cloned three reference repos:
  - `main-source/hyperframes/` — official HyperFrames source (heygen-com/hyperframes, 18.6k stars, ~122MB without LFS)
  - `examples/launch-video/` — HeyGen's actual launch video (~256MB)
  - `examples/student-kit/` — Nate Herkai's 12-project teaching kit with GSAP (~560MB)
- Initialized a starter project at `my-projects/starter/` via `npx hyperframes init`
- Installed all 15 HyperFrames AI skills into `my-projects/starter/.agents/skills/`
- Created folder structure: `assets/{audio,video,images,fonts}`, `brand/`, `scripts/`
- Created supporting files: `README.md`, this `memory.md`, `.env.example`, `.gitignore`, `brand/brand-kit.md`

### What we learned
- **HyperFrames is "video as code"** — write HTML/CSS/JS, render to MP4. Same input = same output (deterministic). Built for AI agents to generate compositions because they're already fluent in HTML.
- **Why HyperFrames over Remotion:** Apache 2.0 open source (no per-render fees, no seat caps), pure HTML (no React build step), and library-clock animations like GSAP are seekable/frame-accurate.
- **The 15 skills cover everything:** main hyperframes, CLI, media preprocessing (TTS via Kokoro, Whisper transcription, background removal via u2net), animation runtimes (GSAP, Anime.js, CSS, Lottie, Three.js, WAAPI), and conversion helpers (Remotion-to-HF, website-to-HF).
- **The catalog has 50+ pre-built blocks** — `npx hyperframes add data-chart`, `flash-through-white`, `instagram-follow`, etc. Don't build from scratch what already exists.
- **Sandbox limitation:** Claude's sandboxed shell can't run `git clone` directly into the macOS Desktop mount because git's atomic file locking doesn't work over the bridge. Workaround: clone in sandbox `/tmp`, then `cp -R` to Desktop.

### Decisions
- Skipped Git LFS on the main repo (saved ~240MB of test baseline `.mp4` files we don't need for reference)
- Kept all three repos at `--depth 1` (latest commit only) to save space and time
- Brand kit set to modern default — will customize when Hugo has specifics
- HeyGen will be used for AI avatars + template videos (decide exact workflows once we start making content)
- Image model: OpenAI GPT Image 2.0 (will look up current API docs when we wire it up; not in Claude's May 2025 training data)

### Open questions / next steps
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`)
- [ ] Get OpenAI API key and add to `.env`
- [ ] Get HeyGen API key and add to `.env`
- [ ] Customize `brand/brand-kit.md` with Hugo's actual colors, fonts, and voice
- [ ] Pick the first real project to build (suggestions: animated chart from a CSV, or a 15-second product intro)
- [ ] Decide on a naming convention for projects in `my-projects/` (e.g., `YYYY-MM-DD-project-name`?)

---

<!-- Add new sessions ABOVE this line. Format:
## Session NNN — YYYY-MM-DD — One-line summary
### What we did
### What we learned
### Decisions
### Open questions / next steps
-->
