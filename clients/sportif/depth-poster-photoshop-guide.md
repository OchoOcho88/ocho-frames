# Depth poster, Photoshop build guide

> Written S032 for Hugo, who is cutting these out himself. This is the type spec and layer recipe
> so a poster built in Photoshop lands on brand without needing a correction pass afterwards.
> Consistent with D-012: hard mattes are Hugo's job in Photoshop, automatic matting is only for
> clean plain-background subjects.

## Before anything, install the font

`brand/fonts/glacial-indifference/` holds three OTFs. Double click each one, hit Install. Restart
Photoshop after installing or the family will not appear in the font menu.

Glacial Indifference **Regular** is the wordmark face. **Bold** is the headline face. Italic is
almost never used.

## Canvas

| Use | Size | Notes |
|---|---|---|
| Instagram feed | 1080 x 1350 | the workhorse |
| Instagram story | 1080 x 1920 | keep everything out of the top 260px and bottom 340px (D-020) |
| Print poster A3 | 3508 x 4961 at 300 DPI | for the launch event or a studio window |

Colour mode RGB for anything going to Instagram. Only switch to CMYK if a printer asks for it.

## Colours

| Role | Hex |
|---|---|
| Blush peach, primary | `F0CDB3` |
| Cream / linen | `F6EEE5` |
| Caramel | `C6926E` |
| Terracotta | `833827` |
| Warm charcoal, primary type | `4A433C` |
| White | `FFFFFF` |

Never black. Never a cool grey. If something needs to be dark, it is warm charcoal.

## Type spec

Photoshop measures tracking in 1/1000 em, so our brand values convert like this:

| Element | Font | Case | Tracking (PS value) | Notes |
|---|---|---|---|---|
| SPORTIF wordmark | Glacial Regular | caps | **-59** | this is the canonical lockup value, do not round it |
| "collection" subline | Glacial Regular | lowercase | **+60** | sits under a rule beneath the wordmark |
| Big headline | Glacial Bold | caps | **-20** | ref 03 style, set to full bleed width |
| Small caps labels | Glacial Regular | caps | **+160** | footers, callouts |

**The lockup** is SPORTIF, then a horizontal rule, then "collection" centred under it (D-017).
Proportions: the rule is **0.43x the width of the wordmark**, and "collection" is sized so the rule
is **0.75x the width of the subline**. Rule thickness is about 4.5% of the wordmark's cap height.

**No @handle** on anything going on Instagram (D-018). Instagram already prints the account name.
The handle is only for assets travelling without the account attached: stockist decks, print, press.

## The depth build, layer by layer

Bottom to top:

1. **Background**, flat colour fill, peach or cream.
2. **Headline**, Glacial Bold, huge, tracked -20. Let it run past the canvas edges if it wants to.
   This is the layer she will sit in front of.
3. **Subject cutout**, your Photoshop cut of the generated plate, on transparency.
4. **Foreground type, optional**, a second type layer ON TOP of the subject. This is the ref 08
   trick: one word behind her, the next word in front. That flip is what sells the depth, more than
   the size of the type does.
5. **Grain**, new layer, fill 50% grey, set to Overlay, Filter > Noise > Add Noise at about 3%,
   monochromatic. Ties the composite together. Skip it and the cutout reads as pasted.

### Making the cutout hold up

- Select Subject to start, then refine. Select and Mask, Refine Edge brush around any soft edges.
- **Shift Edge in by 1 or 2** in Select and Mask. Background removal always leaves a thin halo of
  the old background, and on our peach grounds that halo reads as a pale outline.
- Decontaminate Colors, low amount, if the plate had any colour cast.
- Output to a **Layer Mask**, not a deleted background, so you can keep adjusting.

### The shadow

Do not use Photoshop's default Drop Shadow, it goes grey and muddy on peach. Instead: duplicate the
subject layer, fill the copy with warm brown `7A4E38`, Gaussian Blur about 40, drop opacity to
around 25%, and nudge it down and slightly right. That is the same recipe as D-022 in the scripted
posters, so the two routes match.

## Save it here

`clients/sportif/generated/images/band-posters/photoshop/`

Keep the layered PSD next to the flattened export. If the PSD is where the real work lives, I want
to be able to open it, and future you will want the layers back.

## Where this fits

Two routes now exist, and both are fine:

- **Photoshop, Hugo.** Better mattes, full manual control, and the practice compounds.
- **PIL, scripted.** Reproducible, re-runs in one command when a size or a headline changes.

Use Photoshop for hero pieces and anything with a hard matte. Use the script for anything that
needs six sizes or will be rebuilt often. They share the same type spec, so the outputs sit together.
