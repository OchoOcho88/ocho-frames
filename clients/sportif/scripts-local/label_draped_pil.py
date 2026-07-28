#!/usr/bin/env python3
"""Put CORRECT SPORTIF labels on the draped-arm bands (PIL type, not gpt text).

Same approach as the flat-lay: patch-copy knit over each blank tab (vertical shift keeps the
rib rows), then composite a clean PIL SPORTIF label rotated to each band's hang angle.

    python3 clients/sportif/scripts-local/label_draped_pil.py
"""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
REG = str(ROOT / 'brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf')
CREATED = ROOT / 'clients/sportif/email-03-band-photo/created'
SRC = CREATED / 'draped-arm_low.png'               # clean blank-tab draped shot
OUT = CREATED / 'draped-arm-labeled.png'

# band: blank-tab rect, centre, size word, band hang angle (deg, +=CCW)
BANDS = [
    ((432, 898, 522, 952), (477, 925), 'LIGHT', -3),
    ((573, 893, 662, 947), (617, 920), 'MEDIUM', 1),
    ((748, 852, 838, 906), (793, 879), 'HEAVY', -6),
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
    fs = int(H * 0.31)
    f = ImageFont.truetype(REG, fs); tr = fs * -0.059
    ws = [d.textlength(c, font=f) for c in 'SPORTIF']
    tw = sum(ws) + tr * 6
    x, y = (W - tw) / 2, int(H * 0.19)
    for c, cw in zip('SPORTIF', ws):
        d.text((x, y), c, font=f, fill=INK + (255,)); x += cw + tr
    uw = tw * 0.52; uy = int(H * 0.58)
    d.rectangle([(W - uw) / 2, uy, (W + uw) / 2, uy + max(2, int(s * 1.3))], fill=INK + (255,))
    sf = int(H * 0.155)
    f2 = ImageFont.truetype(REG, sf); tr2 = sf * 0.16
    sws = [d.textlength(c, font=f2) for c in size_text]
    stw = sum(sws) + tr2 * (len(size_text) - 1)
    x, y = (W - stw) / 2, int(H * 0.66)
    for c, cw in zip(size_text, sws):
        d.text((x, y), c, font=f2, fill=INK + (235,)); x += cw + tr2
    return img.resize((w, h), Image.LANCZOS)


arr = np.array(Image.open(SRC).convert('RGB'))
# patch-copy a GENEROUS knit region from BELOW each tab (same columns -> rib rows continue),
# big enough to fully erase the old blank tab before the label goes on
for _, (cx, cy), _, _ in BANDS:
    hw, hh = 74, 52
    x0, y0, x1, y1 = cx - hw, cy - hh, cx + hw, cy + hh
    sy = y1 + 26
    arr[y0:y1, x0:x1] = arr[sy:sy + (y1 - y0), x0:x1]

img = Image.fromarray(arr).convert('RGBA')
LW, LH = 118, 66
for _, (cx, cy), size, ang in BANDS:
    lab = make_label(LW, LH, size).rotate(ang, expand=True, resample=Image.BICUBIC)
    lw, lh = lab.size
    x0, y0 = int(cx - lw / 2), int(cy - lh / 2)
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ss = Image.new('RGBA', (lw, lh), (0, 0, 0, 0))
    ImageDraw.Draw(ss).rounded_rectangle([6, 8, lw - 6, lh - 4], radius=14, fill=(40, 30, 22, 95))
    sh.alpha_composite(ss, (x0, y0))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(7)))
    img.alpha_composite(lab, (x0, y0))

img.convert('RGB').save(OUT)
print('ok ->', OUT.relative_to(ROOT))
