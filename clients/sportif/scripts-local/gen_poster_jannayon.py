#!/usr/bin/env python3
"""Experiment: JANNAYON-style collage poster, Sportif references + warm palette (gpt-image-2).

Borrows the reference poster's LAYOUT (big hero photo, B&W corner shot, two lower photos,
oversized headline overlapping the hero, wordmark along the bottom) but swaps in our warm
Sportif band-in-use shots and palette. Text is left to gpt here on purpose so we can compare
my prompt vs Hugo's prompt on the same tool; the production-final would lay real type in PIL.

Source refs: generated/images/band-inuse/*labeled*.png
Output: generated/images/poster-experiment/poster-jannayon_<quality>.png

Low works inside Claude Code; high hits the ~60s HTTPS cap (run from a native Terminal).
    python3 clients/sportif/scripts-local/gen_poster_jannayon.py low
"""
import base64, os, sys, requests

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
IN = f'{REPO}/clients/sportif/generated/images/band-inuse'
OUT = f'{REPO}/clients/sportif/generated/images/poster-experiment'
os.makedirs(OUT, exist_ok=True)
QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'

REFS = [
    'inuse-squat-labeled_low.png',              # hero (band most visible)
    'inuse-lateral-walk-barefoot-labeled_low.png',
    'inuse-standing-abduction-labeled_low.png',
    'inuse-kneeling-abduction_low.png',
]

PROMPT = (
 "Create a bold, premium fitness-brand POSTER in a COLLAGE GRID layout, portrait. Use ONLY a "
 "warm affordable-luxury palette: blush peach, caramel tan, terracotta clay, warm cream and "
 "soft charcoal. Absolutely NO blue or periwinkle anywhere. "
 "The woman, her warm minimalist studio, her neutral activewear and the ribbed SPORTIF "
 "resistance booty band should match the attached reference photos. "
 "LAYOUT to mirror: "
 "(1) a LARGE hero photo filling the upper-centre, a lean athletic woman mid-movement in a "
 "deep band squat, the terracotta booty band clearly around her thighs; "
 "(2) a smaller BLACK-AND-WHITE photo in the top-right corner, the same woman shown from "
 "behind; "
 "(3) two smaller photos along the bottom row, the woman in a side-lunge and in a standing "
 "balance, each using the band, in warm colour; "
 "(4) an OVERSIZED bold condensed uppercase HEADLINE in soft charcoal, set large on the left "
 "and partly overlapped by the hero photo, reading exactly: STRENGTH YOU CAN WEAR on three "
 "stacked lines; "
 "(5) the brand wordmark SPORTIF in clean letter-spaced caps centred along the very bottom. "
 "Editorial catalogue feel, soft natural daylight, subtle film grain, photographic realism. "
 "Keep every letter correctly spelled, evenly spaced and legible."
)

files = [('image[]', (f, open(f'{IN}/{f}', 'rb'), 'image/png')) for f in REFS]
r = requests.post('https://api.openai.com/v1/images/edits',
    headers={'Authorization': f'Bearer {key}'}, files=files,
    data={'model': 'gpt-image-2', 'prompt': PROMPT, 'size': '1024x1536',
          'quality': QUALITY, 'output_format': 'png'}, timeout=560)
j = r.json()
if 'data' not in j:
    sys.exit(f'FAIL: {str(j)[:400]}')
out = f'{OUT}/poster-jannayon_{QUALITY}.png'
open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
print(f'ok -> {out}')
