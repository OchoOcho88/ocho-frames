#!/usr/bin/env python3
"""Skin a lifestyle fresh-explore photo into an Instagram 4:5 feed ad.

Crops the 2:3 source to 4:5 (1080x1350, IG feed), then lays type in the clean
upper wall space with a CTA footer. Tuned for bw2_r_v5 (model seated right, clean
upper-left wall). Brand-world headline (no product line since there's no band).

    python3 clients/sportif/scripts-local/ad_lifestyle.py bw2_r_v5_low
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
FDIR = ROOT / 'brand/fonts/glacial-indifference'
BOLD = str(FDIR / 'GlacialIndifference-Bold.otf')
REG  = str(FDIR / 'GlacialIndifference-Regular.otf')
FE = ROOT / 'clients/sportif/generated/images/fresh-explore'

NAVY = (24, 34, 50); CREAMW = (253, 246, 239); TERRA = (131, 56, 39)

def fit(draw, text, path, target_w):
    lo, hi = 10, 400
    while lo < hi:
        m = (lo + hi + 1) // 2
        if draw.textlength(text, font=ImageFont.truetype(path, m)) <= target_w: lo = m
        else: hi = m - 1
    return lo

def tracked(draw, y, text, font, fill, track, left=None, cx=None):
    ws = [draw.textlength(c, font=font) for c in text]
    tot = sum(ws) + track * (len(text) - 1)
    x = left if left is not None else (cx - tot / 2)
    for c, w in zip(text, ws):
        draw.text((x, y), c, font=font, fill=fill); x += w + track

def logo(draw, left, y, size, fill):
    T = 'SPORTIF'; f = ImageFont.truetype(REG, size); sp = size * -0.059
    ws = [draw.textlength(c, font=f) for c in T]; w = sum(ws) + sp * (len(T) - 1)
    b = draw.textbbox((0, 0), T, font=f); ch = b[3] - b[1]; x = left
    for c, cw in zip(T, ws): draw.text((x, y - b[1]), c, font=f, fill=fill); x += cw + sp
    rt = max(2, round(ch * 0.05)); rw = w * 0.42; ry = y + ch + ch * 0.42
    draw.rectangle([left, ry, left + rw, ry + rt], fill=fill)
    return w

def cta(img, cx, cy, text):
    d = ImageDraw.Draw(img); f = ImageFont.truetype(BOLD, 34); tk = 3
    ws = [d.textlength(c, font=f) for c in text]; tw = sum(ws) + tk * (len(text) - 1)
    bb = d.textbbox((0, 0), text, font=f); ch = bb[3] - bb[1]
    pw, ph = tw + 108, ch + 56; x0, y0 = cx - pw / 2, cy - ph / 2; r = ph / 2
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 8, x0 + pw, y0 + ph + 8], radius=r, fill=(30, 20, 14, 110))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(11)))
    d = ImageDraw.Draw(img); d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=r, fill=TERRA)
    x = cx - tw / 2; ty = cy - ch / 2 - bb[1]
    for c, w in zip(text, ws): d.text((x, ty), c, font=f, fill=CREAMW); x += w + tk

name = sys.argv[1] if len(sys.argv) > 1 else 'bw2_r_v5_low'
src = Image.open(FE / f'{name}.png').convert('RGB')
# crop 2:3 -> 4:5, top-aligned to keep the upper wall, then scale to IG feed 1080x1350
W0, H0 = src.size
crop_h = int(W0 / 0.8)              # 4:5
src = src.crop((0, 0, W0, crop_h)).resize((1080, 1350), Image.LANCZOS)
img = src.convert('RGBA'); W, H = img.size
d = ImageDraw.Draw(img)
LX = 74                             # left margin for type

# soft light halo behind the headline so navy stays crisp on the warm wall
halo = Image.new('RGBA', (W, H), (0, 0, 0, 0)); hd = ImageDraw.Draw(halo)

# brand logotype top-left
logo(d, LX, 70, 34, NAVY)

# headline: STRENGTH / IN STILLNESS (left-aligned navy)
hs = fit(d, 'IN STILLNESS', BOLD, W * 0.62); hf = ImageFont.truetype(BOLD, hs)
lh = sum(hf.getmetrics()) * 0.95; y0 = 168
for i, ln in enumerate(['STRENGTH', 'IN STILLNESS']):
    tracked(hd, y0 + i * lh, ln, hf, (255, 250, 244, 140), 0, left=LX)
img.alpha_composite(halo.filter(ImageFilter.GaussianBlur(10)))
d = ImageDraw.Draw(img)
for i, ln in enumerate(['STRENGTH', 'IN STILLNESS']):
    tracked(d, y0 + i * lh, ln, hf, NAVY, 0, left=LX)

# small supporting line under the headline
sf = ImageFont.truetype(REG, 30)
tracked(d, y0 + 2 * lh + 14, 'movement, made calm', sf, NAVY, 1, left=LX + 4)

# CTA pill + handle, bottom
cta(img, W / 2, H - 150, 'JOIN THE WAITLIST')
d = ImageDraw.Draw(img)
tracked(d, H - 66, '@sportifcollection', ImageFont.truetype(REG, 26), (250, 246, 240), 2, cx=W / 2)

out = FE / f'{name}_IGAD.png'
img.convert('RGB').save(out); print('ok ->', out, img.size)
