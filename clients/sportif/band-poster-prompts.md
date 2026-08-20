# Band poster prompts (real product as reference)

> Session 032. Settled with Hugo: **text-free plates** (we lay real Glacial Indifference afterwards,
> house rule D-005) and the band must be **our exact product**, not a lookalike.
> Style references: `assets/style-references/posters/` (11 images, indexed in that folder's README).
> Product references: `clients/sportif/products/band-reference-plates/` (6 clean white plates, 2048px).
> Prompt format follows `docs/platform-prompt-formats.md`. Voice rule applies: no em dashes.

---

## The one thing that changes how we work

Eight of Hugo's eleven references are the same layout: **giant type with a body breaking through
it**. That layout cannot be generated as a finished poster, and we should not try. Here is why.

The charm of `poster-08` is that "Pilates" sits in FRONT of the legs and "Power" sits BEHIND them.
That is a z-order trick. A generator hands back one flat image, so there is no way to slide our real
wordmark into the middle of it afterwards.

So the split is:

**The model generates the PHOTOGRAPH. We build the POSTER.**

Which means every prompt below asks for a clean photograph, text-free, shot against a **flat,
evenly lit, plain wall in a single warm tone**. That last instruction is not decoration. A plain
background is what lets rembg cut the figure out cleanly (S028: plain-bg subjects matte flawlessly,
busy studio backgrounds do not), and the cutout is what lets me put type behind the body and the
body in front of the type. Get a busy background back and the whole direction dies.

---

## Reference roles

**Nano Banana Pro** takes up to 14 images, so send product and style in one run and name each role.
Gemini reads them in upload order, so upload in this order and refer to them as image 1, image 2 and
so on. **gpt-image-2** drifts past three or four references, so send only the two product plates plus
one style reference.

| Upload order | File | Say this about it |
|---|---|---|
| 1 | `ref-front-folded.jpg` | the exact product, primary identity |
| 2 | `ref-label-detail.jpg` | the exact label to reproduce |
| 3 | `ref-inside-grip-a.jpg` | the inside grip face, only if the inside will show |
| 4+ | the chosen style reference | composition and lighting only, never content |

Wording that works, adapted per prompt:

```text
Image 1 and image 2 are the actual product and must be reproduced exactly.
Image 3 is a COMPOSITION and LIGHTING reference only. Copy its framing, its crop, the
flatness of its background and the way the light falls. Do not copy its subject, its
colours, its clothing, its text or its layout.
```

## The non-negotiables, in every prompt

```text
Product accuracy: the resistance band must be EXACTLY the band in the product reference
images. Same caramel brown woven fabric with visible knit texture, same flat wide loop,
same cream moulded rectangular label with raised white lettering. Do not redesign it, do
not change its colour, do not invent a different band.
Background: one flat, plain, evenly lit wall in a single warm tone. No furniture, no
windows, no props, no gradient, no texture, no shadows on the wall behind the subject.
The subject must be cleanly separable from the background.
Text: no text anywhere in the image. No headline, no wordmark, no logo, no caption, no
watermark, no numbers. The only lettering allowed is the moulded label on the band itself.
Palette: warm neutrals only. Blush peach, cream, linen, caramel, terracotta, warm charcoal.
No cool greys, no blue cast, no black, no purple, no fluro.
Wardrobe: full length leggings and a relaxed fitting tank or bra top, generous coverage,
smooth four-way-stretch fabric in a colour that contrasts the skin. Nothing high cut,
nothing cropped tight, nothing sheer.
Framing: never centred on the glutes. Aesthetic and lifestyle led, never body targeting.
Constraints: one person only, no clutter, no gym equipment beyond what is named.
```

---

# The prompts

## Prompt A. Type sandwich plate (the main one)

**Style reference:** `poster-03`, `poster-07`, or `poster-08`. Pick one, not all three.
**What we do after:** cut the figure out, lay a giant Glacial Bold headline, slide the figure back in
front of it so the letters run behind her.

```text
A full length editorial photograph of a woman in her early thirties standing against a
flat blush peach wall, turned side on to the camera with her weight on one leg and her
arms relaxed. She wears cream ribbed full length leggings and a matching relaxed tank.
The caramel brown fabric resistance band is looped around both thighs just above the
knees, stretched taut and clearly under tension, not draped or loose, its cream moulded
label facing the camera on the outside of her near thigh.
She is positioned in the lower right of the frame with generous empty wall above her and
to her left. Her head and shoulders sit well inside the frame, not cropped.
Shot straight on at chest height on an 85mm lens, soft even frontal daylight, almost no
shadow on the wall.
Style: calm editorial activewear photography, matte finish, fine film grain.
```

The empty upper left is the type well. Say it, or the model centres her and there is nowhere for
the headline to go.

## Prompt B. Type sandwich, legs only

**Style reference:** `poster-07`. Quieter and easier, because no face means no casting drift.

```text
A cropped editorial photograph showing only the legs and lower torso of a woman lying on
her side on a pale linen mat against a flat cream wall, knees bent and stacked, top knee
lifting.
She wears cream ribbed full length leggings. The caramel brown fabric resistance band is
looped around both thighs just above the knees, stretched taut and clearly under tension,
its cream moulded label facing the camera.
The legs enter from the lower right and reach into the centre of the frame. The entire
upper half of the frame is empty cream wall.
Shot straight on at floor level on a 50mm lens, soft even daylight from the left, warm
paper-like tone across the whole image.
Style: quiet editorial photography, matte, visible paper grain.
```

## Prompt C. Wordmark over body

**Style reference:** `poster-04`. Here the plate is a tight crop and the mark goes straight over it.

```text
A tight editorial crop of a woman from mid back to mid thigh, photographed from behind
against a flat blush peach wall, arms extended out to the sides, back gently arched.
She wears a caramel ribbed tank and matching full length leggings in a smooth
four-way-stretch fabric. The caramel brown fabric resistance band is held taut between
both hands above and behind her, stretched straight and clearly under tension, its cream
moulded label visible near her right hand.
Fills the frame edge to edge, no empty margin.
Shot on an 85mm lens, soft warm daylight from the upper left, gentle skin highlight.
Style: premium activewear campaign photography, warm grade, matte finish.
```

## Prompt D. Motion blur

**Style reference:** `poster-10` and `poster-11`. No type needed at all, or one small line.
Note this is the one direction where a *slight* background gradient is acceptable, since nothing
gets cut out.

```text
A long exposure photograph of a woman mid movement against a near white wall, her body
and limbs smeared into soft motion trails, only her torso holding any sharpness.
She wears caramel ribbed full length leggings and a matching relaxed tank. The caramel
brown fabric resistance band is looped around her thighs and blurs with her.
Warm amber light washing across the frame from the left, blowing out to white on the
right, a faint double exposure ghosting on her arms.
Style: fine art fashion photography, long exposure, warm golden grade, dreamlike and soft,
grainy film.
```

## Prompt E. Colourway strips (blocked, keep for later)

**Style reference:** `poster-06`. This one needs the **light and medium bands photographed** (Q-015).
Three vertical bands of peach, caramel and terracotta, one product per strip. Worth building the
moment the other two bands exist, because it is the range card and the wholesale line sheet in one.

## Prompt F. Exercise guide, rebuilt

**Style reference:** `poster-01` and `poster-02`, format only. Not a generation job at all: build it
in PIL like the posters, so the type is exact and the copy is controlled. Movement names only
("side lying leg lift"), never an outcome ("lift your glutes"). This is real waitlist and email
content, and it is the most useful thing in Hugo's whole reference set.

---

## Running them

**Nano Banana Pro (Gemini 3 Pro Image):** Hugo runs this round himself in the Gemini app. Up to 14
references, 2K and 4K output. Upload product plates first, style reference last, and state the roles.

**gpt-image-2:** I can iterate here at `quality: "low"`, `size: "1088x1360"`. Hugo runs keepers at high
or 4K in ChatGPT (S028: quality tier was the differentiator, not prompt craft). No transparent output,
so cutouts come off the flat wall via rembg.

**Then, always:** matte the figure, lay Glacial Indifference, rebuild as a real poster in PIL. The
generator never gets to set our type.

## Casting note

gpt-image-2 will not hold the same model between runs, and Gemini holds it better but not perfectly.
If a set needs one consistent person, generate her once and edit that image rather than regenerating.
