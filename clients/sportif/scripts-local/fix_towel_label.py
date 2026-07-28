#!/usr/bin/env python3
"""Fix the garbled woven label on the towel in the branded flat-lay test.

Patch-copy clean towel texture over the garble, then composite a small clean cream woven
SPORTIF label (our type) so the spelling is guaranteed.

    python3 clients/sportif/scripts-local/fix_towel_label.py
"""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
REG = str(ROOT / 'brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf')
TEST = ROOT / 'clients/sportif/email-03-band-photo/created/band-swap-test'
SRC = TEST / 'flatlay-branded_low.png'
OUT = TEST / 'flatlay-branded-fixed_low.png'

arr = np.array(Image.open(SRC).convert('RGB'))
# 1. patch-copy towel texture (same rows, from the left) over the garbled label
x0, y0, x1, y1 = 312, 646, 382, 688
w = x1 - x0
sx = x0 - w - 14
arr[y0:y1, x0:x1] = arr[y0:y1, sx:sx + w]

# 2. small clean cream woven SPORTIF label
img = Image.fromarray(arr).convert('RGBA')
LW, LH, s = 60, 26, 4
lab = Image.new('RGBA', (LW * s, LH * s), (0, 0, 0, 0))
d = ImageDraw.Draw(lab)
d.rounded_rectangle([0, 0, LW * s - 1, LH * s - 1], radius=int(LH * s * 0.22), fill=(226, 212, 189, 255))
d.rounded_rectangle([int(LW * s * 0.04), int(LH * s * 0.16), int(LW * s * 0.96), int(LH * s * 0.84)],
                    radius=int(LH * s * 0.12), outline=(198, 180, 152, 200), width=max(1, s))
fs = int(LH * s * 0.44)
f = ImageFont.truetype(REG, fs); tr = fs * -0.055
ws = [d.textlength(c, font=f) for c in 'SPORTIF']
tw = sum(ws) + tr * 6
x, y = (LW * s - tw) / 2, (LH * s - fs) / 2 - int(LH * s * 0.06)
for c, cw in zip('SPORTIF', ws):
    d.text((x, y), c, font=f, fill=(250, 246, 238, 255)); x += cw + tr
lab = lab.resize((LW, LH), Image.LANCZOS)

cx, cy = 347, 667
x0, y0 = cx - LW // 2, cy - LH // 2
sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 2, x0 + LW, y0 + LH + 2], radius=6, fill=(40, 30, 22, 80))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4)))
img.alpha_composite(lab, (x0, y0))

img.convert('RGB').save(OUT)
print('ok ->', OUT.relative_to(ROOT))
