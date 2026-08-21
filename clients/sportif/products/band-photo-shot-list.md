# Band photo shot list (light and medium)

> Written S032, for Hugo. The heavy band is already shot and cut out. This is how to shoot the
> other two so all three match well enough to sit side by side in one image.
> Unblocks Q-015, and with it the colourway strips (ref 06), the range card and the wholesale
> line sheet.

## Shoot 2 result (2026-08-20): reshoot needed, one reason

Hugo shot all three bands in one sitting, which was the important part and it worked. Twenty two
frames, every face covered, all three weights confirmed by their labels. Renamed and filed.

**But they were shot on a blue card, and the colour is not recoverable.** Measured against the
first shoot, whose heavy band is known good at `#8F5B47`:

| | hex | hue | saturation |
|---|---|---|---|
| Heavy, shoot 1 (correct) | `#8F5B47` | 17 deg | 50% |
| Heavy, shoot 2 as shot | `#736A88` | 258 deg | 22% |
| Heavy, shoot 2 white balanced | `#83635E` | 7 deg | 28% |

A caramel band came back reading purple. Correcting white balance against the cream label pulls the
hue back to roughly right, but **saturation only recovers to 28% against a true 50%**. The blue field
filled the frame, the camera balanced for it, and the red channel simply never recorded the
separation. There is nothing in the file to restore.

There was also no neutral in the set to correct against. The sheet under the bands in the family shot
is blue card, not white paper, so the one safeguard that would have rescued this was not in frame.

**Still usable from shoot 2:** shape, weave texture, the labels, every framing. Fine as AI product
references and fine for cutting practice in Photoshop.
**Not usable:** anything where the colour is the point. That is the colourway strips, the range card,
the line sheet, and anything Lucy sees.

## Shoot 3 test frame (2026-08-21): this is the setup

Hugo re-shot the light band on a **white cloth in direct sun** and asked whether it was better than
the shaded set. It is, decisively, and it is the setup to use.

| Same light band | hex | hue | saturation |
|---|---|---|---|
| Blue card, in shade | `#798096` | 226 deg | 19% |
| White cloth, direct sun, as shot | `#8B7B69` | 32 deg | 24% |
| White cloth, direct sun, corrected | `#C2A883` | 34 deg | **33%** |

**Why the shade was the real culprit.** Open shade outdoors is lit by blue sky, not by the sun. So the
old set had two blue sources stacked: blue skylight plus a blue card. Direct sun is a strong warm
source that overwhelms the sky, which is why the hue lands right.

**And now the correction actually works**, because the white cloth is a real neutral sitting in every
frame. Correcting against it puts the moulded label at hue 39 / 36%, against the known-good label at
hue 35 / 34%. That is a match. The blue-card set could not be corrected because nothing neutral was
in shot.

**Shooting on white means the colour reference is always in frame.** No separate white-paper shot is
needed any more. That replaces step 8 below.

### Two refinements before the real shoot

1. **Soften the sun.** Direct sun leaves a hard shadow down one side of the band, and that shadow is
   filled by blue sky, so it goes cold. Fix by standing a **sheet of white paper or card just outside
   the frame on the shadow side** to bounce warm light back in. Keeps the sun's colour, kills the
   hard edge. Thin cloud does the same job for free.
2. **Expose for the band, not the sheet.** The test frame is about a third of a stop dark because the
   bright white cloth pulled the meter down. Tap the **band**, then drag the little sun slider up
   slightly before locking. Nothing is blown, so this is recoverable, but getting it right in camera
   is better than lifting it later.

## Shoot 4 (2026-08-21): PASSED. This is the usable set.

Twelve frames in `assets/Sportif_Bands/Original_New_method/`, white sheet, direct sun, renamed to
the D-021 convention. **The colour verifies.**

Corrected against the white sheet in the family shot, the heavy band lands at **hue 17 deg / 53%
saturation** against the known-good first shoot at **hue 17 deg / 50%**. Hue is exact, saturation is
within three points. That is a match, and it means the whole set can be trusted for colour.

### The three colourways, measured

| Band | hex | RGB | hue / sat |
|---|---|---|---|
| LIGHT | `#B8A080` | 184 160 128 | 35 deg / 30% |
| MEDIUM | `#9D7459` | 157 116 89 | 24 deg / 44% |
| HEAVY | `#6C4333` | 108 67 51 | 17 deg / 53% |

Taken from the family shot, because all three sit under identical light in one frame. That is
exactly what the family shot is for. Swatch card at `clients/sportif/products/band-colourways.jpg`.

**Note for the strips:** the real product runs DEEPER than the brand palette swatches. Heavy at
`#6C4333` is well below terracotta `#833827`. Build the colourway strips off these measured values,
not off brand.md's palette table, or the strip will not match the band sitting on it.

### What is in the set

| Band | front folded | back flat | grip A | grip B |
|---|---|---|---|---|
| Light | yes | yes | **missing** | **missing** |
| Medium | yes | yes | yes | yes |
| Heavy | yes | yes | yes | yes |

Plus two family shots. No front-flat and no label close-ups this round, but the front-folded frames
carry the label and the family shot reads all three labels cleanly, so neither blocks anything.

**Only real gap: the light band's two grip shots.** Four frames next time out and the set is
complete: light grip A, light grip B, and a label close-up or two if convenient.

---

## The one rule

**Shoot all three bands in one sitting, in the same spot, without touching the light.**

Everything below serves that. If the light or the white balance shifts between bands, the three
caramels come back slightly different, and the moment they sit next to each other in a strip
poster it reads as a printing error rather than a colourway. Re-shooting the heavy alongside the
other two is cheaper than trying to match colour afterwards, so **re-shoot all three**, even
though heavy is already done. Keep the existing heavy set either way.

## Setup

- **Surface:** plain white or light grey. Not peach, not wood, and NOT BLUE. This is the one that cost shoot 2. Blue is the opposite of caramel on the colour wheel, so it is the single worst choice for warm product. White printer paper, a white sheet, or a grey card. A coloured surface
  bounces its colour up into the band and contaminates the cutout edge, which is the thing that
  makes a composite look pasted.
- **Light:** **direct sun, softened.** Proven in the shoot 3 test. Do NOT use open shade outdoors:
  it is lit by blue sky and that is what wrecked shoot 2. Stand a sheet of white card just outside
  the frame on the shadow side to bounce warm fill back in and soften the hard edge. Thin cloud does
  the same job. Indoors near a big window works too, as long as the room is not painted a strong
  colour.
- **Camera:** phone directly overhead, band running top to bottom of the frame, filling most of
  the height. That is what the heavy set looks like, so matching it keeps the scale consistent.
- **Lock exposure.** Tap the band, lift the sun slider slightly, then press and hold until AE/AF
  LOCK appears, and do not tap the screen again. Note: **AE/AF Lock does NOT lock white balance**,
  that is not available in the stills camera. It does not matter, because the white sheet is the
  reference and I correct against it per frame. Full phone setup at `iphone-camera-setup.md`.
- **Do not crop in the phone.** Full frame, every shot. Cropping throws away pixels I may want.

## The shots, per band

Six per band, the same six that exist for heavy:

1. **Front flat**, label near the top edge
2. **Front folded**, one soft fold with the label sitting mid band
3. **Back flat**, the plain reverse
4. **Inside grip A**, the striped grip face
5. **Inside grip B**, the grip face from a second angle
6. **Label close up**, filling the frame

Three bands times six shots is eighteen frames. Then:

7. **One family shot** of all three together, laid parallel, same distance. Even though I would
   normally build a lineup from the individual cutouts (more control over spacing), a real group
   shot is the safety net that proves the three colours actually sit together.
8. ~~One frame with white paper as a colour reference.~~ **Not needed once the surface is white.**
   The white surface is the neutral, and it is in every single frame, which is better.

## After the shoot

- **HEIC is fine, do not convert to JPEG.** HEIC reads directly once `pillow-heif` is installed
  (`pip install pillow-heif --break-system-packages`, a few seconds, needed once per sandbox
  session). It keeps the EXIF and the full capture data, both of which a JPEG conversion throws away.
- **Keep the originals as well as the cutouts.** Put the untouched camera files in
  `assets/Sportif_Bands/originals/`. The background removal strips the EXIF, so the cutouts lose
  the camera data, and if a matte comes out badly I need the original to redo it.
- **Naming**, same convention as the heavy set (D-021):
  `sportif-band-<weight>-<face>.png`, weight being `light`, `medium` or `heavy`, face being
  `front-flat`, `front-folded`, `back-flat`, `inside-grip-a`, `inside-grip-b`, `label-detail`.
- Drop them in `clients/sportif/assets/Sportif_Bands/` and tell me.

## What it unlocks the moment they land

- **Colourway strips** (ref 06, Hugo's pick): the strip colour matching the band colour, three up.
- **The three band lineup**, which is the range card.
- **The wholesale line sheet**, needed for the gym placements in the parallel wholesale track.
- Every prompt in `band-poster-prompts.md` gains the option of showing the full set rather than one
  band.

## Worth checking while you have them in hand

The heavy band's label reads SPORTIF over a rule over HEAVY. Confirm the light and medium labels
follow the same lockup with their own weight word, and that the moulded label colour is identical
across all three. If the factory varied it, that is worth knowing now rather than discovering it in
a poster.
