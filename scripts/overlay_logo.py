#!/usr/bin/env python3
"""
overlay_logo.py: stamp the REAL Sportif logo lockup (SPORTIF in Glacial
Indifference Regular, tracking -0.059 em, plus the short underline rule)
onto an image. Geometry measured from assets/05-logo-sportif-white-on-peach.png.

Usage:
  python3 scripts/overlay_logo.py INPUT.png OUTPUT.png [width_frac] [y_center_frac] [color]
  defaults: 0.76 0.49 #F4F2EA  (use #4A433C warm charcoal on light backgrounds)
"""
from PIL import Image, ImageDraw, ImageFont
import sys

src, out = sys.argv[1], sys.argv[2]
target_w_frac = float(sys.argv[3]) if len(sys.argv) > 3 else 0.76
y_center_frac = float(sys.argv[4]) if len(sys.argv) > 4 else 0.49
color = sys.argv[5] if len(sys.argv) > 5 else "#F4F2EA"

TEXT = "SPORTIF"
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
FONT = str(ROOT / "brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf")
TRACK = -0.059        # em, matches measured logo tracking (tighter than natural)
RULE_W = 0.43         # underline width as fraction of wordmark width
RULE_T = 0.045        # underline thickness as fraction of cap height
RULE_GAP = 0.44       # gap wordmark-bottom to underline-top, fraction of cap height

img = Image.open(src).convert("RGB")
W, H = img.size
d = ImageDraw.Draw(img)

def metrics(size):
    f = ImageFont.truetype(FONT, size)
    sp = size * TRACK
    w = sum(d.textlength(c, font=f) + sp for c in TEXT) - sp
    b = d.textbbox((0, 0), TEXT, font=f)
    return w, b[3] - b[1], b[1], f, sp   # width, cap height, top offset, font, spacing

lo, hi = 10, 700
while lo < hi:
    mid = (lo + hi + 1) // 2
    if metrics(mid)[0] <= W * target_w_frac: lo = mid
    else: hi = mid - 1
w, ch, top_off, f, sp = metrics(lo)

rule_t = max(3, round(ch * RULE_T))
gap = ch * RULE_GAP
block_h = ch + gap + rule_t
block_top = H * y_center_frac - block_h / 2

x = (W - w) / 2
y = block_top - top_off
for c in TEXT:
    d.text((x, y), c, font=f, fill=color)
    x += d.textlength(c, font=f) + sp

rw = w * RULE_W
rx = (W - rw) / 2
ry = block_top + ch + gap
d.rectangle([rx, ry, rx + rw, ry + rule_t], fill=color)

img.save(out)
print(f"font={lo} wordmark={w:.0f}px ({w/W:.0%}) cap={ch}px rule={rw:.0f}x{rule_t}px")
