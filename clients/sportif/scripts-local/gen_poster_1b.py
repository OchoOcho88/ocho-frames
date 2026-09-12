#!/usr/bin/env python3
"""Q-019: poster 2 (Prompt 1B, legs only) re-run with the band geometry spelled out.

S032's plates from both engines put the band running ALONG the top thigh instead of
looping both thighs. The fix is wording, not references: the loop is described as a
closed band that encircles both thighs together, so it crosses the legs at a right
angle. Two product references only (gpt-image-2 drifts past three), no style image.

    python3 clients/sportif/scripts-local/gen_poster_1b.py low  [n]
    python3 clients/sportif/scripts-local/gen_poster_1b.py high

Output: generated/images/band-posters/plates-in/p2-legs-gpt-v2-<quality>-<k>.png
The plate is a PHOTOGRAPH only. Type is laid in PIL afterwards (band-poster-prompts.md).
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
REFS = [f'{REPO}/clients/sportif/products/band-reference-plates/ref-front-folded.jpg',
        f'{REPO}/clients/sportif/products/band-reference-plates/ref-label-detail.jpg']
OUT = f'{REPO}/clients/sportif/generated/images/band-posters/plates-in'
QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1

PROMPT = (
 "Image 1 and image 2 are the actual product and must be reproduced exactly. "
 "A cropped editorial photograph showing only the legs and lower torso of a woman lying on "
 "her side on a pale linen mat against a flat cream wall, knees bent and stacked one on top "
 "of the other, the top knee lifting a little. She wears cream ribbed full length leggings. "
 "THE BAND GEOMETRY, which matters most: the caramel brown fabric resistance band is one "
 "closed loop that encircles BOTH thighs together, just above the knees. Seen from the side "
 "it is a wide flat strip lying HORIZONTALLY ACROSS both stacked thighs, perpendicular to "
 "the direction of the legs, like a cuff around both legs at once, never running along the "
 "length of a leg and never wrapped around one thigh alone. The lifting top knee pulls it "
 "taut so it is clearly under tension, and its cream moulded label faces the camera on the "
 "outside of the top thigh. "
 "The legs enter from the lower right and reach into the centre of the frame. The entire "
 "upper half of the frame is empty cream wall. Shot straight on at floor level on a 50mm "
 "lens, soft even daylight from the left, warm paper-like tone across the whole image. "
 "Style: quiet editorial photography, matte, visible paper grain. "
 "Product accuracy: the band must be EXACTLY the band in the product reference images, "
 "same caramel brown woven fabric with visible knit texture, same flat wide loop, same cream "
 "moulded rectangular label with raised lettering. Do not redesign it or change its colour. "
 "Background: one flat, plain, evenly lit wall in a single warm tone, no props, no gradient, "
 "no shadows on the wall. Text: no text anywhere except the moulded label on the band. "
 "Palette: warm neutrals only, no cool greys, no blue cast, no black. Wardrobe: full length "
 "leggings, generous coverage, nothing sheer. Framing: never centred on the glutes, "
 "aesthetic and lifestyle led. One person only, no clutter, no equipment."
)

files = [('image[]', (os.path.basename(f), open(f, 'rb'), 'image/jpeg')) for f in REFS]
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'}, files=files,
    data={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536', 'n': N,
          'quality': QUALITY, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:400]}')
for k, d in enumerate(j['data'], 1):
    out = f'{OUT}/p2-legs-gpt-v2-{QUALITY}-{k}.png'
    open(out, 'wb').write(base64.b64decode(d['b64_json']))
    print(f'ok -> {out}')
