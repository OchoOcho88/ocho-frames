#!/usr/bin/env python3
"""The Sportif master mark, SPORTIF / rule / collection (D-017), as one importable function.

Proportions are the canonical ones from build_band_posters.py: Glacial Indifference Regular,
wordmark tracking -0.059 em, rule 0.43 of the wordmark width and 0.045 of cap height thick,
"collection" tracked 0.06 em and sized so the rule is 0.75 of its width. Import it rather
than copying it (D-050):

    from house_lockup import draw_lockup
    w, h = draw_lockup(draw, x, top, size, fill)                 # wordmark flush left at x
    w, h = draw_lockup(draw, cx, top, size, fill, align='center')  # whole mark centred on cx

Returns (width, height) of the block so callers can centre or stack it. `size` is the
wordmark point size; the block is about 2.3 times the cap height tall.
"""
from pathlib import Path
from PIL import ImageFont


def _root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / 'brand/fonts/glacial-indifference').is_dir():
            return p
    raise SystemExit('could not locate the hyperframes root')


REG = str(_root(Path(__file__).resolve()) / 'brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf')
WORDMARK, SUBLINE = 'SPORTIF', 'collection'
TRACK_EM, SUB_TRACK_EM = -0.059, 0.06
RULE_OF_WORDMARK, RULE_OF_SUBLINE = 0.43, 0.75


def _tracked_width(d, text, font, track):
    ws = [d.textlength(c, font=font) for c in text]
    return ws, sum(ws) + track * (len(text) - 1)


def measure_lockup(d, size):
    """(width, height) of the block at this wordmark size, without drawing."""
    return draw_lockup(d, 0, 0, size, None, dry=True)


def draw_lockup(d, x, top, size, fill, align='left', dry=False):
    wf = ImageFont.truetype(REG, size)
    track = size * TRACK_EM
    b = d.textbbox((0, 0), WORDMARK, font=wf)
    cap = b[3] - b[1]
    ws, w = _tracked_width(d, WORDMARK, wf, track)
    rt, gap, rw = max(2, round(cap * 0.045)), cap * 0.44, w * RULE_OF_WORDMARK

    target_sub_w = rw / RULE_OF_SUBLINE
    sf = sub_ws = None
    sub_w = 0
    for s in range(6, 400):
        f = ImageFont.truetype(REG, s)
        cand_ws, cand_w = _tracked_width(d, SUBLINE, f, s * SUB_TRACK_EM)
        if cand_w >= target_sub_w:
            sf, sub_ws, sub_w = f, cand_ws, cand_w
            break
    sb = d.textbbox((0, 0), SUBLINE, font=sf)
    block_w = max(w, sub_w)
    block_h = cap + gap + rt + cap * 0.42 + (sb[3] - sb[1])
    if dry:
        return block_w, block_h

    x_left = x - w / 2 if align == 'center' else x
    cx = x_left + w / 2
    xx, y = x_left, top - b[1]
    for c, cw in zip(WORDMARK, ws):
        d.text((xx, y), c, font=wf, fill=fill)
        xx += cw + track
    ry = top + cap + gap
    d.rectangle([cx - rw / 2, ry, cx + rw / 2, ry + rt], fill=fill)
    sx = cx - sub_w / 2
    sy = ry + rt + cap * 0.42 - sb[1]
    for c, cw in zip(SUBLINE, sub_ws):
        d.text((sx, sy), c, font=sf, fill=fill)
        sx += cw + sf.size * SUB_TRACK_EM
    return block_w, block_h
