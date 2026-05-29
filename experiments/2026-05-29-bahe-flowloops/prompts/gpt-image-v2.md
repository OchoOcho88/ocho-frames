# gpt-image-2 prompt, image v2 (lifestyle in-use)

> Platform: gpt-image-2 / ChatGPT Images 2.0 (text-to-image, no reference)
> Target: 2:3 portrait (1024x1536), quality high
> Techniques under test: person + hands + product-in-use + brand text on a detailed lifestyle background (harder than the v1 flat-lay), with explicit anatomy constraints. Placeholder branding only.

## Paste-ready prompt

```text
A premium editorial lifestyle photo of a woman in matching warm sand-toned activewear, seated on a light wooden floor in a bright minimalist room, mid-movement in a calm, controlled Pilates pose with a terracotta flat woven-fabric resistance loop around her thighs.
Soft natural morning light from a large window on the left, sheer linen curtains, a single potted plant, warm neutral tones throughout.
Style: high-end editorial fitness photography, shot on an 85mm lens, shallow depth of field, the woman in sharp focus, the background softly blurred, subtle film grain.
Mood: calm, elevated, aspirational, design-led, the product as a natural part of a considered lifestyle.
Text instructions: in the top-left corner, add a small wordmark that reads exactly "FLOW" in bold geometric sans-serif, warm charcoal, all caps, with generous letter spacing. No other text, no logos, no icons.
Constraints: portrait 2:3, one person only, natural relaxed hands with anatomically correct fingers, warm earthy palette, calm and uncluttered room, no health or fitness performance claims, no extra people, no equipment other than the single loop.
```

## API settings
- `model: "gpt-image-2"`, `size: "1024x1536"`, `quality: "high"`, `output_format: "jpeg"`. Do NOT set `input_fidelity`.

## Save the result as
`results/image-v2.png`

## Outcome (see analysis/image-v2-analysis.md)
Strong. Person + hands/feet + product + brand text all clean in one pass. Findings: product read as draped/decorative rather than in functional use (addressed in v3), and casting skewed conventional fitness-aesthetic (specify casting for consistency).
