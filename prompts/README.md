# Prompt Templates

Reusable starting points for the workflows we run most often. Copy a template, fill in the brackets, and paste into Claude (or any AI agent that has the HyperFrames skills loaded).

## Why these exist

Building good video compositions takes the right *first prompt*. Get the brief tight and you save 5–10 rounds of "actually, can you change…" The templates below are the briefs that have worked, distilled to a fill-in-the-blank.

## Naming convention

`<workflow>.md` — lowercase, hyphen-separated. Examples: `csv-to-chart.md`, `tiktok-hook.md`.

## How to use

1. Pick the template that matches your workflow
2. Open it and copy the contents
3. Replace everything in `[brackets]` with your specifics
4. Paste into Claude inside the project directory (so the `.agents/skills/` are loaded)

## When to add a new template

If you've fine-tuned a prompt over 2–3 projects and it consistently produces good first drafts, save it here. Don't save one-offs — only patterns you'll reuse.

## Current templates

- `csv-to-chart.md` — animated chart from a CSV or pasted data
- `pdf-to-summary.md` — turn a PDF into a 30–60s narrated video summary
- `tiktok-hook.md` — 9:16 vertical hook video with bouncy captions + TTS
- `product-intro.md` — 10–20s product intro with hero text + b-roll + music
- `competitor-analysis.md` — break down a competitor's video, extract their playbook
