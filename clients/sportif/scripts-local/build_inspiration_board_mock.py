#!/usr/bin/env python3
"""Mock of the FINAL frame of a Sportif stop-motion inspiration board (S040).

Reference: SABO "Tropic Muse" email GIF, measured in
clients/sportif/inspiration-board/reference-notes.md.

Everything on the board is a real workspace asset: the colour-corrected band cutouts
(D-039), the weave plates (D-028, real product colour per D-046), the Pantone 162 C
chip (D-051), the master mark (D-017, her artwork per D-052), and polaroids from
Lucy's friend's gym photos (composited only, no generator, D-038) plus one Canva pick.

Overrides (D-050, parameterise rather than fork):
  SPORTIF_CAPTION   caption under the board (default "The Collection")
  SPORTIF_OUT       output path
  SPORTIF_SEED      layout jitter seed
  SPORTIF_SIGNATURE PNG or JPG of her real handwritten signature, dark on light;
                    default inspiration-board/lucy-signature.png. Script font stands in if missing.
  SPORTIF_WEAVE_SCALE  tile scale for the fabric swatches
"""
import os, random, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]            # clients/sportif
WS = ROOT.parents[1]                                   # hyperframes
FONTS = WS / "brand/fonts/glacial-indifference"
CUT = ROOT / "assets/Sportif_Bands/Bands_background_removed/colour-corrected"
TEX = ROOT / "assets/textures"
LOGO = ROOT / "assets/logo-pantone-162c/SPORTIF-collection-logo-peach-on-cream-PANTONE162C.png"
FRIEND = ROOT / "Lucy-Wayne-pictures/LUCYFRIENDGYM/Lucy Friend"
CANVA = ROOT / "email-02-social/created/feed-pilates.png"
LUCY = ROOT / "Lucy-Wayne-pictures"


def lucy_pic(stamp):
    """macOS puts a narrow no-break space before am/pm in screenshot names, so match by pattern."""
    hits = sorted(LUCY.glob(f"Screenshot 2026-07-24 at {stamp}*.png"))
    if not hits:
        raise FileNotFoundError(f"no Lucy screenshot at {stamp}")
    return hits[0]
SIGNATURE = os.environ.get("SPORTIF_SIGNATURE", str(ROOT / "inspiration-board/lucy-signature.png"))
SCRIPT_FONTS = ["/System/Library/Fonts/Supplemental/SnellRoundhand.ttc",
                "/System/Library/Fonts/Supplemental/Savoye LET.ttc",
                "/System/Library/Fonts/Supplemental/Brush Script.ttf"]

CAPTION = os.environ.get("SPORTIF_CAPTION", "The Collection")
OUT = Path(os.environ.get("SPORTIF_OUT", ROOT / "generated/images/inspiration-board/final-frame-mock-v3.png"))
random.seed(int(os.environ.get("SPORTIF_SEED", "7")))

W, H = 1200, 1500
PEACH = (0xFF, 0xBE, 0x9F)
BAND = {"light": (0xB8, 0xA0, 0x80), "medium": (0x9D, 0x74, 0x59), "heavy": (0x6C, 0x43, 0x33)}
CHOC = (0x4A, 0x2E, 0x22)
TERRACOTTA = (0xB5, 0x57, 0x3A)


def font(name, size):
    return ImageFont.truetype(str(FONTS / f"GlacialIndifference-{name}.otf"), size)


# ---------- helpers ----------
def drop_shadow(canvas, item, xy, offset=(7, 9), blur=9, opacity=110):
    """Paste an RGBA item with a soft shadow under it."""
    x, y = xy
    a = item.split()[-1]
    sh = Image.new("RGBA", item.size, (0, 0, 0, 0))
    sh.putalpha(a.point(lambda v: v * opacity // 255))
    pad = blur * 3
    big = Image.new("RGBA", (item.width + pad * 2, item.height + pad * 2), (0, 0, 0, 0))
    big.paste(sh, (pad, pad))
    big = big.filter(ImageFilter.GaussianBlur(blur))
    canvas.alpha_composite(big, (x + offset[0] - pad, y + offset[1] - pad))
    canvas.alpha_composite(item, (x, y))


def rotate(item, deg):
    return item.rotate(deg, resample=Image.BICUBIC, expand=True)


def pin(canvas, cx, cy, colour=TERRACOTTA, r=9):
    d = ImageDraw.Draw(canvas)
    # shadow
    sh = Image.new("RGBA", (r * 6, r * 6), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((r * 2, r * 2 + 3, r * 4, r * 4 + 3), fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(3))
    canvas.alpha_composite(sh, (cx - r * 3, cy - r * 3))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=colour + (255,))
    d.ellipse((cx - r // 2 - 1, cy - r // 2 - 2, cx - 1, cy - 2), fill=(255, 255, 255, 150))


def cork(size):
    """Procedural cork: warm base with two scales of speckle."""
    w, h = size
    base = Image.new("RGB", size, (0xC4, 0x93, 0x62))
    noise = Image.effect_noise(size, 60).convert("L")
    fine = Image.effect_noise((w // 3, h // 3), 90).resize(size, Image.BILINEAR).convert("L")
    coarse = Image.effect_noise((w // 9, h // 9), 70).resize(size, Image.BICUBIC).convert("L").filter(ImageFilter.GaussianBlur(2))
    dark = Image.new("RGB", size, (0x8E, 0x5F, 0x38))
    light = Image.new("RGB", size, (0xDD, 0xB3, 0x84))
    out = Image.composite(dark, base, noise.point(lambda v: max(0, v - 165) * 2))
    out = Image.composite(light, out, fine.point(lambda v: max(0, v - 168) * 2))
    out = Image.composite(dark, out, coarse.point(lambda v: min(70, max(0, v - 178) * 2)))
    out = out.filter(ImageFilter.GaussianBlur(0.6))
    return out.convert("RGBA")


def square_crop(im, side):
    im = ImageOps.exif_transpose(im).convert("RGB")
    s = min(im.size)
    l = (im.width - s) // 2
    t = (im.height - s) // 2
    return im.crop((l, t, l + s, t + s)).resize((side, side), Image.LANCZOS)


def polaroid(photo_path, side=200, crop_box=None, landscape=False):
    im = Image.open(photo_path)
    im = ImageOps.exif_transpose(im).convert("RGB")
    if crop_box:
        im = im.crop(crop_box)
    if landscape:
        ph = ImageOps.fit(im, (side, round(side * 0.7)), Image.LANCZOS)
    else:
        ph = square_crop(im, side)
    m = 14
    card = Image.new("RGBA", (ph.width + m * 2, ph.height + m * 2 + 44), (250, 248, 244, 255))
    card.paste(ph, (m, m))
    return card


def signature_ink(path, max_size=(180, 90)):
    """Turn a dark-on-light signature image into chocolate ink on transparent."""
    src = ImageOps.exif_transpose(Image.open(path))
    if src.mode in ("RGBA", "LA"):
        flat = Image.new("RGBA", src.size, (255, 255, 255, 255))
        flat.alpha_composite(src.convert("RGBA"))
        src = flat
    im = src.convert("L")
    # normalise: ink dark, paper light, then ink strength becomes alpha
    lo, hi = im.getextrema()
    im = im.point(lambda v: round((v - lo) * 255 / max(1, hi - lo)))
    alpha = ImageOps.invert(im).point(lambda v: 0 if v < 40 else min(255, round((v - 40) * 1.4)))
    bbox = alpha.getbbox()
    alpha = alpha.crop(bbox)
    ink = Image.new("RGBA", alpha.size, CHOC + (255,))
    ink.putalpha(alpha)
    ink.thumbnail(max_size, Image.LANCZOS)
    return ink


def signature_card():
    """Cream note card carrying the Lucy Wayne signature."""
    card = Image.new("RGBA", (210, 120), (250, 248, 244, 255))
    if SIGNATURE and Path(SIGNATURE).exists():
        sig = signature_ink(SIGNATURE)
        card.alpha_composite(sig, ((card.width - sig.width) // 2, (card.height - sig.height) // 2))
        return card
    f = None
    for fp in SCRIPT_FONTS:
        if Path(fp).exists():
            f = ImageFont.truetype(fp, 46)
            break
    f = f or font("Italic", 40)
    d = ImageDraw.Draw(card)
    tw = d.textlength("Lucy Wayne", font=f)
    d.text(((card.width - tw) / 2, 30), "Lucy Wayne", font=f, fill=CHOC)
    return card


def chip(label, colour, sub=None):
    card = Image.new("RGBA", (128, 158), (250, 248, 244, 255))
    d = ImageDraw.Draw(card)
    d.rectangle((12, 12, 116, 108), fill=colour + (255,))
    f = font("Bold", 15)
    d.text((14, 118), label, font=f, fill=CHOC)
    if sub:
        d.text((14, 136), sub, font=font("Regular", 12), fill=(0x8A, 0x70, 0x60))
    return card


def band(name, height):
    im = Image.open(CUT / f"sportif-band-{name}-front-folded.png").convert("RGBA")
    w = round(im.width * height / im.height)
    return im.resize((w, height), Image.LANCZOS)


WEAVE_SCALE = float(os.environ.get("SPORTIF_WEAVE_SCALE", "0.2"))


def weave_swatch(name, size, rough_edge=True):
    """Tile the seamless weave tile at a scale where the pitch matches the band cutouts."""
    tile = Image.open(TEX / f"texture-{name}-tile.jpg").convert("RGB")
    tile = tile.resize((max(8, round(tile.width * WEAVE_SCALE)), max(8, round(tile.height * WEAVE_SCALE))), Image.LANCZOS)
    w, h = size
    sw = Image.new("RGB", (w, h))
    for yy in range(0, h, tile.height):
        for xx in range(0, w, tile.width):
            sw.paste(tile, (xx, yy))
    sw = sw.convert("RGBA")
    if rough_edge:
        # a frayed-looking edge: nibble the alpha with noise on the border
        a = Image.new("L", (w, h), 255)
        n = Image.effect_noise((w, h), 80).point(lambda v: 255 if v > 118 else 0)
        border = Image.new("L", (w, h), 0)
        ImageDraw.Draw(border).rectangle((3, 3, w - 4, h - 4), fill=255)
        border = border.filter(ImageFilter.GaussianBlur(2))
        a = Image.composite(a, n, border)
        sw.putalpha(a)
    return sw


# ---------- scene ----------
canvas = Image.new("RGBA", (W, H), (0xF1, 0xEC, 0xE4, 255))
d = ImageDraw.Draw(canvas)

# wall gradient and table
for y in range(H):
    t = y / H
    c = tuple(round(a + (b - a) * t) for a, b in zip((0xF3, 0xEE, 0xE7), (0xE6, 0xDE, 0xD3)))
    d.line((0, y, W, y), fill=c + (255,))
TABLE_Y = 1235
d.rectangle((0, TABLE_Y, W, H), fill=(0xE0, 0xD7, 0xCA, 255))
# soft horizon shadow where wall meets table
hz = Image.new("RGBA", (W, 80), (0, 0, 0, 0))
ImageDraw.Draw(hz).rectangle((0, 30, W, 50), fill=(0, 0, 0, 40))
canvas.alpha_composite(hz.filter(ImageFilter.GaussianBlur(10)), (0, TABLE_Y - 40))

# board: white frame, cork inside, leaning against the wall
BX0, BY0, BX1, BY1 = 110, 120, 1090, 1225
FR = 22
frame = Image.new("RGBA", (BX1 - BX0, BY1 - BY0), (0xFA, 0xF8, 0xF4, 255))
fd = ImageDraw.Draw(frame)
fd.rectangle((0, 0, frame.width - 1, frame.height - 1), outline=(0xDC, 0xD6, 0xCC, 255), width=2)
inner = cork((frame.width - FR * 2, frame.height - FR * 2))
# inset shadow along the top and left of the cork
ins = Image.new("RGBA", inner.size, (0, 0, 0, 0))
ImageDraw.Draw(ins).rectangle((0, 0, inner.width, 14), fill=(0, 0, 0, 70))
ImageDraw.Draw(ins).rectangle((0, 0, 10, inner.height), fill=(0, 0, 0, 50))
inner.alpha_composite(ins.filter(ImageFilter.GaussianBlur(7)))
frame.alpha_composite(inner, (FR, FR))
drop_shadow(canvas, frame, (BX0, BY0), offset=(10, 16), blur=18, opacity=90)

CX0, CY0 = BX0 + FR, BY0 + FR          # cork origin on canvas
CW, CH = inner.size

# fabric layer: MEDIUM weave over most of the board, LIGHT and HEAVY as smaller swatches
big = rotate(weave_swatch("medium", (700, 640)), -2.5)
drop_shadow(canvas, big, (CX0 + 40, CY0 + 60), offset=(6, 8), blur=8, opacity=120)
sw_l = rotate(weave_swatch("light", (230, 300)), 4)
drop_shadow(canvas, sw_l, (CX0 + 620, CY0 + 610), offset=(5, 7))
sw_h = rotate(weave_swatch("heavy", (250, 210)), -6)
drop_shadow(canvas, sw_h, (CX0 + 20, CY0 + 730), offset=(5, 7))
pin(canvas, CX0 + 655, CY0 + 640)
pin(canvas, CX0 + 60, CY0 + 760, colour=PEACH)

# master mark card, top left, over the fabric
logo = Image.open(LOGO).convert("RGB")
logo = logo.crop((250, 250, 1750, 1750)).resize((220, 220), Image.LANCZOS)
card = Image.new("RGBA", (236, 236), (250, 248, 244, 255))
card.paste(logo, (8, 8))
card = rotate(card, 2)
drop_shadow(canvas, card, (CX0 + 60, CY0 + 40))
pin(canvas, CX0 + 60 + card.width // 2, CY0 + 52, colour=PEACH)

# signature note card, top row
sig = rotate(signature_card(), -2)
drop_shadow(canvas, sig, (CX0 + 315, CY0 + 70))
pin(canvas, CX0 + 315 + sig.width // 2, CY0 + 80, colour=PEACH)

# colour chips down the right edge, SABO style
chips = [
    ("PANTONE", PEACH, "162 C"),
    ("LIGHT", BAND["light"], None),
    ("MEDIUM", BAND["medium"], None),
    ("HEAVY", BAND["heavy"], None),
]
cy = CY0 + 36
for label, col, sub in chips:
    c = rotate(chip(label, col, sub), random.uniform(-2.5, 2.5))
    drop_shadow(canvas, c, (CX0 + CW - 150, cy))
    pin(canvas, CX0 + CW - 150 + c.width // 2, cy + 8, colour=TERRACOTTA if label != "PANTONE" else CHOC)
    cy += 172

# the three bands, hanging from pins
for name, x, deg in (("light", 330, 2), ("medium", 470, -1.5), ("heavy", 610, 1)):
    b = rotate(band(name, 470), deg)
    drop_shadow(canvas, b, (CX0 + x, CY0 + 250), offset=(8, 10), blur=10, opacity=130)
    pin(canvas, CX0 + x + b.width // 2, CY0 + 262, colour=CHOC)

# polaroids: friend's gym photos plus one Canva pick
polas = [
    (lucy_pic("12.39.24"), (CX0 + 20, CY0 + 290), -5, None, False),      # headshot
    (lucy_pic("12.40.34"), (CX0 + 20, CY0 + 540), 3, None, False),       # red set, Harbour Bridge
    (FRIEND / "sportif-lucyfriend-05-standing-kettlebell-rack.jpeg", (CX0 + 235, CY0 + 720), 4, None, False),
    (FRIEND / "sportif-lucyfriend-03-dumbbell-rack-foot-on-bench.jpeg", (CX0 + 445, CY0 + 780), -3, None, False),
    (lucy_pic("12.42.42"), (CX0 + 640, CY0 + 800), -4, None, True),      # side plank, landscape
    (CANVA, (CX0 + 545, CY0 + 24), 5, (0, 180, 1080, 1260), False),
]
for path, (x, y), deg, box, land in polas:
    p = rotate(polaroid(path, 170, box, land), deg)
    drop_shadow(canvas, p, (x, y), offset=(7, 9), blur=9, opacity=120)
    pin(canvas, x + p.width // 2, y + 12, colour=TERRACOTTA)

# caption under the board
cap = font("Italic", 40)
tw = d.textlength(CAPTION, font=cap)
d = ImageDraw.Draw(canvas)
d.text(((W - tw) / 2, TABLE_Y + 26), CAPTION, font=cap, fill=(0x7A, 0x5A, 0x48, 255))

# foreground: a band lying on the table in front of the board
fg = band("medium", 560).rotate(90, expand=True)
drop_shadow(canvas, fg, ((W - fg.width) // 2, H - fg.height - 26), offset=(4, 10), blur=10, opacity=140)

OUT.parent.mkdir(parents=True, exist_ok=True)
canvas.convert("RGB").save(OUT, quality=94)
print("wrote", OUT, canvas.size)
