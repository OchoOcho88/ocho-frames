#!/usr/bin/env python3
"""Fresh gpt-image-2 GENERATIONS (not edits) — exploratory Sportif key visuals.

Three directions x two variants. Warm-neutral affordable-luxury world, brand
guardrails baked in (no leather, flat knitted fabric band, modest/elevated not glam,
no text — we overlay type ourselves). Prompts are the source of truth (binaries gitignored).

Low quality works in-harness; high hits the ~60s cap -> run from a native Terminal:
    python3 clients/sportif/scripts-local/gen_fresh_explore.py low
    python3 clients/sportif/scripts-local/gen_fresh_explore.py high bw1,ch1
"""
import base64, os, sys, requests
from concurrent.futures import ThreadPoolExecutor

REPO = '/Users/hugobrizuela/Desktop/hyperframes'
key = [l.strip().split('=', 1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
OUT = f'{REPO}/clients/sportif/generated/images/fresh-explore'
os.makedirs(OUT, exist_ok=True)

QUALITY = sys.argv[1] if len(sys.argv) > 1 else 'low'
ONLY = sys.argv[2].split(',') if len(sys.argv) > 2 and sys.argv[2] not in ('all', '') else None
# 3rd arg 'real' appends the photoreal block and writes {name}_r_{quality}.png
REAL = len(sys.argv) > 3 and sys.argv[3] == 'real'
# optional version tag (env VER=v2) so a fresh batch doesn't overwrite kept files
VER = os.environ.get('VER', '')

REALISM = ("Shot on 35mm film, Kodak Portra 400, 50mm f/2 lens, natural available window light. "
           "Authentic unretouched editorial photography: real visible skin texture with pores and "
           "fine detail, faint freckles, a few loose flyaway hairs, natural asymmetry and small "
           "imperfections, subtle film grain, gentle shallow depth of field, soft natural colour and "
           "slightly imperfect focus. Candid and a touch unposed, documentary realism, as if shot by "
           "a real fashion photographer. Absolutely avoid any glossy, plastic, waxy, over-smoothed, "
           "airbrushed, symmetrical, CGI or 3D-render look.")

PALETTE = ("Colour palette: warm neutrals only — blush peach, caramel tan, terracotta clay, "
           "linen cream, warm charcoal. Soft natural warm light, gentle shadows, film-like grain, "
           "muted and elevated, affordable-luxury editorial mood.")
GUARD = ("Modest, tasteful, elevated athletic fitness editorial photograph; full-coverage "
         "activewear; confident and calm, never glamorous or skin-forward. Real natural skin "
         "texture, believable proportions. No text, no words, no logos, no watermarks anywhere. "
         "No leather. Vertical 2:3 portrait.")
WARDROBE = ("Wardrobe: premium performance activewear (a supportive crop or tank plus high-waisted "
            "shorts or leggings) made of SMOOTH matte four-way-stretch nylon/elastane sportswear "
            "fabric, the sleek buttery compressive finish of high-end brands like Lululemon or Alo, "
            "with a clean flat smooth surface and flatlock seams and a defined waistband. The fabric "
            "must be SMOOTH, NOT ribbed, NOT a waffle or cable knit, NOT a chunky sweater-knit and "
            "NOT a seamless-ribbed texture. Colour clearly CONTRASTS her skin so it reads as "
            "clothing, choose one of: soft clay-terracotta, dusty rose, warm oatmeal-cream, or muted "
            "sage-clay. NEVER a nude, flesh, beige-skin or tan tone that blends into her body. Fully "
            "opaque, modest coverage, not underwear and not a bodysuit.")
BAND = ("The resistance booty band is a FLAT WIDE loop of soft knitted stretch fabric (not rubber, "
        "not a thin elastic), blush-to-sand colour, with a small woven fabric label.")

SIZE = '1024x1536'

JOBS = {
 # --- Brand-world lifestyle ---
 'bw1': (
   "A candid editorial lifestyle photograph of a young woman in a matching activewear set, "
   "standing relaxed and confident by a tall window in a sunlit minimalist Australian apartment. Sheer linen curtains "
   "diffuse the morning light; a potted olive branch and pale plaster walls in the background. "
   "Generous empty space in the upper third for a headline. " + PALETTE + " " + GUARD),
 'bw2': (
   "A warm candid lifestyle moment: a woman sitting cross-legged on a woven jute rug in a "
   "sun-dappled cream-toned room, a rolled exercise mat and a ceramic cup of tea beside her, "
   "tying her hair up, wearing an activewear set. Soft long morning shadows across "
   "the floor, unhurried and serene, negative space above. " + PALETTE + " " + GUARD),
 # --- Campaign hero ---
 'ch1': (
   "A bold minimalist fashion-campaign key visual: a single woman in activewear "
   "standing against a large flat terracotta-clay plaster wall, dramatic warm directional "
   "sunlight raking across the wall and casting a long soft shadow beside her. Vast empty wall "
   "space in the upper two thirds for a headline. Strong, elevated, quietly powerful. "
   + PALETTE + " " + GUARD),
 'ch2': (
   "A striking campaign mid-shot with sculptural warm light and shadow play: a woman in "
   "activewear turning gently, a flat knitted fabric booty band held in one hand, an "
   "architectural warm-cream backdrop with a hard sunbeam and deep soft shadow. Editorial, "
   "confident, cinematic. Negative space to one side for type. " + BAND + " " + PALETTE + " " + GUARD),
 # --- Band-in-use editorial ---
 'bu1': (
   "An elevated fitness editorial photograph: a woman mid-pilates in a warm minimalist reformer "
   "studio, standing tall and doing a SMALL controlled lateral leg lift (a gentle standing "
   "hip-abduction, working foot only slightly off the floor, NOT a high kick), a flat wide "
   "knitted-fabric booty band stretched around her upper thighs. She wears a clearly-defined "
   "MATCHING TWO-PIECE ACTIVEWEAR SET: a fitted long-sleeve crop top and separate "
   "high-waisted bike shorts (see wardrobe note for colour), the fabric a distinctly different tone "
   "from her skin so the outfit reads obviously as sportswear (not nude, not a bodysuit, not a "
   "leotard, not loungewear). The band sits around her upper thighs OVER the shorts. Cream plaster walls, arched "
   "backlit mirrors, terracotta accents, soft natural light. Clean composition, band clearly "
   "visible and in use. " + BAND + " " + PALETTE + " " + GUARD),
 'bu2': (
   "An elevated fitness editorial photograph: a woman in a warm minimalist studio holding a deep "
   "squat, a flat wide knitted-fabric booty band stretched around her upper thighs, hips back, "
   "calm focused expression. Warm cream and terracotta surroundings, soft window light, modest "
   "full-coverage activewear. The fabric band is the clear focal product. "
   + BAND + " " + PALETTE + " " + GUARD),
}

def run(item):
    name, prompt = item
    prompt = prompt + ' ' + WARDROBE
    if REAL:
        prompt = prompt + ' ' + REALISM
    try:
        r = requests.post('https://api.openai.com/v1/images/generations',
            headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
            json={'model': 'gpt-image-2', 'prompt': prompt, 'size': SIZE,
                  'quality': QUALITY, 'output_format': 'png', 'n': 1},
            timeout=560)
        j = r.json()
        if 'data' not in j:
            return f'FAIL {name}: {str(j)[:300]}'
        out = f'{OUT}/{name}{"_r" if REAL else ""}{"_" + VER if VER else ""}_{QUALITY}.png'
        open(out, 'wb').write(base64.b64decode(j['data'][0]['b64_json']))
        return f'ok {name} -> {out}'
    except Exception as e:
        return f'FAIL {name}: {e}'

jobs = [(k, v) for k, v in JOBS.items() if ONLY is None or k in ONLY]
with ThreadPoolExecutor(max_workers=3) as ex:
    for res in ex.map(run, jobs):
        print(res, flush=True)
