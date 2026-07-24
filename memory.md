# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## CURRENT STATE (update this block every session, keep it to ~12 lines)

*Last updated: 2026-07-24 | Last session: 026 (Claude Code, CLOSED) | Working tree: committed clean | Git: pushed to GitHub | Next: Canva Pro (~next week) -> brand kit + share Sportif folder with Lucy; standalone waitlist capture page still top unbuilt item*

- **NEW (Session 026): memory system v2 (scaling hardening).** `scripts/memory_tools.py` = check / index / search / decisions / open / reconcile / install-hooks. Decisions + open loops are now extractable registries (`DECISIONS.md`, `OPEN-QUESTIONS.md`, filter by client). Session entries carry `Client:` + `Tags:` lines. Close-out ritual updated in CLAUDE.md; pre-push warn hook installed. Full v2 spec in `docs/memory-system.md`. Query open items: `python3 scripts/memory_tools.py open --client Sportif`.

- **NEW (Session 025): fresh gpt-image-2 GENERATION pipeline + Canva workflow (two avenues).** `gen_fresh_explore.py` makes from-scratch Sportif key visuals (brand-world/campaign/band-in-use). Three DURABLE prompt lessons: name the actual garments; garment colour must CONTRAST skin (not flesh-tone); garment material = SMOOTH four-way-stretch (not ribbed). `PATTERNS=1` explores colourways. `realband_in_hand.py` stamps the real label onto generated bands; `campaign_skin.py` / `ad_lifestyle.py` skin shots into finished IG 4:5 ads (warm-charcoal or cream type, NOT navy on warm bg). **Canva: two avenues** = our pipeline (studio, exact/flat) + Canva (workbench, editable/shareable), chained pipeline->Canva->Lucy. Sportif folder set up (IG Ads + Source Photos), local mirror `clients/sportif/canva-exports/`. Can generate editable Canva designs + use our uploaded photos via asset_ids (short briefs only; complex ones fail). **Brand kit + folder-sharing are Pro-gated (Hugo ~next week); Free only does per-design comment links.** See [[real-band-content-pipeline]].
- **NEW (Session 024): reference-layout reskin technique + 2 finals.** Lucy sent a pilates-studio ad to copy the layout of; established the reusable move = **AI generates a no-text plate, we own the type in PIL**. `reskin_pilates_ref.py` strips text + adds our band; `layout_reskin.py` lays all copy (Glacial Indifference, real SPORTIF logotype, terracotta JOIN THE WAITLIST pill, @sportifcollection, a framed single-band product card in the negative space). Two finals at `clients/sportif/generated/images/reference-reskin/`: `reskin-bridge.png` (lead) + `reskin-asis.png` (alt). Soft waitlist teasers, no dates. Source imagery at `clients/sportif/products/reference-layouts/`. See [[real-band-content-pipeline]].
- **NEW (Session 023): real-band product content suite, 7 compositions total.** From 3 casual real-band snapshots: restaged flatlay + 3 hero cards (gpt-image-2 edits), a **range reel**, two **lifestyle+product blends** (rhythmic beat-cut + calm story), a **"they've landed" drop teaser** (bouncy pop headline, Join-our-community CTA), and a **band-in-use pilates reel** (Stage 5: band around the thighs with the real SPORTIF label stamped in). Full reusable process at `clients/sportif/products/real-bands-content-process.md`. The bands' colourways ARE the peach palette (HEAVY terracotta / MEDIUM blush / LIGHT sand). The **blend is the strongest format** (desire + product together).
- **Label-stamp technique:** to put the real SPORTIF patch on an AI-generated band, pass gpt-image-2 BOTH the scene and the real label crop (`scripts-local/stamp_band_label.py`). Low quality reads natural (Hugo preferred it over a crisp-but-pasted composite). Med/high hit the ~60s cap even in the VS Code terminal.
- **Client gym shots = off-brand** (black weights gym, glam register Sportif is against; even tripped AI moderation). Use fresh generated pilates scenes instead. Real band-in-use = future proper shoot, kept pilates/warm.
- **Open for Lucy:** two scratch music beds on the band-in-use reel (calm ~100 BPM vs upbeat ~118 BPM) — Hugo showing her both for beat-pacing pick. All scratch music is unlicensed preview only.
- **NEW (Session 022): peach beat-cut montage shipped + ElevenLabs slot wired.** Fast 120 BPM hard-cut montage of the cosmos-peach images at `compositions/sportif-peach-cuts/` (15s, 9:16, generator `build_cuts.py`, tunable BPM/order/length). Keeper `renders/sportif-peach-cuts_v3_high.mp4` (silent). A SCRATCH synth music bed (`scratch_music.py`, 120 BPM, NOT licensed) is muxed on in `_MUSICDEMO.mp4` purely to preview sync; **Hugo is showing that to Lucy as a "what's possible" future-feel preview (internal only, do not publish the scratch track).** ElevenLabs TTS wired for premium voice: `.env` slot + `scripts/elevenlabs_tts.py` (ready, awaiting Hugo's API key).
- **NEW (Session 021): peach lookbook reel shipped + HyperFrames upgraded 0.6.37 to 0.7.64.** 15s 9:16 brand-mood teaser (serves both IG Reels + TikTok) at `compositions/sportif-peach-reel/`, keeper is `renders/sportif-peach-reel_v2_high.mp4` (silent, add music in-app). Card-on-peach treatment of 3 cosmos-peach bases, proven taglines, date-free "Coming soon" end card. Build notes in the composition's `design.md`.
- **NEW (Session 021): Tuesday 2026-07-14 Lucy meeting outcomes LOGGED.** Launch is on HOLD pending trademark talks with Lucy's lawyer (no new date, indefinite). Waitlist page was never put to Lucy (Hugo did not show or ask). Incentive decision (A/B/C) still undecided, Lucy to get back. No Shopify movement, also gated on the trademark talks. **The 500 band units HAVE landed** (unboxing now filmable).**
- **TRADEMARK is now the critical-path gate**, not Shopify. Launch, Shopify, and the whole go-to-market are held until Lucy's lawyer clears the trademark. Nothing forces this from our side; use the wait to build what does NOT depend on it (waitlist page, email flow, ambassador shortlist, unboxing footage).
- **cosmos-peach series (Session 020): 15 Lucy-approved finals** (IG 4:5 1088x1360, peach palette, narrow lockup) at `clients/sportif/generated/images/cosmos-peach/` (+ `notext/` bases). Prompts preserved in `clients/sportif/scripts-local/gen_cosmos_peach.py`.
- **Funnel layer (Sessions 017 to 018).** `docs/funnel-playbook.md` (reusable foundations from the Australian Marketing Summit 2026, Ethan Donati) + `clients/sportif/funnel-plan.md` (3 funnels + content x funnel mapping in section 7: every post carries one CTA to the waitlist, FAQ lane is the 4th content format, signups per post is a scorecard metric). Synthesis brief cross-linked.
- **Key unlock: the waitlist capture page does NOT need Shopify.** A standalone Klaviyo-style landing page can go live now, un-deadending all content and partially bypassing the Shopify blocker. Top of the Tuesday agenda.
- **Pending decisions: Lucy-session incentive adaptation (A: monthly group session, recommended / B: capped 1:1 / C: video series), funnel-plan.md section 4.**

- **Client: Sportif.** Strategy LOCKED: Lucy Wayne is the differentiator, parallel wholesale + DTC, one hub (sportifcollection.com.au + @sportifcollection + email). Launch September 2026; 500 band units due early July (may have already landed, confirm with Lucy).
- **Current Lucy-facing docs: exactly two PDFs**, `Sportif-Brand-Value-Plan.pdf` (strategy) + `Sportif-Launch-Plan.pdf` (operations). Everything else archived in `clients/sportif/_archive/superseded-pdfs-2026-07/`.
- **CRITICAL PATH: nowhere to sell the band.** Blocked on Lucy: open Shopify, lock prices + ~$70 pouch threshold, decide fabric, agree who answers customers. Bundled ask email is IN HUGO'S GMAIL DRAFTS (to lucy@lucywayne.com.au); he attaches the two PDFs and sends.
- **Image pipeline is LIVE (Stage 4 started).** OpenAI key in .env, gpt-image-2 working. Production pattern: generate text-free, overlay real Glacial Indifference via `scripts/overlay_wordmark.py`. Fonts at `brand/fonts/glacial-indifference/`. Prompts logged in `clients/sportif/image-prompts.md`. Iterate low quality in Cowork (45s cap), finals high quality in Claude Code.
- **Waiting on Lucy:** her pick of the three 4:5 Instagram hero concepts (v5 unboxed / v6 set / v7 flat, Hugo texting her); then a high-quality final render in Claude Code.
- **Next build steps once unblocked:** Shopify coming-soon page (research done), store build, Klaviyo flows (account to be created after Shopify), ambassador/instructor seeding shortlist (main growth engine, not started).
- **Also open:** trademark clearance (with lawyer), materials question (gates sustainability copy), Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins (switch to real font on next edit).
- **Grid banner READY (Session 015):** 3-tile SPORTIF wordmark banner in three colourways at `clients/sportif/generated/images/grid-banner/`, peach/white is the on-brand pick. Posting recipe PROVEN on a mock account: 1080x1440 tiles, tap Original on the crop screen (default 1:1 crop breaks it), post right tile first, or reorder afterwards (IG added grid drag-reorder June 2026).
- **INSTA LAUNCH IS THIS FRIDAY (2026-07-10). TEASER REEL RENDERED AND LAUNCH-READY, now 15s with the identity end card, in TWO variants.** Standard: `compositions/sportif-teaser/renders/sportif-teaser_2026-07-08_13-48-53.mp4`. With a follow CTA: `compositions/sportif-teaser/renders/sportif-teaser-cta.mp4` (rendered via the `cta` composition variable). Both 1080x1920, 15s, check clean 0/0/0. End card is now blush peach with warm-white wordmark, warm-charcoal launch line, terracotta handle, and holds ~3s before the fade. Backgrounds are MEDIUM quality (true-high blocked by the ~60s Claude Code network cap): to upgrade, run `python3 clients/sportif/scripts-local/gen_action_bg.py <variant> high` in a NATIVE Mac terminal, then rebuild tiles, re-copy, re-render.
- **Still waiting on Lucy:** feedback on the four tagline-row directions and three banner colourways, plus the hero-concept pick and the blocker email reply.

---

## Weekly Review — 2026-07-19 (week of 2026-07-13)

One session this week (019, 2026-07-18), a sharp drop from last week's six. The week's planned centre of gravity — the Tuesday 2026-07-14 Lucy meeting — happened off-workspace and its outcomes were never logged, so nearly the entire open backlog is still hanging in the air five days later. The one session that did run was a clean, self-contained production win on the image pipeline.

### Highlights
- **First production use of the gpt-image-2 `images/edits` endpoint (Session 019).** The Cosmos reference editorial (backbend pose) was edited to a baby blue outfit with the FORM wordmark replaced by the real SPORTIF lockup — no mask needed, a "two changes only" prompt held pose, grain, and backdrop. Three keepers saved to `clients/sportif/generated/images/`, including a reusable text-free base.
- **A second overlay tool joined the pipeline: `scripts/overlay_logo.py`** stamps the full Sportif lockup (Glacial Indifference Regular, -0.059 em tracking, short underline, geometry measured from the reference logo asset). Rule established: `overlay_logo.py` for the logo lockup, `overlay_wordmark.py` for plain headline text only.
- **A third environment flavour was identified and characterised: the Cowork CLOUD sandbox** (Anthropic container + device bridge). Shell calls are NOT capped at 45s — the ~70s high-quality render completed in one call — but files only reach the Mac via an explicit commit step. Recognisable by `/mnt/user-data/uploads/` paths and `device_*` tools.

The week's big miss: **the Tuesday Lucy meeting outcomes (launch slip reason, new launch date, waitlist page approval, incentive decision) are still not captured anywhere.** Last week's #1 suggested focus was "make the Tuesday meeting count" — whether it did is currently unknowable from the workspace.

### Patterns I noticed
- **Human eyeball review keeps catching what tooling can't.** Hugo spotted the wrongly styled first-pass wordmark (hand-styled Bold, wide tracking, no rule) just as he caught the Reel's bottom-edge glitch and the IG crop bug in prior weeks. Verification on the real output by a human remains the last, essential QA gate.
- **Environment constraints keep reshaping the workflow map.** Last week it was the 45s Cowork cap and the ~60s Claude Code cap; this week a third flavour (cloud sandbox, uncapped shell but explicit file commit) joined. The division-of-labour table now has three columns, and recognising which environment a session is in is becoming a session-start skill.
- **The Lucy bottleneck has evolved into a logging gap.** For weeks the pattern was "waiting on Lucy"; this week the meeting apparently happened but the workspace has no record of what was decided. The blocker is no longer only external — un-logged decisions block exactly like un-made ones.

### Skills / knowledge gained
- **gpt-image-2 edits endpoint:** works mask-free when the prompt is scoped to explicit, enumerated changes ("two changes only"); validate at quality low, final at high.
- **Output-stage moderation can false-positive [sexual] at quality high** on poses like backbends even when low passes; appending "tasteful, professional athletic fitness editorial photograph... modest full-coverage sportswear" clears it. Keep that sentence for bodysuit/backbend imagery.
- **Logo-lockup stamping specifics:** tracking -0.059 em, underline rule, geometry measured from `assets/05-logo-sportif-white-on-peach.png`, colour sampled from the source image being replaced (cream #F4F2EA from the FORM letters).
- **Cloud-sandbox mechanics:** uncapped shell calls, live reads via the device bridge, explicit commit step to persist files to the Mac.

### Open questions still unresolved
- [ ] **Log the Tuesday 2026-07-14 Lucy meeting outcomes** (launch slip reason, new launch date, standalone waitlist page approval, incentive decision A/B/C, Shopify blocker movement). From Session 019; still open — most of the backlog below hangs off this.
- [ ] Carried from last week, all still open pending the meeting outcomes: standalone waitlist capture page build, 3-email welcome flow, Lucy blocker email (still in Gmail drafts), Lucy feedback backlog (taglines, colourways, hero pick), confirm whether the 500 band units landed, ambassador/instructor seeding shortlist (fifth week carried, needs nothing from Lucy), Shopify coming-soon/store build, trademark clearance, materials question, Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins, optional true-high background re-render, optional teaser voiceover, git push from Claude Code (local ahead again).

### Suggested focus for next week
1. **Capture the Lucy meeting outcomes first, before anything else.** The meeting is now 5+ days past and memory decays; one short session logging the slip reason, new launch date, waitlist page verdict, and incentive pick would re-anchor the whole backlog and un-gate items 2 and 3.
2. **Ship the standalone waitlist capture page + 3-email welcome flow** the moment the meeting notes confirm approval. It's the one workstream that routes around Shopify, the Funnel 1 spec is written, and every piece of built content is dead-ended until it exists.
3. **Start the ambassador/instructor seeding shortlist.** Now carried five straight weeks, designated the main growth engine, needs lead time before any launch date, and requires nothing from Lucy or the meeting outcomes — it can start today.

---

## Weekly Review — 2026-07-12 (week of 2026-07-06)

Six sessions this week (013, 014, 015, 016, 017, 018), the busiest week the workspace has had. It split into two halves: an early-week production sprint for the planned Friday Instagram launch (grid banner, tagline row, teaser Reel), then a strategy pivot after the launch slipped, with the Australian Marketing Summit notes turned into a permanent funnel layer. The week ends staged for the Tuesday 2026-07-14 Lucy meeting.

### Highlights
- **The teaser Reel is rendered and launch-ready in two variants (Session 016).** 15s, 1080x1920, brand-colour end card holding ~3s, plus a CTA variant driven by a HyperFrames composition variable. A subtle bottom-edge glitch Hugo spotted was diagnosed by frame-sampling and fixed with the over-cover pattern. This was the workspace's first real HyperFrames production piece taken all the way to a shippable render.
- **The full Friday grid package was built and the posting recipe proven on a mock account (Session 015).** 3-tile SPORTIF banner in three colourways, a tagline row in four directions with action imagery, and a live debug of Instagram's 1:1 default crop that was eating letters at tile edges. The recipe (tap Original, 1080x1440 tiles, post right tile first) is verified working.
- **A permanent funnel layer landed (Sessions 017–018).** Summit notes became `docs/funnel-playbook.md` (reusable, research-cross-checked) plus `clients/sportif/funnel-plan.md` (3 funnels, Klaviyo flow spine, budget), and an audit bound content to funnel: every post now carries exactly one CTA to the waitlist, FAQ is the fourth content lane, signups per post is a scorecard metric.
- **Key strategic unlock: the waitlist capture page does not need Shopify.** A standalone landing page can go live now, un-deadending every post and partially bypassing the months-long Lucy/Shopify blocker. This reframes the critical path and tops the Tuesday agenda.
- **Workspace hygiene caught up (Sessions 013–014).** Full review and cleanup, 9 superseded PDFs archived, five weeks of git work committed and pushed to GitHub, the CURRENT STATE block and two-environment sync protocol established, memory auto-archiving built, and the gpt-image-2 pipeline went live with the real Glacial Indifference font overlay pattern.

The one big miss: **the Friday 2026-07-10 IG launch did not happen.** Reason not yet logged; it's the first item on the Tuesday agenda.

### Patterns I noticed
- **Environment time caps keep dictating workflow design.** The 45s Cowork shell cap (iterate at low quality), the ~60s Claude Code HTTPS idle cap (medium quality only, streaming doesn't rescue it), and the native-Mac-terminal escape hatch all shaped this week's renders. The division of labour (author/iterate in Cowork, validate/render in Claude Code, true-high on native Mac) is now an explicit standard, as are path-portable scripts that run in all three.
- **Real-world testing beats desk work, again.** The mock IG account exposed the crop bug no amount of planning would have caught; Hugo's eyeball caught the bottom-edge glitch that `hyperframes validate` cannot see. Same lesson as the week of the competitor audit: verify on the real surface.
- **Lucy is the compounding bottleneck.** The feedback backlog grew all week (taglines, colourways, hero pick, blocker email reply) and the launch itself slipped on her side. The waitlist-page unlock matters precisely because it is the first workstream that routes around her rather than waiting.
- **Shipping beat perfection under deadline.** Session 016 consciously rendered medium-quality backgrounds rather than block the Friday deadline on true-high, with the upgrade path documented. Good instinct worth keeping.

### Skills / knowledge gained
- **HyperFrames production techniques:** composition variables (`data-composition-variables` + `--variables` at render), the Ken Burns over-cover rule (position images past the frame edge, on-brand page background as safety net), `data-layout-allow-overflow` for intentional overflow, and woff2 font conversion via fonttools.
- **Instagram mechanics:** the photo picker's 1:1 default crop breaks grid banners (tap Original), grid thumbnails are 3:4 so banner tiles should be 1080x1440, and IG added manual grid drag-reorder in June 2026.
- **Claude Code drops HTTPS responses after ~60s idle;** gpt-image-2 high quality exceeds it, streaming sends only one early partial, and the background-mode workaround is gated on OpenAI org verification.
- **Prompt-engineering fixes for the band imagery:** describe exercise poses joint by joint, and name the band form explicitly ("wide flat continuous closed loop... not a coiled tube") or it melts into ribbons.
- **Funnel method fundamentals** (Donati): one page one choice, the "How to [outcome] without [objection]" headline formula, honest scarcity, and the content x funnel mapping discipline — plus 2026 conversion benchmarks to sanity-check it.
- **Pillow has no letter tracking;** draw glyph by glyph with per-glyph advance.

### Open questions still unresolved

**Resolved this week (settled by a later session):**
- [x] ~~Did the Friday 2026-07-10 IG launch happen?~~ RESOLVED Session 018: it did NOT happen; reason to be captured at the Tuesday meeting.
- [x] ~~Re-render the 3 action backgrounds at quality high before Friday (Session 015).~~ RESOLVED Session 016: rendered at medium (60s cap blocked true-high), Reel launch-ready; true-high remains an optional upgrade.
- [x] ~~Hugo to git push from the Mac (~10 commits ahead).~~ RESOLVED Session 014: pushed, in sync at the time (local is ahead again after 017–018; push at next Claude Code session).
- [x] ~~Friday grid posting plan (banner row, tagline row, teaser Reel first).~~ OVERTAKEN: launch slipped; re-plan against the new date from the Tuesday meeting.

**Still open (carried into next week):**
- [ ] **Tuesday 2026-07-14 Lucy meeting:** launch slip reason + new launch date, standalone waitlist page approval, Lucy-session incentive decision (A/B/C), Shopify blockers. Agenda in funnel-plan.md.
- [ ] **Build the standalone waitlist capture page** once approved (Klaviyo or similar; no Shopify needed).
- [ ] **Write the 3-email welcome flow** (carried from 017; unblocked, ready-when-page-ships).
- [ ] **Lucy blocker email:** still sitting in Hugo's Gmail drafts; attach the two PDFs and send (or fold the four asks into the Tuesday meeting).
- [ ] **Lucy feedback backlog:** four tagline-row directions, three banner colourways, hero-concept pick (v5/v6/v7).
- [ ] **Confirm whether the 500 band units have landed;** if yes, film the unboxing.
- [ ] **Ambassador/instructor seeding shortlist** (main growth engine, still not started, unblocked).
- [ ] **Shopify coming-soon page / store build** (research done, waiting on Lucy opening the account).
- [ ] Optional: true-high background re-render via native Mac terminal or after OpenAI org verification.
- [ ] Optional: teaser voiceover (TTS via hyperframes-media), undecided.
- [ ] Carried: trademark clearance, materials question (gates sustainability copy), Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins (switch on next edit), consider adding `git push` to the Claude Code close-out ritual.

### Suggested focus for next week
1. **Make the Tuesday Lucy meeting count.** The agenda is already staged in funnel-plan.md: get the launch slip reason and a new launch date, approval for the standalone waitlist page, the incentive decision (A/B/C), and movement on the Shopify blockers. This one meeting unblocks nearly everything else.
2. **Stand up the standalone waitlist capture page immediately after approval.** It is the first workstream that does not wait on Shopify, it un-deadends every piece of content already built, and the Funnel 1 spec is written. Pair it with the 3-email welcome flow so capture and nurture ship together.
3. **Start the ambassador/instructor seeding shortlist.** It has been carried for four straight weeks, it is the designated main growth engine, it needs lead time before any launch date, and it requires nothing from Lucy.

---

## Session 026 (2026-07-24, Claude Code): memory system v2 — hardening for scale (multi-client)

Client: Ochoproductions (workspace infrastructure)
Tags: memory-system, tooling, scaling

Hugo asked for an honest rating of our memory system, then to implement the fixes since the workspace will scale to more clients. Rated it ~8.5/10 for a solo/single-client setup, ~6/10 unmodified at team/multi-client scale; the real ceilings are RETRIEVAL (linear grep, decays with size) and COMPLIANCE (close-out is manual, a single point of failure — we already lost the Tuesday-meeting outcomes once). Built four fixes, all low-tech + stdlib, preserving the plain-markdown legibility.

- **DECISION: adopted memory system v2.** New tool `scripts/memory_tools.py` with subcommands: `check` (verifies close-out: CURRENT STATE dated today + a session entry today + registries well-formed), `index` (regenerates `memory-index.md`, a TOC of every session hot+archived), `search` (grep across memory+registries+docs), `decisions`, `open` (both filter by `--client`; `open` flags questions aged >= N sessions), `reconcile` (flags dead file refs in CURRENT STATE, stale date, aged questions), `install-hooks` (git pre-push warn hook, `MEMORY_ENFORCE=1` to block).
- **DECISION: decisions and open-questions are now first-class registries** (`DECISIONS.md`, `OPEN-QUESTIONS.md`) with a parseable one-line schema incl. a Client field — the two things we re-query most are extractable, not buried in prose, and filter by client.
- **DECISION: multi-client convention.** Session entries now carry `Client:` and `Tags:` lines; registries carry a Client column. One unified chronological log (keeps cross-client learnings) but everything filterable per client. CURRENT STATE will split into per-client mini-blocks once >1 client is active.
- Installed the pre-push hook (warn-only) and regenerated `memory-index.md`. `archive_memory.py` unchanged (still the size-triggered archiver).
- Updated `CLAUDE.md` (close-out ritual now runs `memory_tools.py check` + `index` and updates the registries) and rewrote `docs/memory-system.md` to v2 (Hugo will share that once updated).

LESSON: the compliance SPOF is the biggest real risk as we scale — the `check` hook is the mitigation, but it's warn-only by choice to avoid friction; flip `MEMORY_ENFORCE=1` if close-outs start slipping.

---

## Session 025 (2026-07-23, Claude Code): fresh gpt-image-2 GENERATION pipeline + finished ads + Canva workflow

Big session, two new capabilities established.

**1. Fresh from-scratch imagery (not edits).** First use of the gpt-image-2 `images/generations` endpoint (vs edits). `clients/sportif/scripts-local/gen_fresh_explore.py` generates Sportif key visuals from detailed prompts across 3 directions (brand-world lifestyle `bw*`, campaign hero `ch*`, band-in-use `bu*`), 1024x1536, quality low in-harness (high needs a native Terminal). Iterated v1->v5 as Hugo caught issues, each fix is a DURABLE PROMPT LESSON:
- **v1->v2 photoreal:** plain low proofs looked "a bit AI" (waxy/over-smooth). A REALISM block (`real` 3rd arg: 35mm Portra 400, 50mm, real skin texture/pores/flyaways, film grain, forbid glossy/plastic/CGI) markedly cut the AI look.
- **v3 skin-contrast colour:** flesh-adjacent activewear colours (blush/caramel/sand) read as NUDE/underwear on warm skin. Added a WARDROBE block forcing a skin-CONTRASTING colour (clay/rose/oatmeal) + defined waistband + "not nude/bodysuit"; stripped flesh colours from every prompt.
- **v4 material:** everything rendered as RIBBED seamless knit, wrong for activewear. Real premium activewear is SMOOTH matte four-way-stretch (Lululemon/Alo). Reworked WARDROBE to smooth-fabric + explicit NOT-ribbed forbids; removed "ribbed" from all clothing (band stays knit, that IS the product). v4 = the clean warm-neutral base.
- **v5 colour/pattern exploration** (`PATTERNS=1` env): per-shot COLORWAYS (sage, mocha+cream trim, plum, slate blue, rust, earth-tone print). Earth tones read most on-brand; plum/slate blue add accent range; contrast-trim is a keeper detail.
- Also fixed a bad outfit render (nude long-sleeve unitard) by naming the actual garments (two-piece set) + skin-contrast tone.
**Three lessons to carry into any future shoot brief:** name the actual garments; garment colour must contrast skin; garment material = smooth four-way-stretch (not ribbed). See [[real-band-content-pipeline]].

**2. Real band into generated shots + finished ads.** `realband_in_hand.py` two-image-stamps the real SPORTIF MEDIUM label onto the AI-imagined band in a generation (works in-hand or around thighs). `campaign_skin.py` (full-bleed, right-aligned type) and `ad_lifestyle.py` (crops 2:3 -> IG 4:5 1080x1350, headline/subline/colour as args) skin shots into finished ads. Made 3 finished IG ads: FIND YOUR RESISTANCE (real band held), STRENGTH IN STILLNESS (mocha set, warm-charcoal type after Hugo rejected navy), MADE TO MOVE (plum). Navy type fights the warm palette; use warm charcoal #4A433C or cream on terracotta.

**3. Canva workflow (two avenues).** THE MENTAL MODEL: **Avenue 1 = our pipeline (studio, exact brand control, flat/final); Avenue 2 = Canva (workbench, editable + shareable).** They chain: our pipeline -> Canva -> Lucy. Set up in Hugo's connected Canva: folder **Sportif** (id FAHQK6iSi6I) with **IG Ads** (FAHQK6gD-Do) + **Source Photos** (FAHQK2bvCGc). Local staging mirror at `clients/sportif/canva-exports/` (gitignored binaries, README tracked); finished assets get copied there for easy drag-in. Canva findings/GOTCHAS:
- **Cannot auto-upload our local files** (connector only ingests PUBLIC URLs; must not publish private brand assets). Hugo drags PNGs in manually (seconds).
- **CAN generate native editable designs** (`generate-design` -> candidates -> `create-design-from-candidate` -> `move-item-to-folder`). Long/complex briefs with hex codes FAILED ("design generation failed"); a SHORT simple brief succeeded. Made 5 editable "Find your resistance" designs.
- **Can use OUR photo in a Canva design** by passing `asset_ids` of an image Hugo already uploaded, but Canva only reliably used it in 1 of 4 candidates (substituted stock in the rest). Reliable path: in the editor, click image -> Replace -> our uploaded asset.
- **PLAN-GATED (both need Canva Pro, Hugo getting it ~next week, 2026-07-30ish):** (a) brand kit (fonts/colours/logo so generations come out on-brand), (b) FOLDER sharing (the "one permanent link, auto-updating, real-time with Lucy" setup). On FREE, only per-DESIGN link sharing works (Share -> Share link -> Anyone with link -> can comment -> Copy link). The `/d/` URLs from the API are private editor links and 404 standalone; the real share link is the one generated via Share->Copy.

**Still open:** Hugo to get Canva Pro (~next week) -> then set up Sportif brand kit + share the Sportif folder with Lucy (lucy@lucywayne.com.au). Lucy still to pick music-bed pacing. Standalone waitlist capture page STILL the top unbuilt item (needs neither Lucy nor trademark). Trademark gate unchanged.

---

## Session 024 (2026-07-22, Claude Code): reference-layout reskin (Lucy's pilates-studio ad to a Sportif waitlist poster)

Lucy sent a reference: a pilates-studio "WE'RE OPEN / First class is free" launch ad (tan colour block + oversized PILATES watermark + two models, one glute-bridge with black ankle weights, one on a reformer). She asked us to reskin it as Sportif: keep the layout, put OUR band on the model, change the wording, add the logo. Saved to `clients/sportif/products/reference-layouts/pilates-open-ref.png`.

**Established the "reference reskin" technique = AI plate + our own type layer** (Hugo: "NO YOU LAYOUT TEXT, THATS OUR WORKFLOW"):
1. **No-text plate via gpt-image-2 edits** (`scripts-local/reskin_pilates_ref.py`): edit the reference to a CLEAN plate — strip ALL text and the watermark, add a blush booty band, remove the black ankle weights — keeping layout/poses/palette. Generated TWO pose variants to compare: `asis` (keep her raised leg; AI looped the band on the single raised thigh = ambiguous) and `bridge` (convert to a standard two-foot glute bridge; band loops both thighs = clear "in use"). Bridge won.
2. **Our type layer in PIL** (`scripts-local/layout_reskin.py`, system python): all copy in Glacial Indifference, matched navy #13253D / cream #F4EEE5 sampled from the reference. Copy set "Find your resistance": kicker `meet` (small) over `SPORTIF` (bigger, real logotype = Regular + -0.059 lockup tracking), headline `FIND YOUR / RESISTANCE` (cream, soft drop-shadow so it stays crisp where it crosses the photo), faint oversized `SPORTIF` watermark, a solid terracotta `JOIN THE WAITLIST` CTA pill (with lift shadow), the SPORTIF lockup, and `@sportifcollection`.

**Design iterations Hugo drove (each a one-line tweak in the layout script):** first CTA was a wobbly hand-drawn arc — rejected as bad design, replaced with a proper opaque terracotta pill; filled the left cream void with a framed single-band product card (the blush MEDIUM card, `place_band_card`, rounded + shadow + cream border) so product ties to the lifestyle shot (the blend insight, now inside one still); split "meet sportif" onto two lines; switched the kicker to the real logotype font; opened the meet/SPORTIF gap and made SPORTIF bigger; raised the headline ~15% to clear the doorway.

Two finals kept in `clients/sportif/generated/images/reference-reskin/`: `reskin-bridge.png` (the lead piece, with the band card) and `reskin-asis.png` (dramatic raised-leg alt, no room for the card). Both are soft waitlist teasers with NO dates (respecting the trademark hold). Scripts are the source of truth (finals gitignored). Copy/colour/logo font all editable in one line.

**Key learnings:** (a) the reskin technique generalises — hand any reference layout, get a no-text AI plate, own the type in PIL; (b) generate BOTH plate variants when a pose is ambiguous and let the product-clarity decide; (c) a solid opaque CTA pill sits cleanly over any busy area where a thin script line looks amateur; (d) dropping a matching single-band product card into negative space delivers the lifestyle+product blend inside a single still. See [[real-band-content-pipeline]].

**Still open (unchanged):** standalone waitlist capture page (needs neither Lucy nor trademark, still the top unbuilt item); Lucy's music-bed pick; high-res finals past the ~60s cap; trademark gate.

---

## Session 023 (2026-07-22, Claude Code): real-band product content pipeline (restage, cards, range reel, 2 blends)

Lucy sent Hugo 3 real photos of the bands she received (saved to `clients/sportif/products/real-bands/`). They were casual counter snapshots (clutter, harsh light, all three folded label-end) BUT the product is bang-on brand: the three colourways (HEAVY terracotta / MEDIUM dusty blush / LIGHT sand-cream) ARE the peach palette, and the rubber labels carry the real SPORTIF lockup + resistance tier. This validated the whole peach direction and meant real product could intercut with the AI lifestyle shots seamlessly.

Built a staged product-content suite (Hugo directed "we do in stages"):
1. **Restaged flatlay** via gpt-image-2 `images/edits` (`scripts-local/gen_band_product.py`): scoped "keep the product EXACTLY identical, only change surroundings" prompt strips clutter and drops the bands onto clean peach, holding the labels crisp **even at quality low**. High quality hits the ~60s Claude Code cap (RemoteDisconnected, background doesn't help) -> run from a native Terminal.
2. **3 individual hero cards** (`scripts-local/make_band_cards.py`): cropped each band from the flatlay. Hugo caught a left-edge artifact -> the bands TOUCH, so equal-thirds cropping bled a neighbour sliver onto each card. Fixed by detecting true edges (texture variance for outer, colour/brightness boundary at x~592 for the H/M seam) and cropping inset off the seams.
3. **Range reel** `compositions/sportif-band-range/` (calm Light/Medium/Heavy). Feathered the flatlay edge (Gaussian border alpha) so its peach melts into the peach frame (no rectangle) -- Hugo asked to fix that before viewing.
4. **Two lifestyle+product blends** (Hugo's idea, wanted BOTH): `sportif-blend-cuts` (rhythmic beat-cut, lifestyle cover + product contain, 120 BPM) and `sportif-blend-calm` (editorial card-on-peach story with taglines). Both got mood-matched scratch music. Hugo: "they both look great as concept pieces."

Full reusable pipeline + gotchas written up at `clients/sportif/products/real-bands-content-process.md`. See also [[real-band-content-pipeline]] and [[hyperframes-0-7-tooling]].

Key process learnings (also in the pipeline doc): scope gpt-image-2 edit prompts to keep-product-identical; low quality is fine for social; touching products need colour-boundary crop detection not equal thirds; feather peach-on-peach edges with a blurred alpha mask; the lifestyle+product BLEND is the strongest format (desire + product, but juxtaposition not literal use -- literal-use is the unbuilt Stage 5 composite); system python has PIL-not-numpy, the .venvs/tts python has numpy-not-PIL.

**Stage 4 (they've landed teaser) and Stage 5 (band-in-use pilates reel) both DONE this session.** Stage 4: `compositions/sportif-they-landed/` — announcement teaser, bouncy pop-in headline (+wiggle), popping product reveals, "Find your resistance." band line, "Join our community" CTA pill. Stage 5: `compositions/sportif-band-inuse/` — three pilates poses (standing abduction / squat / lateral walk, barefoot) with the real SPORTIF label stamped via the two-image gpt trick, CTA pill, two music beds (calm + upbeat) for Lucy to pick pacing.

**Stage 5 detours worth remembering:** client gym shots were off-brand (black weights gym, glam register) and even tripped AI `[sexual]` moderation, so we GENERATED fresh modest pilates scenes instead; the real-label two-image stamp at LOW quality looked natural (Hugo preferred it over a pixel-perfect but pasted-looking composite); high-quality label re-render kept hitting the ~60s cap even in the VS Code terminal. Full pipeline + all scripts documented in `real-bands-content-process.md` and each comp's design.md. See [[real-band-content-pipeline]].

**Still open:** print-quality high-res product/in-use finals (need a real macOS Terminal or cloud to beat the ~60s cap); Lucy's pick between the two music beds; and the ORIGINAL top item — the standalone waitlist capture page — still unbuilt (needs neither Lucy nor trademark).

---

## Session 022 (2026-07-22, Claude Code): peach beat-cut montage + scratch music + ElevenLabs setup

Continuation of the Session 021 chat into the next day. Hugo asked for a "quick cut" beat-synced montage from the peach images (different energy from the calm lookbook reel).

**Built `compositions/sportif-peach-cuts/`** (15s, 1080x1920, one file for IG Reels + TikTok). Generated from `build_cuts.py`: a 120 BPM grid of hard cuts with a per-image zoom-punch. Structure: SPORTIF wordmark flash (0-1s), 14 cuts on the beat (1.0-7.5s), a double-time build through the punchiest shots (8-11s), date-free "Coming soon" end card holding ~3.5s to 15s. Full-bleed (punchier than the lookbook's cards) but center-crops the group shots at the edges (acceptable at cut speed). Keeper: `renders/sportif-peach-cuts_v3_high.mp4`.

**Iteration notes (all Hugo feedback):** he liked the cut length + acceleration + zoom-out immediately. Two fixes: (1) extended the end-card hold from ~0.2s readable to ~3.5s (total 12s -> 15s) because the logo only flashed; (2) real bug found by the snapshot QA: the intro's shared `.wm`/`.rule` GSAP selectors also grabbed the end-card wordmark and left it hidden, so the end card showed only "Coming soon" without the SPORTIF lockup. Fixed by scoping the intro selectors to `#intro`. Lesson: scope GSAP selectors per section when class names repeat across scenes.

**Music.** Hugo needed audio to judge the edit. Can't generate licensed music locally (that's HeyGen, which he declined). Synthesized a SCRATCH 120 BPM bed via `scratch_music.py` (numpy/soundfile in the .venvs/tts python: kick on the beat, offbeat hats double-timing through the build, A-minor pad + sub bass), muxed on as `_MUSICDEMO.mp4`. Hugo: "nailed it, the sound helps match the cuts." He is showing the MUSICDEMO to Lucy as a future-feel preview. IMPORTANT: scratch track is unlicensed, internal preview only, never publish it. Real posts get a licensed track (in-app on upload, or send a file and mux + `hyperframes beats` for exact sync).

**ElevenLabs wired (Hugo asked "would elevenlabs be better?" — yes, far more natural than Kokoro).** Promoted the `.env.example` slot to active, added `ELEVENLABS_API_KEY=` to the gitignored `.env`, and wrote `scripts/elevenlabs_tts.py` (zero-dep urllib helper: text -> mp3, reads key from .env, `--list` voices, default warm-female "Sarah" voice). Ready the moment Hugo pastes a key. Best for future narrated content (founder story, product explainer), not beat-cut montages.

**Close-out:** committed both compositions' source (renders/audio/snapshots gitignored), the ElevenLabs setup, and this log. See [[hyperframes-0-7-tooling]].

---

## Session 021 (2026-07-21, Claude Code): housekeeping + logged the Tuesday 2026-07-14 Lucy meeting outcomes

Opened with the sync ritual. Cleaned up Session 020's Cowork-cloud leftovers on the Mac (`.git/*.lock`, `_to_delete/`, stale `tmp_obj_*` objects), confirmed a clean working tree, and pushed 8 commits to GitHub (`43e89a7..fd8d0af`, now in sync). memory.md at 86KB, no archive needed.

**Main event: the Tuesday 2026-07-14 Lucy meeting outcomes, finally captured** (Hugo relayed them). The picture is quieter than the funnel-plan agenda hoped for:

1. **Launch: no launch, held indefinitely.** Lucy is holding off pending trademark talks with her lawyer. No new date, no timeline.
2. **Waitlist capture page: never put to Lucy.** Hugo did not show or ask her about it. So the "does the standalone page get approved" question is still open, but note the page does NOT need Lucy's approval to build, only to point her domain at. We can build it now.
3. **Incentive decision (A group session / B capped 1:1 / C video series): still undecided.** Lucy will get back to Hugo.
4. **Shopify: no movement.** Also gated on the trademark talks with the lawyer.
5. **The 500 band units HAVE landed.** Physical product is in hand. Unboxing footage is now filmable.

**What this changes.** For weeks the framing was "Shopify is the critical path, blocked on Lucy." The real gate is now clearly **trademark clearance**, which sits upstream of Shopify, the launch, and the whole go-to-market, and is entirely on Lucy's lawyer's clock. Nothing we do accelerates it. The correct response is to stop treating the launch as imminent and instead bank everything that does NOT depend on trademark: build the standalone waitlist page (build now, wire up later), draft the 3-email welcome flow, start the ambassador/instructor seeding shortlist (carried five+ weeks, needs nothing from anyone), and film the unboxing now that bands are here.

**Open questions:** trademark timeline (unknowable, Lucy's lawyer); incentive A/B/C (pending Lucy); whether to still bother showing Lucy the waitlist page before building it (recommend: build it regardless, it's the only unblocked go-to-market surface).

**Second half of the session: Hugo asked for a HyperFrames video from the peach images.** Built `compositions/sportif-peach-reel/` (15s, 1080x1920, one file for IG Reels + TikTok) reusing the sportif-teaser engine. Decisions (Hugo picked): card-on-peach framing (each 4:5 shot whole on the blush ground, no crop, premium lookbook feel), proven Lucy-voice taglines, date-free "Coming soon" end card (launch on hold, so no date). Three cosmos-peach text-free bases: studio-yellow-frame / portrait-sage-tank / beach-run-shoreline. Keeper: `renders/sportif-peach-reel_v2_high.mp4` (silent, add a soft music bed in-app on upload). It is a brand-MOOD piece, not product (no band/strap, not real Lucy) — fine for the pre-launch hold; a product-forward cut waits on real Lucy + product footage (bands have landed, unboxing filmable).

**HyperFrames upgraded 0.6.37 to 0.7.64 (new features explored):**
- The stricter one-shot `check` gate caught a latent bug our old lint missed: full-frame scene overlays that start visible before their fade (`gsap_fullscreen_overlay_starts_visible`). Fixed with explicit `opacity:0` + `.to()` reveals. Real robustness win, applies to the teaser too if we ever touch it.
- `snapshot` = built-in frame verification; auto-builds a contact sheet AND runs Gemini vision over each frame (descriptions.md) to flag blank/black frames. Replaces manual ffmpeg frame-pulling. Snapshots are regenerable QA, now gitignored.
- Rendered at `-q high` (7.9MB vs 4.6MB standard).
- `tts` (Kokoro-82M, local, free, offline) PROVEN but NOT used: Hugo found the voice "very AI." Needed a Python 3.11 venv (system python 3.9 too old for kokoro-onnx); venv at `.venvs/tts` (gitignored), point `HYPERFRAMES_PYTHON` at it. Full recipe in the composition's design.md. For a natural read, use a real voice or HeyGen cloud voices, not Kokoro.
- `cloud` (HeyGen server-side render, kills the local render-cap problem) NOT adopted: needs a HeyGen account (`auth login`, billed). Hugo declined — local high-quality is good enough for 1080p social. Revisit only if we need 4K or hit local caps.
- Other new-but-unused commands worth remembering: `beats` (sync cuts to music), `compare` (variant comparison sheet), `grade-compare` (colour grades), `remove-background` (transparent product cutouts, useful once real product footage exists), `keyframes` (onion-shot diagnostics).

**Decision: keep video renders local for now** (Hugo, Session 021). No cloud rendering. The silent v2 is the deliverable; music and any VO get added in-app or in a later pass.

---

## Session 020 (2026-07-20, Cowork cloud): Cosmos folder renamed, full 15-image peach series shipped, Lucy approved

Continuation of the Session 019 chat. Hugo picked the Cosmos references for posture/colour/look and asked for the peach theme to run through all of them with the narrow Sportif lockup, Instagram 4:5.

### What we did
- **Renamed all 17 files in `assets/Cosmos pictures`** to descriptive names (mapping in commit 86b5b2e); image-prompts.md source path updated.
- **Built a 4-worker batch pipeline over the gpt-image-2 edits endpoint:** a handwritten prompt per image, peach palette outfits (palette MIX across group shots so they read as a collection drop), backgrounds warmed to brand neutrals, everything recomposed to 4:5. Low-quality proofs (~$0.01 each) -> Hugo reviewed a contact sheet -> 1088x1360 quality-high finals -> narrow (62 percent) Sportif lockup stamped (cream; peach on the two palest images).
- **Lucy saw the proofs and loves all 15** (via Hugo). Finals + text-free bases saved to `clients/sportif/generated/images/cosmos-peach/` and `cosmos-peach/notext/`; originals in assets untouched. Prompts preserved verbatim in `clients/sportif/scripts-local/gen_cosmos_peach.py`, summary in image-prompts.md.

### What we learned
- **`cosmos_bw-arms-detail` is hard-blocked by output moderation** (3 of 3 attempts, tight body crop); the safety-framing sentence that rescues full-figure poses does not rescue tight crops. Skip it or recompose wider first.
- Staged uploads keep their staging-time filenames; after renaming on the Mac, re-stage or map old to new before batch runs.
- One transient proxy error on a high render; a simple retry fixed it.
- **Mid-session the device trust went stale:** device_stage_files began returning 403 untrusted_device while device_bash and earlier commits kept working. Fix: Hugo re-signs in via the desktop app banner. Text edits can be done through device_bash directly as a fallback.

### Open questions
- `cosmos_yoga-duo.mp4` untouched; a peach video edit would need the Seedance path.
- Tuesday 2026-07-14 Lucy meeting outcomes STILL not logged (carried again).

## Weekly Review, 2026-07-05 (week of 2026-06-29)

One session this week (012), all on Sportif. After the previous week locked strategy, this week was about turning a pile of overlapping documents into a clean, client-ready package: the Brand Value Plan was rebuilt from the ground up and the four confusing Lucy-facing PDFs were consolidated into two.

### Highlights
- **The Brand Value Plan got a full visual and structural rebuild.** New magazine-split cover (FLOW band photo full-height, Lora serif title, letter-spaced Poppins wordmark), an editorial card layout, and, importantly, a regeneration from the *current* source so the stale pre-06-18 body is gone. A reusable, path-independent generator (`build-brand-value-plan.py`) was saved so re-export is now one command.
- **A customer-facing cleaning pass was added.** The generator now strips internal dev notes, dates, and session markers at export time while the source markdown keeps its full provenance, verified with pdftotext. This is a real methodology win: Lucy gets a clean deliverable, the source of truth stays intact.
- **Four overlapping Lucy-facing PDFs were consolidated into two.** A strategy cut (`Sportif-Brand-Value-Plan.pdf`, slimmed to idea + six levers + "What winning looks like") and an operations cut (`Sportif-Launch-Plan.pdf`, with a new single hub-and-funnel SVG diagram replacing two duplicate flow docs, the Shopify store, the phase-by-phase plan, and "What we need from you"). Nothing had been sent to Lucy yet, so this cleanup landed before any confusion reached her.

### Patterns I noticed
- **The "two documents, one internal source and one clean client cut" pattern kept recurring.** It showed up repeatedly this session (`brand-value-plan.md` vs `brand-value-plan-client.md`; `launch-plan-client.md` driving its PDF; the detailed working docs kept as source of truth). It has become the workspace's default way to keep provenance without exposing it to Lucy. The standing risk it creates: two files can drift, so an internal change has to be reflected in the client cut too.
- **"A mum can read it" is still driving every client-facing edit,** same as prior weeks: one-line ideas, tighter bullets, clearer titles, internal "DO NOW" boxes relabelled to "What we'll implement" or removed. Anything Lucy sees gets softened and de-jargoned.
- **Iterative restructuring under Hugo's live review.** The plan was reworked at least three times in the session (cover redo, tighten-for-client cut, four-to-two consolidation), each pass triggered by Hugo looking at the rendered output. Same "the rendered reality overrides the first draft" rhythm seen in prior weeks with the research.
- **Sandbox instability is a recurring tax.** A mid-session reboot wiped the pip-installed weasyprint and the outputs dir and changed the host outputs path, echoing earlier notes about background processes and per-sandbox reinstalls. The durable fix held: keep deliverables in the mounted hyperframes folder, treat the outputs dir as throwaway.

### Skills / knowledge gained
- **Sandbox fonts are limited to Lora (serif) and Poppins (geometric sans);** Glacial Indifference (Sportif's real font) is not installed, so Poppins letter-spaced stands in for the SPORTIF wordmark and Lora carries the titles. Looks intentional.
- **The FLOW reference image has old experiment text baked into its top ~268px,** so it must be cropped before reuse.
- **File deletion in the mounted folder now works** via the `allow_cowork_file_delete` tool (previously blocked, overwrite was the only option).
- **present_files does not reliably show a PDF preview in chat;** a combined PNG montage of the pages is the reliable way to let Hugo see multi-page output.
- **A generator that derives its paths from `__file__`** (rather than hard-coded session paths) survives sandbox session-id changes, which is what makes one-command re-export possible.

### Open questions still unresolved

All pulled from Session 012 (the only session this week). None have a later session yet, so all remain open:
- [ ] **Decide whether to archive or delete the three superseded client PDFs:** `Sportif-Action-Plan.pdf`, `Sportif-Digital-Plan-for-Lucy.pdf`, `Sportif-Socials-to-Shop.pdf` (pending Hugo's ok).
- [ ] **Apply any further tweaks Hugo sends** to `brand-value-plan-client.md` or `launch-plan-client.md` and re-run the matching generator.
- [ ] **Write the Shopify coming-soon page step-by-step** (already researched, waiting on Lucy opening the account).
- [ ] **Items waiting on Lucy:** prices (and the ~$70 pouch threshold), fabric / materials, opening Shopify.
- [ ] **Customer-comms setup:** the Sportif inbox + Lauren + Klaviyo automations (the 7-day no-reply flag from Session 011 is still unaddressed).

### Suggested focus for next week
1. **Get Hugo's sign-off to archive or delete the three superseded PDFs** and lock the two-document set (strategy + operations) as the single Lucy-facing package, so there is one clean pair ready to send.
2. **Write the Shopify coming-soon page step-by-step now.** The research is done and the band ships early July with still nowhere to sell it, so this is the standing critical-path revenue blocker; having the guide ready means Lucy can act the moment she opens the account.
3. **Bundle everything blocked on Lucy into one short ask** (prices + pouch threshold, fabric, opening Shopify, who answers customers), so the build workstreams can finally start.

---

## Weekly Review, 2026-06-21 (week of 2026-06-15)

Four sessions this week (008, 009, 010, 011), all on Sportif. This was the week Sportif went from "research and assumptions" to "real client, real meeting, locked decisions", and the positioning narrowed twice under real-world constraints.

### Highlights
- **First in-person meeting with Lucy, and three big open calls finally settled (Session 011).** Hugo met her face to face and folded her answers into all three source-of-truth docs (`brand.md`, `synthesis-brief.md`, `brand-value-plan.md`). Name LOCKED as **Sportif** (open since Session 007), hero product LOCKED as **the band sold inside a giftable set**, and go-to-market LOCKED as **parallel wholesale + DTC** (not "wholesale-first"). The pouch was reclassified as a gift-with-purchase over ~$70, not a product to sell.
- **The entire Sportif research run executed end to end (Session 008).** All 5 Perplexity passes (segment + 8 competitor deep-dives + references + cultural-lane + budget), synthesized into `brand.md`, with the Stage 3 synthesis brief drafted. This cleared the Session 007 egress blocker and required building a brand-new async tooling pattern to do it.
- **The hands-on competitor audit produced the week's biggest strategic correction (Session 009).** Hugo photographed all 8 named competitors and we built a visual product board from live Shopify `/products.json` data. The finding: the colourful band/strap space is NOT empty (Move Active, Your Reformer, Avara, Kikiva already sell colour), correcting the original desk-research belief. The "real gap is pattern" thesis was born here.
- **Positioning pivoted from product-led to founder-led (Session 011 follow-up).** Once we learned the manufacturer's real constraints (China, ~35-day turnaround, predefined colourways only, no custom pattern), the pattern bet was deferred and the differentiator moved decisively to **Lucy Wayne herself**, her brand, eye, and the community/experience around a standard factory product. Lever 2 of the Brand Value Plan was elevated to THE primary lever.

### Patterns I noticed
- **Reality kept overriding desk research, every single time.** The colourful-space-isn't-empty correction came from Hugo actually browsing competitor sites, not from more analysis. The pattern-is-impossible / colours-are-constrained correction came from learning the manufacturer's real terms. The differentiator hunt narrowed three times in one week, **colour → pattern → Lucy herself**, each step forced by a constraint we didn't know before. Lesson: hold product-based differentiators loosely until manufacturing is confirmed.
- **Devil's advocate passes keep earning their keep.** The digital-plan pass in Session 011 surfaced that **@lucywayne__ has only ~900 followers**, which reframed the entire growth plan from "borrow her audience" to "build one" and promoted ambassador/instructor seeding to the main growth engine.
- **"A mum can read it" is a recurring requirement.** Hugo flagged jargon in Session 009, asked for Claude's own extra questions to be stripped from Lucy's meeting guide (Session 010), and wanted a non-technical WhatsApp guide for the email setup (Session 011). Anything Lucy-facing must be jargon-free.
- **Em-dash leakage, again.** Session 008 had to sweep em/en dashes out of the Perplexity research outputs. Same recurring problem flagged in prior weeks, automated outputs reintroduce them.

### Skills / knowledge gained
- **Cowork environment limit + the fix.** Background shell processes do NOT survive across separate tool calls (the sandbox reaps them; ~45s per call). So the "launch deep-research with nohup and poll" workflow from CLAUDE.md does not work here. Fix built: `scripts/pplx_async.py` submits async Perplexity jobs server-side, persists request IDs to disk, and polls in later short calls. Perplexity rate-limits async submissions (HTTP 429), stagger submits and resubmit-on-fail.
- **Manufacturing reality (the constraint that reshaped strategy).** Lucy's manufacturer is in China, ~35-day turnaround from order, predefined colourways only, no custom pattern. This single fact killed the pattern bet and constrained the palette.
- **Market price anchors are now documented:** booty bands ~$29, ankle straps $30 to 39, grip socks $9 to 39, towels $26 to 79, pouches $70 to 249. Branded pouches do sell (Anine Bing $249 sold out, ODE $70). Towels are in demand.
- **Tooling gotchas captured:** public Shopify `/products.json` gives live prices/images (use `?limit=`); remote images don't render in local HTML so embed base64; local screenshots embed fine but remote binaries can't be downloaded; macOS screenshot filenames contain a no-break space (rename by glob order); deletions are blocked in the mounted folder (overwrite instead); the Read tool can't see brand-new files at the workspace path (copy to outputs to view).
- **2026 digital best practices:** IG product tags now live in Reels (link-in-bio dying), TikTok Shop AU launching 2026, Facebook is an ads/tracking engine not an organic channel, Klaviyo welcome-flow timing matters.

### Open questions still unresolved

**Resolved this week (settled by a later session):**
- [x] ~~Settle the three devil's-advocate calls (hero product, go-to-market, pattern).~~ RESOLVED Session 011: hero = band-in-set, go-to-market = parallel wholesale + DTC, pattern = deferred.
- [x] ~~Lock the brand name.~~ RESOLVED Session 011: name LOCKED as **Sportif** (trademark clearance still pending separately, see below).
- [x] ~~Decide whether the band, strap, pouch, or set should be the hero.~~ RESOLVED Session 011: the band leads, presented inside a giftable set.
- [x] ~~Validate the pattern bet / confirm pattern is manufacturable.~~ RESOLVED Session 011 follow-up: manufacturer offers predefined colourways only, no custom pattern, Step 0 pattern gate closed as DEFERRED.
- [x] ~~Confirm Lucy's custom colours are distinct from Kikiva / Your Reformer.~~ SUPERSEDED Session 011: colours are constrained to the manufacturer's predefined range, so colour is no longer the differentiator; Lucy is.
- [x] ~~Set up the EA's (Lauren's) lucywayne.com.au mailbox.~~ RESOLVED Session 011 follow-up: Workspace already exists, domain at GoDaddy, so it's an add-a-user job; a non-tech WhatsApp guide was produced.

**Still open (carried into next week):**
- [ ] **Trademark clearance**, name is chosen but legal clearance is still in progress with Lucy's lawyer. Hold logo/label-dependent finals until clear.
- [ ] **Materials**, which of recycled / organic / hemp Lucy can actually use. Still being chosen; gates any sustainability claim in copy.
- [ ] **One Shopify store or two**, recommendation logged (one store with Shopify Markets, split later only if forced); confirm with Lucy.
- [ ] **Execute the build workstreams**, Shopify store build, Instagram Shopping setup, content posting calendar, unboxing content ideas for Lucy to self-film, podcast outreach. (EA email is done; the rest are open.)
- [ ] **Ambassador / instructor seeding shortlist**, build it ready for the early-July band delivery; this is now the main growth engine.
- [ ] **Tight Lucy-facing competitor snapshot**, open since Session 009 (the full internal board is too big to send her).
- [ ] **Session 008 Step 11**, fold Sportif AUD budget numbers into `docs/marketing-fundamentals.md` Part 8.
- [ ] **Session 008 Step 12**, the "where we are" summary email to Lucy (largely superseded by the in-person meeting; decide whether it's still needed or can be closed).
- [ ] **Validate low-confidence competitor prices** (Leelo, Avara, Kikiva, Your Reformer), partially addressed by Session 009's live-Shopify capture, but not all confirmed.
- [ ] **Lucy's Leelo quality-check notes**, add when her ordered Leelo item arrives (open since Session 008).
- [ ] **Document the `pplx_async.py` async pattern** in the workspace gotchas so future Cowork sessions use it by default.
- [ ] **Stage 4 production**, pick the first production need from the winning angle and write the gpt-image-2 prompt(s).

### Suggested focus for next week
1. **Start the build workstreams now that strategy is locked, Shopify first.** The band ships early July and there is currently nowhere to sell it. Confirm the one-store decision with Lucy, then stand up the store and Instagram Shopping. This is the critical-path revenue blocker.
2. **Build the ambassador / instructor seeding shortlist before the July delivery.** It's now the primary growth engine (per the devil's advocate revision) and needs lead time to seed before product lands.
3. **Close the materials question with Lucy (recycled / organic / hemp).** It's the last gate on whether any sustainability story can be told, and it's currently blocking copy.

---

## Weekly Review, 2026-05-31 (week of 2026-05-25)

### Highlights
- **Sportif went from concept to first real client with the intake email sent.** Built `clients/sportif/` from scratch (README, brand.md skeleton, customised questionnaire, customised SWOT), ran 9 WebSearch + 4 follow-up queries to populate 8 Opportunities and 10 Threats with 23 cited sources, locked Sportif as Australian, fired the intake email to Lucy with the "Lauren put me in touch about Sportif" subject line, and got a same-day "answers in ~5 days" confirmation. Expected return ~2026-06-03.
- **Stage 4 went from blocked to fully spec'd at the 2.0 generation.** Researched and wrote `docs/platform-prompt-formats.md` covering Seedance 2.0 (launched April 2026, unified audio-video, `@image/@video/@audio` reference syntax) AND GPT Image 2.0 / `gpt-image-2` (launched April 2026, near-pixel-perfect multilingual in-image text). Original sonar-pro pass had missed both 2.0 launches; deep-research caught them. Doc now carries platform specs, failure-mode tables, Sportif-shaped worked examples, and cited sources.
- **Built the post-Lucy trigger system as institutional infrastructure, not a one-off plan.** `clients/sportif/intake/post-lucy-research-plan.md` holds 12 steps + 5 ready-to-run Perplexity passes (~$7 AUD total) with exact bash commands. Saved auto-memory at `~/.claude/projects/.../memory/` for trigger phrases ("Lucy has responded" etc.) so any future Claude session in this workspace auto-loads and executes rather than improvising. First time the workspace built a "wait for external event, then auto-run" pattern.
- **Closed the self-improving prompt loop.** `experiments/` framework built and run live with the BAHE FLOWLOOPS experiment: 3 images + 3 videos generated through Seedance 2.0 and gpt-image-2, analyzed, and ~12 field-validated findings promoted back into `docs/platform-prompt-formats.md`. Notable: gpt-image-2 renders exact text reliably, Seedance human biomechanics are weak (use @video1 motion refs or real footage), Seedance auto-generates audio that can't be silenced via prompt.
- **Two major foundational docs landed.** `docs/marketing-fundamentals.md` (9,084 words, agency-wide knowledge base covering paid, organic, email, creators, metrics, campaign structure, Sportif-applied blueprint with AUD benchmarks) and `docs/platform-prompt-formats.md` (Stage 4 reference). Workspace now has real reference material, not just templates.

### Patterns I noticed
- **Mid-session pivots produced the best work three weeks running.** Session 004's pivot from "test the analyzer" to "design the full pipeline" → all the architecture. Session 005's pivot from "Meta restricts fitness category" to "Meta restricts claim-making language" → a manageable, controllable Sportif rule. Session 006's pivot from "deep-research is broken, move on" to "fix it now" → unblocked the entire post-Lucy plan within the same session. Lesson: when Hugo questions a framing or asks "is this right?", it's usually worth dropping the queue and following the thread.
- **Sonar-pro is fast and cheap, but deep-research catches what sonar-pro misses on currency.** Session 006 missed both Seedance 2.0 and GPT Image 2.0 on the sonar-pro pass and caught both on the deep-research pass. Worth the cost (and the polling wait) when "what shipped in the last 90 days" matters. Pattern: deep-research for synthesis + sources, follow-up sonar-pro for long-tail mechanics.
- **Em dashes keep leaking in despite the hard rule.** Caught in Session 005 across templated sections (link titles, table cells), caught again in Session 006 in the deep-research outputs and an asset. Mechanical sed sweeps fix the bulk but leave awkward fragments; manual grep after every multi-edit is genuinely necessary. Also caught en-dashes this week, added them to the sweep.
- **Security-critical mistakes happen when pasting into the wrong file.** Hugo pasted the real Perplexity API key into `.env.example` (tracked file) in Session 005. Caught pre-commit, key rotated. Two weeks before, no near-misses. As the workspace gets more API keys, the `.env.example` vs `.env` discipline matters more.
- **The two-Claude pattern (Cowork advisor + Opus writer) requires deliberate sync points.** Session 004 had a one-off advisor-builds exception, Session 005 noted the working pattern explicitly, Session 006 ends with a dedicated "For the Cowork advisor (sync)" paragraph. Both Claudes now share the auto-memory directory + the post-Lucy trigger system. Sync is institutional, not ad-hoc.

### Skills / knowledge gained
- **The Meta Restricted Health and Wellness bucket is triggered by claim-making language, NOT product category.** "Stylish wrist weights" stays outside the bucket; "wrist weights proven to boost cardio" goes inside. This single nuance reshapes the entire Sportif creative strategy from "fight a category restriction" to "control our copy."
- **Pilates is the dominant 2026 fitness cultural tailwind**, three years atop the ClassPass charts, 15M bookings, 66% YoY growth on reservations. Stronger than expected. A lead positional lever if Sportif's mix touches it.
- **Australian paid-media benchmarks are now documented:** Meta CPM ~$9.80 AUD (23% below US, 18% above UK), TikTok in AU ~30% cheaper than Meta with Health & Fitness as the cheapest vertical (~$6.50 AUD CPM), Sydney premium 20-50% in peaks, November $24.80 vs January $10.68 seasonality. Plan around Australian summer.
- **The Bala playbook is the proven template for design-led fitness accessories DTC**, multi-million brand built without paid marketing for years, design-as-jewelry, color/aesthetic-led, heavy UGC and influencer seeding. Sportif's reference template (not Gymshark or Alo).
- **Klaviyo is the clear default for ecom email**, 3.8x revenue per subscriber vs Mailchimp at $5K-contact scale, ecom automation included at $100/mo vs Mailchimp's $160/mo Premium tier.
- **Perplexity `sonar-deep-research` cannot run as a sync HTTP call**, long autonomous jobs get RemoteDisconnected by the gateway. Must use the async endpoint (`/async/chat/completions` + polling). Other models 400 there, so routing is automatic. `scripts/perplexity_search.py` now handles this transparently.
- **Stage 4 platform specs (current as of Session 006):**
  - **Seedance 2.0:** directorial prompt (Subject, Action, Environment, Camera, Style, Constraints), accepts text + up to 9 images + 3 video + 3 audio via `@image1/@video1/@audio1` syntax, 4-15s, 480p-1080p (+2K/4K upscale), strong physics, weak human biomechanics, unreliable audio (auto-generates regardless of prompt).
  - **gpt-image-2:** near-pixel-perfect multilingual in-image text (quote exactly, keep short), up to 4K, DOES NOT support transparent backgrounds (use gpt-image-1.5 or white-bg cutout), DO NOT set `input_fidelity` (errors), no API-level "thinking mode" param.
- **The self-improving prompt loop works as a methodology.** Closed-loop produce → generate → analyze → learn, with findings promoted back into reference docs. First worked example (BAHE FLOWLOOPS) shipped ~12 promoted findings in one session. This is now a workspace pattern, not a one-off.

### Open questions still unresolved

From Session 004 (carry-over, still open):
- [ ] `from __future__` annotations shim resilience for the video-analyzer skill on fresh clones (setup.sh re-clones from upstream and loses the fix).
- [ ] Python 3.10+ upgrade via Homebrew, would retire the shim need.
- [ ] OpenAI + HeyGen API keys (Session 001 carryover, HeyGen needed before any avatar work).
- [ ] Repo visibility decision for GitHub Pages (private requires Pro; public is free).

From Session 005 (still open):
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3, mode-aware brand-first vs competitor-first template).
- [ ] Build voice-memo-to-questionnaire transcription recipe at `recipes/transcribe-voice-memos.md` (Whisper already installed).
- [ ] Add image-analyzer skill (Stage 1 second path, static image competitor analysis).
- [ ] Wider em-dash sweep across `docs/pipeline-architecture.md`, top-level `README.md`, older starter prompts (`csv-to-chart.md`, `pdf-to-summary.md`), recipes, skills READMEs.
- [x] ~~Research Seedance + ChatGPT Image 2.0 current prompt formats~~ RESOLVED in Session 006 (`docs/platform-prompt-formats.md`, rewritten 2.0-first in second addendum).

Sportif-active (waiting on Lucy ~2026-06-03):
- [ ] Lucy returns questionnaire. Trigger phrase activates `clients/sportif/intake/post-lucy-research-plan.md`.
- [ ] Run the 5 Perplexity passes (~$7 AUD total).
- [ ] Populate `clients/sportif/brand.md` from responses + research.
- [ ] Draft Stage 3 synthesis brief at `clients/sportif/campaigns/launch-2026-09/synthesis-brief.md`.
- [ ] Update `docs/marketing-fundamentals.md` Part 8 budget bands with Sportif-specific AUD numbers.
- [ ] Send Lucy a "where we are" summary email after research is in.
- [ ] Hugo to send work-samples follow-up email (promised in intake P.S.).

From Session 006 (still open):
- [ ] Write Stage 4 adapters (`prompts/production-seadance.md`, `prompts/production-chatgpt-image.md`) now that the format spec exists. Pick first adapter from Lucy's Q12 timeline answer.
- [ ] Pick the standard Seedance reseller (fal.ai / Pollo / Wavespeed / Dreamina direct). Field names differ per host; adapter should target one.
- [ ] Confirm gpt-image-2 live parameter strings against the OpenAI API reference before writing the adapter parameter block.
- [ ] Stage 5 review-and-iterate workflow (design exists, no code yet; build when first synthesis brief gets reviewed).

### Suggested focus for next week

1. **Be ready for Lucy.** She's expected back ~2026-06-03 (mid next week). The post-Lucy trigger system is built and tested; the moment a trigger phrase fires, the 5 Perplexity passes ($7 AUD) and the brand.md population kick off automatically. Nothing else this week should block on starting that. Pre-stage: glance through `clients/sportif/intake/post-lucy-research-plan.md` and confirm nothing has drifted since it was written.
2. **Write `prompts/synthesis-creative-brief.md` (Stage 3) while waiting.** This is the bridge between Lucy's intake + Perplexity research and the Stage 4 production prompts. Template scaffold doesn't need Sportif specifics, it just needs the mode-aware (brand-first vs competitor-first) structure. Unblocks the rest of the pipeline for Sportif's launch content the moment her answers arrive. Estimated 1-2 hour focused task.
3. **Pick a Seedance reseller and write the first Stage 4 adapter.** Decision (fal.ai vs Pollo vs Wavespeed vs Dreamina direct) gates the adapter shape. Once chosen, the gpt-image-2 OR Seedance adapter (whichever Sportif's first content need points to from Lucy's Q12 answer) becomes the first end-to-end production prompt in the workspace. Pairs naturally with #2.

---

## Weekly Review, 2026-05-24 (week of 2026-05-18)

### Highlights
- **Workspace went from zero to fully scaffolded in a week.** Created `~/Desktop/hyperframes/`, upgraded Node to v22, cloned the three reference repos (official HyperFrames source, HeyGen launch video, Nate Herkai's 12-project student kit), spun up a starter project, and installed all 15 HyperFrames AI skills into `.agents/skills/`.
- **Got everything under version control and pushed to GitHub**, `OchoOcho88/ocho-frames` (private), first commit at 197 files / 2.7MB. Added a `setup.sh` so future clones can restore the ~940MB of `.gitignore`'d reference repos.
- **Built the organizational layer on top of the code**, added top-level `prompts/`, `recipes/`, and `skills/` folders with starter content, clear READMEs, and a documented distinction between project-scoped vs. workspace-scoped skills.
- **Set up automated institutional memory**, scheduled this weekly reflection task so the workspace gets reviewed every Sunday at 6pm without anyone having to remember to do it.

### Patterns I noticed
- **Local environment friction keeps showing up.** First the Node PATH fight (older Node winning over the new v22 install, needing a manual `~/.zshrc` override), then the sandboxed shell's inability to `git clone` directly into the Desktop mount. Tooling that touches macOS bridges/mounts needs a workaround mindset, not a "should just work" assumption.
- **API keys are the biggest unblocking dependency.** Three keys (OpenAI, HeyGen, soon Gemini) have been on the open-questions list across both sessions. Nothing real can be tested end-to-end until at least the first two are in place.
- **Conscious structure for AI-agent use.** Every choice this week, auto-loaded skills, bracketed prompt placeholders that force specificity, prompts vs. recipes vs. memory separation, was made with the assumption that an AI agent (not just a human) would be reading and using these files.

### Skills / knowledge gained
- HyperFrames is "video as code": HTML/CSS/JS rendered to MP4, deterministic, Apache 2.0 (no per-render fees, no seat caps), and frame-accurate seekable for libraries like GSAP, clear win over Remotion for AI-driven video work.
- The 15-skill HyperFrames ecosystem covers main + CLI + media preprocessing (Kokoro TTS, Whisper, u2net) + animation runtimes (GSAP, Anime.js, CSS, Lottie, Three.js, WAAPI) + conversion helpers.
- The catalog has 50+ pre-built blocks via `npx hyperframes add <block>`, checking the catalog first is faster than building from scratch.
- Skill scoping has two distinct modes: project-scoped (`<project>/.agents/skills/`, auto-loaded) vs. workspace-scoped (`skills/`, manually referenced).
- GitHub Pages is free only on public repos, keeping `ocho-frames` private + using Pages requires GitHub Pro ($4/mo) or flipping the repo to public when sharing.
- Sandbox workaround for git: clone to `/tmp` first, then `cp -R` to Desktop mounts.

### Open questions still unresolved
From Session 001:
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`)
- [ ] Get OpenAI API key and add to `.env`
- [ ] Get HeyGen API key and add to `.env`
- [ ] Customize `brand/agency-brand-kit.md` with Hugo's actual colors, fonts, and voice
- [ ] Pick the first real project to build (animated chart from a CSV, or a 15-second product intro)
- [ ] Decide on a naming convention for projects in `my-projects/` (e.g., `YYYY-MM-DD-project-name`?)

From Session 002:
- [ ] Install Hugo's incoming video-analyzer skill into `skills/` and document it
- [ ] First competitor analysis as a real test of the prompt + skill combo
- [ ] Get Gemini API key once we install the video-analyzer skill
- [ ] Decide repo visibility for Pages (public flip vs. GitHub Pro)
- [ ] Enable Pages in repo Settings → Pages once the visibility decision is made

### Suggested focus for next week
1. **Unblock the workspace by collecting API keys.** OpenAI and HeyGen first, those two alone unlock the ability to actually test the starter project end-to-end. Until that happens, every other build task is theoretical.
2. **Install the video-analyzer skill and run the first real competitor analysis.** This is the proof that the prompt + skill + recipe framework delivers value, not just structure. It also feeds back into what HyperFrames work to prioritize.
3. **Customize the brand kit before producing any real videos.** Modern defaults are fine as a placeholder, but anything shipped this week with the default kit will need redoing later.

---

## Session NNN, YYYY-MM-DD, One-line summary
### What we did
### What we learned
### Decisions
### Open questions / next steps
-->
