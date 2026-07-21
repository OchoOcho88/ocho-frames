# Sportif peach beat-cut montage (9:16, IG + TikTok)

A fast, rhythmic montage of the Session 020 cosmos-peach images — hard cuts on the
beat with a per-image zoom-punch — versus the calm `sportif-peach-reel` lookbook.
15s, 1080x1920, serves both Reels and TikTok. Built as a brand-mood / "what's
possible" piece; shown to Lucy (Session 022) to give her a feel for future content.

## Build

`build_cuts.py` generates `index.html` from a 120 BPM grid. Re-run after edits:

    python3 build_cuts.py
    npm run render -- -q high -o renders/sportif-peach-cuts_v3_high.mp4
    npm run snapshot -- --at 0.5,2.25,5.25,8.1,11.9,13.5   # QA

Tunables at the top of build_cuts.py: `BPM` (cut speed), `HIGHLIGHTS` (the double-time
build section), `main`/`INTRO` timing, and `DURATION` (end-card hold). Images are
`img00..img13` in cut order (copied from clients/sportif/generated/images/cosmos-peach/
notext/). Swap a cut by overwriting the matching `imgNN.png`.

Structure: SPORTIF wordmark flash (0-1s) -> 14 cuts on the beat (1.0-7.5s) -> double-
time build through the punchiest shots (8-11s) -> date-free "Coming soon" end card that
holds ~3.5s to 15s. Full-bleed (punchier than cards) center-crops the group shots at the
edges; acceptable at cut speed, swap for solos if it bothers.

Gotcha fixed (Session 022): the intro used shared `.wm`/`.rule` selectors that also
grabbed the end-card wordmark and left it hidden. Intro selectors are now scoped to
`#intro`. Keep them scoped.

## Music

The cuts are on a 120 BPM grid, so any ~120 BPM track dropped in-app on upload lines up.
For an exact match, mux a real licensed track and run `hyperframes beats` to snap cuts to
its beats.

`scratch_music.py` synthesizes a SCRATCH 120 BPM bed (kick/hats/pad, via the .venvs/tts
python) purely to preview the sync — NOT licensed, NOT for publishing. The
`_MUSICDEMO.mp4` render is that scratch bed muxed on; use only for internal preview.
Renders and audio are gitignored.
