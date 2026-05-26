# Creative-Strategy Pipeline Architecture

> The end-to-end workflow this workspace exists to support: turn client brand + competitor creative content (video OR static) into platform-agnostic production briefs that get translated into ready-to-paste prompts for AI media platforms (Seadance, ChatGPT Image 2.0, etc.).

_Last updated: 2026-05-26 (Session 004 — revised after Devil's Advocate pass + Sportif onboarding). This doc is the locked source of truth for the pipeline shape. Update it when decisions change — don't let `memory.md` drift become the only record._

---

## The Goal in One Sentence

Given a real client and their market, produce a creative brief + platform-ready production prompts that adapt the best patterns in the category to that client's brand — with review loops at every stage so we ship work that's actually good, not just generated.

## Two Pipeline Modes

The same scaffolding supports two modes depending on the client's stage:

| Mode | When to use | Starting point |
|---|---|---|
| **Brand-first** | Established client with their own voice, customers, content history | Their brand → competitive check is downstream |
| **Competitor-first** | Net-new launch, no brand voice or content yet (e.g., Sportif) | Category landscape → build their brand against what's working |

Pick the mode per client. Document the chosen mode in `clients/<client>/README.md`.

## Pipeline Diagram

```
PRE-STAGE 0 — Intake / Discovery
   clients/<client>/intake/
     • questionnaire.md  ← email to client, ~10 questions, ~30 min to answer
     • swot-analysis.md  ← your strategic read (with research-helper prompt)
                                   │
                                   ▼
STAGE 0 — Client Context
   clients/<client>/brand.md         ← brand kit + identity, populated from intake
   clients/<client>/products/<sku>.md ← one per product
   clients/<client>/campaigns/<slug>.md ← per-campaign brief when active
                                   │
                                   ▼
STAGE 1 — Competitor Content Ingestion
   VIDEO  → video-analyzer skill (built ✓)
   STATIC → image-analyzer (TODO)
   PDF    → consider as third input type (TBD)
                                   │
                                   ▼
STAGE 2 — Pattern Extraction (12-section analysis)
   prompts/competitor-analysis.md (built ✓ for video)
   Output → clients/<client>/competitor-analyses/<source>-<descriptor>-<date>.md
                                   │
                                   ▼
STAGE 3 — Strategic Synthesis (TODO — mode-aware)
   prompts/synthesis-creative-brief.md
   Input: client brand.md + 1+ competitor analyses + mode (brand-first/competitor-first)
   Output: adapted creative direction for the client
                                   │
                                   ▼
STAGE 4 — Production Brief (TODO — platform-agnostic)
   prompts/production-brief.md → ONE intermediate brief (visual, motion, audio, text, length, aspect)
      ↓
   Thin platform adapters at the final step:
     • prompts/adapters/seadance.md       → Seadance prompt
     • prompts/adapters/chatgpt-image.md  → ChatGPT Image 2.0 prompt
     • (future) runway.md, higgsfield.md, etc.
                                   │
                                   ▼
STAGE 5 — Review & Iterate (NEW)
   After client/Hugo reviews the generated content, feedback flows BACK:
     • Visual off? → re-do Stage 4 adapter step
     • Wrong direction? → re-do Stage 3 synthesis
     • Wrong patterns? → re-do Stage 2 analyses
     • Off-brand? → update Stage 0 brand.md
   Saved as: clients/<client>/campaigns/<slug>-review-notes.md
                                   │
                                   ▼
STAGE 6 — "What's Next?" Offer
   Every stage output ends with 2-4 offered next-steps so the user picks the next
   move. Borrowed from the marketing-analysis YouTuber pattern.
                                   │
                                   ▼
                  Final client deliverable
            (generated outside this workspace by
             Seadance / ChatGPT Image / Runway / etc.)
```

## Decisions Locked (Session 004, revised after Devil's Advocate)

| Question | Decision |
|---|---|
| Where does client context live? | **Per-client folder** at `clients/<client-kebab-slug>/`. New top-level `clients/` folder, sibling of `compositions/` (renamed from `my-projects/`). |
| Folder naming | `clients/` (was `projects/`) + `compositions/` (was `my-projects/`) to avoid collision. Lowercase-kebab-case for client slugs. |
| Brand docs | **Combined `brand.md`** (kit + identity) as a single file. Split into two only if/when it gets unwieldy. |
| Intake | **Pre-Stage-0 intake layer:** questionnaire (email to client) + SWOT analysis (your strategic read with research-helper prompt). |
| Static images | **Add an image-analyzer alongside the video-analyzer** (sibling skill). Defer build to Session 005. |
| Pipeline shape | **Modular stages with "What's Next?" handoffs** + two modes (brand-first vs. competitor-first) per client. |
| Stage 4 platform handling | **Platform-agnostic production brief + thin platform adapters.** Primary adapters: Seadance (video), ChatGPT Image 2.0 (static). Runway/Higgsfield as later additions. |
| Review/iterate | **Stage 5 added** — feedback loops back to whichever upstream stage needs the fix. Documented per-campaign. |
| Campaign structure | **Flat per client** — one brief / synthesis / production-prompts folder at a time. Wrapped campaigns move into `_archive/<YYYY-MM-campaign-slug>/`. Nested campaigns only when needed. |

## Stage-by-Stage Detail

### Pre-Stage 0 — Intake / Discovery

**Status: BUILT ✓ (Session 004)**

Two artifacts live in every client's `intake/` folder:

- **`questionnaire.md`** — A 10-question email-ready intake covering: brand "why", one-liner, product, customer, where-they-hang-out, tone, references (positive + negative), visual identity, constraints + goals. ~30 min for the client to complete. Send before the first deep-dive call so the call is informed.
- **`swot-analysis.md`** — Your strategic assessment with structured quadrants (Strengths, Weaknesses, Opportunities, Threats) + guiding questions + a research-helper prompt at the bottom you can paste into Claude to surface market data for Opportunities and Threats.

The questionnaire is what the client says. The SWOT is what you conclude as the expert. Both feed Stage 0.

### Stage 0 — Client Context

**Status: BUILT ✓ (Session 004 — template + Sportif populated)**

Each client gets a folder under `clients/`. Convention:

```
clients/
├── _template/              ← copy this for each new client
│   ├── README.md
│   ├── brand.md            ← combined kit + identity (skeleton)
│   ├── intake/             ← questionnaire + SWOT templates
│   ├── products/           ← one .md per SKU (_template-product.md skeleton)
│   ├── campaigns/          ← campaign briefs
│   ├── competitor-analyses/ ← Stage 2 outputs per this client
│   ├── _archive/           ← wrapped campaigns move here
│   └── assets/             ← logos, fonts, imagery (gitignored)
└── <client-slug>/          ← actual clients (e.g., sportif/)
```

`brand.md` schema (one file for now, split later if needed):
- **Identity:** one-liner, origin, mission, positioning, values, customer archetype
- **Voice & tone:** adjectives, sound-like / not-sound-like, vocabulary do/don't, register
- **Visual identity:** logo, color palette (hex), typography, image style
- **Hard guardrails:** legal, brand, off-limit words
- **Inspiration:** what they admire / want to avoid

### Stage 1 — Competitor Content Ingestion

**Status: PARTIAL — video built ✓, static TODO**

- **Video path:** existing `video-analyzer` skill (Session 003-004). Invocation in `recipes/analyze-video-with-gemini.md`.
- **Static path:** sibling tool TBD. Session 005 task to evaluate:
  - Gemini's image-vision API via a short Python script (same auth/key as video).
  - Claude's native image vision (works in chat, not scriptable).
  - Existing community skill that does image structured analysis.
- **PDF as third input?** Open question — competitors sometimes share decks / ad mockups as PDFs. Could be handy. TBD.

### Stage 2 — Pattern Extraction

**Status: BUILT ✓ (for video) — `prompts/competitor-analysis.md`**

- 12-section marketing-conversion framework (Format / Hook / Audience / Pain / Angle / Product Intro / Proof / Beat-by-Beat / CTA / What Works / What's Weak / Steal-Worthy Patterns).
- Invoked via: `analyze_video.py --prompt-file prompts/competitor-analysis.md`.
- Output: markdown report saved to `clients/<client>/competitor-analyses/<source>-<descriptor>-<date>.md`.
- **TODO:** Append "What's Next?" offer block to the prompt so analysis outputs end with offered next moves (Stage 6 pattern).

### Stage 3 — Strategic Synthesis (mode-aware)

**Status: TODO**

- New prompt: `prompts/synthesis-creative-brief.md`.
- Input: client `brand.md` + 1+ Stage 2 analysis files + chosen mode.
- Output: an adapted creative direction for the client — NOT a summary, NOT a copy of any one competitor.
- **Mode-aware behavior:**
  - **Competitor-first mode** (e.g., Sportif): start from "what patterns are working in this category" + intersect with what we know about the client. Best when client has no existing voice.
  - **Brand-first mode** (established clients): start from "what's true about this brand" + use competitor analyses as a check, not a foundation. Best for mature brands with their own voice.
- Brief contents (proposed): hook concept, visual direction, tone, structure outline, CTA, what's deliberately different from competitors.

### Stage 4 — Production Brief (platform-agnostic) + adapters

**Status: TODO**

- **Step 4a — `prompts/production-brief.md`** (platform-agnostic): one intermediate brief that captures visual direction, motion direction, audio direction, on-screen text, length, aspect ratio, mood. Independent of which AI tool will render it.
- **Step 4b — platform adapters** (thin translation layers):
  - `prompts/adapters/seadance.md` → translates production-brief into Seadance prompt format
  - `prompts/adapters/chatgpt-image.md` → translates into ChatGPT Image 2.0 format
  - Future: `runway.md`, `higgsfield.md`, etc.
- **Why this two-step structure (from Devil's Advocate Challenge 4):** Platforms change fast — prompt formats, pricing, even whether they exist. Building one platform-agnostic format + thin adapters survives platform churn. Only the adapter needs rewriting when a platform changes; the production brief stays stable.
- **Research prerequisite:** before writing the first adapter, run a research session on current Seadance and ChatGPT Image 2.0 prompt best practices. These have evolved.

### Stage 5 — Review & Iterate

**Status: DESIGN, no code yet (added Session 004 from Devil's Advocate Challenge 5)**

The pipeline is NOT one-directional. After generating output, the user (client or Hugo) reviews and gives feedback. That feedback maps to a specific upstream stage:

| Feedback type | Goes back to |
|---|---|
| "The visual feel is wrong" / "wrong colors" | Stage 4 — re-do the adapter step (or, if it's a deep issue, Stage 3) |
| "Wrong creative direction" / "doesn't match what we want" | Stage 3 — re-do the synthesis |
| "We borrowed from the wrong patterns" | Stage 2 — re-analyze with different competitors, or different lens |
| "This doesn't sound like our brand" | Stage 0 — update `brand.md`, then redo Stage 3 |

Saved as: `clients/<client>/campaigns/<slug>-review-notes.md` (one per campaign). Captures: feedback received, which stage we re-ran, what changed.

### Stage 6 — "What's Next?" Offer Pattern

**Status: DESIGN, no code yet (was Stage 5 before review-iterate was added)**

Every prompt in the pipeline ends with a closing block:

```markdown
---
**What's next?** Pick one and tell me to run it:
- [Option A — most likely useful next step]
- [Option B — alternate path]
- [Option C — deeper dive on something]
```

Generalized from the marketing-analysis YouTuber's closing pattern. Implementation = literally add a "What's Next?" section to the bottom of each prompt's instructions.

## Recommended Build Sequence (Session 005 onward)

1. **Add "What's Next?" closing block to `prompts/competitor-analysis.md`** (Stage 6 first half). Cheap, immediately useful, doesn't depend on anything.
2. **Send Sportif's questionnaire** + start the SWOT (Pre-Stage-0 first real use). Doesn't require more building.
3. **End-to-end smoke test** — run `prompts/competitor-analysis.md` against a real fitness-accessory competitor video, save to `clients/sportif/competitor-analyses/`. Validates Stages 1 + 2 + folder convention end-to-end with a real client.
4. **Research Seadance + ChatGPT Image 2.0 current prompt formats** (Stage 4 prerequisite). Web search + their docs. ~30-60 min focused task.
5. **Write Stage 3 synthesis prompt** (`prompts/synthesis-creative-brief.md`) with mode-aware logic.
6. **Write Stage 4 production-brief + first adapter** (Seadance OR ChatGPT Image, whichever is needed first for Sportif).
7. **Write second adapter** when the second platform is needed.
8. **Add image-analyzer skill** (Stage 1 static path). Standalone — can happen anytime, ideally its own session.

## Open Questions (per stage)

### Pre-Stage 0
- Should the questionnaire be a Google Form / Typeform for better UX, instead of email-with-markdown? Trade-off: prettier vs. version-controlled.

### Stage 0
- Should `brand.md` be free-form or strictly structured? (Currently: structured with field labels — adjust based on first real use.)
- One brief per client, or one per *campaign*? (Currently: one campaign at a time, flat. Nested only when multi-campaign clients appear.)

### Stage 1
- Image-analyzer: build with Gemini API to match the video tooling, or use Claude's native vision and accept it only works in chat?
- Do we need to support PDFs as a third input type?

### Stage 3
- Does the synthesis brief need to be *one* output or *several* (e.g., "5 different creative directions to pick from")?
- How much should it borrow from a *single* competitor analysis vs. synthesize across multiple?
- How explicitly should the mode (brand-first vs. competitor-first) shape the output?

### Stage 4
- Do we need character-count enforcement for Seadance (some platforms cap prompts at ~500 chars)?
- Should Stage 4 output ONE prompt per platform, or a *batch* (e.g., 5 variations for A/B testing)?
- Where does the generated content actually get saved/tracked? Output URLs from Seadance/ChatGPT need a home — probably `clients/<client>/campaigns/<slug>/generated/`.

### Stage 5
- Where do client-side review comments come from? (Slack? Email? In-doc?) How do we capture them in a structured way?
- How many iteration cycles before we step back and rethink at a higher level?

### Stage 6
- Is the "What's Next?" offer hardcoded per stage, or dynamically generated based on what was just produced?

## Reference Materials

- `clients/_template/` — Stage 0 reusable scaffolding (Session 004).
- `clients/sportif/` — first real client, intake materials ready to use (Session 004).
- `prompts/competitor-analysis.md` — Stage 2 prompt (12-section, current).
- `recipes/analyze-video-with-gemini.md` — Stage 1+2 invocation recipe.
- `skills/video-analyzer/README.md` — pointer doc for the video-analyzer skill.
- `outputs/video-analyses/student-kit-linear-promo-30s-2026-05-26.md` — example Stage 2 output (default prompt, not the 12-section).
- `memory.md` Session 003-004 entries — full session-by-session context.

---

_When this doc changes, also note it in `memory.md` so the change shows up in the session log._
