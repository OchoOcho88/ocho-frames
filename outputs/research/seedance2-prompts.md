ByteDance’s Seedance 2.0 prompt style is best treated as a **shot-directed, multimodal production brief**: define the scene in a fixed order, then add references, camera/motion control, audio cues, and hard constraints. The official Seedance materials confirm it is a unified text-image-audio-video model, while the most practical public guides agree that **structure and specificity** matter more than long prose.[7][9][1]

## 1) Official directorial prompt structure and exact component order

The practical “directorial” structure used across Seedance 2.0 guides is:

1. **Subject**
2. **Action**
3. **Environment**
4. **Camera**
5. **Style**
6. **Constraints**[1][5]

A compact template:

```text
Subject: [who/what is on screen, singular if possible]
Action: [what the subject does, present tense, specific verb phrase]
Environment: [location, time of day, weather, key set details]
Camera: [shot size] + [movement] + [angle/lens cue]
Style: [visual anchor, lighting, color treatment, finish]
Constraints: [things to keep fixed, exclude, duration/tempo, consistency rules]
```

A slightly more production-ready version:

```text
Subject: ...
Action: ...
Environment: ...
Camera: ...
Style: ...
Constraints: ...
```

The strongest public templates emphasize that the camera line should include **shot size + movement + angle/lens cue**, while the constraints line should explicitly ban instability, unwanted objects, or style drift.[1] One guide also recommends adding a **quality suffix** such as “4K, ultra HD, rich detail, sharp clarity, cinematic textures, stable picture,” though that is a community practice rather than an official requirement.[3]

## 2) `@image1` / `@video1` / `@audio1` reference syntax, role assignment, and limits

Seedance 2.0 supports **text, image, audio, and video inputs** in a multimodal workflow.[7][9] Public guides and demos show the common reference shorthand as `@image1`, `@video1`, and `@audio1` inside the prompt, with the reference assets attached as separate inputs in the UI or API flow.[2][7][9]

### How to write it

A practical pattern is:

```text
Use the composition from @image1, the camera move from @video1, and the rhythm from @audio1.
```

Other role-assignment examples in natural language:

```text
Match the subject pose and framing of @image1.
Follow the dolly-in motion from @video1.
Keep the pacing and beat structure of @audio1.
Use @image2 as the wardrobe reference and @image3 as the lighting reference.
```

This “role assignment” wording is consistent with how public tutorials describe Seedance Omni/reference workflows: upload the ingredients, then tell the model which asset controls which aspect of the output.[2][7][9]

### Limits

Public guides repeatedly mention reference-count limits of **up to 9 images, 3 videos, and 3 audio clips** in the Seedance 2.0 reference workflow.[7][9] Because those limits are surfaced in the official ecosystem and echoed by third-party guides, they are the most practical working limits to assume.[7][9]

### Best practice for reference assignment

- Use **one reference per role** when possible.[2][9]
- State the role in plain language instead of vague “inspiration” language.[2][1]
- Separate **composition**, **motion**, **identity**, **wardrobe**, and **audio rhythm** into different references when you can.[2][9]

Example:

```text
Use @image1 for character identity and wardrobe, @image2 for scene composition, @video1 for the camera move, and @audio1 for the beat timing.
```

## 3) Camera and motion vocabulary for 2.0, plus multi-shot / time-coded prompting

Public Seedance 2.0 guides consistently recommend **clear cinematography language**: shot size, angle, lens cue, and movement.[1][5] The best-performing vocabulary is short, literal, and production-oriented.

### Useful camera vocabulary

- **Wide shot / establishing shot**
- **Medium shot**
- **Close-up**
- **Extreme close-up**
- **Over-the-shoulder**
- **Low angle**
- **High angle**
- **Eye level**
- **Handheld**
- **Locked-off**
- **Slow push-in**
- **Pull-back**
- **Dolly in / dolly out**
- **Truck left / truck right**
- **Pan left / pan right**
- **Tilt up / tilt down**
- **Rack focus**
- **Orbit / arc around subject**
- **Zoom in / zoom out**[1][5]

### Motion vocabulary

- **Walks**
- **Turns**
- **Reaches**
- **Lifts**
- **Embraces**
- **Nods**
- **Breathes**
- **Swirls**
- **Falls**
- **Pours**
- **Drifts**
- **Shakes**
- **Flutters**
- **Ripples**[1][5]

A recurring failure mode is **camera chaos**, so several guides advise banning motion you do not want, such as snap zooms, whip pans, Dutch angles, and jump cuts.[1]

### Multi-shot / time-coded segment prompting

For multi-shot sequences, the strongest public guidance is to **number each shot** and/or use **timestamps**.[4][5] A practical format looks like this:

```text
[0s–3s] Shot 1: ...
[3s–6s] Shot 2: ...
[6s–10s] Shot 3: ...
```

Or:

```text
Shot 1: ...
Shot 2: ...
Shot 3: ...
```

One guide recommends explicitly stating the **number of shots, total duration, and aspect ratio at the top** of the prompt, then writing each shot separately with a clear escalation arc.[4] Another timeline guide recommends timestamp markers such as `[0s]`, `[3s]`, `[6s]`, and `[8s]` to anchor event changes and camera moves.[5]

A practical template:

```text
Duration: 8s, 16:9, 3 shots

[0s–2s] Establishing shot: ...
[2s–5s] Medium shot: ...
[5s–8s] Close-up: ...

Style: ...
Constraints: ...
```

If you need a short clip, compress the beats; if you need a longer clip, keep each beat simple and avoid overloading one shot with too many actions.[5]

## 4) Audio and dialogue / lip-sync prompting

Seedance 2.0 is positioned as a **joint audio-video generation** model, so audio should be written as a first-class part of the prompt rather than an afterthought.[7][9] Public tutorials emphasize adding **specific sound descriptions** instead of generic “good audio” language.[3]

### What to specify

- **Dialogue**
- **Sound effects**
- **Music**
- **Ambience / room tone**
- **Lip-sync timing**
- **Who speaks when**[3][7][9]

### Dialogue prompting

Write dialogue in quotation marks and identify the speaker if needed:

```text
Dialogue: The woman says, “We should leave now.”
```

For lip-sync, make the timing and shot explicit:

```text
Close-up on the speaker’s face. She speaks clearly and naturally, with accurate lip-sync.
Dialogue: “I found it.”
```

### Sound effects prompting

Be specific and concrete:

```text
Sound effects: soft footsteps on wet pavement, distant traffic, a door creaking open.
```

### Music prompting

Describe genre, tempo, and emotional function:

```text
Music: minimal piano, slow tempo, restrained, tension-building, no vocals.
```

### Ambience prompting

State the environment bed:

```text
Ambience: light rain, faint wind, muffled city hum, subtle indoor room tone.
```

### Practical audio block template

```text
Audio:
- Dialogue: ...
- Sound effects: ...
- Music: ...
- Ambience: ...
- Lip-sync: accurate, natural timing for on-camera speech
```

One public guide explicitly recommends banning subtitles if you plan to add voice-over or captions later.[3]

## 5) Recommended prompt length

Public Seedance guides consistently favor **concise but structured prompts**, not long freeform paragraphs.[1][5] The practical pattern is:

- **1 scene / 1 shot**: short, tightly written prompt
- **Multi-shot / 5–10s clip**: structured by shots or timestamps
- **Longer sequences**: break into explicit segments instead of one monolithic paragraph[4][5]

A useful rule from community workflows is that if the prompt becomes too long, you should compress it back under the target character limit by keeping only the shot list and removing unsupported extras.[2] In practice, the best prompts are usually **brief enough to read like a shot brief**, but detailed enough to pin down subject, motion, camera, style, and constraints.[1][5]

## 6) Common failure modes specific to 2.0, and fixes

### Flagged / refused prompts

Seedance 2.0 guides note that prompts can be refused or degraded when they include unsafe, branded, or policy-sensitive content.[1] Common fixes:

- Remove explicit brand names and logos.[1]
- Avoid text overlays, UI overlays, and watermark requests unless needed.[1][3]
- Rephrase sensitive content into a neutral cinematic description.

### Identity drift

A major failure mode is **identity drift**, where the person’s face, clothing, or body shape changes across frames.[1] Fixes:

- Use one primary identity reference image.[2][9]
- State “keep face and clothing consistent” in constraints.[1][3]
- Avoid mirrors, crowds, or complex occlusions unless necessary.[1]

### Camera chaos

Another common issue is unstable or contradictory camera behavior.[1] Fixes:

- Use one camera move per shot.[1][5]
- Say “locked-off” if you want no movement.
- Ban undesired moves explicitly: “no whip pan, no snap zoom, no Dutch angle.”[1]

### Audio desync

Because audio is generated jointly, desync can happen when the prompt is too vague about timing.[7][9] Fixes:

- Put dialogue inside a specific shot or timestamp.[5]
- Keep spoken lines short.
- Add “accurate lip-sync” or “speech starts at 2s” style timing notes.
- Avoid overlapping dialogue, music, and sound effects unless you really need them.[3][5]

### Body / object artifacts

Several guides warn about malformed hands, warped objects, and melting edges.[1] Fixes:

- Reduce complexity in the action.
- Keep props simple.
- Add negative constraints such as “no extra fingers, no warped hands, no melting edges.”[1]

### Overwritten style

If the model drifts into random aesthetics, anchor the style with one strong visual reference instead of many adjectives.[1] Fixes:

- Choose one style anchor: “35mm film,” “documentary realism,” “advertising gloss,” etc.
- Keep lighting and color treatment in one short line.[1]

## 7) Two strong example prompts, with explanation

### Example 1: cinematic narrative shot with audio and lip-sync

```text
Duration: 6s, 16:9, 1 shot

Subject: A young woman in a red coat, alone at a train platform.
Action: She turns toward the arriving train and quietly says, “You came.”
Environment: Night platform, light rain, reflective wet ground, distant city lights.
Camera: Medium close-up, slow push-in, eye level, 50mm look.
Style: Cinematic realism, soft practical lighting, cool blue shadows, subtle film grain.
Audio: Dialogue: “You came.” Sound effects: train brakes, rain on metal roof, faint footsteps. Ambience: low station hum and wind. Lip-sync: accurate and natural.
Constraints: Keep her face and coat consistent, no subtitles, no extra people, no camera shake, no logos.
```

Why this works:
- It follows the **Subject → Action → Environment → Camera → Style → Constraints** order.[1]
- It gives a single clear camera move, which reduces instability.[1][5]
- It specifies dialogue, SFX, ambience, and lip-sync separately, which is better for multimodal control.[3][7]

### Example 2: multi-shot sequence with reference roles

```text
Duration: 8s, 16:9, 3 shots

Use @image1 for character identity and wardrobe, @image2 for composition, @video1 for the camera movement, and @audio1 for rhythm and pacing.

[0s–2s] Shot 1: Wide shot of a cyclist entering a sunlit alley at dawn. Locked-off camera, establishing the environment.
[2s–5s] Shot 2: Medium shot as the cyclist slows, looks left, and reaches for the handlebars. Slow lateral truck right, matching the motion from @video1.
[5s–8s] Shot 3: Close-up on the cyclist’s face and front wheel as water drips from the frame. Gentle push-in, then hold.
Style: Clean cinematic realism, warm sunrise highlights, soft contrast, natural color.
Audio: Music: restrained percussion with a steady pulse, matching @audio1. Sound effects: tire roll on pavement, chain click, distant birds. Ambience: quiet street morning air.
Constraints: Preserve identity from @image1, preserve composition from @image2, no extra riders, no text, no logo, no whip pans, no jump cuts, no audio drift.
```

Why this works:
- It assigns each reference a clear role in natural language, which is the most reliable way to use multimodal references.[2][9]
- It uses timestamped shots, which aligns with public timeline-prompting advice.[5]
- It separates motion, identity, and audio rhythm into different control channels, reducing prompt conflict.[2][5]

If you want, I can turn this into a **one-page Seedance 2.0 prompt cheat sheet** or a **copy-paste master template** for image-to-video, video-to-video, and audio-led generation.


## Sources

1. [Seedance 2.0 Prompt Template: Copy-Paste Framework for Motion ...](https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/)
2. [Seedance 2.0 Officially Public! Full Prompting Tutorial (Claude + ...](https://www.youtube.com/watch?v=tYJQusOS2jI)
3. [The ULTIMATE Seedance 2.0 Prompting Guide (Complete Control + ...](https://www.youtube.com/watch?v=tZReV23ncuc)
4. [Seedance 2.0 — Complete Prompting Guide (Full Prompt Library)](https://higgsfield.ai/blog/seedance-prompting-guide)
5. [How to Use Timeline Prompting with Seedance 2.0 for Cinematic AI ...](https://www.mindstudio.ai/blog/timeline-prompting-seedance-2-cinematic-ai-video/)
6. [YouMind-OpenLab/awesome-seedance-2-prompts: 2000+ ... - GitHub](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)
7. [Seedance 2.0 Official Launch - ByteDance Seed](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0)
8. [Seedance 2.0 Prompt Library, Guides & Workflow Examples](https://www.seedance2prompt.com)
9. [Seedance 2.0 - ByteDance Seed](https://seed.bytedance.com/en/seedance2_0)
