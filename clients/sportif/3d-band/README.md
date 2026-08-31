# The 3D band (Q-016)

Target is a Shopify AR / 3D viewer asset: GLB, about 4MB total, textures at or
under 2048x2048, real-world scale, origin centred at the product's base.

## Where to put things

| Folder | What goes in it |
|---|---|
| `runs-in/<date>-<tool>/` | exactly what the generator gave back, untouched |
| `renders/` | turntable views and close-ups rendered from those files |
| `notes/` | what each run got right and wrong, and what to try next |

Keep every run, including the bad ones. A dead end that was tried is worth more
than a dead end that gets tried twice.

## Dropping a run in

Put the files in a dated folder under `runs-in/`. From Tripo, export **GLB** if
it is offered: it is self contained, it carries the textures inside the file,
and it is the Shopify target anyway. If GLB is not available, FBX or OBJ with
the texture files beside it both work. Adding the preview image or screenshot
the tool showed you is useful, because it says what the tool THINKS it made.

## What can be checked from here

A GLB can be rendered in the sandbox and looked at from any angle, and the file
itself read directly. That covers:

- turntable views and close-ups, to judge shape and the weave
- polygon count and mesh structure, which is where lumping shows up
- texture maps present, and their resolution
- real-world dimensions and where the origin sits
- whether the loop is genuinely a closed band or a smoothed slab

## The standing caveat, written before the first run (S032)

A booty band is a flat fabric loop. It is a simple shape with a large hole and a
fine repeating surface, and AI meshers tend to lump the hole closed and smooth
the weave away. If the generated mesh comes back soft, the accuracy route is a
hand built loop in Blender textured from the same photos. The weave plates in
`../assets/textures/` are the material source either way, and they are real
photographs of the product, so the texture half is already solved regardless of
what happens to the mesh.

## Runs so far

| Date | Tool | Verdict |
|---|---|---|
| 2026-08-31 | Tripo run 2 | **First closed loop.** Input was a gpt-image-2 image showing the band open as an oval, hole visible. Proves the shoot list works. Still carries the pouch bag from the same image, invented colour, 2M triangles and no real scale. Read in `notes/2026-08-31-tripo-run-2.md`. |
| 2026-08-31 | Tripo run 1 | REJECTED, all four. Prompted rather than photographed, and the prompt asked for a "strap" with a "metal label", so it made open straps with gold plaques and one standalone sign. Also 1.9M triangles, 56 to 63MB, an 8K texture, and no real world scale on any of them. Full read in `notes/2026-08-31-tripo-run-1.md`. |
