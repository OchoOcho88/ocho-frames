#!/usr/bin/env python3
"""SPORTIF weave tiles: weight-line treatments, on the REAL product colours.

Colour is settled (Hugo, 2026-08-31): the tiles keep the D-027 measured product
colours. Recolouring them to the brand palette would sell a colour the customer
does not receive, and colour is a real purchase driver on these bands. The
brand-colour experiments are parked in `../brand-colour-options/`.

Open problem this addresses: the LIGHT / MEDIUM / HEAVY line is too thin and
gets lost (Hugo, 2026-08-31). Three treatments, same geometry otherwise:

  V0  regular    what she has now: Regular, 0.92 of the subline, 0.30em tracking
  V1  bold       Bold at the same footprint
  V2  bold-wide  Bold, 1.06 of the subline, 0.26em tracking, larger on the page

The halo under the weight line is also strengthened on V1 and V2, because the
line sits lower on the plate where the weave is busiest.

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
OUT = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles/weight-line-options")

W, H = base.W, base.H
CREAM = base.CREAM
MEASURED = base.MEASURED           # D-027, the real product. Not negotiable.

# name, font, width as a share of "collection", tracking em, extra halo alpha
VARIANTS = [
    ("V0-regular",   REG,  0.92, 0.30, 0),
    ("V1-bold",      BOLD, 0.92, 0.30, 45),
    ("V2-bold-wide", BOLD, 1.06, 0.26, 45),
]


def rel_lum(rgb):
    def ch(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg, bg):
    a, b = sorted((rel_lum(fg), rel_lum(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def region_mean(im, box):
    c = im.crop(box)
    px = list(c.resize((60, 30), Image.LANCZOS).get_flattened_data())
    n = len(px)
    return tuple(round(sum(q[i] for q in px) / n) for i in range(3))


def fit_bold(d, text, target_w, track_em, font_path, lo=8, hi=600):
    while lo < hi:
        m = (lo + hi + 1) // 2
        f = ImageFont.truetype(font_path, m)
        _, w = base.tracked_width(d, text, f, m * track_em)
        if w <= target_w:
            lo = m
        else:
            hi = m - 1
    return ImageFont.truetype(font_path, lo)


def build(colourway, weight_label, variant):
    name, wfont_path, w_of_sub, w_track_em, extra_halo = variant

    bg = base.cover_crop(os.path.join(base.TEX, f"texture-{colourway}-plate.jpg"), W, H)
    bg = base.tone_match(bg, MEASURED[colourway])

    type_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    weight_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(type_layer)
    dw = ImageDraw.Draw(weight_layer)
    cx = W / 2

    wf = base.fit_to_width(d, base.WORDMARK, W * base.WORD_W_FRAC, base.TRACK_EM)
    wtrack = wf.size * base.TRACK_EM
    wb = d.textbbox((0, 0), base.WORDMARK, font=wf)
    cap = wb[3] - wb[1]
    _, word_w = base.tracked_width(d, base.WORDMARK, wf, wtrack)

    rule_t = max(2, round(cap * 0.045))
    gap_above_rule = cap * 0.44
    rule_w = word_w * base.RULE_OF_WORDMARK

    sf = None
    for s in range(8, 300):
        f = ImageFont.truetype(REG, s)
        _, cw = base.tracked_width(d, base.SUBLINE, f, s * base.SUB_TRACK_EM)
        if cw >= rule_w / base.RULE_OF_SUBLINE:
            sf = f
            break
    stro = sf.size * base.SUB_TRACK_EM
    _, sub_w = base.tracked_width(d, base.SUBLINE, sf, stro)
    sb = d.textbbox((0, 0), base.SUBLINE, font=sf)
    sub_h = sb[3] - sb[1]

    gf = fit_bold(dw, base.WEIGHT_SIZING_REF, sub_w * w_of_sub, w_track_em, wfont_path)
    gtrack = gf.size * w_track_em
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

    out = bg.convert("RGBA")

    # house two-pass warm shadow, over the whole lockup including the weight line
    both = Image.alpha_composite(type_layer, weight_layer)
    for blur, alpha, off in ((base.SHADOW_BLUR, base.SHADOW_ALPHA, base.SHADOW_OFFSET),
                             (base.CORE_BLUR, base.CORE_ALPHA, (2, 4))):
        a = both.split()[3].filter(ImageFilter.GaussianBlur(blur))
        a = a.point(lambda v: int(v * alpha / 255))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        lay.paste(Image.new("RGBA", (W, H), base.SHADOW_TINT + (255,)), off, a)
        out.alpha_composite(lay)

    # extra halo under the weight line only, where the weave is busiest
    if extra_halo:
        a = weight_layer.split()[3].filter(ImageFilter.GaussianBlur(10))
        a = a.point(lambda v: int(v * extra_halo / 255))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        lay.paste(Image.new("RGBA", (W, H), base.SHADOW_TINT + (255,)), (0, 0), a)
        out.alpha_composite(lay)

    out.alpha_composite(both)

    plate_behind_weight = region_mean(bg, (int(W * 0.25), int(gy) - 6,
                                           int(W * 0.75), int(gy + weight_h) + 6))
    return out.convert("RGB"), gf.size, contrast(CREAM, plate_behind_weight)


def main():
    os.makedirs(OUT, exist_ok=True)
    for variant in VARIANTS:
        d = os.path.join(OUT, variant[0])
        os.makedirs(d, exist_ok=True)
        for colourway, label in base.WEIGHTS:
            img, pt, cr = build(colourway, label, variant)
            img.save(os.path.join(d, f"sportif-weave-{colourway}-{variant[0]}.png"))
            print(f"  {variant[0]:<14} {label:<7} weight line {pt}pt"
                  f"  contrast behind it {cr:.2f}:1")


if __name__ == "__main__":
    print("Building weight-line treatments on the real product colours...")
    main()
    print(f"\nDone. Output: {OUT}")
