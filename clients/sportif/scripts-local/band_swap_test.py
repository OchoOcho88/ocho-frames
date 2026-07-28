#!/usr/bin/env python3
"""EXPERIMENT: give gpt-image-2 the scene + our real hero bands, ask it to swap the bands in.

Two-image edit. Tests whether passing our finished 3-band hero (with the correct SPORTIF label)
as a reference lets gpt replace the bands in a scene with our real product + true label, instead
of us stamping the label ourselves. Saved to a separate test batch for comparison.

    python3 clients/sportif/scripts-local/band_swap_test.py draped-arm_low low
    python3 clients/sportif/scripts-local/band_swap_test.py flatlay-concept_low low
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
CREATED = f'{REPO}/clients/sportif/email-03-band-photo/created'
HERO = f'{CREATED}/ref1-3band-hero.png'          # our real bands w/ correct SPORTIF label

scene = sys.argv[1] if len(sys.argv) > 1 else 'draped-arm_low'
Q = sys.argv[2] if len(sys.argv) > 2 else 'low'
base = f'{CREATED}/{scene}.png'
out = f'{CREATED}/band-swap-test/{scene}-swapped_{Q}.png'

PROMPT = (
 "You are given a scene photo (first image) that contains three ribbed resistance bands, and a "
 "product photo of the three real SPORTIF bands (second image). Edit the FIRST image only: make "
 "the three bands in the scene match the SPORTIF bands from the second image exactly, their "
 "ribbed knit texture, the oatmeal, dusty-blush and terracotta colours, and especially the cream "
 "rubber label with the raised white SPORTIF wordmark, the underline rule and the size word. "
 "Reproduce the SPORTIF wordmark crisp, correctly spelled and legible, exactly as in the second "
 "image. Keep the composition, any person, hands, pose, background and lighting of the first "
 "image exactly the same. Change only the bands to be SPORTIF bands."
)

files = [('image[]', ('scene.png', open(base, 'rb'), 'image/png')),
         ('image[]', ('hero.png', open(HERO, 'rb'), 'image/png'))]
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'}, files=files,
    data={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536',
          'quality': Q, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:300]}')
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print('ok ->', out)
