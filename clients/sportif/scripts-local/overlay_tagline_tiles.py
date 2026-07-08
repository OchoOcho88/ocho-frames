#!/usr/bin/env python3
"""Overlay the 3 taglines + mini wordmark onto a generated background.

Usage: python3 overlay_tagline_tiles.py <variant>   variant = linen | plaster
Crops the 1088x1440 gen to 1080x1440, darkens slightly for legibility,
then draws cream Glacial Indifference with a soft shadow.
"""

import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

FONT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf"
OUT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/clients/sportif/generated/images/grid-banner"

TILE_W, TILE_H = 1080, 1440
CREAM = (246, 238, 229)
TILES = [
    ("tagline-1-left", ["Everyday training,", "elevated."]),
    ("tagline-2-centre", ["Too fashionable", "not to WEAR!"]),
    ("tagline-3-right", ["For your", "morning ritual."]),
]
TAG_SIZE, TAG_TRACK, LEADING = 96, 0.06, 1.45
MINI_SIZE, MINI_TRACK = 44, 0.30


def line_widths(font, text, track_px):
    ws = []
    for ch in text:
        if ch == " ":
            ws.append(int(font.size * 0.30) + track_px)
        else:
            b = font.getbbox(ch)
            ws.append((b[2] - b[0]) + track_px)
    return ws


def draw_line(d, font, text, cx, y, track_px, fill):
    ws = line_widths(font, text, track_px)
    x = cx - (sum(ws) - track_px) // 2
    for ch, w in zip(text, ws):
        if ch != " ":
            b = font.getbbox(ch)
            d.text((x - b[0], y), ch, font=font, fill=fill)
        x += w


def make_tile(bg, lines, name, variant):
    img = bg.copy()
    tag_font = ImageFont.truetype(FONT, TAG_SIZE)
    track_px = int(TAG_SIZE * TAG_TRACK)
    line_h = int(TAG_SIZE * LEADING)
    y0 = (TILE_H - line_h * len(lines)) // 2 - int(TILE_H * 0.04)

    shadow = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    y = y0
    for line in lines:
        draw_line(sd, tag_font, line, TILE_W // 2, y + 5, track_px, (35, 15, 8, 130))
        y += line_h
    shadow = shadow.filter(ImageFilter.GaussianBlur(7))
    img.paste(Image.new("RGB", img.size, (0, 0, 0)), (0, 0), shadow)

    d = ImageDraw.Draw(img)
    y = y0
    for line in lines:
        draw_line(d, tag_font, line, TILE_W // 2, y, track_px, CREAM)
        y += line_h

    mini_font = ImageFont.truetype(FONT, MINI_SIZE)
    mini_track = int(MINI_SIZE * MINI_TRACK)
    my = int(TILE_H * 0.80)
    draw_line(d, mini_font, "SPORTIF", TILE_W // 2, my, mini_track, CREAM)
    cap = mini_font.getbbox("S")
    rule_w = int(MINI_SIZE * 1.6)
    rx = (TILE_W - rule_w) // 2
    d.rectangle([rx, my + cap[3] + 18, rx + rule_w, my + cap[3] + 22], fill=CREAM)

    img.save(f"{OUT}/sportif-{name}-{variant}.png")
    return img


def main():
    variant = sys.argv[1]
    bg = Image.open(f"{OUT}/bg-{variant}-low.png").convert("RGB")
    # center-crop 1088 -> 1080 wide
    x0 = (bg.width - TILE_W) // 2
    bg = bg.crop((x0, 0, x0 + TILE_W, TILE_H))
    # slight darken for text legibility
    bg = ImageEnhance.Brightness(bg).enhance(0.92)

    tiles = [make_tile(bg, lines, name, variant) for name, lines in TILES]

    g = 12
    row = Image.new("RGB", (TILE_W * 3 + g * 2, TILE_H), "#DDDDDD")
    for i, t in enumerate(tiles):
        row.paste(t, (i * (TILE_W + g), 0))
    row.thumbnail((1600, 1600))
    row.save(f"{OUT}/preview-tagline-row-{variant}.png")
    print("done", variant)


if __name__ == "__main__":
    main()
