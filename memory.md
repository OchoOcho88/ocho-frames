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
- [ ] Customize `brand/agency-brand-kit.md` with Hugo's actual colors, fonts, and voice
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

## Session 004 — 2026-05-26 — First successful video-analyzer run (+ Python 3.9 fix)

### What we did
- **Ran the video-analyzer skill end-to-end for the first time** — the open item flagged "first thing for session 004" in Session 003. Analyzed `examples/student-kit/video-projects/linear-promo-30s/final.mp4` (the Linear 30s promo from Nate Herkai's student kit).
- **Saved the report** to `outputs/video-analyses/student-kit-linear-promo-30s-2026-05-26.md` and prepended a small provenance header (source / date / tool / model) so each file in the competitive-intel library is self-documenting going forward.
- **Hit and fixed a Python-version blocker** before it could run (see below).

### What we learned
- **The skill is `disable-model-invocation: true`** — it is NOT in the Skill-tool list and can't be auto-invoked. You run it by calling the script directly: `python3 ~/.claude/skills/video-analyzer/scripts/analyze_video.py <video> [--prompt …] [--fps N] [--model …]`. Report → stdout, progress → stderr.
- **This Mac only has system Python 3.9.6** — no 3.10/3.11/3.12/3.13 anywhere on PATH, and `google-genai` (1.47.0) is installed only for 3.9. So the Homebrew upgrade deferred in Session 003 is still pending, and 3.9 is what we have to run on.
- **The script was incompatible with 3.9 out of the box.** It uses PEP-604 `float | None` annotations (lines for `build_video_part` / `analyze`) with no `from __future__ import annotations`, so 3.9 raised `TypeError` at function-definition time — before any upload. SKILL.md claims "Python 3.10+", which is why this surfaced.
- **The default model `gemini-3-flash-preview` works.** 2.9MB file → inline upload path (≤18MB). Two benign noises in stderr: the Python-3.9-EOL `FutureWarning` and a `thought_signature` "non-text parts" warning — text still returned cleanly.
- **Report quality was good and honest** — all 5 sections, accurate `MM:SS` scene breakdown, verbatim on-screen text, and it correctly reported "No speech detected / cinematic music + whooshes" instead of inventing a narrator (the anti-hallucination guardrails held).

### Decisions
- **Fixed the installed skill in place** by adding `from __future__ import annotations` to `~/.claude/skills/video-analyzer/scripts/analyze_video.py` (one line, behavior-preserving, works on 3.9 AND 3.10+). Chose this over a throwaway `/tmp` copy so the validation reflects the real skill and every future run on this machine just works.
- Used the skill's **default prompt and default model** for this first run (no `--prompt`/`--fps`/`--model` overrides) — wanted a clean baseline of stock behavior.

### Open questions / next steps
- [ ] **The `from __future__` fix is local-only and `setup.sh` will lose it.** `setup.sh` re-clones the skill from upstream (mikefutia/claude-vision) on fresh machines, which does NOT have the fix → a fresh clone on a 3.9 box will hit the same `TypeError`. Either (a) PR the one-liner upstream, or (b) have `setup.sh` re-apply it after install, or (c) just upgrade Python to 3.10+ (makes the shim unnecessary, though harmless to keep).
- [ ] **First *real competitor* analysis still untested.** This run was a student-kit teaching asset, not a competitor, and used the script directly — `prompts/competitor-analysis.md` (which routes output to `outputs/video-analyses/`) hasn't been exercised yet.
- [ ] Upgrade Python via Homebrew (`brew install python@3.13`) + reinstall google-genai for it — still from Session 003; would retire the 3.9 shim need.
- [ ] Carry-over from prior sessions: OpenAI + HeyGen keys, verify starter project `npm install && npm run dev`, brand-kit customization, repo-visibility/Pages decision.

### Session 004 addendum — architectural pivot (later in the same session)

After the test passed, Hugo shared the real end goal — this isn't a "competitor analyzer," it's a **creative-strategy pipeline**: ingest competitor content (video OR static) → extract patterns → synthesize a brief adapted to a *client's* brand → output production-ready prompts for AI media platforms (Seadance for video, ChatGPT Image 2.0 for static). That reframe changed the rest of the session from "run the test" to "design the pipeline."

**What we did (addendum):**
- Reviewed a YouTuber's 12-section marketing-conversion framework (Format / Hook / Audience / Pain / Angle / Product Intro / Proof / Beat-by-Beat / CTA / What Works / What's Weak / Steal-Worthy Patterns) — strictly better than the workspace's prior 7-section creative-pattern prompt for ad analysis.
- **Rewrote `prompts/competitor-analysis.md`** from a 7-section human-fill-in template into a 12-section `--prompt-file`-ready prompt. Folded the OLD prompt's visual-craft and audio-craft elements into Section 1 of the new one so the creative lens isn't lost. Added a "Critical rules" block (verbatim quotes, no invented narrators, label inferences, N/A allowed).
- **Updated `recipes/analyze-video-with-gemini.md`** Variations section with a real bash invocation for `--prompt-file prompts/competitor-analysis.md` (replaced the "still open" placeholder).
- **Wrote `docs/pipeline-architecture.md`** — the new source of truth for the full 5-stage pipeline. Locks decisions and lists open questions per stage.

**What we learned (addendum):**
- **Default 5-section skill output ≠ marketing analysis.** The YouTuber's 12-section output is a custom prompt, not the skill default. Two different lenses on the same video: default = "describe what's there"; custom = "explain why it converts." For ads work, marketing-conversion is the right lens.
- **The "What's next?" closing offer is a great UX pattern.** YouTuber's outputs end with offered next-steps. Generalizing this into a Stage 5 pipeline convention so every stage ends with offered next moves the user picks from.
- **The competitor-analysis workflow has 5 stages, not 1.** Stage 0 client brief → Stage 1 ingestion → Stage 2 pattern extraction (current 12-section prompt) → Stage 3 strategic synthesis → Stage 4 platform-specific production prompts. Only Stage 2 (for video) is built today.

**Decisions locked (addendum) — 4 pipeline-architecture decisions, all documented in `docs/pipeline-architecture.md`:**
1. **Client context lives in per-project brief files** at `projects/<client>/brief.md` (new top-level `projects/` folder, sibling of `my-projects/`).
2. **Static image analysis gets a sibling image-analyzer skill** — deferred to Session 005 for build.
3. **Pipeline shape: modular stages with "What's Next?" handoffs.** Stage 2 always runs; Stages 3-4 are user-triggered from offered options.
4. **Primary AI media platforms: Seadance (video) + ChatGPT Image 2.0 (static).** Runway / Higgsfield deferred but listed for future expansion.
5. **Stopped at architecture for Session 004** rather than start building Stages 0/3/4. The pivot was significant enough that locking the plan in writing > rushing into half-built scaffolding. Session 005 starts from a clean architectural map.

**Open questions / next steps (Session 005 entry point):**

Pipeline build queue:
- [ ] **Stage 0 — Set up `projects/` folder + `_template/brief.md`.** Smallest blocking dependency for everything else. Convention documented in `docs/pipeline-architecture.md`.
- [ ] **Stage 5 first half — add "What's Next?" closing block** to `prompts/competitor-analysis.md` so analysis outputs end with offered next moves.
- [ ] **End-to-end smoke test** — pick a real client, drop a competitor video into the project folder, run Stage 2 with the new 12-section prompt, validate the whole flow works. **(Supersedes the "first real competitor analysis still untested" item from earlier in this entry.)**
- [ ] **Research Seadance + ChatGPT Image 2.0 current prompt formats** before writing Stage 4 prompts. Their formats have evolved — old templates won't work.
- [ ] **Write Stage 3** (`prompts/synthesis-creative-brief.md`). Takes client brief + analyses → produces adapted creative direction.
- [ ] **Write Stage 4 prompts** (`prompts/production-seadance.md` + `prompts/production-chatgpt-image.md`). Each takes the synthesis brief → outputs a paste-ready platform prompt.
- [ ] **Add image-analyzer skill** for static-image competitor analysis (Stage 1 second path). Standalone build — likely its own session.

Per-stage design questions (full list in `docs/pipeline-architecture.md`):
- Stage 0: free-form vs. strictly structured `brief.md`? One per client or one per *campaign*?
- Stage 1: image-analyzer via Gemini API (script) vs. Claude native vision (chat-only)?
- Stage 3: single synthesis output vs. multiple creative directions?
- Stage 4: character-count caps for Seadance? Batch variations for A/B testing?
- Stage 5: hardcoded offers per stage vs. dynamically generated from prior output?

### Session 004 second addendum — Devil's Advocate pass + Stage 0 built + Sportif onboarded

After the architecture was documented, ran a Devil's Advocate pass (using the installed skill) to pressure-test the plan before committing more to it. Seven challenges raised. Five led to material changes; two held up (one we kept, one was minor).

**Devil's Advocate outcomes:**

| Challenge | Outcome |
|---|---|
| 1: Building scaffolding for clients you don't have yet? | **Resolved by reality:** Hugo HAS a real client — **Sportif**, fitness accessories, brand new company, launching September 2026. Needs brand identity, brand kit, and launch content for Instagram, TikTok, Facebook. No content or brand kit yet. Concrete deadline (~4 months) reshaped priorities. |
| 2: Is competitor-first pipeline ordering backwards? | **Pipeline now supports two modes:** brand-first (established clients) and competitor-first (net-new launches like Sportif). Picked per client, documented in client README. |
| 3: Stage 0 over-engineered for actual needs? | **Simplified.** Combined brand-kit + brand-identity into ONE `brand.md` file. Template now ~6 meaningful files instead of 12. Grow as needed. |
| 4: Platform lock-in to Seadance + ChatGPT Image is fragile? | **Adopted platform-agnostic structure.** Stage 4 split into `prompts/production-brief.md` (platform-agnostic intermediate format) + thin platform adapters at `prompts/adapters/<platform>.md`. Adapters can swap without touching the brief format. |
| 5: No quality-control / review checkpoint? | **Added Stage 5: Review & Iterate** as a real stage in the architecture. Feedback maps to a specific upstream stage and re-runs that stage. Per-campaign review notes file. |
| 6: Two-Claude workflow is more overhead than value? | **Kept by Hugo's choice** — he's used the pattern before successfully, and needs an explainer (Cowork advisor) for what Opus is producing in VS Code while he learns. Net positive for his learning curve. |
| 7: `projects/` vs. `my-projects/` collision waiting to happen? | **Renamed both:** `my-projects/` → `compositions/`, `projects/` → `clients/`. Updated 16 references across 12 files. |

**New: Pre-Stage 0 intake layer.** Hugo asked for a questionnaire he can email Sportif to gather brand intake data, plus a SWOT analysis template (with research-helper prompt) for his own strategic read. Built both. The questionnaire is what the client says; the SWOT is what Hugo concludes as the expert. Together they feed `brand.md`.

**What we built (advisor session, one-off exception to Opus-writes pattern):**

- **Renamed `my-projects/` → `compositions/`** (preserved content). Updated `setup.sh`, all READMEs, all prompts referencing the old path.
- **`clients/README.md`** — top-level explanation of the clients/ folder convention.
- **`clients/_template/`** with:
  - `README.md` — onboarding sequence for new clients
  - `brand.md` — combined brand kit + identity skeleton
  - `intake/questionnaire.md` — 10-question email-ready intake (~30 min for client to complete)
  - `intake/swot-analysis.md` — SWOT template with Sportif-style research-helper prompt
  - `products/_template-product.md` — one-per-SKU product skeleton
  - `campaigns/`, `competitor-analyses/`, `_archive/`, `assets/` empty folders with `.gitkeep`
- **`clients/sportif/`** populated as the first real client:
  - `README.md` — engagement status + onboarding checklist
  - `brand.md` — skeleton with known facts (name, category, launch date, platforms) + TBD fields tagged to questionnaire question numbers
  - `intake/questionnaire.md` — Sportif-customized, ready to email (placeholders for founder name + deadline)
  - `intake/swot-analysis.md` — Sportif-customized with research-helper prompt pre-filled for fitness accessories DTC, Sept 2026, Instagram/TikTok/Facebook
- **`docs/pipeline-architecture.md`** rewritten end-to-end to reflect all revised decisions: two modes, Pre-Stage-0 intake layer, simplified Stage 0, platform-agnostic Stage 4 with adapters, new Stage 5 Review & Iterate, renumbered Stage 6 "What's Next?" offer.
- **`.gitignore`** updated: `my-projects/` → `compositions/` reference fix, plus `clients/*/assets/*` ignored except `.gitkeep` and `.md` files (so client binary assets like logos/fonts don't bloat the repo).

**Decisions locked in this addendum:**
- **Folder rename:** `my-projects/` → `compositions/`, `projects/` (planned) → `clients/` (built).
- **Two pipeline modes:** brand-first vs competitor-first, chosen per client.
- **Simplified Stage 0:** combined `brand.md`, minimal starter, grow as needed.
- **Platform-agnostic Stage 4:** production-brief + thin adapters.
- **New Stage 5:** Review & Iterate.
- **Pre-Stage-0 intake layer** added (questionnaire + SWOT).
- **Sportif is the first real client.** Engagement at intake stage. Questionnaire ready to email.
- **One-off exception confirmed:** advisor built Stage 0 because hot context outweighed pattern purity. Resume Opus-writes from Session 005.

**Open questions / next steps (Session 005 entry point — revised):**

Sportif-driven:
- [ ] Customize Sportif's questionnaire (founder name, deadline date) and email it.
- [ ] Run the SWOT research-helper prompt (it's pre-filled — just paste into Claude). Populate Sportif's SWOT Opportunities + Threats from the research output.
- [ ] When questionnaire returns, populate `clients/sportif/brand.md` from answers + SWOT conclusions.

Pipeline build (in priority order):
- [ ] Add "What's Next?" closing block to `prompts/competitor-analysis.md` (Stage 6 — cheap, immediately useful).
- [ ] End-to-end smoke test with a real fitness-accessory competitor video for Sportif, save to `clients/sportif/competitor-analyses/`.
- [ ] Research Seadance + ChatGPT Image 2.0 current prompt formats (Stage 4 prerequisite).
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3, mode-aware).
- [ ] Write `prompts/production-brief.md` + first adapter (Seadance OR ChatGPT Image — pick whichever Sportif needs first).
- [ ] Add image-analyzer skill for static-image analysis (Stage 1 second path).

Carry-over:
- [ ] `from __future__` shim resilience (still applies — fresh clone via `setup.sh` loses it).
- [ ] Python 3.10+ upgrade via Homebrew — would retire the shim need.
- [ ] OpenAI + HeyGen keys + brand-kit customization + repo-visibility decision (from prior sessions).
- [x] ~~Rename `brand/brand-kit.md` to `brand/agency-brand-kit.md`~~ DONE (Session 004 cleanup). Path references updated across docs, prompts, and this file.

### Session 004 third addendum — voice rules + agency identity + Sportif onboarding email fully ready

The longest session yet. After Stage 0 was built, focus shifted from architecture to operationalizing the first real client engagement (Sportif) end-to-end. By session close, the entire onboarding email is ready to send to Lucy (the Sportif founder).

**What we did (third addendum):**

Voice and identity:
- **Locked a no-em-dash rule** as a hard, non-negotiable workspace voice rule. Em dashes are an AI tell and violate the friendly-professional-to-the-point voice. Documented in `brand/agency-brand-kit.md` with explicit punctuation substitutes (period, comma, colon, parens). The rule applies to ALL workspace copy: client emails, prompts, generated content, docs.
- **Locked agency identity:** Ochoproductions, domain ochoproductions.com, owner Hugo, contact hugo@ochoproductions.com. Captured in `brand/agency-brand-kit.md`. Logo, landing page, brand colors, typography all explicitly marked TBD (modern defaults are placeholders).
- **Renamed `brand/brand-kit.md` → `brand/agency-brand-kit.md`** to disambiguate the agency's own brand kit from client brand kits (which live at `clients/<client>/brand.md`). Six other files updated with the new path.
- **Em-dash sweep across 13 high-priority files** (intake questionnaires, SWOTs, brand templates, READMEs, the competitor-analysis prompt, the agency brand kit). Initial mechanical sed pass created some awkward fragments which we then rewrote thoughtfully (em dashes serve four different grammatical jobs and need context-appropriate replacements, not one mechanical substitution).
- **Updated `prompts/competitor-analysis.md` Critical Rules** to include "No em dashes" as an explicit rule, so any analysis Claude generates from this prompt inherits the rule.

Sportif onboarding (the real deliverable of the session):
- **Added Q12 (Timeline & rollout)** to both questionnaires (Sportif and template). Covers timeline cadence (single launch drop vs build-up), platform rollout (parallel vs sequenced), and an explicit "open to discuss" option that signals Hugo has ideas. Q11 trimmed to remove the now-redundant Platforms line.
- **Pre-filled questionnaire signoff** with "Kind regards, Hugo, hugo@ochoproductions.com" in both Sportif and template versions.
- **Wrote a warm intro email** for Lucy referencing the mutual connection (Lauren). Frames the no-fee engagement honestly: real portfolio work + practice on a live launch in exchange for word-of-mouth referrals IF the work delivers. Capital-IF used deliberately to signal the referral is conditional on quality.
- **Merged the intro into the Sportif questionnaire file** so it now reads as the complete email body (greeting through signoff). The workspace meta block stays at the top, separated by `---`, as Hugo-facing send instructions.
- **Subject line recommended:** "Lauren put me in touch about Sportif". Lauren's name is the social proof that drives the open rate; Hugo's name is redundant (it's in the sender field).
- **Added a P.S.** about sending work samples in a follow-up email. Replaced the cliché "our only limit is our imagination" with "whatever you can picture, we can build it" (same meaning, less AI-tell-y, more confident).
- **Offered Lucy three answer formats:** type the answers, share a Google Doc, or send WhatsApp voice memos. Voice memos flagged as usually the fastest. This dramatically lowers her friction (speaking is faster than typing 30 minutes of answers).

**Decisions locked in this addendum:**
- **No em dashes** is a hard rule, applies workspace-wide, no exceptions in client-facing or AI-generated copy.
- **Agency name is "Ochoproductions"** (no space). Email is hugo@ochoproductions.com.
- **Questionnaires are 12 questions** (was 11, added timeline/rollout).
- **Voice memo option** is part of the standard intake offering for every client, not just Sportif.
- **Subject line convention** for warm intros: lead with the mutual connection's name.

**Sportif: where we are at session close:**
- `clients/sportif/intake/questionnaire.md` is the complete email body, copy-pasteable.
- Hugo needs to: customize "[Founder name]" line (replace with Lucy), confirm the deadline date, then send.
- After sending: run the SWOT research-helper prompt while waiting for Lucy's response.
- Send a follow-up email with work samples (referenced in the P.S.).

**Open questions / next steps (Session 005 entry point — updated):**

Sportif (active):
- [ ] **Send the Sportif intake email to Lucy.** Subject: "Lauren put me in touch about Sportif". Body is the merged file at `clients/sportif/intake/questionnaire.md`. Customize the founder name placeholder before sending.
- [ ] **Send Hugo's work samples** in a separate follow-up email (the P.S. promised this).
- [ ] **Run the SWOT research helper** for Sportif while Lucy is filling in her questionnaire. Prompt is pre-filled at the bottom of `clients/sportif/intake/swot-analysis.md`.
- [ ] **Populate `clients/sportif/brand.md`** from Lucy's responses + SWOT conclusions when intake is done.
- [ ] **Run first competitor analyses** on competitors Lucy names in Q4, save to `clients/sportif/competitor-analyses/`.

Pipeline build (Session 005 priority order):
- [ ] Add "What's Next?" closing block to `prompts/competitor-analysis.md` (Stage 6, cheap, immediately useful).
- [ ] Research Seadance + ChatGPT Image 2.0 current prompt formats (Stage 4 prerequisite).
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3, mode-aware).
- [ ] Write `prompts/production-brief.md` + first adapter (Seadance or ChatGPT Image, pick based on Sportif's first content need).
- [ ] Add image-analyzer skill for static-image competitor analysis (Stage 1 second path).
- [ ] Build a recipe for transcribing voice memos to questionnaire format (Whisper is already installed per Session 001). Will be needed when Lucy sends voice memos back.

Workspace housekeeping (Session 005 or later):
- [ ] Wider em-dash sweep: `docs/pipeline-architecture.md`, top-level `README.md`, older starter prompts (csv-to-chart, pdf-to-summary, etc.), recipes, skills READMEs. None are client-facing this week so not urgent.
- [ ] `from __future__` shim resilience (still applies on fresh clones).
- [ ] Python 3.10+ upgrade via Homebrew.
- [ ] OpenAI + HeyGen keys.
- [ ] Repo-visibility decision for GitHub Pages.

**Working pattern for Session 005:**
Resume Opus-writes from here (advisor mode does brainstorming and reviews only). Cowork session opens with the Opus startup prompt that briefs Opus on the current state and the top priority.

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
- Created supporting files: `README.md`, this `memory.md`, `.env.example`, `.gitignore`, `brand/agency-brand-kit.md`

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
- [ ] Customize `brand/agency-brand-kit.md` with Hugo's actual colors, fonts, and voice
- [ ] Pick the first real project to build (suggestions: animated chart from a CSV, or a 15-second product intro)
- [ ] Decide on a naming convention for projects in `my-projects/` (e.g., `YYYY-MM-DD-project-name`?)

---

## Session 005 — 2026-05-28 to 2026-05-29 — Sportif onboarding fired, marketing fundamentals doc, Perplexity integration, post-Lucy trigger system

The longest session so far. The Sportif intake email went out, the Perplexity API got wired into the workspace, and the agency-wide marketing knowledge base was written. Two new auto-memory entries created in the memory directory so future Claude sessions auto-load Sportif context and the "Lucy responded" trigger.

### What we did

**Sportif intake fired (2026-05-28).**
- Confirmed the questionnaire at `clients/sportif/intake/questionnaire.md` was effectively ready (Lucy in greeting, signoff set, no bracketed placeholders left).
- Hugo sent the intake email to Lucy with subject "Lauren put me in touch about Sportif". Decision: kept the deadline open-ended ("at your earliest convenience so we stay on track for September") to match the no-fee/favor framing rather than create a transactional feel.
- Lucy responded same-day confirming she'll return answers in ~5 days. Expected return: ~2026-06-03.

**SWOT research and synthesis (Opportunities + Threats populated).**
- Ran 9 WebSearch queries: category dynamics, top brands, underserved segments, DTC failures, regulatory restrictions, Bala content strategy, insurgent brands, Pilates trend, Bala competitors.
- Wrote 8 Opportunities into `swot-analysis.md` (Pilates as cultural tailwind topping fitness charts three years running, the vanity-to-sanity positioning gap, underserved older-adult and women-specific niches, the Bala design-led playbook proven to work without paid ads for years, FitTok format alignment with accessories, sustainability as a real purchase signal in this category, clean-slate launch advantage).
- Wrote 10 Threats with the heaviest emphasis on the 2026 Meta/TikTok ad enforcement changes, paid-acquisition CPM inflation (Meta CPM up from $34 in 2021 to $57 in 2024), undercapitalization killing 45% of failed DTC brands, Amazon dupes destroying margins on commoditizable accessories, channel concentration risk across Meta/TikTok, and rising body-image backlash.
- Added 23 source links grouped by research bucket so every claim is traceable.
- Wrote a preliminary Strategic Synthesis (3 priorities, initially 4 then 5 don'ts, 4 ninety-day hypotheses) flagged as pre-questionnaire and to be hardened once Lucy responds.

**Critical nuance found on the Meta restriction (mid-session pivot).**
- Initial threat #1 read "Meta restricts fitness/wellness brands from optimizing on lower-funnel events and flags audiences whose metadata implies sensitive traits."
- Hugo asked for deeper explanation. WebFetched the AuditSocials and Accelerated Digital Media sources directly. Discovered the trigger is claim-making language, NOT product category. "Fitness accessories" is NOT automatically in Meta's Restricted Health and Wellness bucket. It enters that bucket only if the brand makes a specific health-outcome claim ("improves cardiovascular performance," "burns X calories," "reduces soreness by Y%").
- Rewrote threat #1 with the nuance, added "no specific health-outcome claims in product copy or ads" as a fifth do-not-do rule. Reframed the threat as a creative-positioning lever Sportif controls, not a fixed external constraint. This is now a hard rule across all Sportif creative.

**Built `clients/sportif/intake/swot-summary.md` as a pullable distillation.**
- Self-contained (jargon cheat sheet baked in for DTC, FitTok, UGC, CPM, CAGR, SKU, ACSM, lookalike audience, lower-funnel events, pre-launch waitlist).
- Headline takeaway in one sentence at the top.
- Top 3 opportunities, top 3 threats, 3 strategic priorities, 5 don'ts, hypotheses.
- Cross-link footer pointing back to the full SWOT, questionnaire, brand.md skeleton, and architecture doc.
- Designed for two uses: Hugo can pull it out as a screenshotable artifact, and future Claude sessions can use it as a quick reference without loading the full SWOT.

**Locked in: Sportif is Australian.**
- During the marketing-fundamentals doc scoping, Hugo confirmed Sportif is an Australian business. Previously the SWOT placeholder said "[TBD: assume UK/US until told otherwise]".
- Saved as auto-memory at `~/.claude/projects/-Users-hugobrizuela-Desktop-hyperframes/memory/sportif-australia.md` (first project auto-memory created in this workspace). Future Claude sessions will auto-load this context.
- Implications captured: AUD-denominated benchmarks, AEST/AEDT timing, the Australian fitness creator ecosystem (Kayla Itsines, Tammy Hembrow, Chloe Ting, Ashy Bines, Chontel Duncan, Lauren Simpson, plus TikTok's fastest-growing AU fitness creator Eddie Williams). Australian competitors to consider beyond what Lucy names: Tropeaka, Bondi Sands, Bared Footwear, Pillar Performance.

**Wrote `docs/marketing-fundamentals.md` (9,084 words, agency-wide knowledge base).**
- Scope confirmed via four scoping questions: thorough reference depth, Australia primary plus UK/US sections, AI stack woven through, one combined doc.
- 4 additional WebSearch queries for Australian Meta CPMs (~$9.80 AUD), Australian TikTok CPMs (~$4-10 AUD with Health & Fitness as the cheapest vertical at ~$6.50), Australian fitness creators by tier with AUD rates, and email tool comparison (Klaviyo wins for ecom at 3.8x revenue per subscriber vs Mailchimp).
- Nine parts: lay of the land (the five channels, the funnel, the flywheel, what changed since 2021), paid ads platform-by-platform (Meta auction mechanics, account structure, targeting, formats, the Restricted Health and Wellness trap recap; TikTok Spark Ads with AU benchmarks; brief Google and YouTube coverage), organic content per platform (Instagram Reels-first, TikTok FYP mechanics, the truth about FB organic, YouTube Shorts vs long-form, the repurposing system), email (why post-iOS-14 it's the most reliable channel, the five core flows, Klaviyo vs Mailchimp vs ConvertKit vs Beehiiv with AUD pricing, deliverability basics), creators (the four tiers with AU follower bands and rates, terminology decoded, top AU fitness creators by name, briefing template, compensation models, AI stack integration), metrics stack (all acronyms defined in one table, attribution challenges since iOS 14, post-purchase surveys as the affordable attribution layer, MER as the integrating metric), campaign structure (pre-launch/launch/sustain phasing), Sportif applied blueprint (four phases mapped to dates from now to September to year-end, KPIs per phase, three budget bands lean $5-10K/mid $15-30K/scale $50K+ AUD for launch month, channel-mix table across phases, AI stack integration per phase, risk register), and staying current (newsletters, podcasts, operators, signals your playbook needs updating).
- Zero em dashes (voice rule maintained throughout). Word count 9,084.

**Perplexity integration set up.**
- Honest discussion of Perplexity vs WebSearch tradeoffs. Decision: don't re-run SWOT/marketing-fundamentals (sufficient quality already), save Perplexity for Lucy's research where source quality matters most (AU industry reports, regional segment data).
- Hugo provided his API key. Initial path was `~/.zshrc` (matching the GEMINI_API_KEY video-analyzer pattern). Hugo redirected to project-scoped `.env` for security. Updated approach accordingly.
- Wrote `scripts/perplexity_search.py` (dependency-free Python helper that auto-loads `.env` from workspace root, supports all four models: sonar, sonar-pro, sonar-reasoning-pro, sonar-deep-research). Output to stdout, progress to stderr.
- Created `skills/perplexity-search/README.md` as a pointer doc with setup steps, model cheat sheet, usage examples, and cost guidance.
- Updated `.env.example` with the Perplexity slot and instructions.
- **Security incident caught:** Hugo pasted the real API key into `.env.example` (which is tracked in git). Caught before any commit. Cleaned up: created `.env` with the real key, restored `.env.example` to placeholder, verified `.gitignore` correctly excludes `.env`. Recommended rotation; Hugo rotated the key as the conservative move. Confirmed the new key authenticates with a small smoke test.

**Added "What's Next?" Section 13 to `prompts/competitor-analysis.md` (Stage 6 build).**
- New Section 13 instructs the model to end every competitor analysis with a numbered list of 3 to 4 specific next moves, each tied to something concrete from THIS analysis (a pattern name from Section 12, the hook from Section 2, a specific proof moment, the next competitor in the client list, etc.). Ends with the line "Or tell me something else you want."
- Includes a worked example using Sportif/Pilates language so future runs anchor on the right tone.
- Added a rule to the Critical Rules block: "Section 13 closing offer is required. Never end with Section 12."
- Updated `docs/pipeline-architecture.md` Stage 2 and Stage 6 statuses to reflect built state.

**Built the post-Lucy trigger system (the big institutional artifact).**
- Wrote `clients/sportif/intake/post-lucy-research-plan.md`. Contains: a 12-step to-do list for processing Lucy's responses end-to-end, 5 ready-to-run Perplexity passes (segment profile, per-competitor deep dives, brand-reference reverse-engineering, cultural lane validation, budget benchmarking) with exact bash commands and template prompts, save locations per output, estimated cost per pass (total ~$7 AUD), what's blocked vs unblocked, and the "why Perplexity for AU segment" rationale baked in so it's not lost.
- Saved auto-memory at `~/.claude/projects/-Users-hugobrizuela-Desktop-hyperframes/memory/sportif-post-lucy-trigger.md`. Lists trigger phrases ("Lucy has responded" / "Lucy's answers are in" / "the questionnaire is back" / etc.). When Hugo says one of those phrases in any future session, Claude auto-loads the plan and executes rather than improvising.
- Updated workspace MEMORY.md index at the auto-memory directory with both entries (sportif-australia + sportif-post-lucy-trigger). Em-dash sweep applied.
- Cross-linked `swot-summary.md`'s "Where everything lives" footer to point at the new plan. So anyone reading the SWOT lands on the research queue naturally.

### What we learned

- **The Meta Restricted Health and Wellness trigger is claim-making language, not product category.** "Stylish wrist weights" stays outside the bucket. "Wrist weights proven to boost cardio" goes inside. This makes the threat manageable rather than fatal, and aligns the creative-positioning answer with the cultural shift away from transformation language. Critical for Sportif copy.
- **Pilates is the dominant 2026 fitness cultural tailwind.** Topped global charts three years running, 15M ClassPass bookings, 66% YoY reservation growth. Stronger than expected. If Sportif's product mix touches Pilates at all, that becomes the lead positional lever.
- **Bala built a multi-million-dollar fitness accessories brand without paid marketing for years.** Their template (design-led product treated as jewelry, color/aesthetic, heavy UGC, influencer seeding) is the proven reference for new accessory brands. Confirmed via Shopify case study. Sportif's reference template should be Bala (not Gymshark or Alo, which are too big and apparel-led).
- **The default 2026 fitness-DTC ad playbook is broken.** TikTok bans before-and-after transformation imagery in paid regardless of claims. Meta's Restricted Health and Wellness bucket restricts lower-funnel optimization plus flags audiences/conversions with sensitive-trait metadata. Anyone selling "we'll just run Meta ads" is selling 2022 advice.
- **Klaviyo is the clear default for ecom email.** 3.8x revenue per subscriber vs Mailchimp at $5K-contact scale. Mailchimp requires $160/mo Premium for ecom automation; Klaviyo includes it at $100/mo.
- **Australian Meta CPM (~$9.80 AUD) runs 23% below US, 18% above UK.** TikTok in AU is 30% cheaper than Meta with Health & Fitness as the cheapest vertical (~$6.50 AUD CPM). Sydney CPM premium is 20-50% during peaks. Seasonality is significant: November AU CPM hits $24.80 vs January $10.68. Plan around Australian summer for Sportif.
- **Perplexity's edge over WebSearch is largest on AU and regional segment research.** It surfaces IBISWorld AU, Roy Morgan, Statista AU, ABS, Nielsen AU as primary sources where WebSearch returns US-centric SEO content. Cross-source synthesis with line-by-line citations. The advantage compounds in `sonar-deep-research` mode where it runs 30+ autonomous queries on a single segment question.
- **Project-scoped `.env` beats `~/.zshrc` for workspace-internal scripts.** The video-analyzer pattern was specific to skills installed at `~/.claude/skills/` (system-wide). For helpers that live inside the workspace, project-scoped `.env` is the correct security pattern. Established this clearly for any future API key.
- **API keys can leak through `.env.example` if you're not careful.** It's a tracked file. The placeholder pattern (`pplx-...`) needs to stay placeholder. Real keys go only in `.env` (gitignored). Caught a paste-mistake in this session and rotated the key. Process now clear for future keys.
- **Em dashes leak in when you're not paying attention.** Caught several in my own output across the session, especially in templated sections (link titles, table cells). Manual grep after every multi-edit is necessary. Workspace voice rule holds firm.

### Decisions

- **Sportif's intake deadline:** open-ended. No specific date in Lucy's email. Matches the no-fee/favor framing.
- **Sportif is Australian.** AUD benchmarks, AEST timing, AU creator landscape. Recorded as auto-memory so future sessions auto-load.
- **Sportif's chosen cultural lane:** not yet locked. Will be decided after Lucy's Q1, Q2, Q3, Q7, Q8 answers. Candidate lanes from the SWOT remain: Pilates, longevity, design-led, inclusive-fitness.
- **Meta and TikTok creative rule for Sportif:** no health-outcome claims in any copy. Lead with aesthetic, lifestyle, and function. This is hard rule, applies workspace-wide.
- **Perplexity integration:** project-scoped `.env`, not `~/.zshrc`. Helper at `scripts/perplexity_search.py` is dependency-free (no `python-dotenv` install needed).
- **Perplexity usage strategy:** don't re-run already-shipped research. Save Perplexity for Lucy's questionnaire processing where the source quality differential is largest.
- **Per-competitor Pass 2 not capped.** Run Perplexity sonar-deep-research on every competitor Lucy names in Q4. Judgment call applied at the time if she names 6+.
- **Post-Lucy trigger phrases:** "Lucy has responded" / "Lucy's answers are in" / "the questionnaire is back" / "Lucy sent the questionnaire back" / "we got Lucy's intake" all activate the queued research plan. Documented in auto-memory.
- **Section 13 "What's Next?" closing offer:** now mandatory for every competitor analysis output. Stage 6 of the pipeline is built for Stage 2 (design-only for the rest until they exist).
- **Marketing fundamentals doc** (`docs/marketing-fundamentals.md`) is the agency knowledge base, not a Sportif-specific doc. Part 8 IS Sportif-specific. Refresh structural Parts (1, 6, 7) less often than channel Parts (2, 3, 4, 5) which need updating ~every 6 months as platforms evolve.

### Open questions / next steps

**Top of queue for Session 006:**

1. **Research Seadance + ChatGPT Image 2.0 current prompt formats.** Stage 4 prerequisite. Use Perplexity sonar-deep-research now that it's wired in (prompt-engineering doc changes fast, Perplexity's source quality matters here). Output target: a reference doc at `docs/platform-prompt-formats.md` or similar that captures current spec for both, with examples, character limits, format quirks, and what's changed in the last 6 months. ~30-60 minute focused task.

2. **Write `prompts/synthesis-creative-brief.md`** (Stage 3, mode-aware brand-first vs competitor-first template). Template scaffold can be written without Lucy's specifics; the actual synthesis runs after her responses + Perplexity passes.

3. **Build voice-memo-to-questionnaire transcription recipe.** Whisper is already installed (Session 001). Likely needed when Lucy sends voice memos (one of the three answer formats we offered). Save at `recipes/transcribe-voice-memos.md`.

4. **Add image-analyzer skill (Stage 1 second path).** Static image competitor analysis. Standalone build, likely its own session.

**Sportif-active (waiting on Lucy):**

- [ ] Lucy returns questionnaire ~2026-06-03. Trigger phrase activates the queued plan at `clients/sportif/intake/post-lucy-research-plan.md`.
- [ ] Run the 5 Perplexity passes (~$7 AUD total).
- [ ] Populate `clients/sportif/brand.md` from responses + research.
- [ ] Draft Stage 3 synthesis brief at `clients/sportif/campaigns/launch-2026-09/synthesis-brief.md`.
- [ ] Update `docs/marketing-fundamentals.md` Part 8 budget bands with Sportif-specific AUD numbers.
- [ ] Send Lucy a "where we are" summary email after research is in.
- [ ] Hugo to send work-samples follow-up email (promised in intake P.S.).

**Workspace housekeeping (deferred, not urgent):**

- Wider em-dash sweep: `docs/pipeline-architecture.md` (still has em dashes in the Stage 6 example block), top-level `README.md`, older starter prompts (`csv-to-chart.md`, `pdf-to-summary.md`, etc.), recipes, skills READMEs.
- `from __future__ annotations` shim resilience for the video-analyzer skill on fresh clones. Either PR upstream, modify setup.sh to re-apply, or upgrade Python.
- Python 3.10+ upgrade via Homebrew. Would retire the shim need.
- OpenAI + HeyGen keys still pending (Session 001 carryover). HeyGen needed before any avatar work.
- Repo visibility decision for GitHub Pages (private requires Pro; public is free).
- The "Subject line convention" pattern from Session 004 (lead with mutual connection's name) worked for Lucy. Confirmed pattern. No action needed.

**Pipeline build queue (per architecture doc):**

- Stage 4 production-brief prompt + first adapter (Seadance or ChatGPT Image, pick based on Sportif's first content need from Lucy's Q12 timeline answer).
- Second Stage 4 adapter once first is proven.
- Stage 5 review-and-iterate workflow (design exists, no code yet; build when first synthesis brief gets reviewed by Hugo or Lucy).

### Two-Claude sync note

For the Cowork advisor catching up via this entry: the working pattern for Session 005 was Opus-writes (this session) with no advisor brainstorm needed mid-session. The post-Lucy trigger system means the advisor can also recognize trigger phrases when Hugo brings them up in advisor mode. Both sessions should now use the same auto-memory directory at `~/.claude/projects/-Users-hugobrizuela-Desktop-hyperframes/memory/` and the same MEMORY.md index. The plan file at `clients/sportif/intake/post-lucy-research-plan.md` is the single source of truth for what runs the moment Lucy responds.

---

## Session 006 (2026-05-29): Platform prompt-format research (Stage 4 prerequisite)

Short, focused session. Lucy had not responded yet (expected ~2026-06-03, no trigger phrase used), so the post-Lucy plan stayed parked. Executed the top Session 006 priority: researched current Seedance and GPT-4o image prompt formats and wrote the Stage 4 reference doc.

### What we did

**Wrote `docs/platform-prompt-formats.md` (the Stage 4 prerequisite).**
- Covers both primary platforms: Seedance (video) and GPT-4o image generation / gpt-image-1 (static).
- Per platform: at-a-glance spec table, prompt structure, length guidance, camera/motion vocab (Seedance) or text-rendering (gpt-image-1), style/quality modifiers (what helps vs what is noise), failure-mode table with fixes, supported parameters, one Sportif-shaped fitness-accessory worked example, and a "what changed in the last 90 days" section.
- Added a naming-reconciliation table at the top, a cross-platform cheat sheet, an "open items for Stage 4 build" section, and 21 cited sources. Confidence levels marked [official] vs [inferred] throughout.
- Em-dash AND en-dash swept clean (zero of both).

**Research method: deep-research failed, fell back to split sonar-pro.**
- Ran 3 `sonar-deep-research` calls (2 platforms + 1 retry). All 3 failed with `http.client.RemoteDisconnected: Remote end closed connection without response`. This is a gateway/timeout drop: the synchronous urllib call in `scripts/perplexity_search.py` (600s timeout) gets cut before deep-research finishes its long autonomous run. Consistent 3/3 failure, not transient.
- Pivoted to 4 `sonar-pro` calls (2 focused queries per platform: structure/params, then quality/failures/changes). All 4 completed cleanly and gave rich, well-cited output.
- Raw outputs preserved at `outputs/research/` (seedance-a/b.md, chatgpt-a/b.md) and referenced from the doc footer.

### What we learned

- **`sonar-deep-research` does not work through our current helper.** The synchronous POST gets dropped on the long-running deep-research job (RemoteDisconnected, no HTTP status). Until the script is hardened, deep-research is effectively unavailable via `scripts/perplexity_search.py`. The post-Lucy plan assumes deep-research for the 5 passes, so this needs a fix BEFORE Lucy responds (see open items). `sonar-pro` works fine.
- **Splitting one broad question into 2 focused `sonar-pro` queries is a good substitute for deep-research depth** and far more reliable. Cost stayed tiny.
- **Naming: "Seadance" is really Seedance (ByteDance), "ChatGPT Image 2.0" is really GPT-4o image gen / gpt-image-1 (OpenAI).** There is no product literally called "ChatGPT Image 2.0." Recorded in the doc's naming table so the workspace stops targeting the wrong names.
- **Both platforms reward natural-language prose over keyword stacks, one-primary-subject discipline, and iterative refinement.** Generic quality-stacker buzzwords ("8k, masterpiece, trending on artstation") are noise on both.
- **gpt-image-1's standout is accurate in-image text** (quote it exactly, keep it short). Seedance's standout is multi-shot narrative coherence in a single prompt ("Shot 1 / Shot 2 / Shot 3").
- **Watch for Seedance 2.0.** A Seed-site "seedance2_0" page reference surfaced but is not yet backed by official capability docs. If it goes live, the camera/multi-shot guidance needs a refresh.

### Decisions

- **Doc location and shape:** single combined reference at `docs/platform-prompt-formats.md` (not two files), matching how the architecture doc treats the two platforms together.
- **Research model:** `sonar-pro` split queries, given deep-research is broken via the helper. Did not burn more time retrying deep-research.
- **Worked examples honor the Sportif no-health-claims rule** (aesthetic/lifestyle/function only), so they double as Stage 4 pressure-test fixtures.
- **Cost:** ~14.7K total tokens across 4 sonar-pro calls, roughly $0.50 AUD. Well under the $2-3 AUD estimate because deep-research was abandoned (failed calls returned nothing billable).

### Open questions / next steps

**Newly surfaced (priority):**
- [ ] **Harden `scripts/perplexity_search.py` for deep-research BEFORE Lucy responds.** The post-Lucy plan's 5 passes assume `sonar-deep-research`, which currently fails with RemoteDisconnected. Options: add retry-with-backoff, switch deep-research to Perplexity's async/polling API surface, or change the plan to use split `sonar-pro` queries instead. This is now a blocker on the post-Lucy plan working as written.
- [ ] **Confirm `gpt-image-1` live parameter set** (`quality`, `input_fidelity`, `background`, `output_format`) against the OpenAI API reference before writing the Stage 4 adapter parameter block. Research could not pin exact accepted values.
- [ ] **Pick the standard Seedance reseller** (fal.ai / Pollo / Wavespeed / Dreamina direct). Field names differ per host; the adapter should target one.

**Carried from Session 005 (still queued):**
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3 template, mode-aware).
- [ ] Build voice-memo-to-questionnaire transcription recipe (Whisper) at `recipes/transcribe-voice-memos.md`.
- [ ] Add image-analyzer skill (Stage 1 second path).
- [ ] Write Stage 4 adapters (`prompts/production-seadance.md`, `prompts/production-chatgpt-image.md`) now that the format spec exists. Pick first adapter from Lucy's Q12 timeline answer.

**Sportif-active (waiting on Lucy, ~2026-06-03):** unchanged from Session 005. Trigger phrase activates `clients/sportif/intake/post-lucy-research-plan.md`. The deep-research blocker noted above was FIXED later in this same session (see addendum).

### Session 006 addendum (same session): deep-research fixed + Seedance 2.0 discovered

**Fixed the deep-research blocker.** Hugo asked to fix the script immediately. Root cause: `sonar-deep-research` cannot run as a synchronous HTTP call (the long autonomous job gets dropped by the gateway, RemoteDisconnected). Fix: `scripts/perplexity_search.py` now auto-routes `sonar-deep-research` to Perplexity's async API (submit to `/async/chat/completions`, poll `/async/chat/completions/{id}` until COMPLETED), and added retry-with-backoff to the sync path for other models. Discovered the async endpoint ONLY accepts deep-research (other models 400 there), so routing is automatic, not a user flag (removed an initial `--async` flag that would always error).
- **Validated end-to-end:** a small deep-research query submitted, polled IN_PROGRESS x3, COMPLETED at ~40s, returned a clean answer plus 30 cited sources. Log/output preserved at `outputs/research/async-test.*`.
- Updated the post-Lucy plan with an operational note (deep-research now async, shows IN_PROGRESS, `>` redirects still clean). Updated auto-memory `perplexity-deep-research-broken.md` from "blocker" to "resolved / how it works."

**Seedance 2.0 has officially launched (new finding).** The validation deep-research run surfaced an official ByteDance Seed launch blog ("Official Launch of Seedance 2.0") plus a Seed 2.0 model page and 2.0-vs-Sora-2 comparisons. This corrects the sonar-pro reading in `docs/platform-prompt-formats.md`, which had only found an unconfirmed 2.0 page reference. Concrete proof of deep-research's source-quality edge over sonar-pro. Updated the platform doc's A8 and Part D to reflect the launch and flag that Part A (the 1.0 spec) needs a 2.0-focused refresh. The 1.0 spec stays valid as a baseline since 1.0 is still widely hosted.

**New next step (added):** run a `sonar-deep-research` pass on Seedance 2.0 prompt format and what changed vs 1.0, then refresh Part A of the platform doc. Now unblocked since deep-research works.

### Session 006 second addendum (same session): both platforms had shipped 2.0, doc rewritten

Hugo asked to research Seedance 2.0 AND "GPT Image 2.0." Ran 2 sonar-deep-research passes (via the now-working async path) plus 2 sonar-pro follow-ups for prompt mechanics. Both platforms turned out to have shipped major April 2026 flagships that the original doc completely missed. Rewrote `docs/platform-prompt-formats.md` to be 2.0-first.

**Seedance 2.0 (confirmed live, April 2026):** unified multimodal audio-video model (Dual-Branch Diffusion Transformer, ~4.5B params). Generates synchronized stereo audio (dialogue, SFX, music, phoneme-level lip-sync in 8+ languages) jointly with video. Accepts text + up to 9 images + 3 video + 3 audio as inputs via a new `@image1`/`@video1`/`@audio1` reference syntax (role-assigned in natural language, up to 12 assets). Directorial prompt format: Subject, Action, Environment, Camera, Style, Constraints. 4 to 15s, 480p/720p/1080p (+2K, 4K upscale), aspect 16:9/9:16/4:3/3:4/1:1/21:9. Strong physics. Editing/extension. 1.0 is now the legacy baseline (still hosted).

**GPT Image 2.0 IS REAL (Hugo was right).** The real model is `gpt-image-2` (API), snapshot `gpt-image-2-2026-04-21`, branded "ChatGPT Images 2.0," launched April 2026. Lineage: DALL-E 3 -> gpt-image-1 -> gpt-image-1.5 (late 2025) -> gpt-image-2. DALL-E 2/3 removed from the API 2026-05-12. New: near-pixel-perfect multilingual in-image text, up to 4K, better instruction following. Key gotchas captured in the doc: (1) NO "thinking mode" API parameter (it's ChatGPT-layer orchestration; use Responses API to plan); (2) gpt-image-2 does NOT support transparent backgrounds (regression vs gpt-image-1; use gpt-image-1.5 or white-bg-plus-cutout); (3) do not set `input_fidelity` (errors). Params: size presets + custom (multiples of 16, 655K to 8.29M px, aspect <3:1), quality low/medium/high, output_format png/jpeg/webp, n. Token-priced: ~$0.01 (low 1024) to ~$0.41 (high 4K) per image.

**Lesson reinforced:** deep-research caught two whole product generations that the sonar-pro round missed. Worth the cost when currency matters. Both completion bodies cut off mid-section at ~1.5-2.6K tokens though, so each needed a focused sonar-pro follow-up for the prompt mechanics. Pattern for future deep-research: expect a strong synthesis + sources but budget a follow-up for the long-tail detail.

**Stage 4 is now properly unblocked** with a current, 2.0-accurate format spec for both platforms. Open items live in Part D of the doc (pick resellers, confirm live param strings, transparent-asset path, which model tier Sportif starts on).

---

<!-- Add new sessions ABOVE this line. Format:
## Session NNN — YYYY-MM-DD — One-line summary
### What we did
### What we learned
### Decisions
### Open questions / next steps
-->
