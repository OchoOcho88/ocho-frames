#!/usr/bin/env python3
"""Cut the generated flicked band out of its wall with real transparency (S046).

Hugo masked the band in with a soft brush, which carries a blob of the GENERATED wall with it:
1 to 2 levels lighter than the plate and grainy, so it halos, and it shows at once on any other
ground (the peach room, a story extension, print). The generated wall is one flat colour, so
the band can be unmixed from it instead of masked:

  alpha   solid band (and anything it encloses, like the label) = 1; the wall = 0; the motion
          blur and the antialiased edge get a partial alpha from how far each pixel sits from
          the wall colour toward the local band colour
  colour  the wall is subtracted back out of every partial pixel (colour decontamination), so
          the blur trail is see-through brown, not brown mixed with off-white

Input : generated/images/pilates-flick/photoshop/band-layer-v3-4-1080x1350.png
Output: generated/images/pilates-flick/photoshop/band-cutout-v3-4-1080x1350.png (RGBA, the
        plate's canvas, band in place, so it drops in at 0,0 like the layer it replaces)

    python3 clients/sportif/scripts-local/cutout_flick_band.py
"""
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

PS = Path('/Users/hugobrizuela/Desktop/hyperframes/clients/sportif/generated/images/pilates-flick/photoshop')
SRC = PS / 'band-layer-v3-4-1080x1350.png'
OUT = PS / 'band-cutout-v3-4-1080x1350.png'

ROI = (600, 30, 1020, 360)   # x0, y0, x1, y1: the band and its trail, with margin
T_WALL = 14                  # "looks like wall" for finding the see-through hole in the loop
T_SOLID = 70                 # clearly band
HOLE_MIN = 150               # an enclosed wall-like area bigger than this is the loop's hole


def main():
    im = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float64)
    H, W, _ = im.shape
    x0, y0, x1, y1 = ROI
    roi = im[y0:y1, x0:x1]

    # the generated wall colour, from the ROI's border ring (all wall)
    ring = np.concatenate([roi[:8].reshape(-1, 3), roi[-8:].reshape(-1, 3),
                           roi[:, :8].reshape(-1, 3), roi[:, -8:].reshape(-1, 3)])
    B = np.median(ring, axis=0)
    d = np.linalg.norm(roi - B, axis=2)

    # background: wall-like areas touching the ROI edge, plus any big enclosed one (the loop hole)
    lab, n = ndi.label(d < T_WALL)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    sizes = ndi.sum(np.ones_like(d), lab, index=np.arange(1, n + 1))
    bg = np.zeros_like(d, bool)
    for k in range(1, n + 1):
        if k in border or sizes[k - 1] > HOLE_MIN:
            bg |= lab == k

    # interior: the solid band closed and hole-filled (label and highlights included), minus bg
    solid = d > T_SOLID
    enclosed = bg & ~np.isin(lab, list(border))           # the loop's see-through hole
    interior = ndi.binary_fill_holes(ndi.binary_closing(solid, iterations=3))
    # keep the hole and its antialiased rim OUT of the interior, so the rim gets a partial
    # alpha instead of full alpha on a wall-mixed colour (that showed as a light line)
    interior &= ~ndi.binary_dilation(enclosed, iterations=3) & ~bg
    interior = ndi.binary_erosion(interior, iterations=1)

    # local band colour F for the partial pixels: blurred average of nearby solid pixels
    w = ndi.gaussian_filter(solid.astype(float), 12)
    F = np.stack([ndi.gaussian_filter(roi[..., c] * solid, 12) for c in range(3)], -1)
    glob = roi[solid].mean(axis=0)
    F = np.where(w[..., None] > 1e-3, F / np.maximum(w[..., None], 1e-6), glob)

    # partial alpha: projection of (C - B) onto (F - B)
    FB = F - B
    a = np.einsum('ijk,ijk->ij', roi - B, FB) / np.maximum(np.einsum('ijk,ijk->ij', FB, FB), 1e-6)
    a = np.clip(a, 0, 1)
    # grain is wall, not band: a soft ramp from 5 to 12 levels instead of a hard cut, so the
    # faint end of the blur trail fades out rather than stopping on a line
    a *= np.clip((d - 5) / 7, 0, 1)
    # only the enclosed hole is forced to zero; the open wall is left to the ramp (forcing it
    # clipped the faint end of the trail on a hard line), limited to 30px around the band so
    # stray grain further out cannot pick up a whisper of alpha
    near = ndi.binary_dilation(solid, iterations=30)
    a[~near] = 0
    a[interior] = 1
    a[enclosed] = 0
    a[a <= 0.02] = 0

    # colour decontamination: take the wall back out of every partial pixel
    safe = np.maximum(a, 1e-3)[..., None]
    fg = np.clip(B + (roi - B) / safe, 0, 255)
    fg = np.where(a[..., None] > 0.02, fg, 0)

    out = np.zeros((H, W, 4), np.uint8)
    out[y0:y1, x0:x1, :3] = np.round(fg).astype(np.uint8)
    out[y0:y1, x0:x1, 3] = np.round(a * 255).astype(np.uint8)
    Image.fromarray(out).save(OUT)
    part = ((a > 0) & (a < 1)).sum()
    hole = int(enclosed.sum())
    print(f'wall colour {B.round(1)}, solid px {int((a == 1).sum())}, partial px {int(part)}, '
          f'enclosed wall (loop hole) cleared: {hole} px')
    print('ok ->', OUT.name)


if __name__ == '__main__':
    main()
