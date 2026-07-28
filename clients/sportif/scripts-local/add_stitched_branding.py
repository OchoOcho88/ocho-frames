#!/usr/bin/env python3
"""EXPERIMENT: add a stitched-on SPORTIF to the other flat-lay products (towel/socks/pouch).

Two-image edit: the labelled-band flat-lay + our SPORTIF reference, asking gpt to add subtle
embroidered/woven SPORTIF branding to the soft goods so the set reads as one collection.

    python3 clients/sportif/scripts-local/add_stitched_branding.py low
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
CREATED = f'{REPO}/clients/sportif/email-03-band-photo/created'
BASE = f'{CREATED}/band-swap-test/flatlay-concept_low-swapped_low.png'   # bands already labelled
REF = f'{CREATED}/ref1-3band-hero.png'
Q = sys.argv[1] if len(sys.argv) > 1 else 'low'
out = f'{CREATED}/band-swap-test/flatlay-branded_{Q}.png'

PROMPT = (
 "You are given a flat-lay (first image) and a SPORTIF product photo (second image). Edit the "
 "FIRST image only: add subtle SPORTIF branding to the OTHER products so they read as one "
 "matching set. On the rolled towel add a small woven SPORTIF label near its edge. On the "
 "ribbed grip socks add a small tonal embroidered SPORTIF wordmark on the cuff. On the cream "
 "cotton pouch add a small stitched SPORTIF wordmark centred. Every SPORTIF wordmark must be "
 "crisp, correctly spelled and legible, in a subtle raised embroidered/stitched style, tonal "
 "and understated in the warm palette. Do NOT change the three bands, their labels, the layout, "
 "the background or the lighting."
)

files = [('image[]', ('base.png', open(BASE, 'rb'), 'image/png')),
         ('image[]', ('ref.png', open(REF, 'rb'), 'image/png'))]
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'}, files=files,
    data={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536',
          'quality': Q, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:300]}')
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print('ok ->', out)
