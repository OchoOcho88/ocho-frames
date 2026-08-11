#!/usr/bin/env python3
"""SPORTIF collection: 3-tile Instagram grid banner.

One 3240x1440 canvas (three 1080x1440 portrait tiles side by side) in blush
peach with a letter-spaced white SPORTIF wordmark, a short rule, and
"collection" underneath, matching Lucy's reference lockup.
Splits into tiles numbered by POST ORDER (right tile posts first on IG).
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Brand
BLUSH = "#F0CDB3"
CREAM = "#F6EEE5"
WHITE = "#FFFFFF"

BG, INK, SUFFIX = BLUSH, WHITE, ""

# paths resolve from this file, so the script works in both Cowork and Claude Code
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FONT = os.path.join(ROOT, "brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf")
OUT = os.path.join(ROOT, "clients/sportif/Sportif_Collection/grid")

TILE_W, TILE_H = 1080, 1440
W, H = TILE_W * 3, TILE_H
WORD = "SPORTIF"
SUB = "collection"
TRACKING_EM = 0.28         # SPORTIF letter-spacing, fraction of font size
SUB_TRACKING_EM = 0.06     # "collection" letter-spacing
TARGET_W = int(W * 0.80)   # wordmark spans 80% of canvas width

# lockup proportions. On the reference the rule is ~0.75x the width of
# "collection"; both are sized off the CENTRE TILE so IG gutters never clip them.
SUB_W_FRAC = float(os.environ.get("SUB_W_FRAC", 0.55))   # "collection" width / tile width
RULE_TO_SUB = 0.75                                       # rule width / "collection" width
NUDGE_UP = 0.012           # slight optical lift of the whole lockup


def tracked_width(font, text, track):
    w = 0
    for ch in text:
        b = font.getbbox(ch)
        w += (b[2] - b[0]) + track
    return w - track


def draw_tracked(d, font, text, track, cx, y, fill):
    total = tracked_width(font, text, track)
    x = cx - total // 2
    for ch in text:
        b = font.getbbox(ch)
        d.text((x - b[0], y), ch, font=font, fill=fill)
        x += (b[2] - b[0]) + track
    return total


def main():
    os.makedirs(OUT, exist_ok=True)

    # size SPORTIF so its tracked width hits the target
    size = 100
    while True:
        f = ImageFont.truetype(FONT, size)
        if tracked_width(f, WORD, int(size * TRACKING_EM)) >= TARGET_W:
            break
        size += 4
    font = ImageFont.truetype(FONT, size)
    track = int(size * TRACKING_EM)

    cap_bbox = font.getbbox("S")
    cap_h = cap_bbox[3] - cap_bbox[1]

    # "collection": sized to a share of the centre tile's width
    sub_target_w = int(TILE_W * SUB_W_FRAC)
    sub_size = 40
    while True:
        sf = ImageFont.truetype(FONT, sub_size)
        if tracked_width(sf, SUB, int(sub_size * SUB_TRACKING_EM)) >= sub_target_w:
            break
        sub_size += 2
    sub_font = ImageFont.truetype(FONT, sub_size)
    sub_track = int(sub_size * SUB_TRACKING_EM)
    sub_w = tracked_width(sub_font, SUB, sub_track)

    # --- vertical rhythm (reference: cap 41, gap 25, rule, gap 15, sub) ---
    rule_h = max(6, size // 40)
    gap_above_rule = int(cap_h * 0.60)
    gap_below_rule = int(cap_h * 0.36)
    sub_asc = sub_font.getbbox("l")
    sub_asc_h = sub_asc[3] - sub_asc[1]

    lockup_h = cap_h + gap_above_rule + rule_h + gap_below_rule + sub_asc_h
    top = (H - lockup_h) // 2 - int(H * NUDGE_UP)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    cx = W // 2

    # SPORTIF
    y_word = top - cap_bbox[1]
    draw_tracked(d, font, WORD, track, cx, y_word, INK)

    # rule, kept inside the centre tile so IG gutters never clip it
    rule_w = int(sub_w * RULE_TO_SUB)
    ry = top + cap_h + gap_above_rule
    d.rectangle([cx - rule_w // 2, ry, cx + rule_w // 2, ry + rule_h], fill=INK)

    # collection
    y_sub = ry + rule_h + gap_below_rule - sub_asc[1]
    draw_tracked(d, sub_font, SUB, sub_track, cx, y_sub, INK)

    img.save(f"{OUT}/sportif-collection-banner-full{SUFFIX}.png")

    # split into tiles; filename number = POST ORDER (rightmost posts first)
    for i in range(3):
        tile = img.crop((i * TILE_W, 0, (i + 1) * TILE_W, TILE_H))
        tile.save(f"{OUT}/sportif-collection-tile-{3 - i}-of-3-post-order{SUFFIX}.png")

    # IG-style montage preview
    gutter = 12
    montage = Image.new("RGB", (TILE_W * 3 + gutter * 2, TILE_H), "#DDDDDD")
    for i in range(3):
        t = Image.open(f"{OUT}/sportif-collection-tile-{3 - i}-of-3-post-order{SUFFIX}.png")
        montage.paste(t, (i * (TILE_W + gutter), 0))
    montage.thumbnail((1600, 1600))
    montage.save(f"{OUT}/preview-collection-grid{SUFFIX}.png")

    print(f"SPORTIF size {size}, cap {cap_h}, sub size {sub_size}, rule {rule_w}x{rule_h}")


if __name__ == "__main__":
    main()
