#!/usr/bin/env python3
"""Lay Sportif type on a no-text plate (our workflow: we own the typography).

Copy set "Find your resistance":
  kicker   : meet sportif           (navy, top of tan block)
  headline : FIND YOUR / RESISTANCE (cream, big, tan block)
  watermark: SPORTIF                (faint oversized, lower area)
  curved   : Join the waitlist      (navy italic arc)
  logo     : SPORTIF + underline    (small footer lockup)

All in Glacial Indifference. Run with system python (has PIL).
    python3 clients/sportif/scripts-local/layout_reskin.py asis
    python3 clients/sportif/scripts-local/layout_reskin.py bridge
    python3 clients/sportif/scripts-local/layout_reskin.py all
"""
import math, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
FDIR = ROOT / 'brand/fonts/glacial-indifference'
BOLD = str(FDIR / 'GlacialIndifference-Bold.otf')
REG  = str(FDIR / 'GlacialIndifference-Regular.otf')
ITAL = str(FDIR / 'GlacialIndifference-Italic.otf')
INDIR = ROOT / 'clients/sportif/generated/images/reference-reskin'
PROD  = ROOT / 'clients/sportif/generated/images/product-bands'

NAVY   = (19, 37, 61)
CREAM  = (244, 238, 229)
WM     = (150, 122, 98)   # watermark tint (darker than cream floor so it reads faint)
TERRA  = (131, 56, 39)    # #833827 terracotta clay (brand CTA colour)
CREAMW = (253, 246, 239)  # near-white cream for CTA text

def fit_size(draw, text, font_path, target_w, track_em=0.0):
    lo, hi = 10, 640
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = ImageFont.truetype(font_path, mid)
        sp = mid * track_em
        w = sum(draw.textlength(c, font=f) + sp for c in text) - sp
        if w <= target_w: lo = mid
        else: hi = mid - 1
    return lo

def tracked(draw, xy, text, font, fill, track_px=0.0, anchor_center=None):
    """draw text with letter spacing; if anchor_center given (cx), center it."""
    widths = [draw.textlength(c, font=font) for c in text]
    total = sum(widths) + track_px * (len(text) - 1)
    x = (anchor_center - total / 2) if anchor_center is not None else xy[0]
    y = xy[1]
    for c, w in zip(text, widths):
        draw.text((x, y), c, font=font, fill=fill)
        x += w + track_px
    return total

def draw_arc(base, text, font, fill, cx, cy, radius, span_deg):
    """draw text along an upward (smile) arc centred on vertical."""
    d = ImageDraw.Draw(base)
    widths = [d.textlength(c, font=font) for c in text]
    total_w = sum(widths)
    if total_w == 0: return
    ang_per_px = span_deg / total_w
    a = -span_deg / 2
    asc = font.getmetrics()[0]
    for c, w in zip(text, widths):
        ca = a + ang_per_px * (w / 2)
        rad = math.radians(ca)
        # char tile
        cw = max(1, int(w) + 4); chh = int(font.size * 1.6)
        tile = Image.new('RGBA', (cw, chh), (0, 0, 0, 0))
        ImageDraw.Draw(tile).text((cw / 2 - w / 2, 0), c, font=font, fill=fill + (255,))
        tile = tile.rotate(-ca, expand=True, resample=Image.BICUBIC)
        # position: point on circle below centre (smile), text baseline tangent
        x = cx + radius * math.sin(rad)
        y = cy - radius * math.cos(rad) + radius  # bottom arc
        base.alpha_composite(tile, (int(x - tile.width / 2), int(y - tile.height / 2)))
        a += ang_per_px * w

def cta_pill(img, cx, cy, text):
    """solid terracotta rounded CTA button with letter-spaced cream text + soft shadow."""
    f = ImageFont.truetype(BOLD, 33)
    track = 3
    d0 = ImageDraw.Draw(img)
    widths = [d0.textlength(c, font=f) for c in text]
    tw = sum(widths) + track * (len(text) - 1)
    bb = d0.textbbox((0, 0), text, font=f); ch = bb[3] - bb[1]
    padx, pady = 52, 27
    pw, ph = tw + padx * 2, ch + pady * 2
    x0, y0 = cx - pw / 2, cy - ph / 2
    r = ph / 2
    # soft lift shadow
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 8, x0 + pw, y0 + ph + 8],
                                         radius=r, fill=(30, 20, 14, 120))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(11)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=r, fill=TERRA)
    x = cx - tw / 2; ty = cy - ch / 2 - bb[1]
    for c, w in zip(text, widths):
        d.text((x, ty), c, font=f, fill=CREAMW)
        x += w + track

def logo_lockup(draw, cx, y_top, size, fill):
    """small SPORTIF wordmark + underline rule, centred at cx."""
    TEXT = 'SPORTIF'; TRACK = -0.059
    f = ImageFont.truetype(REG, size)
    sp = size * TRACK
    widths = [draw.textlength(c, font=f) for c in TEXT]
    w = sum(widths) + sp * (len(TEXT) - 1)
    b = draw.textbbox((0, 0), TEXT, font=f); ch = b[3] - b[1]
    x = cx - w / 2
    for c, cw in zip(TEXT, widths):
        draw.text((x, y_top - b[1]), c, font=f, fill=fill)
        x += cw + sp
    rt = max(2, round(ch * 0.045)); gap = ch * 0.44; rw = w * 0.43
    ry = y_top + ch + gap
    draw.rectangle([cx - rw / 2, ry, cx + rw / 2, ry + rt], fill=fill)

def place_band_card(img, path, cx, cy, target_h):
    """drop a single-band product card as a rounded, shadowed, cream-bordered inset."""
    card = Image.open(path).convert('RGB')
    cw, ch = card.size
    crop = card.crop((int(cw * 0.22), int(ch * 0.15), int(cw * 0.79), int(ch * 0.88)))
    cw2, ch2 = crop.size
    tw = int(target_h * cw2 / ch2)
    crop = crop.resize((tw, target_h), Image.LANCZOS)
    rad = int(min(tw, target_h) * 0.055)
    mask = Image.new('L', (tw, target_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, tw - 1, target_h - 1], radius=rad, fill=255)
    x0, y0 = int(cx - tw / 2), int(cy - target_h / 2)
    # soft drop shadow
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 12, x0 + tw, y0 + target_h + 12],
                                         radius=rad, fill=(42, 30, 22, 105))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(20)))
    # card
    rgba = crop.convert('RGBA'); rgba.putalpha(mask)
    img.alpha_composite(rgba, (x0, y0))
    # thin cream border
    ImageDraw.Draw(img).rounded_rectangle([x0, y0, x0 + tw, y0 + target_h],
                                          radius=rad, outline=CREAMW + (235,), width=4)

def build(plate):
    src = INDIR / f'plate-{plate}_low.png'
    img = Image.open(src).convert('RGBA')
    W, H = img.size
    d = ImageDraw.Draw(img)
    cx = W / 2

    # --- watermark SPORTIF (faint oversized, lower area) ---
    wl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wl)
    wsize = fit_size(wd, 'SPORTIF', BOLD, W * 1.02, track_em=0.02)
    wf = ImageFont.truetype(BOLD, wsize)
    for i, yy in enumerate((H * 0.60, H * 0.72)):
        tracked(wd, (0, yy), 'SPORTIF', wf, WM + (255,), track_px=wsize * 0.02, anchor_center=cx)
    wl.putalpha(wl.split()[3].point(lambda a: int(a * 0.12)))
    img.alpha_composite(wl)
    d = ImageDraw.Draw(img)

    # --- kicker: small 'meet' lead-in over a larger SPORTIF logotype (Glacial Regular) ---
    mf = ImageFont.truetype(REG, 34)
    sf = ImageFont.truetype(REG, 60)
    tracked(d, (0, H * 0.024), 'meet', mf, NAVY, track_px=34 * 0.08, anchor_center=cx)
    tracked(d, (0, H * 0.068), 'SPORTIF', sf, NAVY, track_px=60 * -0.059, anchor_center=cx)

    # --- headline: FIND YOUR / RESISTANCE (cream, soft shadow for contrast) ---
    hsize = fit_size(d, 'RESISTANCE', BOLD, W * 0.84, track_em=0.0)
    hf = ImageFont.truetype(BOLD, hsize)
    asc, desc = hf.getmetrics(); lh = (asc + desc) * 0.92
    y0 = H * 0.123
    lines = ['FIND YOUR', 'RESISTANCE']
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); shd = ImageDraw.Draw(sh)
    for i, ln in enumerate(lines):
        tracked(shd, (0, y0 + i * lh), ln, hf, (18, 26, 40, 130), anchor_center=cx)
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)), (0, 6))
    d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        tracked(d, (0, y0 + i * lh), ln, hf, CREAM, anchor_center=cx)

    # --- single-band product card in the left void (bridge only has the room) ---
    if plate == 'bridge':
        place_band_card(img, PROD / 'bands-card-medium.png', W * 0.255, H * 0.495, int(H * 0.27))

    # --- CTA pill + footer logo lockup + IG handle (bottom stack) ---
    cta_pill(img, cx, H * 0.885, 'JOIN THE WAITLIST')
    d = ImageDraw.Draw(img)
    logo_lockup(d, cx, H * 0.935, 32, NAVY)
    hf2 = ImageFont.truetype(REG, 27)
    tracked(d, (0, H * 0.972), '@sportifcollection', hf2, NAVY, track_px=2, anchor_center=cx)

    out = INDIR / f'reskin-{plate}.png'
    img.convert('RGB').save(out)
    print(f'ok -> {out}')

which = sys.argv[1] if len(sys.argv) > 1 else 'all'
for p in (['asis', 'bridge'] if which == 'all' else [which]):
    build(p)
