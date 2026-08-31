# Shot list: references for the 3D band

Written 2026-08-31 after Tripo run 1 came back as flat straps.

**The whole reason this shoot exists:** every band photo in the workspace shows
the band pressed FLAT. There is not one frame anywhere where the hole is
visible. A flattened loop photographed from above is the same picture as a
strap, so no generator can tell the difference. That is why run 1 made straps.

**Updated 2026-08-31 after run 2, which worked.** Fed a gpt-image-2 image showing
a band lying OPEN as an oval with the hole visible, Tripo returned a genuine
closed loop. So the target staging is no longer a guess, it is a copy of a frame
that is known to work. Reproduce it with the real product.

## Lighting: these are GEOMETRY shots, not colour shots

This is the one place the house setup does not apply. D-026 specifies direct sun
because the problem it solved was COLOUR, and direct sun is what makes the
measured colourways come back right.

Reconstruction wants the opposite. Hard sun throws a strong cast shadow, and a
mesher reads a hard shadow edge as geometry, which is a good way to get a lump
welded to the side of the band. What it wants is soft even light, a plain
background, and the object clearly separated from what it is sitting on.

So for these frames: **bright indirect light, plain white or light grey
background, no hard shadow.** Colour accuracy does not matter here, because the
colour comes from the measured D-027 values and the real weave plates later,
never from the mesh. Shoot the colour set separately under D-026 if it is needed.

**One object in frame. Nothing else.** Run 2's input had a pouch bag beside the
band and Tripo modelled the bag as well, welded into the same mesh. No props, no
hands, no second band, no ruler in the reconstruction frames.

---

## Set 0: the one frame that matters most, shoot this first

A single copy of what already worked, with the real band.

- Band lying OPEN as a relaxed oval on a plain light surface
- Camera above and to one side, roughly 30 to 45 degrees down, NOT straight down
  and NOT straight on, so you can see through the hole AND see the far side of
  the loop rising behind it
- Fills most of the frame, nothing else in shot

Filename: `3d-hero-oval.jpg`

Run ONE Tripo job on this single image before shooting anything else. It is the
cheap test. Run 2 was a single image job and it produced the loop, so if this
frame is right the shape problem is closed and the rest of the shoot is about
quality rather than viability.

## Set A: the four orthogonal views (only if Set 0 needs improving)

Set the band into ONE three-dimensional pose and photograph it from four sides
without moving it. Same pose, same distance, same height, four angles at ninety
degrees. This is what multi-view reconstruction actually needs.

Getting a floppy loop to hold a shape, in order of preference:

1. **Stand it on edge.** The heavy band is stiff enough that it may hold an oval
   standing up on its own. Try this first, it needs no prop.
2. **Hang it.** Over a hook or a door handle so gravity makes a long oval. Only
   the top few centimetres are obstructed.
3. **Prop it.** Over something cylindrical and matte white. Anything shiny or
   coloured will confuse the reconstruction.

Shoot: `3d-front.jpg`, `3d-right.jpg`, `3d-back.jpg`, `3d-left.jpg`

Camera at the band's mid height, level, not looking down at it.

## Set B: the hole, said plainly

Two frames whose only job is to prove this is a closed loop.

- `3d-hole-through.jpg` : looking straight through the opening
- `3d-open-oval.jpg` : laid on the sheet but opened into an oval, shot from
  directly above, so the hole reads as a hole

## Set C: the detail that keeps getting lost

- `3d-label-straight.jpg` : the moulded label square on and filling the frame.
  It is a CREAM MOULDED RUBBER patch, not metal, and every generated version so
  far has made it gold and misspelled it. This also closes Q-020.
- `3d-grip-strips.jpg` : the inside face, showing the two black silicone strips.
- `3d-edge-on.jpg` : the band's edge, so the thickness is visible.

## Set D: scale

- `3d-with-ruler.jpg` : the band laid flat with a ruler alongside it, in frame.

And write these three numbers down, in millimetres, measured not estimated:

- width across the band
- length laid flat, folded end to folded end
- fabric thickness

Scale is the one thing that cannot be recovered later. Every model Tripo
returned was normalised into a 2 x 2 x 2 unit cube with no dimensions at all.

---

## Prompt for the retry

Paste this, with Set A as the multi-view input:

```
A closed elastic fabric loop resistance band, like a wide continuous ring of
knitted fabric. It is a seamless loop with a large opening through the middle,
not a strap and not a belt. Knitted textile with a fine diagonal rib, matte,
no shine. A small cream moulded rubber label sits on the outer face. Two black
silicone grip strips run around the inner face.
```

Notes on the wording, so it does not drift back:

- "closed loop", "continuous ring", "opening through the middle" all say the
  same thing three ways. Say it three ways.
- "not a strap and not a belt" is there because those are exactly where run 1
  landed when left to itself.
- "moulded rubber", never "metal" or "badge". Run 1 said metal and got a gold
  plaque, including one run that was nothing but the plaque.
- No weight word in the prompt. The label text comes out mangled every time
  (run 1 gave HESVY and eaif), so the label is fixed from the real photograph
  afterwards, the same conclusion D-033 reached for the posters.

---

## What still has to be fixed afterwards, and it is not Hugo's problem

Even a perfect mesh arrives failing the Shopify spec, exactly as run 1 did:
about 1.9 million triangles against a target in the tens of thousands, 56 to
63MB against 4MB, an 8192 texture against a 2048 cap, and no real world scale.

All four are post-processing and all four can be done from the workspace:
decimate, rescale to the measured millimetres, move the origin to the base,
resize and repack the maps. So the retry only has to get ONE thing right, which
is the SHAPE. Everything else is recoverable.
