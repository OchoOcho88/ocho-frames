#!/usr/bin/env python3
"""Lifestyle + product beat-cut blend. Alternates full-bleed lifestyle shots with the
real bands (contained on peach) as hard cuts on a 120 BPM grid, with a zoom-punch,
a double-time build, and a date-free end card. Re-run after editing the order below."""
BPM = 120; BEAT = 60.0 / BPM
INTRO = 2 * BEAT  # 1.0s wordmark

# unique images: life* = full-bleed cover, prod* = contained on peach
IMGS = ['life0','life1','life2','life3','life4','life5','life6','life7',
        'prodL','prodM','prodH','prodF']

# alternating main order (lifestyle, product, lifestyle, product, ...)
MAIN = ['life0','prodL','life1','prodM','life2','prodH','life3','prodF',
        'life4','prodL','life5','prodM','life6','prodH','life7','prodF']
# double-time build: punchy lifestyle + product accents
BUILD = ['life0','life1','prodM','life4','life2','prodH','life5','prodF']

main = [(INTRO + i * BEAT, m) for i, m in enumerate(MAIN)]
bstart = main[-1][0] + BEAT
build = [(bstart + i * (BEAT/2), m) for i, m in enumerate(BUILD)]
end_card = build[-1][0] + BEAT/2
DURATION = end_card + 6 * BEAT  # end card holds ~3s
cuts = main + build

imgs_html = "\n".join(
    f'        <img id="{m}" class="cut {"cover" if m.startswith("life") else "prod"}" '
    f'src="images/{m}.png" alt="" data-layout-allow-overflow />' for m in IMGS)

tl = []
for i, (t, m) in enumerate(cuts):
    if i > 0:
        tl.append(f'      tl.set("#{cuts[i-1][1]}", {{ opacity: 0 }}, {t:.3f});')
    tl.append(f'      tl.set("#{m}", {{ opacity: 1 }}, {t:.3f});')
    dur = (cuts[i+1][0] - t) if i+1 < len(cuts) else BEAT
    tl.append(f'      tl.fromTo("#{m}", {{ scale: 1.06 }}, {{ scale: 1.0, duration: {dur*0.9:.3f}, ease: "power2.out" }}, {t:.3f});')
tl.append(f'      tl.set("#{cuts[-1][1]}", {{ opacity: 0 }}, {end_card:.3f});')
timeline = "\n".join(tl)

html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Glacial Indifference"; src: url("fonts/GlacialIndifference-Regular.woff2") format("woff2"); font-weight: 400; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #EEC7AF; font-family: "Glacial Indifference", sans-serif; }}
      #stage {{ position: absolute; inset: 0; overflow: hidden; background: #EEC7AF; }}
      .cut {{ position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0; transform-origin: center; will-change: transform, opacity; }}
      .cover {{ object-fit: cover; object-position: center; }}
      .prod {{ object-fit: contain; }}
      .overlay {{ position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: #EEC7AF; z-index: 50; }}
      #endcard {{ opacity: 0; }}
      .wm {{ color: #FFFBF8; font-size: 132px; letter-spacing: 0.26em; text-indent: 0.26em; }}
      .rule {{ width: 200px; height: 7px; background: #FFFBF8; margin-top: 34px; transform-origin: center; }}
      .soon {{ margin-top: 40px; color: #4A433C; font-size: 50px; letter-spacing: 0.12em; text-indent: 0.12em; }}
      .handle {{ margin-top: 20px; color: #833827; font-size: 38px; letter-spacing: 0.08em; text-indent: 0.08em; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DURATION:.2f}" data-width="1080" data-height="1920">
      <div id="stage" class="clip" data-start="0" data-duration="{DURATION:.2f}" data-track-index="1">
{imgs_html}
      </div>
      <div id="intro" class="overlay clip" data-start="0" data-duration="{INTRO:.2f}" data-track-index="2">
        <div class="wm">SPORTIF</div><div class="rule"></div>
      </div>
      <div id="endcard" class="overlay clip" data-start="{end_card:.2f}" data-duration="{(DURATION-end_card):.2f}" data-track-index="3">
        <div class="wm">SPORTIF</div><div class="rule" id="ec-rule"></div>
        <div class="soon">Coming soon</div><div class="handle">@sportifcollection</div>
      </div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.from("#intro .wm", {{ opacity: 0, y: 30, duration: 0.4, ease: "power3.out" }}, 0.05);
      tl.from("#intro .rule", {{ scaleX: 0, duration: 0.35, ease: "power2.inOut" }}, 0.25);
      tl.to("#intro", {{ opacity: 0, duration: 0.18, ease: "power1.in" }}, {INTRO-0.18:.3f});
{timeline}
      tl.to("#endcard", {{ opacity: 1, duration: 0.2, ease: "power1.out" }}, {end_card:.3f});
      tl.from("#endcard .wm", {{ opacity: 0, y: 34, duration: 0.45, ease: "power3.out" }}, {end_card+0.05:.3f});
      tl.from("#ec-rule", {{ scaleX: 0, duration: 0.35, ease: "power2.inOut" }}, {end_card+0.2:.3f});
      tl.from("#endcard .soon", {{ opacity: 0, y: 22, duration: 0.4, ease: "power2.out" }}, {end_card+0.3:.3f});
      tl.from("#endcard .handle", {{ opacity: 0, duration: 0.35, ease: "sine.out" }}, {end_card+0.42:.3f});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
open("index.html", "w").write(html)
print(f"wrote index.html: {len(cuts)} cuts, {DURATION:.2f}s, end card {end_card:.2f}s")
