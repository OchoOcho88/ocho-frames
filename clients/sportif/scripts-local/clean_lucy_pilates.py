#!/usr/bin/env python3
"""Make a clean photographic plate of Lucy's pilates ref (NO AI): strip the Canva overlays.

Removes the navy "First class is free!" curved text (cv2 inpaint) and the large faint
PILATES watermark (background-beige flatten: reclassify near-background pixels to a single
clean beige, which erases the ghosted letters while leaving the model untouched). Keeps the
photo otherwise as shot.

Source: reference-images/lucy-canva-picks/lucy-pilates-ref-with-text.png
Output: reference-images/lucy-canva-picks/lucy-pilates-ref-clean.png

    python3 clients/sportif/scripts-local/clean_lucy_pilates.py
"""
import cv2
import numpy as np
from pathlib import Path
from PIL import Image

REF = Path('/Users/hugobrizuela/Desktop/hyperframes/clients/sportif/reference-images/lucy-canva-picks')
SRC = REF / 'lucy-pilates-ref-with-text.png'
OUT = REF / 'lucy-pilates-ref-clean.png'

arr = np.array(Image.open(SRC).convert('RGB'))
H, W = arr.shape[:2]

# --- 1. inpaint the navy "First class is free!" curved text + its soft drop shadow ---
# Region sits to the right of / above her raised shin. Condition catches navy (b>r) and the
# neutral grey shadow (b~=r) but NOT skin (r>b) or beige bg (r>b), so the model is untouched.
mask = np.zeros((H, W), np.uint8)
rx0, ry0, rx1, ry1 = int(W * 0.42), int(H * 0.49), int(W * 0.685), int(H * 0.77)
reg = arr[ry0:ry1, rx0:rx1].astype(int)
r, b = reg[..., 0], reg[..., 2]
txt = (reg.mean(axis=2) < 180) & (b >= r - 2)
mask[ry0:ry1, rx0:rx1][txt] = 255
mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)), 1)
arr = cv2.inpaint(arr, mask, 6, cv2.INPAINT_TELEA)

# --- 2. flatten the background beige to erase the faint PILATES watermark ---
# clean background colour, sampled from a text-free corner patch
bg = np.median(arr[24:150, 24:170].reshape(-1, 3), axis=0)
dist = np.abs(arr.astype(int) - bg).sum(axis=2)
is_bg = dist < 60                                        # beige + faint watermark, NOT the model
# tidy the mask so stray in-model specks don't get flattened, and edges stay crisp
m = cv2.morphologyEx((is_bg * 255).astype(np.uint8), cv2.MORPH_OPEN,
                     cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
is_bg = m > 0
out = arr.copy()
out[is_bg] = bg.astype(np.uint8)

Image.fromarray(out).save(OUT)
print('ok ->', OUT.name, out.shape[1], 'x', out.shape[0], '| bg', tuple(int(c) for c in bg))
