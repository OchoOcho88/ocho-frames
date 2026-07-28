#!/usr/bin/env python3
"""Email 03: draped-arm 3-band shot (from scratch, gpt-image-2), AI model + our bands.

Original generation (not an edit of any reference photo): a woman's forearm with the three
Sportif bands draped over it, warm affordable-luxury palette. Answers Lucy's pg-3 look with
fully ownable imagery.

Output: email-03-band-photo/created/draped-arm_<quality>.png
    python3 clients/sportif/scripts-local/gen_draped_arm.py low
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
OUT = f'{REPO}/clients/sportif/email-03-band-photo/created'
QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'

PROMPT = (
 "A warm editorial product photograph, waist-up, of a woman in a simple cream ribbed tank top "
 "standing against a soft warm-taupe studio background. Her forearm is extended horizontally "
 "across the frame, and three folded ribbed-knit resistance booty bands are draped over her "
 "forearm, hanging down as soft loops: one warm oatmeal, one dusty blush, one terracotta clay, "
 "each with a small plain cream rubber label tab. Soft natural daylight, gentle shadows, "
 "affordable-luxury warm palette (blush peach, caramel tan, terracotta, cream). 35mm film "
 "photograph, subtle grain, realistic skin and fabric texture, calm and premium. No text, no "
 "words, no lettering, no logos anywhere."
)

r = requests.post('https://api.openai.com/v1/images/generations',
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    json={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536',
          'quality': QUALITY, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:400]}')
out = f'{OUT}/draped-arm_{QUALITY}.png'
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print('ok ->', out)
