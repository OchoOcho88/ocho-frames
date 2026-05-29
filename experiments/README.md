# Experiments: the self-improving prompt loop

This folder is where we pressure-test the creative-strategy pipeline on itself. Each experiment runs one closed loop:

1. **Produce** a Stage 4 production prompt (Seedance 2.0 video, gpt-image-2 static) from the platform spec at `docs/platform-prompt-formats.md`.
2. **Generate** the asset (Hugo runs the prompt in Seedance / ChatGPT Images 2.0).
3. **Analyze** the result (video-analyzer skill for video, Claude vision for images until the image-analyzer skill is built).
4. **Learn**: compare intent (the prompt) against the result, record what worked and what did not, change one thing, run again.

Over rounds, the learnings feed back into `docs/platform-prompt-formats.md` and the Stage 4 adapter prompts. That is the self-improving part: the system gets better at writing prompts because it watches its own output.

## Folder convention per experiment

```
YYYY-MM-DD-<slug>/
  brief.md            what we are testing, the source reference, the intent, success criteria
  source/             the reference image(s) the test is based on
  prompts/            versioned prompts: seedance-v1.md, gpt-image-v1.md, seedance-v2.md ...
  results/            generated assets Hugo drops in: video-v1.mp4, image-v1.png ...
  analysis/           analyzer output per result: video-v1-analysis.md, image-v1-analysis.md
  iteration-log.md    the loop record: per round, hypothesis -> result -> learnings -> next change
```

## Rules that keep it rigorous

- **One variable per round.** Change the reference strategy, OR the camera plan, OR the audio block, not all at once.
- **Judge against intent.** Each round states which technique it is testing. Score the output on whether that technique delivered, not just on overall prettiness.
- **Log everything, including failures.** A failure that teaches us a failure mode is a win for the doc.
- **Promote learnings.** When a pattern proves out, update `docs/platform-prompt-formats.md` and note it in the iteration log.

## Active experiments

- [2026-05-29-bahe-flowloops](2026-05-29-bahe-flowloops/) first loop. BAHE FLOWLOOPS LUXE resistance loops as a design-led stand-in for Sportif's possible product. Tests the Seedance 2.0 and gpt-image-2 formats end to end.
