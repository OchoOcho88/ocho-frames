#!/usr/bin/env python3
"""SPORTIF weave tiles, three colour directions for Lucy to choose between.

Lucy (2026-08-28) asked to see the weave grid tiles "in my brand colour".
The tiles as built carry the REAL product colourways (D-027), which was the
whole pitch of the concept: nothing invented. Pushing them to a single brand
colour collapses the light-to-heavy read across the row, so this builds the
trade-off rather than deciding it.

  A  as-shot      the D-027 measured product colours (what she already has)
  B  brand-tinted 50% toward the brand ramp, three weights still distinct
  C  brand-full   the brand ramp at full strength

Brand ramp runs Blush Peach #F0CDB3 (primary, her "Light Orange") to
Terracotta #833827 (rich accent), with a measured midpoint for MEDIUM.

Type colour flips by plate luminance: cream on dark plates, Warm Charcoal
#4A433C on light ones, with the halo flipping with it. S035 measured that
black beats white on terracotta 6.8:1 against 2.1:1.

Re-runs clean, no arguments.
"""

import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_texture_weight_tiles as base

ROOT = base.ROOT
TEX = base.TEX
OUT = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles/brand-colour-options")

W, H = base.W, base.H
CREAM = base.CREAM
CHARCOAL = (0x4A, 0x43, 0x3C)          # brand primary type colour
HALO_DARK = base.SHADOW_TINT           # warm dark, under cream type
HALO_LIGHT = (255, 248, 240)           # warm light, under charcoal type

BLUSH_PEACH = (0xF0, 0xCD, 0xB3)
TERRACOTTA = (0x83, 0x38, 0x27)
RAMP_MID = tuple(round((a + b) / 2) for a, b in zip(BLUSH_PEACH, TERRACOTTA))

MEASURED = base.MEASURED               # D-027, the real product
BRAND_RAMP = {"light": BLUSH_PEACH, "medium": RAMP_MID, "heavy": TERRACOTTA}

TINT_MIX = 0.50                        # how far set B travels toward the ramp
LUMA_FLIP = 145                        # plate luma above this gets charcoal type


def mix(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(a, b))


SETS = {
    # Set A reproduces the files Lucy already has, so the ink is forced to cream
    # rather than chosen. B and C pick the ink by measured contrast.
    "A-as-shot": ({c: MEASURED[c] for c in MEASURED}, CREAM),
    "B-brand-tinted": ({c: mix(MEASURED[c], BRAND_RAMP[c], TINT_MIX) for c in MEASURED}, None),
    "C-brand-full": (dict(BRAND_RAMP), None),
}


def luma(rgb):
    r, g, b = rgb
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def rel_lum(rgb):
    def ch(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg, bg):
    a, b = sorted((rel_lum(fg), rel_lum(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def type_region_mean(im):
    """Mean colour of the plate behind the lockup, which is what the type has
    to survive. Measured, not assumed from the tone-match target."""
    c = im.crop((int(W * 0.20), int(H * 0.30), int(W * 0.80), int(H * 0.62)))
    px = list(c.resize((60, 40), Image.LANCZOS).get_flattened_data())
    n = len(px)
    return tuple(round(sum(q[i] for q in px) / n) for i in range(3))


def build(colourway, weight_label, target, force_ink=None):
    """Same geometry as the house build, with the colour target and the type
    colour driven by the plate instead of hard-coded."""
    bg = base.cover_crop(os.path.join(TEX, f"texture-{colourway}-plate.jpg"), W, H)
    bg = base.tone_match(bg, target)

    behind = type_region_mean(bg)
    if force_ink is not None:
        ink = force_ink
    else:
        ink = max((CREAM, CHARCOAL), key=lambda k: contrast(k, behind))
    halo = HALO_LIGHT if ink == CHARCOAL else HALO_DARK

    type_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(type_layer)
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
        f = ImageFont.truetype(base.REG, s)
        _, cw = base.tracked_width(d, base.SUBLINE, f, s * base.SUB_TRACK_EM)
        if cw >= rule_w / base.RULE_OF_SUBLINE:
            sf = f
            break
    stro = sf.size * base.SUB_TRACK_EM
    _, sub_w = base.tracked_width(d, base.SUBLINE, sf, stro)
    sb = d.textbbox((0, 0), base.SUBLINE, font=sf)
    sub_h = sb[3] - sb[1]

    gf = base.fit_to_width(d, base.WEIGHT_SIZING_REF, sub_w * base.WEIGHT_OF_SUB,
                           base.WEIGHT_TRACK_EM)
    gtrack = gf.size * base.WEIGHT_TRACK_EM
    gb = d.textbbox((0, 0), weight_label, font=gf)
    weight_h = gb[3] - gb[1]
    gap_above_weight = cap * 0.52

    block_h = (cap + gap_above_rule + rule_t + cap * 0.42 + sub_h
               + gap_above_weight + weight_h)
    top = (H - block_h) / 2 - H * base.NUDGE_UP

    base.draw_centred(d, base.WORDMARK, wf, wtrack, cx, top - wb[1], ink)
    ry = top + cap + gap_above_rule
    d.rectangle([cx - rule_w / 2, ry, cx + rule_w / 2, ry + rule_t], fill=ink)
    sy = ry + rule_t + cap * 0.42
    base.draw_centred(d, base.SUBLINE, sf, stro, cx, sy - sb[1], ink)
    gy = sy + sub_h + gap_above_weight
    base.draw_centred(d, weight_label, gf, gtrack, cx, gy - gb[1], ink)

    a = type_layer.split()[3].filter(ImageFilter.GaussianBlur(base.SHADOW_BLUR))
    a = a.point(lambda v: int(v * base.SHADOW_ALPHA / 255))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow.paste(Image.new("RGBA", (W, H), halo + (255,)), base.SHADOW_OFFSET, a)

    ca = type_layer.split()[3].filter(ImageFilter.GaussianBlur(base.CORE_BLUR))
    ca = ca.point(lambda v: int(v * base.CORE_ALPHA / 255))
    core = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    core.paste(Image.new("RGBA", (W, H), halo + (255,)), (2, 4), ca)

    out = bg.convert("RGBA")
    out.alpha_composite(shadow)
    out.alpha_composite(core)
    out.alpha_composite(type_layer)
    return out.convert("RGB"), ink, behind


def main():
    os.makedirs(OUT, exist_ok=True)
    report = []
    for set_name, (targets, force_ink) in SETS.items():
        d = os.path.join(OUT, set_name)
        os.makedirs(d, exist_ok=True)
        for colourway, label in base.WEIGHTS:
            img, ink, behind = build(colourway, label, targets[colourway], force_ink)
            img.save(os.path.join(d, f"sportif-weave-{colourway}-{set_name}.png"))
            cr = contrast(ink, behind)
            report.append((set_name, label, targets[colourway], behind, ink, round(cr, 2)))
            print(f"  {set_name:<15} {label:<7} target #{'%02X%02X%02X' % targets[colourway]}"
                  f"  behind-type #{'%02X%02X%02X' % behind}"
                  f"  ink {'CHARCOAL' if ink == CHARCOAL else 'CREAM  '}"
                  f"  contrast {cr:.2f}:1")
    return report


if __name__ == "__main__":
    print("Building three colour directions...")
    main()
    print(f"\nDone. Output: {OUT}")
