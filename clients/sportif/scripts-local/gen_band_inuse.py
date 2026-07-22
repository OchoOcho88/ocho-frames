#!/usr/bin/env python3
"""Stage 5: generate on-brand pilates 'band in use' scenes (gpt-image-2 generations).

Modest, elevated, peach-world pilates poses with a Sportif booty band around the thighs.
Prompts are the source of truth. Low quality works in-harness; high from a native Terminal
(the ~60s cap). Poses are chosen to READ as band-in-use (glute bridge, squat, kickback)."""
import base64, os, sys, requests
from concurrent.futures import ThreadPoolExecutor

REPO='/Users/hugobrizuela/Desktop/hyperframes'
key=[l.strip().split('=',1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
OUT=f'{REPO}/clients/sportif/generated/images/band-inuse'
os.makedirs(OUT, exist_ok=True)
Q=sys.argv[1] if len(sys.argv)>1 else 'low'
ONLY=sys.argv[2].split(',') if len(sys.argv)>2 else None

BASE=("Warm, elevated editorial PILATES photograph in a calm feminine studio. Soft natural window "
      "light, golden warmth, Sportif palette (blush peach #F0CDB3, caramel tan #C6926E, terracotta clay "
      "#833827, cream linen). A healthy woman in MODEST full-coverage feminine activewear (a supportive "
      "high-neck sports bra and high-waist leggings, {set} tones) {pose} on a soft cream pilates mat. "
      "She wears a wide flat continuous closed-loop ribbed fabric SPORTIF resistance booty band in {band} "
      "around BOTH thighs just above the knees (a flat fabric training loop, not a coiled tube), lightly "
      "stretched as she engages it. Tasteful, professional, calm, elevated, minimalist Australian pilates "
      "aesthetic, respectful and modest. No text, no logos, no watermark.")

JOBS={
 'glute-bridge': dict(set='blush peach and cream', band='terracotta clay',
    pose='performing a glute bridge, lying on her back with hips lifted and knees bent, feet flat on the mat'),
 'squat': dict(set='cream and caramel', band='blush peach',
    pose='in a slow controlled low squat, feet hip-width apart, knees pressing gently outward against the band'),
 'kickback': dict(set='sand and cream', band='caramel tan',
    pose='on all fours in a tabletop position performing a bent-knee glute kickback, one leg lifting'),
 'lateral-walk': dict(set='blush peach', band='terracotta clay',
    pose='standing side-on in a graceful low half-squat mid lateral band walk, stepping to the side, '
         'back straight and poised, one arm softly extended for balance'),
 'standing-abduction': dict(set='cream and blush', band='terracotta clay',
    pose='standing tall and elegant, balanced on one leg while lifting the other leg out to the side '
         'against the band, one hand resting lightly on a wall for balance, long lean controlled line'),
 'curtsy-lunge': dict(set='caramel and cream', band='blush peach',
    pose='in a graceful controlled curtsy lunge, one leg stepping behind the other, torso upright and '
         'poised, arms in a soft pilates position'),
 'kneeling-abduction': dict(set='blush peach and cream', band='terracotta clay',
    pose='kneeling upright and tall on the mat, side-on, lifting one bent knee out to the side against '
         'the band, spine long, calm and elegant'),
}

def run(item):
    name, v = item
    prompt=BASE.format(**v)
    try:
        r=requests.post('https://api.openai.com/v1/images/generations',
            headers={'Authorization':f'Bearer {key}'},
            json={'model':'gpt-image-2','prompt':prompt,'size':'1024x1536','quality':Q,'output_format':'png'},
            timeout=560)
        j=r.json()
        if 'data' not in j: return f'FAIL {name}: {str(j)[:220]}'
        out=f'{OUT}/inuse-{name}_{Q}.png'
        open(out,'wb').write(base64.b64decode(j['data'][0]['b64_json']))
        return f'ok {name} -> {out}'
    except Exception as e:
        return f'FAIL {name}: {e}'

jobs=[(k,v) for k,v in JOBS.items() if ONLY is None or k in ONLY]
with ThreadPoolExecutor(max_workers=3) as ex:
    for res in ex.map(run, jobs): print(res, flush=True)
