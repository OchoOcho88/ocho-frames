"""Take the Opera House out of the 2:55 CLOSER panel on the afternoon storyboard (S047).

You cannot see the Opera House from a Double Bay rooftop, and Lucy lives and works there, so the
far background behind her right shoulder is redrawn as the bay: moored yachts and a low wooded
headland. Only that corner changes. The panel is cropped (with a strip of paper each side so it
is 3:2), sent to gpt-image-2 edits, and just the Opera House box is pasted back from the result
with a feathered edge, so her face, the loops, the skyline on the left and the captions stay the
pixels already chosen.

Run:  python3 clients/sportif/scripts-local/fix_closer_panel.py gen [n]     (edits, writes takes)
      python3 clients/sportif/scripts-local/fix_closer_panel.py paste <take>
"""

import base64
import io
import sys
from pathlib import Path

import requests
from PIL import Image, ImageFilter

REPO = Path("/Users/hugobrizuela/Desktop/hyperframes")
SB = REPO / "clients/sportif/generated/images/storyboard"
SHEET = SB / "7-storyboard-afternoon_medium-b-1230.png"
TAKES = SB / "closer-fix"
OUT = SB / "7-storyboard-afternoon_medium-b-1230-closerfix.png"

CROP = (515, 1162, 987, 1477)          # the CLOSER panel plus 12 px of paper each side, 472 x 315
BOX = (342, 78, 458, 162)              # the Opera House and its buildings, in crop pixels
FEATHER = 8

PROMPT = (
    "This is one panel of a hand-drawn pencil and ink film storyboard on cream paper. Change ONLY the far "
    "background on the right side, behind her left shoulder (the right of the picture): remove the Sydney "
    "Opera House and the buildings beside it, and draw instead what you would see from a hotel rooftop in "
    "Double Bay, Sydney: the calm bay with a few moored yachts and a low headland covered in trees with a "
    "few houses among them, under the same soft cloudy sky. Match the existing loose pencil and fine ink "
    "line work and soft grey marker shading exactly. Keep everything else exactly as it is: the woman, her "
    "face, hair, shirt, the fabric loops in her hands, the city skyline on the left, the water and boats in "
    "the middle, the glass railing, the plants, the cream paper margins and the panel's rounded ink border. "
    "No Opera House, no bridge, no text, no logos.")


def gen(n):
    key = [l.split("=", 1)[1].strip() for l in open(REPO / ".env") if l.startswith("OPENAI_API_KEY=")][0]
    crop = Image.open(SHEET).convert("RGB").crop(CROP).resize((1536, 1024), Image.LANCZOS)
    buf = io.BytesIO(); crop.save(buf, "PNG")
    r = requests.post("https://api.openai.com/v1/images/edits",
                      headers={"Authorization": f"Bearer {key}"},
                      files=[("image[]", ("panel.png", buf.getvalue(), "image/png"))],
                      data={"model": "gpt-image-2", "prompt": PROMPT, "size": "1536x1024",
                            "quality": "medium", "n": str(n), "output_format": "png"},
                      timeout=900)
    j = r.json()
    if "data" not in j:
        sys.exit(f"FAIL: {str(j)[:500]}")
    TAKES.mkdir(parents=True, exist_ok=True)
    for i, d in enumerate(j["data"], 1):
        p = TAKES / f"take-{i}.png"
        Image.open(io.BytesIO(base64.b64decode(d["b64_json"]))).save(p)
        print("ok ->", p.relative_to(REPO))


def paste(take):
    sheet = Image.open(SHEET).convert("RGB")
    w, h = CROP[2] - CROP[0], CROP[3] - CROP[1]
    fixed = Image.open(TAKES / f"take-{take}.png").convert("RGB").resize((w, h), Image.LANCZOS)
    mask = Image.new("L", (w, h), 0)
    x0, y0, x1, y1 = BOX
    mask.paste(255, (x0 + FEATHER, y0 + FEATHER, x1 - FEATHER, y1 - FEATHER))
    mask = mask.filter(ImageFilter.GaussianBlur(FEATHER / 2))
    panel = sheet.crop(CROP)
    panel.paste(fixed, (0, 0), mask)
    sheet.paste(panel, CROP[:2])
    sheet.save(OUT)
    print("ok ->", OUT.relative_to(REPO))


if __name__ == "__main__":
    if sys.argv[1] == "gen":
        gen(int(sys.argv[2]) if len(sys.argv) > 2 else 2)
    else:
        paste(int(sys.argv[2]))
