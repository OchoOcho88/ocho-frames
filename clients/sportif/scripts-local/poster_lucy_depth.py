#!/usr/bin/env python3
"""JANNAYON-style DEPTH poster from Lucy's real photos: cut-out hero popping forward.

The hero (clean pilates plate, ankle weights removed) is matted out and layered in FRONT of
the collage grid and the headline, with a soft cast shadow for the 3D depth Hugo liked. All
imagery is Lucy's real photos; type is real Glacial.

    python3 clients/sportif/scripts-local/poster_lucy_depth.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
from rembg import remove, new_session

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
FDIR = ROOT / 'brand/fonts/glacial-indifference'
BOLD, REG = str(FDIR / 'GlacialIndifference-Bold.otf'), str(FDIR / 'GlacialIndifference-Regular.otf')
REF = ROOT / 'clients/sportif/reference-images/lucy-canva-picks'
OUT = ROOT / 'clients/sportif/generated/images/poster-experiment/poster-lucy-depth.png'

W, H = 1100, 1560
CREAM, CHAR, CARAMEL = (246, 238, 229), (58, 52, 47), (198, 146, 110)
canvas = Image.new('RGB', (W, H), CREAM)


def cover(path, tw, th, bw=False):
    im = Image.open(path).convert('RGB')
    if bw:
        im = ImageOps.grayscale(im).convert('RGB')
    sw, sh = im.size
    s = max(tw / sw, th / sh)
    im = im.resize((round(sw * s), round(sh * s)), Image.LANCZOS)
    l, t = (im.width - tw) // 2, (im.height - th) // 2
    return im.crop((l, t, l + tw, t + th))


# --- grid panels (behind the hero) ---
canvas.paste(cover(REF / 'lucy-studio-reformer-duo.png', 400, 540, bw=True), (700, 0))       # top-right B&W
canvas.paste(cover(REF / 'lucy-studio-reformer-sidestretch.png', 470, 462), (0, 978))         # bottom-left colour

d = ImageDraw.Draw(canvas)


def fit_width(text, fp, target_w, track_em=0.0):
    lo, hi = 20, 460
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = ImageFont.truetype(fp, mid)
        sp = mid * track_em
        w = sum(d.textlength(c, font=f) + sp for c in text) - sp
        if w <= target_w: lo = mid
        else: hi = mid - 1
    return lo


def tracked(xy, text, font, fill, track_px=0.0, cx=None):
    ws = [d.textlength(c, font=font) for c in text]
    total = sum(ws) + track_px * (len(text) - 1)
    x = (cx - total / 2) if cx is not None else xy[0]
    for c, w in zip(text, ws):
        d.text((x, xy[1]), c, font=font, fill=fill)
        x += w + track_px


# --- kicker + headline (behind hero) ---
kf = ImageFont.truetype(REG, 30)
tracked((64, 60), 'MEET SPORTIF', kf, CARAMEL, track_px=30 * 0.30)
hsize = fit_width('STRENGTH', BOLD, 620, -0.005)
hf = ImageFont.truetype(BOLD, hsize)
asc, desc = hf.getmetrics(); pitch = (asc + desc) * 0.9
hy = 360
for i, ln in enumerate(['STRENGTH', 'YOU CAN', 'WEAR']):
    tracked((60, hy + i * pitch), ln, hf, CHAR, track_px=hsize * -0.005)

# --- hero cutout (front) with soft cast shadow ---
sess = new_session('isnet-general-use')
base = Image.open(REF / 'lucy-pilates-ref-noweights.png').convert('RGB')
# paint out the second person's stray forearms (left of the ball) before matting
ImageDraw.Draw(base).rectangle((0, 1128, 418, 1350), fill=(230, 224, 217))
hero = remove(base.convert('RGBA'), session=sess,
              alpha_matting=True, alpha_matting_foreground_threshold=248,
              alpha_matting_background_threshold=12, alpha_matting_erode_size=6)
hero = hero.crop(hero.split()[3].getbbox())
th = 1200
hw = round(hero.width * th / hero.height)
hero = hero.resize((hw, th), Image.LANCZOS)
hx, hyy = (W - hw) // 2 + 20, H - th - 96

canvas = canvas.convert('RGBA')
# cast shadow: dark, blurred silhouette offset down-right
sh = Image.new('RGBA', (hw, th), (0, 0, 0, 0))
sh.putalpha(hero.split()[3].point(lambda a: int(a * 0.42)))
sh = Image.composite(Image.new('RGBA', (hw, th), (35, 26, 20, 255)), Image.new('RGBA', (hw, th), (0, 0, 0, 0)),
                     hero.split()[3].point(lambda a: int(a * 0.42)))
sh = sh.filter(ImageFilter.GaussianBlur(20))
canvas.alpha_composite(sh, (hx + 22, hyy + 30))
canvas.alpha_composite(hero, (hx, hyy))

# --- wordmark ---
d = ImageDraw.Draw(canvas)
wf = ImageFont.truetype(REG, 54)
wb = d.textbbox((0, 0), 'SPORTIF', font=wf)
tracked((0, H - 74 - (wb[3] + wb[1]) / 2 + 20), 'SPORTIF', wf, CHAR, track_px=54 * 0.44, cx=W / 2)

canvas.convert('RGB').save(OUT)
print('ok ->', OUT.relative_to(ROOT), (W, H))
