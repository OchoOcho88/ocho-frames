# Band poster prompts (real product as reference)

> Session 032. Settled with Hugo: **text-free plates** (we lay real Glacial Indifference afterwards,
> house rule D-005) and the band must be **our exact product**, not a lookalike.
> Style references: `assets/style-references/posters/`, active set is 03, 05, 06, 07, 10, 11.
> Product references: `clients/sportif/products/band-reference-plates/` (6 clean white plates, 2048px).
> Prompt format follows `docs/platform-prompt-formats.md`. Voice rule applies: no em dashes.

---

## What Hugo is actually after

Reading his notes back, three of his six picks are the same idea: **depth between the type and the
subject**. Ref 03 ("how the individual is positioned in front of the text"), ref 07 ("that depth
creation between text and subject"), and what he wants to do with the blur pair ("some Sportif text
either behind or in front").

That is a build problem, not a prompt problem. A generator returns one flat image, so there is no
way to slide our real wordmark into the middle of it afterwards. So:

**The model generates the PHOTOGRAPH. We build the POSTER.**

There are two different ways to get depth, and which one applies depends on whether the subject has
a hard edge.

### Method 1, the cutout, for sharp subjects (refs 03, 07)

Matte the figure off the background, draw the type on the background layer, drop the figure back on
top. Real occlusion, the letters genuinely pass behind her.

This only works if the plate has a **flat, evenly lit, plain background**. S028 established that
plain-background subjects matte flawlessly and busy studio backgrounds do not. That instruction is
load bearing, not styling. Get a cluttered background back and the direction dies.

### Method 2, the burn-in, for blurred subjects (refs 10, 11)

Motion blur has no hard edge, so it cannot be cut out. Nothing to matte.

Instead, use the technique from S031: **shift the background's own tone a few percent inside the
letterforms**, masked by a feathered luminance threshold. The type appears to be printed on the wall
behind her, and the subject naturally occludes it because the subject is simply brighter or darker
than the threshold. It only works on flat, evenly lit plates, and a blown-out near-white blur shot is
exactly that.

So the blur prompts ask for a bright, even, low-contrast background and generous empty space. Type
in front is trivial on top of that; type behind uses the burn-in.

---

## Reference roles

**Nano Banana Pro** takes up to 14 images. Upload in this order and refer to them as image 1, image 2
and so on. **gpt-image-2** drifts past three or four, so send two product plates plus one style image.

| Upload order | File | Say this about it |
|---|---|---|
| 1 | `ref-front-folded.jpg` | the exact product, primary identity |
| 2 | `ref-label-detail.jpg` | the exact label to reproduce |
| 3 | `ref-inside-grip-a.jpg` | the inside grip face, only if the inside will show |
| 4+ | the chosen style reference | composition and lighting only, never content |

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

# Direction 1. The type sandwich

**Refs:** 03 and 07. **Method:** cutout. **Hugo:** "the text layout and thickness, and how the
individual is positioned in front of the text."

## Prompt 1A. Full figure

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

The empty upper left is the type well. Say it, or she lands dead centre and the headline has nowhere
to go.

## Prompt 1B. Legs only

Quieter, closer to ref 07, and it sidesteps casting drift entirely because there is no face.

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

## Type spec for this direction

Glacial Indifference Bold, all caps, tracked tight (around minus 0.02 em), set to full bleed width so
the line runs edge to edge like ref 03. Terracotta `#833827` on cream, or cream on peach.

Checked rather than assumed: Glacial Bold is **narrower** than ref 03's grotesque, not lighter. So it
matches the visual mass at a larger size. The brand font stands, no substitute needed.

Four short lines stacked is the ref 03 rhythm. Candidates from the brand say-list: EVERY / DAY /
TRAINING / ELEVATED, or MADE / TO BE / SEEN.

---

# Direction 2. Blur, with type behind and in front

**Refs:** 10 and 11. **Method:** burn-in. **Hugo:** "that blur effect on the subject. I could imagine
some Sportif text either behind or in front."

Note the deliberate exception: this is the one direction where the background does NOT need to
support a clean cutout, but it DOES need to be flat and evenly lit for the burn-in to work.

## Prompt 2A. Warm amber blur (closest to ref 11)

```text
A long exposure photograph of a woman mid movement against a plain, evenly lit near white
wall, her body and limbs smeared into soft motion trails, only her torso holding any
sharpness.
She wears caramel ribbed full length leggings and a matching relaxed tank. The caramel
brown fabric resistance band is looped around her thighs and blurs with her.
Warm amber light washing across the frame from the left, the wall behind her bright, even
and almost featureless, a faint double exposure ghosting on her arms.
She sits in the lower two thirds of the frame with clear empty wall above her.
Style: fine art fashion photography, long exposure, warm golden grade, dreamlike and soft,
grainy film. Low contrast in the background.
```

## Prompt 2B. Pale blush blur (closest to ref 10)

```text
A long exposure photograph of a woman stretching one arm overhead against a plain, evenly
lit off white wall, her whole body smeared into soft motion trails with no sharp edges
anywhere.
She wears blush peach ribbed full length leggings and a matching tank. The caramel brown
fabric resistance band is held loosely in her raised hand and trails into the blur.
Flat soft daylight, no visible shadow, the wall an even pale tone edge to edge.
Style: fine art fashion photography, long exposure, pale warm grade, quiet and dreamlike,
fine grain.
```

## Type spec for this direction

SPORTIF in Glacial Regular at the canonical tracking, large, centred. Two versions off the same
plate: one burned in behind her, one laid cleanly in front in cream. Hugo picks.

---

# Direction 3. The four panel grid

**Ref:** 05. **Method:** PIL build. **Hugo:** "the full grid structure and the composition of balance
between photos and words."

Not a generation job. Generate **two photographs**, then build the grid ourselves: two photo panels
and two flat colour panels carrying type, in a 2x2. Ref 05 alternates them diagonally, which is what
makes it balance.

Panels: top left photo, top right flat terracotta with a short line, bottom left flat peach with a
short line, bottom right photo. Thin caramel hairline callouts with small caps labels pointing at the
band, ref 05's annotation language, which is what makes a product feel engineered.

Callout labels must be **facts, not claims**: WOVEN COTTON BLEND, FLAT LOOP, MOULDED LABEL, THREE
RESISTANCES. Never an outcome.

Use prompt 1A and 1B outputs as the two photo panels, or generate a tighter product-in-hand shot for
one of them.

---

# Direction 4. Colourway strips (blocked)

**Ref:** 06. **Hugo:** "how the swatches correlate to the colour people are wearing."

Three vertical colour strips, peach, caramel and terracotta, each carrying the band in that
colourway. Ref 06's trick is that the strip colour and the worn colour match, so the swatch and the
product read as one system.

**Blocked on Q-015: the light and medium bands have not been photographed.** Worth building the day
they exist, because it is the range card and the wholesale line sheet in one asset.

---

## Running them

**Nano Banana Pro (Gemini 3 Pro Image):** Hugo runs this round in the Gemini app. Up to 14 references,
2K and 4K output. Product plates first, style reference last, roles stated.

**gpt-image-2:** I can iterate here at `quality: "low"`, `size: "1088x1360"`. Hugo runs keepers at high
or 4K in ChatGPT (S028: quality tier was the differentiator, not prompt craft). No transparent output,
so cutouts come off the flat wall via rembg.

**Then, always:** matte or burn in, lay Glacial Indifference, build the poster in PIL. The generator
never gets to set our type.

## Casting note

gpt-image-2 will not hold the same model between runs, and Gemini holds it better but not perfectly.
If a set needs one consistent person, generate her once and edit that image rather than regenerating.
