#!/usr/bin/env python3
"""Swap a generated band's fake weave for the REAL band texture (S032).

Image models get the band's SHAPE, POSITION and LIGHTING right but render the fabric as fuzzy
towelling instead of our fine interlocking knit. This keeps everything the model got right and
replaces only the surface.

How it works: find the band (saturated, mid-dark, one big blob, widest rows only), tile the real
texture plate over it at the correct physical scale, then multiply that texture by the generated
plate's own blurred luminance so the original shading, curve and shadow all survive. The moulded
label is masked out and left untouched.

    python3 clients/sportif/scripts-local/retexture_band.py <plate.png> [weight] [out.png]

weight = light | medium | heavy (default heavy), picks the texture plate.
Works when the band is LARGE in frame. On a full-figure poster the band is too small to matter,
and there the label swap (D-013) is the job instead.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / 'brand/fonts/glacial-indifference').is_dir():
            return p
    raise SystemExit('could not locate the hyperframes root')


ROOT = find_root(Path(__file__).resolve())
TEX = ROOT / 'clients/sportif/assets/textures'


def retexture(plate_path, weight='heavy', out_path=None):
    src = Image.open(plate_path).convert('RGB')
    W, H = src.size
    a = np.array(src).astype(float)

    mx, mn = a.max(axis=2), a.min(axis=2)
    sat = np.divide(mx - mn, np.maximum(mx, 1))
    lum = a.mean(axis=2)

    # the band: saturated and mid-dark. The cream label is much lighter, so it drops out.
    band = (sat > 0.32) & (lum < 145) & (lum > 25)
    band = ndimage.binary_closing(band, np.ones((9, 9)))
    lab, n = ndimage.label(band)
    if n == 0:
        raise SystemExit('no band found: is it large enough in frame?')
    sizes = ndimage.sum(band, lab, range(1, n + 1))
    band = ndimage.binary_fill_holes(lab == (np.argmax(sizes) + 1))

    # keep only the rows where the blob is genuinely wide. This is what stops shadows between
    # the legs being treated as part of the band.
    rw = band.sum(axis=1)
    band &= (rw > rw.max() * 0.45)[:, None]

    # protect the moulded label
    label_px = (lum > 170) & (sat < 0.35)
    band &= ~ndimage.binary_dilation(label_px, np.ones((5, 5)))

    ys, _ = np.where(band)
    band_h = ys.max() - ys.min()

    # tile the real weave at the band's physical scale, running along its length
    tex = Image.open(TEX / f'texture-{weight}-plate.jpg').convert('RGB').rotate(90, expand=True)
    s = (band_h * 0.85) / tex.height
    tex = tex.resize((max(1, int(tex.width * s)), max(1, int(tex.height * s))), Image.LANCZOS)
    tile = Image.new('RGB', (W, H))
    for x in range(0, W, tex.width):
        for y in range(0, H, tex.height):
            tile.paste(tex, (x, y))
    t = np.array(tile).astype(float)

    # carry the generated shading across, so the band still curves and still casts its shadow
    gl = np.array(Image.fromarray(lum.astype('uint8')).filter(ImageFilter.GaussianBlur(11))).astype(float)
    tm = gl[band].mean()
    shade = np.clip(gl / max(tm, 1), 0.5, 1.6)[..., None]
    tl = t.mean(axis=2)
    newtex = np.clip(t * (tm / max(tl[band].mean(), 1)) * shade, 0, 255)

    alpha = ndimage.binary_erosion(band, np.ones((3, 3))).astype(float)
    alpha = np.array(Image.fromarray((alpha * 255).astype('uint8'))
                     .filter(ImageFilter.GaussianBlur(1.5))).astype(float) / 255.0
    out = (a * (1 - alpha[..., None]) + newtex * alpha[..., None]).astype('uint8')

    out_path = out_path or str(Path(plate_path).with_name(Path(plate_path).stem + '-retextured.png'))
    Image.fromarray(out).save(out_path)
    print('ok ->', out_path, f'(band {band_h}px tall, {band.sum()} px)')
    return out_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    retexture(sys.argv[1],
              sys.argv[2] if len(sys.argv) > 2 else 'heavy',
              sys.argv[3] if len(sys.argv) > 3 else None)
