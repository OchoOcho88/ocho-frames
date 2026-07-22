#!/usr/bin/env python3
"""Stamp the real SPORTIF label onto a band in a pilates in-use shot (gpt-image-2, two-image edit).

Passes the in-use photo AND the real label crop together so gpt reproduces the CORRECT text
instead of hallucinating it. Low quality leaves small sub-text ("MEDIUM") fuzzy; run HIGH from a
native Mac Terminal (the harness has a ~60s HTTPS cap) for crisp legible text:

    python3 clients/sportif/scripts-local/stamp_band_label.py squat medium high
    python3 clients/sportif/scripts-local/stamp_band_label.py glute-bridge heavy high
    python3 clients/sportif/scripts-local/stamp_band_label.py kickback light high

Args: <pose> <tier: heavy|medium|light> [quality: low|high]  (match tier to band colour:
terracotta->heavy, blush->medium, sand/caramel->light)."""
import base64, os, sys, requests

REPO='/Users/hugobrizuela/Desktop/hyperframes'
key=[l.strip().split('=',1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
DIR=f'{REPO}/clients/sportif/generated/images/band-inuse'

pose=sys.argv[1] if len(sys.argv)>1 else 'squat'
tier=sys.argv[2] if len(sys.argv)>2 else 'medium'
Q=sys.argv[3] if len(sys.argv)>3 else 'high'
base=f'{DIR}/inuse-{pose}_low.png'          # in-use scene (generated at low is fine as the base)
label=f'{DIR}/label-{tier}.png'             # real label crop
out=f'{DIR}/inuse-{pose}-labeled_{Q}.png'

prompt=(f"You are given a pilates photo (first image) and a real SPORTIF rubber label patch (second "
 f"image). Edit the FIRST image only: place that exact SPORTIF label patch onto the front face of the "
 f"fabric resistance band around her thighs, sized naturally and following the band's curve and the "
 f"scene's warm lighting. Keep the SPORTIF wordmark, the underline and the small word '{tier.upper()}' "
 f"crisp and perfectly legible exactly as shown in the label image. Change nothing else in the photo.")

files=[('image[]',('base.png',open(base,'rb'),'image/png')),
       ('image[]',('label.png',open(label,'rb'),'image/png'))]
r=requests.post('https://api.openai.com/v1/images/edits',
  headers={'Authorization':f'Bearer {key}'}, files=files,
  data={'model':'gpt-image-2','prompt':prompt,'size':'1024x1536','quality':Q,'output_format':'png'},
  timeout=560)
j=r.json()
if 'data' not in j: sys.exit(f'FAIL: {str(j)[:300]}')
open(out,'wb').write(base64.b64decode(j['data'][0]['b64_json'])); print('ok ->',out)
