# Three posters, paste-ready for ChatGPT Images 2.0

> S032. Each block below is **self-contained**. Upload the named plates, paste the whole block,
> nothing to assemble. Reference plates: `clients/sportif/products/band-reference-plates-v2/`
> (rebuilt from shoot 4 and 5, colour corrected, all three bands).
>
> **Our method, unchanged:** the model makes the PHOTOGRAPH, we make the POSTER. Every prompt asks
> for zero text and a flat plain background, so the figure cuts out cleanly and the real Glacial
> Indifference goes on afterwards, in Photoshop or in PIL.

---

## Before you start

**Ask for portrait, 4:5.** In ChatGPT just say "make it a vertical 4:5 image" as the last line, or it
defaults to square.

**Upload order matters.** Product plates first, style reference last, and say what each one is for.
gpt-image-2 drifts past three or four references, so do not send more than the three named.

**Two things to check in what comes back**, before you spend time cutting it out:

1. Is the background genuinely plain and evenly lit? If there is a window, a skirting board, a
   shadow gradient or furniture, the cutout will fight you. Regenerate.
2. Is the band OUR band? Same deep caramel weave, same cream moulded label. If it invented a plain
   rubber band or changed the colour, regenerate.

---

# POSTER 1. Full figure, type sandwich

**Upload:** `ref-heavy-front-folded.jpg`, `ref-heavy-texture.jpg`, `poster-03-eat-sleep-pilates-repeat.jpg`
**After:** cut her out, giant headline behind her, second word in front.

```text
Image 1 and image 2 are the actual product. The resistance band in the photo must be exactly
this band: deep caramel brown woven fabric with a fine visible knit, a flat wide loop, and a
cream moulded rectangular label with raised white lettering. Do not redesign it, do not change
its colour, do not invent a different band.
Image 3 is a COMPOSITION reference only. Copy how the figure is framed and how flat the
background is. Do not copy its subject, its colours, its clothing, its text or its layout.

Make a full length editorial photograph of a woman in her early thirties standing against a
flat blush peach wall, turned side on to the camera with her weight on one leg and her arms
relaxed at her sides. She wears cream ribbed full length leggings and a matching relaxed tank.
The caramel resistance band is looped around both thighs just above the knees, stretched taut
and clearly under tension, not draped or loose, its cream moulded label facing the camera on
the outside of her near thigh.
Place her in the lower right of the frame with generous empty wall above her and to her left.
Her head and shoulders sit well inside the frame, not cropped.
Shot straight on at chest height on an 85mm lens, soft even frontal daylight, almost no shadow
on the wall behind her.
Style: calm editorial activewear photography, matte finish, fine film grain.

Background: one flat, plain, evenly lit peach wall. No furniture, no window, no skirting board,
no gradient, no texture, no shadow cast on the wall. She must be cleanly separable from it.
Text: no text anywhere in the image. No headline, no wordmark, no logo, no caption, no
watermark, no numbers. The only lettering allowed is the moulded label on the band itself.
Palette: warm neutrals only. No cool greys, no blue cast, no black, no purple.
Framing: aesthetic and lifestyle led, never centred on the glutes, never body targeting.
One person only, no clutter, no gym equipment.
Vertical 4:5 image.
```

The empty upper left is the type well. If she lands dead centre, say "move her further right and
leave the whole upper left empty" and regenerate.

---

# POSTER 2. Legs only, type sandwich

**Upload:** `ref-heavy-front-flat.jpg`, `ref-heavy-inside-grip.jpg`, `poster-07-pilates-poster.jpg`
**After:** same treatment, quieter. No face means no casting problems, so this is the reliable one.

```text
Image 1 and image 2 are the actual product. The resistance band must be exactly this band: deep
caramel brown woven fabric with a fine visible knit, a flat wide loop, and a cream moulded
rectangular label with raised white lettering. Image 2 shows its inside face with two dark
stripes. Do not redesign it, do not change its colour, do not invent a different band.
Image 3 is a COMPOSITION reference only. Copy the crop and the flatness of the background. Do
not copy its subject, its colours, its clothing, its text or its layout.

Make a cropped editorial photograph showing only the legs and lower torso of a woman lying on
her side on a pale linen mat against a flat cream wall, knees bent and stacked, the top knee
lifting away from the lower one.
She wears cream ribbed full length leggings. The caramel resistance band is looped around both
thighs just above the knees, stretched taut and clearly under tension, its cream moulded label
facing the camera.
The legs enter from the lower right and reach into the centre of the frame. The entire upper
half of the frame is empty cream wall.
Shot straight on at floor level on a 50mm lens, soft even daylight from the left, a warm
paper-like tone across the whole image.
Style: quiet editorial photography, matte finish, visible paper grain.

Background: one flat, plain, evenly lit cream wall. No furniture, no window, no skirting board,
no gradient, no shadow cast on the wall.
Text: no text anywhere in the image, no wordmark, no logo, no caption, no watermark, no
numbers. The only lettering allowed is the moulded label on the band itself.
Palette: warm neutrals only. No cool greys, no blue cast, no black.
No face in frame, no clutter, aesthetic and lifestyle led, never body targeting.
Vertical 4:5 image.
```

---

# POSTER 3. Motion blur

**Upload:** `ref-heavy-front-folded.jpg`, `poster-11-blur-sitting.jpg`
**After:** no cutting out. Blur has no hard edge, so the type gets burned into the wall behind her
instead (the S031 luminance trick). That is why this one asks for a bright, even, low-contrast wall.

```text
Image 1 is the actual product. The resistance band must be exactly this band: deep caramel
brown woven fabric with a fine visible knit and a cream moulded label. Do not change its colour.
Image 2 is a STYLE reference only, for the long exposure blur and the warm grade. Do not copy
its subject, its clothing or its composition.

Make a long exposure photograph of a woman mid movement against a plain, evenly lit near white
wall, her body and limbs smeared into soft motion trails, only her torso holding any sharpness.
She wears caramel ribbed full length leggings and a matching relaxed tank. The caramel
resistance band is looped around her thighs and blurs with her.
Warm amber light washing across the frame from the left, the wall behind her bright, even and
almost featureless, a faint double exposure ghosting on her arms.
Place her in the lower two thirds of the frame with clear empty wall above her.
Style: fine art fashion photography, long exposure, warm golden grade, dreamlike and soft,
grainy film. Keep the background low contrast and free of detail.

Text: no text anywhere in the image, no wordmark, no logo, no caption, no watermark.
Palette: warm neutrals and amber only. No cool greys, no blue cast, no black.
One person only, aesthetic and lifestyle led, never body targeting.
Vertical 4:5 image.
```

---

## When you have them

Send me whichever you like and I will do the type. Or if you want to cut them out yourself, the
layer recipe and the exact tracking values are in `clients/sportif/depth-poster-photoshop-guide.md`.

Headline candidates, all from the brand say-list, all safe on claims:

- EVERY / DAY / TRAINING / ELEVATED (the ref 03 four line stack)
- MADE / TO BE / SEEN
- SLOW / AND / BEAUTIFUL
- SPORTIF alone, with the rule and "collection" beneath it

For the ref 08 flip, split the headline so one word sits behind her and the next sits in front. That
one move does more for the depth than making the type bigger.
