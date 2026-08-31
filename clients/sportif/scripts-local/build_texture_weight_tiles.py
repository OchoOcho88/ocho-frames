#!/usr/bin/env python3
"""SPORTIF weave tiles: one 4:5 Instagram feed post per colourway.

Full-bleed crop of the band's own weave (the real single-crop texture plates,
no tiling and no mirror seam) under the canonical SPORTIF / rule / collection
lockup, with the band's WEIGHT set as a fourth line underneath.

Three posts, one per weight, sized to sit as a row in the Instagram grid.
Re-runs clean, no arguments.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
REG = os.path.join(ROOT, "brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf")
BOLD = os.path.join(ROOT, "brand/fonts/glacial-indifference/GlacialIndifference-Bold.otf")
TEX = os.path.join(ROOT, "clients/sportif/assets/textures")
OUT = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles")

W, H = 1080, 1350                 # Instagram 4:5 feed
CREAM = (246, 238, 229)

WORDMARK, SUBLINE = "SPORTIF", "collection"
TRACK_EM, SUB_TRACK_EM = -0.059, 0.06        # canonical lockup tracking (D-017)
RULE_OF_WORDMARK, RULE_OF_SUBLINE = 0.43, 0.75

# The whole lockup keys off this one number. Cap height, the rule, "collection",
# the weight line and every gap derive from it, so changing it scales the block
# and holds every proportion. Raised from 0.66 to 0.76 on 2026-08-31 (S1),
# because type reads smaller on Instagram than on a desktop screen. The ceiling
# is the 3:4 profile-grid crop, a centred 1012px column: 0.76 leaves 96px of
# margin each side. See generated/.../scale-options/README.md.
WORD_W_FRAC = 0.76                # SPORTIF tracked width as a share of canvas width
SCALE_K = WORD_W_FRAC / 0.66      # blurs and offsets scale with the type
WEIGHT_FONT = BOLD                # 2026-08-31: the weight line was too thin and got lost
WEIGHT_HALO = 45                  # extra halo under the weight line, where the weave is busiest
WEIGHT_TRACK_EM = 0.30            # wide tracking on the weight line
WEIGHT_OF_SUB = 0.92              # weight line width relative to "collection"
NUDGE_UP = 0.015
INSET = 0.02              # trim past the selvedge so no sheet survives the crop

SHADOW_TINT = (45, 24, 18)        # warm dark, never grey (house rule)
SHADOW_BLUR, SHADOW_OFFSET, SHADOW_ALPHA = 26, (6, 12), 135
CORE_BLUR, CORE_ALPHA = 7, 95        # tight second pass, lifts type off pale weave

# D-027 measured colourways, the source of truth. Each plate is tone-matched to
# its own value with a per-channel gamma, which preserves black and white so no
# highlight in the weave clips. Medium and heavy already sit on target, so their
# correction is near 1.0 and all three get the identical treatment.
MEASURED = {"light": (0xB8, 0xA0, 0x80),
            "medium": (0x9D, 0x74, 0x59),
            "heavy": (0x6C, 0x43, 0x33)}

WEIGHTS = [("light", "LIGHT"), ("medium", "MEDIUM"), ("heavy", "HEAVY")]
WEIGHT_SIZING_REF = "MEDIUM"      # longest label, so all three share one point size


def tracked_width(d, text, font, track):
    ws = [d.textlength(c, font=font) for c in text]
    return ws, sum(ws) + track * (len(text) - 1)


def fit_to_width(d, text, target_w, track_em, lo=8, hi=700, path=REG):
    while lo < hi:
        m = (lo + hi + 1) // 2
        f = ImageFont.truetype(path, m)
        _, w = tracked_width(d, text, f, m * track_em)
        if w <= target_w:
            lo = m
        else:
            hi = m - 1
    return ImageFont.truetype(path, lo)


def draw_centred(d, text, font, track, cx, y, fill):
    ws, total = tracked_width(d, text, font, track)
    x = cx - total / 2
    for c, cw in zip(text, ws):
        d.text((x, y), c, font=font, fill=fill)
        x += cw + track
    return total


def band_only(im, thresh=26):
    """Trim the white sheet the band was shot on, leaving weave edge to edge."""
    import colorsys
    small = im.resize((im.width // 8, im.height // 8), Image.LANCZOS)
    px = small.load()

    def sat_col(x):
        vals = [max(px[x, y]) - min(px[x, y]) for y in range(small.height)]
        vals.sort()
        return vals[len(vals) // 2]

    def sat_row(y):
        vals = [max(px[x, y]) - min(px[x, y]) for x in range(small.width)]
        vals.sort()
        return vals[len(vals) // 2]

    cols = [x for x in range(small.width) if sat_col(x) >= thresh]
    rows = [y for y in range(small.height) if sat_row(y) >= thresh]
    if not cols or not rows:
        return im
    x0, y0 = cols[0] * 8, rows[0] * 8
    x1, y1 = (cols[-1] + 1) * 8, (rows[-1] + 1) * 8
    ix, iy = round((x1 - x0) * INSET), round((y1 - y0) * INSET)
    return im.crop((x0 + ix, y0 + iy, x1 - ix, y1 - iy))


def cover_crop(path, w, h):
    im = band_only(Image.open(path).convert("RGB"))
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    left, top = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((left, top, left + w, top + h))


def tone_match(im, target):
    """Per-channel gamma so the plate's mean lands on the measured colourway."""
    import math
    px = list(im.resize((80, 100), Image.LANCZOS).get_flattened_data())
    n = len(px)
    lut = []
    for c in range(3):
        cur = sum(p[c] for p in px) / n
        cur = min(max(cur, 1.0), 254.0)
        g = math.log(target[c] / 255.0) / math.log(cur / 255.0)
        lut += [min(255, round(255 * (v / 255.0) ** g)) for v in range(256)]
    return im.point(lut)


def build(colourway, weight_label):
    bg = cover_crop(os.path.join(TEX, f"texture-{colourway}-plate.jpg"), W, H)
    bg = tone_match(bg, MEASURED[colourway])

    type_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    weight_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(type_layer)
    dw = ImageDraw.Draw(weight_layer)
    cx = W / 2

    # SPORTIF
    wf = fit_to_width(d, WORDMARK, W * WORD_W_FRAC, TRACK_EM)
    wtrack = wf.size * TRACK_EM
    wb = d.textbbox((0, 0), WORDMARK, font=wf)
    cap = wb[3] - wb[1]
    _, word_w = tracked_width(d, WORDMARK, wf, wtrack)

    # rule
    rule_t = max(2, round(cap * 0.045))
    gap_above_rule = cap * 0.44
    rule_w = word_w * RULE_OF_WORDMARK

    # collection
    sf = None
    for s in range(8, 300):
        f = ImageFont.truetype(REG, s)
        _, cw = tracked_width(d, SUBLINE, f, s * SUB_TRACK_EM)
        if cw >= rule_w / RULE_OF_SUBLINE:
            sf = f
            break
    stro = sf.size * SUB_TRACK_EM
    _, sub_w = tracked_width(d, SUBLINE, sf, stro)
    sb = d.textbbox((0, 0), SUBLINE, font=sf)
    sub_h = sb[3] - sb[1]

    # weight line
    # size off the LONGEST label so the point size is identical across the set
    gf = fit_to_width(dw, WEIGHT_SIZING_REF, sub_w * WEIGHT_OF_SUB, WEIGHT_TRACK_EM,
                      path=WEIGHT_FONT)
    gtrack = gf.size * WEIGHT_TRACK_EM
    gb = dw.textbbox((0, 0), weight_label, font=gf)
    weight_h = gb[3] - gb[1]
    gap_above_weight = cap * 0.52

    block_h = (cap + gap_above_rule + rule_t + cap * 0.42 + sub_h
               + gap_above_weight + weight_h)
    top = (H - block_h) / 2 - H * NUDGE_UP

    draw_centred(d, WORDMARK, wf, wtrack, cx, top - wb[1], CREAM)
    ry = top + cap + gap_above_rule
    d.rectangle([cx - rule_w / 2, ry, cx + rule_w / 2, ry + rule_t], fill=CREAM)
    sy = ry + rule_t + cap * 0.42
    draw_centred(d, SUBLINE, sf, stro, cx, sy - sb[1], CREAM)
    gy = sy + sub_h + gap_above_weight
    draw_centred(dw, weight_label, gf, gtrack, cx, gy - gb[1], CREAM)

    # warm drop shadow, built from the lockup's own alpha. Blurs and offsets
    # scale with the type, otherwise the halo thins out as the type grows.
    both = Image.alpha_composite(type_layer, weight_layer)
    out = bg.convert("RGBA")

    off = (round(SHADOW_OFFSET[0] * SCALE_K), round(SHADOW_OFFSET[1] * SCALE_K))
    for blur, alpha, offset in ((SHADOW_BLUR * SCALE_K, SHADOW_ALPHA, off),
                                (CORE_BLUR * SCALE_K, CORE_ALPHA,
                                 (round(2 * SCALE_K), round(4 * SCALE_K)))):
        a = both.split()[3].filter(ImageFilter.GaussianBlur(blur))
        a = a.point(lambda v: int(v * alpha / 255))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        lay.paste(Image.new("RGBA", (W, H), SHADOW_TINT + (255,)), offset, a)
        out.alpha_composite(lay)

    # the weight line sits lower on the plate, where the weave is busiest, so
    # it carries an extra halo of its own
    a = weight_layer.split()[3].filter(ImageFilter.GaussianBlur(10 * SCALE_K))
    a = a.point(lambda v: int(v * WEIGHT_HALO / 255))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lay.paste(Image.new("RGBA", (W, H), SHADOW_TINT + (255,)), (0, 0), a)
    out.alpha_composite(lay)

    out.alpha_composite(both)
    return out.convert("RGB"), (wf.size, sf.size, gf.size)


def main():
    os.makedirs(OUT, exist_ok=True)
    tiles = []
    for colourway, label in WEIGHTS:
        img, sizes = build(colourway, label)
        p = os.path.join(OUT, f"sportif-weave-{colourway}-feed.png")
        img.save(p)
        tiles.append(p)
        print(f"{colourway:7s} -> {os.path.basename(p)}  "
              f"SPORTIF {sizes[0]}, collection {sizes[1]}, weight {sizes[2]}")

    # Instagram fills a row left to right with the NEWEST post on the left, so the
    # upload order is the reverse of how the row reads. Numbered copies carry that.
    order = list(reversed(WEIGHTS))
    ordinal = ["first", "second", "third"]
    for i, (colourway, _) in enumerate(order):
        src = Image.open(os.path.join(OUT, f"sportif-weave-{colourway}-feed.png"))
        src.save(os.path.join(
            OUT, f"POST-{i + 1}-{ordinal[i]}-{colourway}.png"))
    print("post order: " + " then ".join(c for c, _ in order))

    gut = 12
    m = Image.new("RGB", (W * 3 + gut * 2, H), "#DDDDDD")
    for i, p in enumerate(tiles):
        m.paste(Image.open(p), (i * (W + gut), 0))
    m.thumbnail((1800, 1800))
    m.save(os.path.join(OUT, "preview-grid-row.jpg"), quality=92)
    print("montage -> preview-grid-row.jpg")


if __name__ == "__main__":
    main()
