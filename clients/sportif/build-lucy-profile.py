#!/usr/bin/env python3
"""Build the Lucy-facing profile PDF from lucy-profile.md + lucy-content-library.md.

On-brand (warm palette, Glacial Indifference embedded), rendered to PDF via headless
Chrome (weasyprint is not on the Mac). Sources are the two markdown files; this is the
render step. Re-run after editing either file.

    python3 clients/sportif/build-lucy-profile.py
"""
import base64, html, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
FONTS = os.path.join(ROOT, 'brand/fonts/glacial-indifference')
PROFILE = os.path.join(HERE, 'lucy-profile.md')
LIBRARY = os.path.join(HERE, 'lucy-content-library.md')
OUT_HTML = os.path.join(HERE, 'lucy-profile-for-review.html')
OUT_PDF = os.path.join(HERE, 'lucy-profile-for-review.pdf')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def font_b64(name):
    with open(os.path.join(FONTS, name), 'rb') as f:
        return base64.b64encode(f.read()).decode()


def inline(t):
    t = html.escape(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', t)
    return t


def md_to_html(md):
    out, lines = [], md.split('\n')
    para, quote, items, oitems = [], [], [], []
    OL = re.compile(r'^\d+\.\s+(.*)$')

    def flush_para():
        if para: out.append('<p>' + ' '.join(inline(x) for x in para) + '</p>'); para.clear()

    def flush_quote():
        if quote: out.append('<blockquote>' + ' '.join(inline(x) for x in quote) + '</blockquote>'); quote.clear()

    def flush_items():
        if items:
            out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>'); items.clear()

    def flush_oitems():
        if oitems:
            out.append('<ol>' + ''.join(f'<li>{inline(x)}</li>' for x in oitems) + '</ol>'); oitems.clear()

    def flush_all():
        flush_para(); flush_quote(); flush_items(); flush_oitems()

    for ln in lines:
        s = ln.rstrip()
        if not s.strip():
            flush_all(); continue
        om = OL.match(s)
        if s.startswith('### '):
            flush_all(); out.append(f'<h3>{inline(s[4:])}</h3>')
        elif s.startswith('## '):
            flush_all(); out.append(f'<h2>{inline(s[3:])}</h2>')
        elif s.startswith('# '):
            flush_all(); out.append(f'<h1>{inline(s[2:])}</h1>')
        elif s.strip() == '---':
            flush_all(); out.append('<hr>')
        elif s.startswith('> '):
            flush_para(); flush_items(); flush_oitems(); quote.append(s[2:])
        elif s.startswith('- '):
            flush_para(); flush_quote(); flush_oitems(); items.append(s[2:])
        elif om:
            flush_para(); flush_quote(); flush_items(); oitems.append(om.group(1))
        else:
            flush_quote(); flush_items(); flush_oitems(); para.append(s.strip())
    flush_all()
    return '\n'.join(out)


profile_html = md_to_html(open(PROFILE).read())
# drop the library's own leading H1 so the section band reads cleanly
lib_src = open(LIBRARY).read()
library_html = md_to_html(lib_src)

CSS = """
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
@page { size: A4; margin: 20mm 18mm 18mm; }
@font-face { font-family: 'Glacial'; font-weight: 400; src: url(data:font/otf;base64,__REG__); }
@font-face { font-family: 'Glacial'; font-weight: 700; src: url(data:font/otf;base64,__BOLD__); }
@font-face { font-family: 'GlacialI'; font-style: italic; src: url(data:font/otf;base64,__ITAL__); }
body { font-family: 'Glacial', sans-serif; color: #4A433C; background: #FBF7F2;
       line-height: 1.62; font-size: 11.4pt; margin: 0; }
.cover { text-align: center; padding: 6mm 0 4mm; border-bottom: 1px solid #E3D4C4; margin-bottom: 7mm; }
.wordmark { font-weight: 700; letter-spacing: .34em; color: #833827; font-size: 15pt; }
.wordmark .rule { display:block; width:42px; height:3px; background:#833827; margin:6px auto 0; }
.kicker { color:#C6926E; letter-spacing:.16em; text-transform:uppercase; font-size:8.6pt; margin-top:11mm; }
h1 { font-weight:700; color:#833827; font-size:23pt; letter-spacing:.005em; margin:.1em 0 .15em; line-height:1.1; }
.subtitle { color:#6b6258; font-size:10.4pt; max-width:150mm; margin:0 auto; }
h2 { font-weight:700; color:#4A433C; font-size:14pt; margin:9mm 0 2.5mm; padding:2mm 0 2mm 4mm;
     border-left:4px solid #833827; background:#F5E7DA; letter-spacing:.01em; break-after:avoid; }
h3 { font-weight:700; color:#833827; font-size:11.6pt; margin:5mm 0 1.5mm; }
p { margin:.5em 0; }
strong { font-weight:700; color:#4A433C; }
em { font-family:'GlacialI', serif; font-style:italic; }
ul { list-style:none; margin:.4em 0; padding:0; }
li { position:relative; padding-left:1.15em; margin:.34em 0; break-inside:avoid; }
li:before { content:''; position:absolute; left:.1em; top:.62em; width:.42em; height:.42em;
            background:#C6926E; border-radius:50%; }
ol { margin:.4em 0; padding-left:1.4em; }
ol li { position:static; padding-left:.2em; margin:.4em 0; break-inside:avoid; }
ol li:before { display:none; }
ol li::marker { color:#833827; font-weight:700; }
blockquote { font-family:'GlacialI', serif; font-style:italic; color:#5c5349; margin:.6em 0;
             padding:2.4mm 4mm; border-left:3px solid #C6926E; background:#FDF4EA; font-size:11.6pt;
             break-inside:avoid; }
hr { border:none; border-top:1px solid #E3D4C4; margin:7mm 0; }
.libwrap { break-before:page; }
.note { margin-top:9mm; padding-top:4mm; border-top:1px solid #E3D4C4; color:#8a8177; font-size:8.8pt; text-align:center; }
"""
CSS = (CSS.replace('__REG__', font_b64('GlacialIndifference-Regular.otf'))
          .replace('__BOLD__', font_b64('GlacialIndifference-Bold.otf'))
          .replace('__ITAL__', font_b64('GlacialIndifference-Italic.otf')))

DOC = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover">
  <div class="wordmark">SPORTIF<span class="rule"></span></div>
  <div class="kicker">Founder profile, working draft</div>
  <h1>Who is Lucy Wayne</h1>
  <div class="subtitle">A portrait drawn from Lucy's published interviews, and a starting point for her content. Nothing here is fixed. It is meant for Lucy to read and react to.</div>
</div>
{profile_html.split('</h1>',1)[-1] if '</h1>' in profile_html else profile_html}
<div class="libwrap">{library_html}</div>
<div class="note">Working draft prepared for Lucy Wayne. Taglines and the marked draft lines are for approval before use.</div>
</body></html>"""

with open(OUT_HTML, 'w', encoding='utf-8') as f:
    f.write(DOC)
print('wrote', os.path.relpath(OUT_HTML, ROOT))

if not os.path.exists(CHROME):
    sys.exit('Chrome not found; open the HTML and Print to PDF manually.')

for flag in ('--headless=new', '--headless'):
    if os.path.exists(OUT_PDF):
        os.remove(OUT_PDF)
    subprocess.run([CHROME, flag, '--disable-gpu', '--no-pdf-header-footer',
                    f'--print-to-pdf={OUT_PDF}', f'file://{OUT_HTML}'],
                   capture_output=True, timeout=90)
    if os.path.exists(OUT_PDF) and os.path.getsize(OUT_PDF) > 1000:
        print('wrote', os.path.relpath(OUT_PDF, ROOT), f'({os.path.getsize(OUT_PDF)} bytes)')
        break
else:
    sys.exit('Chrome render failed; open the HTML and Print to PDF manually.')
