#!/usr/bin/env python3
"""Posters built from the REAL band cutouts (Session 032).

Two directions, each in IG feed 4:5 and IG story 9:16:

  collage  editorial layered collage (peach plate, big headline, band cut out in front)
  teaser   coming-soon teaser (band as the one pop of colour, waitlist CTA, no dates)

Source cutouts are Hugo's iPhone shots of the real HEAVY band with the background removed,
in clients/sportif/assets/Sportif_Bands/. Type is real Glacial Indifference, laid in PIL,
using the canonical SPORTIF / rule / collection lockup (D-017).

    python3 clients/sportif/scripts-local/build_band_posters.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


# ---------------------------------------------------------------- paths (portable)
def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / 'brand/fonts/glacial-indifference').is_dir():
            return p
    raise SystemExit('could not locate the hyperframes root')


ROOT = find_root(Path(__file__).resolve())
FDIR = ROOT / 'brand/fonts/glacial-indifference'
REG, BOLD = str(FDIR / 'GlacialIndifference-Regular.otf'), str(FDIR / 'GlacialIndifference-Bold.otf')
BANDS = ROOT / 'clients/sportif/assets/Sportif_Bands'
OUT = ROOT / 'clients/sportif/generated/images/band-posters'
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- brand constants
CREAM = (246, 238, 229)
PEACH = (240, 205, 179)
CARAMEL = (198, 146, 110)
TERRA = (131, 56, 39)
CHAR = (74, 67, 60)
WHITE = (255, 255, 255)

WORDMARK, SUBLINE = 'SPORTIF', 'collection'
TRACK_EM, SUB_TRACK_EM = -0.059, 0.06     # canonical lockup tracking
RULE_OF_WORDMARK, RULE_OF_SUBLINE = 0.43, 0.75

FORMATS = {'feed': (1080, 1350), 'story': (1080, 1920)}
# Instagram story chrome: profile row + progress bar on top, reply bar underneath.
STORY_SAFE_TOP, STORY_SAFE_BOTTOM = 260, 340


# ---------------------------------------------------------------- type helpers
def tracked_width(d, text, font, track):
    ws = [d.textlength(c, font=font) for c in text]
    return ws, sum(ws) + track * (len(text) - 1)


def draw_tracked(d, x, y, text, font, track, fill):
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + track


def fit_size(d, text, fontpath, target_w, track_em, lo=10, hi=600):
    """Largest point size whose tracked width fits target_w."""
    while lo < hi:
        m = (lo + hi + 1) // 2
        f = ImageFont.truetype(fontpath, m)
        _, w = tracked_width(d, text, f, m * track_em)
        if w <= target_w:
            lo = m
        else:
            hi = m - 1
    return lo


def lockup(d, x_left, top, size, fill):
    """SPORTIF / rule / collection, wordmark flush left, rule + subline centred beneath."""
    wf = ImageFont.truetype(REG, size)
    track = size * TRACK_EM
    b = d.textbbox((0, 0), WORDMARK, font=wf)
    cap = b[3] - b[1]
    ws, w = tracked_width(d, WORDMARK, wf, track)
    rt, gap, rw = max(2, round(cap * 0.045)), cap * 0.44, w * RULE_OF_WORDMARK

    target_sub_w = rw / RULE_OF_SUBLINE
    sf = sub_ws = None
    sub_w = 0
    for s in range(8, 240):
        f = ImageFont.truetype(REG, s)
        cand_ws, cand_w = tracked_width(d, SUBLINE, f, s * SUB_TRACK_EM)
        if cand_w >= target_sub_w:
            sf, sub_ws, sub_w = f, cand_ws, cand_w
            break
    sb = d.textbbox((0, 0), SUBLINE, font=sf)

    cx = x_left + w / 2
    x, y = x_left, top - b[1]
    for c, cw in zip(WORDMARK, ws):
        d.text((x, y), c, font=wf, fill=fill)
        x += cw + track

    ry = top + cap + gap
    d.rectangle([cx - rw / 2, ry, cx + rw / 2, ry + rt], fill=fill)

    sx = cx - sub_w / 2
    sy = ry + rt + cap * 0.42 - sb[1]
    for c, cw in zip(SUBLINE, sub_ws):
        d.text((sx, sy), c, font=sf, fill=fill)
        sx += cw + sf.size * SUB_TRACK_EM

    block_h = cap + gap + rt + cap * 0.42 + (sb[3] - sb[1])
    return max(w, sub_w), block_h


# ---------------------------------------------------------------- image helpers
def cutout(name, height, angle=0.0):
    """Load a band cutout, trim to its alpha, scale to height, optionally rotate."""
    im = Image.open(BANDS / name).convert('RGBA')
    im = im.crop(im.split()[3].getbbox())
    w = max(1, round(im.width * height / im.height))
    im = im.resize((w, height), Image.LANCZOS)
    if angle:
        im = im.rotate(angle, expand=True, resample=Image.BICUBIC)
    return im


def shadow(layer, obj, xy, blur=38, offset=(14, 22), opacity=70, tint=(122, 78, 56)):
    """Soft warm drop shadow from an RGBA object's alpha.

    The tint is a warm brown, not grey: a neutral shadow goes muddy on the peach ground.
    """
    pad = blur * 3
    a = obj.split()[3].point(lambda v: int(v * opacity / 255))
    canvas_a = Image.new('L', (obj.width + pad * 2, obj.height + pad * 2), 0)
    canvas_a.paste(a, (pad, pad))
    sh = Image.new('RGBA', canvas_a.size, tint + (0,))
    sh.putalpha(canvas_a.filter(ImageFilter.GaussianBlur(blur)))
    layer.alpha_composite(sh, (xy[0] + offset[0] - pad, xy[1] + offset[1] - pad))


def card(layer, obj, xy, border=18, tilt=0.0, bg=CREAM, blur=26, opacity=64):
    """Mount a cutout on a cream card (a collage element), optionally tilted."""
    w, h = obj.width + border * 2, obj.height + border * 2
    plate = Image.new('RGBA', (w, h), bg + (255,))
    plate.alpha_composite(obj, (border, border))
    if tilt:
        plate = plate.rotate(tilt, expand=True, resample=Image.BICUBIC)
    shadow(layer, plate, xy, blur=blur, offset=(8, 14), opacity=opacity)
    layer.alpha_composite(plate, xy)
    return plate.size


def pill(d, cx, top, text, size, fg, bg, pad_x=52, pad_y=26, track_em=0.14):
    f = ImageFont.truetype(REG, size)
    track = size * track_em
    _, w = tracked_width(d, text, f, track)
    b = d.textbbox((0, 0), text, font=f)
    h = b[3] - b[1]
    x0, y0 = cx - w / 2 - pad_x, top
    x1, y1 = cx + w / 2 + pad_x, top + h + pad_y * 2
    d.rounded_rectangle([x0, y0, x1, y1], radius=(y1 - y0) / 2, fill=bg)
    draw_tracked(d, cx - w / 2, y0 + pad_y - b[1], text, f, track, fg)
    return y1 - y0


# ---------------------------------------------------------------- poster 1: collage
def build_collage(fmt):
    W, H = FORMATS[fmt]
    story = fmt == 'story'
    top_edge = STORY_SAFE_TOP if story else 0
    bot_edge = H - STORY_SAFE_BOTTOM if story else H
    live = bot_edge - top_edge
    M = 84

    canvas = Image.new('RGBA', (W, H), CREAM + (255,))
    d = ImageDraw.Draw(canvas)

    # The story canvas is taller than the feed one, so the plate is pushed closer to the
    # safe edges and the type keys up, otherwise everything huddles in the middle third.
    f_top, f_bot, f_rule, f_mark, t_scale = (
        (0.10, 0.945, 0.075, 0.018, 1.22) if story else (0.16, 0.90, 0.125, 0.045, 1.0))

    # the peach plate, inset from the margins, with a thin terracotta rule above it
    plate_top = top_edge + round(live * f_top)
    plate_bot = top_edge + round(live * f_bot)
    d.rectangle([M, plate_top, W - M, plate_bot], fill=PEACH)
    rule_y = top_edge + round(live * f_rule)
    d.rectangle([M, rule_y, W - M, rule_y + 3], fill=CARAMEL)

    # kicker lockup, cream ground above the plate
    lw, lh = lockup(d, M, top_edge + round(live * f_mark), round(W * 0.048 * t_scale), CHAR)

    # headline, set on the plate, left aligned, three lines.
    # Width is capped so the band only kisses the last letter, never eats a word.
    text_x = M + round(W * 0.045)
    lines = ['EVERYDAY', 'TRAINING', 'ELEVATED']
    hsize = fit_size(d, max(lines, key=len), BOLD, W * 0.43 * (1.05 if story else 1.0), 0.01)
    hf = ImageFont.truetype(BOLD, hsize)
    htrack = hsize * 0.01
    lead = hsize * 1.08
    hy = plate_top + round((plate_bot - plate_top) * 0.10)
    for i, ln in enumerate(lines):
        b = d.textbbox((0, 0), ln, font=hf)
        draw_tracked(d, text_x, hy + i * lead - b[1], ln, hf, htrack, CHAR)
    head_bot = hy + 2 * lead + hsize

    # the band, cut out and tilted, breaking out of the plate at the bottom.
    # Sized so its foot lands just below the plate and stays clear of the footer line.
    footer_y = plate_bot + round(live * 0.032)
    band = cutout('sportif-band-heavy-front-folded.png', round(live * 0.68), angle=10)
    bx = W - band.width - round(W * 0.015)
    by = min(plate_top + round((plate_bot - plate_top) * 0.05),
             plate_bot + round(live * 0.045) - band.height)
    shadow(canvas, band, (bx, by), blur=44, offset=(14, 26), opacity=60)
    canvas.alpha_composite(band, (bx, by))

    # collage element: a swatch of the inside grip face, on a tilted cream card.
    # It shows the second texture of the product, so it earns its place next to the band.
    grip = cutout('sportif-band-heavy-inside-grip-a.png', round(live * 0.62))
    seg_h = round(grip.width * 0.62)
    top = round(grip.height * 0.40)
    swatch = grip.crop((0, top, grip.width, top + seg_h)).rotate(90, expand=True)
    swatch.thumbnail((round(W * 0.20), round(W * 0.20)), Image.LANCZOS)
    card_y = max(head_bot + round(live * 0.055), plate_bot - round(live * 0.30))
    card(canvas, swatch, (text_x - round(W * 0.012), card_y),
         border=round(W * 0.020), tilt=-6)

    # footer line, on the cream below the plate
    ff = ImageFont.truetype(REG, round(W * 0.024 * t_scale))
    fb = d.textbbox((0, 0), 'MADE TO BE SEEN', font=ff)
    fy = footer_y - fb[1]
    draw_tracked(d, M, fy, 'MADE TO BE SEEN', ff, ff.size * 0.16, CARAMEL)
    rt = 'BOOTY BAND, HEAVY'
    _, rw = tracked_width(d, rt, ff, ff.size * 0.16)
    draw_tracked(d, W - M - rw, fy, rt, ff, ff.size * 0.16, CARAMEL)

    name = f'poster-collage-{fmt}.png'
    canvas.convert('RGB').save(OUT / name)
    return name


# ---------------------------------------------------------------- poster 2: teaser
def build_teaser(fmt):
    W, H = FORMATS[fmt]
    story = fmt == 'story'
    top_edge = STORY_SAFE_TOP if story else 0
    bot_edge = H - STORY_SAFE_BOTTOM if story else H
    live = bot_edge - top_edge

    canvas = Image.new('RGBA', (W, H), PEACH + (255,))
    d = ImageDraw.Draw(canvas)

    # lockup, centred at the top of the live area
    t_scale = 1.30 if story else 1.0
    size = round(W * 0.056 * t_scale)
    probe = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    wf = ImageFont.truetype(REG, size)
    _, ww = tracked_width(probe, WORDMARK, wf, size * TRACK_EM)
    lw, lh = lockup(d, (W - ww) / 2, top_edge + round(live * 0.055), size, WHITE)

    # the band, near vertical, one pop of colour on the peach
    band_h = round(live * (0.48 if story else 0.60))
    band = cutout('sportif-band-heavy-front-flat.png', band_h, angle=-4)
    bx = (W - band.width) // 2
    by = top_edge + round(live * (0.235 if story else 0.165))
    shadow(canvas, band, (bx, by), blur=54, offset=(0, 26), opacity=46)
    canvas.alpha_composite(band, (bx, by))

    # "Coming soon", tracked, warm charcoal
    cs = round(W * 0.062 * t_scale)
    cf = ImageFont.truetype(REG, cs)
    ctrack = cs * 0.10
    _, cw = tracked_width(d, 'COMING SOON', cf, ctrack)
    cb = d.textbbox((0, 0), 'COMING SOON', font=cf)
    cy = top_edge + round(live * 0.795)
    draw_tracked(d, (W - cw) / 2, cy - cb[1], 'COMING SOON', cf, ctrack, CHAR)

    # waitlist pill
    pill(d, W / 2, cy + (cb[3] - cb[1]) + round(live * 0.045),
         'JOIN THE WAITLIST', round(W * 0.030 * t_scale), CREAM, TERRA)

    name = f'poster-teaser-{fmt}.png'
    canvas.convert('RGB').save(OUT / name)
    return name


if __name__ == '__main__':
    made = []
    for fmt in FORMATS:
        made.append(build_collage(fmt))
        made.append(build_teaser(fmt))
    for n in made:
        print('ok ->', (OUT / n).relative_to(ROOT))
