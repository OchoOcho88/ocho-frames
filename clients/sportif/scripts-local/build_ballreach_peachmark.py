#!/usr/bin/env python3
"""The ball photo as it is, with the master mark in Pantone 162 C (Q-026).

Lucy, 18 Sep: "try with the branded logo peach colour". 21 Sep: "use this picture here
with the peach pantone colour", attaching 1-as-it-is.png. Hugo's reading (S044): the
photo untouched, the LOGO in the brand peach. This script is build_email02_social_v3
with peach treatments added; placement is Lucy's own top-right box for the ball photo.

The wall under the mark is pale and warm, so 162 C on it is low contrast by nature.
Each treatment is a different way of making the peach read: shadow weight, a thin
charcoal edge, or both. Contrast of the fill against the wall under the mark is
measured and printed so the choice is made on numbers as well as by eye.

    python3 clients/sportif/scripts-local/build_ballreach_peachmark.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_email02_social_v3 as v3  # noqa: E402

PEACH = (0xFF, 0xBE, 0x9F)
CHARCOAL = (0x4A, 0x43, 0x3C)                                # brand.md primary type colour
OUT = v3.ROOT / 'clients/sportif/email-02-social/created/v5-peachmark'
v3.OUT = OUT
v3.DRAW_HANDLE = False                                       # Instagram, handle off (D-018)

s = v3._s
v3.TREATMENTS.clear()
v3.TREATMENTS.update({
    # the white recipe's shadow, which is what makes light type survive a light wall
    'peach':          dict(fill=PEACH, stroke=None,     sw=0,    blur=s(13), sa=0.85, dy=s(4)),
    # heavier, tighter shadow: more of a lift off the wall
    'peach-deep':     dict(fill=PEACH, stroke=None,     sw=0,    blur=s(9),  sa=1.0,  dy=s(4)),
    # a hairline of the brand charcoal around the letters, light shadow
    'peach-edge':     dict(fill=PEACH, stroke=CHARCOAL, sw=s(1), blur=s(8),  sa=0.45, dy=s(3)),
    # the black concept's shadow only, no extra help: the honest baseline
    'peach-bare':     dict(fill=PEACH, stroke=None,     sw=0,    blur=s(7),  sa=0.34, dy=s(3)),
})


def rel_lum(rgb):
    c = np.array(rgb, np.float64) / 255
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return float(c @ [0.2126, 0.7152, 0.0722])


def contrast(a, b):
    la, lb = rel_lum(a), rel_lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


if __name__ == '__main__':
    src = Image.open(v3.REF / v3.SOURCES['ballreach']).convert('RGB')
    box = v3.MANUAL_PLACEMENT[('feed', 'ballreach')]
    wall = np.asarray(v3.cover(src, 1080, 1350))[box[1]:box[3], box[0]:box[2]].reshape(-1, 3).mean(0)
    wall_hex = '#%02X%02X%02X' % tuple(int(round(v)) for v in wall)
    print(f'wall under the mark {wall_hex}: peach {contrast(PEACH, wall):.2f}:1, '
          f'black {contrast((17, 17, 17), wall):.2f}:1, white {contrast((255, 255, 255), wall):.2f}:1')
    tiles = []
    font = ImageFont.truetype(v3.REG, 30)
    for treat in v3.TREATMENTS:
        for fmt, size in v3.FORMATS.items():
            top, how, _, _ = v3.build(src, fmt, size, treat, 'ballreach')
            print(f'ok {treat:12s} {fmt}-ballreach mark y={top} [{how}]')
        feed = Image.open(OUT / treat / 'feed-ballreach.png')
        crop = feed.crop((700, 180, 1060, 380))                     # the mark at 100 percent
        small = feed.resize((360, 450), Image.LANCZOS)
        t = Image.new('RGB', (360, 450 + 200 + 40), (255, 255, 255))
        t.paste(small, (0, 40)); t.paste(crop, (0, 490))
        ImageDraw.Draw(t).text((8, 4), treat, font=font, fill=(17, 17, 17))
        tiles.append(t)
    sheet = Image.new('RGB', (372 * len(tiles), 690), (255, 255, 255))
    for i, t in enumerate(tiles):
        sheet.paste(t, (i * 372, 0))
    sheet.save(OUT / 'SHEET-peachmark.jpg', quality=90)
    print('sheet', OUT / 'SHEET-peachmark.jpg')
