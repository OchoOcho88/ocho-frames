# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## Weekly Review — 2026-05-24 (week of 2026-05-18)

### Highlights
- **Workspace went from zero to fully scaffolded in a week.** Created `~/Desktop/hyperframes/`, upgraded Node to v22, cloned the three reference repos (official HyperFrames source, HeyGen launch video, Nate Herkai's 12-project student kit), spun up a starter project, and installed all 15 HyperFrames AI skills into `.agents/skills/`.
- **Got everything under version control and pushed to GitHub** — `OchoOcho88/ocho-frames` (private), first commit at 197 files / 2.7MB. Added a `setup.sh` so future clones can restore the ~940MB of `.gitignore`'d reference repos.
- **Built the organizational layer on top of the code** — added top-level `prompts/`, `recipes/`, and `skills/` folders with starter content, clear READMEs, and a documented distinction between project-scoped vs. workspace-scoped skills.
- **Set up automated institutional memory** — scheduled this weekly reflection task so the workspace gets reviewed every Sunday at 6pm without anyone having to remember to do it.

### Patterns I noticed
- **Local environment friction keeps showing up.** First the Node PATH fight (older Node winning over the new v22 install, needing a manual `~/.zshrc` override), then the sandboxed shell's inability to `git clone` directly into the Desktop mount. Tooling that touches macOS bridges/mounts needs a workaround mindset, not a "should just work" assumption.
- **API keys are the biggest unblocking dependency.** Three keys (OpenAI, HeyGen, soon Gemini) have been on the open-questions list across both sessions. Nothing real can be tested end-to-end until at least the first two are in place.
- **Conscious structure for AI-agent use.** Every choice this week — auto-loaded skills, bracketed prompt placeholders that force specificity, prompts vs. recipes vs. memory separation — was made with the assumption that an AI agent (not just a human) would be reading and using these files.

### Skills / knowledge gained
- HyperFrames is "video as code": HTML/CSS/JS rendered to MP4, deterministic, Apache 2.0 (no per-render fees, no seat caps), and frame-accurate seekable for libraries like GSAP — clear win over Remotion for AI-driven video work.
- The 15-skill HyperFrames ecosystem covers main + CLI + media preprocessing (Kokoro TTS, Whisper, u2net) + animation runtimes (GSAP, Anime.js, CSS, Lottie, Three.js, WAAPI) + conversion helpers.
- The catalog has 50+ pre-built blocks via `npx hyperframes add <block>` — checking the catalog first is faster than building from scratch.
- Skill scoping has two distinct modes: project-scoped (`<project>/.agents/skills/`, auto-loaded) vs. workspace-scoped (`skills/`, manually referenced).
- GitHub Pages is free only on public repos — keeping `ocho-frames` private + using Pages requires GitHub Pro ($4/mo) or flipping the repo to public when sharing.
- Sandbox workaround for git: clone to `/tmp` first, then `cp -R` to Desktop mounts.

### Open questions still unresolved
From Session 001:
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`)
- [ ] Get OpenAI API key and add to `.env`
- [ ] Get HeyGen API key and add to `.env`
- [ ] Customize `brand/brand-kit.md` with Hugo's actual colors, fonts, and voice
- [ ] Pick the first real project to build (animated chart from a CSV, or a 15-second product intro)
- [ ] Decide on a naming convention for projects in `my-projects/` (e.g., `YYYY-MM-DD-project-name`?)

From Session 002:
- [ ] Install Hugo's incoming video-analyzer skill into `skills/` and document it
- [ ] First competitor analysis as a real test of the prompt + skill combo
- [ ] Get Gemini API key once we install the video-analyzer skill
- [ ] Decide repo visibility for Pages (public flip vs. GitHub Pro)
- [ ] Enable Pages in repo Settings → Pages once the visibility decision is made

### Suggested focus for next week
1. **Unblock the workspace by collecting API keys.** OpenAI and HeyGen first — those two alone unlock the ability to actually test the starter project end-to-end. Until that happens, every other build task is theoretical.
2. **Install the video-analyzer skill and run the first real competitor analysis.** This is the proof that the prompt + skill + recipe framework delivers value, not just structure. It also feeds back into what HyperFrames work to prioritize.
3. **Customize the brand kit before producing any real videos.** Modern defaults are fine as a placeholder, but anything shipped this week with the default kit will need redoing later.

---

## Session 003 — 2026-05-25 — video-analyzer skill installed, Gemini API key live

### What we did
- **Installed the video-analyzer Claude Code skill** at `~/.claude/skills/video-analyzer/` (from https://github.com/mikefutia/claude-vision by Mike Futia, MIT license)
  - Uses Gemini's vision API to "watch" videos and return structured markdown reports
  - Strong anti-hallucination guardrails (won't invent narrators/voiceovers)
  - 220KB skill, single Python script (`scripts/analyze_video.py`)
- **Installed Python dependency:** `google-genai` 1.47.0 via `pip3 install google-genai` (no `--break-system-packages` needed because Hugo's pip is old enough not to enforce PEP 668)
- **Created Gemini API key** on Google AI Studio, scoped to a new project called "Hyperframes" so usage/billing stays separated from other projects
- **Set `GEMINI_API_KEY` in `~/.zshrc`** — system-wide shell env var, available in every Terminal session
- **Verified no conflict with Altarize project:** Altarize Active Campaign (`~/Desktop/OrbitAll/Altarize Active Campaign`) uses ActiveCampaign, Railway, Supabase, Metabase, Claude, Resend, Perplexity — but NOT Gemini. Zero risk of the new hyperframes key being picked up by Altarize.
- **Documented the install in `skills/video-analyzer/README.md`** — the workspace has a pointer doc even though the actual skill lives outside the workspace (at `~/.claude/skills/`)
- **Updated `setup.sh`** to install the video-analyzer skill + google-genai automatically on fresh clones
- **Added `outputs/` folder** at workspace root for everything the AI/pipeline produces (vs `scripts/` which is for inputs):
  - `outputs/video-analyses/` — markdown reports from video-analyzer (tracked in git, builds a competitive intel library over time)
  - `outputs/downloads/` — competitor videos (gitignored — copyright + size)
  - `outputs/generated-images/` — AI image generations (gitignored)
  - `outputs/voiceovers/` — AI narration audio (gitignored)
  - Updated `prompts/competitor-analysis.md` to route output to `outputs/video-analyses/` instead of `scripts/`
  - Updated `README.md` to document the inputs-vs-outputs distinction

### What we learned
- **Two ways to manage API keys, each appropriate for different things:**
  - **Shell env var (`~/.zshrc`):** system-wide, always-on. Good for tools that expect env vars (like the video-analyzer skill). Bad for project-scoped secrets — anything else on your Mac can read it.
  - **Project `.env` file:** project-scoped, loaded on demand via `python-dotenv` (`load_dotenv()`) or `dotenv.config()` in Node. Good for keeping projects isolated. Standard best practice.
- **`load_dotenv()` default is NOT override.** By default, if the shell already has `MY_VAR` set, `load_dotenv()` will NOT replace it with the `.env` value. To force `.env` to win, use `load_dotenv(override=True)`. This is a subtle conflict source — flagged so future Altarize work (or any project adding `GEMINI_API_KEY` to its `.env`) doesn't get the wrong key.
- **Claude Code skills live at `~/.claude/skills/`**, separate from workspace `skills/` and project `.agents/skills/`. Three scopes:
  - **Cowork Personal skills** (Customize panel in Cowork) — across all Cowork sessions
  - **Claude Code skills** (`~/.claude/skills/`) — across all Claude Code sessions
  - **Workspace skills** (`~/Desktop/hyperframes/skills/`) — only when working in this workspace
  - **Project skills** (`<project>/.agents/skills/`) — only inside that project
- **Pip 21.x is OLD** but works fine for our purposes. Decided NOT to upgrade Python via Homebrew right now to avoid mid-flow disruption. Worth doing later as its own focused task: `brew install python@3.13` + reinstall google-genai for the new Python.
- **Gemini free tier limits:** 15 requests/min, 1,500 requests/day. Plenty for personal use.

### Decisions
- **Did NOT upgrade Python via Homebrew this session** — added to open questions for later. Reasoning: validating skill works on current setup first, then doing clean upgrade as its own session.
- **Did NOT touch Altarize's `load_dotenv()` calls** to add `override=True` — only an issue IF Altarize ever adds `GEMINI_API_KEY` to its `.env`, which it currently doesn't. Documented in open questions in case it ever does.
- **Skill installed at `~/.claude/skills/` (NOT in workspace `skills/`)** — required by the skill's hardcoded path. Workspace `skills/video-analyzer/README.md` is a pointer doc only.
- **Created separate Google AI Studio project** ("Hyperframes") for the new key so usage/billing tracks separately from the existing "Altarize analysis" project.

### Open questions / next steps
- [ ] **First test of video-analyzer skill** — pick a video file, run end-to-end, validate the output (this is the first thing for session 004)
- [ ] First competitor analysis using `prompts/competitor-analysis.md` + the new skill
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`) — still from session 001
- [ ] Get OpenAI API key and add to `.env` — still from session 001
- [ ] Get HeyGen API key and add to `.env` — still from session 001
- [ ] Find out where the "Altarize analysis" Gemini key (from Mar 2026) is actually being used — might be `~/Desktop/Altarize-Content-Pipeline/`, `~/Desktop/Altarize-Landscape-Analysis/`, or `~/Documents/Claude/Projects/Altarize Active Campaign/`. Not blocking — just curiosity.
- [ ] Upgrade Python via Homebrew (`brew install python@3.13`) once video-analyzer is validated working. Includes reinstalling google-genai for the new Python.
- [ ] If future Altarize work adds `GEMINI_API_KEY` to its `.env`, change `load_dotenv()` → `load_dotenv(override=True)` in all `tools/*.py` files
- [ ] Decide repo visibility for GitHub Pages (private requires Pro; public is free) — still from session 002
- [ ] Enable Pages in repo Settings → Pages once visibility decision is made — still from session 002

---

## Session 002 — 2026-05-23 — Framework additions + GitHub repo live

### What we did
- Added three new top-level folders to the workspace:
  - `prompts/` — reusable prompt templates with starter content for CSV→chart, PDF→summary, TikTok hook, product intro, and competitor analysis
  - `recipes/` — workflows we've proven and want to repeat, with a `_template.md` to copy from
  - `skills/` — workspace-level custom skills (different from the project-scoped `.agents/skills/`)
- Scheduled a weekly memory reflection task: every Sunday at 6pm, Claude reads `memory.md`, writes a "Weekly Review" section at the top, identifies patterns, and cleans up resolved open questions
- Documented the distinction between project-scoped vs workspace-scoped skills in `skills/README.md`
- Added `GEMINI_API_KEY` slot to `.env.example` for the incoming video-analyzer skill (uses Gemini Vision because Claude can't natively watch video yet)
- **Initialized git, made first commit (197 files, 2.7MB), pushed to GitHub at https://github.com/OchoOcho88/ocho-frames (private repo)**
- Created `setup.sh` so future clones can restore the ~940MB of reference repos that are excluded via `.gitignore`
- Added Contributing section to README + `index.html` + `docs/PAGES_SETUP.md` for when we enable GitHub Pages

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
- [ ] Get Gemini API key once we install the video-analyzer skill
- [ ] **Decide repo visibility for Pages:** GitHub Pages only works free on PUBLIC repos. To enable Pages on the current private repo, either (a) flip the repo to public when ready to share, or (b) upgrade to GitHub Pro ($4/mo)
- [ ] Enable Pages in repo Settings → Pages once the visibility decision is made (see `docs/PAGES_SETUP.md`)

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
