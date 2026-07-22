#!/usr/bin/env python3
"""Turn the AI-imagined band held in a fresh-explore campaign shot into the REAL SPORTIF band.

Two-image gpt-image-2 edit: pass the campaign photo AND the real SPORTIF label crop so gpt
reproduces the correct label text on the band the model is holding, keeping her grip/pose/light.
Blush band = MEDIUM tier.

    python3 clients/sportif/scripts-local/realband_in_hand.py ch2_r_low
    python3 clients/sportif/scripts-local/realband_in_hand.py ch2_low high     # crisp, native Terminal
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
FE = f'{REPO}/clients/sportif/generated/images/fresh-explore'
LABEL = f'{REPO}/clients/sportif/generated/images/band-inuse/label-medium.png'

name = sys.argv[1] if len(sys.argv) > 1 else 'ch2_r_low'
Q = sys.argv[2] if len(sys.argv) > 2 else 'low'
base = f'{FE}/{name}.png'
out = f'{FE}/{name}_realband_{Q}.png'

prompt = (
 "You are given a photo of a woman with a soft blush fabric resistance booty band (first image) and "
 "a real SPORTIF rubber label patch (second image). Edit the FIRST image only: make that band a "
 "genuine SPORTIF band by placing the exact SPORTIF label patch onto the visible front face of the "
 "band (whether she is holding it in her hand or wearing it around her thighs), sized and angled "
 "naturally to follow the band's surface, curve and the scene's warm directional light and shadow. "
 "Keep the SPORTIF wordmark, its underline and the small word 'MEDIUM' crisp and perfectly legible, "
 "exactly as in the label image. Keep the band's soft blush knitted-fabric texture. Keep her body, "
 "hands, pose, outfit, the background, the light and the shadow all completely identical. Change "
 "nothing else in the photo.")

files = [('image[]', ('base.png', open(base, 'rb'), 'image/png')),
         ('image[]', ('label.png', open(LABEL, 'rb'), 'image/png'))]
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'}, files=files,
    data={'model': 'gpt-image-2', 'prompt': prompt, 'size': '1024x1536',
          'quality': Q, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL {name}: {str(j)[:300]}')
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print('ok ->', out)
