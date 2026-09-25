#!/usr/bin/env python3
"""Visual shot list for the Double Bay filming day (2 Oct 2026), gpt-image-2 generations.

Pass 2d (Hugo): she holds the bands in every interview panel, small sketched loops. Pass 2c (S045, Hugo): panel order is the order of the afternoon, arrive, propped wide, medium, hands,
interview, leave. Pass 2 (S045): portrait 1024x1536, simple sketched faces (pass 1 gave blank faces), the band
only on the gym sheet (pass 1 grew stray loops on every sheet).

One storyboard sheet per stop (six panels, the six clips in double-bay-shot-list.md) plus one
overview sheet of the afternoon. Prompts are the source of truth (mirrored in image-prompts.md).
Usage: gen_storyboard.py [low|medium|high] [stop,stop,...]
Rules: generic woman, not Lucy's likeness (no generator touches her photos); the band is never
drawn large (D-033); no logos. Style is a drawn storyboard, so the band appears only as a small
sketched loop where the list needs it."""
import base64, os, sys, requests
from concurrent.futures import ThreadPoolExecutor

REPO='/Users/hugobrizuela/Desktop/hyperframes'
key=[l.strip().split('=',1)[1] for l in open(f'{REPO}/.env') if l.startswith('OPENAI_API_KEY=')][0]
OUT=f'{REPO}/clients/sportif/generated/images/storyboard'
os.makedirs(OUT, exist_ok=True)
Q=sys.argv[1] if len(sys.argv)>1 else 'low'
ONLY=sys.argv[2].split(',') if len(sys.argv)>2 else None
TAG=f'-{sys.argv[3]}' if len(sys.argv)>3 else ''  # variant suffix, so a second take does not overwrite the first

STYLE=("Hand-drawn film storyboard sheet on warm cream paper. Loose confident pencil and fine ink "
       "line work with soft grey marker shading and a single light peach wash accent (#FFBE9F) on one "
       "element per panel. Every panel is a tall vertical 9:16 phone frame drawn as a rounded rectangle "
       "with a thin ink border, arranged in a neat grid with even gutters. The same woman in every "
       "panel: mid thirties, blonde ponytail, tasteful modest activewear or a blazer over activewear, "
       "drawn simply with clear simple sketched facial features (eyes, brows, nose, mouth) in every "
       "panel, never a blank face, not a portrait likeness. Calm, elevated, Australian editorial "
       "mood, morning light hatching. ")
TEXT=("Under each panel a short caption in small clean geometric sans-serif capitals, dark grey, "
      "reading exactly: {caps}. A sheet title at the top left in the same typeface reading exactly "
      "\"{title}\". No other text, no logos, no watermark, no brand names anywhere. Keep all text "
      "spelled exactly as given. ")
GUARD=("Six panels, three columns and two rows, left to right, top to bottom, filling a portrait sheet. "
       "Panels are sketches, not photos. No camera drawn in the panels; each panel is what the phone sees. ")
NO_BAND=("The only resistance bands on this sheet are in panel 5, where she holds two or three small "
         "simple sketched flat fabric loops loosely in her hands while she talks, never large, never "
         "the focus. No band and no exercise equipment in any other panel.")
GYM_BAND=("Resistance bands appear only in panel 4 (one small simple sketched fabric loop coming out of "
          "the bag) and panel 5 (two or three small flat fabric loops held loosely in her hands while she "
          "talks), never large, never the focus. No band in any other panel.")

def sheet(title, panels, band=NO_BAND):
    caps=", ".join(f'"{c}"' for c,_ in panels)
    scenes=" ".join(f"Panel {i+1} ({c}): {d}" for i,(c,d) in enumerate(panels))
    return STYLE + scenes + " " + TEXT.format(caps=caps, title=title) + GUARD + band

JOBS={
 'studio': sheet("DOUBLE BAY, STOP 1: THE STUDIO", [
   ("1 ARRIVE","seen from INSIDE the studio: she pushes the front door open and steps in from the bright street, FACING the camera, tote bag on her shoulder, keys in hand, the room in the foreground"),
   ("2 PROPPED WIDE","a whole calm pilates studio seen from a low corner at table height, mirrors along one wall, the woman small in the middle laying out a mat, phone propped and still"),
   ("3 MEDIUM","waist up, she adjusts the mirror and a small shelf of props, handheld feel"),
   ("4 HANDS","close on her hands unrolling a mat, a water bottle, a folded towel on the shelf"),
   ("5 INTERVIEW","close, eye level, she sits on the mat edge talking to the lens, soft window light on her face, the room blurred behind, a few small flat fabric loops held loosely in her hands"),
   ("6 LEAVE","seen from INSIDE the studio: her BACK to the camera as she walks out through the door into the bright street, the empty room in the foreground")]),
 'gym': sheet("DOUBLE BAY, STOP 2: THE GYM", [
   ("1 ARRIVE","seen from inside the gym: she walks in through the entrance TOWARD the camera, facing us, gym bag on her shoulder, the front desk beside her"),
   ("2 PROPPED WIDE","a bright gym floor by the windows, phone propped low, the woman small mid frame coaching a client through a squat"),
   ("3 MEDIUM","waist up, she demonstrates a standing move, one hand on a rack for balance"),
   ("4 HANDS","close on her hands opening the gym bag and lifting out a small folded fabric loop and a water bottle"),
   ("5 INTERVIEW","close, eye level, she sits on a bench in a quiet corner by a window, talking to the lens, a few small flat fabric loops held loosely in her hands"),
   ("6 LEAVE","seen from inside the gym: her BACK to the camera as she pushes the glass door open and walks out into the sunlight")], band=GYM_BAND),
 'walking': sheet("DOUBLE BAY, STOP 3: ON FOOT", [
   ("1 ARRIVE","from behind, she walks away down the footpath under plane trees, tote on her shoulder"),
   ("2 PROPPED WIDE","a leafy village street with cafe awnings, phone propped on a ledge, the woman small crossing the street with a coffee"),
   ("3 MEDIUM","waist up, she walks toward the lens holding a takeaway coffee, smiling past the camera"),
   ("4 HANDS","close on her hand taking a coffee from a cafe counter, a receipt, her keys"),
   ("5 INTERVIEW","she films herself at arm's length while walking, talking to the phone, the street soft behind her, a few small flat fabric loops held loosely in her hands"),
   ("6 LEAVE","she turns a corner toward the harbour, water glimpsed between buildings")]),
 'work': sheet("DOUBLE BAY, STOP 4: THE WORK", [
   ("1 ARRIVE","she has just arrived at the table, facing the camera, pulling out the chair and setting down her phone and coffee, laptop still closed"),
   ("2 PROPPED WIDE","a cafe table by a window or a small office desk, phone propped across the table, the woman small at a laptop with a notebook and coffee"),
   ("3 MEDIUM","waist up, phone to her ear, other hand writing in the notebook"),
   ("4 HANDS","close on her hands on the keyboard and a pen on the notebook, the screen turned away"),
   ("5 INTERVIEW","close, eye level, she leans on the desk and talks to the lens, laptop closed beside her, a few small flat fabric loops held loosely in her hands"),
   ("6 LEAVE","she closes the laptop and stands, chair pushed back")]),
 'meeting': sheet("DOUBLE BAY, STOP 5: THE CLIENT MEETING", [
   ("1 ARRIVE","seen from inside the cafe: she greets a client who has just walked in, handshake at the door, both facing the camera at an angle, smiling"),
   ("2 PROPPED WIDE","a cafe or meeting table seen from the corner at table height, the woman and one client across from each other, small in frame, coffees on the table"),
   ("3 MEDIUM","waist up, the two of them at the table, she is showing something on her phone"),
   ("4 HANDS","close on two coffee cups, a notebook, her hands mid gesture"),
   ("5 INTERVIEW","close, eye level, she sits alone at the emptied table afterwards, talking to the lens, a few small flat fabric loops held loosely in her hands"),
   ("6 LEAVE","the two of them part on the footpath, she waves")]),
 'close': sheet("DOUBLE BAY, STOP 6: THE LAST STOP", [
   ("1 ARRIVE","she arrives at a bench facing the water and sits"),
   ("2 PROPPED WIDE","the harbour foreshore at late afternoon, phone propped on a bench, the woman small walking along the water"),
   ("3 MEDIUM","waist up, she looks out at the water, hair moving, golden light from the side"),
   ("4 HANDS","close on her hands holding her phone, the water and boats soft behind"),
   ("5 INTERVIEW","close, eye level, she sits on the bench and talks to the lens, warm low sun on her face, the harbour behind, a few small flat fabric loops held loosely in her hands"),
   ("6 LEAVE","she walks toward a parked car, keys out, the day ending")]),
 'overview': (STYLE +
   "Panel 1 (OPENER): she says a line to the lens outside the studio door, morning. "
   "Panel 2 (STUDIO): the propped wide of the studio with her laying out a mat. "
   "Panel 3 (GYM): she coaches a client, bright gym by the windows. "
   "Panel 4 (ON FOOT): she crosses a leafy village street with a coffee. "
   "Panel 5 (THE WORK): she sits at a laptop by a cafe window, phone to her ear. "
   "Panel 6 (THE MEETING): two women at a table, coffees, mid conversation. "
   "Panel 7 (THE WATER): she sits on a bench by the harbour in late light. "
   "Panel 8 (CLOSER): close on her face at the bench, saying the last line to the lens. "
   + TEXT.format(caps='"OPENER", "STUDIO", "GYM", "ON FOOT", "THE WORK", "THE MEETING", "THE WATER", "CLOSER"',
                 title="DOUBLE BAY, A DAY IN THE LIFE: THE REEL") +
   "Eight panels, two columns and four rows, left to right, top to bottom, filling a portrait sheet. "
   "Panels are sketches, not photos. No camera drawn in the panels. " + NO_BAND),
 # S047: Lucy's own order of the afternoon (her 25 Sep reply), 1 to 3 pm, all on Cross Street.
 'afternoon': (STYLE +
   "Panel 1 (1:00 OPENER): she stands on a leafy village footpath under plane trees and says a line to the lens, tote bag on her shoulder, smiling. "
   "Panel 2 (1:05 ERRANDS): she walks toward the lens past boutique shop windows and cafe awnings, a small shopping bag in her hand. "
   "Panel 3 (1:20 JUICE AND EMAILS): she sits at a small cafe table by a window, a tall glass of green celery juice beside an open laptop, phone in her hand, the screen turned away. "
   "Panel 4 (1:45 GYM AND STUDIO): a bright modern hotel gym and studio seen from a low corner at table height, mirrors and equipment, large windows, the woman small in the middle setting up a mat. "
   "Panel 5 (2:00 EXERCISING): she does a slow standing side step on the gym floor by the windows, one small simple sketched fabric loop just above her knees, calm and focused, modest activewear. "
   "Panel 6 (2:15 CLIENTS ON THE FLOOR): she stands and chats with two women in activewear on the gym floor, everyone relaxed and laughing, nobody exercising. "
   "Panel 7 (2:30 ROOFTOP POOL): a calm hotel rooftop pool with sun loungers, the harbour and city far behind, the woman small walking along the pool edge in activewear and a light open shirt, not swimwear. "
   "Panel 8 (2:55 CLOSER): close on her face at the rooftop pool, the harbour soft behind her, saying the last line to the lens, two or three small flat fabric loops held loosely in her hands. "
   + TEXT.format(caps='"1:00 OPENER", "1:05 ERRANDS", "1:20 JUICE AND EMAILS", "1:45 GYM AND STUDIO", "2:00 EXERCISING", "2:15 CLIENTS ON THE FLOOR", "2:30 ROOFTOP POOL", "2:55 CLOSER"',
                 title="DOUBLE BAY, FRIDAY 2 OCTOBER: THE AFTERNOON") +
   "Eight panels, two columns and four rows, left to right, top to bottom, filling a portrait sheet. "
   "Panels are sketches, not photos. No camera drawn in the panels. "
   "The only resistance bands on this sheet are the one small loop in panel 5 and the small loops in her hands in panel 8, never large, never the focus."),
}

def run(item):
    name, prompt = item
    try:
        r=requests.post('https://api.openai.com/v1/images/generations',
            headers={'Authorization':f'Bearer {key}'},
            json={'model':'gpt-image-2','prompt':prompt,'size':'1024x1536','quality':Q,'output_format':'png'},
            timeout=560)
        j=r.json()
        if 'data' not in j: return f'FAIL {name}: {str(j)[:220]}'
        sub='proofs-low' if Q=='low' else ''
        os.makedirs(f'{OUT}/{sub}', exist_ok=True)
        num={'overview':0,'studio':1,'gym':2,'walking':3,'work':4,'meeting':5,'close':6,'afternoon':7}[name]
        out=f'{OUT}/{sub}/{num}-storyboard-{name}_{Q}{TAG}.png'.replace('//','/')
        open(out,'wb').write(base64.b64decode(j['data'][0]['b64_json']))
        return f'ok {name} -> {out}'
    except Exception as e:
        return f'ERR {name}: {e}'

if __name__=='__main__':
    jobs=[(k,v) for k,v in JOBS.items() if not ONLY or k in ONLY]
    with ThreadPoolExecutor(max_workers=7) as ex:
        for line in ex.map(run, jobs): print(line)
