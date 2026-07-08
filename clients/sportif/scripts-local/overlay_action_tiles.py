#!/usr/bin/env python3
"""Overlay taglines onto the action backgrounds (text in the upper third)."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[3]
FONT = str(ROOT / "brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf")
OUT = str(ROOT / "clients/sportif/generated/images/grid-banner")

TILE_W, TILE_H = 1080, 1440
CREAM = (250, 245, 238)
PAIRS = [
    ("training", "tagline-1-left", ["Everyday training,", "elevated."]),
    ("fashion", "tagline-2-centre", ["Too fashionable", "not to WEAR!"]),
    ("ritual", "tagline-3-right", ["For your", "morning ritual."]),
]
TAG_SIZE, TAG_TRACK, LEADING = 88, 0.06, 1.42
MINI_SIZE, MINI_TRACK = 40, 0.30


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


def main():
    tiles = []
    for variant, name, lines in PAIRS:
        bg = Image.open(f"{OUT}/bg-action-{variant}-low.png").convert("RGB")
        x0 = (bg.width - TILE_W) // 2
        img = bg.crop((x0, 0, x0 + TILE_W, TILE_H))

        tag_font = ImageFont.truetype(FONT, TAG_SIZE)
        track_px = int(TAG_SIZE * TAG_TRACK)
        line_h = int(TAG_SIZE * LEADING)
        y0 = int(TILE_H * 0.10)

        shadow = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)
        y = y0
        for line in lines:
            draw_line(sd, tag_font, line, TILE_W // 2, y + 5, track_px, (40, 18, 10, 150))
            y += line_h
        shadow = shadow.filter(ImageFilter.GaussianBlur(8))
        img.paste(Image.new("RGB", img.size, (0, 0, 0)), (0, 0), shadow)

        d = ImageDraw.Draw(img)
        y = y0
        for line in lines:
            draw_line(d, tag_font, line, TILE_W // 2, y, track_px, CREAM)
            y += line_h

        mini_font = ImageFont.truetype(FONT, MINI_SIZE)
        mini_track = int(MINI_SIZE * MINI_TRACK)
        my = int(TILE_H * 0.92)
        # small shadow for the mini wordmark too
        ms = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
        msd = ImageDraw.Draw(ms)
        draw_line(msd, mini_font, "SPORTIF", TILE_W // 2, my + 3, mini_track, (40, 18, 10, 150))
        ms = ms.filter(ImageFilter.GaussianBlur(5))
        img.paste(Image.new("RGB", img.size, (0, 0, 0)), (0, 0), ms)
        draw_line(d, mini_font, "SPORTIF", TILE_W // 2, my, mini_track, CREAM)

        img.save(f"{OUT}/sportif-{name}-action.png")
        tiles.append(img)

    g = 12
    row = Image.new("RGB", (TILE_W * 3 + g * 2, TILE_H), "#DDDDDD")
    for i, t in enumerate(tiles):
        row.paste(t, (i * (TILE_W + g), 0))
    row.thumbnail((1600, 1600))
    row.save(f"{OUT}/preview-tagline-row-action.png")
    print("done")


if __name__ == "__main__":
    main()
