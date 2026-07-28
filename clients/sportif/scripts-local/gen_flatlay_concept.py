#!/usr/bin/env python3
"""Email 03: a Sportif-only 'range concept' flat-lay (from scratch, gpt-image-2).

Lucy's pg-6 reference is a competitor's full-range flat-lay (ball, blocks, massage tools) we
cannot honestly copy with props that are not Sportif products. Instead we generate a warm,
minimal flat-lay of the 3 booty bands plus a couple of IMAGINARY Sportif range pieces
(ribbed pilates grip socks, a cotton pouch, a rolled towel) so Lucy sees the mood, entirely
our own imagery, no competitor photos, no logos.

Output: email-03-band-photo/created/flatlay-concept_<quality>.png
    python3 clients/sportif/scripts-local/gen_flatlay_concept.py low
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
OUT = f'{REPO}/clients/sportif/email-03-band-photo/created'
os.makedirs(OUT, exist_ok=True)
QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'

PROMPT = (
 "A top-down flat-lay product photograph of a minimalist Pilates accessories set in a warm "
 "affordable-luxury palette: blush peach, caramel tan, terracotta clay, warm oatmeal and "
 "cream. Arranged neatly with generous negative space on a soft warm-cream linen surface in "
 "gentle natural daylight with soft diffuse shadows. Include: three folded ribbed-knit "
 "resistance booty bands in oatmeal, dusty blush and terracotta, each with a small plain cream "
 "rubber label tab; a neatly folded pair of ribbed cream pilates grip socks; a small natural "
 "cotton drawstring pouch; and a rolled warm-beige cotton towel. Elegant editorial catalogue "
 "styling, 35mm film photograph, subtle grain, realistic soft fabric texture, calm and premium. "
 "Absolutely no text, no words, no lettering and no logos anywhere in the image."
)

r = requests.post('https://api.openai.com/v1/images/generations',
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    json={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536',
          'quality': QUALITY, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:400]}')
out = f'{OUT}/flatlay-concept_{QUALITY}.png'
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print('ok ->', out)
