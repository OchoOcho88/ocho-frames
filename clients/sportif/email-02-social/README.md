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

## Revision 1 (2026-08-14, Lucy's reply), v2

Lucy's notes: move the feed-duo logo to the LEFT in BLACK; the ceiling beam is covering the
logo on the rest; story pilates notes to follow on Canva.

- [x] Rebuilt by `scripts-local/build_email02_social_v2.py` -> `created/v2/{black,white,outline}/`
- [x] Lockup is now LEFT-anchored and beam-aware: the script scans the left column and slides
      the lockup down until its footprint clears every dark pixel, so it can never land on the
      beam again. Chosen y is printed per file.
- [x] IG STORY SAFE ZONE fixed (not requested, but v1 was broken): v1 put story lockups at
      y=150, under Instagram's own header. Now constrained to y>=260 and clear of the bottom
      340px reply bar.
- [x] Three treatments for Lucy to choose from, all with a soft drop shadow for depth:
      black (recommended), white, black-with-white-outline.
- [x] The v1 dark corner scrim is gone. The shadow replaces it.
- [ ] AWAITING LUCY: which of the three treatments to lock as the house standard.
- [ ] AWAITING LUCY: Canva notes on the pilates picture (v2 pilates files are provisional).

Note on white: these studio walls are near-white, so the white treatment only holds together
because of a heavy shadow. If Lucy picks it, check each new photo individually.

LOCKUP SIZE: `SCALE` at the top of the v2 script drives everything (type, rule, gaps, shadow,
stroke). Currently 1.25, because Hugo checked the first pass against a real IG post on a phone and
called the lettering small. Change that one number to resize; the beam-clearance search
re-solves placements automatically against the new footprint, so don't hand-tune positions.

**MASTER MARK CHANGED (2026-08-17, Hugo's call): the lockup is now SPORTIF / rule /
collection**, per Lucy's artwork at `Sportif_Collection/Sportif_Collection_wordmark.jpg`.
This is the master mark for EVERYTHING from here, not just collection-launch artwork. The
back catalogue (posters, product shots, ads, PDFs) is still on the old wordmark+rule and will
need a pass. Proportions are derived, not eyeballed: rule = 0.43x wordmark width (our
canonical rule), then 'collection' is sized so rule = 0.75x its width, matching her
reference. Measured against the 500px original: rule/sub 0.741 vs 0.750, sub/cap 0.458 vs
0.488.

HANDLE: `@sportifcollection` is OFF these images (`DRAW_HANDLE = False`). Two reasons, in
order: it read as a stutter directly under the word "collection", and more fundamentally
Instagram already prints the account name above every post and story, so stamping it into
the image repeats information the viewer can already see (Hugo's call, 2026-08-17).

The footer code is kept, not deleted. Flip `DRAW_HANDLE = True` for anything that travels
WITHOUT the account name attached: stockist/wholesale decks, Pinterest, print, press. When
on, it's left-aligned to the same margin and positioned by the same clearance search running
upward from the bottom edge (these studio floors are full of black straps and cables, and a
fixed bottom position landed straight on them). One function, `find_clear_y`, serves both the
mark and the footer, with `prefer='top'` for the mark, `prefer='bottom'` for the footer.

ART DIRECTION OVERRIDE: `MANUAL_PLACEMENT` at the top of the v2 script. The automatic search
finds ground the type can legibly SIT on; it can't judge composition. When Hugo marks a box
on a frame, that box wins. Entries are `(x0, y0, x1, y1)` in the final image's own pixels,
and the mark is centred in the box (the boxes are drawn as zones, not tight bounds). Anything
not listed falls back to the auto search. Currently set: story-ballreach, story-sidestretch,
feed-pilates. NOTE story-sidestretch is deliberately on the RIGHT of frame, so the set is no
longer uniformly left-aligned.

WORKFLOW THAT WORKS: Hugo opens the PNG, drags a selection box where the mark should go,
screenshots it. Full-frame screenshots convert cleanly; Preview-window screenshots need the
toolbar offset backed out (~88px) so they're slightly less precise. Naming the file in the
message removes the guesswork.

Send-ready copies with client-friendly filenames: `TO-SEND-2026-08-17/` (12 files, ~20MB),
including two EXPERIMENT files (the wordmark sunk into the wall behind her on the pilates
shot, built by `scripts-local/build_pilates_bg_wordmark.py`). Those are flagged in the email
as experiments with nothing to action.

VOICE RULE BREACH, worth remembering: the first drafts of this email and this README were
full of em dashes, against the rule in the workspace CLAUDE.md. Hugo caught it. Rewritten
clean. Check any client-facing copy against that rule before sending.
