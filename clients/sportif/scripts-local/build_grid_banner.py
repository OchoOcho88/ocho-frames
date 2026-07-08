#!/usr/bin/env python3
"""Build the SPORTIF 3-tile Instagram grid banner.

One 3240x1440 canvas (three 1080x1440 tiles side by side), cream background,
letter-spaced Glacial Indifference SPORTIF wordmark in blush peach with the
short underline, then split into tile-1/2/3 (post RIGHT tile first on IG).
"""

from PIL import Image, ImageDraw, ImageFont

import sys

# Brand
CREAM = "#F6EEE5"
BLUSH = "#F0CDB3"

# variant support: "white" = white bg / blush text, "peach" = blush bg / white text
if "peach" in sys.argv:
    BG, INK, SUFFIX = BLUSH, "#FFFFFF", "-peach"
elif "white" in sys.argv:
    BG, INK, SUFFIX = "#FFFFFF", BLUSH, "-white"
else:
    BG, INK, SUFFIX = CREAM, BLUSH, ""
FONT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf"
OUT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/clients/sportif/generated/images/grid-banner"

TILE_W, TILE_H = 1080, 1440
W, H = TILE_W * 3, TILE_H
WORD = "SPORTIF"
TRACKING_EM = 0.28          # letter-spacing as a fraction of font size
TARGET_W = int(W * 0.80)   # wordmark spans 80% of canvas width


def word_width(font, size):
    f = ImageFont.truetype(FONT, size)
    track = int(size * TRACKING_EM)
    w = 0
    for ch in WORD:
        bbox = f.getbbox(ch)
        w += (bbox[2] - bbox[0]) + track
    return w - track, f, track


def main():
    import os
    os.makedirs(OUT, exist_ok=True)

    # find the font size whose tracked width hits the target
    size = 100
    while True:
        w, _, _ = word_width(FONT, size)
        if w >= TARGET_W:
            break
        size += 4
    total_w, font, track = word_width(FONT, size)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # vertical placement: optically centered, slightly above true center
    asc, desc = font.getmetrics()
    cap_bbox = font.getbbox("S")
    cap_h = cap_bbox[3] - cap_bbox[1]
    y = (H - cap_h) // 2 - cap_bbox[1] - int(H * 0.03)

    x = (W - total_w) // 2
    for ch in WORD:
        bbox = font.getbbox(ch)
        d.text((x - bbox[0], y), ch, font=font, fill=INK)
        x += (bbox[2] - bbox[0]) + track

    # short underline, centered below the wordmark
    baseline = y + cap_bbox[3]
    rule_w = int(size * 1.2)
    rule_h = max(6, size // 40)
    gap = int(size * 0.35)
    rx = (W - rule_w) // 2
    d.rectangle([rx, baseline + gap, rx + rule_w, baseline + gap + rule_h], fill=INK)

    img.save(f"{OUT}/sportif-grid-banner-full{SUFFIX}.png")

    # split into tiles; tile numbering = post order (right tile posts FIRST)
    for i in range(3):
        tile = img.crop((i * TILE_W, 0, (i + 1) * TILE_W, TILE_H))
        # tile at i=2 (rightmost) is posted first
        post_order = 3 - i
        tile.save(f"{OUT}/sportif-grid-tile-{post_order}-of-3-post-order{SUFFIX}.png")

    # montage preview with IG-style gutters (grey gutter so white tiles read)
    gutter = 12
    mw = TILE_W * 3 + gutter * 2
    montage = Image.new("RGB", (mw, TILE_H), "#DDDDDD")
    for i in range(3):
        tile = Image.open(f"{OUT}/sportif-grid-tile-{3 - i}-of-3-post-order{SUFFIX}.png")
        montage.paste(tile, (i * (TILE_W + gutter), 0))
    montage.thumbnail((1600, 1600))
    montage.save(f"{OUT}/preview-grid-montage{SUFFIX}.png")
    print("done", size, total_w)


if __name__ == "__main__":
    main()
