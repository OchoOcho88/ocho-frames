#!/usr/bin/env python3
"""feed-pilates variant: SPORTIF / collection set large and burned INTO the wall behind her.

The idea (Hugo, 2026-08-17): instead of a small mark sitting on top of the photo, set the
wordmark huge and tone-on-tone so it reads as part of the studio wall, and crucially it
passes BEHIND her, so her raised leg and arms occlude the type.

How the "behind" is done without a matting model: this plate's background is a perfectly
flat (230,224,217) and the histogram has a clean empty gap between the wall (~222+) and her
skin (~130). So a luminance threshold at 200, feathered, is a clean subject mask, no rembg
needed. The type is composited ONLY into the background region.

"Screen method" = we don't paste a colour, we shift the wall's own tone by a few percent,
which is what makes it read as a texture in the wall rather than a graphic on it.

    python3 clients/sportif/scripts-local/build_pilates_bg_wordmark.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / 'brand/fonts/glacial-indifference').is_dir():
            return p
    raise SystemExit('could not locate the hyperframes root')


ROOT = find_root(Path(__file__).resolve())
REG = str(ROOT / 'brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf')
SRC = ROOT / 'clients/sportif/reference-images/lucy-canva-picks/lucy-pilates-ref-noweights.png'
OUT = ROOT / 'clients/sportif/email-02-social/created/v2/pilates-bg-wordmark'
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1350
WORDMARK, SUBLINE = 'SPORTIF', 'collection'
TRACK_EM, SUB_TRACK_EM = -0.059, 0.06
RULE_OF_WORDMARK, RULE_OF_SUBLINE = 0.43, 0.75

WORDMARK_WIDTH = 0.86      # share of canvas width
# Sits high: SPORTIF crosses behind her raised leg (good, that's the depth cue), but the
# 'collection' line has to clear her thigh or the word gets eaten and stops reading.
MARK_TOP = 175
BG_THRESHOLD = 200         # luminance above this is wall, below is her
FEATHER = 1.6

# strength = how far the wall tone shifts. direction: 'deboss' darkens, 'emboss' lightens.
VARIANTS = {
    'deboss-soft':   dict(direction='deboss', strength=0.055),
    'deboss-medium': dict(direction='deboss', strength=0.100),
    'deboss-strong': dict(direction='deboss', strength=0.160),
    'emboss-soft':   dict(direction='emboss', strength=0.070),
}


def cover(im, tw, th):
    sw, sh = im.size
    s = max(tw / sw, th / sh)
    im = im.resize((round(sw * s), round(sh * s)), Image.LANCZOS)
    l, t = (im.width - tw) // 2, (im.height - th) // 2
    return im.crop((l, t, l + tw, t + th))


def tracked(d, text, font, track):
    ws = [d.textlength(c, font=font) for c in text]
    return ws, sum(ws) + track * (len(text) - 1)


def fit_font(d, text, track_em, target_w):
    """Largest font size whose tracked width fits target_w."""
    lo, hi = 8, 900
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = ImageFont.truetype(REG, mid)
        _, w = tracked(d, text, f, mid * track_em)
        if w <= target_w:
            lo = mid
        else:
            hi = mid - 1
    f = ImageFont.truetype(REG, lo)
    ws, w = tracked(d, text, f, lo * track_em)
    return f, ws, w


def build_type_layer():
    """White-on-black mask of the full SPORTIF / rule / collection lockup, set large."""
    layer = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(layer)

    wf, ws, w = fit_font(d, WORDMARK, TRACK_EM, W * WORDMARK_WIDTH)
    track = wf.size * TRACK_EM
    b = d.textbbox((0, 0), WORDMARK, font=wf)
    cap = b[3] - b[1]
    x = (W - w) / 2
    for c, cw in zip(WORDMARK, ws):
        d.text((x, MARK_TOP - b[1]), c, font=wf, fill=255)
        x += cw + track

    rw, rt, gap = w * RULE_OF_WORDMARK, max(2, round(cap * 0.045)), cap * 0.44
    ry = MARK_TOP + cap + gap
    d.rectangle([W / 2 - rw / 2, ry, W / 2 + rw / 2, ry + rt], fill=255)

    sf, sub_ws, sub_w = fit_font(d, SUBLINE, SUB_TRACK_EM, rw / RULE_OF_SUBLINE)
    sb = d.textbbox((0, 0), SUBLINE, font=sf)
    sx = (W - sub_w) / 2
    sy = ry + rt + cap * 0.42 - sb[1]
    for c, cw in zip(SUBLINE, sub_ws):
        d.text((sx, sy), c, font=sf, fill=255)
        sx += cw + sf.size * SUB_TRACK_EM
    return layer


def subject_mask(arr):
    """1.0 where the wall is, 0.0 where she is. Feathered so edges don't crawl."""
    lum = arr.mean(axis=2)
    bg = np.clip((lum - (BG_THRESHOLD - 14)) / 14.0, 0, 1)
    return np.asarray(
        Image.fromarray((bg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(FEATHER)),
        dtype=np.float32) / 255.0


def build(name, direction, strength):
    base = cover(Image.open(SRC).convert('RGB'), W, H)
    arr = np.asarray(base, dtype=np.float32)

    type_a = np.asarray(build_type_layer(), dtype=np.float32) / 255.0
    bg = subject_mask(arr)
    a = (type_a * bg * strength)[..., None]          # type, but only on the wall

    # shift the wall's OWN tone rather than pasting a colour, so it stays in the photo
    target = arr * (0.0 if direction == 'deboss' else 1.0)
    target = np.zeros_like(arr) if direction == 'deboss' else np.full_like(arr, 255.0)

    out = arr * (1 - a) + target * a
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(OUT / f'pilates-{name}.png')
    return name


if __name__ == '__main__':
    for name, cfg in VARIANTS.items():
        print('ok', build(name, **cfg))
    print('->', OUT)
