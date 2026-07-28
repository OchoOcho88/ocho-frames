#!/usr/bin/env python3
"""Lay Sportif type on the CLEAN bridge plate (band not worn, shown as product placement).

Lucy email #1: hip-raise model, band as a product placement (not on the body) + the logo.
So the band appears only as the product card, and we carry the wordmark + waitlist CTA.
Reuses the helpers from layout_reskin.py; only the source plate, band-card size and output
name change.

    python3 clients/sportif/scripts-local/layout_reskin_clean.py
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
from layout_reskin import (  # noqa: E402  reuse the exact type helpers
    BOLD, REG, INDIR, PROD, NAVY, CREAM, WM,
    fit_size, tracked, cta_pill, logo_lockup, place_band_card,
)


def build():
    src = INDIR / 'plate-clean_low.png'
    img = Image.open(src).convert('RGBA')
    W, H = img.size
    d = ImageDraw.Draw(img)
    cx = W / 2

    # --- watermark SPORTIF (faint oversized, lower area) ---
    wl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wl)
    wsize = fit_size(wd, 'SPORTIF', BOLD, W * 1.02, track_em=0.02)
    wf = ImageFont.truetype(BOLD, wsize)
    for yy in (H * 0.60, H * 0.72):
        tracked(wd, (0, yy), 'SPORTIF', wf, WM + (255,), track_px=wsize * 0.02, anchor_center=cx)
    wl.putalpha(wl.split()[3].point(lambda a: int(a * 0.12)))
    img.alpha_composite(wl)
    d = ImageDraw.Draw(img)

    # --- kicker: 'meet' over SPORTIF logotype ---
    mf = ImageFont.truetype(REG, 34)
    sf = ImageFont.truetype(REG, 60)
    tracked(d, (0, H * 0.024), 'meet', mf, NAVY, track_px=34 * 0.08, anchor_center=cx)
    tracked(d, (0, H * 0.068), 'SPORTIF', sf, NAVY, track_px=60 * -0.059, anchor_center=cx)

    # --- headline: FIND YOUR / RESISTANCE ---
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

    # --- band product card in the left void (the ONLY band now, so a touch larger) ---
    place_band_card(img, PROD / 'bands-card-medium.png', W * 0.258, H * 0.492, int(H * 0.30))

    # --- CTA pill + footer logo lockup + IG handle ---
    cta_pill(img, cx, H * 0.885, 'JOIN THE WAITLIST')
    d = ImageDraw.Draw(img)
    logo_lockup(d, cx, H * 0.935, 32, NAVY)
    hf2 = ImageFont.truetype(REG, 27)
    tracked(d, (0, H * 0.972), '@sportifcollection', hf2, NAVY, track_px=2, anchor_center=cx)

    out = INDIR / 'reskin-clean.png'
    img.convert('RGB').save(out)
    print(f'ok -> {out}')


build()
