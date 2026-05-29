# gpt-image-2 prompt, image v3 (functional-use test)

> Platform: gpt-image-2 / ChatGPT Images 2.0 (text-to-image, no reference)
> Target: 2:3 portrait (1024x1536), quality high
> One variable changed from v2: the pose is forced to genuine functional use (loop stretched taut, clearly in use), to test whether that costs the editorial aesthetic.

## Paste-ready prompt

```text
A premium editorial lifestyle photo of a woman in matching warm sand-toned activewear, sitting upright and grounded on a linen mat on a light wooden floor in a bright minimalist room.
She is performing a controlled seated hip-abduction exercise: knees bent with feet flat on the floor, a terracotta flat woven-fabric resistance loop wrapped around both thighs just above the knees, knees pressed outward so the loop is visibly stretched taut and clearly under tension. Her posture is tall and composed.
Soft natural morning light from a large window on the left, sheer linen curtains, a single olive tree in a clay pot, warm neutral tones throughout.
Style: high-end editorial fitness photography, shot on an 85mm lens, shallow depth of field, the woman in sharp focus, the background softly blurred, subtle film grain.
Mood: calm, elevated, intentional, design-led, movement shown as something quiet and considered.
Text instructions: in the top-left corner, add a small wordmark that reads exactly "FLOW" in bold geometric sans-serif, warm charcoal, all caps, with generous letter spacing. No other text, no logos, no icons.
Constraints: portrait 2:3, one person only, natural relaxed face, hands resting naturally with anatomically correct fingers, feet with correct toes, the resistance loop must be stretched taut around both thighs and clearly in use, not draped or loose, warm earthy palette, calm and uncluttered room, no health or fitness performance claims, no extra people, no equipment other than the single loop.
```

## API settings
- `model: "gpt-image-2"`, `size: "1024x1536"`, `quality: "high"`, `output_format: "jpeg"`. Do NOT set `input_fidelity`.

## Save the result as
`results/image-v3.png`

## Outcome (see analysis/image-v3-analysis.md)
Best asset of the experiment. The explicit "stretched taut, clearly in use, not draped" instruction produced genuine functional product use with no aesthetic penalty. Confirmed recipe: to show real use, name the exercise position + the taut/in-use phrase.

## Note
This same prompt was later (accidentally) fed to Seedance text-to-video with no reference, producing results/video-gpt.mp4 (see analysis/video-gpt-analysis.md). That run is what surfaced the "image prompts port to video," "short invented wordmark renders clean," "single-shot avoids glitch," and "human biomechanics are weak" findings.
