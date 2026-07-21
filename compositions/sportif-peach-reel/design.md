# Sportif peach lookbook reel (9:16, IG + TikTok)

A 15s brand-mood teaser built on the same HyperFrames engine as `sportif-teaser`.
One 1080x1920 render serves both Instagram Reels and TikTok.

## Source imagery

Three of the Session 020 cosmos-peach text-free bases, copied into `images/`:

- `scene1-training.png`  = `cosmos-peach_studio-yellow-frame_notext.png`  ("Everyday training, elevated.")
- `scene2-fashion.png`   = `cosmos-peach_portrait-sage-tank_notext.png`   ("Too fashionable not to WEAR!")
- `scene3-ritual.png`    = `cosmos-peach_beach-run-shoreline_notext.png`  ("For your morning ritual.")

Sources live in `clients/sportif/generated/images/cosmos-peach/notext/`. To swap a
scene, copy a different base over the matching `scene*.png` and re-render.

## Design

- **Card-on-peach treatment:** each 4:5 shot sits whole on the blush-peach ground
  (#F0CDB3) as a soft-shadowed framed print. Preserves the full composition (no crop),
  reads as a premium lookbook, keeps the brand colour dominant.
- Scenes 2-5 start at `opacity:0` and fade in on cue (explicit, satisfies the 0.7.64
  `gsap_fullscreen_overlay_starts_visible` lint rule). Do not remove the initial
  `opacity:0` without also converting the reveals back to `.from()`.
- Copy is the proven Lucy-voice tagline set. End card is date-free ("Coming soon" +
  @sportifcollection): the launch is on hold for trademark, so no launch date.
- The cream wordmark on peach is intentionally low-contrast (matches Sportif's real
  white-on-peach logo lockup); it trips a contrast warning in `check`, which is expected.

## Build

    npm run check        # lint + validate + inspect (hyperframes 0.7.64)
    npm run render -- -q high -o renders/sportif-peach-reel_v2_high.mp4
    npm run snapshot -- --at 1.6,4.6,7.2,9.8,12.6   # QA frames + contact sheet

Keeper: `renders/sportif-peach-reel_v2_high.mp4` (silent; add a soft music bed in-app
on upload). Renders are gitignored.

## Voiceover path (proven, NOT used)

Local TTS via `hyperframes tts` (Kokoro-82M) works but sounds noticeably synthetic;
Hugo passed on it (Session 021). Kept here for reference:

    # one-time: Python 3.11 venv with Kokoro (system python 3.9 is too old)
    /opt/homebrew/opt/python@3.11/bin/python3.11 -m venv .venvs/tts
    .venvs/tts/bin/pip install kokoro-onnx soundfile
    # then, per line:
    HYPERFRAMES_PYTHON=/Users/hugobrizuela/Desktop/hyperframes/.venvs/tts/bin/python \
      npx hyperframes@0.7.64 tts "..." -v bf_emma -s 0.92 -o line.wav

For a natural read, use a real voice or HeyGen cloud voices (needs `auth login`),
not local Kokoro.
