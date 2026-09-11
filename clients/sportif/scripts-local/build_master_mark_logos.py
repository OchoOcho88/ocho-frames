#!/usr/bin/env python3
"""SPORTIF / rule / collection master mark (D-017) as standalone logo files, Pantone 162 C (D-051).

Lucy's own logo files (assets/05, assets/08) predate the master mark: they are SPORTIF and
the rule only. Her collection lockup exists only as a 500px reference
(Sportif_Collection/Sportif_Collection_wordmark.jpg), too small to hand back. This rebuilds
it at 2000px from the real font, in the two colourways of her originals.

DEFAULT = Lucy's own artwork (D-052, Hugo's pick S039): every proportion is measured off her
500px original, so "collection" is bigger and untracked and the gaps are tighter than the house
lockup. Matches her artwork within a pixel at 500px. SPORTIF_LOCKUP=house builds the house
lockup instead (the spacing on the weave and grid tiles), tagged -HOUSE. Font helpers are
imported from build_texture_weight_tiles.py rather than copied (D-050).

Run: python3 clients/sportif/scripts-local/build_master_mark_logos.py
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_texture_weight_tiles as base  # noqa: E402  (house lockup, D-017)

ROOT = base.ROOT
OUT = os.environ.get("SPORTIF_OUT", os.path.join(ROOT, "clients/sportif/assets/logo-pantone-162c"))

SIZE = 2000
PEACH = (0xFF, 0xBE, 0x9F)   # Pantone 162 C, D-051
CREAM = (0xFF, 0xFB, 0xF8)   # the cream of her peach-on-cream original
WHITE = (0xFF, 0xFF, 0xFF)

WORD_W_FRAC = 0.418          # SPORTIF width / canvas, measured off her reference (209 of 500px)
LIFT = 0.033                 # block centre sits this far above canvas centre on her reference

# Default reproduces Lucy's own artwork (D-052); SPORTIF_LOCKUP=house gives the house lockup.
# Her artwork:
# "collection" untracked and bigger, tighter gaps. All measured off her 500px original
# (SPORTIF 209 wide / cap 45, rule 86 wide 21 below the cap, "collection" 119 wide 11 below the rule).
MODE = os.environ.get("SPORTIF_LOCKUP", "reference")
if MODE == "reference":
    SUB_TRACK_EM = 0.0
    RULE_OF_WORD = 86 / 209
    SUB_OF_WORD = 119 / 209
    GAP_ABOVE, GAP_BELOW = 21 / 45, 11 / 45
    TAG = ""
else:
    SUB_TRACK_EM = base.SUB_TRACK_EM
    RULE_OF_WORD = base.RULE_OF_WORDMARK
    SUB_OF_WORD = base.RULE_OF_WORDMARK / base.RULE_OF_SUBLINE
    GAP_ABOVE, GAP_BELOW = 0.44, 0.42
    TAG = "-HOUSE"

JOBS = [
    (f"SPORTIF-collection-logo-white-on-peach-PANTONE162C{TAG}.png", PEACH, WHITE),
    (f"SPORTIF-collection-logo-peach-on-cream-PANTONE162C{TAG}.png", CREAM, PEACH),
]


def lockup(bg, ink):
    img = Image.new("RGB", (SIZE, SIZE), bg)
    d = ImageDraw.Draw(img)
    cx = SIZE / 2

    wf = base.fit_to_width(d, base.WORDMARK, SIZE * WORD_W_FRAC, base.TRACK_EM)
    wtrack = wf.size * base.TRACK_EM
    wb = d.textbbox((0, 0), base.WORDMARK, font=wf)
    cap = wb[3] - wb[1]
    _, word_w = base.tracked_width(d, base.WORDMARK, wf, wtrack)

    rule_t = max(2, round(cap * 0.045))
    gap_above_rule, gap_below_rule = cap * GAP_ABOVE, cap * GAP_BELOW
    rule_w = word_w * RULE_OF_WORD

    sf = None
    for s in range(8, 600):
        f = ImageFont.truetype(base.REG, s)
        _, cw = base.tracked_width(d, base.SUBLINE, f, s * SUB_TRACK_EM)
        if cw >= word_w * SUB_OF_WORD:
            sf = f
            break
    stro = sf.size * SUB_TRACK_EM
    sb = d.textbbox((0, 0), base.SUBLINE, font=sf)
    sub_h = sb[3] - sb[1]

    block_h = cap + gap_above_rule + rule_t + gap_below_rule + sub_h
    top = (SIZE - block_h) / 2 - SIZE * LIFT

    base.draw_centred(d, base.WORDMARK, wf, wtrack, cx, top - wb[1], ink)
    ry = top + cap + gap_above_rule
    d.rectangle([cx - rule_w / 2, ry, cx + rule_w / 2, ry + rule_t], fill=ink)
    sy = ry + rule_t + gap_below_rule
    base.draw_centred(d, base.SUBLINE, sf, stro, cx, sy - sb[1], ink)
    return img, (wf.size, sf.size, round(rule_w), rule_t)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, bg, ink in JOBS:
        img, sizes = lockup(bg, ink)
        img.save(os.path.join(OUT, name), optimize=True)
        print(f"wrote {name}  SPORTIF {sizes[0]}pt, collection {sizes[1]}pt, rule {sizes[2]}x{sizes[3]}")
