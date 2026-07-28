#!/usr/bin/env python3
"""Stamp the real SPORTIF label onto the blank tabs of the email-03 generated band shots.

Two-image gpt-image-2 edit: pass the scene + the real SPORTIF label crop so gpt reproduces the
correct wordmark instead of hallucinating it, filling each band's existing blank cream tab and
following its angle + the scene lighting. LIGHT->oatmeal, MEDIUM->blush, HEAVY->terracotta.

    python3 clients/sportif/scripts-local/stamp_label_e03.py draped-arm_low low
    python3 clients/sportif/scripts-local/stamp_label_e03.py flatlay-concept_low low
Low works in-harness (may leave the small size word soft); run high from a native Terminal for crisp.
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
CREATED = f'{REPO}/clients/sportif/email-03-band-photo/created'
LABEL = f'{REPO}/clients/sportif/generated/images/band-inuse/label-medium.png'

name = sys.argv[1] if len(sys.argv) > 1 else 'draped-arm_low'
Q = sys.argv[2] if len(sys.argv) > 2 else 'low'
base = f'{CREATED}/{name}.png'
out = f'{CREATED}/{name}-sportif_{Q}.png'

PROMPT = (
 "You are given a product photo (first image) showing three ribbed resistance bands, each with a "
 "small BLANK cream rubber label tab, and a real SPORTIF rubber label patch (second image). Edit "
 "the FIRST image only: on each band's existing blank tab, add the raised white SPORTIF wordmark "
 "and the short underline rule exactly in the style, colour and finish of the SPORTIF label patch "
 "shown, following each tab's angle, curve and the scene's soft warm lighting. Beneath the "
 "underline add the size in small white caps: LIGHT on the pale oatmeal band, MEDIUM on the dusty "
 "blush band, HEAVY on the terracotta band. Keep the SPORTIF wordmark and underline crisp and "
 "legible. Change nothing else in the image, keep the bands, background and any skin exactly as is."
)

files = [('image[]', ('base.png', open(base, 'rb'), 'image/png')),
         ('image[]', ('label.png', open(LABEL, 'rb'), 'image/png'))]
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'}, files=files,
    data={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536',
          'quality': Q, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:300]}')
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print('ok ->', out)
