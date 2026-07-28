#!/usr/bin/env python3
"""Remove the black ankle weights via gpt-image-2, but composite only the ankle patches back
onto the native-resolution clean plate so the rest of Lucy's photo stays untouched.

Lucy requested the weights gone; cv2 inpaint smudged the ankle anatomy, so we let gpt
reconstruct bare ankles. To avoid softening the whole photo, we pad to a 2:3 canvas (no
distortion), run the edit, then feather-composite ONLY the two ankle regions back.

Source: reference-images/lucy-canva-picks/lucy-pilates-ref-clean.png
Output: reference-images/lucy-canva-picks/lucy-pilates-ref-noweights.png

Low works inside Claude Code; high hits the ~60s cap (run from a native Terminal).
    python3 clients/sportif/scripts-local/remove_ankle_weights_ai.py low
"""
import base64, io, sys
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import requests

REPO = Path('/Users/hugobrizuela/Desktop/hyperframes')
key = [l.strip().split('=', 1)[1] for l in open(REPO / '.env') if l.startswith('OPENAI_API_KEY=')][0]
REF = REPO / 'clients/sportif/reference-images/lucy-canva-picks'
SRC = REF / 'lucy-pilates-ref-clean.png'
OUT = REF / 'lucy-pilates-ref-noweights.png'
QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'

orig = Image.open(SRC).convert('RGB')
W, H = orig.size                       # 1080 x 1350 (4:5)
BG = (230, 224, 217)

# pad to 2:3 (1080x1620) so the supported 1024x1536 export scales uniformly (no distortion)
padH = round(W * 3 / 2)                 # 1620
pad = (padH - H) // 2                   # 135
canvas = Image.new('RGB', (W, padH), BG)
canvas.paste(orig, (0, pad))

buf = io.BytesIO(); canvas.save(buf, 'PNG'); buf.seek(0)
PROMPT = (
 "Remove the black segmented ankle weights from BOTH of the model's ankles. Reconstruct "
 "natural, bare ankles and lower legs with skin tone, shading and soft film grain that match "
 "the rest of her leg exactly. Keep the pose, the beige shorts, the tan cushion, both feet, "
 "her toes and the plain warm beige background all identical. No text, no logos anywhere."
)
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'},
    files={'image[]': ('pad.png', buf, 'image/png')},
    data={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536',
          'quality': QUALITY, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:400]}')
edited = Image.open(io.BytesIO(base64.b64decode(j['data'][0]['b64_json']))).convert('RGB')

# back to native geometry: resize to padded size, crop the padding away
edited = edited.resize((W, padH), Image.LANCZOS).crop((0, pad, W, pad + H))

# feathered composite of ONLY the ankle regions onto the untouched original
m = Image.new('L', (W, H), 0)
d = ImageDraw.Draw(m)
for box in [(400, 345, 600, 515), (475, 1015, 680, 1215)]:
    d.rectangle(box, fill=255)
m = m.filter(ImageFilter.GaussianBlur(22))
out = Image.composite(edited, orig, m)
out.save(OUT)
print('ok ->', OUT.name, out.size)
