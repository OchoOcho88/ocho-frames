# SPORTIF collection: Instagram grid banner, Pantone 162 C (reissued S039, 2026-09-11)

The same three 1080x1440 (3:4 portrait) tiles as the August set in `../grid/`, which join up
across one row of the profile grid to read SPORTIF, rule, collection. Identical layout; the
only change is the ground colour, now the brand peach Pantone 162 C, screen hex `#FFBE9F`
(D-051). Wordmark in white, Glacial Indifference.

## Post in this order

Instagram fills a row right to left, so the file numbers are the posting order:

1. `sportif-collection-tile-1-of-3-post-order-PANTONE162C.png` posts FIRST (lands on the right)
2. `sportif-collection-tile-2-of-3-post-order-PANTONE162C.png` posts SECOND (lands in the middle)
3. `sportif-collection-tile-3-of-3-post-order-PANTONE162C.png` posts THIRD (lands on the left)

Post all three back to back with nothing in between, or the row breaks up.
On the crop screen, tap Original. The default 1:1 crop breaks the alignment.

## Replacing the old row

The August row is already live. Either delete the three old tiles first (it is exactly one
row, so the rest of the grid stays aligned), or post these and drag them into place with
Instagram's grid reorder.

## Also here

- `sportif-collection-banner-full-PANTONE162C.png`, the 3240x1440 master before splitting
- `preview-collection-grid-PANTONE162C.png`, how the row reads with Instagram's gutters

## Notes

The seam still clips the crossbar of the T, same as the August set. It is unavoidable with a
7-letter word across 3 tiles (S030) and reads correctly once the row is complete.

Rebuild with:
`SPORTIF_OUT=clients/sportif/Sportif_Collection/grid-pantone-162c SPORTIF_SUFFIX=-PANTONE162C python3 clients/sportif/scripts-local/build_collection_grid.py`
