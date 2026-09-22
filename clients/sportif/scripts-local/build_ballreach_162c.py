#!/usr/bin/env python3
"""The ball photo with the room in Pantone 162 C (Q-026, Lucy's answer of 2026-09-21).

Lucy sent back `1-as-it-is.png` (the ball reach, feed crop) and asked for it "with the
peach pantone colour". That is concept 2 from the 27 Aug email (the brand colour room)
rebuilt in 162 C, screen #FFBE9F (D-051), instead of the heavy band terracotta.

How it is built (the WEAVE-ROOM-RECIPE.md idea, in script):
  1. the untouched photo (the feed source IS 1080x1350, no crop)
  2. the room treated, one of several recipes below
  3. her, cut out, laid back on top untouched. The cutout is Hugo's refined Photoshop
     mask read out of feed-ballreach-split-texture-heavy-bg.psd with psd-tools and
     saved as photoshop/feed-ballreach-cutout.png (RGBA). She never gets graded.
  4. the master mark, black, in Lucy's own top-right box from build_email02_social_v3

Story: the story crop is the same frame scaled 1.4222 and cropped 228px each side, so
the same cutout is scaled and cropped with it.

    python3 clients/sportif/scripts-local/build_ballreach_162c.py --sheet     # compare recipes
    python3 clients/sportif/scripts-local/build_ballreach_162c.py multiply   # render feed + story
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_email02_social_v3 import (MANUAL_PLACEMENT, TREATMENTS, lockup_metrics,  # noqa: E402
                                     draw_lockup, cover, REG)

HERE = Path(__file__).resolve().parent
CLIENT = HERE.parent
SRC = CLIENT / 'reference-images/lucy-canva-picks/lucy-studio-ball-overhead-back.png'
CUT = CLIENT / 'email-02-social/photoshop/feed-ballreach-cutout.png'
OUT = CLIENT / 'email-02-social/created/v5-162c'

PEACH = np.array([0xFF, 0xBE, 0x9F], np.float32) / 255      # Pantone 162 C on screen
DEEP = np.array([0x4A, 0x2C, 0x22], np.float32) / 255       # sportif_grade.py's shadow end
WALL_PATCH = (900, 600, 1060, 800)                          # x0, y0, x1, y1: plain wall, right of her


def lum(a):
    return a[..., 0] * 0.2126 + a[..., 1] * 0.7152 + a[..., 2] * 0.0722


def overlay(b, s):
    return np.where(b < 0.5, 2 * b * s, 1 - 2 * (1 - b) * (1 - s))


def soft_light(b, s):
    d = np.where(b <= 0.25, ((16 * b - 12) * b + 4) * b, np.sqrt(b))
    return np.where(s <= 0.5, b - (1 - 2 * s) * b * (1 - b), b + (2 * s - 1) * (d - b))


def set_lum(rgb, target_l):
    """Photoshop's Color blend: keep the fill's hue and saturation, take the photo's
    luminance. Lum is moved by an offset, then clipped back into gamut."""
    c = rgb + (target_l - lum(rgb))[..., None]
    L = lum(c)[..., None]
    n, x = c.min(-1)[..., None], c.max(-1)[..., None]
    c = np.where(n < 0, L + (c - L) * L / np.maximum(L - n, 1e-6), c)
    c = np.where(x > 1, L + (c - L) * (1 - L) / np.maximum(x - L, 1e-6), c)
    return np.clip(c, 0, 1)


def s_curve(a, k):
    L = lum(a)[..., None]
    S = np.clip(L + k * (L - 0.5) * (1 - np.abs(L - 0.5) * 2) * 2, 1e-5, 1)
    return np.clip(a * (S / np.maximum(L, 1e-5)), 0, 1)


def lift_wall(a, p=95.0):
    """Levels: put the wall's bright end on white so a Multiply lands on the Pantone."""
    w = a[WALL_PATCH[1]:WALL_PATCH[3], WALL_PATCH[0]:WALL_PATCH[2]]
    white = np.percentile(lum(w), p)
    return np.clip(a / max(white, 1e-3), 0, 1)


# ---------------------------------------------------------------- the recipes
def r_overlay60(a):
    """The 27 Aug recipe with the fill swapped: Overlay at 60 percent."""
    return a * 0.4 + overlay(a, PEACH) * 0.6


def r_color(a):
    """Color blend at 100 percent: 162 C's hue and chroma on the photo's own tones."""
    return set_lum(np.broadcast_to(PEACH, a.shape).copy(), lum(a))


def r_multiply(a):
    """Wall lifted to white, then Multiply by 162 C: the brightest wall IS the Pantone,
    every shadow is the Pantone darkened. A light S for a little body."""
    return s_curve(lift_wall(a) * PEACH, 0.06)


def r_tonemap(a):
    """sportif_grade.py's ramp at full strength with MID moved to 162 C: shadows go
    heavy-band brown, the wall goes peach, brightness stays the photo's (D-042)."""
    l = lum(a)
    pivot = 0.62
    ll = l[..., None]
    lo = DEEP + (PEACH - DEEP) * np.clip(ll / pivot, 0, 1)
    hi = PEACH + (np.array([1, 0.98, 0.96], np.float32) - PEACH) * np.clip((ll - pivot) / (1 - pivot), 0, 1)
    t = np.where(ll < pivot, lo, hi)
    t = t * (l / np.maximum(lum(t), 1e-5))[..., None]
    return np.clip(t, 0, 1)


def r_multiply_flat(a):
    """As multiply, but the wall's own shading is flattened first (pulled 40 percent of
    the way to its mean), so the room reads as a painted 162 C wall, less like a photo."""
    b = lift_wall(a)
    L = lum(b)[..., None]
    wall_mean = float(np.percentile(lum(b[WALL_PATCH[1]:WALL_PATCH[3], WALL_PATCH[0]:WALL_PATCH[2]]), 50))
    flat = np.clip(b * ((L * 0.6 + wall_mean * 0.4) / np.maximum(L, 1e-5)), 0, 1)
    # only flatten the bright end (the wall); keep shadows and objects
    wgt = np.clip((L - 0.55) / 0.3, 0, 1)
    b = b * (1 - wgt) + flat * wgt
    return s_curve(b * PEACH, 0.05)


def _wall(a):
    return a[WALL_PATCH[1]:WALL_PATCH[3], WALL_PATCH[0]:WALL_PATCH[2]].reshape(-1, 3)


def shoulder(v, knee=0.82):
    """Soft clip above the knee so the lit top of the wall keeps its texture instead
    of pinning flat on the Pantone."""
    over = np.clip(v - knee, 0, None)
    return np.where(v > knee, knee + (1 - knee) * np.tanh(over / (1 - knee)), v)


def r_pantone(a, ref_pct=50.0):
    """Neutralise the wall (divide by its own per-channel reference, which also lifts
    it to white), soft-shoulder the bright end, then Multiply by 162 C. The wall's
    reference tone lands ON the Pantone and the room keeps its shading."""
    ref = np.percentile(_wall(a), ref_pct, axis=0)
    b = shoulder(a / np.maximum(ref, 1e-3))
    return np.clip(b * PEACH, 0, 1)


def r_pantone_lift(a):
    """As pantone, referenced to the wall's brighter end: a paler, airier room, the
    Pantone only where the wall is lit."""
    return r_pantone(a, ref_pct=85.0)


RECIPES = {
    'overlay60': r_overlay60,
    'color': r_color,
    'multiply': r_multiply,
    'pantone': r_pantone,
    'pantone-lift': r_pantone_lift,
    'tonemap': r_tonemap,
}


# ---------------------------------------------------------------- assembly
def room_and_her(recipe, fmt):
    """The treated room with her composited back on, at the format's size, no mark."""
    src = Image.open(SRC).convert('RGB')
    cut = Image.open(CUT).convert('RGBA')
    W, H = (1080, 1350) if fmt == 'feed' else (1080, 1920)
    a = np.asarray(src, np.float32) / 255
    room = Image.fromarray((np.clip(RECIPES[recipe](a), 0, 1) * 255 + 0.5).astype(np.uint8))
    room = cover(room, W, H).convert('RGBA')
    her = cover(cut, W, H)
    room.alpha_composite(her)
    return room


def add_mark(img, fmt, treat='black'):
    m = lockup_metrics(ImageDraw.Draw(img))
    bx0, by0, bx1, by1 = MANUAL_PLACEMENT[(fmt, 'ballreach')]
    x_left = round(bx0 + ((bx1 - bx0) - m['w']) / 2)
    top = round(by0 + ((by1 - by0) - m['block_h']) / 2)
    t = TREATMENTS[treat]
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    draw_lockup(layer, x_left, top, m, t['fill'] + (255,), None, 0)
    shadow = Image.new('RGBA', img.size, (28, 22, 18, 0))
    shadow.putalpha(layer.split()[3].filter(ImageFilter.GaussianBlur(t['blur'])).point(lambda v: int(v * t['sa'])))
    img.alpha_composite(shadow, (0, t['dy']))
    img.alpha_composite(layer)
    return img


def wall_hex(img):
    a = np.asarray(img.convert('RGB'))[WALL_PATCH[1]:WALL_PATCH[3], WALL_PATCH[0]:WALL_PATCH[2]]
    r, g, b = a.reshape(-1, 3).mean(0)
    return '#%02X%02X%02X' % (round(r), round(g), round(b))


def sheet():
    OUT.mkdir(parents=True, exist_ok=True)
    tiles, labels = [], []
    font = ImageFont.truetype(REG, 34)
    for name in RECIPES:
        img = add_mark(room_and_her(name, 'feed'), 'feed')
        img.convert('RGB').save(OUT / f'feed-ballreach-{name}.png')
        hx = wall_hex(img)
        labels.append(f'{name}  wall {hx}')
        t = img.convert('RGB').resize((540, 675), Image.LANCZOS)
        d = ImageDraw.Draw(t)
        d.rectangle([0, 0, 540, 52], fill=(255, 255, 255))
        d.text((14, 8), f'{name}   wall {hx}', font=font, fill=(17, 17, 17))
        d.rectangle([420, 560, 530, 670], fill=(0xFF, 0xBE, 0x9F))
        d.rectangle([420, 560, 530, 670], outline=(17, 17, 17), width=2)
        tiles.append(t)
    W = 540 * len(tiles) + 12 * (len(tiles) - 1)
    out = Image.new('RGB', (W, 675), (255, 255, 255))
    for i, t in enumerate(tiles):
        out.paste(t, (i * 552, 0))
    out.save(OUT / 'SHEET-162c-recipes.jpg', quality=90)
    print('\n'.join(labels))
    print('sheet', OUT / 'SHEET-162c-recipes.jpg')


def render(recipe, dest):
    dest.mkdir(parents=True, exist_ok=True)
    for fmt in ('feed', 'story'):
        img = add_mark(room_and_her(recipe, fmt), fmt)
        p = dest / f'{fmt}-ballreach-162c.png'
        img.convert('RGB').save(p)
        print('ok', p, 'wall', wall_hex(img) if fmt == 'feed' else '')


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args or args[0] == '--sheet':
        sheet()
    else:
        render(args[0], OUT / 'final')
