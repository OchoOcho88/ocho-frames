#!/usr/bin/env python3
"""JANNAYON-style collage poster built from Lucy's REAL Canva photos (no AI imagery).

Composites her three clean studio shots into a grid and lays real Glacial type on top:
  hero (top-right)  : ball-overhead back view
  bottom-left       : reformer side-stretch (colour)
  bottom-right      : reformer duo (B&W, the monochrome accent)
  headline (top-left, cream) : STRENGTH / YOU CAN / WEAR
  wordmark (bottom band)     : SPORTIF

    python3 clients/sportif/scripts-local/poster_lucy_real.py
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

# optional args: headline (pipe-separated lines) and output filename
HEADLINE = sys.argv[1].split('|') if len(sys.argv) > 1 else ['STRENGTH', 'YOU CAN', 'WEAR']
OUTNAME = sys.argv[2] if len(sys.argv) > 2 else 'poster-lucy-real.png'

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
FDIR = ROOT / 'brand/fonts/glacial-indifference'
BOLD = str(FDIR / 'GlacialIndifference-Bold.otf')
REG = str(FDIR / 'GlacialIndifference-Regular.otf')
REF = ROOT / 'clients/sportif/reference-images/lucy-canva-picks'
OUT = ROOT / 'clients/sportif/generated/images/poster-experiment' / OUTNAME

W, H = 1100, 1560
CREAM = (246, 238, 229)
CHAR = (74, 67, 60)          # warm charcoal #4A433C
CARAMEL = (198, 146, 110)    # #C6926E kicker accent

# grid geometry
xL = 442                     # headline column right edge / hero left edge
yA = 846                     # row A (hero) bottom
yB = 1446                    # row B (bottom photos) bottom
xMidL, xMidR = 543, 557      # bottom split with a 14px cream gutter
bandTop = 1460               # wordmark band top

canvas = Image.new('RGB', (W, H), CREAM)


def cover(path, tw, th, bw=False):
    im = Image.open(path).convert('RGB')
    if bw:
        im = ImageOps.grayscale(im).convert('RGB')
    sw, sh = im.size
    s = max(tw / sw, th / sh)
    im = im.resize((round(sw * s), round(sh * s)), Image.LANCZOS)
    nw, nh = im.size
    l, t = (nw - tw) // 2, (nh - th) // 2
    return im.crop((l, t, l + tw, t + th))


# --- photos
canvas.paste(cover(REF / 'lucy-studio-ball-overhead-back.png', W - xL, yA), (xL, 0))          # hero
canvas.paste(cover(REF / 'lucy-studio-reformer-sidestretch.png', xMidL, yB - 860), (0, 860))  # bottom-left
canvas.paste(cover(REF / 'lucy-studio-reformer-duo.png', W - xMidR, yB - 860, bw=True), (xMidR, 860))  # bottom-right B&W

d = ImageDraw.Draw(canvas)


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


# --- headline block (top-left, on cream), vertically centred in the panel ---
LEFT, TRACK_EM = 42, -0.005
lines = HEADLINE
hsize = min(fit_width(ln, BOLD, xL - LEFT - 34, TRACK_EM) for ln in lines)  # widest line fits
hf = ImageFont.truetype(BOLD, hsize)
asc, desc = hf.getmetrics()
pitch = (asc + desc) * 0.9
block_h = pitch * (len(lines) - 1) + hsize * 0.72
top = (yA - block_h) / 2 + 18            # centre the block in the hero-row height
# kicker just above the headline
kf = ImageFont.truetype(REG, 30)
draw_tracked((LEFT + 3, top - 58), 'MEET SPORTIF', kf, CARAMEL, track_px=30 * 0.28)
for i, ln in enumerate(lines):
    draw_tracked((LEFT, top + i * pitch), ln, hf, CHAR, track_px=hsize * TRACK_EM)

# --- wordmark (bottom band) ---
wf = ImageFont.truetype(REG, 52)
wb = d.textbbox((0, 0), 'SPORTIF', font=wf)
wy = (bandTop + H) / 2 - (wb[3] + wb[1]) / 2
draw_tracked((0, wy), 'SPORTIF', wf, CHAR, track_px=52 * 0.44, center_x=W / 2)

canvas.save(OUT)
print('ok ->', OUT.relative_to(ROOT), canvas.size)
