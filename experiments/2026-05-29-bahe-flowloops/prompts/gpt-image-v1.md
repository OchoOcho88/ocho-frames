# gpt-image-2 prompt, image v1

> Platform: gpt-image-2 / ChatGPT Images 2.0 (text-to-image, no reference this round)
> Target: 2:3 portrait product hero (1024x1536), quality high for final
> Techniques under test this round: ordered natural-language brief, grouped text-instruction block (testing gpt-image-2 text rendering), explicit negative constraints, warm design-led art direction. Placeholder branding only.

## Paste-ready prompt

```text
A premium product photo of three flat woven-fabric resistance loops arranged in a neat fan on a pale linen surface, in three warm tones: light tan, terracotta, and espresso brown.
Shot from slightly above, soft natural daylight from the left, gentle shadows, a faint reflection on the surface, fine woven fabric texture clearly visible.
Style: high-end minimalist ecommerce and editorial photography, sharp focus on the loops, background softly blurred, warm earthy palette.
Mood: calm, elevated, design-led, fitness equipment treated as a lifestyle object.
Text instructions: at the top center, add a headline that reads exactly "FLOW" in bold modern geometric sans-serif, warm charcoal, all caps, with generous letter spacing. Directly below it, add a smaller tagline that reads exactly "move with ease" in a light-weight sans-serif, sentence case, warm grey. No other text, no logos, no icons anywhere.
Constraints: portrait 2:3 composition, no people, no clutter, calm neutral background, no health or fitness performance claims.
```

## API settings (if generating via the API rather than the ChatGPT app)

- `model: "gpt-image-2"`
- `size: "1024x1536"` (2:3 portrait)
- `quality: "high"` for the final, `"medium"` for cheap iterations
- `output_format: "jpeg"` (or `"png"` if you want to edit further)
- Do NOT set `input_fidelity` (errors on gpt-image-2).
- Transparency is not supported on gpt-image-2. This hero uses a solid linen background, so that is fine. If we later need a cutout asset, generate on pure white and cut out externally, or use gpt-image-1.5.

## Notes for the operator

- In the ChatGPT app, just paste the prompt block and request a 2:3 portrait.
- Save the result as `../results/image-v1.png` (or .jpg).

## What we are testing (fill in after generation)

- Did the headline "FLOW" and tagline "move with ease" render cleanly and exactly (the gpt-image-2 text strength)?
- Did all three loops render in the correct warm tones with fabric (not rubber) texture?
- Did the negative constraints hold (no people, no extra text, no logos)?
- Is the art direction warm, premium, and design-led, or did it drift generic?
