"""Lift Lucy's "Lucy Wayne" signature out of the Canva email-signature PDF as vector.

Q-034. Her Canva is a free account, so SVG export is locked and PNG is capped at the
400x150 canvas with no transparency. PDF Print is free and keeps the text live, so the
signature comes out as real outlines at any size.

What the PDF holds (checked S042): "Lucy Wayne" is live text in an embedded subset of
Amsterdam-Two at 16pt. We convert it to PATHS here rather than extracting the font file.
That keeps us inside Canva's export licence, which covers the artwork, not the typeface.

Run:  python3 extract_lucy_signature.py
"""
from pathlib import Path
import re

import fitz
import numpy as np
from PIL import Image


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / 'brand/fonts/glacial-indifference').is_dir():
            return p
    raise SystemExit('could not locate the hyperframes root')


ROOT = find_root(Path(__file__).resolve())
BASE = ROOT / 'clients/sportif/email-signature-motion'
SRC = BASE / 'from-canva/Lucy Wayne Email Signature.pdf'
OUT = BASE / 'signature'

# The headshot's top edge. Everything above it on page 1 is the signature and nothing
# else: the divider, the rule under BOOK A CALL and the stray right-hand shape all sit
# lower or further right. Verified against page.get_drawings() and get_image_info().
SIG_FLOOR_PT = 54.7
MARGIN_PT = 2.0
PNG_WIDTH = 2400          # transparent master, plenty for a 1080 end card or print


def ink_bbox(page, floor, scale=8):
    """True ink extent, which is wider than the text bbox because Amsterdam Two's
    swashes overflow the advance width on both sides."""
    page.set_cropbox(fitz.Rect(0, 0, page.rect.width, floor))
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    ys, xs = np.where(a.min(axis=2) < 200)
    if not len(xs):
        raise SystemExit('no ink found above the headshot')
    return fitz.Rect(xs.min() / scale, ys.min() / scale,
                     xs.max() / scale + 1 / scale, ys.max() / scale + 1 / scale)



INK_HEX = '#0e0f0b'
SIG_FONT = 'font_12'      # the Amsterdam Two run; font_11/14/16 are the Canva Sans blocks


def flatten_signature(svg, font=SIG_FONT, ink=INK_HEX):
    """PyMuPDF's text_as_path does NOT emit flat paths: it writes each glyph once into
    <defs> and instances it with <use xlink:href>. Illustrator imports that as symbol
    instances, and because Amsterdam Two is not installed anywhere it would also flag a
    missing font. So resolve every <use> of the signature's font into a real <path>,
    carrying the use's own transform, and drop the rest of the page.

    Returns (svg, glyph_count).
    """
    glyphs = dict(re.findall(r'<path id="(%s_\d+)" d="([^"]+)"' % font, svg))
    uses = re.findall(
        r'<use data-text="(.)" xlink:href="#(%s_\d+)"[^>]*transform="([^"]+)"[^>]*/>' % font,
        svg)
    head = re.match(r'<svg[^>]*>', svg).group(0)

    out = [head]
    n = 0
    for ch, gid, tf in uses:
        d = glyphs.get(gid)
        if not d:                       # the space has no outline
            continue
        out.append(f'<path data-text="{ch}" transform="{tf}" fill="{ink}" d="{d}"/>')
        n += 1
    out.append('</svg>')
    return '\n'.join(out), n


def write_ae_artboard(svg, out_path, page_w=1080, page_h=1920, frac=0.76):
    """A signature-only page at comp size, vector, with NO embedded fonts.

    Built from the FLATTENED svg, not from the Canva pdf. show_pdf_page would clip the
    source page visually but carry its resources, so the artboard would still hold all
    four Canva fonts, the nine page drawings and the headshot, and Illustrator would ask
    for Amsterdam Two on open. Going via the outlines leaves pure geometry.

    AI and PDF map 1pt to 1px at 72ppi, so this imports into After Effects at exactly
    page_w x page_h with no scaling.
    """
    svgdoc = fitz.open(stream=svg.encode(), filetype='svg')
    src = fitz.open('pdf', svgdoc.convert_to_pdf())
    sr = src[0].rect

    doc = fitz.open()
    pg = doc.new_page(width=page_w, height=page_h)
    w = page_w * frac
    h = w * (sr.height / sr.width)
    box = fitz.Rect((page_w - w) / 2, (page_h - h) / 2,
                    (page_w + w) / 2, (page_h + h) / 2)
    pg.show_pdf_page(box, src, 0)
    doc.save(out_path)
    return box, len(doc[0].get_fonts())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(SRC)
    page = doc[0]

    bb = ink_bbox(page, SIG_FLOOR_PT)
    crop = fitz.Rect(bb.x0 - MARGIN_PT, bb.y0 - MARGIN_PT,
                     bb.x1 + MARGIN_PT, bb.y1 + MARGIN_PT)
    print(f'ink   {bb.x0:.2f},{bb.y0:.2f} to {bb.x1:.2f},{bb.y1:.2f}  '
          f'({bb.width:.2f} x {bb.height:.2f} pt)')
    print(f'crop  {crop.width:.2f} x {crop.height:.2f} pt, {MARGIN_PT}pt margin')

    page.set_cropbox(crop)

    # SVG, text converted to paths.
    # get_svg_image emits the WHOLE page clipped to the crop, so the file also carries
    # Canva's white background rects and the blue BOOK A CALL paths sitting outside the
    # visible area, plus a stack of clipPaths. In Illustrator those land as stray objects
    # and clipping groups. Keep the ink and nothing else.
    svg = page.get_svg_image(matrix=fitz.Matrix(8, 8), text_as_path=True)
    svg = re.sub(r'<image.*?(?:/>|</image>)', '', svg, flags=re.S)
    (OUT / 'lucy-wayne-signature-raw.svg').write_text(svg)
    clean, kept = flatten_signature(svg)
    (OUT / 'lucy-wayne-signature.svg').write_text(clean)
    print(f'svg   {kept} glyph outlines flattened, {len(clean)} bytes')

    # Transparent PNG master.
    # NOTE alpha=True on get_pixmap does NOT give transparency here: the Canva page
    # carries two full-page white rects, so every pixel comes back opaque. The art is a
    # single ink colour over pure white, so we invert the composite instead, which is
    # exact and keeps the anti-aliased edges honest:
    #     P = a*C + (1-a)*255   ->   a = (255-P) / (255-C)
    scale = PNG_WIDTH / crop.width
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    a = a[..., :3].astype(np.float64)

    core = a[a.min(axis=2) < 30]
    ink = core.mean(axis=0)                      # the real ink colour, not assumed black
    d = 255.0 - ink
    alpha = ((255.0 - a) * d).sum(axis=2) / (d * d).sum()
    alpha = np.clip(alpha, 0.0, 1.0)

    out = np.zeros((*alpha.shape, 4), dtype=np.uint8)
    out[..., :3] = np.round(ink).astype(np.uint8)
    out[..., 3] = np.round(alpha * 255).astype(np.uint8)
    png = OUT / 'lucy-wayne-signature.png'
    Image.fromarray(out).save(png)
    box, nf = write_ae_artboard(clean, OUT / 'lucy-wayne-signature-1080x1920.pdf')
    print(f'ae    1080x1920 pdf, signature {box.width:.0f} x {box.height:.0f} px centred, '
          f'{nf} embedded fonts')
    print(f'png   {pix.width} x {pix.height}, ink rgb {tuple(np.round(ink).astype(int))}, '
          f'alpha {out[...,3].min()} to {out[...,3].max()} -> {png.name}')


if __name__ == '__main__':
    main()
