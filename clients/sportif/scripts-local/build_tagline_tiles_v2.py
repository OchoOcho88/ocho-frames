#!/usr/bin/env python3
"""Tagline tiles v2: terracotta gradient background + soft text shadow.

Vertical gradient (lighter terracotta up top, deep clay at the base) with a
faint warm highlight behind the tagline, subtle shadow under the text.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf"
OUT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/clients/sportif/generated/images/grid-banner"

TILE_W, TILE_H = 1080, 1440
CREAM = (246, 238, 229)

# gradient stops (top to bottom): lifted terracotta down to deep clay
TOP = (154, 74, 50)
BOT = (85, 32, 20)

TILES = [
    ("tagline-1-left-v2", ["Everyday training,", "elevated."]),
    ("tagline-2-centre-v2", ["Too fashionable", "not to WEAR!"]),
    ("tagline-3-right-v2", ["For your", "morning ritual."]),
]

TAG_SIZE = 96
TAG_TRACK = 0.06
LEADING = 1.45
MINI_SIZE = 44
MINI_TRACK = 0.30


def gradient_bg():
    img = Image.new("RGB", (TILE_W, TILE_H))
    d = ImageDraw.Draw(img)
    for y in range(TILE_H):
        t = y / TILE_H
        c = tuple(int(TOP[i] + (BOT[i] - TOP[i]) * t) for i in range(3))
        d.line([(0, y), (TILE_W, y)], fill=c)
    # faint warm glow behind the tagline block
    glow = Image.new("L", (TILE_W, TILE_H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([TILE_W * -0.25, TILE_H * 0.18, TILE_W * 1.25, TILE_H * 0.72], fill=46)
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    warm = Image.new("RGB", (TILE_W, TILE_H), (255, 214, 180))
    img = Image.composite(warm, img, glow)
    return img


def line_widths(font, text, track_px):
    ws = []
    for ch in text:
        if ch == " ":
            ws.append(int(font.size * 0.30) + track_px)
        else:
            b = font.getbbox(ch)
            ws.append((b[2] - b[0]) + track_px)
    return ws


def draw_line(layer_draw, font, text, cx, y, track_px, fill):
    ws = line_widths(font, text, track_px)
    total = sum(ws) - track_px
    x = cx - total // 2
    for ch, w in zip(text, ws):
        if ch != " ":
            b = font.getbbox(ch)
            layer_draw.text((x - b[0], y), ch, font=font, fill=fill)
        x += w


def draw_text_block(img, lines):
    tag_font = ImageFont.truetype(FONT, TAG_SIZE)
    track_px = int(TAG_SIZE * TAG_TRACK)
    line_h = int(TAG_SIZE * LEADING)
    block_h = line_h * len(lines)
    y0 = (TILE_H - block_h) // 2 - int(TILE_H * 0.04)

    # shadow layer: same text, dark translucent, blurred, offset down
    shadow = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    y = y0
    for line in lines:
        draw_line(sd, tag_font, line, TILE_W // 2, y + 5, track_px, (40, 12, 5, 120))
        y += line_h
    shadow = shadow.filter(ImageFilter.GaussianBlur(6))
    img.paste(Image.new("RGB", img.size, (0, 0, 0)), (0, 0), shadow)

    d = ImageDraw.Draw(img)
    y = y0
    for line in lines:
        draw_line(d, tag_font, line, TILE_W // 2, y, track_px, CREAM)
        y += line_h

    # mini wordmark + underline
    mini_font = ImageFont.truetype(FONT, MINI_SIZE)
    mini_track = int(MINI_SIZE * MINI_TRACK)
    my = int(TILE_H * 0.80)
    ws = line_widths(mini_font, "SPORTIF", mini_track)
    total = sum(ws) - mini_track
    x = TILE_W // 2 - total // 2
    for ch, w in zip("SPORTIF", ws):
        b = mini_font.getbbox(ch)
        d.text((x - b[0], my), ch, font=mini_font, fill=CREAM)
        x += w
    cap = mini_font.getbbox("S")
    baseline = my + cap[3]
    rule_w = int(MINI_SIZE * 1.6)
    rx = (TILE_W - rule_w) // 2
    d.rectangle([rx, baseline + 18, rx + rule_w, baseline + 22], fill=CREAM)
    return img


def main():
    tiles = []
    for name, lines in TILES:
        img = draw_text_block(gradient_bg(), lines)
        img.save(f"{OUT}/sportif-{name}.png")
        tiles.append(img)

    g = 12
    row = Image.new("RGB", (TILE_W * 3 + g * 2, TILE_H), "#DDDDDD")
    for i, t in enumerate(tiles):
        row.paste(t, (i * (TILE_W + g), 0))
    row.thumbnail((1600, 1600))
    row.save(f"{OUT}/preview-tagline-row-v2.png")
    print("done")


if __name__ == "__main__":
    main()
