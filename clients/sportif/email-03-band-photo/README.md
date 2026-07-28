# Email 03, band photo (Lucy)

Everything for Lucy's third request lives in this folder.

## The request
Canva design shared 2026-07-24 with 6 reference photos Lucy added.
Lucy's message: "Hi Hugo, could you please create a picture of my 3 bands like this once
you have received them? Thank you."

So: make a styled picture of the 3 Sportif bands (LIGHT / MEDIUM / HEAVY), matching the
look of her 6 reference photos. "Received them" = the physical bands have landed
(500 units confirmed in Session 021).

## What we are making (clarified with Hugo)
Lucy shared competitor product shots (YR, Pilates Reformers Australia, moveactive) as STYLE
references. The job: recreate each reference look but with OUR Sportif bands swapped in,
using our band assets on file, in our warm brand palette (not a moveactive clone).
Approach: build ONE first (page 1, the 3-band hero) to lock the look, then roll across the set.

References (rendered from downloads/photo 1.pdf):
- pg 1: 3 bands folded + fanned/stacked on white (the hero product shot)
- pg 3: 3 bands draped over a forearm, warm bg
- pg 4/5: single band in-use on a model
- pg 6/7: moveactive IG flatlays ("almond studio essentials")

Band source: our cutouts at ../generated/images/product-bands/cutouts/ + the peach flatlay.
Palette: our warm brand (blush/cream/peach).

## Folder use
- `downloads/`  Lucy's 6 reference photos (+ any real band shots Hugo takes), source of truth
- `created/`    the band picture(s) made here

## Source band assets we already have (for reference)
- ../generated/images/product-bands/bands-flatlay-peach_low.png  (the 3 bands together)
- ../generated/images/product-bands/bands-card-{light,medium,heavy}.png  (single bands)
- ../generated/images/product-bands/cutouts/  (transparent PNG cutouts of each + the set)
- real band snapshots exist in Hugo's ~/Downloads (Sportif_bands_*.jpg, cropped_sportif_bands.png)

## Status
- [x] Lucy's 6 references reviewed (downloads/photo 1.pdf, competitor style refs: YR /
      Pilates Reformers Australia / moveactive).
- [x] Built the pg-1 3-band hero with our bands: created/ref1-3band-hero.png (fanned trio,
      warm palette, our labels). Also fixed the band cutouts at the source (removed the leftover
      peach floor strip at the bottom, band_cutouts.py trim_base).
- [x] Built a Sportif-only range-concept flat-lay: created/flatlay-concept_low.png (bands +
      imaginary pilates grip socks + pouch + towel; pg-6 could not be copied faithfully because
      it is a competitor full-range flat-lay with props that are not Sportif products).

## Constraint on the on-body references (IMPORTANT)
Pg 3/4/5/6 are competitor brands' OWN professional photos. We must NOT edit those images
(swap the band, reuse the model) into Sportif marketing: it is their copyrighted photography
and the model's release is for their brand, not Sportif. Lucy also does not want AI models.
So real-model + our-band content needs a REAL shot (Lucy or a friend using the actual bands,
even a phone photo), which we then retouch/style. The reference photos stay as private STYLE
references only. Product-only assets (hero, flat-lay) need no model and are fully ownable.

Next: a real photo for the in-use / draped-arm looks, or more product-only compositions.
