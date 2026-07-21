#!/usr/bin/env python3
"""Generate index.html for the Sportif peach beat-cut montage.

Hard cuts on a 120 BPM grid (beat = 0.5s) with a per-image zoom-punch, a fast
wordmark intro, a double-time build section, and a date-free end card. Re-run
after changing BPM / order / section lengths below. Drop any ~120 BPM track
under the render in-app and the cuts line up.
"""

BPM = 120
BEAT = 60.0 / BPM                 # 0.5s
N_IMAGES = 14                     # img00..img13

INTRO = 2 * BEAT                  # 0.0 - 1.0  wordmark
main_start = INTRO                # first image lands on beat 2
# main section: one image per beat
main = [(main_start + i * BEAT, i) for i in range(N_IMAGES)]   # t=1.0 .. 7.5
build_start = main[-1][0] + BEAT  # 8.0
# build section: double-time (half-beat) cuts through the punchiest shots
HIGHLIGHTS = [0, 3, 1, 9, 2, 6, 4, 7, 0, 3, 1, 9]
half = BEAT / 2                   # 0.25s
build = [(build_start + i * half, m) for i, m in enumerate(HIGHLIGHTS)]  # 8.0 .. 10.75
end_card = build[-1][0] + half    # 11.0
# end card assembles over ~0.8s, so hold well past that: total 15s => logo readable ~3s
DURATION = end_card + 8 * BEAT    # 15.0

cuts = main + build               # (time, image_index)

# ---- emit HTML ----
imgs = "\n".join(
    f'        <img id="img{m:02d}" class="cut" src="images/img{m:02d}.png" alt="" data-layout-allow-overflow />'
    for m in range(N_IMAGES)
)

tl_lines = []
for idx, (t, m) in enumerate(cuts):
    # hide the previous cut exactly as this one appears (hard cut, one image at a time)
    if idx > 0:
        pt, pm = cuts[idx - 1]
        tl_lines.append(f'      tl.set("#img{pm:02d}", {{ opacity: 0 }}, {t:.3f});')
    tl_lines.append(f'      tl.set("#img{m:02d}", {{ opacity: 1 }}, {t:.3f});')
    dur = (cuts[idx + 1][0] - t) if idx + 1 < len(cuts) else BEAT
    tl_lines.append(
        f'      tl.fromTo("#img{m:02d}", {{ scale: 1.06 }}, {{ scale: 1.0, duration: {dur * 0.9:.3f}, ease: "power2.out" }}, {t:.3f});'
    )
# hide the last image when the end card takes over
last_t, last_m = cuts[-1]
tl_lines.append(f'      tl.set("#img{last_m:02d}", {{ opacity: 0 }}, {end_card:.3f});')
timeline = "\n".join(tl_lines)

html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Glacial Indifference"; src: url("fonts/GlacialIndifference-Regular.woff2") format("woff2"); font-weight: 400; }}
      @font-face {{ font-family: "Glacial Indifference"; src: url("fonts/GlacialIndifference-Bold.woff2") format("woff2"); font-weight: 700; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #F0CDB3; font-family: "Glacial Indifference", sans-serif; }}
      #stage {{ position: absolute; inset: 0; overflow: hidden; background: #F0CDB3; }}
      /* stacked full-bleed cuts, all hidden until the timeline reveals them */
      .cut {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center; opacity: 0; transform-origin: center; will-change: transform, opacity; }}

      /* intro wordmark + end card overlays */
      .overlay {{ position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: #F0CDB3; z-index: 50; }}
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
{imgs}
      </div>

      <!-- intro wordmark (fades out as the cuts begin) -->
      <div id="intro" class="overlay clip" data-start="0" data-duration="{INTRO:.2f}" data-track-index="2">
        <div class="wm">SPORTIF</div>
        <div class="rule"></div>
      </div>

      <!-- end card (no launch date) -->
      <div id="endcard" class="overlay clip" data-start="{end_card:.2f}" data-duration="{(DURATION-end_card):.2f}" data-track-index="3">
        <div class="wm">SPORTIF</div>
        <div class="rule" id="ec-rule"></div>
        <div class="soon">Coming soon</div>
        <div class="handle">@sportifcollection</div>
      </div>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      /* intro: quick reveal, hold, snap away right on the first beat */
      tl.from("#intro .wm", {{ opacity: 0, y: 30, duration: 0.4, ease: "power3.out" }}, 0.05);
      tl.from("#intro .rule", {{ scaleX: 0, duration: 0.35, ease: "power2.inOut" }}, 0.25);
      tl.to("#intro", {{ opacity: 0, duration: 0.18, ease: "power1.in" }}, {INTRO - 0.18:.3f});

      /* beat-cut montage */
{timeline}

      /* end card assembles and holds */
      tl.to("#endcard", {{ opacity: 1, duration: 0.2, ease: "power1.out" }}, {end_card:.3f});
      tl.from("#endcard .wm", {{ opacity: 0, y: 34, duration: 0.45, ease: "power3.out" }}, {end_card + 0.05:.3f});
      tl.from("#ec-rule", {{ scaleX: 0, duration: 0.35, ease: "power2.inOut" }}, {end_card + 0.2:.3f});
      tl.from("#endcard .soon", {{ opacity: 0, y: 22, duration: 0.4, ease: "power2.out" }}, {end_card + 0.3:.3f});
      tl.from("#endcard .handle", {{ opacity: 0, duration: 0.35, ease: "sine.out" }}, {end_card + 0.42:.3f});

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

with open("index.html", "w") as f:
    f.write(html)
print(f"wrote index.html: {len(cuts)} cuts, {DURATION:.2f}s, end card at {end_card:.2f}s")
