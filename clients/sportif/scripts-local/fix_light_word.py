#!/usr/bin/env python3
"""Fix the one garbled size word ('UGIOI') on the LIGHT band of the gpt-stamped draped shot.

The gpt stamp got SPORTIF (and MEDIUM/HEAVY) right; only the LIGHT band's size word garbled.
Cover just that word with the tab cream and draw a clean 'LIGHT'. Keeps the natural gpt tabs.

    python3 clients/sportif/scripts-local/fix_light_word.py
"""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
REG = str(ROOT / 'brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf')
CREATED = ROOT / 'clients/sportif/email-03-band-photo/created'
SRC = CREATED / 'draped-arm_low-sportif_low.png'
OUT = CREATED / 'draped-arm-labeled.png'

im = Image.open(SRC).convert('RGB')
arr = np.array(im)
# robustly sample the tab CREAM = the brightest pixels inside the tab bounding box
box = arr[905:950, 445:535].reshape(-1, 3)
lum = box.mean(axis=1)
cream = tuple(int(c) for c in box[lum >= np.percentile(lum, 78)].mean(axis=0))
d = ImageDraw.Draw(im)
# cover the garbled word
d.rectangle([463, 934, 522, 951], fill=cream)
# draw a clean LIGHT, centred on the word slot
f = ImageFont.truetype(REG, 12)
txt, track = 'LIGHT', 1.6
ws = [d.textlength(c, font=f) for c in txt]
tw = sum(ws) + track * (len(txt) - 1)
x, y = 492 - tw / 2, 935
for c, cw in zip(txt, ws):
    d.text((x, y), c, font=f, fill=(250, 247, 240)); x += cw + track

im.save(OUT)
print('ok ->', OUT.relative_to(ROOT), 'cream', cream)
