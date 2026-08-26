# Lucy's friend, gym shoot: band placement job

Lucy asked for Sportif bands to be placed into five existing photos of her friend,
shot in a gym on 18 April 2025. She supplied marked-up references showing where each
band should sit. **The bands are PROPS in the scene, not worn.**

## Folders

| Folder | What goes in it |
|---|---|
| `lucy-direction/` | Lucy's marked-up references, one per photo, named to match the source |
| `plates/` | working files: clean plates, band cutouts scaled for a shot, shadow passes |
| `created/` | finished composites, the only files that go back to Lucy |

## Source photos

The originals stay untouched at
`clients/sportif/Lucy-Wayne-pictures/LUCYFRIENDGYM/Lucy Friend/`:

| # | File | Taken | What it shows |
|---|---|---|---|
| 01 | `sportif-lucyfriend-01-floor-seated.jpeg` | 2:14pm | seated on the floor against a slam ball, knees up, towel and skipping rope beside her |
| 02 | `sportif-lucyfriend-02-seated-bosu.jpeg` | 2:19pm | seated on a BOSU balance trainer, hand to chin, towel on the floor to her left |
| 03 | `sportif-lucyfriend-03-dumbbell-rack-foot-on-bench.jpeg` | 2:21pm | standing at the dumbbell rack, one foot on the bench, a dumbbell in each hand |
| 04 | `sportif-lucyfriend-04-leaning-kettlebell-rack.jpeg` | 2:31pm | leaning on the kettlebell rack, elbow on the shelf, smiling |
| 05 | `sportif-lucyfriend-05-standing-kettlebell-rack.jpeg` | 2:33pm | standing forward of the kettlebell rack, hand at her waist |

Numbering is shoot order. The first pass of these names was read off a contact sheet that
ignored the EXIF rotation flag and described three of them wrongly; corrected Session 034
against the upright images.

All five: iPhone 13 / 13 Pro Max, 4032x3024, EXIF intact, portrait orientation flag set.

## Lucy's placements

Her direction came as four iPhone screenshots with a red mark drawn where the band goes.
**Four of the five shots are marked. There is no direction for 03.**

| # | Where the band goes | Surface | Difficulty |
|---|---|---|---|
| 01 | on the floor in front of her, in the open space between the white towel and the skipping rope | flat floor, unobstructed | straightforward |
| 02 | on the floor to her left, foreground, open ground | flat floor, unobstructed | straightforward |
| 04 | on the kettlebell rack shelf, to the left of her elbow | flat shelf, in front of a mirrored wall | see the mirror note |
| 05 | on the kettlebell rack shelf, upper left | flat shelf, in front of a mirrored wall | see the mirror note |

She does not overlap any of the four marks, so **no clean plate is needed on any of them**
and she never has to be cut out.

## Naming

Lucy's direction files carry the SAME number and descriptor as the photo they annotate,
so a markup can never be confused with a source or paired with the wrong shot:

- `sportif-lucyfriend-01-floor-seated.jpeg` (source, other folder)
- `lucy-direction/direction-01-floor-seated.jpeg` (her markup)
- `created/sportif-lucyfriend-01-floor-seated-banded.jpeg` (finished)

## Method (agreed Session 034)

No AI touches these photos. Lucy's friend has not given permission for her likeness to be
put through a generator, and Hugo is not asking for it. Since the bands are props rather
than worn, none is needed anyway.

1. Pick the real band cutout matching each placement (`assets/Sportif_Bands/`, all three
   colourways, every face, colour-matched to the D-027 measured values).
2. Composite it into the photo on its own layer in Photoshop.
3. Scale against something known in frame (a dumbbell handle, the bench width).
4. Warp to sit on the surface, for the perspective squash of something lying flat.
5. Contact shadow on its own layer underneath, tight at the touch point, spreading as it lifts.
6. Match the gym's colour temperature so the band does not read as a sticker.

A clean plate is only needed where a placement overlaps her body. On open floor, an empty
bench or the rack, she is not in the way and there is nothing to cut out.

## Notes and cautions

- **Shadow colour is sampled from the photo, NOT the warm brown house value.** The
  `(122, 78, 56)` rule is for the peach and cream palette. This gym floor is dark neutral
  grey and a warm shadow will read wrong on it.
- **A flat cutout will not drape.** Our band shots are all flat or folded. If a placement
  calls for a band hanging over a kettlebell handle or a rack bar, shoot the real band in
  that pose on the white sheet in direct sun (D-026) and cut that out, rather than faking
  a drape from a flat plate.
- **These are the black-weights gym shots flagged off-brand in Session 023**, a different
  register to the warm pilates world the rest of the content lives in. Lucy has directed
  the work, so it proceeds, but the tonal gap is on the record.
- No band appears in any of the five originals.
- **The kettlebell rack stands against a mirrored wall.** Shots 04 and 05 both place the band
  on a shelf with the mirror right behind it, and the mirror is clearly showing reflections of
  the kettlebells and of her. A band composited onto that shelf with no reflection behind it
  will read as wrong to anyone who looks, so those two need a flipped, dimmed, slightly
  offset copy of the band on a lower layer inside the mirror. That is the hardest part of
  this job, and it is why 01 and 02 are the ones to build first.
- **No direction for 03.** Either Lucy skipped it or a screenshot did not come through. Worth
  asking her before assuming it is out.
