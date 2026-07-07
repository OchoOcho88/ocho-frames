# -*- coding: utf-8 -*-
"""
Generator for the client-facing Sportif Brand Value Plan PDF.
Cover: magazine split (photo right, serif title left).
Reads brand-value-plan-client.md (the condensed client cut).
The detailed internal version stays in brand-value-plan.md.
Run:  python3 build-brand-value-plan.py
"""
import re, html, os, tempfile
from PIL import Image
from weasyprint import HTML

SPORTIF = os.path.dirname(os.path.abspath(__file__))
HYPER   = os.path.dirname(os.path.dirname(SPORTIF))
MD      = os.path.join(SPORTIF, "brand-value-plan-client.md")
SRC_FLOW= os.path.join(HYPER, "experiments/2026-05-29-bahe-flowloops/results/FLOW.png")
OUT     = os.path.join(SPORTIF, "Sportif-Brand-Value-Plan.pdf")
FLOW    = os.path.join(tempfile.gettempdir(), "sportif_flow_clean.png")

im = Image.open(SRC_FLOW).convert("RGB"); w, h = im.size
im.crop((0, 268, w, h)).save(FLOW)

raw = open(MD, encoding="utf-8").read()

def inline(t):
    t = html.escape(t.strip())
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`(.+?)`", r'<span class="mono">\1</span>', t)
    return t

# preamble (before first "## ") -> intro is the LAST blockquote group
preamble = raw.split("\n## ", 1)[0]
groups, cur = [], []
for line in preamble.splitlines():
    if line.startswith(">"):
        cur.append(line.lstrip("> ").strip())
    else:
        if cur: groups.append(" ".join(cur)); cur = []
if cur: groups.append(" ".join(cur))
intro = groups[-1] if groups else ""

# sections
secs = re.split(r"\n## ", raw)[1:]
levers, closers = [], []
for s in secs:
    head, _, body = s.partition("\n")
    lines = body.splitlines()
    idea = ""
    bullets_all, impl = [], []
    in_impl = False
    for ln in lines:
        t = ln.strip()
        if re.match(r"^\*[^*].*\*$", t):            # *italic idea*
            idea = t.strip("*").strip(); continue
        if t.lower().startswith("**what we"):        # implement marker
            in_impl = True; continue
        if t.startswith("- "):
            (impl if in_impl else bullets_all).append(t[2:].strip())
    m = re.match(r"^(\d+)\.\s*(.+)", head.strip())
    if m:
        levers.append(dict(num=m.group(1), title=m.group(2).strip(),
                           idea=idea, body=bullets_all, impl=impl))
    else:
        closers.append(dict(title=head.strip(), body=bullets_all, idea=idea))

def ul(items, cls="blts"):
    return f'<ul class="{cls}">' + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"

lever_html = ""
for L in levers:
    impl_box = ""
    if L["impl"]:
        impl_box = f'<div class="impl"><div class="dolabel">WHAT WE\'LL IMPLEMENT</div>{ul(L["impl"],"impls")}</div>'
    lever_html += f"""
    <div class="card lever">
      <div class="lhead"><div class="badge">{L['num']}</div>
        <div class="ltitle">{html.escape(L['title'])}</div></div>
      <div class="idea">{inline(L['idea'])}</div>
      {ul(L['body'])}
      {impl_box}
    </div>"""

closer_html = ""
for C in closers:
    idea_line = f'<div class="idea">{inline(C["idea"])}</div>' if C.get("idea") else ""
    closer_html += f'<div class="card"><div class="sec">{html.escape(C["title"])}</div>{idea_line}{ul(C["body"])}</div>'

DOC = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:19mm 17mm 16mm 17mm; }}
@page cover {{ margin:0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
:root{{ --peach:#F0CDB3; --caramel:#C6926E; --terr:#833827; --choc:#2D1814;
        --cream:#F6EEE5; --linen:#FFFBF8; --charcoal:#4A433C; --line:rgba(198,146,110,.34); }}
body{{ font-family:'Poppins',sans-serif; color:var(--charcoal); font-size:10.6pt; line-height:1.5; }}
strong{{ font-weight:600; color:var(--choc); }}
.mono{{ font-weight:500; }}
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
.lhead{{ display:flex; align-items:center; gap:9px; margin-bottom:3mm; }}
.badge{{ flex:none; width:24px; height:24px; border-radius:50%; background:var(--terr); color:var(--cream); font-weight:600; font-size:11pt; text-align:center; line-height:24px; }}
.ltitle{{ font-family:'Lora',serif; font-weight:600; font-size:16.5pt; color:var(--choc); line-height:1.1; }}
.idea{{ font-style:italic; color:var(--caramel); font-size:10.6pt; margin-bottom:3.5mm; line-height:1.45; }}
ul.blts{{ margin:0 0 0 4.8mm; }}
ul.blts li{{ margin-bottom:2.4mm; padding-left:1.5mm; line-height:1.46; }}
ul.blts li::marker{{ color:var(--caramel); }}
.impl{{ background:#F3E1D2; border-radius:8px; padding:4.5mm 5.5mm 4mm; margin-top:4mm; }}
.impl .dolabel{{ display:block; font-weight:700; letter-spacing:.12em; color:var(--terr); font-size:8.5pt; margin-bottom:2.5mm; }}
ul.impls{{ margin:0 0 0 4.8mm; }}
ul.impls li{{ margin-bottom:1.8mm; padding-left:1.5mm; font-size:9.9pt; line-height:1.42; }}
ul.impls li::marker{{ color:var(--terr); }}
.sec{{ font-weight:600; letter-spacing:.2em; text-transform:uppercase; color:var(--terr); font-size:9.5pt; margin-bottom:4mm; }}
</style></head><body>
<div class="cover">
  <div class="photo"><img src="file://{FLOW}"></div>
  <div class="col">
    <div class="mast">Sportif</div><div class="grow"></div>
    <div class="rule"></div>
    <div class="title">Brand<br>Value<br>Plan</div>
    <div class="sub">How we build the one thing competitors cannot copy: the brand around the band.</div>
    <div class="grow"></div>
    <div class="foot">Prepared for Sportif&nbsp;&middot;&nbsp;by Ocho&nbsp;&middot;&nbsp;July 2026<br>Read alongside the Brand Kit and the Launch Plan</div>
  </div>
</div>
<div class="intro"><span class="kick">The idea in one line.</span> {inline(intro)}</div>
{lever_html}
{closer_html}
</body></html>"""

HTML(string=DOC).write_pdf(OUT)
print("levers:", len(levers), "closers:", len(closers), "->", OUT)
