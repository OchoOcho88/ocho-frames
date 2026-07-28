#!/usr/bin/env python3
"""Retouch a reskin plate to remove the WORN band from the model's thigh.

Lucy's email #1 ask (updated): keep the ORIGINAL pose (one leg raised straight up, foot on
the ball) exactly as in her reference, but show the band as a PRODUCT PLACEMENT, not worn on
the person, plus the SPORTIF logo. So we take our clean plate (ankle weights already removed,
text stripped) and paint the band off her thigh, leaving clean bare skin. The band then lives
only as a product card in the PIL layout step (layout_reskin_clean.py).

    pose = asis   -> keep original raised-leg pose  (default; what Lucy asked for)
    pose = bridge -> glute-bridge variant

Source: generated/images/reference-reskin/plate-<pose>_low.png
Output: generated/images/reference-reskin/plate-clean_<quality>.png

Low works inside Claude Code; high hits the ~60s HTTPS cap (run from a native Terminal).
    python3 clients/sportif/scripts-local/reskin_clean_plate.py low            # asis
    python3 clients/sportif/scripts-local/reskin_clean_plate.py high asis
    python3 clients/sportif/scripts-local/reskin_clean_plate.py low bridge
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
DIR = f'{REPO}/clients/sportif/generated/images/reference-reskin'
QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'
POSE = sys.argv[2] if len(sys.argv) > 2 else 'asis'
SRC = f'{DIR}/plate-{POSE}_low.png'

POSE_KEEP = {
 'asis': "the same original pose (lying on her back, one leg raised straight up in the air, "
         "the other foot resting on the round cushion/ball)",
 'bridge': "the same glute-bridge pose, both feet down",
}[POSE]

PROMPT = (
 "Edit this image to REMOVE the ribbed resistance band that is wrapped around the foreground "
 "model's raised upper thigh, along with its small label tab. Replace it with clean, natural "
 "bare thigh skin that matches her skin tone, lighting and the soft film grain exactly, so it "
 "looks like she was never wearing a band. Keep EVERYTHING else identical: " + POSE_KEEP + ", "
 "the beige shorts and white crop, her ankles bare (no ankle weights), the warm tan colour "
 "block across the top third, the cream lower area, the background model stretching on the "
 "reformer in the minimalist studio, and the warm palette. Do NOT add any text, letters, logos "
 "or watermarks anywhere. Keep it photographic and elegant."
)

SIZE = '1024x1536'
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'},
    files={'image[]': (os.path.basename(SRC), open(SRC, 'rb'), 'image/png')},
    data={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': SIZE,
          'quality': QUALITY, 'output_format': 'png'},
    timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:400]}')
out = f'{DIR}/plate-clean_{QUALITY}.png'
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print(f'ok -> {out}')
