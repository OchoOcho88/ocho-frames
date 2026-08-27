#!/usr/bin/env python3
"""The Sportif house grade (D-041, 2026-08-26).

Hugo asked for the photos to carry the brand colour. The first attempt was the obvious
one, brand peach laid over the frame, and it did almost nothing: the studio walls in
Lucy's photos already sit at the peach hue, so adding warmth had nothing to warm. It
also flattened the picture, because an overlay pours light grey-peach on everything.

What works is a TONE MAP, not an overlay. Every brightness level in the picture is given
a Sportif version of itself: the darks become the deep heavy-band brown, the mid-tones
become brand peach, the brightest end stays a warm white. Then it is mixed back toward
the original so it stays a photograph. Like printing on peach paper rather than taping a
peach sheet over the print. What it actually changes is the things that were NOT already
warm: grey leggings, black dumbbells, the brown ceiling beams. They join the family.

House strength is 0.45 (Hugo, 2026-08-26). Skin is held back 30 percent of the way so
nobody goes orange, which is the failure mode this look has.

Apply it to the PHOTO, before any type goes on, or the black wordmark turns brown.

Also exports a 3D LUT: `python3 sportif_grade.py` writes sportif-peach-45.cube next to
the brand assets, for Photoshop, Lightroom, Premiere and Resolve.
"""
import numpy as np

# Sportif ramp. DEEP is the measured HEAVY band (D-027) taken down a little so the
# darkest end still reads as shadow; MID is brand peach; TOP is a warm white.
DEEP = np.array([0x4A, 0x2C, 0x22], np.float32) / 255
MID = np.array([0xF0, 0xCD, 0xB3], np.float32) / 255
TOP = np.array([0xFF, 0xFA, 0xF4], np.float32) / 255

HOUSE_STRENGTH = 0.45
PIVOT = 0.62          # where the ramp hands over from DEEP->MID to MID->TOP


def lum(a):
    return a[..., 0] * 0.2126 + a[..., 1] * 0.7152 + a[..., 2] * 0.0722


def ramp(l):
    l = l[..., None]
    lo = DEEP + (MID - DEEP) * np.clip(l / PIVOT, 0, 1)
    hi = MID + (TOP - MID) * np.clip((l - PIVOT) / (1 - PIVOT), 0, 1)
    return np.where(l < PIVOT, lo, hi)


def peach_tone(a, amount=HOUSE_STRENGTH, contrast=0.10,
               dull_lift=0.18, dull_limit=0.24, black=0.008):
    """a is float RGB 0..1. amount 0 = untouched, 1 = full peach monotone.

    Three rules, each one learned the hard way on 2026-08-26. See the notes at the
    bottom of this file before changing any of them.

    1. COLOUR comes from the ramp, BRIGHTNESS stays with the photo. The ramp value is
       rescaled to each pixel's own luminance before mixing, so the hue moves and the
       tonal range does not.
    2. NO global saturation boost. Chroma is given only to pixels that were dull to
       begin with: anything already above dull_limit gains nothing. Skin is the most
       saturated warm thing in any of these frames, so a global boost tans it.
    3. Contrast stays light. A heavy S-curve darkens the shadow side of an arm and
       reads as fake tan just as fast as saturation does.
    """
    l = lum(a)
    t = ramp(l)
    t = t * (l / np.maximum(lum(t), 1e-5))[..., None]     # keep the photo's brightness
    out = np.clip(a * (1 - amount) + t * amount, 0, 1)
    out = np.clip((out - black) / (1 - black), 0, 1)      # black point back on zero

    L = lum(out)[..., None]
    S = np.clip(L + contrast * (L - 0.5) * (1 - np.abs(L - 0.5) * 2) * 2, 1e-5, 1)
    out = np.clip(out * (S / np.maximum(L, 1e-5)), 0, 1)

    g = lum(out)[..., None]                               # chroma for the dull only
    mx, mn = out.max(-1), out.min(-1)
    sat = np.where(mx > 1e-6, (mx - mn) / np.maximum(mx, 1e-6), 0)
    gain = 1 + dull_lift * np.clip((dull_limit - sat) / dull_limit, 0, 1)
    return np.clip(g + (out - g) * gain[..., None], 0, 1)


def grade_image(im, amount=HOUSE_STRENGTH):
    """PIL image in, graded PIL image out. Keeps the mode it was given."""
    from PIL import Image
    mode = im.mode
    a = np.asarray(im.convert('RGB'), np.float32) / 255.0
    g = (peach_tone(a, amount) * 255 + 0.5).astype(np.uint8)
    out = Image.fromarray(g)
    return out.convert(mode) if mode != 'RGB' else out


def write_cube(path, size=33, amount=HOUSE_STRENGTH):
    """Bake the grade into a 3D LUT so it can be reused outside this repo."""
    g = np.linspace(0, 1, size, dtype=np.float32)
    b, gg, r = np.meshgrid(g, g, g, indexing='ij')
    grid = np.stack([r, gg, b], -1).reshape(-1, 1, 3)
    out = peach_tone(grid, amount).reshape(-1, 3)
    with open(path, 'w') as f:
        f.write(f'TITLE "Sportif peach {int(round(amount*100))}"\n')
        f.write(f'LUT_3D_SIZE {size}\nDOMAIN_MIN 0 0 0\nDOMAIN_MAX 1 1 1\n')
        for px in out:
            f.write('%.6f %.6f %.6f\n' % tuple(px))
    return path


if __name__ == '__main__':
    from pathlib import Path
    root = Path(__file__).resolve().parents[3]
    dest = root / 'clients/sportif/assets/luts'
    dest.mkdir(parents=True, exist_ok=True)
    for amt in (0.25, 0.45, 0.70):
        p = write_cube(dest / f'sportif-peach-{int(amt*100)}.cube', 33, amt)
        print('wrote', p)


# ---------------------------------------------------------------------------
# Two dead ends, kept because both are easy to walk back into.
#
# D-042: the grade must not touch brightness. The first build mixed the ramp colour in
# brightness and all. Because the ramp's dark end is #4A2C22, a mid brown rather than a
# black, every shadow got lifted toward it: the black point on story-duo went from 0.024
# to 0.094, four times lighter, and the whole set read washed out and lifeless. Hugo
# called it on sight. Rule: tint the hue, never the tone. If a grade lifts the black
# point, that is a mistake, not a look.
#
# D-043: on these photos, more peach and tanned skin are the SAME slider. Her skin and
# the studio wall both sit near hue 25 degrees, so nothing that warms the wall can leave
# her alone. A hue-based skin mask is no help either: on feed-ballreach it selected 91
# percent of the frame, because the wall qualifies as skin. The second build tried to
# compensate with a saturation boost and a heavy S-curve for punch, and both land hardest
# on the most saturated warm thing in frame, which is her. It read as fake tan. Hugo
# called that one too. What survives: no global saturation, light contrast, chroma only
# for what was dull. That caps how strong this look can go, and the cap is the honest
# answer rather than a setting to be tuned around. The only way past it is cutting the
# person out and grading the room separately, which was considered and not taken.
