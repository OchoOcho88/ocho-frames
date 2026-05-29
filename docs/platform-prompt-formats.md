# Platform Prompt Formats: Seedance 2.0 + GPT Image 2 (ChatGPT Images 2.0)

> Source: Perplexity research. Round 1 (2026-05-29): 4 sonar-pro passes on Seedance 1.0 and gpt-image-1. Round 2 (2026-05-29): 2 sonar-deep-research passes + 2 sonar-pro follow-ups after both platforms turned out to have shipped major 2.0 versions.
> Tool: scripts/perplexity_search.py (deep-research now runs via the async API, fixed Session 006)
> Date: 2026-05-29
> Owner: Ochoproductions. Voice rule applies (no em dashes).

This is the Stage 4 reference for the creative-strategy pipeline (see docs/pipeline-architecture.md). Stage 4 turns a synthesis brief into paste-ready production prompts for our two primary AI media platforms. You cannot write the Stage 4 adapter prompts (`prompts/production-seedance.md`, `prompts/production-chatgpt-image.md`) without the current format spec for each. This doc is that spec.

**Major update (2026-05-29):** both platforms shipped new flagship versions in April 2026. The research initially documented the older versions (Seedance 1.0, gpt-image-1). Deep-research then surfaced that **Seedance 2.0** and **GPT Image 2 / ChatGPT Images 2.0** are both live. This doc now targets the 2.0 models. The 1.x details are kept only as legacy baseline where useful.

---

## Naming reconciliation (read this first)

| Pipeline doc name | Real product (current) | Notes |
|---|---|---|
| "Seadance" (video) | **Seedance 2.0** by ByteDance | Correct spelling is Seedance. 2.0 launched April 2026, a unified text-image-audio-video model. Seedance 1.0 / 1.0 Pro is the prior generation, still widely hosted on resellers. |
| "ChatGPT Image 2.0" (static) | **gpt-image-2** (API) / **ChatGPT Images 2.0** (product) | Launched April 2026, snapshot `gpt-image-2-2026-04-21`. "ChatGPT Images 2.0" is the user-facing branding over the same engine. Lineage: DALL-E 3 to gpt-image-1 to gpt-image-1.5 to gpt-image-2. The workspace's informal "ChatGPT Image 2.0" label turned out to match a real product. |

Target the real model names in file names and prompts. The pipeline doc's informal labels are fine in conversation.

## Confidence levels

Both vendors publish thin official prompt docs. **[official]** = from vendor material (ByteDance Seed, OpenAI docs). **[inferred]** = from reseller API docs, prompt guides, or hands-on reviews. Treat **[inferred]** as a strong default to pressure-test. Re-check any live API parameter (sizes, quality tiers, pricing) against the vendor reference before a paid production run.

---

# Part A. Seedance 2.0 (video)

## A0. What Seedance 2.0 is, and what changed from 1.0

Seedance 2.0 is not "1.0 plus audio." It is a **unified multimodal audio-video model**: a Dual-Branch Diffusion Transformer (about 4.5B parameters per partner docs) that jointly generates video and synchronized stereo audio in a single pass, and accepts text, images, audio, and video as conditioning inputs. **[official]**

| Dimension | Seedance 1.0 | Seedance 2.0 |
|---|---|---|
| Inputs | Text, optional single image (I2V) | Text, up to 9 images, up to 3 video clips, up to 3 audio clips, combinable in one run |
| Output | Video only | Video plus native synchronized stereo audio (dialogue, SFX, ambience, music), phoneme-level lip-sync in 8+ languages |
| Reference system | Implicit single-image conditioning | Explicit `@image1` / `@video1` / `@audio1` tags (up to 12 assets), with natural-language role assignment |
| Resolution | Up to 1080p | 480p, 720p, 1080p widely available, some 2K, 4K via upscaling |
| Duration | 5 to 15s | 4 to 15s in 1-second increments, multi-shot inside one generation |
| Aspect ratios | Limited docs | 16:9, 9:16, 4:3, 3:4, 1:1, 21:9 |
| Physics / motion | Smooth motion | Stronger physical accuracy (gravity, fabric, liquid, collisions), better for sport, dance, interaction |
| Editing | Basic | Extend forward/backward, add/remove/replace elements, merge clips, video-to-video |

The practical shift: Seedance 2.0 is a **directing system**, not a text-to-video box. Prompt design is now explicitly directorial, and the reference tags let you lock identity, composition, camera, and rhythm from separate assets.

## A1. Prompt structure (the directorial format)

Official and partner guidance converge on a fixed component order. Treat the prompt like a shot brief, not a pile of style tags. **[official + inferred]**

1. **Subject** (who or what, singular where possible)
2. **Action** (present tense, one specific verb phrase)
3. **Environment** (location, time of day, weather, set details)
4. **Camera** (shot size + movement + angle/lens cue)
5. **Style** (visual anchor, lighting, color treatment, finish)
6. **Constraints** (what to keep fixed, what to exclude, duration/tempo, consistency rules)

Copy-paste template:

```text
Subject: ...
Action: ...
Environment: ...
Camera: [shot size] + [movement] + [angle/lens cue]
Style: [visual anchor, lighting, color, finish]
Constraints: [keep fixed, exclude, duration/tempo, consistency]
```

## A2. The `@image` / `@video` / `@audio` reference system (new in 2.0)

This is the headline 2.0 feature for brand work. Attach assets as inputs, then reference them by tag inside the prompt and assign each a role in plain language.

- Syntax: `@image1`, `@image2`, `@video1`, `@audio1`, etc.
- Limits: up to **9 images, 3 videos, 3 audio clips** (12 assets total).
- Assign one role per reference. Separate composition, motion, identity, wardrobe, and audio rhythm into different references.

Example role assignment:

```text
Use @image1 for character identity and wardrobe, @image2 for scene composition,
@video1 for the camera move, and @audio1 for the beat timing.
```

Best practice: state the role explicitly ("use the camera move from @video1"), not vague "inspiration" language.

**Field-validated findings (2026-05-29 prompt-lab test):**
- **Text rendering is better than expected for short wordmarks.** A short simple wordmark ("FLOW", 4 caps letters) rendered clean and stable even when INVENTED with no reference. So Seedance can be trusted with a short logo-style wordmark. The garble risk is for longer strings, taglines, and complex typography. For anything beyond a short wordmark, supply it via an `@image` reference (Seedance reproduces referenced text cleanly), ideally a gpt-image-2 still which renders exact text.
- **A finished hero reference overrides shot direction.** If you reference a complete, composed still, Seedance animates close to that still ("the poster comes alive") and largely ignores a detailed multi-beat shot plan, with weak pacing control. Use a strong/finished reference for "animate this hero + logo" clips. Use a loose reference or none (text-only direction) when you need a multi-beat cinematic sequence, since text-only direction holds structure well.
- **Image-style prompts port to video.** A static, photographic prompt (no motion direction) fed to text-to-video still produced coherent motion: Seedance inferred movement from a specific exercise description. You do not always need explicit beat/camera direction.

## A3. Camera, motion, and multi-shot

**Camera vocabulary** (short, literal, production-oriented): wide / establishing, medium, close-up, extreme close-up, over-the-shoulder, low angle, high angle, eye level, handheld, locked-off, slow push-in, pull-back, dolly in/out, truck left/right, pan, tilt, rack focus, orbit/arc, zoom.

**Motion verbs:** walks, turns, reaches, lifts, nods, breathes, swirls, pours, drifts, ripples, flutters. One primary motion per shot.

**Multi-shot / time-coded:** number the shots or use timestamps. Declare shot count, duration, and aspect ratio at the top.

```text
Duration: 8s, 16:9, 3 shots

[0s-2s] Establishing shot: ...
[2s-5s] Medium shot: ...
[5s-8s] Close-up: ...

Style: ...
Constraints: ...
```

## A4. Audio prompting (new in 2.0)

Audio is a first-class part of the prompt, generated jointly. Be specific, not "good audio." Specify dialogue, sound effects, music, ambience, and lip-sync separately.

```text
Audio:
- Dialogue: The woman says, "We should leave now."
- Sound effects: soft footsteps on wet pavement, distant traffic
- Music: minimal piano, slow tempo, tension-building, no vocals
- Ambience: light rain, faint wind, muffled city hum
- Lip-sync: accurate, natural timing for on-camera speech
```

Put dialogue inside a specific shot or timestamp, keep spoken lines short, and ban subtitles if you will add captions later.

**Audio moderation is strict, default to audio-off (field-validated 2026-05-29).** Seedance 2.0 ("Seedance 2 Omni") runs an audio safety review that blocks generations whose music could resemble existing or copyrighted work (error code `content_moderation_inferred`, not retryable, but not charged). In testing it blocked an innocent "soft ambient pad + chime" line, AND blocked again on the vendor's own moderation-safe boilerplate. So do not rely on prompting your way past it. Recommended approach:
- **Generate with audio OFF** (set the audio block to "None, completely silent" and toggle audio off in the UI), then add music in post. This is the reliable production path.
- If you must try in-engine audio, the moderation-safe boilerplate is worth one attempt but expect it to fail: "Music: original score, unrecognizable; no clear or hummable main melody; no repeating hook sections; do not use melodies, chords, or rhythmic motifs from any existing works; do not imitate any specific artist or era; no sampling, no vocals." Shorter clips (around 5s) trip the filter less often.
- Net: treat Seedance 2.0 native audio as not production-ready yet. Plan music and sound as a post step.

**Audio behaves counterintuitively (field-validated 2026-05-29):** the prompt text does NOT control audio. Seedance generates music on its own even when the prompt says "Audio: None, silent." And the moderation pattern is inverted from what you would expect: UNspecified audio (let Seedance auto-fill) passes moderation, while user-SPECIFIED music descriptions get blocked. So in practice: to ship with sound, either let Seedance auto-generate (do not describe music) and accept what you get, or generate true silence via the UI audio toggle (not the prompt) and add licensed music in post. The post route remains the recommended one for brand control.

## A5. Length

Concise and structured beats long prose. Single shot: short tight prompt. Multi-shot (5 to 10s): structure by shots or timestamps. Longer: break into explicit segments. If it gets too long, keep the shot list and drop unsupported extras.

## A6. Style modifiers and failure modes

**What helps:** one strong style anchor ("35mm film," "documentary realism," "advertising gloss"), one lighting/color line, one camera move per shot. A "4K, ultra HD, sharp clarity, stable picture" quality suffix is a community practice, not official.

**Mostly noise:** stacked conflicting styles, long buzzword chains, vague adjectives without a visual anchor.

| Failure mode | Fix |
|---|---|
| Flagged/refused prompt | Remove brand names, logos, watermark requests. Rephrase sensitive content neutrally. |
| Identity drift (face/clothing changes) | One primary identity reference image, "keep face and clothing consistent" in constraints, avoid mirrors/crowds. |
| Camera chaos | One camera move per shot. Ban unwanted moves: "no whip pan, no snap zoom, no Dutch angle." |
| Audio desync | Anchor dialogue to a shot/timestamp, short lines, "accurate lip-sync," avoid overlapping audio. |
| Body/object artifacts | Reduce action complexity, simple props, "no extra fingers, no warped hands, no melting edges." |
| Style drift | One style anchor instead of many adjectives. |
| Mid-clip glitch / bad jump cut | Seen around 5 to 7s of a 15s multi-beat reference clip. CONFIRMED FIX: a single continuous shot (no beats) ran smooth end to end. So prefer "one continuous shot, no cuts" for short clips; multi-beat structures risk a discontinuity. Note: the Gemini video-analyzer does not flag motion glitches, review with human eyes. |
| Unnatural / awkward human action | Seedance animates people but specific human biomechanics come out unnatural, especially "correct" use of equipment (a seated band exercise looked awkward and not a believable use of the band). Mitigate: supply a motion reference via `@video1`, keep human actions simple and generic (a stretch, a turn, walking) rather than precise exercise demonstrations, or reserve precise demos for filmed footage. The Gemini analyzer OVER-RATES motion naturalness (it praised "good form" on the awkward clip), so judge human motion with human eyes. |

## A7. Parameters and access

- Resolution: 480p, 720p, 1080p (some 2K, 4K via upscaling).
- Duration: 4 to 15s, 1-second increments.
- Aspect: 16:9, 9:16, 4:3, 3:4, 1:1, 21:9.
- Access: Dreamina, Volcengine, BytePlus, and resellers (fal.ai went live April 2026, plus Replicate, Wavespeed, Segmind, Higgsfield). A "Seedance 2.0 Fast" lower-cost tier exists for iteration.
- Consistency: driven mainly by the reference system plus constraints, not a single seed knob.

## A8. Worked examples (fitness accessory, Sportif-shaped)

Sportif hard rule: lead with aesthetic, lifestyle, function. No health-outcome claims ("burns calories," "tones arms") in copy or generated media. These honor that.

**Single shot with audio (text-to-video):**

```text
Duration: 6s, 9:16, 1 shot

Subject: A woman in a sand-toned activewear set, in a bright minimalist home studio.
Action: She fastens a matte clay-tone wrist weight and begins a slow, controlled Pilates arm circle.
Environment: Morning light through large windows, linen mat, a single potted plant.
Camera: Medium shot, very slow push-in, eye level, 50mm look.
Style: Calm editorial realism, soft diffused light, warm neutral palette, subtle film grain.
Audio: Sound effects: soft fabric movement, a gentle exhale. Ambience: quiet room tone, faint birdsong. Music: minimal warm piano, slow tempo, no vocals. No dialogue.
Constraints: Keep face and outfit consistent, no text, no logos, no camera shake, calm pacing.
```

**Multi-shot with reference roles (image and video to video):**

```text
Duration: 8s, 9:16, 3 shots

Use @image1 for product identity (the wrist weights), @image2 for the model's
identity and wardrobe, and @audio1 for pacing.

[0s-3s] Shot 1: Wide shot of a tidy sunlit studio, the wrist weights resting on a folded linen mat. Locked-off camera.
[3s-6s] Shot 2: Medium shot as the model picks one up and turns it to show the texture. Slow push-in.
[6s-8s] Shot 3: Close-up of the weight fastened on her wrist as she begins a slow stretch. Gentle hold.
Style: Clean editorial realism, soft morning light, warm neutral palette.
Audio: Music matching @audio1, soft fabric and footstep SFX, quiet room ambience. No dialogue.
Constraints: Preserve product from @image1 and identity from @image2, no text, no logos, no whip pans.
```

## A9. Open Seedance items for Stage 4

- Pick the standard reseller (fal.ai, Replicate, Wavespeed, Dreamina/Volcengine direct). Field names and the exact `@` reference attachment flow differ per host.
- Confirm whether the chosen host exposes 1080p vs caps at 720p, and whether audio generation is on by default.
- Decide whether Sportif's first videos use 1.0 (cheaper, simpler, still hosted) or 2.0 (audio, references). Likely 2.0 for the reference-driven brand consistency.

---

# Part B. GPT Image 2 / ChatGPT Images 2.0 (static)

## B0. What it is, naming, and lineage

The current OpenAI flagship image model is **`gpt-image-2`** (API), snapshot `gpt-image-2-2026-04-21`, branded **ChatGPT Images 2.0** in the product. Launched April 2026. **[official]**

Lineage and a key date:
- DALL-E 2 and DALL-E 3 are being **removed from the API on 2026-05-12**. Treat DALL-E as legacy, do not build on it.
- `gpt-image-1` (and `gpt-image-1-mini`) introduced the token-priced Image API.
- `gpt-image-1.5` (late 2025) was a transitional flagship: about 4x faster than gpt-image-1, stronger editing and image preservation, powered the first "ChatGPT Images" experience.
- `gpt-image-2` (April 2026) is the current flagship.

What is new in gpt-image-2 vs 1.5/1: better instruction following and spatial reasoning, **multilingual understanding and text rendering**, higher and more flexible resolution (up to 4K), and near-pixel-perfect in-image text.

**Myth to avoid:** there is **no separate "thinking mode" API parameter**. Any reasoning you see is orchestration in the ChatGPT assistant layer. The Image API is still prompt plus parameters in, images out. To get planning, use the Responses API (a text model plans, then calls gpt-image-2 as a tool) or iterate with edits.

## B1. Prompt structure

Natural-language brief, no special syntax. 4 to 6 short ordered clauses. **[official]**

1. **Subject and main action**
2. **Context / environment**
3. **Style and camera / rendering details**
4. **Mood and color / lighting**
5. **Text instructions** (group all text together, see B2)
6. **Constraints / quality** (including negative instructions)

Length: about **40 to 160 words** for complex scenes, shorter for simple ones. Short declarative sentences beat one long run-on. State each requirement once.

## B2. In-image text (the headline strength of 2.0)

gpt-image-2 renders text far better than any prior OpenAI model, near pixel-perfect for short copy, and is multilingual. Best practices:

- Quote the **exact string**: `a headline that reads exactly "FOCUS MODE"`.
- Specify **case and punctuation**, **font feel** ("modern geometric sans-serif, bold"), **placement and hierarchy**, **color and contrast**.
- For non-Latin scripts, paste the **exact Unicode** and name the language: `Japanese text that reads "集中モード" in white bold sans-serif`.
- Forbid stray text: `no other text or logos anywhere`.
- Keep it short: headline about 30 to 40 characters. Full paragraphs, dense body copy, and multi-column layouts still fail (misspellings, skipped words). For pixel-perfect paragraphs, generate the layout and imagery, then overlay real copy in a design tool.

## B3. Parameters (gpt-image-2 API)

Endpoints: `images.generate` (text-to-image), `images.edit` (inpainting/outpainting/composition with prompt + image + optional mask), and as a tool in the Responses API.

- **size:** presets `1024x1024` (1:1), `1536x1024` (landscape), `1024x1536` (portrait), plus 16:9 (1920x1088), 9:16 (1088x1920), and 4K (about 3824x2160 or 2160x3824). Custom sizes allowed: each dimension a multiple of 16, total pixels between 655,360 and 8,294,400, aspect ratio under 3:1.
- **quality:** `low` / `medium` / `high`. Trades cost and speed vs fidelity.
- **background / transparency:** **transparent backgrounds are NOT supported on gpt-image-2.** A `background: "transparent"` request fails. If you need a true transparent PNG, use gpt-image-1.5 (keep a dual model path) or generate on a solid background and cut out externally. (This is a regression from gpt-image-1, note it for asset pipelines.)
- **input_fidelity:** do NOT set it. gpt-image-2 runs high input fidelity by default and passing the legacy parameter can error.
- **output_format:** `png` (default), `jpeg`, `webp`.
- **n:** multiple images per request. Each counts toward cost. Use n>1 to explore, n=1 for production.
- **moderation:** implicit, no per-request toggle. Pre-check prompts with the text moderation endpoint or handle refusals in your UX.
- **edits / references:** masks (white = edit, black = preserve), inpainting, outpainting, multi-image composition (up to 16 images in some integrations), style transfer (one image for style, another for subject).

## B4. Pricing (2026, token-based)

Token rates (Microsoft Foundry source): image input about $8 per 1M tokens, image output about $30 per 1M tokens. Per-image estimates (OpenAI direct API):

| Quality | 1024x1024 | 1024x1536 or 1536x1024 | 4K (about 3824x2160) |
|---|---|---|---|
| Low | about $0.01 | about $0.01 | about $0.02 |
| Medium | about $0.06 | about $0.05 | about $0.11 |
| High | about $0.22 | about $0.17 | about $0.41 |

Higher resolution and quality cost more. Edits with reference images add input tokens. Verify against the OpenAI pricing page before building billing logic. Practical pattern: iterate at medium 1024x1024, render hero assets at high or 4K.

## B5. Style techniques and failure modes

**What helps:** be explicit about style not just subject, use camera and layout language, use negative instructions ("no text except the headline," "no people"), keep constraints in short separate sentences, iterate with edits and masks, use reference images for style consistency across a brand set.

| Failure mode | Fix |
|---|---|
| Text inaccuracies | Isolate text instructions, shorten, split lines, increase contrast, "no other text." |
| Unwanted objects/clutter | Forbid explicitly, simplify the environment. |
| Faces/hands off in crowds | Reduce subject count, generate close-ups separately, edit with a mask. |
| Style drift across a batch | Add a style lock ("same lighting, angle, grading"), use a reference image, standardize templates. |
| Composition off | Specify aspect ratio and placement directly, edit with masks to reposition. |
| Product looks decorative, not in use | gpt-image-2 defaults to elegant-but-passive product placement. To show real use, name the exact position and add "stretched taut, clearly under tension, not draped or loose" (field-validated, no aesthetic penalty). |
| Casting drifts across generations | gpt-image-2 will not hold the same model or representation across runs. Specify casting explicitly (age, hair, body type, skin tone) when consistency or specific representation matters. |

## B6. Worked examples (fitness accessory, Sportif-shaped)

Same Sportif rule: aesthetic, lifestyle, function. No health claims.

**Product hero with brand text:**

```text
A high-end product photo of a single pair of matte clay-tone wrist weights
standing upright on a pale linen surface.
Shot from a slightly elevated angle, soft daylight from the left, gentle shadows,
a faint reflection on the surface.
Style: premium minimalist ecommerce photography, sharp focus on the product,
background softly blurred. Color palette: warm neutrals, the product the only
saturated element.
Text instructions: at the top center, add a headline that reads exactly "SPORTIF",
in bold modern geometric sans-serif, warm charcoal, all caps. No other text or logos.
Constraints: 3:2 landscape, calm and editorial mood, no people, no clutter.
```

API: `size: "1536x1024"`, `quality: "high"` for final (`medium` for iterations), `output_format: "jpeg"` for web.

**Note on transparent cutout assets:** gpt-image-2 cannot output transparent backgrounds. For a clean cutout (for example a resistance band to composite into layouts), either generate on a pure white seamless background and cut out in a design tool, or route that specific asset to gpt-image-1.5. Do not rely on `background: "transparent"` here.

## B7. Open gpt-image-2 items for Stage 4

- Decide the transparent-asset path (gpt-image-1.5 dual path vs white-bg-plus-external-cutout). This affects how the Stage 4 adapter emits asset prompts.
- Confirm the exact `quality` and `size` parameter strings against the live `gpt-image-2` model page before writing the adapter parameter block.
- Decide default render tier for Sportif (likely medium 1024 for drafts, high 1536 or 4K for hero).

---

# Part C. Cross-platform cheat sheet

| Dimension | Seedance 2.0 (video) | gpt-image-2 (static) |
|---|---|---|
| Prompt voice | Directorial shot brief (Subject to Constraints) | Natural-language brief, 4 to 6 ordered clauses |
| Length | Concise, shot/timestamp structured | 40 to 160 words |
| References | `@image/@video/@audio` tags, role-assigned, up to 12 | Multi-image input and masks for edits, up to 16 in some hosts |
| Audio | Native, joint, promptable (dialogue, SFX, music, lip-sync) | N/A |
| Text in output | Weak, avoid relying on it | Best-in-class, multilingual, quote exactly, keep short |
| Multi-part | Multi-shot via timestamps in one prompt | One image per call, compose externally |
| Transparency | N/A | NOT supported (regression), use gpt-image-1.5 or external cutout |
| Hard control | resolution, duration, aspect, reference roles | size, quality, output_format, n |
| Pricing signal | Fast tier for iteration, 1080p for hero | medium 1024 to iterate, high/4K for hero (about $0.01 to $0.41/image) |
| Biggest failure | Identity drift + camera chaos + audio desync | Text errors + clutter + transparency assumption |

Unifying principle: front-load the decisions that matter, hold one primary subject / motion / style, assign each reference one clear role, drop buzzword chains, and refine in passes.

---

# Part D. Open items for Stage 4 build

- Confirm `gpt-image-2` live parameter strings (`size`, `quality`, `output_format`) against the model page, and the transparent-asset workaround path.
- Pick the standard Seedance 2.0 reseller and confirm its `@`-reference attachment flow, resolution cap, and audio default.
- Decide per platform whether Sportif starts on the 2.0 model or the cheaper 1.x.
- When Lucy's Q12 timeline answer is in, decide which adapter to build first (video vs static) based on Sportif's first content need.
- Watch for further version moves. Both vendors shipped a major release in April 2026, the cadence is fast. Re-run a deep-research refresh before each big Sportif production batch.

---

# Sources

**Seedance (1.0 baseline + 2.0)**
1. Official launch of Seedance 2.0, ByteDance Seed blog: https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0
2. Seedance 2.0, ByteDance Seed: https://seed.bytedance.com/en/seedance2_0
3. Seedance 2.0 the complete guide, Scenario: https://help.scenario.com/articles/7140699840-seedance-2-0-the-complete-guide
4. Seedance 2.0 prompt template, Wavespeed: https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/
5. Seedance 2.0 complete prompting guide, Higgsfield: https://higgsfield.ai/blog/seedance-prompting-guide
6. Seedance 2.0 prompt guide, RunDiffusion: https://www.rundiffusion.com/seedance-2-0-prompt-guide
7. Timeline prompting with Seedance 2.0, MindStudio: https://www.mindstudio.ai/blog/timeline-prompting-seedance-2-cinematic-ai-video/
8. Seedance 2.0 API live on fal (April 2026): https://fal.ai/seedance-2.0
9. Seedance 2.0 pricing breakdown 2026, Atlas Cloud: https://www.atlascloud.ai/blog/case-studies/seedance-2.0-pricing-full-cost-breakdown-2026
10. How to make videos with Seedance 2.0, Replicate blog: https://replicate.com/blog/seedance-2
11. Seedance 1.0, ByteDance Seed (baseline): https://seed.bytedance.com/en/seedance
12. Seedance 1.0 paper, arXiv: https://arxiv.org/html/2506.09113v1
13. Seedance 1.0 Pro image-to-video, fal.ai (baseline): https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/image-to-video

**GPT Image (1.x baseline + 2)**
14. Introducing ChatGPT Images 2.0, OpenAI: https://openai.com/index/introducing-chatgpt-images-2-0/
15. GPT Image 2 model page, OpenAI API: https://developers.openai.com/api/docs/models/gpt-image-2
16. Image generation guide, OpenAI API: https://developers.openai.com/api/docs/guides/image-generation
17. GPT Image generation models prompting guide, OpenAI cookbook: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
18. The new ChatGPT Images is here (gpt-image-1.5), OpenAI: https://openai.com/index/new-chatgpt-images-is-here/
19. Deprecations (DALL-E removal 2026-05-12), OpenAI API: https://developers.openai.com/api/docs/deprecations
20. GPT Image 2 in Microsoft Foundry (params + token pricing): https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-openais-gpt-image-2-in-microsoft-foundry/4500571
21. GPT Image 2 API guide (params + per-image pricing), WaveSpeed: https://wavespeed.ai/blog/posts/gpt-image-2-api-guide/
22. GPT Image 2 docs (pricing table), gpt-image-2.art: https://gpt-image-2.art/docs
23. ChatGPT Images 2.0 reasoning, 2K, multilingual, Neurohive: https://neurohive.io/en/news/chatgpt-images-2-0-openai-launches-image-generation-model-with-reasoning-2k-resolution-and-multilingual-text/

Raw research output is preserved at outputs/research/ (round 1: seedance-a/b.md, chatgpt-a/b.md; round 2: seedance2-raw.md, seedance2-prompts.md, gptimage2-raw.md, gptimage2-prompts.md; async fix test: async-test.*).
