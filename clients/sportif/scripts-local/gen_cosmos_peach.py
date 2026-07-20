#!/usr/bin/env python3
# Cosmos peach series batch (Session 020). Prompts are the source of truth for generated/images/cosmos-peach/.
# Written for the Cowork cloud sandbox: SRC/OUT paths and the .env path need adapting to run locally.
import base64, os, sys, requests
from concurrent.futures import ThreadPoolExecutor

key = [l.strip().split('=',1)[1] for l in open('/mnt/user-data/uploads/hyperframes/.env') if l.startswith('OPENAI_API_KEY=')][0]
SRC = '/tmp/peach/src'
QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'
SIZE = '1088x1360' if QUALITY == 'high' else '1024x1280'
ONLY = sys.argv[2].split(',') if len(sys.argv) > 2 else None
OUT = f'/tmp/peach/{QUALITY}'
os.makedirs(OUT, exist_ok=True)

PALETTE = ("Sportif palette: blush peach #F0CDB3, caramel tan #C6926E, terracotta clay #833827, "
           "cream linen #F6EEE5, warm charcoal #4A433C.")
SAFE = ("This is a tasteful, professional athletic fitness editorial photograph of athletes in modest "
        "full-coverage sportswear, suitable for a mainstream sportswear catalogue.")
KEEP = ("Keep the exact same person, face, hair, body position, posture, camera angle, lighting direction "
        "and fabric texture. Recompose to 4:5 portrait framing centred on the subject, extending the scene naturally if needed. "
        "No text, no logos, no watermarks anywhere.")

JOBS = {
 'beach-run-shoreline': "Recolour her outfit: the jacket to cream linen, the shorts to blush peach, shoes to warm white. Grade the whole scene with a warm golden-hour tone, warm sand and soft peach-tinted sky.",
 'studio-yellow-frame': "Recolour her sports bra to cream and her shorts to blush peach with a caramel waistband. Replace the bright yellow background and border with a soft blush peach studio backdrop.",
 'bw-arms-detail': "Colourise this black-and-white fine-art sports photograph, a close-up detail of an athlete's outstretched arms and ruched athletic shorts. Warm natural skin tones, the shorts and top in blush peach, background warm pale linen. Keep the soft artistic contrast. Abstract, respectful, gallery-style athletic detail study.",
 'teal-warrior-pose-circle': "Recolour her sports bra and leggings from teal to blush peach with subtle caramel seam details. Change the backdrop to warm cream linen and the large circle graphic behind her to soft terracotta.",
 'mint-set-blue-sky': "Recolour her ribbed top and leggings from mint green to blush peach. Change the yellow wall to terracotta clay and warm the sky to a soft pale golden tone.",
 'duo-rust-orange': "Recolour the outfits: the left model's long-sleeve top and shorts to blush peach, the right model's top and shorts to terracotta clay. Change the wall to warm cream, keeping the strong sunlight and shadow patterns.",
 'trio-earth-tones': "Recolour the three outfits: left model in blush peach, centre model in caramel tan, right model in cream. Keep the warm beige studio backdrop.",
 'group4-baby-blue': "Recolour the four baby blue outfits so each model wears a different colour: blush peach, caramel tan, cream, and terracotta clay. Keep the warm beige studio backdrop and white socks and sneakers.",
 'group5-orange-backdrop': "Recolour the five outfits across blush peach, caramel tan, cream, terracotta and warm charcoal, one colour each. Change the orange backdrop to soft blush peach, keeping the palm shadow.",
 'sky-white-bra-sage-leggings': "Recolour her strappy sports bra to cream and her drawstring leggings to blush peach. Warm the blue sky to a soft golden late-afternoon tone.",
 'outdoor-cream-set-blue-hoodie': "Recolour her hooded jacket from light blue to caramel tan and her top and shorts to blush peach, headband to cream. Grade the rock landscape warmer and golden.",
 'la-skyline-rooftop-group': "Recolour the four outfits across blush peach, caramel tan, cream and terracotta, one colour each, shoes warm white. Grade the whole scene to warm golden-hour light over the city skyline.",
 'portrait-sage-tank': "Recolour her ribbed tank top and bottoms from sage green to blush peach, and remove any printed logos or text from the garments, leaving plain fabric. Keep the warm studio light.",
 'bw-forward-fold': "Colourise this black-and-white photo with a warm natural palette: natural skin tones, her outfit in blush peach, the floor and backdrop warm pale linen. Keep the quiet, soft editorial mood.",
 'lookbook-grid-9up': "Recolour every garment across the nine tiles using only the Sportif palette (blush peach, caramel tan, cream, terracotta), varying the colour tile to tile. Keep the pale grey tile backgrounds, poses and grid layout.",
 'form-backbend-editorial': "Recolour her fitted ribbed athletic outfit from dark chocolate brown to blush peach, keeping fabric texture and ribbing. Completely remove the large white 'FORM' text overlay, cleanly reconstructing everything behind the letters.",
}

def run(item):
    name, instr = item
    fn = f'{SRC}/cosmos_{name}.jpeg'
    prompt = f"Edit this photo. {instr} {PALETTE} {KEEP} {SAFE}"
    try:
        r = requests.post('https://api.openai.com/v1/images/edits',
            headers={'Authorization': f'Bearer {key}'},
            files={'image[]': (os.path.basename(fn), open(fn,'rb'), 'image/jpeg')},
            data={'model':'gpt-image-2','prompt':prompt,'size':SIZE,'quality':QUALITY,'output_format':'png'},
            timeout=560)
        j = r.json()
        if 'data' not in j:
            return f'FAIL {name}: {str(j)[:200]}'
        open(f'{OUT}/{name}.png','wb').write(base64.b64decode(j['data'][0]['b64_json']))
        return f'ok {name}'
    except Exception as e:
        return f'FAIL {name}: {e}'

jobs = [(k,v) for k,v in JOBS.items() if ONLY is None or k in ONLY]
with ThreadPoolExecutor(max_workers=4) as ex:
    for res in ex.map(run, jobs):
        print(res, flush=True)
