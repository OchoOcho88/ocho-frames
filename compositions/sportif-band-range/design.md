# Sportif band range reel (Light / Medium / Heavy, 9:16)

Calm product reel: SPORTIF -> flatlay "Three strengths." -> LIGHT/MEDIUM/HEAVY band cards
with tier + kicker -> "Coming soon". Card-on-peach engine; frame bg #EEC7AF matches the
product images' peach so the bands blend into the ground. The flatlay is feathered
(Gaussian border alpha) so its edge melts in, no rectangle.

Images come from the real-band pipeline: see
`clients/sportif/products/real-bands-content-process.md`. Build:
`npm run check && npm run render -- -q high -o renders/sportif-band-range_v3_high.mp4`.
Keeper: `_v3_high.mp4` (silent) + `_v3_MUSICDEMO.mp4` (calm scratch bed, preview only).
Renders/audio/snapshots gitignored.
