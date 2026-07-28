#!/usr/bin/env python3
"""Put CORRECT SPORTIF labels on the flat-lay bands, our way (PIL type, not gpt text).

gpt garbles brand text, so: inpaint the AI's blank portrait tabs back to knit, then composite
a clean PIL-rendered SPORTIF rubber label (Glacial Regular wordmark + underline + size) onto
each band. Guaranteed-correct spelling at any resolution.

    python3 clients/sportif/scripts-local/label_flatlay_pil.py
"""
import cv2
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
REG = str(ROOT / 'brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf')
CREATED = ROOT / 'clients/sportif/email-03-band-photo/created'
SRC = CREATED / 'flatlay-concept_low.png'          # the clean blank-tab flat-lay
OUT = CREATED / 'flatlay-concept-labeled.png'

# each band: blank-tab rect (x0,y0,x1,y1), label centre, size word
BANDS = [
    ((756, 766, 824, 900), (790, 833), 'LIGHT'),
    ((756, 971, 824, 1105), (790, 1038), 'MEDIUM'),
    ((758, 1201, 828, 1340), (793, 1270), 'HEAVY'),
]
CREAMTAB = (232, 221, 199)
INK = (252, 249, 242)


def make_label(w, h, size_text, s=3):
    W, H = w * s, h * s
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(H * 0.17)
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=r, fill=CREAMTAB + (255,))
    d.rounded_rectangle([int(W * 0.045), int(H * 0.13), int(W * 0.955), int(H * 0.87)],
                        radius=int(r * 0.6), outline=(205, 188, 158, 190), width=max(1, s))
    # SPORTIF wordmark (tight tracking, our lockup)
    fs = int(H * 0.31)
    f = ImageFont.truetype(REG, fs); tr = fs * -0.059
    ws = [d.textlength(c, font=f) for c in 'SPORTIF']
    tw = sum(ws) + tr * 6
    x, y = (W - tw) / 2, int(H * 0.19)
    for c, cw in zip('SPORTIF', ws):
        d.text((x, y), c, font=f, fill=INK + (255,)); x += cw + tr
    # underline rule
    uw = tw * 0.52
    uy = int(H * 0.58)
    d.rectangle([(W - uw) / 2, uy, (W + uw) / 2, uy + max(2, int(s * 1.3))], fill=INK + (255,))
    # size word
    sf = int(H * 0.155)
    f2 = ImageFont.truetype(REG, sf); tr2 = sf * 0.16
    sws = [d.textlength(c, font=f2) for c in size_text]
    stw = sum(sws) + tr2 * (len(size_text) - 1)
    x, y = (W - stw) / 2, int(H * 0.66)
    for c, cw in zip(size_text, sws):
        d.text((x, y), c, font=f2, fill=INK + (235,)); x += cw + tr2
    return img.resize((w, h), Image.LANCZOS)


arr = np.array(Image.open(SRC).convert('RGB'))
# 1. patch-copy clean knit from the same band (same rows -> ribs align) over each blank tab
pad = 20
for (x0, y0, x1, y1), _, _ in BANDS:
    x0, y0, x1, y1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    w = x1 - x0
    sx = x0 - w - 24                       # source knit to the LEFT of the tab
    if sx < 0:
        sx = x1 + 24                       # fall back to the right if no room
    arr[y0:y1, x0:x1] = arr[y0:y1, sx:sx + w]

# 2. composite clean PIL labels
img = Image.fromarray(arr).convert('RGBA')
LW, LH = 168, 100
for _, (cx, cy), size in BANDS:
    lab = make_label(LW, LH, size)
    x0, y0 = int(cx - LW / 2), int(cy - LH / 2)
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 5, x0 + LW, y0 + LH + 5], radius=18,
                                         fill=(40, 30, 22, 90))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)))
    img.alpha_composite(lab, (x0, y0))

img.convert('RGB').save(OUT)
print('ok ->', OUT.relative_to(ROOT))
