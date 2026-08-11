# SPORTIF collection: Instagram grid banner

Three 1080x1440 (3:4 portrait) tiles that join up across one row of the profile
grid to read SPORTIF, rule, collection.

Blush peach `#F0CDB3` background, wordmark in white, Glacial Indifference.

## Post in this order

Instagram fills a row right to left, so the file numbers are the posting order:

1. `sportif-collection-tile-1-of-3-post-order.png` posts FIRST (lands on the right)
2. `sportif-collection-tile-2-of-3-post-order.png` posts SECOND (lands in the middle)
3. `sportif-collection-tile-3-of-3-post-order.png` posts THIRD (lands on the left)

Post all three back to back with nothing in between, or the row breaks up.
On the crop screen, tap Original. The default 1:1 crop breaks the alignment.

## Also here

- `sportif-collection-banner-full.png`, the 3240x1440 master before splitting
- `preview-collection-grid.png`, how the row reads with Instagram's gutters

## Notes

The centre tile carries the rule and "collection" with clear margin either side,
so nothing important sits near a gutter.

The seam does clip the crossbar of the T. Same as the first SPORTIF grid, it is
unavoidable with a 7-letter word across 3 tiles (checked by brute force across
every sensible tracking and size), and it reads correctly once the row is
complete.

Rebuild with `python3 clients/sportif/scripts-local/build_collection_grid.py`.
