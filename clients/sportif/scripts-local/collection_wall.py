"""Mock the wall type on the pilates picture (SPORTIF stack, S046) with 'collection' added (S050).

Lucy, 8 Oct: "The logo will need to say Sportif Collection." Hugo: she wants SPORTIF COLLECTION
on the wall behind her. This script re-renders Hugo's Photoshop wall type (Glacial Indifference
Regular, 150pt, transform x 1.8336 / y 2.1435, tracking -59, Overlay black, drop shadow 8%
multiply 3px at 120 deg) so layouts can be compared before he rebuilds the winner in the PSD.

Calibration: render the five SPORTIF rows exactly as the PSD has them and diff against the PSD's
own composite (`calibrate`). Then `layout_*` functions place the rows for each option and
composite the real foreground (girl, band, label from the PSD) back on top.

Run: .venvs/pdf/bin/python clients/sportif/scripts-local/collection_wall.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[3]
FONT = ROOT / "brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf"
DIR = ROOT / "clients/sportif/generated/images/pilates-flick/collection-wall"
W, H = 1080, 1350
SS = 4  # supersample

# Hugo's PSD text settings (read with psd-tools, S050)
PT = 150.0
SX, SY = 1.8336293237133565, 2.1435497395751524
TRACK = -59
ROWS_PSD = [  # (tx, baseline ty) of the five SPORTIF layers, top to bottom
    (94.0, 262.08608969942964),
    (93.82335690365383, 524.0892198097256),
    (93.82335690365383, 784.9995058416889),
    (93.35049092002214, 1046.9097918736525),
    (93.35049092002214, 1308.820077905616),
]


def load_refs():
    plate = np.asarray(Image.open(DIR / "_ref-plate.png").convert("RGB")).astype(np.float32)
    notype = np.asarray(Image.open(DIR / "_ref-no-type.png").convert("RGB")).astype(np.float32)
    full = np.asarray(Image.open(DIR / "_ref-full-composite.png").convert("RGB")).astype(np.float32)
    alpha = np.asarray(Image.open(DIR / "_ref-fg-alpha.png")).astype(np.float32) / 255
    return plate, notype, full, alpha


def text_mask(text, tx, ty, scale=1.0, track=TRACK, kern=True):
    """Coverage mask (H x W, 0..1) of one type layer, as Photoshop would place it.

    scale multiplies the PSD transform uniformly (1.0 = the SPORTIF rows)."""
    sx, sy = SX * scale, SY * scale
    px_v = PT * sy * SS  # vertical em in supersampled px
    font = ImageFont.truetype(str(FONT), int(round(px_v)))
    # lay the string out in vertical-em px, then squeeze horizontally by sx/sy
    xs, x = [], 0.0
    for i, ch in enumerate(text):
        xs.append(x)
        adv = font.getlength(ch)
        if kern and i + 1 < len(text):
            pair = font.getlength(ch + text[i + 1]) - font.getlength(ch) - font.getlength(text[i + 1])
            adv += pair
        x += adv + track / 1000.0 * px_v
    wide = int(x + px_v)
    img = Image.new("L", (wide, int(px_v * 1.4)), 0)
    d = ImageDraw.Draw(img)
    base = int(px_v * 1.1)
    for ch, cx in zip(text, xs):
        d.text((cx, base), ch, font=font, fill=255, anchor="ls")
    squeezed = img.resize((max(1, int(round(wide * sx / sy))), img.height), Image.LANCZOS)
    canvas = Image.new("L", (W * SS, H * SS), 0)
    canvas.paste(squeezed, (int(round(tx * SS)), int(round(ty * SS - base))))
    return np.asarray(canvas.resize((W, H), Image.LANCZOS)).astype(np.float32) / 255


def shadow_from(mask, opacity=0.08, distance=3.0, size=3.0, angle=120.0):
    a = np.deg2rad(angle)
    dx, dy = -np.cos(a) * distance, np.sin(a) * distance
    im = Image.fromarray((mask * 255).astype(np.uint8))
    im = im.filter(ImageFilter.GaussianBlur(size / 2.0))
    big = im.resize((W * SS, H * SS), Image.BILINEAR)
    shifted = Image.new("L", big.size, 0)
    shifted.paste(big, (int(round(dx * SS)), int(round(dy * SS))))
    return np.asarray(shifted.resize((W, H), Image.LANCZOS)).astype(np.float32) / 255 * opacity


def type_over(plate, masks):
    """Each type layer is its own Overlay layer with its own drop shadow, stacked in order."""
    out = plate.copy()
    for m in masks:
        # "Layer Knocks Out Drop Shadow" (Photoshop default): no shadow under the fill
        sh = (shadow_from(m) * (1 - m))[..., None]
        out = out * (1 - sh)  # multiply black at the shadow's opacity
        over = np.where(out >= 128, 2 * out - 255, 0)  # Overlay with black fill
        out = out * (1 - m[..., None]) + over * m[..., None]
    return out


def composite(typed, plate, notype, alpha):
    a = alpha[..., None]
    return np.clip(notype + (typed - plate) * (1 - a), 0, 255)


def save(arr, name):
    Image.fromarray(np.round(arr).astype(np.uint8)).save(DIR / name)
    print("wrote", DIR / name)


def calibrate():
    plate, notype, full, alpha = load_refs()
    masks = [text_mask("SPORTIF", tx, ty) for tx, ty in ROWS_PSD]
    out = composite(type_over(plate, masks), plate, notype, alpha)
    diff = np.abs(out - full)
    bg = alpha < 0.01
    print("calibration: mean diff %.3f, mean on wall %.3f, max %.0f, p99.9 %.1f" % (
        diff.mean(), diff[bg].mean(), diff.max(), np.percentile(diff, 99.9)))
    ys, xs = np.where((masks[0] > 0.5))
    print("row 1 ink bbox x %d..%d y %d..%d" % (xs.min(), xs.max(), ys.min(), ys.max()))
    save(out, "_calibration-render.png")
    save(np.clip(diff * 10, 0, 255), "_calibration-diff-x10.png")


SPORTIF_W = 876  # ink width of a SPORTIF row, x 104..980 (PSD bounds)
LEFT = 104


def ink_bounds(m, thr=0.02):  # thr 0.02 reproduces Photoshop's layer bounds exactly
    ys, xs = np.where(m > thr)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def fit_row(text, baseline, track=TRACK, width=SPORTIF_W, left=LEFT):
    """Uniform scale and origin so the word's INK spans exactly left..left+width on this baseline."""
    probe = text_mask(text, 20, 700, scale=0.5, track=track)
    x0, y0, x1, y1 = ink_bounds(probe)
    scale = width / ((x1 - x0) * 2.0)
    m = text_mask(text, 0, baseline, scale=scale, track=track)
    bx0 = ink_bounds(m)[0]
    tx = left - bx0
    return scale, tx, text_mask(text, tx, baseline, scale=scale, track=track)


def render(rows, name):
    """rows: list of (text, baseline, track). Returns per-row Photoshop numbers."""
    plate, notype, full, alpha = load_refs()
    masks, spec = [], []
    for text, baseline, track in rows:
        if text == "SPORTIF" and track == TRACK:
            tx = [r for r in ROWS_PSD if abs(r[1] - baseline) < 1]
            tx = tx[0][0] if tx else 94.0
            m, scale = text_mask(text, tx, baseline), 1.0
        else:
            scale, tx, m = fit_row(text, baseline, track)
        masks.append(m)
        x0, y0, x1, y1 = ink_bounds(m)
        spec.append(dict(text=text, scale=scale, size_pt=PT * scale, track=track, baseline=baseline,
                         X=x0, Y=y0, W=x1 - x0, H=y1 - y0))
    out = composite(type_over(plate, masks), plate, notype, alpha)
    save(out, name)
    for s in spec:
        print("   %-11s scale %.4f (=%.2fpt at the PSD transform) track %d  bounds X %d Y %d W %d H %d  baseline %.1f" % (
            s["text"], s["scale"], s["size_pt"], s["track"], s["X"], s["Y"], s["W"], s["H"], s["baseline"]))
    return spec


def stacked(words, top=39, bottom=1314, track_for=None):
    """Re-space rows of different heights so they fill top..bottom with equal ink gaps."""
    track_for = track_for or {}
    info = []
    for w in words:
        tr = track_for.get(w, TRACK)
        if w == "SPORTIF" and tr == TRACK:
            m = text_mask(w, 94.0, 700)
        else:
            m = fit_row(w, 700, tr)[2]
        x0, y0, x1, y1 = ink_bounds(m)
        info.append((w, tr, 700 - y0, y1 - 700))  # ink above / below baseline
    total = sum(a + b for _, _, a, b in info)
    gap = (bottom - top - total) / (len(words) - 1)
    rows, y = [], top
    for w, tr, above, below in info:
        rows.append((w, y + above, tr))
        y = y + above + below + gap
    print("   ink gap between rows: %.1f px (the original wall: 34)" % gap)
    return rows


# Photoshop's Properties > Transform box for a point-type layer is the TEXT box, not the ink:
# X = text origin, W = (advances + (n-1) * tracking) * PT * sx, Y = baseline - 0.84 em * PT * sy,
# H = 1.092 em * PT * sy. Matched to Hugo's panel on row 1 (W 891.42, H 351.11, X 94, Y -8), S050.
PANEL_ASC, PANEL_H = 0.84, 1.092


def panel_numbers(text, tx, baseline, scale, track=TRACK):
    f = ImageFont.truetype(str(FONT), 1000)
    tot = 0.0
    for i, ch in enumerate(text):
        a = f.getlength(ch)
        if i + 1 < len(text):
            a += f.getlength(ch + text[i + 1]) - f.getlength(ch) - f.getlength(text[i + 1])
        tot += a
    em = tot / 1000 + (len(text) - 1) * track / 1000
    return dict(X=tx, Y=baseline - PANEL_ASC * PT * SY * scale, W=em * PT * SX * scale, H=PANEL_H * PT * SY * scale)


FEED = ROOT / "clients/sportif/generated/images/pilates-flick/photoshop/pilates-flick-v3-4-sportif-collection_lucy_02.png"
STORY = DIR / "pilates-flick-v3-4-sportif-collection_lucy_02_story-1080x1920.png"
STORY_H, STORY_Y = 1920, 248  # 248 = eight whole rows, 106 px margins top and bottom
WALL = (230, 224, 217)  # #E6E0D9, the plate at its top and bottom edges (measured flat, S050)
# Hugo's six rows as built (read from the _lucy_02 PSD): pair pitch 433.0 px
COLL_SCALE, COLL_TX = 0.63416, 97.0


def story():
    """Hugo's feed export, pixel for pixel, on a 1080x1920 wall, plus one COLLECTION row above
    and one SPORTIF row below on the same rhythm. Story safe zone (house): top 260, bottom 340."""
    feed_im = Image.open(FEED)
    feed = np.asarray(feed_im.convert("RGB")).astype(np.float32)
    global H
    H_feed, H = H, STORY_H  # text_mask and shadow_from render on a canvas of height H
    try:
        canvas = np.empty((STORY_H, W, 3), np.float32)
        canvas[:] = WALL
        canvas[STORY_Y:STORY_Y + H_feed] = feed
        top = text_mask("COLLECTION", COLL_TX, STORY_Y + 439.28 - 433.0, scale=COLL_SCALE)
        bottom = text_mask("SPORTIF", ROWS_PSD[4][0], STORY_Y + 1128.09 + 433.0)
        out = type_over(canvas, [top, bottom])
    finally:
        H = H_feed
    Image.fromarray(np.round(out).astype(np.uint8)).save(STORY, icc_profile=feed_im.info.get("icc_profile"))
    print("wrote", STORY)


BANDFLICK_FEED = ROOT / "clients/sportif/generated/images/pilates-flick/photoshop/pilates-flick-v3-4_lucy_01.png"
BANDFLICK_STORY = ROOT / "clients/sportif/generated/images/pilates-flick/pilates-flick-v3-4_lucy_01_story-1080x1920.png"
NUB_BOX = (583, 1037, 617, 1071)  # x0, y0, x1, y1: the grey nub beside her shin, Hugo's S050 fill
NUB_FILL = (228, 221, 215)  # #E4DDD7, the local wall there (not the #E6E0D9 of the edges)
ANKLE_PATCHES = [(360, 308, 642, 562), (436, 976, 720, 1258)]  # x0, y0, x1, y1, padded 8 px


def story_bandflick():
    """The band flick (no type, no logo for Instagram, Lucy 8 Oct) on a 1080x1920 wall at the same
    y as the COLLECTION story. Same plate as the stack PSD, so the nub fix is applied the way Hugo
    did it there: the plate filled under the girl cut-out, i.e. export + (fill - plate) * (1 - alpha)."""
    feed_im = Image.open(BANDFLICK_FEED)
    feed = np.asarray(feed_im.convert("RGB")).astype(np.float32)
    plate, _, _, alpha = load_refs()
    # The two soft square ankle patches from the weight removal (Q-027: 1 to 3 levels darker,
    # mapped S050) hold the nub too. The rest of the wall is a dead-flat #E6E0D9, so flattening
    # the wall inside both boxes (the girl cut-out stays on top) clears patches and nub together.
    fixed_plate = plate.copy()
    for x0, y0, x1, y1 in ANKLE_PATCHES:
        fixed_plate[y0:y1, x0:x1] = WALL
    feed = feed + (fixed_plate - plate) * (1 - alpha[..., None])
    canvas = np.empty((STORY_H, W, 3), np.float32)
    canvas[:] = WALL
    canvas[STORY_Y:STORY_Y + feed.shape[0]] = feed
    Image.fromarray(np.clip(np.round(canvas), 0, 255).astype(np.uint8)).save(
        BANDFLICK_STORY, icc_profile=feed_im.info.get("icc_profile"))
    print("wrote", BANDFLICK_STORY)


if __name__ == "__main__":
    if "story-bandflick" in sys.argv:
        story_bandflick()
        sys.exit()
    if "story" in sys.argv:
        story()
        sys.exit()
    if "panel" in sys.argv:  # Hugo's pick, S050: C, six rows. Print the numbers to type in Properties.
        psd_tx = {0: ROWS_PSD[0][0], 2: ROWS_PSD[2][0], 4: ROWS_PSD[4][0]}
        for i, (w, b, tr) in enumerate(stacked(["SPORTIF", "COLLECTION"] * 3)):
            s, tx = (1.0, psd_tx[i]) if w == "SPORTIF" else fit_row(w, b, tr)[:2]
            p = panel_numbers(w, tx, b, s)
            print("row %d %-10s X %.2f Y %.2f W %.2f H %.2f" % (i + 1, w, p["X"], p["Y"], p["W"], p["H"]))
        sys.exit()
    if "calibrate" in sys.argv:
        calibrate()
        sys.exit()
    base = [r[1] for r in ROWS_PSD]
    print("A  lowercase collection on rows 2 and 4, the wall's tracking (-59), grid unchanged")
    render([("SPORTIF", base[0], TRACK), ("collection", base[1], TRACK), ("SPORTIF", base[2], TRACK),
            ("collection", base[3], TRACK), ("SPORTIF", base[4], TRACK)], "A-lowercase-track-59.png")
    print("B  lowercase collection on rows 2 and 4, untracked like her logo (0), grid unchanged")
    render([("SPORTIF", base[0], TRACK), ("collection", base[1], 0), ("SPORTIF", base[2], TRACK),
            ("collection", base[3], 0), ("SPORTIF", base[4], TRACK)], "B-lowercase-track-0.png")
    print("C  CAPS COLLECTION alternating, six rows, re-spaced")
    render(stacked(["SPORTIF", "COLLECTION"] * 3), "C-caps-six-rows.png")
    print("D  CAPS COLLECTION alternating, five rows, re-spaced")
    render(stacked(["SPORTIF", "COLLECTION", "SPORTIF", "COLLECTION", "SPORTIF"]), "D-caps-five-rows.png")
