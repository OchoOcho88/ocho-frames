#!/usr/bin/env python3
"""Layered depth poster: legs-in-air (background) -> SPORTIF wordmark (middle) -> ball hero (front).

z-order gives the 3D sandwich Hugo asked for: the big SPORTIF wordmark sits BETWEEN the faded
legs-in-air background and the cut-out ball hero in front (the hero covers the middle letters).

Hero cutout path can be passed as arg (default = the rough placeholder). Drop Hugo's clean
Photoshop cutout in as hero-ball-cut.png and re-run.

    python3 clients/sportif/scripts-local/poster_lucy_layered.py [hero_png]
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageDraw as D
from rembg import remove, new_session

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
FDIR = ROOT / 'brand/fonts/glacial-indifference'
BOLD, REG = str(FDIR / 'GlacialIndifference-Bold.otf'), str(FDIR / 'GlacialIndifference-Regular.otf')
REF = ROOT / 'clients/sportif/reference-images/lucy-canva-picks'
EXP = ROOT / 'clients/sportif/generated/images/poster-experiment'
HERO = Path(sys.argv[1]) if len(sys.argv) > 1 else EXP / 'hero-ball-cut.png'
OUT = EXP / 'poster-lucy-layered.png'

W, H = 1100, 1560
CREAM, CHAR, CARAMEL = (246, 238, 229), (58, 52, 47), (198, 146, 110)
canvas = Image.new('RGBA', (W, H), CREAM + (255,))

# --- background layer: legs-in-air (pilates), matted + faded so it sits back ---
sess = new_session('isnet-general-use')
base = Image.open(REF / 'lucy-pilates-ref-noweights.png').convert('RGB')
ImageDraw.Draw(base).rectangle((0, 1128, 418, 1350), fill=(230, 224, 217))  # drop stray arms
legs = remove(base.convert('RGBA'), session=sess, alpha_matting=True,
              alpha_matting_foreground_threshold=248, alpha_matting_background_threshold=12)
legs = legs.crop(legs.split()[3].getbbox())
lh = 1150
lw = round(legs.width * lh / legs.height)
legs = legs.resize((lw, lh), Image.LANCZOS)
legs.putalpha(legs.split()[3].point(lambda a: int(a * 0.55)))   # fade the backdrop
canvas.alpha_composite(legs, (W - lw + 60, H - lh + 40))         # anchored bottom-right

# --- middle layer: big SPORTIF wordmark ---
d = ImageDraw.Draw(canvas)


def fit(text, fp, tw, track_em):
    lo, hi = 20, 520
    while lo < hi:
        m = (lo + hi + 1) // 2
        f = ImageFont.truetype(fp, m)
        sp = m * track_em
        w = sum(d.textlength(c, font=f) + sp for c in text) - sp
        if w <= tw: lo = m
        else: hi = m - 1
    return lo


def tracked(y, text, font, fill, track_px, cx):
    ws = [d.textlength(c, font=font) for c in text]
    total = sum(ws) + track_px * (len(text) - 1)
    x = cx - total / 2
    for c, w in zip(text, ws):
        d.text((x, y), c, font=font, fill=fill)
        x += w + track_px


sp_size = fit('SPORTIF', BOLD, W * 0.98, 0.02)
spf = ImageFont.truetype(BOLD, sp_size)
sb = d.textbbox((0, 0), 'SPORTIF', font=spf)
tracked(H * 0.46 - (sb[3] + sb[1]) / 2, 'SPORTIF', spf, CHAR, sp_size * 0.02, W / 2)

# small kicker top-left
kf = ImageFont.truetype(REG, 30)
d.text((60, 60), 'MEET SPORTIF', font=kf, fill=CARAMEL)

# --- front layer: ball hero cutout ---
hero = Image.open(HERO).convert('RGBA')
hero = hero.crop(hero.split()[3].getbbox())
th = 1300
tw = round(hero.width * th / hero.height)
hero = hero.resize((tw, th), Image.LANCZOS)
canvas.alpha_composite(hero, ((W - tw) // 2, H - th - 40))

canvas.convert('RGB').save(OUT)
print('ok ->', OUT.relative_to(ROOT), 'hero:', HERO.name)
