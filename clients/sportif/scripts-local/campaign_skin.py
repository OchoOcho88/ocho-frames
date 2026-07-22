#!/usr/bin/env python3
"""Skin a full-bleed fresh-explore campaign photo with Sportif type (headline + logo + CTA + handle).

Unlike layout_reskin (tan-block poster), this lays type over an open area of a photographic
campaign shot. Tuned for ch2_r_low_realband (model left, clean warm wall upper-right).

    python3 clients/sportif/scripts-local/campaign_skin.py ch2_r_low_realband_low
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

def tracked(draw, y, text, font, fill, track, anchor, right=None, cx=None):
    ws = [draw.textlength(c, font=font) for c in text]
    tot = sum(ws) + track * (len(text) - 1)
    if right is not None: x = right - tot
    elif cx is not None: x = cx - tot / 2
    else: x = anchor
    for c, w in zip(text, ws):
        draw.text((x, y), c, font=font, fill=fill); x += w + track

def logo(draw, cx, y, size, fill):
    T = 'SPORTIF'; f = ImageFont.truetype(REG, size); sp = size * -0.059
    ws = [draw.textlength(c, font=f) for c in T]; w = sum(ws) + sp * (len(T) - 1)
    b = draw.textbbox((0, 0), T, font=f); ch = b[3] - b[1]; x = cx - w / 2
    for c, cw in zip(T, ws): draw.text((x, y - b[1]), c, font=f, fill=fill); x += cw + sp
    rt = max(2, round(ch * 0.045)); rw = w * 0.43; ry = y + ch + ch * 0.44
    draw.rectangle([cx - rw / 2, ry, cx + rw / 2, ry + rt], fill=fill)

def cta(img, cx, cy, text):
    d = ImageDraw.Draw(img); f = ImageFont.truetype(BOLD, 33); tk = 3
    ws = [d.textlength(c, font=f) for c in text]; tw = sum(ws) + tk * (len(text) - 1)
    bb = d.textbbox((0, 0), text, font=f); ch = bb[3] - bb[1]
    pw, ph = tw + 104, ch + 54; x0, y0 = cx - pw / 2, cy - ph / 2; r = ph / 2
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 8, x0 + pw, y0 + ph + 8], radius=r, fill=(30, 20, 14, 120))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(11)))
    d = ImageDraw.Draw(img); d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=r, fill=TERRA)
    x = cx - tw / 2; ty = cy - ch / 2 - bb[1]
    for c, w in zip(text, ws): d.text((x, ty), c, font=f, fill=CREAMW); x += w + tk

name = sys.argv[1] if len(sys.argv) > 1 else 'ch2_r_low_realband_low'
img = Image.open(FE / f'{name}.png').convert('RGBA'); W, H = img.size
d = ImageDraw.Draw(img); cx = W / 2

# headline: FIND YOUR / RESISTANCE, right-aligned in the clean upper-right wall (soft light halo)
hs = fit(d, 'RESISTANCE', BOLD, W * 0.46); hf = ImageFont.truetype(BOLD, hs)
lh = sum(hf.getmetrics()) * 0.94; y0 = H * 0.055; rx = W * 0.955
halo = Image.new('RGBA', (W, H), (0, 0, 0, 0)); hd = ImageDraw.Draw(halo)
for i, ln in enumerate(['FIND YOUR', 'RESISTANCE']):
    tracked(hd, y0 + i * lh, ln, hf, (255, 250, 244, 150), 0, None, right=rx)
img.alpha_composite(halo.filter(ImageFilter.GaussianBlur(9)))
d = ImageDraw.Draw(img)
for i, ln in enumerate(['FIND YOUR', 'RESISTANCE']):
    tracked(d, y0 + i * lh, ln, hf, NAVY, 0, None, right=rx)

# kicker 'meet sportif' small, above headline right
kf = ImageFont.truetype(REG, 30)
tracked(d, y0 - 42, 'meet sportif', kf, NAVY, 4, None, right=rx)

# CTA pill + handle bottom-centre
cta(img, cx, H * 0.9, 'JOIN THE WAITLIST')
d = ImageDraw.Draw(img)
tracked(d, H * 0.955, '@sportifcollection', ImageFont.truetype(REG, 25), (250, 246, 240), 2, None, cx=cx)

out = FE / f'{name}_AD.png'
img.convert('RGB').save(out); print('ok ->', out)
