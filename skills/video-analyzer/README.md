# video-analyzer (Claude Code skill)

A pointer doc — the actual skill lives at `~/.claude/skills/video-analyzer/` on Hugo's Mac (NOT inside this workspace folder).

## What it does

Gives Claude the ability to "watch" videos by routing them through Google Gemini's vision API. Returns a structured markdown report:

- **Top-Level Summary** — 2-3 sentence overview
- **Scene-by-Scene Breakdown** — with `MM:SS` timestamps
- **Audio** — verbatim transcript OR honest "silent" note (anti-hallucination)
- **Visual Details** — on-screen text, UI elements, products, branding
- **Key Moments** — 3-7 timestamped highlights

Strong anti-hallucination guardrails baked in: the default prompt explicitly forbids inventing narrators, voiceovers, or speaker names that aren't actually in the video.

## Source

- Author: Mike Futia
- Repo: https://github.com/mikefutia/claude-vision
- License: MIT

## Why this README is in `skills/` if the skill itself isn't

The skill is a **Claude Code skill** — it hardcodes its install location to `~/.claude/skills/video-analyzer/scripts/analyze_video.py` inside the SKILL.md. So it MUST live there for Claude Code (and Cowork) to find it. We can't move it into our workspace `skills/` folder without editing the SKILL.md and breaking compatibility with the upstream repo.

This README exists in the workspace so:
- Future-you (and anyone else who clones `ocho-frames`) knows the skill exists, what it does, and how to install it on a fresh machine
- `setup.sh` knows to install it during a fresh clone
- It shows up in `git log` if we change install procedures

## Install on a fresh machine

```bash
# 1. Clone the skill into the Claude Code skills folder
git clone https://github.com/mikefutia/claude-vision.git ~/.claude/skills/video-analyzer

# 2. Install the Python dependency (Gemini SDK)
pip3 install google-genai
# If your pip complains about externally-managed environments, add: --break-system-packages

# 3. Get a free Gemini API key
# Go to https://aistudio.google.com/apikey and create a key.
# Tip: create a project named "Hyperframes" to track usage separately.

# 4. Set the key as a shell env var (paste this in Terminal — key won't be visible as you paste)
printf "Paste your Gemini API key (input WON'T be visible): " && read -s GEMINI_KEY && echo "" && printf 'export GEMINI_API_KEY="%s"\n' "$GEMINI_KEY" >> ~/.zshrc && source ~/.zshrc && unset GEMINI_KEY && echo "✓ Set"

# 5. Verify
python3 -c "from google import genai; print('Gemini SDK ready, version:', genai.__version__)"
```

`setup.sh` automates steps 1 and 2. Steps 3-5 require manual action (API key creation can't be scripted).

## How to use

From any Claude Code session (or Cowork), once the skill is installed and `GEMINI_API_KEY` is in your shell:

> "Use the video-analyzer skill on /path/to/video.mp4"

Or invoke directly:

> "/video-analyzer ~/Downloads/competitor-ad.mp4"

Optional flags:
- `--prompt "..."` — override the default structured-report prompt
- `--fps N` — change frame sampling rate (default 1 fps; raise for fast-cut content)
- `--model gemini-2.5-flash` — pick a different Gemini model

## Supported video formats

mp4, mov, webm, avi, mpeg, mpg, flv, wmv, 3gpp, 3gp

## Related files in this workspace

- `prompts/competitor-analysis.md` — prompt template that calls this skill for competitor video breakdowns
- `recipes/` — once we have a proven workflow using this skill, we save it as a recipe here

## Free tier limits (as of 2026)

- 15 requests per minute
- 1,500 requests per day
- Free tier sufficient for personal use

## Troubleshooting

- **"GEMINI_API_KEY environment variable is not set"** — open a fresh Terminal window so it re-reads `~/.zshrc`, or run `source ~/.zshrc` in the current one
- **"google-genai is not installed"** — run `pip3 install google-genai` (re-do step 2 above)
- **Upload timeout on large videos** — Gemini's Files API takes 30-60 seconds to process longer videos. The script polls up to 5 minutes before giving up. Try a shorter clip if it keeps timing out.
- **Model 404 error** — try `--model gemini-2.5-flash` if the default `gemini-3-flash-preview` isn't available in your region
