"""Lucy's Magnate View cover (March 2026) as a grid on her PERSONAL Instagram (S047).

Her ask, 25 Sep: "I would like to create a grid of my first cover from March on my Personal
Instagram." In her words a grid is a row of posts that reads as one picture on the profile (the
3-tile SPORTIF banner, S030). The only source is Magnate View's own post of the cover, 1201 px square
with the cover on a plum ground, so the cover itself is 812 x 1069. Two ways, built side by side:

  split   the cover cut into 3 x 3 (nine posts). Four times upscaled, and the seams run through the
          masthead and through her name.
  row     one row of three: the whole cover in the middle post, "On the cover of Magnate View" on
          the left, her philosophy line on the right (her words as reported in the interview, already
          in `lucy-content-library.md`). Nothing is cut and each post stands alone when tapped.

Tiles are 1080 x 1440 (3:4, the profile grid shape). File numbers are the posting order: POST-1
goes up first and lands on the right.

Run: .venvs/pdf/bin/python clients/sportif/scripts-local/build_magnate_cover_grid.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

SP = Path(__file__).resolve().parents[1]
SRC = SP / "assets/press/magnate-view-cover-2026-03-ig-post.jpg"
OUT = SP / "generated/images/magnate-cover-grid"   # gitignored; the file that is sent gets copied to lucy-personal/
COVER_BOX = (185, 65, 997, 1134)      # the cover inside Magnate View's square post, plum trimmed

TW, TH = 1080, 1440
CREAM, INK, BEIGE, SOFT = (247, 243, 238), (43, 37, 34), (207, 188, 167), (120, 110, 102)
SERIF = str(Path.home() / "Library/Fonts/CormorantGaramond-Regular.ttf")
SERIF_I = str(Path.home() / "Library/Fonts/CormorantGaramond-Italic.ttf")
SANS, SANS_I = "/System/Library/Fonts/Avenir Next.ttc", 5          # Avenir Next Medium

QUOTE = ["Confidence is not", "about perfection but", "about feeling good and", "showing up as oneself."]


def tracked(d, xy, text, font, fill, track, anchor_centre=True):
    w = sum(font.getlength(c) for c in text) + track * (len(text) - 1)
    x, y = xy
    if anchor_centre:
        x -= w / 2
    for c in text:
        d.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + track
    return w


UPSCALED = SP / "assets/press/magnate-view-cover-2026-03-crop-upscaled.png"   # Hugo's Adobe upscale, if present


def cover():
    """The cover alone. Uses Hugo's upscale of `magnate-view-cover-2026-03-crop.png` when it exists."""
    if UPSCALED.exists():
        return Image.open(UPSCALED).convert("RGB")
    return Image.open(SRC).convert("RGB").crop(COVER_BOX)


def split():
    c = cover()
    W, H = TW * 3, TH * 3
    scale = W / c.width
    big = c.resize((W, round(c.height * scale)), Image.LANCZOS)
    master = Image.new("RGB", (W, H), (6, 3, 4))
    master.paste(big, (0, (H - big.height) // 2))
    tiles = []
    for r in range(3):
        for col in range(3):
            tiles.append(master.crop((col * TW, r * TH, (col + 1) * TW, (r + 1) * TH)))
    return master, tiles, scale


def row():
    W, H = TW * 3, TH
    m = Image.new("RGB", (W, H), CREAM)
    c = cover()
    ch = 1250
    cw = round(c.width * ch / c.height)
    cv = c.resize((cw, ch), Image.LANCZOS)
    cx, cy = TW + (TW - cw) // 2, (H - ch) // 2
    # a soft shadow under the cover, the way Magnate View presents it
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).rectangle((cx + 10, cy + 24, cx + cw + 10, cy + ch + 24), fill=110)
    sh = sh.filter(ImageFilter.GaussianBlur(28))
    m.paste(Image.new("RGB", (W, H), (60, 48, 42)), (0, 0), sh)
    m.paste(cv, (cx, cy))
    d = ImageDraw.Draw(m)

    # left post: on the cover of
    lx = TW / 2
    small = ImageFont.truetype(SANS, 30, index=SANS_I)
    ital = ImageFont.truetype(SERIF_I, 76)
    big = ImageFont.truetype(SERIF, 132)
    mid = ImageFont.truetype(SANS, 34, index=SANS_I)
    y = 405
    tracked(d, (lx, y), "MARCH 2026", small, SOFT, 9)
    y += 92
    w = ital.getlength("On the cover of")
    d.text((lx - w / 2, y), "On the cover of", font=ital, fill=INK)
    y += 104
    for line in ("Magnate", "View"):
        w = big.getlength(line)
        d.text((lx - w / 2, y), line, font=big, fill=INK)
        y += 138
    y += 40
    d.line((lx - 70, y, lx + 70, y), fill=BEIGE, width=3)
    y += 44
    for line in ("THE 5 MOST IMPACTFUL", "LEADERS TO WATCH IN 2026"):
        tracked(d, (lx, y), line, mid, INK, 5)
        y += 54

    # right post: her line
    rx = TW * 2 + TW / 2
    q = ImageFont.truetype(SERIF_I, 78)
    y = 450
    for line in QUOTE:
        w = q.getlength(line)
        d.text((rx - w / 2, y), line, font=q, fill=INK)
        y += 96
    y += 44
    d.line((rx - 70, y, rx + 70, y), fill=BEIGE, width=3)
    y += 44
    tracked(d, (rx, y), "LUCY WAYNE", mid, INK, 9)

    tiles = [m.crop((i * TW, 0, (i + 1) * TW, TH)) for i in range(3)]
    return m, tiles, ch / c.height


def preview(tiles, cols, gap=4, width=1170, bg=(255, 255, 255)):
    rows = len(tiles) // cols
    tw = (width - gap * (cols - 1)) / cols
    th = tw * TH / TW
    p = Image.new("RGB", (width, round(rows * th + gap * (rows - 1))), bg)
    for i, t in enumerate(tiles):
        r, c = divmod(i, cols)
        p.paste(t.resize((round(tw), round(th)), Image.LANCZOS), (round(c * (tw + gap)), round(r * (th + gap))))
    return p


def save(name, master, tiles):
    d = OUT / name
    d.mkdir(parents=True, exist_ok=True)
    master.save(d / "master.png")
    # posting order: the last tile (bottom right) goes up first
    for n, t in enumerate(reversed(tiles), 1):
        t.save(d / f"POST-{n}.png")
    return d


# S048: her 27 Sep answer, "I would like the cover to be across three tiles", and on 29 Sep she
# sent the issue page. Its "Digital Version" is Magnate View's FlipHTML5 book of the issue
# (online.fliphtml5.com/bgtkc/pgty), whose page 1 is her cover at 1676 x 2200 with clean type:
# `assets/press/magnate-view-flipbook-cover-2026-03.png`. The best source found; the web upload on
# their site is 1000 px. Hugo's call: build both nine-post versions and let Lucy pick.
#   A  straight split, the whole cover edge to edge; the top row seam crosses her nose.
#   B  face whole, the cover dropped 190 px on its own black so the top seam runs through her fringe
#      above the brows; costs the foot of the barcode and bottom room under the subtitle.
# Scale 2.0 for both: the right column seam then runs through her hair clear of the ear, and the left
# one lands in the G|N gap of the masthead. Lanczos plus a light unsharp mask, no generator (D-066).
FLIP = SP / "assets/press/magnate-view-flipbook-cover-2026-03.png"
FLIP_TRIM = (2, 0, 1674, 2196)       # a light 1 px edge left and right, 3 px along the bottom
FLIP_SCALE = 2.0
DROP_B = 190                         # option B: the cover's own black added above the masthead


def flip_cover():
    return Image.open(FLIP).convert("RGB").crop(FLIP_TRIM)


def nine(drop):
    c = flip_cover()
    W, H = TW * 3, TH * 3
    big = c.resize((round(c.width * FLIP_SCALE), round(c.height * FLIP_SCALE)), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=2, percent=35, threshold=3))
    master = Image.new("RGB", (W, H), (0, 0, 0))      # the cover's top band is pure black
    master.paste(big, (0, drop))                       # overflow comes off the right and the bottom
    tiles = [master.crop((col * TW, r * TH, (col + 1) * TW, (r + 1) * TH)) for r in range(3) for col in range(3)]
    return master, tiles


#   C  the cover on cream (the ground of the row she called beautiful), tilted 2 degrees like a magazine
#      put down, placed so her face sits whole in the middle right post. The title goes in the top left
#      post and her line in the bottom left, each inside one post so no seam cuts the words.
C_SCALE, C_TILT = 1.40, -2.0         # PIL angle: negative is clockwise
FACE_BOX = (1083, 540, 1371, 875)    # ear to cheek, crown to chin, in trimmed flipbook pixels


def tilt_point(x, y, s, w, h, cx, cy):
    """Where cover pixel (x, y) lands on the canvas once scaled by s, tilted, and centred at (cx, cy)."""
    import math
    a = math.radians(-C_TILT)
    dx, dy = x * s - w / 2, y * s - h / 2
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


def cream_nine():
    c = flip_cover()
    W, H = TW * 3, TH * 3
    s = C_SCALE
    w, h = c.width * s, c.height * s
    # supersample: scale to 2s, tilt, come back down, so the edges are clean
    big = c.resize((round(w * 2), round(h * 2)), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=3, percent=35, threshold=3)).convert("RGBA")
    big = big.rotate(C_TILT, resample=Image.BICUBIC, expand=True)
    cv = big.resize((round(big.width / 2), round(big.height / 2)), Image.LANCZOS)

    # place it: face just inside the middle right post (seam through the hair, as in A and B)
    corners = [(FACE_BOX[0], FACE_BOX[1]), (FACE_BOX[2], FACE_BOX[1]), (FACE_BOX[0], FACE_BOX[3]), (FACE_BOX[2], FACE_BOX[3])]
    pts = [tilt_point(x, y, s, w, h, 0, 0) for x, y in corners]
    cx = TW * 2 + 25 - min(p[0] for p in pts)
    cy = TH + 30 - min(p[1] for p in pts)
    x0, y0 = round(cx - cv.width / 2), round(cy - cv.height / 2)

    m = Image.new("RGB", (W, H), CREAM)
    sh = Image.new("L", (W, H), 0)
    sh.paste(cv.getchannel("A").point(lambda v: v * 110 // 255), (x0 + 10, y0 + 24))
    sh = sh.filter(ImageFilter.GaussianBlur(28))
    m.paste(Image.new("RGB", (W, H), (60, 48, 42)), (0, 0), sh)
    m.paste(cv, (x0, y0), cv)
    d = ImageDraw.Draw(m)

    left, right = x0, W - (x0 + cv.width)
    top, bottom = y0, H - (y0 + cv.height)
    face = [tilt_point(x, y, s, w, h, cx, cy) for x, y in corners]
    print(f"C: margins left {left} right {right} top {top} bottom {bottom}; face x "
          f"{min(p[0] for p in face):.0f}-{max(p[0] for p in face):.0f}, y {min(p[1] for p in face):.0f}-{max(p[1] for p in face):.0f}")

    # top left post: the title, centred in the cream above the cover (the date is on the cover itself)
    lx = TW / 2
    ital = ImageFont.truetype(SERIF_I, 74)
    big_t = ImageFont.truetype(SERIF, 124)
    block = 74 + 18 + 124
    y = (top - block) / 2 - 10
    t = "On the cover of"
    d.text((lx - ital.getlength(t) / 2, y), t, font=ital, fill=INK)
    y += 74 + 18
    t = "Magnate View"
    d.text((lx - big_t.getlength(t) / 2, y), t, font=big_t, fill=INK)
    print(f"C: title ends near y {y + 150:.0f}, cover top {top}")

    # bottom left post: her line, in the margin beside the cover
    qx = left / 2
    size = 60
    while max(ImageFont.truetype(SERIF_I, size).getlength(l) for l in QUOTE) > left - 110:
        size -= 2
    q = ImageFont.truetype(SERIF_I, size)
    lh = round(size * 1.25)
    y = TH * 2 + 380
    for line in QUOTE:
        d.text((qx - q.getlength(line) / 2, y), line, font=q, fill=INK)
        y += lh
    y += 30
    d.line((qx - 50, y, qx + 50, y), fill=BEIGE, width=3)
    y += 34
    tracked(d, (qx, y), "LUCY WAYNE", ImageFont.truetype(SANS, 26, index=SANS_I), INK, 7)
    print(f"C: quote at {size}px, column {left} wide")

    tiles = [m.crop((col * TW, r * TH, (col + 1) * TW, (r + 1) * TH)) for r in range(3) for col in range(3)]
    return m, tiles


def main_flip():
    sheets = []
    for name, drop in (("option-A-nine-straight", 0), ("option-B-nine-face-whole", DROP_B)):
        m, t = nine(drop)
        save(name, m, t)
        p = preview(t, 3)
        p.save(OUT / name / "grid-preview.jpg", quality=90)
        sheets.append(p)
    m, t = cream_nine()
    save("option-C-nine-on-cream", m, t)
    p = preview(t, 3)
    p.save(OUT / "option-C-nine-on-cream/grid-preview.jpg", quality=90)
    sheets.append(p)
    sheet = Image.new("RGB", (sheets[0].width * 3 + 160, sheets[0].height), (255, 255, 255))
    for i, p in enumerate(sheets):
        sheet.paste(p, (i * (p.width + 80), 0))
    sheet.save(OUT / "COMPARE-A-B-C.jpg", quality=90)
    print(f"from the flipbook cover, A and B at {FLIP_SCALE}x, C at {C_SCALE}x ->", OUT)


def main():
    sm, st, s1 = split()
    rm, rt, s2 = row()
    save("option-split-3x3", sm, st)
    save("option-row-of-three", rm, rt)
    a, b = preview(st, 3), preview(rt, 3)
    sheet = Image.new("RGB", (a.width * 2 + 80, max(a.height, b.height)), (255, 255, 255))
    sheet.paste(a, (0, 0))
    sheet.paste(b, (a.width + 80, 0))
    sheet.save(OUT / "COMPARE-split-vs-row.jpg", quality=90)
    b.save(OUT / "option-row-of-three/grid-preview.jpg", quality=90)
    a.save(OUT / "option-split-3x3/grid-preview.jpg", quality=90)
    src = "Hugo's upscale" if UPSCALED.exists() else "the 812 px cover"
    print(f"from {src}: split scale {s1:.2f}x, row scale {s2:.2f}x ->", OUT)


if __name__ == "__main__":
    import sys
    main_flip() if "--flip" in sys.argv else main()
