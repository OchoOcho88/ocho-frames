# Band poster prompts (real product as reference)

> Session 032. Direction settled with Hugo: **text-free plates** (we lay real Glacial Indifference
> afterwards, house rule D-005), and the band must be **our exact product**, not a lookalike.
> Prompt format follows `docs/platform-prompt-formats.md`.
> Voice rule applies: no em dashes, no en dashes.

## Reference images to upload

Clean white plates, 2048px, in `clients/sportif/products/band-reference-plates/`:

| File | Role to give it in the prompt |
|---|---|
| `ref-front-folded.jpg` | primary product identity, label visible mid band |
| `ref-front-flat.jpg` | product identity, label near the top edge |
| `ref-inside-grip-a.jpg` | the inside grip face, twin dark stripes |
| `ref-label-detail.jpg` | the moulded SPORTIF / HEAVY label, for exact reproduction |
| `ref-back-flat.jpg` | the plain reverse |

**Nano Banana Pro** takes up to 14 references, so send the product plates AND the Pinterest style
references in the same run, with a role stated for each. **gpt-image-2** composes from multiple
images too, but keep it to three or four or identity starts to drift.

## The non-negotiables, in every prompt

Paste this block into any prompt below. It is what keeps the output ownable and on brand.

```text
Product accuracy: the resistance band must be EXACTLY the band in the reference images.
Same caramel brown woven fabric with visible knit texture, same flat wide loop, same
cream moulded rectangular label with raised white lettering. Do not redesign it, do not
change its colour, do not invent a different band.
Text: no text anywhere in the image. No headline, no wordmark, no logo, no caption, no
watermark. The only lettering allowed is the moulded label on the band itself.
Palette: warm neutrals only. Blush peach, cream, linen, caramel, terracotta, warm charcoal.
No cool greys, no blue cast, no black.
Constraints: no people unless stated, no clutter, no props beyond those named.
```

---

## Prompt 1. Product still life, plinth

The elevated ecommerce hero. Closest to Anine Bing's product register.

```text
A premium still-life photograph of a single caramel brown fabric resistance band,
resting over the edge of a low cream plaster plinth on a linen surface.
The band falls naturally with one soft fold, its cream moulded label facing the camera.
Shot slightly above eye level on a 50mm lens, soft directional daylight from the left,
long gentle shadow to the right, faint warm bounce on the shadow side.
Style: editorial product photography, quiet and expensive, sharp on the band, background
falling softly out of focus. Blush peach wall behind, cream and linen tones throughout,
the band the only saturated element.
Mood: calm, warm, morning light.
```

Then: crop to 4:5, lay the lockup and headline in PIL.

## Prompt 2. Flat lay, morning ritual

For the ritual angle in the brand doc. Props stay few and all warm.

```text
An overhead flat lay on a washed linen sheet in cream and blush peach.
A single caramel brown fabric resistance band lies in a loose relaxed loop slightly off
centre, its cream moulded label face up and readable. Beside it, arranged with generous
space between them: a folded linen towel, a small ceramic cup in unglazed clay, and one
dried palm frond.
Shot straight down, soft diffused morning light from the top left, gentle shadows.
Style: elevated lifestyle flat lay, calm and uncrowded, natural texture, film grain.
Mood: slow morning, warm and tactile.
```

## Prompt 3. In use, pilates, product led

The band under real tension. Note the field-validated fix from `platform-prompt-formats.md`:
gpt-image-2 defaults to passive placement, so tension has to be named.

```text
A woman in her early thirties in a warm cream ribbed activewear set, seated on a pale
wooden pilates reformer in a bright studio with blush peach walls.
The caramel brown fabric resistance band is looped around both thighs just above the knees,
stretched taut and clearly under tension, not draped or loose. Its cream moulded label sits
on the outside of her right thigh, facing the camera.
Cropped from mid torso to mid calf so the face is out of frame. Shot at eye level on an 85mm
lens, soft window light from the left, warm shadows.
Style: editorial activewear photography, calm and elevated, never glossy or skin heavy.
Mood: composed, unhurried.
```

Casting note: gpt-image-2 will not hold the same model between runs, so if a set needs one
consistent person, describe her the same way every time or generate once and edit.

## Prompt 4. Graphic poster plate

A background built to be typed on. Leave the space empty deliberately.

```text
A minimal poster background. A large soft blush peach arc fills the lower two thirds of a
cream field, with fine paper grain across the whole image.
A single caramel brown fabric resistance band lies diagonally across the lower right corner
in one relaxed fold, its cream moulded label visible, casting a soft warm shadow.
The entire upper left half is empty cream, uninterrupted, with nothing in it.
Style: contemporary graphic poster, flat colour blocking with one photographic object,
warm neutral palette, matte finish.
```

The empty upper left is the type well. That instruction matters more than it looks.

---

## Running them

**gpt-image-2:** iterate here at `quality: "low"`, `size: "1088x1360"` for feed. Hugo runs the keeper
at high or 4K in ChatGPT (S028 learning: the differentiator was quality tier, not prompt craft).
gpt-image-2 cannot output transparent backgrounds, so cutouts still come from white plates.

**Nano Banana Pro (Gemini 3 Pro Image):** needs `GEMINI_API_KEY` in `.env`. Hugo's key is in his Mac
`~/.zshrc`, which the sandbox cannot read, so it has to be copied into the file. Sandbox network
egress must also allow `generativelanguage.googleapis.com`, and that only applies to a freshly
booted sandbox, so a NEW chat is required after changing it.

## Still to fold in

Hugo's Pinterest poster references. Once they land, each one becomes a named style reference in the
prompt ("use the composition of @image5, the colour grading of @image6") rather than something I
paraphrase into adjectives, which is always weaker.
