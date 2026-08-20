# Poster style references

Workspace-level, not client-specific. This is Hugo's own taste in poster and layout design,
collected so it can be pointed at from any client's creative work.

## What goes in here

Poster, editorial and layout images Hugo likes: Pinterest saves, magazine spreads, campaign
posters, anything with a composition or type treatment worth borrowing.

## Naming

`poster-NN-short-slug.jpg`, numbered in the order they were added. Keep the number stable once
assigned, because the prompts reference these by name.

## Copyright position

Same rule as competitor imagery (D-014): **style only**. These are never edited into client
assets, never traced, never fed in as content to be reproduced. They inform composition,
palette, type scale and mood. They are gitignored, exactly like `competitor-analyses/product-images/`,
so third party imagery stays out of the repo.

## Index

Added 2026-08-20 (S032). **Hugo's own words** are quoted. Unquoted notes are mine.

### The active set (Hugo picked these)

Eight of eleven. 08 and 09 added on his second pass.

| File | What it is | Hugo's read | Contributes |
|---|---|---|---|
| `poster-03-eat-sleep-pilates-repeat.jpg` | enormous terracotta type on off-white, body pushing through the letterforms | "the text layout and thickness, and how the individual is positioned in front of the text" | type scale, depth, colour |
| `poster-05-activewear-campaign-highlight.jpg` | four panel campaign grid, thin annotation callouts, blue and rust | "the full grid structure and the composition of balance between photos and words" | grid, photo-to-type balance |
| `poster-06-five-shades.jpg` | five vertical Pantone strips, one model per strip in that colourway | "how the swatches correlate to the colour people are wearing" | colourway system |
| `poster-07-pilates-poster.jpg` | huge white PILATES on warm paper stock, pale pink legs cut across it | "that depth creation between text and subject" | depth, type scale |
| `poster-08-pilates-power.jpg` | cobalt type on grey, legs between the two words | kept in by Hugo. The clearest example of the flip: first word in FRONT of the body, second word BEHIND it | depth |
| `poster-09-sculpting.jpg` | PILATES repeated four times as background texture, foot and ball in front | kept in by Hugo. Repetition as pattern instead of a single headline | type as texture, depth |
| `poster-10-blur-standing.jpg` | long exposure blur, pale pink activewear on near-white | "that blur effect on the subject. I could imagine some Sportif text either behind or in front" | blur, colour, depth |
| `poster-11-blur-sitting.jpg` | seated figure, warm amber blur, double exposure feel | as above, and the warmest thing in the set, closest to our palette | blur, colour |

### In the library, not in the active set

Kept because they may earn their place later. Hugo did not call these out.

| File | What it is | Why it is still here |
|---|---|---|
| `poster-01-5-glute-exercises.jpg` | purple and pink banded workout infographic | The exercise-guide FORMAT is good content. The styling and the claim language are both out (see below). |
| `poster-02-7-day-resistance-band-workout-plan.jpg` | seven day banded plan, colour-coded rows | Same, at bigger scale. |
| `poster-04-side-stance.jpg` | sage activewear against sky, cream wordmark over the body | Proof a bare wordmark over a photo can carry a poster. |

## The thread Hugo is actually pulling on

Six of his eight picks (03, 07, 08, 09, and what he wants to do with 10 and 11) are the same thing:
**depth between the type and the subject**. Not big type. Not type over a photo. Type and body
occupying different distances from the camera.

That is a build problem, not a prompt problem, and it is covered in
`clients/sportif/band-poster-prompts.md`.

## Type weight, checked rather than assumed

Ref 03 uses a heavy grotesque, which looked at first like a problem, since Glacial Indifference is a
geometric sans and geometric sans bolds are usually light. Rendered side by side against a
Helvetica-class bold, **Glacial Bold holds its own**. It is narrower, not lighter. So to match ref 03's
visual mass we set it larger and tighter rather than reaching for a different typeface. The brand font
stands.

## Two warnings on 01 and 02

1. **Register.** Purple, pink, dense grids and stock gym imagery are the exact look the Sportif brand
   doc positions against. Borrow the format, throw away the styling.
2. **Copy.** They are full of banned language: "tone and lift your glutes", "build strength", "burn".
   Sportif makes no health or performance claims, in copy or in an infographic. An exercise guide has
   to name the movement without promising the outcome.
