#!/usr/bin/env python3
"""Email 02 social batch, v3. Lucy's second round of marks (2026-08-26).

Her notes:
  - feed-duo: move the logo to the LEFT and make the font black
  - "the rest of the pictures the beam is covering the logo" -> reposition
  - story pilates pic: notes coming on Canva (built anyway, provisional)

What changed from v1:
  1. LOCKUP IS LEFT-ANCHORED (was right).
  2. BEAM-AWARE PLACEMENT. The studio ceiling beam runs diagonally through the top of
     every reformer shot. We scan the left column and slide the lockup down until it
     clears every dark pixel, so it never sits on the beam again.
  3. IG STORY SAFE ZONE. v1 put story lockups at y=150, underneath Instagram's own
     header (profile row + progress bar ~ top 250px). Stories now start below that and
     stay clear of the bottom reply bar too.
  4. THREE TREATMENTS for Lucy to choose from: black / white / black-with-white-outline,
     each with a soft drop shadow for depth.
  5. The dark corner scrim from v1 is gone. The shadow does that job now, and the scrim
     was only ever there to rescue cream type in the corner.

    python3 clients/sportif/scripts-local/build_email02_social_v2.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


# ---------------------------------------------------------------- paths (portable)
def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / 'brand/fonts/glacial-indifference').is_dir():
            return p
    raise SystemExit('could not locate the hyperframes root')


ROOT = find_root(Path(__file__).resolve())
REG = str(ROOT / 'brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf')
REF = ROOT / 'clients/sportif/reference-images/lucy-canva-picks'
OUT = ROOT / 'clients/sportif/email-02-social/created/v3'

SOURCES = {
    'duo':         'lucy-studio-reformer-duo.png',
    'sidestretch': 'lucy-studio-reformer-sidestretch.png',
    'ballreach':   'lucy-studio-ball-overhead-back.png',
    'pilates':     'lucy-pilates-ref-noweights.png',
}
FORMATS = {'feed': (1080, 1350), 'story': (1080, 1920)}

# Instagram story chrome: profile row + progress bar on top, reply bar underneath.
STORY_SAFE_TOP, STORY_SAFE_BOTTOM = 260, 340

MARGIN_X = 96
WORDMARK, SUBLINE, HANDLE = 'SPORTIF', 'collection', '@sportifcollection'

# Lockup scale. 1.0 was v1/v2-first-pass; Hugo checked it against a real IG post on a phone
# and called it small, so we're at 1.25. Everything (type, rule, gap, shadow) keys off this,
# and the beam-clearance search re-runs against the larger footprint automatically.
SCALE = 1.25
S, TRACK_EM = round(54 * SCALE), -0.059    # canonical lockup: Glacial Regular, -0.059 em
H_S, H_TRACK_EM = round(24 * SCALE), 0.05  # the @handle footer, when it's used at all

# Instagram already prints @sportifcollection above every post and story, so stamping it
# into the image as well is redundant on our own feed (Hugo, 2026-08-17). Kept as a switch
# because it DOES earn its place off-platform: wholesale decks, Pinterest, print, or any
# image that travels without the account name attached to it.
DRAW_HANDLE = False

# The master mark is now SPORTIF / rule / collection (Lucy's artwork,
# clients/sportif/Sportif_Collection/Sportif_Collection_wordmark.jpg).
# Proportions taken off that 500px reference: rule width is 0.75x the subline width.
# We keep our canonical rule (0.43x the wordmark) and size 'collection' from it, which
# reproduces her rule:subline relationship without inheriting any tracking distortion.
SUB_TRACK_EM = 0.06
RULE_OF_WORDMARK = 0.43
RULE_OF_SUBLINE = 0.75

# ---------------------------------------------------------------- art direction
# The automatic search finds ground the type can SIT on; it can't judge composition.
# When Hugo marks a box on a frame, that box wins. Boxes are (x0, y0, x1, y1) in the
# final image's own pixels. The mark is left-aligned to x0 and centred vertically in
# the box, keeping its size. The box says WHERE, not how big.
# Anything not listed here falls back to the automatic beam-clearance search.
MANUAL_PLACEMENT = {
    # Lucy, 2026-08-26. She marked four of the v2 files by hand and sent them back.
    # Each X is "put the mark here". Photos of her markup live in
    # clients/sportif/Lucy-Wayne-pictures/changes_needed_pilates_room/.
    # Boxes below are her X positions, measured by homography onto the real asset,
    # then nudged only where the story safe zone or the ceiling beam forced it.
    ('feed',  'ballreach'):   (764, 220, 984, 333),   # Lucy: top RIGHT (was auto, left)
    ('story', 'ballreach'):   (764, 270, 984, 383),   # Lucy: top RIGHT (was left box)
    ('story', 'sidestretch'): (96,  290, 316, 403),   # Lucy: top LEFT (was right box)
    ('story', 'duo'):         (96,  355, 316, 468),   # Lucy: same spot, dropped lower
    ('feed',  'pilates'):     (155, 293, 376, 473),   # Hugo, 2026-08-17
}

# sw = stroke width on the wordmark; the handle gets a lighter stroke so the small type
# doesn't clog. White needs a much heavier shadow, because these studio walls are near-white, so
# unshadowed white type disappears.
def _s(v):
    return max(1, round(v * SCALE))


TREATMENTS = {
    'black':   dict(fill=(17, 17, 17),    stroke=None,            sw=0,     blur=_s(7),  sa=0.34, dy=_s(3)),
    'white':   dict(fill=(255, 255, 255), stroke=None,            sw=0,     blur=_s(13), sa=0.85, dy=_s(4)),
    'outline': dict(fill=(17, 17, 17),    stroke=(255, 255, 255), sw=_s(3), blur=_s(8),  sa=0.38, dy=_s(4)),
}


# ---------------------------------------------------------------- helpers
def cover(im, tw, th):
    sw, sh = im.size
    s = max(tw / sw, th / sh)
    im = im.resize((round(sw * s), round(sh * s)), Image.LANCZOS)
    l, t = (im.width - tw) // 2, (im.height - th) // 2
    return im.crop((l, t, l + tw, t + th))


def _tracked_width(d, text, font, track):
    ws = [d.textlength(c, font=font) for c in text]
    return ws, sum(ws) + track * (len(text) - 1)


def lockup_metrics(d):
    """Geometry of the left-anchored SPORTIF / rule / collection mark, measured once."""
    wf = ImageFont.truetype(REG, S)
    track = S * TRACK_EM
    b = d.textbbox((0, 0), WORDMARK, font=wf)
    cap = b[3] - b[1]
    ws, w = _tracked_width(d, WORDMARK, wf, track)
    rt, gap, rw = max(2, round(cap * 0.045)), cap * 0.44, w * RULE_OF_WORDMARK

    # size 'collection' so the rule is 0.75x its width, as in Lucy's reference
    target_sub_w = rw / RULE_OF_SUBLINE
    sf, sub_ws, sub_w = None, None, None
    for size in range(8, 200):
        f = ImageFont.truetype(REG, size)
        cand_ws, cand_w = _tracked_width(d, SUBLINE, f, size * SUB_TRACK_EM)
        if cand_w >= target_sub_w:
            sf, sub_ws, sub_w = f, cand_ws, cand_w
            break
    sb = d.textbbox((0, 0), SUBLINE, font=sf)
    sub_h = sb[3] - sb[1]
    sub_gap = cap * 0.42

    block_h = cap + gap + rt + sub_gap + sub_h
    return dict(wf=wf, track=track, b=b, cap=cap, ws=ws, w=w, rt=rt, gap=gap, rw=rw,
                sf=sf, strack=sf.size * SUB_TRACK_EM, sub_ws=sub_ws, sub_w=sub_w,
                sb=sb, sub_h=sub_h, sub_gap=sub_gap,
                block_w=max(w, sub_w), block_h=block_h)


def handle_metrics(d):
    hf = ImageFont.truetype(REG, H_S)
    htrack = H_S * H_TRACK_EM
    hws, hw = _tracked_width(d, HANDLE, hf, htrack)
    hb = d.textbbox((0, 0), HANDLE, font=hf)
    return dict(hf=hf, htrack=htrack, hws=hws, hw=hw, hb=hb, hh=hb[3] - hb[1])


def draw_lockup(layer, x_left, top, m, fill, stroke, sw):
    """Left-anchored: wordmark flush left, rule + 'collection' centred beneath it."""
    d = ImageDraw.Draw(layer)
    kw = dict(stroke_width=sw, stroke_fill=stroke) if stroke else {}
    cx = x_left + m['w'] / 2

    x, y = x_left, top - m['b'][1]
    for c, cw in zip(WORDMARK, m['ws']):
        d.text((x, y), c, font=m['wf'], fill=fill, **kw)
        x += cw + m['track']

    ssw = max(1, round(sw * 0.6)) if stroke else 0      # lighter stroke on the small type
    skw = dict(stroke_width=ssw, stroke_fill=stroke) if stroke else {}

    ry = top + m['cap'] + m['gap']
    if stroke:
        d.rectangle([cx - m['rw'] / 2 - ssw, ry - ssw,
                     cx + m['rw'] / 2 + ssw, ry + m['rt'] + ssw], fill=stroke)
    d.rectangle([cx - m['rw'] / 2, ry, cx + m['rw'] / 2, ry + m['rt']], fill=fill)

    sx = cx - m['sub_w'] / 2
    sy = ry + m['rt'] + m['sub_gap'] - m['sb'][1]
    for c, cw in zip(SUBLINE, m['sub_ws']):
        d.text((sx, sy), c, font=m['sf'], fill=fill, **skw)
        sx += cw + m['strack']


def draw_handle(layer, x_left, top, hm, fill, stroke, sw):
    """@handle as a small footer, left-aligned to the same margin as the mark."""
    d = ImageDraw.Draw(layer)
    hsw = max(1, round(sw * 0.6)) if stroke else 0
    kw = dict(stroke_width=hsw, stroke_fill=stroke) if stroke else {}
    x, y = x_left, top - hm['hb'][1]
    for c, cw in zip(HANDLE, hm['hws']):
        d.text((x, y), c, font=hm['hf'], fill=fill, **kw)
        x += cw + hm['htrack']


def find_clear_y(img, x_left, block_w, block_h, lo, hi, prefer='top', pad=34):
    """Find a vertical position in [lo, hi] where the type's footprint sits on calm,
    light ground: no ceiling beam, no cables, no skin.

    Type is dark, so we want the footprint's darkest pixels to still be light: the 2nd
    percentile is the test. `prefer` decides which end we search from, so the mark drifts
    down from the top and the footer drifts up from the bottom, each moving the least
    distance needed. Falls back to the lightest window found.
    """
    W, H = img.size
    a = np.asarray(img.convert('L'), dtype=np.float32)
    x0, x1 = max(0, x_left - 12), min(W, int(x_left + block_w) + 12)
    box_h = int(block_h) + 2 * pad

    lo, hi = int(lo), max(int(lo) + 1, int(hi))
    candidates = range(lo, hi, 6) if prefer == 'top' else range(hi, lo, -6)

    best, score = lo, -1.0
    for y in candidates:
        win = a[max(0, y - pad):y + box_h, x0:x1]
        if not win.size:
            continue
        s = float(np.percentile(win, 2))
        if s > 178:
            return y, 'clear'
        if s > score:
            best, score = y, s
    return best, f'best-effort (p2={score:.0f})'


def clear_top(img, x_left, m, fmt):
    """Slide the mark down the left column until it clears the ceiling beam."""
    H = img.size[1]
    lo = STORY_SAFE_TOP if fmt == 'story' else 104
    hi = (H - STORY_SAFE_BOTTOM - m['block_h']) if fmt == 'story' else int(H * 0.46)
    return find_clear_y(img, x_left, m['block_w'], m['block_h'], lo, hi, prefer='top')


def clear_bottom(img, x_left, hm, fmt, mark_bottom):
    """Slide the @handle footer UP from the bottom edge until it's off the reformer
    rails, cables and skin. Never rides up into the mark."""
    H = img.size[1]
    inset = STORY_SAFE_BOTTOM if fmt == 'story' else MARGIN_X
    hi = H - inset - hm['hh']
    lo = max(mark_bottom + 60, int(H * 0.55))
    return find_clear_y(img, x_left, hm['hw'], hm['hh'], lo, hi, prefer='bottom', pad=22)


def build(src, fmt, size, treat, name):
    W, H = size
    img = cover(src, W, H).convert('RGBA')
    d0 = ImageDraw.Draw(img)
    m, hm = lockup_metrics(d0), handle_metrics(d0)

    box = MANUAL_PLACEMENT.get((fmt, name))
    if box:
        # centre the mark in the marked area, both axes, since the boxes are drawn as zones
        # ("put it about here"), not as tight bounding boxes
        bx0, by0, bx1, by1 = box
        x_left = round(bx0 + ((bx1 - bx0) - m['w']) / 2)
        top = round(by0 + ((by1 - by0) - m['block_h']) / 2)
        how = 'manual box'
    else:
        x_left = MARGIN_X
        top, how = clear_top(img, MARGIN_X, m, fmt)
    t = TREATMENTS[treat]

    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    fill = t['fill'] + (255,)
    stroke = (t['stroke'] + (255,)) if t['stroke'] else None
    draw_lockup(layer, x_left, top, m, fill, stroke, t['sw'])

    if DRAW_HANDLE:
        # searched upward so it lands on calm ground, not on cables or skin
        handle_top, hhow = clear_bottom(img, MARGIN_X, hm, fmt, top + m['block_h'])
        draw_handle(layer, MARGIN_X, handle_top, hm, fill, stroke, t['sw'])
    else:
        handle_top, hhow = None, 'off'

    shadow = Image.new('RGBA', (W, H), (28, 22, 18, 0))
    blurred = layer.split()[3].filter(ImageFilter.GaussianBlur(t['blur']))
    shadow.putalpha(blurred.point(lambda v: int(v * t['sa'])))

    img.alpha_composite(shadow, (0, t['dy']))
    img.alpha_composite(layer)
    (OUT / treat).mkdir(parents=True, exist_ok=True)
    img.convert('RGB').save(OUT / treat / f'{fmt}-{name}.png')
    return top, how, handle_top, hhow


if __name__ == '__main__':
    for name, fname in SOURCES.items():
        src = Image.open(REF / fname).convert('RGB')
        for fmt, size in FORMATS.items():
            for treat in TREATMENTS:
                top, how, hy, hhow = build(src, fmt, size, treat, name)
                tail = f'handle y={hy} [{hhow}]' if hy is not None else 'handle off'
                print(f'ok {treat:8s} {fmt}-{name:12s} mark y={top:4d} [{how:22s}] {tail}')
