# Sportif band-in-use pilates reel (9:16) — Stage 5

Shows the band actually IN USE (pilates, band around the thighs, real SPORTIF label) in the
warm Sportif world. Card-on-peach so poses stay whole; pop (`back.out`) motion; end card with
the **Join our community** CTA pill.

Flow: SPORTIF -> standing abduction "For your practice." -> squat "Find your resistance." ->
lateral walk "Made to move with you." -> Coming soon / @sportifcollection / Join our community.

## Images (all AI-generated pilates scenes, on-brand; not real Lucy)

Generated via `clients/sportif/scripts-local/gen_band_inuse.py` (modest/elevated poses so they
pass moderation). Labels stamped via the two-image trick (see below). Poses were iterated on
Hugo's calls: the glute bridge was cut (flat/awkward); kneeling-abduction (band into knee) and
curtsy-lunge (pose off) were rejected; standing-abduction + squat + lateral-walk kept. Grip
socks on the lateral walk were edited to barefoot; a red-tinted label was re-stamped to cream.

## Label = the real product signature

`stamp_band_label.py <pose> <heavy|medium|light> low` runs a **two-image gpt-image-2 edit**
(the in-use photo + the real label crop) so the SPORTIF patch integrates with correct text and
natural perspective/lighting. Tier matches band colour (terracotta->heavy, blush->medium,
sand->light). Findings:
- **Low quality reads natural**; SPORTIF legible, small "MEDIUM" soft on extreme zoom. Hugo
  preferred this ("blurred one better") over a crisp composite.
- **Compositing the real label** (`composite_band_label.py`) gives pixel-perfect text but looks
  PASTED-ON / flat, rejected. Kept only as a reference tool.
- **Medium/high quality hit the ~60s network cap** (RemoteDisconnected) even from the VS Code
  integrated terminal (it shares the sandbox). A true macOS Terminal.app might escape it; not
  yet confirmed.

## Music (both kept for Lucy to choose beat pacing)

- `scratch_music.py` -> `audio/scratch_music.wav` (calm, ~100 BPM) -> `_v3_MUSICDEMO.mp4`
- `scratch_music_uplift.py` -> `audio/scratch_uplift.wav` (upbeat major, ~118 BPM, fuller bass)
  -> `_v3_UPLIFT_MUSICDEMO.mp4`
Both are SCRATCH previews, NOT licensed. Real music brief reference: warm, ~100 (calm) vs
~118 BPM upbeat major with moving bass. Renders/audio/snapshots gitignored.
