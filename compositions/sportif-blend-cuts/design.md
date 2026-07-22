# Sportif lifestyle + product beat-cut blend (9:16)

The strongest format: alternates full-bleed peach LIFESTYLE shots with the real BANDS
(contained on peach) as hard cuts on a 120 BPM grid, with zoom-punch + double-time build +
"Coming soon" end card. Reads as one warm world because the bands ARE the peach palette.

`gen_blend_cuts.py` is the source of truth (edit MAIN/BUILD order, BPM). `life*` images use
`object-fit: cover` (full-bleed), `prod*` use `contain` (band floats on peach). Re-run the
generator, then `npm run render -- -q high`. `_v1_MUSICDEMO.mp4` carries a punchy 120 BPM
scratch bed (preview only, not licensed).

Works by juxtaposition (models are not literally using the bands). Pipeline + gotchas:
`clients/sportif/products/real-bands-content-process.md`. Renders/audio/snapshots gitignored.
