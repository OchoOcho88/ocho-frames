# Placing a band into a photo: the full sequence

Written Session 034, from the shot 01 build. Follow it top to bottom for each shot.
Every block is self-contained, paste or type it as written.

Assumes: the bands are props lying on a surface, not worn. No AI is used anywhere.

---

## Before you start

Use the COLOUR CORRECTED cutouts, never the raw ones:

```
assets/Sportif_Bands/Bands_background_removed/colour-corrected/
    sportif-band-light-front-folded.png
    sportif-band-medium-front-folded.png
    sportif-band-heavy-front-folded.png
```

The uncorrected versions in the parent folder are about a stop dark and well down on
saturation, because the source frames were underexposed. On a white sheet you cannot see
it. On a dark gym floor the band turns to putty. The corrected ones land on the measured
colourways: LIGHT `#B8A080`, MEDIUM `#9D7459`, HEAVY `#6C4333`.

---

## 1. Open the photo and make it a PSD

```
1. File > Open:  the source photo from
     Lucy-Wayne-pictures/LUCYFRIENDGYM/Lucy Friend/

2. File > Save As...
     Format:  Photoshop  (change it, it defaults to JPEG)
     Cmd + Shift + G, then paste:
       ~/Desktop/hyperframes/clients/sportif/lucyfriend-band-placement/plates
     Name: <shot>-work.psd
```

**Never press Cmd S before this step.** The document is still a JPEG, so a plain Save
flattens everything and writes over Lucy's original photo. That is the one destructive
mistake available in this whole process.

Leave Embed Color Profile: Display P3 ticked. Convert to sRGB only at final export.

---

## 2. Place the band

```
1. File > Place Embedded...   (NOT Open, NOT copy and paste)
     pick the colour-corrected PNG

2. In the options bar, with the chain link between W and H ON:
     W: 21%      (then Tab)
     Rotation: about -101      (90 to lay it across frame, plus ~11 to tilt)

3. Enter to commit

4. Rename the layer: band
```

Place Embedded gives a Smart Object. That means the full resolution original stays tucked
inside, so you can scale up and down as often as you like with no loss, and any blur or
noise you add later stays editable.

Copy and paste gives a flat pixel layer. Scale that down and the pixels are gone for good.

---

## 3. Squash it onto the floor

```
1. Cmd + T
2. Drag the TOP MIDDLE handle down until the band is about
   two thirds its current height on screen
3. Enter
```

Commit the rotation first, then squash as a separate step. While the layer is rotated, the
W and H fields run along the band's own axes, not the screen's, so typing H: 65% makes the
band shorter rather than flatter.

**Sanity check the size against something real in the frame.** The band is 33cm long.
It should read slightly shorter than a rolled towel (about 40cm) and roughly two and a
half times a skipping rope handle. Objects lying on the same floor at the same distance
carry the same perspective, so match them rather than trusting a number.

---

## 4. The contact shadow

This does about 80% of the work of making the band look real. Everything else is detail.

```
1. Hold Cmd and click the band layer's THUMBNAIL
     (the little picture, not the layer name)
     -> marching ants appear around the band. If not, it did not work. Retry.

2. Without clicking the canvas, click the Background layer,
   then Cmd + Shift + N for a new empty layer above it. Name it "contact".
     -> the marching ants must still be there.

3. Edit > Fill... > Contents: Color... > about #1A1A1C
4. Cmd + D to deselect
5. Filter > Blur > Gaussian Blur: 4 px
6. Arrow keys: Down 6, Left 3
7. Layer opacity: 65%

Then the second, wider pass:
8. Cmd + J to duplicate it, rename "ambient"
9. Gaussian Blur: 30 px
10. Layer opacity: 18%
```

Two layers because a real shadow has two parts: the near-black line where the object
actually touches, and a faint wider darkening from blocked ambient light. One layer can
only be one or the other, and a single soft glow is what a *floating* object casts.

Clicking anywhere on the canvas between steps 1 and 3 kills the selection. Only click in
the Layers panel.

**Keep it small.** Look at the skipping rope handles in the photo: much fatter objects,
and they still cast almost nothing. The gym light is diffuse and overhead. If your shadow
is bigger than theirs, it is too big.

**Sample the shadow colour from the photo.** The warm brown `(122, 78, 56)` house value is
for the peach and cream palette. This floor is dark neutral grey and a warm shadow reads
wrong on it.

---

## 5. Match the ambient light

The band was shot in direct sun. The gym is dim and cool. Straight out of the corrected
file it will look too bright.

```
1. Layer > New Adjustment Layer > Curves
2. Tick "Use Previous Layer to Create Clipping Mask"
     (so it only touches the band, not the photo)
3. Pull the middle of the curve down until the band drops roughly 20%
```

To judge it: white in this scene sits at 70% (rope handles) to 87% (towel), against about
100% for white in direct sun. So the band should land near 55 to 58% brightness, with its
saturation intact. Grey and dull is wrong; darker and still warm is right.

---

## 6. Grain and sharpness

The last thing that reads as pasted. The photo has grain, the band has none.

```
With the band layer selected:

1. Filter > Blur > Gaussian Blur:  0.6 px
2. Filter > Noise > Add Noise
     Amount:        2.5%
     Distribution:  Gaussian
     Monochromatic: ON
3. Judge at 100%. Cleaner than the floor -> raise to 3.5%.
   Gritty -> drop to 2%.
```

Do this AFTER the Curves, or the colour adjustment alters the grain you just added.
Both arrive as Smart Filters, so double click either one to change it later.

---

## 7. Export

```
1. Cmd + S   (safe now, it is a PSD)
2. File > Export > Export As...
     Format: JPEG, quality 90
     Convert to sRGB: ON
     to:   lucyfriend-band-placement/created/
     name: sportif-lucyfriend-<NN>-<descriptor>-banded-<COLOURWAY>.jpg
```

Put the colourway in the filename. You will not remember which is which.

---

## Per-shot notes

| # | Photo | Where the band goes | Watch out for |
|---|---|---|---|
| 01 | floor seated | floor in front of her, between the towel and the skipping rope | done |
| 02 | seated on the BOSU | floor to her left, foreground | easiest of the remaining four |
| 03 | dumbbell rack, foot on bench | **no direction from Lucy, improvised.** Building two: the bench pad, and the floor bottom left near the barbell | the bench pad is shiny vinyl, so it wants a soft blurred copy of the band underneath as well as a shadow |
| 04 | leaning on kettlebell rack | rack shelf, left of her elbow | THE MIRROR |
| 05 | standing at kettlebell rack | rack shelf, upper left | THE MIRROR |

### The mirror, shots 04 and 05

The kettlebell rack stands against a mirrored wall, and that mirror is already reflecting
the kettlebells and her. A band on that shelf with no reflection behind it will look wrong
to anyone who looks twice.

```
1. Build the band on the shelf as normal
2. Duplicate the band layer
3. Edit > Transform > Flip Vertical
4. Move it up behind the shelf line into the mirror
5. Drop opacity to about 55% and add a slight blur
6. Mask it so it only shows inside the mirror
```

Match the offset to what the real kettlebells are doing. Do not invent it, measure it off
the photo.

`Filter > Vanishing Point` is worth trying on these two. Define the shelf as a plane and
anything you drop on it takes the correct perspective automatically as you move it.
Trade-off: it works on flat pixels, not Smart Objects, so you lose Replace Contents.

---

## The staging trap (learned on shot 01)

The hardest thing to fix is not the light. It is that **our cutouts are product-shot poses
and these are candid photos.**

In shot 01 the towel is crumpled, the rope is coiled in a heap, her shoes sit at odd
angles. Everything was dropped by a person not thinking about it. Our band is a perfect
rectangle: dead straight edges, square-cut ends, identical width at both ends, absolutely
flat. It was photographed laid out and squared up on a sheet, because that is what a
product shot is.

Composite one into the other and the eye catches it instantly, even though nothing about
the light or the shadow is wrong. Measured on shot 01, the band's shadow was 16 levels
below the floor against 30 for the real skipping rope handles, so the shadow was if
anything too light. The tell was the tidiness.

**Short fix, in Photoshop:**

```
Edit > Transform > Warp
Pull the middle 6 to 10 px so the long edges bow very slightly.
Nudge one end a touch out of line with the other.
```

Tiny amounts. Not crumpled, just not machined.

**Proper fix, ten minutes away from the desk:** photograph the real band actually DROPPED
on a floor, not laid out. White surface, direct sun, house setup. Cut that out and it
composites into any of the five with no warping at all, because it is already sitting the
way a real band sits. Do this once and it serves every remaining shot.

---

## Things worth knowing

- **Judge at fit to screen (Cmd 0), not at 200%.** At 200% you will find flaws that do not
  exist at real size and spend an hour on them. Go to 100% only to check a specific edge.
- **A sideways label is correct.** The label is fixed across the band, so a band lying
  horizontally has a label reading up the frame. That is what a real photo would show.
  Only a *mirrored* label is wrong, and rotating never mirrors.
- **Photoshop has no 3D.** Adobe removed the whole toolset. `Filter > Vanishing Point` is
  the nearest equivalent for placing objects on a plane.
- **Order matters.** Rotate, commit, squash, commit, shadow, colour, then grain. Doing the
  shadow before the squash means building it twice.
