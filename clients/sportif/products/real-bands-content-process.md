# Real-product content pipeline (Sportif bands)

How we turned Lucy's 3 casual phone snapshots of the real bands into a suite of
on-brand product + lifestyle content. Reuse this whenever new real product photos
arrive. Established Session 023 (2026-07-22).

## Source material reality

Lucy's photos were casual counter snapshots (clutter, harsh window light, all three
bands folded label-end, near-identical). BUT the product itself is bang-on brand: the
three colourways (HEAVY = terracotta, MEDIUM = dusty blush, LIGHT = sand-cream) ARE the
peach palette, and the rubber labels carry the real SPORTIF lockup + the resistance tier.
Lesson: casual real photos are fine as *raw material*; the value is in restaging them.

## Step 1 — Restage onto brand grounds (gpt-image-2 edits)

`scripts-local/gen_band_product.py`. The `images/edits` endpoint with a tightly scoped
"keep EXACTLY identical" prompt strips the clutter and drops the real bands onto a clean
blush-peach studio surface. Key findings:
- **Scope the prompt to "keep the product identical, only change surroundings."** Enumerate
  what must survive (colours, knit texture, folds, the label text SPORTIF/HEAVY/MEDIUM/LIGHT).
  It then holds the labels crisp and legible **even at `quality low`.**
- **Low quality is genuinely usable** for 1080px social. Use it in-harness.
- **High quality hits the ~60s Claude Code network cap** (`RemoteDisconnected`), and running
  it in a background shell does NOT help (same egress). Run high from a **native Mac Terminal**:
  `python3 clients/sportif/scripts-local/gen_band_product.py high flatlay`

## Step 2 — Individual hero cards (crop the flatlay)

`scripts-local/make_band_cards.py`. Cut each band from the flatlay into its own 4:5 card
on peach. **Gotcha (caught by Hugo's eye): touching products bleed into each other.**
- The bands touch, so equal-thirds cropping put a sliver of the neighbour on each card's edge.
- Fix: find true band edges by **texture** (knit = high vertical-gradient variance, peach =
  smooth) for the outer edges, and by the **colour/brightness boundary** where two bands
  abut (HEAVY dark -> MEDIUM light stepped at x~592 in our flatlay). Crop **inset just clear
  of the seams**, then centre on a peach canvas. No neighbour bleed.
- Always zoom the card edges to verify (a left-edge strip crop) before shipping.

## Step 3 — Feather a peach-bg image into a peach frame

When a generated peach-bg image (e.g. the flatlay) sits on a peach video frame, its outer
vignette shows as a faint rectangle. Fix with a **Gaussian-blurred border alpha mask** (PIL):
draw an opaque rect inset by ~110px, blur by ~0.55x, `putalpha`. It melts into the frame.
Saved as `bands-flatlay-peach_low-feathered.png`.

## Step 4 — Compositions built from these assets

All 1080x1920, HyperFrames 0.7.64, silent (music added after). Generators are the source
of truth; renders/audio/snapshots are gitignored.
- `compositions/sportif-band-range/` — calm "Light / Medium / Heavy" range reel.
- `compositions/sportif-blend-cuts/` — **lifestyle+product BEAT-CUT blend** (lifestyle
  full-bleed `cover`, product `contain` on peach, alternating on a 120 BPM grid). `gen_blend_cuts.py`.
- `compositions/sportif-blend-calm/` — **lifestyle+product CALM story blend** (framed
  card-on-peach, alternating lifestyle print / product card with taglines).
- **The blend is the strongest format**: it pairs desire (lifestyle mood) with the actual
  product, which neither product-only nor lifestyle-only achieves. NOTE it works by
  juxtaposition; the models are not literally using the bands (that is the Stage 5 composite,
  not yet built).

## Step 5 — Mock music to feel the edit

Synthesize a SCRATCH bed matched to the piece's energy and mux with ffmpeg. Punchy 120 BPM
(kick/hats) for beat-cuts, calm ~100 BPM (soft pad/pluck/shaker) for editorial. Code in each
comp's `scratch_music.py` (run with the `.venvs/tts` python: it has numpy+soundfile).
**Scratch = internal preview only, NEVER publish it.** Real posts get a licensed track
(in-app on upload, or a supplied file muxed + `hyperframes beats` for exact sync).

## Environment gotchas (which python has what)

- **System python 3.9**: has Pillow (PIL), NOT numpy. Use for crops/feather.
- **`.venvs/tts` python 3.11**: has numpy + soundfile (+ kokoro), NOT Pillow. Use for audio synth.
- gpt-image-2 high quality: native Terminal only (harness ~60s cap).

## GSAP lesson

Scope per-scene selectors (`#intro .wm`, not `.wm`) when a class repeats across scenes, or
one scene's tween will grab and hide another scene's element (this hid the end-card wordmark
in the beat-cut montage until fixed).

## Step 6 — Product IN USE (pilates), Stage 5

Goal: show the band used in pilates (band around the thighs), on-brand.

- **Client gym shots are NOT the base.** Lucy's real client shots were a black-and-chrome
  weights gym, all-black outfit, skin-forward posing, the exact masculine/glam register Sportif
  positions AGAINST (White Fox anti-reference in brand.md). Restaging them even tripped
  gpt-image-2's `[sexual]` output moderation. Lesson: they're authentic but off-brand; the
  brand-aligned route is to GENERATE fresh pilates scenes. (Real band-in-use content should be a
  future proper shoot kept pilates/warm/elevated, not black-gym-glam.)
- **Generate on-brand pilates in-use scenes**: `scripts-local/gen_band_inuse.py`. Modest,
  elevated, peach-world poses (glute bridge, squat, lateral walk, standing/kneeling abduction),
  band around thighs. Keep poses MODEST/tasteful or output moderation blocks `[sexual]`. Pick
  poses that flatter and read as "in use"; drop awkward ones (a side glute bridge read flat;
  kneeling-abduction cut the band into the knee; a curtsy lunge looked off). Fix stray details
  with a scoped edit (e.g. grip socks -> barefoot).
- **Stamp the real SPORTIF label** with the two-image trick: `stamp_band_label.py <pose> <tier>
  low`. Passing the in-use photo AND the real label crop together makes gpt reproduce the
  correct text with natural perspective/lighting. Match tier to band colour. Low quality reads
  natural (SPORTIF legible, tiny sub-text soft) and Hugo preferred it. Compositing the real
  label (`composite_band_label.py`) is pixel-perfect but looks PASTED-ON, rejected. Medium/high
  hit the ~60s network cap even in the VS Code terminal (shares the sandbox); a real
  Terminal.app might escape it (unconfirmed).
- Reel: `compositions/sportif-band-inuse/` (card-on-peach, pop motion, CTA pill). Two scratch
  music beds kept for Lucy to choose pacing: calm ~100 BPM and upbeat ~118 BPM (fuller bass).
