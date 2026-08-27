# The weave room, and the brand colour room

Two background treatments built by Hugo in Photoshop on 2026-08-27, on
`feed-ballreach`. Both depend on one thing: the person is separated from the room, so
the room can be treated hard while she stays untouched.

Working files: `feed-ballreach-split.psd` (grade only) and
`feed-ballreach-split-texture-heavy-bg.psd` (the full stack, both concepts in it).

## Why separate her at all

On these photos, more peach and tanned skin are the same slider. Her skin and the
studio wall both sit near hue 25 degrees, so nothing that warms the wall can leave her
alone, and a hue-based skin mask is no help because the wall qualifies as skin (91
percent of the frame on this photo). Separating her is the only way past that ceiling.
See D-043 in `scripts-local/sportif_grade.py`.

## The layer stack, bottom to top

    Layer 0                  the photo, untouched
    Color Fill 1             #833827 terracotta, blend OVERLAY, opacity 60%
    texture-heavy-tile       assets/textures/texture-heavy-tile.jpg, Blend If on
    Curves 2                 CLIPPED to the texture, blends it into the room
    Hue/Saturation 1         off, an experiment that stayed in the file
    Photo Filter 1           #F0CDB3, density 25%, PRESERVE LUMINOSITY ON
    Curves 1                 shallow S, contrast on the room
    Layer 1 copy             her, cut out, with the refined mask

Everything between `Layer 0` and her layer only ever touches the room, because she sits
on top of all of it. No inverted masks needed.

## Settings that matter, and why

- **Preserve Luminosity, ticked.** It moves colour and leaves brightness alone. Unticked
  it washes the picture out, which is D-042, learned the hard way the same day.
- **Overlay at 60% for the colour fill.** Overlay gives colour AND contrast, where Color
  mode gives colour only. Measured at 60%: the room's darkest 5 percent went from 0.317
  to 0.242 luminance and pixels pinned at pure black only moved from 0.30 to 0.33 percent
  of the frame, so nothing is lost. At 80% the wall loses its texture and reads as painted
  card. 60% is the ceiling.
- **Blend If on the texture layer.** Underlying Layer, black slider to 40 split to 90,
  white slider to 235 split to 200. This makes the weave appear only over mid tones, so
  it behaves like fabric on the wall rather than a pattern printed over the whole picture.
  The Option-drag split is what stops a hard edge appearing around every object.
- **Curves clipped to the texture.** Clipping means the adjustment sees only the layer
  below it, so the weave can be tuned without touching the terracotta or the photo.
- **Keep the BLACK lockup on terracotta.** Counterintuitive but measured: black on that
  terracotta is 6.8:1 contrast, white is 2.1:1. Terracotta sits at 43 percent luminance,
  a mid tone, so black has more to work with. White looks elegant at full size and
  vanishes on a phone.

## The mask

Select Subject, then Select and Mask with Shift Edge -15%, Feather 0.5px, Smooth 2,
Decontaminate Colors 60%, output to New Layer with Layer Mask.

A hard colour behind her makes any leftover rim of pale wall visible instantly, which is
what fringing is. Shift Edge pulls the outline inside the contaminated pixels;
Decontaminate repaints the remaining edge using her own colours. Decontaminate changes
real pixels, which is why Photoshop forces it onto a new layer. Keep the original layer
switched off rather than deleting it.

Ease Shift Edge back toward -8% if hair starts looking cut out. A soft edge on hair reads
as real, a hard one never does.

## Tile versus plate

Hugo used `texture-heavy-tile.jpg` (1024px) and at 1080x1350 that is roughly one repeat,
so no grid is visible. On a 1920-tall story it would repeat twice and the seam becomes
findable. **Use `texture-heavy-plate.jpg` for story crops.**

## Status

Not house method yet. Both treatments go to Lucy on 2026-08-27 as concepts alongside the
ungraded set she actually asked for, on one photo only. Building the other seven is
deliberately deferred until she reacts to the idea.
