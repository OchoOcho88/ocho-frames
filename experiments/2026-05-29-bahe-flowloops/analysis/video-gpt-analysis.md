# Video-gpt analysis (accidental cross-platform test)

> Analyzed: 2026-05-29 via video-analyzer (gemini-3-flash-preview), plus pending human review of text + motion
> What happened: Hugo accidentally fed the gpt-image-v3 prompt (an IMAGE prompt written for gpt-image-2) directly into Seedance as text-to-video, with NO reference image.
> Result: results/video-gpt.mp4

## Why this is a useful accident
It isolates two things our deliberate runs did not:
1. Does an image-oriented prompt (static, photographic, "85mm lens", "portrait 2:3", a "Text instructions: FLOW" block, no motion/beat direction) port to Seedance text-to-video?
2. First real test of Seedance INVENTING on-screen text (v2's clean "FLOW" came from the reference image; here there is no reference).

## Analyzer findings
- **Motion:** a single continuous shot of the woman actually performing the seated hip-abduction, rhythmic reps, knees pushing out against the taut band, good form. Seedance inferred believable functional MOTION from a static exercise description with no beat/camera direction.
- **No glitch reported** (single continuous shot), unlike video-v2's 5 to 7s jump cut (multi-beat + reference). Supports the hypothesis: single continuous shot avoids the mid-clip glitch.
- **Audio:** soft rhythmic instrumental, auto-generated. The image prompt had NO audio block at all, yet music appeared. Third confirmation Seedance forces its own audio regardless of prompt.
- **Casting:** blonde/brown hair, different again (no reference), confirms casting drift across generations.
- **Text:** analyzer reads "FLOW" top-left, but the analyzer is unreliable on text legibility. PENDING human confirmation.

## Human review (Hugo, confirmed)
1. **Text:** "FLOW" came out clean and stable, on point, even though invented (no reference). REVISES the earlier "invented text garbles" rule: short simple wordmarks render clean even invented. Garble risk is for longer/complex text.
2. **Motion smoothness:** smooth all the way, no jump cut. CONFIRMS single continuous shot avoids the glitch.
3. **Human action:** terrible and unnatural. The exercise was awkward and not a believable use of a band around the knees. NEW failure mode: Seedance human biomechanics are weak for specific equipment use. (The Gemini analyzer wrongly praised "good form", so it over-rates human motion.)

## Confirmed learnings (promoted to docs/platform-prompt-formats.md)
- Seedance renders short invented wordmarks clean (Part A2, rule revised).
- Single continuous shot avoids the mid-clip glitch (Part A6, confirmed fix).
- Seedance human-action realism is weak for specific movements; use @video1 motion reference or keep actions simple, and judge motion with human eyes (Part A6, new failure mode).
- Image-style prompts port to video and yield motion without beat direction (Part A2).
- Auto-audio and casting-drift reconfirmed.
