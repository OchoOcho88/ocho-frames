#!/usr/bin/env python3
"""Restage Lucy's real SPORTIF bands onto clean brand grounds via gpt-image-2 edits.

Source: the real band photos in clients/sportif/products/real-bands/.
Output: clients/sportif/generated/images/product-bands/.

Prompts here are the source of truth (binaries gitignored). Low quality holds the
labels crisp and works inside Claude Code; HIGH quality exceeds the ~60s HTTPS cap in
the harness, so run high from a NATIVE Mac terminal:

    python3 clients/sportif/scripts-local/gen_band_product.py high
    python3 clients/sportif/scripts-local/gen_band_product.py low flatlay   # one job
"""
import base64, os, sys, requests
from concurrent.futures import ThreadPoolExecutor

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
SRC = f'{REPO}/clients/sportif/products/real-bands'
OUT = f'{REPO}/clients/sportif/generated/images/product-bands'
os.makedirs(OUT, exist_ok=True)

QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'
ONLY = sys.argv[2].split(',') if len(sys.argv) > 2 else None

KEEP = ("Keep the SPORTIF fabric resistance booty bands EXACTLY identical: same warm colours "
        "(terracotta-brown HEAVY, dusty blush MEDIUM, sand-cream LIGHT), same knit texture and folds, "
        "and keep the cream rubber SPORTIF labels with their exact embossed text intact and legible "
        "(the SPORTIF wordmark with underline, and the words HEAVY / MEDIUM / LIGHT). "
        "Clean minimalist editorial product photograph, warm and tactile, soft diffuse studio light, "
        "gentle soft contact shadow. No extra text or logos anywhere except the real labels.")

# each job: (source file, size, instruction)
JOBS = {
 'flatlay': ('bands.jpg', '1536x1024',
    "Remove all clutter (juice glass, water bottle, plastic bag, hard shadows) and replace the "
    "countertop and background with a smooth seamless blush-peach studio surface (#F0CDB3). "
    "Keep all three bands laid in a neat row."),
 'flatlay-cream': ('bands.jpg', '1536x1024',
    "Remove all clutter and replace the surface with a soft cream linen studio backdrop (#F6EEE5), "
    "keeping all three bands in a neat row."),
 'trio-portrait': ('bands_2.jpg', '1024x1536',
    "Remove all clutter and replace the background with a smooth blush-peach studio surface (#F0CDB3). "
    "Recompose to a vertical 4:5-friendly portrait product shot of the three bands stacked, generous "
    "clean peach space above and below for a caption."),
}

def run(item):
    name, (fn, size, instr) = item
    src = f'{SRC}/{fn}'
    prompt = f"Edit this photo. {instr} {KEEP}"
    try:
        r = requests.post('https://api.openai.com/v1/images/edits',
            headers={'Authorization': f'Bearer {key}'},
            files={'image[]': (fn, open(src, 'rb'), 'image/jpeg')},
            data={'model': 'gpt-image-2', 'prompt': prompt, 'size': size,
                  'quality': QUALITY, 'output_format': 'png'},
            timeout=560)
        j = r.json()
        if 'data' not in j:
            return f'FAIL {name}: {str(j)[:200]}'
        out = f'{OUT}/bands-{name}-peach_{QUALITY}.png'
        open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
        return f'ok {name} -> {out}'
    except Exception as e:
        return f'FAIL {name}: {e}'

jobs = [(k, v) for k, v in JOBS.items() if ONLY is None or k in ONLY]
with ThreadPoolExecutor(max_workers=3) as ex:
    for res in ex.map(run, jobs):
        print(res, flush=True)
