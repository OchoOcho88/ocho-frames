#!/usr/bin/env python3
"""Email 02 social batch: light-touch feed (4:5) + stories (9:16) from Lucy's cleaned photos.

Per Lucy ("just use these images for social to save time"): minimal branding only, a small
cream SPORTIF wordmark + @sportifcollection handle bottom-centre, with a whisper of gradient
so it stays legible on any photo. No headlines, no heavy templates.

Sources: reference-images/lucy-canva-picks/ (the 4 cleaned plates from email 1)
Output:  email-02-social/created/{feed,story}-{key}.png

    python3 clients/sportif/scripts-local/build_email02_social.py
"""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
FDIR = ROOT / 'brand/fonts/glacial-indifference'
REG = str(FDIR / 'GlacialIndifference-Regular.otf')
REF = ROOT / 'clients/sportif/reference-images/lucy-canva-picks'
OUT = ROOT / 'clients/sportif/email-02-social/created'
OUT.mkdir(parents=True, exist_ok=True)

CREAM = (246, 238, 229)
SOURCES = {
    'pilates':     'lucy-pilates-ref-noweights.png',
    'sidestretch': 'lucy-studio-reformer-sidestretch.png',
    'ballreach':   'lucy-studio-ball-overhead-back.png',
    'duo':         'lucy-studio-reformer-duo.png',
}
FORMATS = {'feed': (1080, 1350), 'story': (1080, 1920)}


def cover(im, tw, th):
    sw, sh = im.size
    s = max(tw / sw, th / sh)
    im = im.resize((round(sw * s), round(sh * s)), Image.LANCZOS)
    l, t = (im.width - tw) // 2, (im.height - th) // 2
    return im.crop((l, t, l + tw, t + th))


def tracked_right(d, y, text, font, fill, track_px, x_right):
    """draw letter-spaced text right-aligned so its right edge sits at x_right."""
    ws = [d.textlength(c, font=font) for c in text]
    total = sum(ws) + track_px * (len(text) - 1)
    x = x_right - total
    for c, w in zip(text, ws):
        d.text((x, y), c, font=font, fill=fill)
        x += w + track_px


def corner_scrim(W, H, max_a=150, toppx=440):
    """soft darkening concentrated in the TOP-RIGHT corner for wordmark legibility."""
    ys, xs = np.mgrid[0:H, 0:W]
    xr = np.clip((xs - 0.46 * W) / (0.54 * W), 0, 1)
    yt = np.clip((toppx - ys) / toppx, 0, 1)
    a = (max_a * (xr ** 1.15) * (yt ** 1.15)).astype(np.uint8)
    scrim = np.zeros((H, W, 4), np.uint8)
    scrim[..., 0], scrim[..., 1], scrim[..., 2] = 35, 28, 22
    scrim[..., 3] = a
    return Image.fromarray(scrim, 'RGBA')


def brand(img, fmt):
    """Real Sportif logo lockup (Glacial Regular, tracking -0.059em, + underline rule),
    right-aligned in the top-right, with the @handle below."""
    W, H = img.size
    img = img.convert('RGBA')
    img.alpha_composite(corner_scrim(W, H))
    d = ImageDraw.Draw(img)
    x_right = W - 96                                    # more inset from the corner
    top = 150 if fmt == 'story' else 104
    S, TR = 54, -0.059                                 # matches the canonical logo lockup, larger
    wf = ImageFont.truetype(REG, S)
    track = S * TR
    b = d.textbbox((0, 0), 'SPORTIF', font=wf)
    cap = b[3] - b[1]
    ws = [d.textlength(c, font=wf) for c in 'SPORTIF']
    w = sum(ws) + track * (len('SPORTIF') - 1)
    cx = x_right - w / 2                                # wordmark centre (underline + handle centre here)
    # wordmark: soft shadow then cream
    tracked_right(d, top - b[1] + 1, 'SPORTIF', wf, (25, 18, 14, 120), track, x_right + 1)
    tracked_right(d, top - b[1], 'SPORTIF', wf, CREAM + (255,), track, x_right)
    # underline rule (0.43 x wordmark width, centred under it)
    rt = max(2, round(cap * 0.045)); gap = cap * 0.44; rw = w * 0.43
    ry = top + cap + gap
    d.rectangle([cx - rw / 2, ry, cx + rw / 2, ry + rt], fill=CREAM + (255,))
    # handle: CENTRED under the wordmark
    hf = ImageFont.truetype(REG, 30)
    htrack = 30 * 0.05
    hws = [d.textlength(c, font=hf) for c in '@sportifcollection']
    htot = sum(hws) + htrack * (len('@sportifcollection') - 1)
    hx = cx - htot / 2
    hy = ry + rt + cap * 0.5
    for c, cw in zip('@sportifcollection', hws):
        d.text((hx, hy), c, font=hf, fill=(245, 238, 230, 240))
        hx += cw + htrack
    return img.convert('RGB')


for key, fname in SOURCES.items():
    src = Image.open(REF / fname).convert('RGB')
    for fmt, (W, H) in FORMATS.items():
        out = brand(cover(src, W, H), fmt)
        out.save(OUT / f'{fmt}-{key}.png')
        print(f'ok {fmt}-{key}.png ({W}x{H})')
