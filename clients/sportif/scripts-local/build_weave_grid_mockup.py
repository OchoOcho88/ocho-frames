#!/usr/bin/env python3
"""Two review images for Lucy's 2026-08-28 reply.

1. grid-mockup: the three colour directions as three rows of a real Instagram
   profile grid, at the 3:4 thumbnail crop Instagram applies (Jan 2025 change).
   This answers "make them fit the instagram tiles": they already do, and this
   shows the crop is safe.
2. comparison-sheet: the same nine tiles at full 4:5 with the direction named,
   so the trade-off is visible at a glance.

Re-runs clean, no arguments.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
REG = os.path.join(ROOT, "brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf")
BOLD = os.path.join(ROOT, "brand/fonts/glacial-indifference/GlacialIndifference-Bold.otf")
SRC = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles/brand-colour-options")
OUT = SRC

SETS = [("A-as-shot", "AS SHOT", "the real product colours"),
        ("B-brand-tinted", "BRAND TINTED", "halfway to the brand palette"),
        ("C-brand-full", "BRAND COLOUR", "blush peach to terracotta")]
ORDER = ["light", "medium", "heavy"]

PAGE = (255, 255, 255)
INK = (0x4A, 0x43, 0x3C)
SOFT = (0x8C, 0x84, 0x7A)


def tile(set_name, colourway):
    return Image.open(os.path.join(SRC, set_name,
                                   f"sportif-weave-{colourway}-{set_name}.png"))


def crop_3x4(im):
    """The Instagram profile-grid crop: centred 3:4 out of a 4:5 post."""
    w = round(im.height * 3 / 4)
    left = (im.width - w) // 2
    return im.crop((left, 0, left + w, im.height))


def grid_mockup():
    """A phone profile grid: 3 across, 3:4 thumbs, 2px gutters, labels at left."""
    tw, th = 300, 400
    gap = 2
    lab = 250
    pad = 34
    rows = len(SETS)
    W = pad * 2 + lab + tw * 3 + gap * 2
    H = pad * 2 + th * rows + gap * (rows - 1)

    page = Image.new("RGB", (W, H), PAGE)
    d = ImageDraw.Draw(page)
    fb = ImageFont.truetype(BOLD, 21)
    fr = ImageFont.truetype(REG, 16)

    for r, (set_name, title, blurb) in enumerate(SETS):
        y = pad + r * (th + gap)
        d.text((pad, y + th / 2 - 26), title, font=fb, fill=INK)
        d.text((pad, y + th / 2 + 4), blurb, font=fr, fill=SOFT)
        for c, colourway in enumerate(ORDER):
            x = pad + lab + c * (tw + gap)
            page.paste(crop_3x4(tile(set_name, colourway)).resize((tw, th), Image.LANCZOS),
                       (x, y))

    p = os.path.join(OUT, "grid-mockup-3x4-crop.jpg")
    page.save(p, quality=94)
    return p, page.size


def comparison_sheet():
    """Full 4:5 posts, three directions stacked, nothing cropped."""
    tw, th = 380, 475
    gap = 16
    lab = 58
    pad = 40
    rows = len(SETS)
    W = pad * 2 + tw * 3 + gap * 2
    H = pad * 2 + (th + lab) * rows + gap * (rows - 1)

    page = Image.new("RGB", (W, H), PAGE)
    d = ImageDraw.Draw(page)
    fb = ImageFont.truetype(BOLD, 24)
    fr = ImageFont.truetype(REG, 17)

    for r, (set_name, title, blurb) in enumerate(SETS):
        y = pad + r * (th + lab + gap)
        d.text((pad, y), title, font=fb, fill=INK)
        d.text((pad + d.textlength(title, font=fb) + 14, y + 5), blurb, font=fr, fill=SOFT)
        for c, colourway in enumerate(ORDER):
            x = pad + c * (tw + gap)
            page.paste(tile(set_name, colourway).resize((tw, th), Image.LANCZOS),
                       (x, y + lab))

    p = os.path.join(OUT, "comparison-sheet.jpg")
    page.save(p, quality=94)
    return p, page.size


if __name__ == "__main__":
    for fn in (grid_mockup, comparison_sheet):
        path, size = fn()
        print(f"  {os.path.basename(path):<28} {size[0]}x{size[1]}")
