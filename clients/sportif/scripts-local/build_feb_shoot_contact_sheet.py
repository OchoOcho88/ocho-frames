"""Contact sheet for Lucy's February 2026 phone shoot (Dropbox, received S047).

Numbers every file in capture order, photos F01.. and videos V1.., so a picture can be
named in one word in an email ("F07?") instead of by its Dropbox file name. Orientation
comes from the EXIF flag, video frames are pulled at 1 s with ffmpeg (they are HLG HDR,
so the frames look flatter than the clip plays on a phone).

Run: .venvs/pdf/bin/python clients/sportif/scripts-local/build_feb_shoot_contact_sheet.py
Out: clients/sportif/assets/photoshoot-feb-2026/_contact-sheet.jpg (gitignored)
"""

import re
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1] / "assets" / "photoshoot-feb-2026"
OUT = ROOT / "_contact-sheet.jpg"
FONT = Path.home() / "Library/Fonts/GlacialIndifference-Regular.otf"

CELL, LABEL, GAP, COLS = 420, 44, 16, 8
BG, INK, SUB = (246, 238, 229), (74, 67, 60), (140, 128, 116)


def capture_key(p):
    """Sort by the time in the file name, 'Photo 18-2-2026, 1 44 14 pm (1).jpg'."""
    h, m, s = map(int, re.search(r", (\d+) (\d+) (\d+) pm", p.name).groups())
    return (h % 12 + 12) * 3600 + m * 60 + s, p.name


def video_frame(p, tmp):
    out = Path(tmp) / (p.stem + ".jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1", "-i", str(p),
                    "-frames:v", "1", str(out)], check=True)
    return Image.open(out)


def main():
    files = sorted([p for p in ROOT.iterdir() if p.suffix.lower() in (".jpg", ".mov")],
                   key=capture_key)
    font = ImageFont.truetype(str(FONT), 24)
    small = ImageFont.truetype(str(FONT), 18)
    rows = -(-len(files) // COLS)
    sheet = Image.new("RGB", (GAP + COLS * (CELL + GAP),
                              GAP + rows * (CELL + LABEL + GAP)), BG)
    draw = ImageDraw.Draw(sheet)
    f_n = v_n = 0
    with tempfile.TemporaryDirectory() as tmp:
        for i, p in enumerate(files):
            if p.suffix.lower() == ".mov":
                v_n += 1
                tag, im = f"V{v_n}", video_frame(p, tmp)
            else:
                f_n += 1
                tag, im = f"F{f_n:02d}", ImageOps.exif_transpose(Image.open(p))
            im = im.convert("RGB")
            im.thumbnail((CELL, CELL))
            x = GAP + (i % COLS) * (CELL + GAP)
            y = GAP + (i // COLS) * (CELL + LABEL + GAP)
            sheet.paste(im, (x + (CELL - im.width) // 2, y + (CELL - im.height) // 2))
            t = re.search(r", (\d+ \d+ \d+) pm", p.name).group(1).replace(" ", ":")
            dup = " (1)" if "(1)" in p.name else ""
            draw.text((x, y + CELL + 8), tag, font=font, fill=INK)
            draw.text((x + 70, y + CELL + 12), f"{t} pm{dup}", font=small, fill=SUB)
            print(f"{tag}\t{p.name}")
    sheet.save(OUT, quality=88)
    print(OUT, sheet.size)


if __name__ == "__main__":
    main()
