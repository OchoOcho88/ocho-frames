# Lucy's second round of marks, 2026-08-26

Photos Hugo took of his screen, showing four of the v2 files with Lucy's black pen
marks on them. Originally landed as `Lucy-Wayne-pictures/changes_needed_pilates_room/`
(IMG_1783 to IMG_1786), renamed here to pair with the asset each one marks up.

## What she asked for

An X means "put the mark here", with a line drawn from the current lockup to the X.

| file | asset | her direction |
|---|---|---|
| mark-feed-ballreach.jpeg | feed-ballreach | move the lockup to the TOP RIGHT |
| mark-story-ballreach.jpeg | story-ballreach | move the lockup to the TOP RIGHT |
| mark-story-sidestretch.jpeg | story-sidestretch | move the lockup to the TOP LEFT |
| mark-story-duo.jpeg | story-duo | keep it where it is, drop it a little lower |

## How the positions were read off the photos

The photos are of a screen, at an angle, so the marks were not eyeballed. Each photo
was matched to its real asset with SIFT plus a RANSAC homography (81 to 210 inliers),
warped into the asset's own pixel space, then differenced against the asset so the only
thing left was the pen. The centre of each X in asset pixels:

- feed-ballreach     x 831, y 239   (canvas 1080 x 1350)
- story-ballreach    x 858, y 300   (canvas 1080 x 1920)
- story-sidestretch  x 396, y 137   (canvas 1080 x 1920)
- story-duo          x 219, y 395   (canvas 1080 x 1920, a stroke not an X)

## Where we could not follow her exactly, and why

- **story-sidestretch.** Her X sits at y 137, which is inside the top 260px of a story.
  Instagram prints the profile row and progress bar over that strip, so anything there
  is half hidden on a real phone. The lockup went to the same corner at y 290, the first
  clean spot below the safe line and below the ceiling beam.
- **story-duo.** Directly under her stroke is the second wooden ceiling beam. Black type
  on it is unreadable. The measured limit is y 360, so the lockup dropped from y 260 to
  y 355, which is as low as it goes without touching the beam.
- **story-ballreach.** Her X is at y 300, which puts the block top at 243, just inside
  the safe strip. Moved down 27px to y 270.

Everything is in `../created/v3/`, built by `scripts-local/build_email02_social_v3.py`.
