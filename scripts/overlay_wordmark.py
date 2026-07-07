#!/usr/bin/env python3
"""
overlay_wordmark.py: stamp a letter-spaced wordmark in a real brand font
onto an image (typically an AI-generated photo made text-free on purpose).

Usage:
  python3 scripts/overlay_wordmark.py INPUT.png OUTPUT.png \
      [--text SPORTIF] [--font brand/fonts/glacial-indifference/GlacialIndifference-Bold.otf] \
      [--size 96] [--spacing 30] [--color "#4A433C"] [--y 0.10]

Defaults are the Sportif wordmark. --y is the vertical position as a
fraction of image height (0.10 = 10 percent from the top). Text is
horizontally centered.
"""

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent

p = argparse.ArgumentParser()
p.add_argument("input")
p.add_argument("output")
p.add_argument("--text", default="SPORTIF")
p.add_argument("--font", default=str(ROOT / "brand/fonts/glacial-indifference/GlacialIndifference-Bold.otf"))
p.add_argument("--size", type=int, default=96)
p.add_argument("--spacing", type=int, default=30)
p.add_argument("--color", default="#4A433C")
p.add_argument("--y", type=float, default=0.10)
a = p.parse_args()

img = Image.open(a.input).convert("RGB")
W, H = img.size
d = ImageDraw.Draw(img)
f = ImageFont.truetype(a.font, a.size)

w = sum(d.textlength(c, font=f) + a.spacing for c in a.text) - a.spacing
x = (W - w) / 2
y = H * a.y
for c in a.text:
    d.text((x, y), c, font=f, fill=a.color)
    x += d.textlength(c, font=f) + a.spacing

img.save(a.output)
print(f"Saved {a.output} ({W}x{H}), wordmark '{a.text}' at y={a.y:.0%}")
