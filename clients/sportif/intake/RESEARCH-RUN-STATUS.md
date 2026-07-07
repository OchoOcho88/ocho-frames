# Research Run Status

_Last updated: 2026-06-16_

## Status: COMPLETE

The post-Lucy research run finished on 2026-06-16. All 5 passes ran, brand.md is populated, and the Stage 3 synthesis brief is drafted.

## What ran

- **Pass 1 (AU customer segment profile):** `research/au-segment-profile.md`. sonar-deep-research.
- **Pass 2 (8 competitor deep dives):** `competitor-analyses/<brand>-perplexity-profile-2026-06-16.md` for all 8 named brands (Move Active, Your Reformer, Leelo Active, Avara Athletics, Kikiva, PE Nation, AJE, Anine Bing). sonar-deep-research.
- **Pass 3 (brand references):** `research/brand-references.md` (Anine Bing, Kikiva, White Fox). sonar-pro.
- **Pass 4 (cultural lane validation):** `research/cultural-lane-validation.md`. sonar-reasoning-pro.
- **Pass 5 (budget benchmarks):** `research/budget-benchmarks.md`. sonar-pro.
- **Synthesis:** `brand.md` updated (Customer, Strategic positioning, Competitors differentiation, Voice, Budget bands). Stage 3 brief at `campaigns/launch-2026-09/synthesis-brief.md`.
- **Verbatim intake** captured at `intake/lucy-responses.md`.

## Environment note (important for next runs)

In this Cowork session, background shell processes do NOT survive across separate tool calls (the sandbox reaps them, and each call caps at 45s). So the old "launch sonar-deep-research with nohup and poll across calls" workflow from CLAUDE.md does not work here.

Solution built this run: `scripts/pplx_async.py`. It submits async jobs to Perplexity (which run server-side), persists the request ids to a registry file on disk, and polls them in later short calls, writing each answer when COMPLETED. Registry for this run: `research/jobs.json`, manifest at `research/manifest.json`. Use this helper for deep-research in Cowork. (On Hugo's Mac via Claude Code, the original background approach still works.)

Note: Perplexity rate-limits async submissions (HTTP 429), so submit in small staggered batches. Three of the 8 competitor jobs failed server-side on the first attempt and were resubmitted successfully.

## Still open (need Hugo or Lucy)

- Step 11: update `docs/marketing-fundamentals.md` Part 8 budget bands with the Sportif AUD numbers (not done; optional).
- Step 12: send Lucy a "where we are" summary email (proposed positioning, channel-sequencing recommendation, budget envelope, next-call agenda). Draft not written yet.
- Naming and trademark lock, platform-sequencing call, script-accent font, activewear-range timing (all on Lucy's side).
