#!/usr/bin/env python3
"""Stage 2: cut each real band from the flatlay into its own 4:5 hero card on peach.

Faithful crops (no fabrication) of the generated flatlay, recomposed onto a 1088x1360
IG-ready peach canvas. Re-run after regenerating the flatlay.
"""
import os
from PIL import Image

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
DIR = f'{REPO}/clients/sportif/generated/images/product-bands'
flat = Image.open(f'{DIR}/bands-flatlay-peach_low.png').convert('RGB')
W, H = flat.size  # 1536x1024

# sample the peach background from a corner so the card padding matches exactly
bg = flat.getpixel((20, 20))

# band column crops, inset just clear of the seams so no neighbour bleeds in.
# True edges (texture+colour detected): HEAVY 193-592, MEDIUM 592-976, LIGHT 977-1369.
COLS = {
    'heavy':  (205, 586),   # left = true outer edge (+a little), right stops before the H/M seam
    'medium': (600, 970),   # both edges inset off the seams
    'light':  (986, 1360),  # left inset off the M/L gap, right = true outer edge
}
Y0, Y1 = 200, 862

CARD_W, CARD_H = 1088, 1360   # 4:5 IG
for name, (x0, x1) in COLS.items():
    crop = flat.crop((x0, Y0, x1, Y1))
    # scale the band so it sits at ~66% of the card height, centred
    target_h = int(CARD_H * 0.66)
    scale = target_h / crop.height
    cw, ch = int(crop.width * scale), target_h
    crop = crop.resize((cw, ch), Image.LANCZOS)
    card = Image.new('RGB', (CARD_W, CARD_H), bg)
    card.paste(crop, ((CARD_W - cw) // 2, (CARD_H - ch) // 2))
    out = f'{DIR}/bands-card-{name}.png'
    card.save(out)
    print(f'ok {name} -> {out}  (bg {bg})')
