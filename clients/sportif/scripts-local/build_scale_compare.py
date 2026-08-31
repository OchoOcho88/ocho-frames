#!/usr/bin/env python3
"""Review sheets for the lockup scale ladder (V1 Bold, real product colours).

  scale-thumbnail-test.jpg  each tile downsampled to a real 128px grid thumb,
                            then blown back up with nearest-neighbour so no
                            detail is invented. This is the decisive view.
  scale-full.jpg            whole tiles, so nothing is won at thumbnail size
                            and lost at full size.

Re-runs clean, no arguments.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FONTS = os.path.join(ROOT, "brand/fonts/glacial-indifference")
REG = os.path.join(FONTS, "GlacialIndifference-Regular.otf")
BOLD = os.path.join(FONTS, "GlacialIndifference-Bold.otf")
SRC = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles/scale-options")

VARIANTS = [("S0-current-066", "S0  CURRENT", "SPORTIF at 66% of the canvas"),
            ("S1-076", "S1  UP 15%", "76%, margin 96px inside the grid crop"),
            ("S2-084", "S2  UP 27%", "84%, margin 54px inside the grid crop")]
ORDER = ["light", "medium", "heavy"]

PAGE, INK, SOFT = (255, 255, 255), (0x4A, 0x43, 0x3C), (0x8C, 0x84, 0x7A)


def tile(v, c):
    return Image.open(os.path.join(SRC, v, f"sportif-weave-{c}-{v}.png"))


def page_of(render, name, tag):
    probe = render(tile(VARIANTS[0][0], ORDER[0]))
    tw, th = probe.size
    gap, lab, pad = 14, 66, 42
    W = pad * 2 + tw * 3 + gap * 2
    H = pad * 2 + (th + lab) * len(VARIANTS) + gap * (len(VARIANTS) - 1)
    page = Image.new("RGB", (W, H), PAGE)
    d = ImageDraw.Draw(page)
    fb, fr = ImageFont.truetype(BOLD, 25), ImageFont.truetype(REG, 18)
    for r, (v, title, blurb) in enumerate(VARIANTS):
        y = pad + r * (th + lab + gap)
        d.text((pad, y), title, font=fb, fill=INK)
        d.text((pad + d.textlength(title, font=fb) + 16, y + 5), blurb, font=fr, fill=SOFT)
        for c, colourway in enumerate(ORDER):
            page.paste(render(tile(v, colourway)), (pad + c * (tw + gap), y + lab))
    p = os.path.join(SRC, name)
    page.save(p, quality=95)
    print(f"  {name:<28} {W}x{H}   {tag}")


def as_thumb(im, tw=128, scale=3):
    w = round(im.height * 3 / 4)
    im = im.crop(((im.width - w) // 2, 0, (im.width - w) // 2 + w, im.height))
    th = round(tw * 4 / 3)
    return im.resize((tw, th), Image.LANCZOS).resize((tw * scale, th * scale), Image.NEAREST)


def as_full(im, tw=360):
    return im.resize((tw, round(tw * im.height / im.width)), Image.LANCZOS)


if __name__ == "__main__":
    page_of(as_thumb, "scale-thumbnail-test.jpg", "real 128px grid thumbnail")
    page_of(as_full, "scale-full.jpg", "whole tiles")
