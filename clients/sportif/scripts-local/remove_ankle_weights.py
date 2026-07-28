#!/usr/bin/env python3
"""Remove the black ankle weights from Lucy's clean pilates plate (Lucy's request).

Tries a non-AI route first: mask the near-black weight bands inside their two ankle regions
and cv2-inpaint them, reconstructing skin from the surrounding leg. Keeps the rest of the
photo pixel-identical and at native resolution.

Source: reference-images/lucy-canva-picks/lucy-pilates-ref-clean.png
Output: reference-images/lucy-canva-picks/lucy-pilates-ref-noweights.png

    python3 clients/sportif/scripts-local/remove_ankle_weights.py
"""
import cv2
import numpy as np
from pathlib import Path
from PIL import Image

REF = Path('/Users/hugobrizuela/Desktop/hyperframes/clients/sportif/reference-images/lucy-canva-picks')
SRC = REF / 'lucy-pilates-ref-clean.png'
OUT = REF / 'lucy-pilates-ref-noweights.png'

arr = np.array(Image.open(SRC).convert('RGB'))
H, W = arr.shape[:2]

mask = np.zeros((H, W), np.uint8)
# two ankle-weight regions (raised ankle, and ankle resting on the ball)
for (x0, y0, x1, y1) in [(410, 355, 590, 505), (485, 1025, 670, 1205)]:
    sub = arr[y0:y1, x0:x1]
    dark = sub.mean(axis=2) < 75          # the black segmented weight only
    mask[y0:y1, x0:x1][dark] = 255
mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13)), 1)
out = cv2.inpaint(arr, mask, 9, cv2.INPAINT_TELEA)

Image.fromarray(out).save(OUT)
print('ok ->', OUT.name, out.shape[1], 'x', out.shape[0], '| masked px', int((mask > 0).sum()))
