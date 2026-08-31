#!/usr/bin/env python3
"""Client-facing comparison: the real product colour against the full brand colour.

Lucy asked (2026-08-28) to be SHOWN what the weave tiles would look like in her
brand colour. This is that, and only that.

Two rules this file exists to honour.

1. **One variable.** Both rows are built by the CURRENT house build, so the
   only difference between them is the colour target. Comparing against the
   older files would also change the type weight and the lockup size, and the
   comparison would prove nothing.
2. **Two rows, not three.** The halfway tinted version is deliberately left out.
   It fails the same accuracy test as the full brand colour, just by half, and
   showing it invites a compromise that does not survive the reasoning.

The brand ramp runs Blush Peach #F0CDB3 (primary) to Terracotta #833827 (rich
accent), with the measured midpoint for MEDIUM. On the peach tile the type flips
to Warm Charcoal #4A433C with a light halo, because cream on peach is unreadable.

Re-runs clean, no arguments.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_texture_weight_tiles as base

ROOT = base.ROOT
FONTS = os.path.join(ROOT, "brand/fonts/glacial-indifference")
REG = os.path.join(FONTS, "GlacialIndifference-Regular.otf")
BOLD = os.path.join(FONTS, "GlacialIndifference-Bold.otf")
TILES = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles")
OUT = os.path.join(TILES, "brand-colour-options")

BLUSH_PEACH = (0xF0, 0xCD, 0xB3)
TERRACOTTA = (0x83, 0x38, 0x27)
BRAND_RAMP = {"light": BLUSH_PEACH,
              "medium": tuple(round((a + b) / 2) for a, b in zip(BLUSH_PEACH, TERRACOTTA)),
              "heavy": TERRACOTTA}

CHARCOAL = (0x4A, 0x43, 0x3C)
HALO_LIGHT = (255, 248, 240)

PAGE, INK, SOFT = (255, 255, 255), (0x4A, 0x43, 0x3C), (0x8C, 0x84, 0x7A)


def brand_tile(colourway, label):
    """The house build, with the colour target swapped for the brand ramp."""
    keep = (base.MEASURED, base.CREAM, base.SHADOW_TINT)
    base.MEASURED = dict(BRAND_RAMP)
    if colourway == "light":                 # cream on peach is unreadable
        base.CREAM = CHARCOAL
        base.SHADOW_TINT = HALO_LIGHT
    try:
        img, _ = base.build(colourway, label)
    finally:
        base.MEASURED, base.CREAM, base.SHADOW_TINT = keep
    return img


ROWS = [("THE REAL BAND COLOUR", "what the fabric actually looks like",
         lambda c, l: Image.open(os.path.join(TILES, f"sportif-weave-{c}-feed.png"))),
        ("IN THE BRAND COLOUR", "blush peach through to terracotta", brand_tile)]

ORDER = [("light", "LIGHT"), ("medium", "MEDIUM"), ("heavy", "HEAVY")]


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    tw = 400
    th = round(tw * 1350 / 1080)
    gap, lab, pad = 16, 62, 46
    W = pad * 2 + tw * 3 + gap * 2
    H = pad * 2 + (th + lab) * 2 + gap
    page = Image.new("RGB", (W, H), PAGE)
    d = ImageDraw.Draw(page)
    fb, fr = ImageFont.truetype(BOLD, 26), ImageFont.truetype(REG, 18)

    for r, (title, blurb, get) in enumerate(ROWS):
        y = pad + r * (th + lab + gap)
        d.text((pad, y), title, font=fb, fill=INK)
        d.text((pad + d.textlength(title, font=fb) + 16, y + 6), blurb, font=fr, fill=SOFT)
        for c, (colourway, label) in enumerate(ORDER):
            im = get(colourway, label).resize((tw, th), Image.LANCZOS)
            page.paste(im, (pad + c * (tw + gap), y + lab))

    p = os.path.join(OUT, "real-vs-brand-colour-for-lucy.jpg")
    page.save(p, quality=95)
    print(f"  real-vs-brand-colour-for-lucy.jpg   {W}x{H}")
