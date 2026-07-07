# -*- coding: utf-8 -*-
"""
Generator for the client-facing Sportif Launch Plan PDF (operations).
Pairs with the Brand Value Plan (strategy). Reads launch-plan-client.md.
Includes an SVG "how it all connects" diagram. Run: python3 build-launch-plan.py
"""
import re, html, os, tempfile
from PIL import Image
from weasyprint import HTML

SPORTIF = os.path.dirname(os.path.abspath(__file__))
HYPER   = os.path.dirname(os.path.dirname(SPORTIF))
MD      = os.path.join(SPORTIF, "launch-plan-client.md")
SRC_FLOW= os.path.join(HYPER, "experiments/2026-05-29-bahe-flowloops/results/FLOW.png")
OUT     = os.path.join(SPORTIF, "Sportif-Launch-Plan.pdf")
FLOW    = os.path.join(tempfile.gettempdir(), "sportif_flow_clean.png")

im = Image.open(SRC_FLOW).convert("RGB"); w, h = im.size
im.crop((0, 268, w, h)).save(FLOW)

raw = open(MD, encoding="utf-8").read()

def inline(t):
    t = html.escape(t.strip())
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`(.+?)`", r'<span class="mono">\1</span>', t)
    return t

# intro = last blockquote group in preamble
preamble = raw.split("\n## ", 1)[0]
groups, cur = [], []
for line in preamble.splitlines():
    if line.startswith(">"): cur.append(line.lstrip("> ").strip())
    elif cur: groups.append(" ".join(cur)); cur = []
if cur: groups.append(" ".join(cur))
intro = groups[-1] if groups else ""

DIAGRAM = '''<svg viewBox="0 0 720 350" xmlns="http://www.w3.org/2000/svg" class="dgm">
<style>
 .lbl{font-family:'Poppins',sans-serif;fill:#C6926E;font-size:12px;font-weight:600;letter-spacing:2px;}
 .pill{font-family:'Poppins',sans-serif;fill:#4A433C;font-size:12px;font-weight:500;}
 .cap{font-family:'Poppins',sans-serif;fill:#C6926E;font-size:11px;font-style:italic;}
 .shopA{font-family:'Poppins',sans-serif;fill:#F6EEE5;font-size:14px;font-weight:600;letter-spacing:.5px;}
 .shopB{font-family:'Poppins',sans-serif;fill:#F6EEE5;font-size:12px;}
 .shopC{font-family:'Poppins',sans-serif;fill:#F6EEE5;font-size:9.5px;opacity:.95;}
 .out{font-family:'Poppins',sans-serif;fill:#2D1814;font-size:12px;font-weight:600;}
 .sub{font-family:'Poppins',sans-serif;fill:#8a7a6c;font-size:9px;}
 .loop{font-family:'Poppins',sans-serif;fill:#833827;font-size:9px;font-weight:500;}
</style>
<text x="360" y="18" text-anchor="middle" class="lbl">WHERE PEOPLE FIND US</text>
<rect x="30" y="30" width="660" height="52" rx="12" fill="#FFFBF8" stroke="#C6926E" stroke-opacity=".45"/>
<g>
 <rect x="44"  y="43" width="118" height="26" rx="13" fill="#F0CDB3"/><text x="103" y="60" text-anchor="middle" class="pill">Instagram</text>
 <rect x="174" y="43" width="118" height="26" rx="13" fill="#F0CDB3"/><text x="233" y="60" text-anchor="middle" class="pill">TikTok</text>
 <rect x="304" y="43" width="118" height="26" rx="13" fill="#F0CDB3"/><text x="363" y="60" text-anchor="middle" class="pill">Lucy</text>
 <rect x="434" y="43" width="118" height="26" rx="13" fill="#F0CDB3"/><text x="493" y="60" text-anchor="middle" class="pill">Ambassadors</text>
 <rect x="564" y="43" width="118" height="26" rx="13" fill="#F0CDB3"/><text x="623" y="60" text-anchor="middle" class="pill">A little paid</text>
</g>
<text x="360" y="100" text-anchor="middle" class="cap">one tap: link in bio or a tagged product</text>
<line x1="360" y1="106" x2="360" y2="122" stroke="#C6926E" stroke-width="2"/>
<polygon points="353,120 367,120 360,130" fill="#C6926E"/>
<rect x="200" y="130" width="320" height="74" rx="14" fill="#833827"/>
<text x="360" y="158" text-anchor="middle" class="shopA">THE SHOP  +  EMAIL LIST</text>
<text x="360" y="177" text-anchor="middle" class="shopB">sportifcollection.com.au</text>
<text x="360" y="193" text-anchor="middle" class="shopC">powered by Shopify</text>
<text x="360" y="221" text-anchor="middle" class="cap">it becomes</text>
<line x1="360" y1="206" x2="360" y2="210" stroke="#C6926E" stroke-width="2"/>
<polygon points="353,210 367,210 360,220" fill="#C6926E"/>
<rect x="140" y="232" width="180" height="36" rx="18" fill="#F6EEE5" stroke="#C6926E" stroke-opacity=".5"/>
<text x="230" y="255" text-anchor="middle" class="out">A sale</text>
<rect x="350" y="232" width="230" height="36" rx="18" fill="#F6EEE5" stroke="#C6926E" stroke-opacity=".5"/>
<text x="465" y="251" text-anchor="middle" class="out">An email we keep</text>
<text x="465" y="263" text-anchor="middle" class="sub">the owned audience</text>
<path d="M598,250 C695,210 695,95 632,60" fill="none" stroke="#833827" stroke-width="2" stroke-dasharray="1 0"/>
<polygon points="624,52 642,58 628,70" fill="#833827"/>
<text x="612" y="150" class="loop">customers +</text>
<text x="612" y="163" class="loop">ambassadors</text>
<text x="612" y="176" class="loop">loop back</text>
<text x="360" y="300" text-anchor="middle" class="lbl" style="fill:#C6926E">ALONGSIDE</text>
<rect x="170" y="308" width="380" height="34" rx="17" fill="#F0CDB3"/>
<text x="360" y="330" text-anchor="middle" class="pill">Wholesale: Lucy's gyms, in person, in parallel</text>
</svg>'''

secs = re.split(r"\n## ", raw)[1:]
cards = []
for s in secs:
    head, _, body = s.partition("\n")
    idea, bullets, has_dgm = "", [], False
    for ln in body.splitlines():
        t = ln.strip()
        if t == "{{DIAGRAM}}": has_dgm = True; continue
        if re.match(r"^\*[^*].*\*$", t): idea = t.strip("*").strip(); continue
        if t.startswith("- "): bullets.append(t[2:].strip())
    cards.append(dict(title=head.strip(), idea=idea, bullets=bullets, dgm=has_dgm))

def ul(items):
    return '<ul class="blts">' + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"

body_html = ""
for C in cards:
    idea = f'<div class="idea">{inline(C["idea"])}</div>' if C["idea"] else ""
    dgm  = f'<div class="dgmwrap">{DIAGRAM}</div>' if C["dgm"] else ""
    body_html += f'<div class="card"><div class="sec">{html.escape(C["title"])}</div>{idea}{dgm}{ul(C["bullets"])}</div>'

DOC = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:19mm 17mm 16mm 17mm; }}
@page cover {{ margin:0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
:root{{ --peach:#F0CDB3; --caramel:#C6926E; --terr:#833827; --choc:#2D1814;
        --cream:#F6EEE5; --linen:#FFFBF8; --charcoal:#4A433C; --line:rgba(198,146,110,.34); }}
body{{ font-family:'Poppins',sans-serif; color:var(--charcoal); font-size:10.6pt; line-height:1.5; }}
strong{{ font-weight:600; color:var(--choc); }}
.cover{{ page:cover; width:210mm; height:297mm; position:relative; overflow:hidden; background:var(--cream); }}
.cover .photo{{ position:absolute; top:0; right:0; bottom:0; width:53%; overflow:hidden; }}
.cover .photo img{{ width:100%; height:100%; object-fit:cover; object-position:center 40%; display:block; }}
.cover .col{{ position:absolute; top:0; left:0; bottom:0; width:47%; padding:19mm 15mm 16mm 18mm; display:flex; flex-direction:column; }}
.cover .mast{{ font-weight:600; letter-spacing:.42em; text-transform:uppercase; color:var(--terr); font-size:11.5pt; }}
.cover .rule{{ width:16mm; height:2px; background:var(--terr); margin-bottom:8mm; }}
.cover .title{{ font-family:'Lora',serif; font-weight:600; color:var(--choc); font-size:35pt; line-height:1.03; }}
.cover .sub{{ font-weight:300; font-size:11.5pt; line-height:1.5; margin-top:7mm; }}
.cover .foot{{ font-weight:300; font-size:8pt; letter-spacing:.03em; color:var(--caramel); border-top:1px solid var(--line); padding-top:5mm; line-height:1.6; }}
.grow{{ flex:1; }}
.intro{{ background:var(--linen); border-left:3px solid var(--terr); border-radius:4px 10px 10px 4px; padding:6.5mm 8mm; margin-bottom:8mm; font-size:12pt; line-height:1.55; }}
.intro .kick{{ font-weight:600; color:var(--terr); }}
.card{{ background:var(--linen); border:1px solid var(--line); border-radius:12px; padding:7mm 8mm; margin-bottom:6mm; break-inside:avoid; }}
.sec{{ font-family:'Lora',serif; font-weight:600; font-size:15pt; color:var(--choc); margin-bottom:3.5mm; letter-spacing:0; text-transform:none; }}
.idea{{ font-style:italic; color:var(--caramel); font-size:10.6pt; margin-bottom:4mm; line-height:1.45; }}
.dgmwrap{{ margin:2mm 0 5mm; }}
svg.dgm{{ width:100%; height:auto; display:block; }}
ul.blts{{ margin:0 0 0 4.8mm; }}
ul.blts li{{ margin-bottom:2.4mm; padding-left:1.5mm; line-height:1.46; }}
ul.blts li::marker{{ color:var(--caramel); }}
</style></head><body>
<div class="cover">
  <div class="photo"><img src="file://{FLOW}"></div>
  <div class="col">
    <div class="mast">Sportif</div><div class="grow"></div>
    <div class="rule"></div>
    <div class="title">The<br>Launch<br>Plan</div>
    <div class="sub">How the brand becomes a business: one hub, and the path to September.</div>
    <div class="grow"></div>
    <div class="foot">Prepared for Sportif&nbsp;&middot;&nbsp;by Ocho&nbsp;&middot;&nbsp;July 2026<br>Read alongside the Brand Kit and the Brand Value Plan</div>
  </div>
</div>
<div class="intro"><span class="kick">In one line.</span> {inline(intro)}</div>
{body_html}
</body></html>"""

HTML(string=DOC).write_pdf(OUT)
print("sections:", len(cards), "->", OUT)
