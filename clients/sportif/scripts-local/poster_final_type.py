#!/usr/bin/env python3
"""Make the JANNAYON-style poster pixel-perfect: lift gpt's baked-in type, lay real Glacial.

Works on Hugo's high-res ChatGPT poster at NATIVE resolution (no resampling of the photos).
Surgically removes the charcoal headline and the SPORTIF wordmark by masking the dark text
pixels over their beige panels and reconstructing the beige, then sets real Glacial type:
  headline : STRENGTH / YOU CAN / WEAR   (Bold, warm charcoal, left panel)
  wordmark : SPORTIF                       (tracked caps, centred bottom band)

    python3 clients/sportif/scripts-local/poster_final_type.py
"""
import cv2
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
FDIR = ROOT / 'brand/fonts/glacial-indifference'
BOLD = str(FDIR / 'GlacialIndifference-Bold.otf')
REG = str(FDIR / 'GlacialIndifference-Regular.otf')
EXP = ROOT / 'clients/sportif/generated/images/poster-experiment'
SRC = EXP / 'ChatGPT Image Jul 25, 2026, 11_09_16 AM.png'
OUT = EXP / 'poster-jannayon-final.png'

im = Image.open(SRC).convert('RGB')
arr = np.array(im)
Hh, Ww = arr.shape[:2]

# ---- sample the exact charcoal gpt used (median of dark text pixels in the headline panel)
def sample_charcoal(x0, y0, x1, y1, lum_thresh=150):
    sub = arr[y0:y1, x0:x1].astype(np.int16)
    mask = sub.mean(axis=2) < lum_thresh
    return tuple(int(c) for c in (sub[mask].mean(axis=0) if mask.any() else [70, 64, 58]))

CHAR = sample_charcoal(16, 24, 405, 610)
print('sampled headline charcoal:', CHAR)

# ---- inpaint the old baked-in type out of its beige panels (blends from surroundings, no box)
# Mask = dark text pixels inside each text zone only, so the photos are never touched.
mask = np.zeros((Hh, Ww), np.uint8)
for (x0, y0, x1, y1) in [(4, 6, 432, 285),        # headline line 1 (extend right to catch the bar)
                          (4, 285, 410, 642),       # headline lines 2-3 (stop short of the band)
                          (150, 1358, 905, 1476)]:  # wordmark band (below the lower photos)
    lum = arr[y0:y1, x0:x1].mean(axis=2)
    mask[y0:y1, x0:x1][lum < 150] = 255
mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)), iterations=1)
arr = cv2.inpaint(arr, mask, 6, cv2.INPAINT_TELEA)

# ---- lay real Glacial type
img = Image.fromarray(arr).convert('RGB')
d = ImageDraw.Draw(img)


def fit_width(text, font_path, target_w, track_em=0.0):
    lo, hi = 20, 400
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = ImageFont.truetype(font_path, mid)
        sp = mid * track_em
        w = sum(d.textlength(c, font=f) + sp for c in text) - sp
        if w <= target_w: lo = mid
        else: hi = mid - 1
    return lo


def draw_tracked(xy, text, font, fill, track_px=0.0, center_x=None):
    ws = [d.textlength(c, font=font) for c in text]
    total = sum(ws) + track_px * (len(text) - 1)
    x = (center_x - total / 2) if center_x is not None else xy[0]
    for c, w in zip(text, ws):
        d.text((x, xy[1]), c, font=font, fill=fill)
        x += w + track_px

# Headline: STRENGTH sets the size (widest line), fit to panel width; tight leading like the ref.
LEFT = 20
TRACK_EM = -0.005
hsize = fit_width('STRENGTH', BOLD, 392, TRACK_EM)
hf = ImageFont.truetype(BOLD, hsize)
asc, desc = hf.getmetrics()
pitch = (asc + desc) * 0.92
top = 20
for i, ln in enumerate(['STRENGTH', 'YOU CAN', 'WEAR']):
    draw_tracked((LEFT, top + i * pitch), ln, hf, CHAR, track_px=hsize * TRACK_EM)

# Wordmark: SPORTIF, widely tracked caps, centred on the bottom band (match the ref's spacing).
wsize = 46
wf = ImageFont.truetype(REG, wsize)
# vertically centre in the scrubbed band y=1378..1452
wb = d.textbbox((0, 0), 'SPORTIF', font=wf)
wy = (1378 + 1452) / 2 - (wb[3] + wb[1]) / 2
draw_tracked((0, wy), 'SPORTIF', wf, CHAR, track_px=wsize * 0.42, center_x=Ww / 2)

img.save(OUT)
print('ok ->', OUT.relative_to(ROOT))
