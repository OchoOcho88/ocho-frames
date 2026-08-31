#!/usr/bin/env python3
"""Two review sheets for the weight-line treatments.

  weightline-detail.jpg  the lockup at 1:1 pixels, which is where the weight
                         of the line is actually judged
  weightline-full.jpg    the whole tiles, so nothing gets fixed in close-up
                         and broken at feed size

Re-runs clean, no arguments.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FONTS = os.path.join(ROOT, "brand/fonts/glacial-indifference")
REG = os.path.join(FONTS, "GlacialIndifference-Regular.otf")
BOLD = os.path.join(FONTS, "GlacialIndifference-Bold.otf")
SRC = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles/weight-line-options")

VARIANTS = [("V0-regular", "V0  REGULAR", "what she has now"),
            ("V1-bold", "V1  BOLD", "same size, heavier stroke"),
            ("V2-bold-wide", "V2  BOLD WIDE", "heavier and larger on the page")]
ORDER = ["light", "medium", "heavy"]

PAGE = (255, 255, 255)
INK = (0x4A, 0x43, 0x3C)
SOFT = (0x8C, 0x84, 0x7A)


def tile(v, c):
    return Image.open(os.path.join(SRC, v, f"sportif-weave-{c}-{v}.png"))


def sheet(crop_box, scale, name, tag):
    """crop_box in source pixels, scale applied after cropping."""
    probe = tile(VARIANTS[0][0], ORDER[0]).crop(crop_box)
    tw = round(probe.width * scale)
    th = round(probe.height * scale)
    gap, lab, pad = 14, 66, 40

    W = pad * 2 + tw * 3 + gap * 2
    H = pad * 2 + (th + lab) * len(VARIANTS) + gap * (len(VARIANTS) - 1)
    page = Image.new("RGB", (W, H), PAGE)
    d = ImageDraw.Draw(page)
    fb = ImageFont.truetype(BOLD, 25)
    fr = ImageFont.truetype(REG, 18)

    for r, (v, title, blurb) in enumerate(VARIANTS):
        y = pad + r * (th + lab + gap)
        d.text((pad, y), title, font=fb, fill=INK)
        d.text((pad + d.textlength(title, font=fb) + 16, y + 5), blurb, font=fr, fill=SOFT)
        for c, colourway in enumerate(ORDER):
            im = tile(v, colourway).crop(crop_box).resize((tw, th), Image.LANCZOS)
            page.paste(im, (pad + c * (tw + gap), y + lab))

    p = os.path.join(SRC, name)
    page.save(p, quality=95)
    print(f"  {name:<26} {W}x{H}   {tag}")


if __name__ == "__main__":
    # the lockup sits centred; this box holds the rule, "collection" and the weight line
    sheet((140, 545, 940, 990), 0.46, "weightline-detail.jpg", "lockup, 1:1 then halved")
    sheet((0, 0, 1080, 1350), 0.34, "weightline-full.jpg", "whole tiles")


def thumb_test():
    """The real test. On a phone a profile-grid thumbnail is about 128px wide,
    at the 3:4 crop. If the weight line does not survive here it does not work,
    because the grid is where these tiles live."""
    tw = 128
    th = round(tw * 4 / 3)
    gap, lab, pad, scale = 3, 60, 46, 3          # scale is display only, so it is readable here
    W = pad * 2 + (tw * 3 + gap * 2) * scale
    H = pad * 2 + (th * scale + lab) * len(VARIANTS) + 30 * (len(VARIANTS) - 1)
    page = Image.new("RGB", (W, H), PAGE)
    d = ImageDraw.Draw(page)
    fb = ImageFont.truetype(BOLD, 25)
    fr = ImageFont.truetype(REG, 18)

    for r, (v, title, blurb) in enumerate(VARIANTS):
        y = pad + r * (th * scale + lab + 30)
        d.text((pad, y), title, font=fb, fill=INK)
        d.text((pad + d.textlength(title, font=fb) + 16, y + 5), blurb, font=fr, fill=SOFT)
        for c, colourway in enumerate(ORDER):
            im = tile(v, colourway)
            w = round(im.height * 3 / 4)
            im = im.crop(((im.width - w) // 2, 0, (im.width - w) // 2 + w, im.height))
            im = im.resize((tw, th), Image.LANCZOS)          # down to real thumbnail size
            im = im.resize((tw * scale, th * scale), Image.NEAREST)   # back up, no new detail
            page.paste(im, (pad + c * (tw + gap) * scale, y + lab))

    p = os.path.join(SRC, "weightline-thumbnail-test.jpg")
    page.save(p, quality=95)
    print(f"  {'weightline-thumbnail-test.jpg':<26} {W}x{H}   downsampled to a real 128px grid thumb")


thumb_test()
