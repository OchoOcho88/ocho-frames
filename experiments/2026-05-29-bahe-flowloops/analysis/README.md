# Analysis

How to analyze each generated result, then feed it back into the loop.

## Video (video-v1.mp4)

Run the video-analyzer skill on the generated clip:

```bash
python3 ~/.claude/skills/video-analyzer/scripts/analyze_video.py \
  experiments/2026-05-29-bahe-flowloops/results/video-v1.mp4 \
  > experiments/2026-05-29-bahe-flowloops/analysis/video-v1-analysis.md
```

For a marketing-conversion lens instead of the default description, add the competitor-analysis prompt:

```bash
python3 ~/.claude/skills/video-analyzer/scripts/analyze_video.py \
  experiments/2026-05-29-bahe-flowloops/results/video-v1.mp4 \
  --prompt-file prompts/competitor-analysis.md \
  > experiments/2026-05-29-bahe-flowloops/analysis/video-v1-analysis.md
```

Then we read the analysis against the prompt's intent and log learnings in ../iteration-log.md.

## Image (image-v1.png)

The image-analyzer skill is not built yet (it is on the pipeline queue). For now, paste the generated image back into this chat and Claude will analyze it with native vision against the brief's success criteria. Save that read as `image-v1-analysis.md` here.

## The point

We are not just describing the output. We compare it to the intent stated in the prompt and brief, decide what to change, and record it. One variable per round.
