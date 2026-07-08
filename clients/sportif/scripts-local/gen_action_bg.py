#!/usr/bin/env python3
"""Generate text-free action/lifestyle images for the tagline tiles (gpt-image-2).

Usage: python3 gen_action_bg.py <variant>   variant = training | fashion | ritual
Quality low (Cowork iteration); winner re-renders high in Claude Code.
Each prompt reserves soft negative space in the upper third for the tagline.
"""

import base64
import json
import sys
import urllib.request

ROOT = "/sessions/cool-inspiring-shannon/mnt/hyperframes"
OUT = f"{ROOT}/clients/sportif/generated/images/grid-banner"

COMMON = (
    " Warm terracotta, blush peach and sand palette, soft golden natural "
    "window light, editorial minimalist, tasteful and elevated, not "
    "skin-heavy. Composition: subject in the lower two thirds, upper third "
    "kept as soft clean negative space for a text overlay. No text, no "
    "logos, no leather, no black or fluro gym gear."
)

PROMPTS = {
    "training": (
        "Editorial lifestyle photograph: a woman in her late twenties, dark "
        "hair in a low bun, wearing warm-neutral elevated activewear, "
        "performing a glute bridge on a cream mat in a sunlit minimalist "
        "studio. Anatomically correct bridge position: she lies on her "
        "back, the back of her head, shoulders, upper back and arms resting "
        "flat on the mat, arms relaxed alongside her body with palms down, "
        "knees bent, feet flat on the mat hip-width apart, hips raised so "
        "her torso forms one straight diagonal line from shoulders to "
        "knees, face relaxed looking up at the ceiling. A blush-peach "
        "fabric resistance band (a wide flat elastic loop band, not a "
        "coiled tube) around her lower thighs just above the knees, "
        "stretched taut between her legs, clearly under tension." + COMMON
    ),
    "fashion": (
        "Editorial still-life photograph, fashion accessory styling: two "
        "fabric resistance bands (wide flat elastic loop bands, not coiled "
        "tubes) in blush peach and terracotta, laid like luxury accessories "
        "on a linen-draped surface next to a natural cotton drawstring "
        "pouch and delicate gold jewellery." + COMMON
    ),
    "ritual": (
        "Editorial lifestyle photograph, quiet morning scene: sunrise light "
        "across a warm minimalist bedroom corner, a rolled cream exercise "
        "mat leaning against the wall. On a linen bench in the foreground, "
        "a blush-peach fabric resistance band lying flat: it is a wide flat "
        "continuous closed loop of knitted elastic fabric, like an "
        "oversized fabric headband, shown as a clean open circle lying "
        "flat on the bench so the loop shape is clearly visible (not "
        "folded, not twisted, not a coiled tube, not a ribbon). Beside it "
        "a ceramic cup of coffee with gentle steam." + COMMON
    ),
}


def key():
    for line in open(f"{ROOT}/.env"):
        line = line.strip()
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"')
    raise SystemExit("no OPENAI_API_KEY in .env")


def main():
    variant = sys.argv[1]
    body = json.dumps({
        "model": "gpt-image-2",
        "prompt": PROMPTS[variant],
        "size": "1088x1440",
        "quality": "low",
        "n": 1,
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body,
        headers={"Authorization": f"Bearer {key()}",
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.load(r)
    with open(f"{OUT}/bg-action-{variant}-low.png", "wb") as f:
        f.write(base64.b64decode(data["data"][0]["b64_json"]))
    print("saved", variant)


if __name__ == "__main__":
    main()
