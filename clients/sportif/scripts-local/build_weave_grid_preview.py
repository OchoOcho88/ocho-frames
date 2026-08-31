#!/usr/bin/env python3
"""Client-facing preview: the three weave tiles as they sit on a profile grid.

Answers Lucy's "can you create them so they fit in the instagram tiles"
(2026-08-28). They already fit. This shows it rather than explains it.

Instagram crops profile-grid thumbnails to 3:4, so a 1080 x 1350 post shows a
centred 1012px column. The lockup is 820px wide, so it clears the crop by 96px
each side and nothing is lost. The row is shown left to right as it will read
on the profile: light, medium, heavy.

Re-runs clean, no arguments.
"""

import os
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(ROOT, "clients/sportif/generated/images/texture-weight-tiles")
ORDER = ["light", "medium", "heavy"]

TW, GAP, PAD = 460, 4, 40
BG = (255, 255, 255)


def crop_3x4(im):
    w = round(im.height * 3 / 4)
    left = (im.width - w) // 2
    return im.crop((left, 0, left + w, im.height))


if __name__ == "__main__":
    th = round(TW * 4 / 3)
    W = PAD * 2 + TW * 3 + GAP * 2
    H = PAD * 2 + th
    page = Image.new("RGB", (W, H), BG)
    for i, c in enumerate(ORDER):
        im = Image.open(os.path.join(SRC, f"sportif-weave-{c}-feed.png"))
        page.paste(crop_3x4(im).resize((TW, th), Image.LANCZOS),
                   (PAD + i * (TW + GAP), PAD))
    p = os.path.join(SRC, "grid-preview-for-lucy.jpg")
    page.save(p, quality=95)
    print(f"  grid-preview-for-lucy.jpg   {W}x{H}")
