#!/usr/bin/env python3
"""Make clean NO-TEXT plates from Lucy's reference pilates-studio ad (gpt-image-2 edit).

We keep the exact layout (tan top block, both model poses, navy+cream warm palette) and
swap in a Sportif booty band, but strip ALL text/watermark so we can lay Sportif type on
top ourselves (Glacial Indifference + real logo) in a separate PIL step. That is our
workflow: the AI does the photographic plate, we own the typography.

Two pose variants to compare:
  asis   - keep the foreground model's raised-leg glute bridge (see how AI reads a band there)
  bridge - convert her to a standard two-foot glute bridge (band around thighs sits naturally)

Source: clients/sportif/products/reference-layouts/pilates-open-ref.<ext>
Output: clients/sportif/generated/images/reference-reskin/

Low works inside Claude Code; high hits the ~60s HTTPS cap (run from a native Terminal).
    python3 clients/sportif/scripts-local/reskin_pilates_ref.py low            # both
    python3 clients/sportif/scripts-local/reskin_pilates_ref.py low bridge     # one
"""
import base64, glob, os, sys, requests
from concurrent.futures import ThreadPoolExecutor

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
REFDIR = f'{REPO}/clients/sportif/products/reference-layouts'
OUT = f'{REPO}/clients/sportif/generated/images/reference-reskin'
os.makedirs(OUT, exist_ok=True)

QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'
ONLY = sys.argv[2].split(',') if len(sys.argv) > 2 else None

cands = sorted(glob.glob(f'{REFDIR}/pilates-open-ref.*'))
if not cands:
    sys.exit(f'No source. Save the screenshot to {REFDIR}/pilates-open-ref.png (or .jpg)')
SRC = cands[0]
ext = os.path.splitext(SRC)[1].lower()
MIME = 'image/png' if ext == '.png' else 'image/jpeg'
print(f'source: {SRC}', flush=True)

# Shared: strip text, add band, keep the warm minimalist composition.
COMMON = (
 "Edit this pilates social ad into a CLEAN BACKGROUND PLATE with NO TEXT of any kind. "
 "Keep the exact same layout and composition: the warm tan/taupe colour block across the "
 "top third, the cream/off-white lower area, the same background model stretching on the "
 "reformer in the warm minimalist studio, and the same navy-and-cream warm palette and mood. "
 "REMOVE every piece of text, lettering, headline and the large faint background watermark "
 "words completely, leaving smooth clean tan and cream areas with no type at all. "
 "Put a soft dusty-blush ribbed-knit SPORTIF resistance BOOTY BAND around the foreground "
 "model's upper thighs, sitting naturally above the knees, with a small cream rubber label "
 "tab (leave the tab blank, no readable text). Remove the black segmented ankle weights from "
 "her ankles and foot entirely, leaving her ankles bare. "
 "Warm affordable-luxury tone: blush peach, caramel tan, terracotta, cream. Keep it "
 "photographic and elegant. Absolutely no words, letters or logos anywhere in the image."
)

JOBS = {
 'asis': ("Keep the foreground model in her current pose exactly (single-leg glute bridge "
          "with one leg raised straight up). " + COMMON),
 'bridge': ("Change the foreground model to a standard two-foot glute bridge: lying on her "
            "back, BOTH feet flat on the floor, knees bent and raised, hips lifted, so the "
            "blush booty band sits naturally around both upper thighs. " + COMMON),
}

SIZE = '1024x1536'  # closest vertical to the 4:5 reference

def run(item):
    name, prompt = item
    try:
        r = requests.post('https://api.openai.com/v1/images/edits',
            headers={'Authorization': f'Bearer {key}'},
            files={'image[]': (os.path.basename(SRC), open(SRC, 'rb'), MIME)},
            data={'model': 'gpt-image-2', 'prompt': prompt, 'size': SIZE,
                  'quality': QUALITY, 'output_format': 'png'},
            timeout=560)
        j = r.json()
        if 'data' not in j:
            return f'FAIL {name}: {str(j)[:300]}'
        out = f'{OUT}/plate-{name}_{QUALITY}.png'
        open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
        return f'ok {name} -> {out}'
    except Exception as e:
        return f'FAIL {name}: {e}'

jobs = [(k, v) for k, v in JOBS.items() if ONLY is None or k in ONLY]
with ThreadPoolExecutor(max_workers=2) as ex:
    for res in ex.map(run, jobs):
        print(res, flush=True)
