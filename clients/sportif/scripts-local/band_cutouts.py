#!/usr/bin/env python3
"""Cut the band product shots out onto TRANSPARENT PNGs for Hugo's Photoshop design.

Mattes each single band (light/medium/heavy) plus the joined 3-band flatlay off the peach
background using rembg (isnet-general-use), then trims to a tight alpha bounding box so each
file is a clean, ready-to-composite product cutout.

Source: generated/images/product-bands/bands-card-{light,medium,heavy}.png + bands-flatlay-peach_low.png
Output: generated/images/product-bands/cutouts/band-{light,medium,heavy}-cutout.png + bands-set-cutout.png

    python3 clients/sportif/scripts-local/band_cutouts.py
"""
import os
import numpy as np
from scipy.ndimage import distance_transform_edt
from PIL import Image
from rembg import remove, new_session

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
SRCDIR = f'{REPO}/clients/sportif/generated/images/product-bands'
OUT = f'{SRCDIR}/cutouts'
os.makedirs(OUT, exist_ok=True)

JOBS = [
    ('bands-card-light.png',        'band-light-cutout.png'),
    ('bands-card-medium.png',       'band-medium-cutout.png'),
    ('bands-card-heavy.png',        'band-heavy-cutout.png'),
    ('bands-flatlay-peach_low.png', 'bands-set-cutout.png'),
]

session = new_session('isnet-general-use')  # higher-quality general matting


def trim_alpha(im, pad=16):
    """Crop to the non-transparent bounding box, keeping a small transparent margin."""
    bbox = im.split()[3].getbbox()
    if not bbox:
        return im
    l, t, r, b = bbox
    l, t = max(0, l - pad), max(0, t - pad)
    r, b = min(im.width, r + pad), min(im.height, b + pad)
    return im.crop((l, t, r, b))


def clean_edges(im, floor=28, opaque_at=250):
    """Kill the faint background halo and decontaminate edge colour.

    1. Alpha floor: anything below `floor` becomes fully transparent (drops the faint
       peach fringe rembg leaves behind).
    2. Colour defringe: every non-opaque pixel's RGB is replaced with the colour of the
       nearest fully-opaque pixel (via an exact distance transform), so any remaining
       soft edge takes on band colour, never the peach background.
    """
    arr = np.array(im).astype(np.uint8)
    rgb, a = arr[..., :3], arr[..., 3].astype(np.int16)
    a[a < floor] = 0
    opaque = a >= opaque_at
    if opaque.any():
        idx = distance_transform_edt(~opaque, return_distances=False, return_indices=True)
        rgb = rgb[tuple(idx)]  # each pixel gets its nearest opaque colour
    out = np.dstack([rgb, a.astype(np.uint8)])
    return Image.fromarray(out, 'RGBA')


for src, dst in JOBS:
    im = Image.open(f'{SRCDIR}/{src}').convert('RGBA')
    cut = remove(im, session=session,
                 alpha_matting=True, alpha_matting_foreground_threshold=250,
                 alpha_matting_background_threshold=10, alpha_matting_erode_size=8)
    cut = clean_edges(cut)
    cut = trim_alpha(cut)
    cut.save(f'{OUT}/{dst}')
    print(f'ok {src} -> cutouts/{dst}  ({cut.width}x{cut.height})')
