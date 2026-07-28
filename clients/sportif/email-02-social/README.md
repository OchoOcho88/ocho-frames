# Email 02, social batch (Lucy)

Everything for Lucy's second request lives in this folder.

## The request
Canva design shared: "Use these Pictures only for Social Media" (2026-07-24).
Lucy's message: "Hi Hugo, let's just use these images for the time being for social's
to save time. :)"

So: keep it simple, use these existing photos to make ready-to-post social content.

## What we are making
- IG feed posts, 4:5 (1080x1350)
- IG stories, 9:16 (1080x1920)
- Light-touch branding only: a small SPORTIF wordmark + @sportifcollection handle in a
  corner. Let the photo lead. No big headlines or heavy templates.

## Folder use
- `downloads/`  raw images Hugo pulls from Lucy's Canva (source of truth for this batch)
- `created/`    finished posts made here (feed + stories)

## Status
- [x] Confirmed: same 4 images as email 1. Sourcing from ../reference-images/lucy-canva-picks
      (no re-download needed). `downloads/` left empty for this batch.
- [x] Built light-touch feed (4:5) set: created/feed-{pilates,sidestretch,ballreach,duo}.png
- [x] Built light-touch stories (9:16) set: created/story-{pilates,sidestretch,ballreach,duo}.png

Built by scripts-local/build_email02_social.py (re-run to regenerate). Wordmark is
top-right, cream, over a soft top-right corner scrim for legibility. Change position/colour
there if needed.
