Seedance 1.0 / Seedance Pro currently has **very little “official” prompt-engineering documentation**, but between the ByteDance paper, the Seed product page, and host‑API docs (AI.cc, Pollo, AIMLAPI, fal.ai), you can infer fairly consistent behavior and parameter support.[1][2][5][7][9] Below is what is known and what is strongly inferred, with a bias toward sources that explicitly expose the model’s controls.

---

### 1. Recommended prompt structure & style

**How Seedance parses prompts**

ByteDance’s paper repeatedly emphasizes “accurate instruction adherence” to **natural‑language prompts**, including complex actions and rich camera movement.[2][5][9] A Seedance overview video notes that it “accurately parses natural language prompts enabling stable control over multi‑agent interactions, complex action sequences, [and] rich variety of camera movements.”[6] This indicates the model is primarily tuned for **natural prose**, not short keyword lists.

Unofficial integrator docs (AI.cc, Pollo, AIMLAPI) all show the `prompt` as a free‑form string with no special syntax, and no mention of comma‑only keyword style.[1][3][7]

**Recommended structure (highly compatible with how Sora/Runway/etc. are trained)**

From model behavior described in the paper and demos, plus general video‑model practice, the most reliable structure is:

1. **Subject & identity**
2. **Action & behavior**
3. **Scene / environment**
4. **Camera movement & framing**
5. **Lighting & atmosphere**
6. **Style, medium & quality hints**

You can write this as **1–2 descriptive sentences**, optionally followed by a shorter “style line”.

**Example structure (text‑to‑video)**

> A **young woman in a red raincoat** walks briskly through a **neon‑lit city street at night**, rain falling around her and reflections on the wet pavement.  
> The **camera slowly pushes in** from a wide shot to a medium close‑up, with **handheld, slightly shaky motion**. **Moody, high‑contrast lighting**, cinematic, shot on 35mm, shallow depth of field.

Broken down:

- **Subject** – “young woman in a red raincoat”
- **Action** – “walks briskly”
- **Scene** – “neon‑lit city street at night, rain, reflections”
- **Camera** – “camera slowly pushes in from a wide shot to a medium close‑up, handheld…”
- **Lighting** – “moody, high‑contrast”
- **Style** – “cinematic, shot on 35mm, shallow depth of field”

**Prose vs comma‑lists**

- ByteDance and integrator materials implicitly assume **full sentences / descriptive prose**.[2][5][6][9]
- Comma‑lists (“woman, red coat, city, night, neon, cinematic”) also work, but you get **better control** over motion and staging when you spell out the relationships: *who does what, where, with which camera movement*.
- Best practice: **short, clear sentences**, with specific camera verbs (see section 3).

---

### 2. Recommended prompt length / limits

No public ByteDance or Volcengine spec gives a strict token/character limit for Seedance prompts.[2][5][9] However:

- The AI.cc Seedance Pro spec describes the model as having “strong prompt adherence” and being used via generic LLM/video APIs that typically accept **hundreds of tokens**, not just a short caption.[1]
- AIMLAPI’s Seedance Lite docs show the `prompt` as a simple string field with no small hard cap indicated.[3]
- No host (AI.cc, Pollo, fal.ai, AIMLAPI) mentions truncation at very short lengths, which they do mention for some other models.

**Practical guidance (inferred from similar video models and API behavior):**

- Keep prompts in the range of **20–120 words** (roughly **150–800 characters**) for best control.  
- Beyond ~200–250 words, many video models start ignoring tail details; Seedance is likely similar.
- Put **critical instructions early**: subject → action → scene → camera → lighting → style.

**Example lengths**

- **Short, controlled (≈35 words)**  
  > A small orange cat jumps from a couch to a window sill in a sunny living room. Side‑view shot. Camera remains fixed. Soft daylight, cozy atmosphere, realistic style.

- **Medium, detailed (≈85 words)**  
  > A middle‑aged man in a blue business suit sits alone at a train station at dawn, reading a newspaper as a train slowly passes behind him. The camera starts in a wide establishing shot, then slowly dollies in to a medium close‑up, keeping him centered. Soft, cool morning light with subtle fog in the distance. Realistic, cinematic style, shallow depth of field, 24 fps film look.

---

### 3. Camera & motion vocabulary, motion intensity, multi‑shot prompting

#### 3.1 What camera terms does Seedance respond to?

ByteDance’s description emphasizes “rich variety of camera movements” and “precise prompt following” for camera instructions, but does not list a canonical vocabulary.[6][9] In practice, it follows the **standard film‑language verbs** that are also used in model demos and third‑party docs:

Commonly effective:

- **Push in** (move camera closer)
- **Pull out** / **push out** (move camera away)
- **Dolly in / dolly out** (similar to push/pull along a track)
- **Truck / track left/right** (move sideways)
- **Pan left/right** (rotate camera horizontally in place)
- **Tilt up/down** (rotate vertically in place)
- **Orbit around** / **circling around** the subject
- **Zoom in/out** (change focal length, not camera position)
- **Handheld**, **steady**, **locked‑off** / **fixed camera**  
  – the Pollo and AIMLAPI docs explicitly expose a `cameraFixed` boolean parameter, confirming that “fixed camera / no movement” is a supported behavior.[3][7]
- **Static shot**, **wide shot**, **medium shot**, **close‑up**, **over‑the‑shoulder**, **bird’s‑eye**, **low‑angle**, etc. – commonly respected by video models and consistent with Seedance’s emphasis on cinematic control.[1][2][5][6]

Because the paper and Seed site state that it can “precisely translate your textual concepts into videos” including camera movements, these are reliable terms.[2][5][6][9]

**Camera control examples**

- **Push in**:  
  > The camera slowly pushes in from a wide shot to a tight close‑up on her face.

- **Pan and tilt**:  
  > Start with a static shot of the city skyline at dusk, then slowly pan right and tilt down to reveal the bustling street below.

- **Orbit**:  
  > The camera orbits 360 degrees around the dancer, keeping her centered in frame.

- **Static / fixed**:  
  > The camera is completely fixed and does not move, like a tripod‑mounted shot.

Note: For “fixed” behavior you can also use the **parameter** `cameraFixed: true` where supported (see section 4).[1][3][7]

#### 3.2 Controlling motion intensity

There is no explicit numeric “motion scale” parameter in public docs, but AI.cc and Pollo mention “configurable motion dynamics (such as `cameraFixed`)” and “smooth motion,” implying the control is **prompt‑based plus a fixed‑camera flag**.[1][7]

Effective pattern:

- Use **adverbs/adjectives** to specify intensity:
  - “very slow,” “slow,” “smooth,” “gentle,” “slight”
  - “fast,” “quick,” “rapid,” “energetic,” “aggressive”
- Limit each shot to **one primary movement** for reliability.

Examples:

- **Subtle**:  
  > The camera makes a very slow, subtle push in, barely noticeable over the 5‑second shot.

- **Strong**:  
  > The camera rapidly dollies in toward the character, creating a dramatic, high‑energy move.

Combined with `cameraFixed: true` you can get almost **zero camera motion** if desired.[1][3][7]

#### 3.3 Multi‑shot / sequential‑shot prompting

Seedance 1.0’s key selling point is **native multi‑shot narrative coherence**.[2][5][6][9] The Seed page and video emphasize that it:

- “supports multi‑shot video generation from both text and image”[5]
- can maintain “consistency in the main subject, visual style and atmosphere across shot transitions and temporal spatial shifts.”[6]

The paper describes narrative videos made from a single prompt that internally contains multiple shots.[9]

However, no public API docs expose a “shot list” JSON; multi‑shot is driven by **structured text in a single prompt**.

**Prompt pattern for multiple shots**

Use numbered or clearly segmented shot descriptions:

> Shot 1: Wide aerial shot of a futuristic city at sunrise, the camera slowly flying forward over the skyline.  
> Shot 2: Cut to a street‑level view with a young woman walking through the crowd, the camera tracking alongside her at a medium shot.  
> Shot 3: Cut to a close‑up of her face as she looks up at a giant holographic billboard, the camera holding steady.

Guidelines:

- Use explicit markers like **“Shot 1: … Shot 2: … Shot 3: …”** or “Scene 1 / Scene 2”.
- For 5–10 s clips, **2–3 shots** is realistic; more will compress action heavily.
- Keep **consistent subject identifiers** (“the same woman”) so Seedance can maintain identity, which the paper says it is trained to do.[2][6][9]

---

### 4. Supported parameters: resolution, duration, aspect, fps, seed, consistency

Here we rely on **host APIs that explicitly expose Seedance Pro** plus hints from the Seedance 1.0 paper and Seed site.

#### 4.1 Resolution

- AI.cc Seedance Pro spec:  
  – “Resolution Output: **480p or high-definition 1080p**.”[1]  
- Pollo Seedance Pro API allows `"resolution": "480p"` in requests and implies 1080p as default or alternative.[7]

So, currently documented resolutions:

- **480p** (SD)
- **1080p** (Full HD)

There is **no explicit mention of 720p** in the Seedance 1.0 Pro docs or the AI.cc feature list.[1][7] If 720p exists, it is not publicly documented; assume 480p or 1080p for now.

Example (Pollo):

```json
"input": {
  "prompt": "A cinematic night city scene with neon lights and rain.",
  "resolution": "480p",
  "length": 5,
  "seed": 123,
  "cameraFixed": false
}
```
[7]

#### 4.2 Duration

- AI.cc: “Max Duration: **10 seconds** for generated videos.”[1]  
  It also states Seedance 1.0 can “generate 5–10 second videos in stunning 1080p resolution.”[1]
- ByteDance’s Seedance site and paper show 5‑second 1080p demos, but the AI.cc spec is explicit about 10 s max.[1][2][5][9]
- Pollo’s API shows `"length": 5` as an example field.[7]

So, supported durations:

- Minimum typically **5 seconds**; many demos use 5 s.[6][9]
- Maximum **10 seconds** (documented by AI.cc for Seedance 1.0 Pro).[1]
- Host APIs usually accept discrete values like **5** or **10** seconds via a `length` field.[1][7]

#### 4.3 Aspect ratios

AI.cc lists “Aspect Ratios: Comprehensive support including **16:9, 9:16, 1:1, 3:4, 4:3, and 21:9**.”[1]

The exact input field name depends on host API (e.g. `aspect_ratio` or `ratio`), but these are the **explicitly documented ratios** Seedance Pro supports through AI.cc.[1]

Common mappings:

| Ratio | Use case              |
|-------|-----------------------|
| 16:9  | Standard landscape    |
| 9:16  | Vertical / mobile     |
| 1:1   | Square, social feeds  |
| 3:4   | Portrait-ish          |
| 4:3   | Classic TV            |
| 21:9  | Ultra‑wide cinematic  |

If your host doesn’t expose aspect controls yet, you may be locked to 16:9.

#### 4.4 Frame rate (fps)

AI.cc: “Supported Frame Rates: **24 FPS** (standard cinematic), **30 FPS** (for certain image‑to‑video outputs).”[1]

So:

- **24 fps** – default and recommended for cinematic text‑to‑video[1]  
- **30 fps** – may be used for some image‑to‑video configurations[1]

The API might not let you pick fps explicitly; it can be implicit based on endpoint (text vs image‑to‑video).

#### 4.5 Seed & consistency controls

Seed and deterministic generation are explicitly documented:

- AI.cc: “deterministic video generation through reliable **seed control**.”[1]  
- fal.ai Seedance Pro I2V example includes `"seed": 42` and returns a deterministic video.[4]
- Pollo: `"seed": 123` shown in the Seedance Pro request body.[7]

So:

- **Seed** is an integer; same prompt + same seed → **highly similar or identical output**, subject to host implementation.[1][4][7]
- You can use seeds to:
  - Iterate on **prompt phrasing** while keeping motion/composition similar.
  - Generate **variants** by changing seed value.

For temporal consistency **within** a video, ByteDance’s paper describes architectural choices to maintain structure and subject identity; that is automatic and not user‑configurable beyond using coherent prompts and seeds.[2][6][9]

#### 4.6 CameraFixed and motion

The most explicit non‑prompt control is the **fixed camera flag**:

- AI.cc mentions “configurable motion dynamics (such as `cameraFixed`).”[1]
- Pollo’s Seedance Pro API example includes `"cameraFixed": false` in the `input`.[7]
- AIMLAPI’s Seedance Lite docs explicitly say you can “keep the camera fixed throughout the entire clip.”[3]

So, supported motion parameter:

- **`cameraFixed`: boolean**  
  - `true` → camera locked, no movement (only subject/object motion).  
  - `false` → allow camera moves as described in prompt.[1][3][7]

Use this in combination with natural language camera instructions.

---

### 5. Concrete example prompts & full request examples

#### 5.1 Text‑to‑video, single cinematic shot (Pro)

**Prompt (≈70 words)**

> A lone astronaut in a white spacesuit stands on the edge of a rocky cliff on Mars, looking out over a vast red desert with dust storms on the horizon. The camera slowly dollies in from a wide shot to a medium shot behind him, over his shoulder, revealing the landscape. Golden hour lighting, long shadows, cinematic, 24 fps, realistic style.

If using a Pollo‑style API wrapper around Seedance Pro:[7]

```json
{
  "input": {
    "prompt": "A lone astronaut in a white spacesuit stands on the edge of a rocky cliff on Mars, looking out over a vast red desert with dust storms on the horizon. The camera slowly dollies in from a wide shot to a medium shot behind him, over his shoulder, revealing the landscape. Golden hour lighting, long shadows, cinematic, 24 fps, realistic style.",
    "resolution": "1080p",
    "length": 10,
    "seed": 98765,
    "cameraFixed": false
  }
}
```

#### 5.2 Text‑to‑video, multi‑shot sequence

**Prompt**

> Shot 1: Wide aerial shot of a bustling Tokyo street at night, neon signs glowing in the rain as cars and people move below. The camera slowly glides forward, high above the street.  
> Shot 2: Cut to a ground‑level tracking shot following a young man with an umbrella from behind as he walks through the crowd. The camera tracks alongside him at a medium shot.  
> Shot 3: Cut to a close‑up of his face as he looks up at a giant holographic billboard, the camera holding completely still. Moody, high‑contrast lighting, cinematic style.

Use `length: 10` and `resolution: "1080p"` to give the model enough time to transition between the three shots.[1][7]

#### 5.3 Image‑to‑video (Seedance Pro on fal.ai)

Fal.ai example (simplified from docs):[4]

```typescript
const result = await fal.subscribe(
  "fal-ai/bytedance/seedance/v1/pro/image-to-video",
  {
    input: {
      image_url: "YOUR_IMAGE_URL",
      prompt: "The image comes to life as the camera slowly orbits around the subject in a smooth 360 degree motion, keeping the subject centered. Gentle, cinematic movement, 24 fps.",
      seed: 42
    }
  }
);
```
[4]

This uses prose to describe **one main camera motion** (“slowly orbits around”), plus mood/fps hints.

---

### 6. Practical prompting checklist (Seedance 1.0 / Pro)

- Use **natural‑language sentences**, not bare keyword lists.
- Order components as: **subject → action → scene → camera → lighting → style**.
- Keep prompts around **20–120 words**, with crucial directives at the start.
- For camera control, explicitly use terms like **push in, pull back, pan, tilt, dolly, track, orbit, zoom**, plus **“fixed camera”** where needed.
- Control intensity with words like **“very slow,” “gentle,” “fast,” “aggressive”**.
- For multi‑shot clips, segment with **“Shot 1 / Shot


## Sources

1. [Seedance 1.0 Pro API - 300+ AI Models One API - AI.cc](https://www.ai.cc/seedance-10-pro/)
2. [Seedance 1.0: Exploring the Boundaries of Video Generation Models](https://huggingface.co/papers/2506.09113)
3. [Seedance 1.0 Lite (Text-to-Video) - AI/ML API Documentation](https://docs.aimlapi.com/api-references/video-models/bytedance/seedance-1.0-lite-text-to-video)
4. [Seedance 1.0 Pro (Image to Video) API on fal](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/image-to-video)
5. [Seedance 1.0 - ByteDance Seed](https://seed.bytedance.com/en/seedance)
6. [Seedance 1.0 New Video Generation AI Stuns Industry ... - YouTube](https://www.youtube.com/watch?v=Mla03aT_rX8)
7. [Seedance 1.0 Pro API Documentation - Pollo AI API](https://docs.pollo.ai/m/seedance/seedance-pro)
8. [Seedance 2.0 - ByteDance Seed](https://seed.bytedance.com/en/seedance2_0)
9. [Seedance 1.0: Exploring the Boundaries of Video Generation Models](https://arxiv.org/html/2506.09113v1)
