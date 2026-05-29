OpenAI’s **gpt-image-2** is a token‑metered image model exposed via the Image API (`images.generate`, `images.edit`) and as a tool in the Responses API.[7][4] It improves instruction following, multilingual understanding, resolution flexibility, and text rendering over gpt-image‑1.x.[6][8] Below is a practical, implementation‑oriented guide based primarily on OpenAI docs plus closely aligned partner docs.

---

## 1. Prompt structure & “thinking” for gpt-image-2

There is no special syntax; **natural language briefs** work best.[7] For production, treat prompts like a compact creative brief.

### Recommended prompt structure (order)

Use 4–6 short sentences or bullet‑like clauses, in this order:

1. **Subject & main action**
2. **Context / environment**
3. **Style & camera / rendering details**
4. **Mood & color / lighting**
5. **Text instructions (if any)**
6. **Constraints / quality instructions**

Example structure:

> A close-up product photo of a matte black wireless mouse on a white desk.  
> Shot from a 45-degree angle, shallow depth of field, soft daylight from the left.  
> Ultra-clean ecommerce style, no props, pure white background.  
> High detail, no motion blur, realistic shadows.  
> Add centered headline text above the mouse: “Focus Mode”, in bold modern sans-serif, all caps.

Why this works:

- gpt-image-2 is optimized for **instruction‑like, ordered descriptions**; it follows explicit constraints well.[6][7]  
- Grouping all **text-in-image** instructions together makes typography more reliable.  
- Listing **negative constraints** (“no props”, “no text except…”) helps reduce common failures.

### Prompt length

- **Best range**: ~40–160 words for complex scenes; short prompts work for simple scenes.  
- Avoid long story‑like paragraphs; prefer **short, declarative sentences** or comma‑separated clauses.  
- Keep **each requirement explicit once**, not repeated in different ways (can confuse style).

OpenAI’s image generation guide emphasizes clear, specific instructions, with enough context to disambiguate style and subject, rather than extremely short or extremely long prompts.[7]

### New vs gpt-image-1.x (including “thinking mode”)

From OpenAI and partner docs:

- **Improved instruction following & fidelity**: gpt-image-2 better respects prompt constraints than gpt-image‑1, especially for composition and text.[6][8]
- **Multilingual understanding** is improved; prompts and text rendering work across more languages.[6][8]
- **Higher and more flexible resolutions** including 4K, and custom sizes under a pixel budget with 16‑pixel alignment.[6][2]
- **Routing / configuration intelligence**: systems (Azure Foundry, OpenAI’s internal routing) can select size tiers or token buckets automatically to balance quality and cost.[6]

As of the available docs, there is **no separate “thinking mode” parameter** (like a toggled reasoning mode) for gpt-image-2. Any “thinking” you see in ChatGPT UI is orchestration in the assistant layer; the underlying Image API remains: prompt + parameters in, images out.[7][2] You *can* simulate chain‑of‑thought visually by:

- Using the **Responses API** so a GPT‑4.* text model plans and refines the prompt, then calls gpt-image-2 as a tool.[2][7]
- Iterating with **edits**: generate a base, then progressively refine via `images.edit` with masks and updated prompts.[7][2]

---

## 2. In‑image text rendering (quality, multilingual, control, limits)

### How good is the text now?

OpenAI’s ChatGPT Images 2.0 announcement highlights **“improved text rendering”** and **near‑pixel‑perfect text** in many cases.[8] Partner platforms describe gpt-image-2 as capable of **“pixel-perfect text rendering”** for design‑like tasks and product imagery.[3]

In practice (from docs and partner guidance):

- Text is **much more reliable** than gpt-image‑1.x for:
  - Single slogans, labels, UI mock text.
  - Simple layouts (headline + subhead, short labels).
- Production use is viable when you:
  - Keep the amount of text modest.
  - Specify the exact text and style clearly.
  - Avoid complex long paragraphs.

### Multilingual text

- gpt-image-2 provides **“multilingual understanding”** at the model level, including for prompts and generated content.[6][8]
- This extends to **in‑image text**: you can request text in different languages/scripts as long as you supply the exact characters in the prompt.

For best results:

- Paste the **exact Unicode** text you want.
- Avoid mixing languages in a single line unless necessary.
- For non‑Latin scripts, specify also the language: e.g. “Japanese text that reads ‘集中モード’ in white bold sans-serif”.

### How to specify exact text & typography

Use a dedicated section in the prompt, as if briefing a designer:

- **Exact string**:
  - “Add a headline that reads exactly: ‘Work. Flow. Focus.’”
  - Use quotes around the full string.
- **Case and punctuation**:
  - “All caps, no extra punctuation.”  
  - “Keep the period at the end.”
- **Font style (type family, weight, feel)**:
  - “Modern geometric sans-serif similar to Futura, bold.”
  - “Elegant high-contrast serif like a fashion magazine.”
- **Placement & hierarchy**:
  - “Headline centered at the top.”
  - “Small label text on the coffee cup near the middle.”
- **Color & contrast**:
  - “White text on a dark blue background with strong contrast.”
- **No extra text**:
  - “No text anywhere else in the image.”

Example text block:

> Text instructions:  
> - Add a large centered headline at the top: “FOCUS MODE”.  
> - All caps, bold geometric sans-serif, pure white.  
> - Add a small tagline under it: “Deep work, zero noise.” sentence case, light weight.  
> - No other visible text or logos.

### Current limits on amount of text

OpenAI does not publish a numeric “max characters of text” limit inside images, but the behavior across docs and guidance is:

- **Best:** short phrases, titles, short taglines, small UI labels.  
- **Risky:** full paragraphs, multi‑column layouts, dense body copy.  
- **Failure modes** with too much text:
  - Misspellings, letter substitutions.
  - Skipped words.
  - Layout not matching exact line breaks.

Practical rules for near‑production usage:

- Keep **headline ≤ 30–40 characters**, subheadlines similar.
- For UI screens or posters, treat each block of text as **short, high‑level copy**, not real T&Cs or article text.
- If you need pixel‑perfect paragraphs, use gpt-image-2 for layout & imagery, then overlay text programmatically with a design tool.

---

## 3. API reference: parameters & capabilities (gpt-image-2)

### Endpoints & surfaces

From OpenAI’s image guide and partner docs:

- **Image API endpoints** (OpenAI):  
  - `images.generate` – text‑to‑image generation.[7]  
  - `images.edit` – edits/inpainting/outpainting with prompt + image + optional mask.[7][2]
- **Responses API**: image generation is available as a **built‑in tool** in multi‑turn flows.[2][7]
- **Multi‑image edit / composition**:
  - Supports multiple reference images to combine subjects/styles.[7][2][5]

### Size & aspect ratio

Microsoft’s Foundry integration and partner docs align on size rules for gpt-image-2:

- **Fixed presets** commonly used:[6][1][2]
  - 1024×1024 (1:1)
  - 1536×1024 (≈3:2 landscape)
  - 1024×1536 (≈2:3 portrait)
  - 4K (e.g. 3824×2160 or 2160×3824)[1][6]
- **Aspect ratios** often exposed by partner tooling:[1]
  - 1:1
  - 3:2 (landscape 1536×1024)
  - 2:3 (portrait 1024×1536)
  - 16:9 (1920×1088)
  - 9:16 (1088×1920)
  - 4K variants (3824×2160 or 2160×3824)

Core technical constraints for gpt-image-2 (Microsoft Foundry + WaveSpeed):[6][2]

- **Each dimension must be a multiple of 16.**[6][2]
- **Total pixels**:
  - Minimum: 655,360 pixels.[6]
  - Maximum: 8,294,400 pixels (≈ 4K).[6]
  - Requests outside this range are automatically resized to fit.[6]
- **Aspect ratio**:
  - Maximum aspect ratio under **3:1**.[2]

So for custom sizes via the OpenAI API:

- Choose width/height multiples of 16.
- Respect pixel budget and aspect ratio < 3:1.
- You can specify direct dimensions (where supported) or choose a preset like `"1024x1024"` depending on the client surface.

### Resolution tiers (up to 2K, 4K)

From official & partner docs:[6][1][2]

- Supported **resolution tiers** for gpt-image-2:
  - ~1K class: 1024×1024, 1536×1024, 1024×1536.
  - **4K class:** ~3824×2160 or 2160×3824 (within 8.29M pixel budget).[1][6]
- Some integrations label tiers as:
  - `smimage` (small), `image` (standard), `xlimage` (large/4K), or token bucket sizes 16–96 mapped to those.[6]

OpenAI’s direct Image API uses size options consistent with these; client libraries may abstract them behind presets or routing.

### Quality tiers (low / medium / high)

gpt-image-2 supports **multiple quality levels**.[5][1][2]

Typical quality labels in partner and pricing docs:

- `low`
- `medium`
- `high`

WaveSpeed describes cost differences for **low/medium/high** at different resolutions, mapping to token usage.[2][1] You choose quality in the API request (exact parameter often `quality`), trading cost and speed vs fidelity.

### Background / transparency

- **Transparent backgrounds are not supported** by gpt-image-2.[2]
  - Requests like `background: "transparent"` will fail.[2]
  - If you need true transparent PNGs, you must use another model (e.g. gpt-image‑1.5) and maintain dual model paths.[2]
- For solid backgrounds, specify in the prompt:
  - “Pure white seamless studio background”  
  - “Solid #111111 dark gray background”

### `input_fidelity`

- WaveSpeed notes: gpt-image-2 effectively runs with **high input fidelity by default**, and the legacy `input_fidelity` parameter **must not be set**; including it can cause errors.[2]
- In other words:
  - Edits respect input images strongly.
  - You cannot dial input fidelity lower via that parameter as was possible on some earlier models.

### `output_format`

Common formats (as documented by partners, consistent with OpenAI Image API behavior):[2][5]

- Defaults to **PNG**.
- You can request:
  - `png`
  - `jpeg` (often faster / smaller, good for previews)[2]
  - `webp` (where exposed by client).

Choose based on your pipeline:

- PNG if you need lossless edges or further editing.
- JPEG or WebP when latency and file size are more important.

### `n` (number of images)

- The Image API exposes an **`n` parameter** to generate multiple images per request.[2][7]
- Each image counts against your token (and cost) budget. Use `n > 1` for exploration; use `n = 1` for production to minimize spend.

### Moderation

- The image generation guide stresses that all generations go through **safety and moderation filtering**; disallowed content is blocked or altered.[7]
- As of now, moderation is **implicit** for gpt-image-2; there is no public per‑request moderation toggle.  
  You can optionally:
  - Pre‑check prompts with the **separate text moderation endpoint**, or
  - Handle blocked responses and rephrase prompts in your app’s UX.

### Reference image / editing inputs

From OpenAI’s guide and partner docs:[7][2][5]

- `images.edit` accepts:
  - One or more **input images** (base64 or file URL).
  - An optional **mask** image:
    - White = region to edit.
    - Black = region to preserve.
- Capabilities:
  - **Inpainting**: modify only masked areas.
  - **Outpainting**: extend canvas beyond original boundaries (respecting size constraints).
  - **Multi‑image composition**: up to **16 images** in some integrations for composing subjects/styles.[5]
  - **Style transfer**: use one image for style, another for subject (via prompt + multi‑image input).[5][2]
- All inputs are processed at high fidelity and counted as **image input tokens**.[2][6]

---

## 4. Pricing in 2026 (token-based, by resolution & quality)

OpenAI has moved image billing for gpt-image-2 to a **token‑based** model, but some partner docs still present **per‑image estimates**.

### Official OpenAI token pricing (Microsoft Foundry source)

Microsoft’s Foundry documentation for GPT-image-2 (standard global offer) states:[6]

- **Image input tokens**:  
  - $8 per 1M tokens  
  - $2 per 1M cached input tokens
- **Image output tokens**:  
  - $30 per 1M tokens  
- **Text input tokens** (when used via Responses API etc.):  
  - $5 per 1M tokens  
  - $1.25 per 1M cached input tokens

They also note:

- “There is no billing for output tokens for the GPT-image-2 model” in their table context for text output; however, image output tokens are explicitly priced at $30/1M tokens.[6]  
- Token counts scale with image dimensions and quality; larger and higher‑quality images consume more output tokens.

### Per‑image price estimates by resolution & quality

WaveSpeed (using OpenAI’s token calculator) gives concrete estimates for the OpenAI **direct API** at the `v1/images/generations` endpoint:[2][1]

For **1024×1024**:

- **Low quality:** ≈ **$0.006** per image.[2]
- **Medium quality:** ≈ **$0.053** per image.[2]
- **High quality:** ≈ **$0.211** per image.[2]

For **1024×1536** or **1536×1024**:

- **Low:** ≈ **$0.005**  
- **Medium:** ≈ **$0.041**  
- **High:** ≈ **$0.165**[2]

For **4K (≈3824×2160)**:

- Partner docs (gpt-image-2.art) list **$0.41** for high quality, **$0.11** for medium, **$0.02** for low.[1]

gpt-image-2.art explicitly states these prices are **OpenAI direct API pricing** via `v1/images/generations`:[1]

| Quality | 1024×1024 | 1024×1536 | 1536×1024 | 4K (3824×2160) |
|--------|-----------|-----------|-----------|----------------|
| Low    | $0.01     | $0.01     | $0.01     | $0.02          |
| Medium | $0.06     | $0.05     | $0.05     | $0.11          |
| High   | $0.22     | $0.17     | $0.17     | $0.41          |

Note that these per‑image figures and WaveSpeed’s are both based on **OpenAI’s token rates**; minor discrepancies reflect estimation vs rounding or caching assumptions.

Key practical points:

- **Higher resolution and quality** → noticeably higher cost.  
- **Batch processing** may get discounted token rates; WaveSpeed notes batch processing can halve standard rates for some billing arrangements.[2]
- Edits with reference images add **image input tokens** on top of output cost.[2]

Always verify against OpenAI’s current **official pricing page** when implementing billing logic, as prices can change.

---

## 5. Style/quality prompting techniques & common failure modes

### Techniques for better style & quality

1. **Be explicit about style, not just subject**

   - “Cinematic, shallow depth of field, 35mm lens, natural skin tones”  
   - “Flat vector illustration, clean outlines, minimal shading, pastel color palette”  
   - “High‑end product photography, studio lighting with soft boxes, reflections controlled”

2. **Control composition**

   - Use camera terms: “wide shot”, “medium shot”, “close-up”, “overhead”, “isometric view”.  
   - Use layout language: “subject centered”, “rule of thirds, subject on left, empty space on right”.

3. **Use negative instructions**

   - “No text except the main headline.”  
   - “No people, only objects and abstract shapes.”  
   - “No motion blur, no bokeh.”

4. **Separate constraints into short sentences**

   - gpt-image-2 follows clear, unambiguous sentences more reliably than a long stylistic run‑on prompt.[7][6]

5. **Iterate with edits**

   - Generate a base at **medium quality 1024×1024** to explore.  
   - Once composition is right, upscale/refine at higher resolution or with a 4K edit.  
   - Use masks to adjust only problematic regions (faces, hands, text).

6. **Use reference images for style consistency**

   - For product lines or brand visuals, use `images.edit` or multi‑image inputs to maintain consistent lighting, backgrounds, or color grading across assets.[5][2]

### Common failure modes & fixes

1. **Text inaccuracies (spelling, extra text)**

   - *Symptoms*: Letters swapped, extra characters, random small text elsewhere.
   - *Fixes*:
     - Isolate text instructions: “Add text: ‘FOCUS MODE’. No other text anywhere.”  
     - Shorten text; split into two lines rather than many words on one line.  
     - Increase contrast and specify placement clearly.

2. **Unwanted objects or clutter**

   - *Symptoms*: Extra people, props, or logos appear.
   - *Fixes*:
     - Explicitly forbid them: “No people, no logos, no additional objects.”  
     - Use simpler environments: “plain white background” instead of “modern office with many desks”.

3. **Faces / hands slightly off in complex scenes**

   - *Symptoms*: Subtle anatomical issues in crowded scenes.
   - *Fixes*:
     - Reduce crowd size: specify “one person” or “two people”.  
     - Generate face close‑ups separately and composite later.  
     - Use `images.edit` with a mask on problem areas to refine.

4. **Style drift across a batch**

   - *Symptoms*: Same prompt, multiple images, but style varies more than desired.
   - *Fixes*:
     - Add a very explicit “style lock”: “Same lighting, camera angle, and color grading across all outputs.”  
     - Include a reference image for style via `images.edit` or multi‑image composition.[5][2]  
     - In production, standardize prompt templates for each asset type.

5. **Composition not matching expectations**

   - *Symptoms*: Subject cropped oddly, text overlaps subject.
   - *Fixes*:
     - Specify aspect ratio and composition directly: “vertical 9:16, subject centered in the lower third, headline in top third.”[1]  
     - Use edits with masks to reposition or resize elements.

---

## 6. Two strong example prompts with explanations

### Example 1 – Marketing hero image with text

**Prompt:**

> A high-end product photo of a matte black wireless keyboard on a clean white desk.  
> Shot from a slightly elevated 45-degree angle, with soft natural daylight coming from the left, gentle shadows, and subtle reflections on the keys.  
> Style: premium ecommerce photography, minimalistic, sharp focus on the keyboard, background softly blurred.  
> Color palette: neutral whites and grays, with the keyboard as the only dark element.  
> Text instructions: At the top center of the image, add a large headline that reads exactly “FOCUS MODE”. All caps, bold modern geometric sans-serif, pure black text. No other text, logos, or icons anywhere in the image.  
> The overall mood is calm, focused, and professional, suitable for a landing page hero section.

**Why this works (for gpt-image-2):**

- Clear **subject** and **composition** in sentence 1–2.  
- Explicit **style** and **lighting** in sentence 2–3.  
- **Color palette** constraints reduce unexpected colors.  
- Text is treated as a separate section with:
  - Exact wording in quotes.
  - Case, font style, color, and placement defined.
  - “No other text” to avoid random labels.  
- This plays to gpt-image-2’s strengths in high‑quality product imagery and improved text rendering.[6][8]

For the API, you might pair this with:

- `size: "1536x1024"` (landscape hero).[1][6]  
- `quality: "high"` for final export; `medium` for iterations.[1][2]  
- `output_format: "jpeg"` for web performance.[2]

---

### Example 2 – Multilingual poster with controlled typography

**Prompt:**

> A bold minimalist poster design for a productivity app, in portrait orientation.  
> A dark navy blue background with a subtle gradient from top to bottom.  
> In the upper half, a simple flat illustration of a person working at a laptop, drawn in a clean vector style with smooth shapes and no outlines.  
> Color palette: navy blue, teal, and white only.  
> Text instructions: Centered below the illustration, add a large headline in Japanese that reads exactly “集中モード”. Use pure white, heavy-weight sans-serif, all characters the same size, with generous letter spacing.  
> Below the headline, add a smaller English tagline: “Deep work, no distractions.


## Sources

1. [GPT Image 2 Docs & Free Generator - No API Key Required](https://gpt-image-2.art/docs)
2. [GPT Image 2 API Guide for Generation and Editing | WaveSpeed Blog](https://wavespeed.ai/blog/posts/gpt-image-2-api-guide/)
3. [GPT Image 2 | State-of-the-Art Image Model live on fal - Fal.ai](https://fal.ai/gpt-image-2)
4. [GPT Image 2 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-image-2)
5. [OpenAI GPT Image 2 - Cloudflare Docs](https://developers.cloudflare.com/ai/models/openai/gpt-image-2/)
6. [Introducing OpenAI's GPT-image-2 in Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-openais-gpt-image-2-in-microsoft-foundry/4500571)
7. [Image generation | OpenAI API](https://developers.openai.com/api/docs/guides/image-generation)
8. [Introducing ChatGPT Images 2.0 - OpenAI](https://openai.com/index/introducing-chatgpt-images-2-0/)
9. [GPT Image 2 Is Here — Everything You NEED to Know - YouTube](https://www.youtube.com/watch?v=blOlUnC75O4)
10. [GPT Image 2 API | Runware Docs](https://runware.ai/docs/models/openai-gpt-image-2)
