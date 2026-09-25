"""Re-time the captions on the afternoon storyboard without regenerating the drawing (S047).

Hugo moved the meet from 1pm to 12:30 for breathing room. The keeper sheet (take b) stays as
drawn; only the eight time captions are painted out with the paper colour and set again in
Avenir Next Medium, sized and tracked to match the generator's lettering (cap height 13 px,
tracking fitted so "1:00 OPENER" comes out the width of the original, 112 px). Each new caption is
centred where the old one was.

Run: .venvs/pdf/bin/python clients/sportif/scripts-local/retime_afternoon_storyboard.py
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

SP = Path(__file__).resolve().parents[1]
SRC = SP / "generated/images/storyboard/7-storyboard-afternoon_medium-b.png"
OUT = SP / "generated/images/storyboard/7-storyboard-afternoon_medium-b-1230.png"
# Avenir Next Medium is the closest face to the generator's lettering (Glacial Regular read thin and
# wide, Glacial Bold heavy), trialled against the original caption in S047.
FONT, FONT_INDEX = "/System/Library/Fonts/Avenir Next.ttc", 5

INK = (70, 68, 65)  # a touch lighter than the measured ink, so Medium reads at the original weight
CAP_H = 13
# (top, bottom) of each caption row, and the new captions left then right
ROWS = [(426, 438), (795, 807), (1132, 1144), (1490, 1502)]
NEW = [("12:30 OPENER", "12:35 ERRANDS"),
       ("1:00 JUICE AND EMAILS", "1:30 GYM AND STUDIO"),
       ("1:50 EXERCISING", "2:10 CLIENTS ON THE FLOOR"),
       ("2:30 ROOFTOP POOL", "2:55 CLOSER")]
COLS = [(40, 505), (520, 990)]


def font_for_cap_height(h):
    for size in range(8, 40):
        f = ImageFont.truetype(FONT, size, index=FONT_INDEX)
        top, bottom = f.getbbox("H")[1], f.getbbox("H")[3]
        if bottom - top >= h:
            return f
    raise SystemExit("no size fits")


def text_width(f, s, track):
    return sum(f.getlength(c) for c in s) + track * (len(s) - 1)


def draw_tracked(d, f, x, y_cap_top, s, track):
    offset = f.getbbox("H")[1]
    for c in s:
        d.text((x, y_cap_top - offset), c, font=f, fill=INK)
        x += f.getlength(c) + track


def main():
    im = Image.open(SRC).convert("RGB")
    a = np.asarray(im).astype(float)
    g = a.mean(2)
    f = font_for_cap_height(CAP_H)
    # fit tracking on the first caption as drawn by the generator
    track = (112 - sum(f.getlength(c) for c in "1:00 OPENER")) / (len("1:00 OPENER") - 1)
    rng = np.random.default_rng(7)
    out = a.copy()
    boxes = []
    for (y0, y1), pair in zip(ROWS, NEW):
        for (x0, x1), new in zip(COLS, pair):
            cols = np.where((g[y0:y1 + 1, x0:x1] < 110).any(0))[0]
            xa, xb = x0 + cols.min(), x0 + cols.max()
            centre = (xa + xb) / 2
            # paper sampled from the strip just above and below the caption
            ring = np.concatenate([a[y0 - 12:y0 - 5, xa - 10:xb + 10].reshape(-1, 3),
                                   a[y1 + 5:y1 + 12, xa - 10:xb + 10].reshape(-1, 3)])
            clean = ring[ring.mean(1) > 225]  # paper only, no border ink or drawing
            mu, sd = np.median(clean, 0), min(clean.std(0).mean(), 2.5)
            h, w = (y1 + 4) - (y0 - 4), (xb + 6) - (xa - 6)
            out[y0 - 4:y1 + 4, xa - 6:xb + 6] = mu + rng.normal(0, 1, (h, w, 1)) * sd
            boxes.append((new, centre, y0))
    im2 = Image.fromarray(np.clip(out, 0, 255).astype("uint8"))
    d = ImageDraw.Draw(im2)
    for new, centre, y0 in boxes:
        wdt = text_width(f, new, track)
        draw_tracked(d, f, centre - wdt / 2, y0, new, track)
        print(f"{new:28s} centre {centre:.0f} width {wdt:.0f}")
    im2.save(OUT)
    print(OUT, "font size", f.size, "track", round(track, 2))


if __name__ == "__main__":
    main()
