"""Recolour Lucy's peach logo files from the old #F0CDB3 to Pantone 162 C (#FFBE9F).

D-051 (S039, 2026-09-11): the primary brand colour is Pantone 162 C, screen hex
#FFBE9F. Her logo artwork was still the old peach, so the logo would have been
the one thing out of step. Each source is flat: peach plus one neutral (white
type, or a cream ground). Every pixel is projected onto the line from that
neutral to the old peach, and the peach share of it is moved to the new peach.
Anti-aliased edges keep their blend, the neutral stays untouched.

Originals in assets/ are never overwritten. Output: assets/logo-pantone-162c/.
Re-run: python3 clients/sportif/scripts-local/recolour_logos_162c.py
"""
import os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(ASSETS, "logo-pantone-162c")

OLD = np.array([0xF0, 0xCD, 0xB4], dtype=float)   # measured off her artwork
NEW = np.array([0xFF, 0xBE, 0x9F], dtype=float)   # Pantone 162 C, sRGB

# source file, the neutral it blends against, output name
JOBS = [
    ("05-logo-sportif-white-on-peach.png", (255, 255, 255), "SPORTIF-logo-white-on-peach-PANTONE162C.png"),
    ("07-logo-s-monogram.png",             (255, 255, 255), "SPORTIF-monogram-white-on-peach-PANTONE162C.png"),
    ("08-logo-sportif-peach-on-cream.png", (255, 251, 248), "SPORTIF-logo-peach-on-cream-PANTONE162C.png"),
    ("11-swatch-peach-nude.png",           (255, 255, 255), "SPORTIF-swatch-PANTONE162C.png"),
]


def recolour(src, neutral):
    im = Image.open(src).convert("RGBA")
    a = np.asarray(im).astype(float)
    rgb, alpha = a[..., :3], a[..., 3:]
    n = np.array(neutral, dtype=float)
    axis = OLD - n
    w = ((rgb - n) @ axis) / (axis @ axis)          # 0 at the neutral, 1 at the old peach
    w = np.clip(w, 0.0, 1.0)[..., None]
    out = np.clip(rgb + w * (NEW - OLD), 0, 255)
    return Image.fromarray(np.concatenate([out, alpha], axis=-1).round().astype(np.uint8))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, neutral, out_name in JOBS:
        img = recolour(os.path.join(ASSETS, name), neutral)
        img.save(os.path.join(OUT, out_name), optimize=True)
        print("wrote", out_name, img.size)
