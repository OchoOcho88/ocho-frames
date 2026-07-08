#!/usr/bin/env python3
"""Generate a text-free textured background for the tagline tiles (gpt-image-2).

Usage: python3 gen_tagline_bg.py <variant>   variant = linen | plaster
Quality low (Cowork iteration); finals re-render high in Claude Code.
"""

import base64
import json
import os
import sys
import urllib.request

ROOT = "/sessions/cool-inspiring-shannon/mnt/hyperframes"
OUT = f"{ROOT}/clients/sportif/generated/images/grid-banner"

PROMPTS = {
    "linen": (
        "Backdrop-only photograph: warm terracotta linen fabric, softly draped "
        "with gentle natural creases, lit by soft window light from the upper "
        "left with a smooth shadow falloff toward the bottom. Editorial, "
        "minimalist, warm clay and rust tones. Empty background only: no text, "
        "no logo, no objects, no people, no product."
    ),
    "plaster": (
        "Backdrop-only photograph: warm blush-sand limewash plaster wall with "
        "subtle texture, soft diagonal morning window light casting one faint "
        "soft-edged leaf shadow across the upper corner. Editorial, minimalist, "
        "warm neutral tones. Empty background only: no text, no logo, no "
        "objects, no people, no product."
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
    img = base64.b64decode(data["data"][0]["b64_json"])
    path = f"{OUT}/bg-{variant}-low.png"
    with open(path, "wb") as f:
        f.write(img)
    print("saved", path)


if __name__ == "__main__":
    main()
