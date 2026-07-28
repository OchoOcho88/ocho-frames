#!/usr/bin/env python3
"""Email 03, reference pg 1 recreated with OUR bands: 3 Sportif bands fanned/stacked, warm palette.

Uses our transparent band cutouts (light/medium/heavy), fans them in an overlapping stack with
soft drop shadows on a clean warm-cream ground, echoing the competitor hero shot Lucy referenced
but in the Sportif palette, no competitor logos. Clean product picture, no text overlay.

Sources: generated/images/product-bands/cutouts/band-{light,medium,heavy}-cutout.png
Output:  email-03-band-photo/created/ref1-3band-hero.png

    python3 clients/sportif/scripts-local/band_hero_ref1.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
CUT = ROOT / 'clients/sportif/generated/images/product-bands/cutouts'
OUT = ROOT / 'clients/sportif/email-03-band-photo/created/ref1-3band-hero.png'
OUT.parent.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1350
CREAM = (244, 236, 227)

canvas = Image.new('RGBA', (W, H), CREAM + (255,))

# subtle warm floor gradient (very soft, top lighter -> bottom a touch deeper) for a studio feel
grad = Image.new('L', (1, H))
for y in range(H):
    grad.putpixel((0, y), int(18 * y / H))
shade = Image.new('RGBA', (W, H), (198, 146, 110, 0))
shade.putalpha(grad.resize((W, H)))
canvas.alpha_composite(shade)


def place(name, cx, cy, target_h, rot=0):
    band = Image.open(CUT / name).convert('RGBA')
    scale = target_h / band.height
    band = band.resize((round(band.width * scale), target_h), Image.LANCZOS)
    if rot:
        band = band.rotate(rot, expand=True, resample=Image.BICUBIC)
    bw, bh = band.size
    x, y = int(cx - bw / 2), int(cy - bh / 2)
    # soft contact shadow
    sh = Image.new('RGBA', (bw, bh), (0, 0, 0, 0))
    sh = Image.composite(Image.new('RGBA', (bw, bh), (45, 33, 24, 255)),
                         sh, band.split()[3].point(lambda a: int(a * 0.38)))
    sh = sh.filter(ImageFilter.GaussianBlur(24))
    canvas.alpha_composite(sh, (x + 16, y + 30))
    canvas.alpha_composite(band, (x, y))


# fanned stack: light at back, heavy at front, staggered down-right so all 3 labels read
th = 600
ox, oy = 232, 74
place('band-light-cutout.png',  W / 2 - ox, H / 2 - oy, th)
place('band-medium-cutout.png', W / 2,      H / 2,      th)
place('band-heavy-cutout.png',  W / 2 + ox, H / 2 + oy, th)

canvas.convert('RGB').save(OUT)
print('ok ->', OUT.relative_to(ROOT), (W, H))
