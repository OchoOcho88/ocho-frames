# Recipe: Analyze a video with the video-analyzer skill

> Turn any video file (competitor ad, our own render, reference clip) into a structured markdown report saved to `outputs/video-analyses/`.

## When to use this
- Studying a competitor's ad or product video before designing our own
- Capturing what a reference clip is doing visually so we can pattern-match against it later
- Reviewing our own HyperFrames renders with fresh eyes (gets a second opinion on pacing, on-screen text, key moments)
- Building up the competitive-intel library in `outputs/video-analyses/` over time — the reports are tracked in git so the library compounds

## Prerequisites
- `GEMINI_API_KEY` set in `~/.zshrc` (see Session 003 in `memory.md`)
- `google-genai` installed for the Python that's first on `PATH` (`python3 -c "from google import genai"` must succeed)
- video-analyzer skill at `~/.claude/skills/video-analyzer/scripts/analyze_video.py`
- **One-line shim applied to that script** — `from __future__ import annotations` at the top, IF this Mac is still on Python 3.9 (see Session 004). Verify with: `head -1 ~/.claude/skills/video-analyzer/scripts/analyze_video.py`
- Video file in a supported format: `mp4, mov, webm, avi, mpeg, mpg, flv, wmv, 3gpp, 3gp`
- Video is small enough for the inline path (≤18MB) — larger files use the Files API which can stall 30-60s on first call

## Steps

1. **Sanity-check prereqs (10 seconds).**
   ```bash
   echo "GEMINI_API_KEY set? $([ -n "$GEMINI_API_KEY" ] && echo YES || echo NO)" && \
   python3 -c "from google import genai; print('google-genai:', genai.__version__)" && \
   head -1 ~/.claude/skills/video-analyzer/scripts/analyze_video.py
   ```
   - All three should pass. The `head -1` should show `from __future__ import annotations` if you're on Python 3.9.
   - If `GEMINI_API_KEY` shows `NO`, open a fresh Terminal (re-reads `~/.zshrc`) or run `source ~/.zshrc`.

2. **Pick the output filename** using the convention from `outputs/README.md`: `<source>-<descriptor>-<YYYY-MM-DD>.md`.
   - `source` = where the video came from (e.g., `competitor-acme`, `student-kit`, `our-render`)
   - `descriptor` = short slug describing the clip (e.g., `tiktok-ad-launch`, `linear-promo-30s`)
   - Date = today, ISO format

3. **Run the analyzer with stdout redirected to the chosen file.**
   ```bash
   cd ~/Desktop/hyperframes && \
   mkdir -p outputs/video-analyses && \
   python3 ~/.claude/skills/video-analyzer/scripts/analyze_video.py \
     <path-to-video> \
     > outputs/video-analyses/<source>-<descriptor>-<YYYY-MM-DD>.md
   ```
   - Report goes to stdout (your file); progress messages go to stderr (your screen) — that's why the redirect is `>` not `&>`.
   - Expect ~30-90s for a short clip. The two stderr warnings (`FutureWarning` about Python 3.9 EOL, `thought_signature` non-text-parts warning) are benign — the text still streams back cleanly.

4. **(Optional but recommended) Prepend a provenance header** so each report in the library is self-documenting. Just edit the top of the file to add:
   ```markdown
   # Video Analysis — <descriptor>

   | | |
   |---|---|
   | **Source** | `<path-to-video>` |
   | **Analyzed** | YYYY-MM-DD |
   | **Tool** | `video-analyzer` skill (Gemini Vision) |
   | **Model** | `gemini-3-flash-preview` |

   ---
   ```
   - Future-you will thank present-you when the library has 20+ reports.

5. **Spot-check for hallucinations before trusting the report.** Open the file and check:
   - **Audio section:** if the video has no voiceover, it should say so explicitly ("No speech detected" or similar). If it invents narrator names or quotes that weren't spoken, the guardrails failed — investigate.
   - **On-screen text:** read 2-3 entries against your memory of the video. Should be verbatim, not paraphrased.
   - **Timestamps:** scan that they're monotonically increasing and don't exceed the video's duration.

## Key configs

| Setting | Default | When to change it |
|---------|---------|-------------------|
| Prompt | Skill's built-in structured-report prompt | Use `--prompt "..."` (or `--prompt-file path.md`) when you want a competitor-specific take — e.g., point it at `prompts/competitor-analysis.md` |
| FPS sampling | `1` (one frame per second) | Bump with `--fps 2` or `--fps 4` for fast-cut TikTok/Reels content where 1fps misses cuts |
| Model | `gemini-3-flash-preview` | If you get a 404 in your region, fall back with `--model gemini-2.5-flash` |

## Watch out for

- **Python 3.9 + missing shim → `TypeError` at startup.** The upstream script uses PEP-604 `float | None` syntax. If `head -1 analyze_video.py` does NOT show `from __future__ import annotations` and you're on 3.9, add it (one line, behavior-preserving on all Python versions). See Session 004 in `memory.md` for the full diagnosis.
- **Fresh-clone regression.** `setup.sh` re-clones the skill from upstream, which doesn't yet have the shim. After running `setup.sh` on a new machine, re-apply the one-liner OR upgrade to Python 3.10+. Open question to resolve: PR the fix upstream so `setup.sh` is enough on its own.
- **Files >18MB go through the Files API.** That's a two-step upload-then-poll process that can take 30-60s on first call and times out after 5 minutes. If a large file keeps stalling, try a shorter clip — or upload + reuse the file ID manually.
- **Quota:** free tier is 15 requests/min, 1,500/day. Plenty for personal use, but a batch of 20 clips in a tight loop will hit the per-minute cap.
- **`GEMINI_API_KEY` not visible in new shell.** Means `~/.zshrc` wasn't sourced — open a fresh Terminal window or run `source ~/.zshrc`.

## Reference implementation
- `outputs/video-analyses/student-kit-linear-promo-30s-2026-05-26.md` — the Session 004 first-test output. Compare future runs against this for "what good looks like."

## Variations worth trying

- **Competitor-analysis mode (marketing-conversion lens):** swap the default 5-section report for the 12-section framework in `prompts/competitor-analysis.md`. Use when studying ads, UGC, or any video where the question is "why does this convert" rather than "what's in this video."
  ```bash
  cd ~/Desktop/hyperframes && \
  python3 ~/.claude/skills/video-analyzer/scripts/analyze_video.py \
    <path-to-video> \
    --prompt-file prompts/competitor-analysis.md \
    > outputs/video-analyses/<source>-<descriptor>-<YYYY-MM-DD>.md
  ```
  The prompt file's HTML-comment header is stripped by markdown renderers but Gemini sees it — that's fine, it's labeled clearly as meta.

- **Fast-cut content:** `--fps 4` for TikTok/Reels-style cuts that switch every <0.5s — default `--fps 1` will miss beats.

- **Cheaper/faster batch runs:** `--model gemini-2.5-flash-lite` if available, for scanning a backlog where deep detail isn't needed.

- **Custom one-off focus:** `--prompt "Focus only on the on-screen text and brand colors. Ignore audio."` for asset-extraction passes where you just want one slice of the analysis.

---
_Added: 2026-05-26 — proven in Session 004 against the Linear 30s promo._
