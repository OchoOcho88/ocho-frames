#!/usr/bin/env python3
"""Composite the REAL crisp SPORTIF label onto the band in an in-use shot (local, no API).

Guaranteed pixel-perfect text (no AI fuzz). Masks the badge from the real label crop, feathers
it, scales/rotates it to sit on the band, and pastes it onto the clean in-use scene.
Tweak CENTER / WIDTH / ANGLE per pose. Usage: python3 composite_band_label.py
"""
from PIL import Image, ImageDraw, ImageFilter

REPO='/Users/hugobrizuela/Desktop/hyperframes'
DIR=f'{REPO}/clients/sportif/generated/images/band-inuse'

# --- per-pose placement (squat) ---
BASE=f'{DIR}/inuse-squat_low.png'
LABEL=f'{DIR}/label-medium.png'
OUT=f'{DIR}/inuse-squat-labeled-composite.png'
CENTER=(478, 922)   # where the label centre lands on the band (full-image px)
WIDTH=150           # label width in px on the band
ANGLE=-3            # degrees, + = counter-clockwise

base=Image.open(BASE).convert('RGBA')
lab=Image.open(LABEL).convert('RGBA')
lw,lh=lab.size
# mask the badge (inset off the surrounding band fabric), feather the edge
m=Image.new('L',(lw,lh),0)
d=ImageDraw.Draw(m)
d.rounded_rectangle([14,12,lw-14,lh-12], radius=22, fill=255)
m=m.filter(ImageFilter.GaussianBlur(5))
lab.putalpha(m)
# scale to target width, rotate
scale=WIDTH/lw
lab=lab.resize((WIDTH, max(1,int(lh*scale))), Image.LANCZOS)
lab=lab.rotate(ANGLE, expand=True, resample=Image.BICUBIC)
# paste centred at CENTER
px=int(CENTER[0]-lab.width/2); py=int(CENTER[1]-lab.height/2)
base.alpha_composite(lab,(px,py))
base.convert('RGB').save(OUT)
# zoom for review
zx0,zy0=CENTER[0]-170,CENTER[1]-130
base.convert('RGB').crop((zx0,zy0,zx0+340,zy0+260)).save('/private/tmp/claude-501/-Users-hugobrizuela-Desktop-hyperframes/2cb1d5b4-55d8-4929-be7f-02ccd33c93b9/scratchpad/composite_zoom.png')
print('saved',OUT,'+ zoom')
