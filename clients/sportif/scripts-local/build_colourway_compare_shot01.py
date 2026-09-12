#!/usr/bin/env python3
"""Q-025: the colourway compare for band placement shot 01, one variable changed.

Hugo built shot 01 in Photoshop with the LIGHT band (plates/01-floor-seated-work.psd).
This script lifts the exact placement, contact shadow and grade out of that PSD and
rebuilds the composite three times, once per colour-corrected cutout, so the only thing
that differs between the three frames is the band's colour. No AI touches the photo.

Outputs (never into created/, these are a judgement aid for Hugo, not deliverables):
    plates/colourway-compare/01-floor-seated-{LIGHT,MEDIUM,HEAVY}.jpg   full res, sRGB
    plates/colourway-compare/01-colourway-compare.jpg                   contact sheet

Needs psd_tools, which lives in the PDF venv:
    .venvs/pdf/bin/python clients/sportif/scripts-local/build_colourway_compare_shot01.py
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from psd_tools import PSDImage


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / 'brand/fonts/glacial-indifference').is_dir():
            return p
    raise SystemExit('could not locate the hyperframes root')


ROOT = find_root(Path(__file__).resolve())
SP = ROOT / 'clients/sportif'
JOB = SP / 'lucyfriend-band-placement'
SRC = SP / 'Lucy-Wayne-pictures/LUCYFRIENDGYM/Lucy Friend/sportif-lucyfriend-01-floor-seated.jpeg'
PSD = JOB / 'plates/01-floor-seated-work.psd'
CUTS = SP / 'assets/Sportif_Bands/Bands_background_removed/colour-corrected'
OUT = JOB / 'plates/colourway-compare'
FONT = ROOT / 'brand/fonts/glacial-indifference/GlacialIndifference-Bold.otf'

COLOURWAYS = ['LIGHT', 'MEDIUM', 'HEAVY']
ROTATION = 101           # PHOTOSHOP-GUIDE step 2 says -101 in Photoshop, where negative is
                         # counter-clockwise. Pillow's positive angle IS counter-clockwise, so
                         # the sign flips. Checked against the PSD layer: this sign matches.
GRADE = 0.80             # step 5, band drops about 20 percent
BLUR_PX, NOISE = 0.6, 0.025   # step 6


def alpha_bbox(im):
    return im.split()[-1].getbbox()


def crop_alpha(im):
    return im.crop(alpha_bbox(im))


def place_like_psd(cutout, target_size):
    """Rotate the way Hugo did, then fit to the exact pixel box the PSD band occupies."""
    c = crop_alpha(cutout.convert('RGBA'))
    r = c.rotate(ROTATION, resample=Image.BICUBIC, expand=True)
    r = crop_alpha(r)
    return r.resize(target_size, Image.LANCZOS)


def grade_and_grain(band):
    rgb = band.convert('RGB')
    rgb = ImageEnhance.Brightness(rgb).enhance(GRADE)
    rgb = rgb.filter(ImageFilter.GaussianBlur(BLUR_PX))
    a = np.asarray(rgb).astype(np.float32)
    rng = np.random.default_rng(41)
    noise = rng.normal(0, NOISE * 255, a.shape[:2]).astype(np.float32)[..., None]  # monochromatic
    a = np.clip(a + noise, 0, 255).astype(np.uint8)
    out = Image.fromarray(a).convert('RGBA')
    out.putalpha(band.split()[-1])
    return out


def luminance(im_rgb, mask):
    a = np.asarray(im_rgb.convert('L')).astype(np.float32)
    return float(a[mask].mean()) / 255 * 100


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    base = ImageOps.exif_transpose(Image.open(SRC)).convert('RGB')
    psd = PSDImage.open(PSD)
    assert base.size == psd.size, (base.size, psd.size)

    layers = {l.name: l for l in psd}
    band_layer = [l for l in psd if l.name.startswith('sportif-band')][0]
    contact = layers['contact']
    band_px = band_layer.topil().convert('RGBA')
    bb = alpha_bbox(band_px)
    target = (bb[2] - bb[0], bb[3] - bb[1])
    offset = (band_layer.bbox[0] + bb[0], band_layer.bbox[1] + bb[1])
    shadow = contact.topil().convert('RGBA')
    sa = shadow.split()[-1].point(lambda v: int(v * contact.opacity / 255))
    shadow.putalpha(sa)
    print(f'PSD band {band_layer.name}: box {target} at {offset}, shadow opacity {contact.opacity}')

    frames, crops, stats = {}, {}, {}
    pad = 260
    region = (offset[0] - pad, offset[1] - pad, offset[0] + target[0] + pad, offset[1] + target[1] + pad)
    for cw in COLOURWAYS:
        cut = Image.open(CUTS / f'sportif-band-{cw.lower()}-front-folded.png')
        placed = place_like_psd(cut, target)
        if cw == 'LIGHT':   # sanity: the pipeline should land on Hugo's own placement
            ref = crop_alpha(band_px).resize(target)
            diff = np.abs(np.asarray(placed.convert('L'), np.float32) - np.asarray(ref.convert('L'), np.float32))
            m = np.asarray(ref.split()[-1]) > 128
            print(f'LIGHT pipeline vs PSD layer: mean abs diff {diff[m].mean():.1f}/255 inside the band')
        band = grade_and_grain(placed)
        frame = base.copy()
        frame.paste(shadow, (contact.bbox[0], contact.bbox[1]), shadow)
        frame.paste(band, offset, band)
        frame.save(OUT / f'01-floor-seated-{cw}.jpg', quality=90)
        frames[cw] = frame
        crops[cw] = frame.crop(region)
        # separation: band luminance against the floor ring around it
        full_mask = np.zeros(base.size[::-1], bool)
        full_mask[offset[1]:offset[1] + target[1], offset[0]:offset[0] + target[0]] = np.asarray(band.split()[-1]) > 128
        ring = np.zeros_like(full_mask)
        ring[region[1]:region[3], region[0]:region[2]] = True
        ring &= ~full_mask
        stats[cw] = (luminance(frame, full_mask), luminance(frame, ring))
        print(f'{cw:6s} band {stats[cw][0]:.0f}%  floor {stats[cw][1]:.0f}%  separation {stats[cw][0] - stats[cw][1]:+.0f} points')

    # contact sheet: three columns, full frame on top, 100 percent crop underneath
    f = ImageFont.truetype(str(FONT), 44)
    cw_, ch_ = crops['LIGHT'].size
    fh = 900
    th = [fr.resize((int(fr.width * fh / fr.height), fh), Image.LANCZOS) for fr in frames.values()]
    col, gap = cw_, 40
    W = gap + (col + gap) * 3
    H = gap + 70 + fh + gap + 70 + ch_ + gap
    sheet = Image.new('RGB', (W, H), (246, 238, 229))
    d = ImageDraw.Draw(sheet)
    for i, (cw, t) in enumerate(zip(COLOURWAYS, th)):
        x = gap + i * (col + gap)
        b, fl = stats[cw]
        d.text((x, gap), f'{cw}   band {b:.0f}%  floor {fl:.0f}%  separation {b - fl:+.0f}', font=f, fill=(74, 67, 60))
        sheet.paste(t, (x + (col - t.width) // 2, gap + 70))
        y = gap + 70 + fh + gap
        d.text((x, y), f'{cw}, 100 percent', font=f, fill=(74, 67, 60))
        sheet.paste(crops[cw], (x, y + 70))
    sheet.save(OUT / '01-colourway-compare.jpg', quality=88)
    print('wrote', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
