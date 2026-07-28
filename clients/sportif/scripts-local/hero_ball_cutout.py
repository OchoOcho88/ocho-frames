#!/usr/bin/env python3
"""Clean cutout of the ball-overhead figure (hard matte: white bra + white ball on a light wall).

rembg, then: alpha floor to kill the soft ghost/smear, fill only SMALL holes (the bra) but NOT
the large enclosed gap between her raised arms, keep the main figure component, and defringe.

Output: generated/images/poster-experiment/hero-ball-cut.png (+ a checker preview in scratchpad)
    python3 clients/sportif/scripts-local/hero_ball_cutout.py
"""
import numpy as np
from pathlib import Path
from scipy import ndimage
from scipy.ndimage import distance_transform_edt
from PIL import Image
from rembg import remove, new_session

ROOT = Path('/Users/hugobrizuela/Desktop/hyperframes')
REF = ROOT / 'clients/sportif/reference-images/lucy-canva-picks'
OUT = ROOT / 'clients/sportif/generated/images/poster-experiment/hero-ball-cut.png'
SCR = Path('/private/tmp/claude-501/-Users-hugobrizuela-Desktop-hyperframes/2cb1d5b4-55d8-4929-be7f-02ccd33c93b9/scratchpad')

cut = remove(Image.open(REF / 'lucy-studio-ball-overhead-back.png').convert('RGBA'),
             session=new_session('isnet-general-use'),
             alpha_matting=True, alpha_matting_foreground_threshold=250,
             alpha_matting_background_threshold=8, alpha_matting_erode_size=4)
arr = np.array(cut)
a = arr[..., 3].astype(np.int16)
a[a < 36] = 0                                   # kill the soft ghost smear
mask = a > 96

# keep the main figure component(s), drop stray blobs
lbl, n = ndimage.label(mask)
if n:
    sizes = ndimage.sum(np.ones_like(lbl), lbl, range(1, n + 1))
    keep = np.where(sizes > 0.01 * mask.size)[0] + 1
    mask = np.isin(lbl, keep)

# fill ONLY small holes (bra); leave the big between-arms gap as background
filled = ndimage.binary_fill_holes(mask)
new = filled & ~mask
nl, nn = ndimage.label(new)
if nn:
    nsz = ndimage.sum(np.ones_like(nl), nl, range(1, nn + 1))
    small = np.where(nsz < 0.004 * mask.size)[0] + 1     # small holes only
    mask = mask | np.isin(nl, small)

# compose final alpha: soft edges preserved, small holes opaque, everything else cleared
holes = mask & (a < 96)
a[~mask] = 0
a[holes] = 255
arr[..., 3] = a.astype(np.uint8)

# defringe: recolour non-opaque pixels to nearest opaque colour so edges aren't wall-tinted
rgb = arr[..., :3]
opaque = a >= 250
if opaque.any():
    idx = distance_transform_edt(~opaque, return_distances=False, return_indices=True)
    arr[..., :3] = rgb[tuple(idx)]

out = Image.fromarray(arr, 'RGBA')
out = out.crop(out.split()[3].getbbox())
out.save(OUT)

# checker preview
w, h = out.size
chk = Image.new('RGB', (w, h), (70, 90, 110)); px = chk.load()
for y in range(h):
    for x in range(w):
        if ((x // 26) + (y // 26)) % 2 == 0: px[x, y] = (45, 60, 75)
chk.paste(out, (0, 0), out); chk.thumbnail((520, 720)); chk.save(SCR / 'hero_ball_clean_chk.png')
print('ok ->', OUT.name, out.size)
