#!/usr/bin/env python3
"""Build the 3 standalone tagline tiles for the Sportif Instagram grid.

Row sits ABOVE the SPORTIF banner row: terracotta background, cream tagline,
mini letter-spaced SPORTIF wordmark with underline at the base of each tile.
Also renders a 2-row grid preview (tagline row over the peach banner row).
"""

from PIL import Image, ImageDraw, ImageFont

TERRACOTTA = "#833827"
CREAM = "#F6EEE5"
FONT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf"
OUT = "/sessions/cool-inspiring-shannon/mnt/hyperframes/clients/sportif/generated/images/grid-banner"

TILE_W, TILE_H = 1080, 1440

# left-to-right in the finished grid; post order is reversed (right first)
TILES = [
    ("tagline-1-left", ["Everyday training,", "elevated."]),
    ("tagline-2-centre", ["Too fashionable", "not to WEAR!"]),
    ("tagline-3-right", ["For your", "morning ritual."]),
]

TAG_SIZE = 96
TAG_TRACK = 0.06   # gentle tracking for the tagline
LEADING = 1.45
MINI_SIZE = 44
MINI_TRACK = 0.30  # wordmark tracking, matches the banner


def tracked_width(font, text, track_px):
    w = 0
    for ch in text:
        b = font.getbbox(ch)
        w += (b[2] - b[0]) + track_px
    return w - track_px if text else 0


def draw_tracked(d, font, text, cx, y, track_px, fill):
    total = tracked_width(font, text, track_px)
    x = cx - total // 2
    for ch in text:
        b = font.getbbox(ch)
        if ch != " ":
            d.text((x - b[0], y), ch, font=font, fill=fill)
        x += (b[2] - b[0]) + track_px


def space_fix(font, track_px):
    # give spaces a real advance (getbbox on " " is empty)
    return int(font.size * 0.30) + track_px


def draw_line(d, font, text, cx, y, track_px, fill):
    # like draw_tracked but with proper space advances
    widths = []
    for ch in text:
        if ch == " ":
            widths.append(space_fix(font, track_px))
        else:
            b = font.getbbox(ch)
            widths.append((b[2] - b[0]) + track_px)
    total = sum(widths) - track_px
    x = cx - total // 2
    for ch, w in zip(text, widths):
        if ch != " ":
            b = font.getbbox(ch)
            d.text((x - b[0], y), ch, font=font, fill=fill)
        x += w


def build_tile(name, lines):
    img = Image.new("RGB", (TILE_W, TILE_H), TERRACOTTA)
    d = ImageDraw.Draw(img)
    tag_font = ImageFont.truetype(FONT, TAG_SIZE)
    track_px = int(TAG_SIZE * TAG_TRACK)

    line_h = int(TAG_SIZE * LEADING)
    block_h = line_h * len(lines)
    y = (TILE_H - block_h) // 2 - int(TILE_H * 0.04)
    for line in lines:
        draw_line(d, tag_font, line, TILE_W // 2, y, track_px, CREAM)
        y += line_h

    # mini wordmark + underline near the bottom
    mini_font = ImageFont.truetype(FONT, MINI_SIZE)
    mini_track = int(MINI_SIZE * MINI_TRACK)
    my = int(TILE_H * 0.80)
    draw_tracked(d, mini_font, "SPORTIF", TILE_W // 2, my, mini_track, CREAM)
    cap = mini_font.getbbox("S")
    baseline = my + cap[3]
    rule_w = int(MINI_SIZE * 1.6)
    rx = (TILE_W - rule_w) // 2
    d.rectangle([rx, baseline + 18, rx + rule_w, baseline + 22], fill=CREAM)

    img.save(f"{OUT}/sportif-{name}.png")
    return img


def main():
    tiles = [build_tile(n, l) for n, l in TILES]

    # row preview
    g = 12
    row = Image.new("RGB", (TILE_W * 3 + g * 2, TILE_H), "#DDDDDD")
    for i, t in enumerate(tiles):
        row.paste(t, (i * (TILE_W + g), 0))
    row.thumbnail((1600, 1600))
    row.save(f"{OUT}/preview-tagline-row.png")

    # full 2-row grid preview over the peach banner row
    banner = Image.open(f"{OUT}/sportif-grid-banner-full-peach.png")
    full = Image.new("RGB", (TILE_W * 3 + g * 2, TILE_H * 2 + g), "#DDDDDD")
    for i, t in enumerate(tiles):
        full.paste(t, (i * (TILE_W + g), 0))
    for i in range(3):
        bt = banner.crop((i * TILE_W, 0, (i + 1) * TILE_W, TILE_H))
        full.paste(bt, (i * (TILE_W + g), TILE_H + g))
    full.thumbnail((1400, 1400))
    full.save(f"{OUT}/preview-full-grid-2rows.png")
    print("done")


if __name__ == "__main__":
    main()
