# PDF → Video Summary

## When to use
You have a PDF (research paper, whitepaper, pitch deck, report) and want a short narrated video that hits the key points.

## Prompt

```
Using /hyperframes and /hyperframes-media, create a [30 / 45 / 60]-second narrated video summary of the attached PDF.

PDF: [path to PDF in assets/ or upload]

Structure I want:
1. Hook (0–3s): one-sentence "why this matters"
2. 3–4 key points (with simple animated visuals — not just text on screen)
3. CTA / takeaway (last 3–5s)

Specs:
- Aspect ratio: [16:9 for LinkedIn/YouTube, 9:16 for TikTok/Reels/Shorts]
- Duration: [30 / 45 / 60] seconds
- Voice: use HyperFrames built-in TTS (Kokoro) with voice "[af_bella / am_michael / etc.]"
  OR use my HeyGen voice ID: [HEYGEN_DEFAULT_VOICE_ID from .env]
- Style: brand-kit.md
- Captions: yes, synced to TTS, bouncy entry per word

Important:
- Read the PDF, extract the actual key points (don't make up content)
- Each point gets its own scene with a relevant visual (stat callout, icon, simple chart, etc.)
- Cite the PDF title + author in the final frame

Output to my-projects/[project-name]/
```

## Notes
- Tell Claude to read the PDF FIRST, then plan the script, then build the composition
- 45s is the sweet spot for LinkedIn; 30s for TikTok hooks
- Always preview before rendering — TTS pacing sometimes needs tightening
