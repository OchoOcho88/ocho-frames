#!/usr/bin/env python3
"""The pilates picture with a band flicked off her raised foot (Lucy's Canva note, 22 Sep).

Lucy's note on page 1 of the shared Canva: "add booty band as its like she is flicking the
booty band off. Keep the background colour as is." Her arc runs from the toe tip up and to
the right. Hugo's call (S046): try a generator first, with our real band and the photo as
references, and he composites the band onto the untouched plate in Photoshop. That keeps
the model's photo pixel-identical in the final: only the band's pixels come from here.

Inputs (sent to images/edits in this order, the prompt names them by position):
  1. the plate: reference-images/lucy-canva-picks/lucy-pilates-ref-noweights.png
     (weights removed at Lucy's earlier request; her background, no grade, no peach room)
  2. the HEAVY band, label side, from the colour-corrected cutouts (D-039)
  3. the HEAVY band, inside with the grip stripes, tone-matched to the measured HEAVY
     colour (D-027) because the raw photo is about a stop dark

Output: generated/images/pilates-flick/<model>-<quality>-<prompt>-<n>.png at the plate's 4:5, plus
the two band references in refs/ so the run is reproducible.

    python3 clients/sportif/scripts-local/gen_pilates_flick.py [model] [quality] [n] [v1|v2|v3]
    model: sunburst (default) | flare | gpt-image-2
"""
import base64, io, math, sys, time
from pathlib import Path

import requests
from PIL import Image

REPO = Path('/Users/hugobrizuela/Desktop/hyperframes')
SP = REPO / 'clients/sportif'
key = [l.strip().split('=', 1)[1] for l in open(REPO / '.env') if l.startswith('OPENAI_API_KEY=')][0]

PLATE = SP / 'reference-images/lucy-canva-picks/lucy-pilates-ref-noweights.png'
BAND_LABEL = SP / 'assets/Sportif_Bands/Bands_background_removed/colour-corrected/sportif-band-heavy-front-folded.png'
BAND_INSIDE = SP / 'assets/Sportif_Bands/sportif-band-heavy-inside-grip-a.png'
OUT = SP / 'generated/images/pilates-flick'
REFS = OUT / 'refs'

MODELS = {'sunburst': 'gpt-image-2.5-sunburst', 'flare': 'gpt-image-2.5-flare',
          'gpt-image-2': 'gpt-image-2'}
MODEL = MODELS[sys.argv[1] if len(sys.argv) > 1 else 'sunburst']
QUALITY = sys.argv[2] if len(sys.argv) > 2 else 'medium'
N = int(sys.argv[3]) if len(sys.argv) > 3 else 3
PV = sys.argv[4] if len(sys.argv) > 4 else 'v2'
SIZE = '1088x1360'          # the plate's 4:5, both sides multiples of 16

HEAVY = (0x6C, 0x43, 0x33)  # D-027, measured
REF_BG = (245, 242, 238)    # neutral light ground for the product refs


def flatten(im, bg=REF_BG):
    im = im.convert('RGBA')
    base = Image.new('RGBA', im.size, bg + (255,))
    base.alpha_composite(im)
    return base.convert('RGB')


def tone_match_fabric(im_rgba, target):
    """Per-channel gamma (as build_texture_weight_tiles.tone_match) with the mean taken over
    the knit only: opaque, saturated pixels, so the grey grip stripes do not drag it down."""
    px = list(im_rgba.convert('RGBA').resize((120, 440), Image.LANCZOS).getdata())
    fab = [p for p in px if p[3] > 200 and p[0] - p[2] > 25]
    lut = []
    for c in range(3):
        cur = min(max(sum(p[c] for p in fab) / len(fab), 1.0), 254.0)
        g = math.log(target[c] / 255.0) / math.log(cur / 255.0)
        lut += [min(255, round(255 * (v / 255.0) ** g)) for v in range(256)]
    r, g_, b, a = im_rgba.convert('RGBA').split()
    rgb = Image.merge('RGB', (r, g_, b)).point(lut)
    return Image.merge('RGBA', (*rgb.split(), a)), len(fab)


def fit(im, box=1024):
    im = im.copy()
    im.thumbnail((box, box), Image.LANCZOS)
    return im


def png_bytes(im):
    b = io.BytesIO(); im.save(b, 'PNG'); b.seek(0); return b


PROMPT_V1 = (
    "Edit Image 1, a studio photograph of a woman in a single-leg glute bridge with her feet on "
    "a tan ball and one leg raised straight up, toes pointed. "
    "Add exactly one fabric booty band flying through the air just above and to the right of the "
    "toes of her raised foot, as if she flicked it off her toes a split second ago and it is "
    "travelling up and to the right on a rising arc, away from her foot. Keep it close enough to "
    "the toes that the flick reads, with a small gap of clear background between toes and band. "
    "In mid-air the band is a closed loop that is NOT being worn and NOT stretched: a loose, "
    "slightly twisted and flattened oval, tumbling, seen at an angle so both the outer face and "
    "a little of the inside of the loop are visible. Realistic size: the loop's length is about "
    "the length of her foot from heel to toe. A light motion blur on the trailing edge nearest her "
    "toes only; the label stays sharp. "
    "Images 2 and 3 are the real product and the only source for how it looks. Image 2 is the "
    "outer face: a thick, fine, matte interlocking knit in deep terracotta brown, with a flat "
    "cream-gold rubber label reading SPORTIF over a thin rule and the word HEAVY. Image 3 is the "
    "inside of the same band: the same brown knit with two dark charcoal grip stripes running its "
    "full length. Match the colour, knit texture, width, proportions, stripes and label exactly. "
    "Do not invent a different band, colour, logo or any other text. "
    "Keep everything else in Image 1 exactly as it is: the woman, her skin, her pose, both feet "
    "and every toe, the beige shorts, the tan ball, her hands, the plain warm beige background "
    "colour and its fine grain, the framing. No ankle weights, no other objects, no text, no "
    "motion lines, no cast shadow on the background (the band is in the air, far from the wall). "
    "Light the band with the same soft, even studio light as the photograph."
)

# v2 (S046): v1 drew the knit as pebbled leather, the label in invented letterforms, every
# band as a tidy upright oval, and pushed it against the top edge with ghost streaks.
PROMPT_V2 = (
    "Edit Image 1, a studio photograph of a woman in a single-leg glute bridge with her feet on "
    "a tan ball and one leg raised straight up, toes pointed. "
    "Add exactly one fabric booty band in mid-air, as if she flicked it off her toes a split "
    "second ago. It has just left her foot and is travelling up and to the right on a rising arc. "
    "Position: its centre about one and a half foot-lengths from the tip of her big toe, up and "
    "to the right, and well clear of the top edge of the frame (at least a fifth of the frame "
    "height of clear background above it). "
    "Shape: a closed loop that is not being worn and not stretched, caught mid-tumble. It is "
    "loose and soft, twisted a quarter to a half turn along its length and bent, one end nearer "
    "the camera than the other, the way fabric looks when thrown. Not a neat upright oval and "
    "not a product standing on its edge. Realistic size: the loop's length is about the length "
    "of her foot from heel to toe. "
    "Motion: a short, soft blur on the trailing edge nearest her toes only. No ghost copies, no "
    "speed streaks, no motion lines. The label side is sharp. "
    "Images 2 and 3 are the real product and the only source for how it looks. Image 2 is the "
    "outer face, Image 3 the inside. The fabric is a tight, fine interlocking knit elastic webbing "
    "with a small regular knitted grain, matte, in deep terracotta brown, exactly as in Images 2 "
    "and 3. It is NOT leather, NOT suede, NOT pebbled, NOT towelling, NOT felt. The outer face "
    "carries one flat rectangular cream-gold rubber label, facing the camera. The inside carries "
    "two dark charcoal grip stripes running its full length. Match the colour, knit, width, "
    "proportions, stripes and label exactly. Do not invent a different band, colour, logo or "
    "any other text. "
    "Keep everything else in Image 1 exactly as it is: the woman, her skin, her pose, both feet "
    "and every toe, the beige shorts, the tan ball, her hands, the plain warm beige background "
    "colour and its fine grain, the framing. No ankle weights, no other objects, no text, no "
    "cast shadow on the background (the band is in the air, far from the wall). Light the band "
    "with the same soft, even studio light as the photograph."
)

# v3 (S046): v2 fixed the knit and the tumble, but every variant turned the label 90 degrees.
# On the real band the label's long side runs ACROSS the strap (583px of a 776px strap, D-027
# cutouts), so SPORTIF reads across the band's width, never along its length.
PROMPT_V3 = PROMPT_V2.replace(
    "The outer face carries one flat rectangular cream-gold rubber label, facing the camera. ",
    "The outer face carries one flat, matte, rectangular cream-gold rubber label, facing the "
    "camera. The label is oriented exactly as in Image 2: its long side runs ACROSS the width of "
    "the strap, perpendicular to the band's length, and it covers about three quarters of the "
    "strap's width, so the word SPORTIF reads across the strap, never along it. ")
assert PROMPT_V3 != PROMPT_V2
PROMPTS = {'v1': PROMPT_V1, 'v2': PROMPT_V2, 'v3': PROMPT_V3}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    REFS.mkdir(parents=True, exist_ok=True)

    plate = Image.open(PLATE).convert('RGB')
    label_ref = fit(flatten(Image.open(BAND_LABEL)))
    inside_rgba, nfab = tone_match_fabric(Image.open(BAND_INSIDE), HEAVY)
    inside_ref = fit(flatten(inside_rgba))
    label_ref.save(REFS / 'ref-2-heavy-label.png')
    inside_ref.save(REFS / 'ref-3-heavy-inside.png')
    print(f'refs ok (inside tone-matched on {nfab} knit samples)')

    files = [('image[]', ('plate.png', png_bytes(plate), 'image/png')),
             ('image[]', ('band-label.png', png_bytes(label_ref), 'image/png')),
             ('image[]', ('band-inside.png', png_bytes(inside_ref), 'image/png'))]
    data = {'model': MODEL, 'prompt': PROMPTS[PV], 'size': SIZE, 'quality': QUALITY,
            'n': str(N), 'output_format': 'png'}
    t0 = time.time()
    r = requests.post('https://api.openai.com/v1/images/edits',
                      headers={'Authorization': f'Bearer {key}'},
                      files=files, data=data, timeout=900)
    j = r.json()
    if 'data' not in j:
        sys.exit(f'FAIL after {time.time() - t0:.0f}s: {str(j)[:600]}')
    tag = MODEL.replace('gpt-image-', '').replace('2.5-', '')
    for i, d in enumerate(j['data'], 1):
        im = Image.open(io.BytesIO(base64.b64decode(d['b64_json']))).convert('RGB')
        p = OUT / f'{tag}-{QUALITY}-{PV}-{i}.png'
        im.save(p)
        print('ok ->', p.relative_to(REPO), im.size)
    print(f'{time.time() - t0:.0f}s, usage: {j.get("usage")}')


if __name__ == '__main__':
    main()
