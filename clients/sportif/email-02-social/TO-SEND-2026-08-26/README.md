# Staged set, 2026-08-26

Both folders carry Lucy's new lockup placement from her 2026-08-26 marks. The only
difference between them is colour.

- `natural/` : the photos as they are, no grade at all. Source `created/v3/black/`.
- `peach/`   : the same eight files with the Sportif house grade at 0.45.
               Source `created/v4/black/`.

Eight files each: four feed at 1080x1350, four story at 1080x1920. Black lockup.
The white and outline treatments of both sets sit in `created/v3/` and `created/v4/`
if Lucy ever picks a different one.

## Revision, 2026-09-17 (S042)

`story-sidestretch.png` only, both colourways. Lucy: "move the SPORTIF collection
above her hand, the middle of the logo to line up with middle finger." The mark
moved from the top left (block y 290) to above her raised hand, centred on her
middle finger: wordmark centre x=343 against a middle finger centre of x=340,
ink bottom y=280 against fingertips starting at y=306.

Two things to know about this folder now:

1. That placement sits ABOVE `STORY_SAFE_TOP` (y=260), knowingly. Above her hand
   and inside the IG story safe zone cannot both be true on this frame, and the
   story already uses the full height of the source so there is no crop to borrow
   from. On Instagram Stories the top of the wordmark sits close to the username
   row. Off-platform (feed, Pinterest, wholesale deck) it is unaffected.
2. The other seven files in each folder are still the 26 Aug renders and were NOT
   refreshed from `created/`. A rebuild on the current Pillow and FreeType no
   longer reproduces them byte for byte (see `docs/gotchas.md`), so only the one
   changed file was copied across. `created/v3` and `created/v4` were reverted to
   their committed 26 Aug state afterwards, so they still hold the OLD sidestretch
   placement. The scripts are the source of truth for the new one: re-running them
   reproduces this revision, and everything else it emits should be ignored.
