#!/usr/bin/env python3
"""SPORTIF weave tiles: V1 Bold lockup, scaled up proportionally.

Settled 2026-08-31 (Hugo):
  - colour stays the REAL product (D-027). Not the brand palette.
  - the weight line is Glacial Indifference BOLD (V1), same footprint as before.
  - the whole lockup goes UP, because type reads smaller on Instagram.

Everything in the lockup keys off SPORTIF's width, so one number scales the
whole block: WORD_W_FRAC, SPORTIF's tracked width as a share of canvas width.
The blurs and the shadow offset scale with it too, otherwise the halo gets
proportionally thinner as the type grows.

The ceiling is the Instagram profile grid crop. Instagram crops grid thumbs to
3:4, so a 1080 x 1350 post shows a centred 1012px column. Anything wider than
that is trimmed on the grid. Each scale below reports its own margin.

Re-runs clean, no arguments.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_texture_weight_tiles as base

ROOT = base.ROOT
FONTS = os.path.join(ROOT, "brand/fonts/glacial-indifference")
REG = os.path.join(FONTS, "GlacialIndifference-Regular.otf")
BOLD = os.path.join(FONTS, "GlacialIndifference-Bold.otf")
OUT = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles/scale-options")

W, H = base.W, base.H
CREAM = base.CREAM
MEASURED = base.MEASURED
BASE_FRAC = base.WORD_W_FRAC          # 0.66, what Lucy has now
SAFE_W = H * 3 / 4                    # 1012px, the 3:4 grid column

WEIGHT_FONT = BOLD                    # V1
WEIGHT_OF_SUB = base.WEIGHT_OF_SUB    # 0.92, V1 keeps the original footprint
WEIGHT_TRACK_EM = base.WEIGHT_TRACK_EM
WEIGHT_HALO = 45                      # V1's extra halo under the weight line

SCALES = [("S0-current-066", 0.66),
          ("S1-076", 0.76),
          ("S2-084", 0.84)]


def fit(d, text, target_w, track_em, path, lo=8, hi=700):
    while lo < hi:
        m = (lo + hi + 1) // 2
        f = ImageFont.truetype(path, m)
        _, w = base.tracked_width(d, text, f, m * track_em)
        if w <= target_w:
            lo = m
        else:
            hi = m - 1
    return ImageFont.truetype(path, lo)


def build(colourway, weight_label, word_frac):
    k = word_frac / BASE_FRAC          # everything absolute scales by this

    bg = base.cover_crop(os.path.join(base.TEX, f"texture-{colourway}-plate.jpg"), W, H)
    bg = base.tone_match(bg, MEASURED[colourway])

    type_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    weight_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(type_layer)
    dw = ImageDraw.Draw(weight_layer)
    cx = W / 2

    wf = fit(d, base.WORDMARK, W * word_frac, base.TRACK_EM, REG)
    wtrack = wf.size * base.TRACK_EM
    wb = d.textbbox((0, 0), base.WORDMARK, font=wf)
    cap = wb[3] - wb[1]
    _, word_w = base.tracked_width(d, base.WORDMARK, wf, wtrack)

    rule_t = max(2, round(cap * 0.045))
    gap_above_rule = cap * 0.44
    rule_w = word_w * base.RULE_OF_WORDMARK

    sf = None
    for s in range(8, 400):
        f = ImageFont.truetype(REG, s)
        _, cw = base.tracked_width(d, base.SUBLINE, f, s * base.SUB_TRACK_EM)
        if cw >= rule_w / base.RULE_OF_SUBLINE:
            sf = f
            break
    stro = sf.size * base.SUB_TRACK_EM
    _, sub_w = base.tracked_width(d, base.SUBLINE, sf, stro)
    sb = d.textbbox((0, 0), base.SUBLINE, font=sf)
    sub_h = sb[3] - sb[1]

    gf = fit(dw, base.WEIGHT_SIZING_REF, sub_w * WEIGHT_OF_SUB, WEIGHT_TRACK_EM, WEIGHT_FONT)
    gtrack = gf.size * WEIGHT_TRACK_EM
    gb = dw.textbbox((0, 0), weight_label, font=gf)
    weight_h = gb[3] - gb[1]
    gap_above_weight = cap * 0.52

    block_h = (cap + gap_above_rule + rule_t + cap * 0.42 + sub_h
               + gap_above_weight + weight_h)
    top = (H - block_h) / 2 - H * base.NUDGE_UP

    base.draw_centred(d, base.WORDMARK, wf, wtrack, cx, top - wb[1], CREAM)
    ry = top + cap + gap_above_rule
    d.rectangle([cx - rule_w / 2, ry, cx + rule_w / 2, ry + rule_t], fill=CREAM)
    sy = ry + rule_t + cap * 0.42
    base.draw_centred(d, base.SUBLINE, sf, stro, cx, sy - sb[1], CREAM)
    gy = sy + sub_h + gap_above_weight
    base.draw_centred(dw, weight_label, gf, gtrack, cx, gy - gb[1], CREAM)

    both = Image.alpha_composite(type_layer, weight_layer)
    out = bg.convert("RGBA")

    for blur, alpha, off in (
            (base.SHADOW_BLUR * k, base.SHADOW_ALPHA,
             (round(base.SHADOW_OFFSET[0] * k), round(base.SHADOW_OFFSET[1] * k))),
            (base.CORE_BLUR * k, base.CORE_ALPHA, (round(2 * k), round(4 * k)))):
        a = both.split()[3].filter(ImageFilter.GaussianBlur(blur))
        a = a.point(lambda v: int(v * alpha / 255))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        lay.paste(Image.new("RGBA", (W, H), base.SHADOW_TINT + (255,)), off, a)
        out.alpha_composite(lay)

    a = weight_layer.split()[3].filter(ImageFilter.GaussianBlur(10 * k))
    a = a.point(lambda v: int(v * WEIGHT_HALO / 255))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lay.paste(Image.new("RGBA", (W, H), base.SHADOW_TINT + (255,)), (0, 0), a)
    out.alpha_composite(lay)

    out.alpha_composite(both)
    return out.convert("RGB"), word_w, block_h, wf.size, gf.size


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, frac in SCALES:
        d = os.path.join(OUT, name)
        os.makedirs(d, exist_ok=True)
        shown = False
        for colourway, label in base.WEIGHTS:
            img, word_w, block_h, wpt, gpt = build(colourway, label, frac)
            img.save(os.path.join(d, f"sportif-weave-{colourway}-{name}.png"))
            if not shown:
                margin = (SAFE_W - word_w) / 2
                print(f"  {name:<16} SPORTIF {word_w:.0f}px ({frac:.2f} of canvas), "
                      f"{wpt}pt   weight line {gpt}pt   block height {block_h:.0f}px "
                      f"({block_h / H * 100:.0f}% of canvas)")
                print(f"  {'':<16} grid-crop margin each side {margin:.0f}px"
                      f"   {'SAFE' if margin > 30 else 'TIGHT' if margin > 0 else 'CLIPPED'}")
                shown = True


if __name__ == "__main__":
    print(f"V1 Bold lockup at three scales. 3:4 grid column is {SAFE_W:.0f}px.\n")
    main()
    print(f"\nDone. Output: {OUT}")
