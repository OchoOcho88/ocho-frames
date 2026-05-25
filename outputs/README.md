# Outputs

Everything the AI and HyperFrames pipeline **produces** lands here. Compare with `scripts/` (your inputs — briefs, storyboards, voiceover scripts) and `prompts/` (templates you copy from).

## Folder structure

```
outputs/
├── video-analyses/        ← markdown reports from video-analyzer skill
├── downloads/             ← competitor videos downloaded for analysis (gitignored)
├── generated-images/      ← AI-generated images (GPT Image 2.0, etc.) (gitignored)
└── voiceovers/            ← AI-generated audio narration (gitignored)
```

**Renders (finished MP4s) do NOT live here.** Each video project keeps its own renders inside `my-projects/<project>/out/` so the render stays alongside the composition that produced it.

## Naming convention

`<source>-<descriptor>-<YYYY-MM-DD>.<ext>`

Examples:
- `video-analyses/competitor-acme-corp-tiktok-ad-2026-05-26.md`
- `downloads/competitor-acme-corp-tiktok-ad-2026-05-26.mp4`
- `generated-images/hero-brand-mockup-2026-05-26.png`
- `voiceovers/product-intro-script-v3-2026-05-26.mp3`

Keeps things alphabetically grouped and obvious-at-a-glance.

## What's tracked in git vs ignored

| Type | Tracked in git? | Why |
|------|-----------------|-----|
| `video-analyses/*.md` | ✅ Yes | Small, valuable knowledge — competitive intel library over time |
| `downloads/*` | ❌ No | Copyrighted competitor content + large files |
| `generated-images/*` | ❌ No | Large binaries, easy to regenerate |
| `voiceovers/*` | ❌ No | Large audio files, easy to regenerate |

If you ever want to track a *specific* asset (e.g., a hero image you'll reuse), move it from `outputs/generated-images/` into `assets/images/` — those are tracked.

## Cleaning up

`outputs/` accumulates over time. When it gets noisy, archive the old stuff:

```bash
# Move anything older than 90 days into an archive folder
find ~/Desktop/hyperframes/outputs -type f -mtime +90 -exec mv {} ~/Desktop/hyperframes/outputs/_archive/ \;
```

Or just delete what you know you don't need.
