#!/usr/bin/env python3
"""The rest of the email-02 set with the logo in Pantone 162 C (Q-026 answered, S046).

Lucy, 23 Sep, on the room-in-peach thread: "I would like this photo just in peach for now,
The other pictures changed to the logo peach colour please." So the ball photo keeps the room
in peach (built, `created/v5-162c/`), and the other three photos (duo, side stretch, pilates)
get the master mark in 162 C, the `peach` treatment she saw on the ball photo in email 1
(`build_ballreach_peachmark.py`). Placements are v3's (her own marks where she made them),
the photos are untouched (no house grade), handle off (Instagram, D-018).

The peach is light and these studio walls are pale, so the fill's contrast against the wall
under each mark is measured and printed, next to black for reference.

Output: email-02-social/created/v6-peachmark-set/<treatment>/{feed,story}-<photo>.png (pilates
in peach-deep, the rest in peach)
plus SHEET-peachmark-set.jpg (every file small, and each mark at 100 percent).

    python3 clients/sportif/scripts-local/build_email02_peachmark_set.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_email02_social_v3 as v3  # noqa: E402

PEACH = (0xFF, 0xBE, 0x9F)
PHOTOS = ['duo', 'sidestretch', 'pilates']
OUT = v3.ROOT / 'clients/sportif/email-02-social/created/v6-peachmark-set'
v3.OUT = OUT
v3.DRAW_HANDLE = False
s = v3._s
v3.TREATMENTS.clear()
v3.TREATMENTS['peach'] = dict(fill=PEACH, stroke=None, sw=0, blur=s(13), sa=0.85, dy=s(4))
# the pilates wall is the palest in the set (#E6E0D9, peach 1.22:1): the same look with a
# heavier, tighter shadow (the ball-photo test's `peach-deep`) so SPORTIF reads. A hairline
# charcoal edge reads best of all but turns the mark into outlined sticker type (S046).
v3.TREATMENTS['peach-deep'] = dict(fill=PEACH, stroke=None, sw=0, blur=s(9), sa=1.0, dy=s(4))
TREATMENT_FOR = {'pilates': 'peach-deep'}


def rel_lum(rgb):
    c = np.array(rgb, np.float64) / 255
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return float(c @ [0.2126, 0.7152, 0.0722])


def contrast(a, b):
    la, lb = rel_lum(a), rel_lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def main():
    font = ImageFont.truetype(v3.REG, 28)
    tiles = []
    for name in PHOTOS:
        src = Image.open(v3.REF / v3.SOURCES[name]).convert('RGB')
        for fmt, size in v3.FORMATS.items():
            treat = TREATMENT_FOR.get(name, 'peach')
            top, how, _, _ = v3.build(src, fmt, size, treat, name)
            d0 = ImageDraw.Draw(Image.new('RGB', (10, 10)))
            m = v3.lockup_metrics(d0)
            box = v3.MANUAL_PLACEMENT.get((fmt, name))
            x_left = round(box[0] + ((box[2] - box[0]) - m['w']) / 2) if box else v3.MARGIN_X
            clean = np.asarray(v3.cover(src, *size))
            wall = clean[int(top):int(top + m['block_h']), int(x_left):int(x_left + m['w'])].reshape(-1, 3).mean(0)
            print(f'{fmt:5s} {name:11s} mark at x={x_left} y={top} [{how}]  wall #%02X%02X%02X  '
                  f'peach {contrast(PEACH, wall):.2f}:1  black {contrast((17, 17, 17), wall):.2f}:1'
                  % tuple(int(round(v)) for v in wall))
            out = Image.open(OUT / treat / f'{fmt}-{name}.png')
            crop = out.crop((int(max(0, x_left - 40)), int(max(0, top - 40)),
                             int(min(size[0], x_left + m['w'] + 40)), int(min(size[1], top + m['block_h'] + 40))))
            small = out.resize((300, round(300 * size[1] / size[0])), Image.LANCZOS)
            t = Image.new('RGB', (360, 560 + 40 + crop.height), (255, 255, 255))
            t.paste(small, (0, 40)); t.paste(crop.resize((360, round(crop.height * 360 / crop.width))), (0, 600))
            ImageDraw.Draw(t).text((6, 4), f'{fmt} {name} ({treat})', font=font, fill=(17, 17, 17))
            tiles.append(t)
    h = max(t.height for t in tiles)
    sheet = Image.new('RGB', (372 * len(tiles), h), (255, 255, 255))
    for i, t in enumerate(tiles):
        sheet.paste(t, (i * 372, 0))
    sheet.save(OUT / 'SHEET-peachmark-set.jpg', quality=90)
    print('sheet', (OUT / 'SHEET-peachmark-set.jpg').relative_to(v3.ROOT))


if __name__ == '__main__':
    main()
