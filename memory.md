# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## CURRENT STATE (update this block every session, keep it to ~12 lines)

*Last updated: 2026-07-21 | Last session: 021 (Claude Code, in progress) | Working tree: committed clean | Git: in sync with GitHub | Next: standalone waitlist capture page (does not need Lucy or trademark), then ambassador/instructor seeding shortlist*

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

## Session 019 (2026-07-18, Cowork cloud): Cosmos reference edit, first gpt-image-2 edits-endpoint production piece

Hugo supplied a reference editorial image (`assets/Cosmos pictures/cosmos_sportif logo.jpeg`, backbend pose, chocolate brown outfit, big cream FORM wordmark) and asked for two changes: outfit recoloured baby blue, and FORM replaced with the SPORTIF wordmark in the real brand font.

### What we did
- **First production use of the gpt-image-2 `images/edits` endpoint** (everything before was text-to-image generation). Validated at quality low, final at quality high, 1024x1280. No mask needed; a "two changes only" prompt held the pose, film grain and backdrop.
- **Proven overlay pattern applied:** text-free edit first, then the real Sportif logo lockup stamped via the NEW `scripts/overlay_logo.py` (Glacial Indifference REGULAR, tracking -0.059 em, short underline rule, geometry measured from `assets/05-logo-sportif-white-on-peach.png`), cream #F4F2EA sampled from the original FORM letters, block centred at 49 percent height. Main at 76 percent width (FORM's footprint) plus a 62 percent narrow variant. First pass wrongly stamped a hand-styled Bold wide-tracked wordmark with no rule; Hugo caught it and the logo was corrected in the same session. Rule going forward: stamp the lockup with `overlay_logo.py`, keep `overlay_wordmark.py` for plain headline text only.
- **Keepers saved** to `clients/sportif/generated/images/`: `cosmos-babyblue-notext.png` (reusable base), `cosmos-babyblue-wordmark.png`, `cosmos-babyblue-wordmark-narrow.png`. Full prompt and settings logged in `image-prompts.md`.

### What we learned
- **Output-stage moderation false-positived [sexual] at quality high** on the backbend pose (low passed the same prompt). Appending "tasteful, professional athletic fitness editorial photograph... modest full-coverage sportswear" cleared it. Keep that sentence for any bodysuit or backbend imagery.
- **This Cowork session ran in the CLOUD sandbox** (Anthropic container + device bridge to the Mac), a third environment flavour: shell calls are NOT capped at 45s (the ~70s high-quality render ran fine in one call), but files only reach the Mac via an explicit commit step, and the mounted folder reads live via the bridge. Recognise it by `/mnt/user-data/uploads/` paths plus `device_*` tools.

### Decisions
- Baby blue is OFF the Sportif palette; Hugo confirmed it is an intentional concept exploration, not a new brand colour.

### Open questions
- The Tuesday 2026-07-14 Lucy meeting outcomes (launch slip reason, new date, waitlist page approval, incentive pick) are still not logged anywhere. Capture them next session; most of the open backlog hangs off them.

## Session 018 (2026-07-11, Cowork): Content strategy x funnel method alignment audit, Tuesday agenda prep

Same day as Session 017. Hugo confirmed the Friday IG launch did not happen and he meets Lucy Tuesday (2026-07-14). He asked whether the content creation strategy (synthesis brief, three angles) matches the funnel method, and to bake the funnel structure into content creation.

### What we did
- **Audited `campaigns/launch-2026-09/synthesis-brief.md` against `docs/funnel-playbook.md`.** Verdict: about 70 percent aligned in spirit (Angle C = the story funnel, pouch + 500 units = the offer, seeding = social proof, email from day one) but the funnel spine was missing from the content layer.
- **Five gaps found:** (1) content has no capture destination (no waitlist page exists, Shopify blocked), (2) no one-CTA-per-post discipline, (3) no FAQ content lane, (4) metrics track saves/follows but not signups per post or cost per lead, (5) no explicit 1-to-2-second hook rule.
- **Baked the fix into `clients/sportif/funnel-plan.md` section 7:** a content x funnel mapping table (four stages, each with content job, format, ONE next action, money metric) plus the five fixes. Cross-linked from the synthesis brief (new "Funnel integration" section). Next actions now carry the Tuesday agenda.

### What we learned / key insight
- **The waitlist capture page does not need Shopify.** A standalone landing page (Klaviyo or similar) can go live this week, which un-deadends every post and partially bypasses the Lucy/Shopify blocker. This reframes the critical path.

### Decisions
- Content and funnel are now formally bound: every post is a funnel stage with exactly one next action; an angle that wins saves but captures no emails is treated as failing.
- FAQ lane added as the fourth content format alongside Angles A/B/C.

### Open questions / next
- [ ] Tuesday 2026-07-14 Lucy meeting: launch slip reason + new date, standalone waitlist page approval, Lucy-session adaptation A/B/C, Shopify blockers.
- [ ] Build the standalone waitlist capture page once approved.
- [ ] Write the 3-email welcome flow (carried from 017).
- [ ] Carried: Lucy feedback backlog, ambassador shortlist, trademark, materials, PDF generators on Poppins.

## Session 017 (2026-07-11, Cowork): Funnel playbook + Sportif funnel plan from the Australian Marketing Summit notes

Hugo attended the Australian Marketing Summit 2026 (2026-07-10, presented by Ethan Donati and Jane Lu) and brought back scrambled notes on funnel building. We turned them into a permanent funnel layer for the workspace.

### What we did
- **Organised the raw notes** into `docs/summit-notes-2026-07-10-raw.md` (verbatim, provenance) and a clean reusable playbook at `docs/funnel-playbook.md`: what a funnel is (one page, one choice, ads to funnels never websites), the 4 page elements, the "How to [outcome] without [objection]" headline formula, offer requirements (incentive, honest scarcity, special offer, outcome+objection testimonials), the 11-step ad-to-scale journey, neuromarketing techniques (emotional buying, affinity buying, green-light questions), channel roles, and a new-funnel checklist.
- **Cross-checked against 2026 research** (WebSearch): landing page conversion by source (paid social 1 to 3 percent, dedicated pages 2.5 to 4), founder presence lifts conversion 15 to 28 percent, welcome flows ~$2.65 RPR and abandoned cart ~$3.65 RPR with email at 1hr + SMS at 24hr, Meta instant forms 30 to 50 percent cheaper per lead but lower intent than landing pages, $30 to 50/day minimum test spend. Donati's book confirmed as "The Neuroscience Behind 7 Figure Funnels".
- **Wrote the Sportif application** at `clients/sportif/funnel-plan.md`: the health-claim headline formula translated to aesthetic/lifestyle outcomes (guardrail-safe candidates drafted); 3 funnels (waitlist funnel = the Shopify coming-soon page upgraded, launch funnel with the pouch gift as the built-in incentive and 500 units / 35-day restock as honest scarcity, educational FAQ funnel = one Reel per question); Klaviyo flow spine (welcome, launch, abandoned cart, post-purchase); budget aligned to the Lean band.

### Decisions
- Two-layer placement (Hugo's pick): reusable playbook in docs/, application in clients/sportif/. Internal only, no Lucy PDF yet.
- Explicitly rejected from the summit material: outcome claims, hype urgency, quiz funnels at launch, ChatGPT ads.
- The "band sale = half hour with Lucy" idea flagged as unscalable at 500 units (250 hours); three adaptations proposed (A: monthly group session, recommended; B: capped top-tier 1:1; C: evergreen ritual video series). Decision pending.

### Open questions / next
- [x] ~~Did the Friday 2026-07-10 IG launch happen? Confirm with Hugo what got posted.~~ RESOLVED Session 018: launch did not happen; reason to be captured at the Tuesday 2026-07-14 Lucy meeting.
- [ ] Fold Funnel 1 (waitlist) spec into the Shopify coming-soon build when unblocked.
- [ ] Lucy-session adaptation decision (A/B/C) on the next Lucy agenda.
- [ ] Write the 3-email welcome flow so it is ready when the waitlist page ships.
- [ ] Carried: Lucy feedback (taglines, colourways, hero pick, blocker email), Shopify, ambassador shortlist, trademark, materials, PDF generators still on Poppins, optional true-high background re-render.

## Session 016 (2026-07-08, Claude Code): Friday launch handoff, teaser Reel rendered (backgrounds at medium, true-high blocked by a 60s network cap)

Ran the Friday launch handoff jobs from Session 015. The teaser Reel is rendered and launch-ready. The one deviation: the action backgrounds are medium quality, not high, because of a network limit in the Claude Code environment (details below), with a clean upgrade path documented.

### What we did
- **Pushed the three Session 015 commits to GitHub** (`7ec00fb..7a650d1`). Local and origin/main in sync.
- **Made both scripts-local scripts path-portable.** `gen_action_bg.py` and `overlay_action_tiles.py` hardcoded the Cowork sandbox paths, so they could not run on the Mac. Both now derive the workspace root from their own file location (`Path(__file__).resolve().parents[3]`), so they work in BOTH environments. Added a `quality` argument to `gen_action_bg.py` (default low, pass high) plus a streaming path for slow renders.
- **Re-rendered the three action backgrounds** (training glute bridge, fashion still life, ritual morning scene) at medium quality, keeping the `bg-action-<variant>-low.png` filenames (per the handoff instruction) so downstream references did not move. Visually verified all three: correct flat band form (no coil/pastry), correct bridge anatomy, warm palette, clean upper-third negative space.
- **Rebuilt the tagline tiles** with `overlay_action_tiles.py` (sportif-tagline-1/2/3-action.png + preview). Verified the taglines overlay legibly.
- **Copied the three backgrounds into `compositions/sportif-teaser/images/`** (byte-verified identical to source).
- **Ran `npm run check` on the composition.** Lint 0/0, validate no console errors. Inspect flagged 6 `container_overflow` warnings on the three scene images (the intentional Ken Burns zoom/pan overflow, which `.photo-wrap` already clips with `overflow:hidden`). Fixed by adding `data-layout-allow-overflow` to the three scene `<img>` tags. Re-check fully clean: 0 layout issues.
- **Rendered the Reel:** `compositions/sportif-teaser/renders/sportif-teaser_2026-07-08_12-56-55.mp4`, 1080x1920, 13.0s, h264, 7.3 MB. Confirmed a sampled frame looks correct and on-brand.

### What we learned
- **The Claude Code environment drops HTTPS responses after ~60s of idle (no bytes).** High-quality gpt-image-2 at 1088x1440 takes longer than that, so the synchronous request dies with `RemoteDisconnected` at exactly 60s. This is the same class of limit as the Perplexity deep-research issue. Disabling the Bash sandbox did NOT help (the cap is outside that toggle).
- **Streaming does not rescue it.** Instrumenting the SSE stream showed gpt-image-2 sends ONE early partial (~16s) then computes silently and batches the rest at the end, so there is a >60s gap before the completed event and the connection is killed. `partial_images:3` did not add mid-render keepalives.
- **The proper workaround (background submit + poll) is blocked by org verification.** The Responses API background mode needs a verified org for the driver model (`gpt-4.1-mini` returned HTTP 403 "organization must be verified"). So it is unavailable until Hugo verifies the org.
- **Medium quality (~50s) completes under the 60s cap** and is a clear step up from the low drafts. For background imagery behind taglines with Ken Burns motion, the quality difference is minor.
- **HyperFrames `inspect` (Chrome, Claude-Code-only) catches Ken Burns overflow.** Declare intentional zoom/pan overflow with `data-layout-allow-overflow` on the animated element; the clip container keeps it visually contained.

### Decisions
- **Rendered medium, not high, this session.** The Friday deadline plus a launch-ready Reel outweighed blocking on true-high. Flagged to Hugo with the upgrade path. Kept the `-low` filenames per the handoff instruction.
- **Two upgrade paths to TRUE high**, whenever wanted: (1) run `gen_action_bg.py <variant> high` in a NATIVE Mac terminal (Terminal.app, outside Claude Code) where there is no 60s cap, the script is now portable and has a streaming high path, then re-run overlay + copy + composition render; or (2) verify the OpenAI org and use background mode.
- Path-portable scripts are the standard now (root from `__file__`), so scripts-local tools run in both environments.

### Follow-up (same day, continued): end-card revision, brand colours, CTA variant

Reworked the teaser end card (scene 5) live via `npm run dev` (studio at localhost:3002).
- **Holds longer.** Composition duration 13 to 15s, s5 duration 2.2 to 4.2s. Re-timed the entrance tweens to assemble by ~11.7s so the fully readable card holds about 3s before a gentle fade at 14.8s.
- **Brand colours (matches scene 1 identity).** End card background is now blush peach #F0CDB3, SPORTIF wordmark and underline warm white #FFFBF8, "Launching September 2026" warm charcoal #4A433C, handle terracotta #833827 for contrast. `hyperframes validate` passes (it checks runtime/console, not WCAG; manually confirmed the terracotta handle is about 5.5:1 on peach, and the warm-white wordmark intentionally matches scene 1).
- **CTA variant via a composition variable.** Declared `data-composition-variables='{"cta": false}'` on root, read with `window.__hyperframes.getVariables()`. When `cta` is true, a "Follow for the launch" line (warm charcoal, calm, its own entrance tween) appears under the handle. Hidden by default so the standard cut is unchanged.
- **Rendered both** (check clean 0/0/0 first): standard `renders/sportif-teaser_2026-07-08_13-24-41.mp4` and `npx hyperframes render --variables '{"cta":true}' --output renders/sportif-teaser-cta.mp4`. Both 15.0s, verified by frame grab. No dashes, no hype in the on-screen copy.
- Learned: HyperFrames composition variables are declared on root via `data-composition-variables` (JSON defaults), read in-composition via `window.__hyperframes.getVariables()`, and overridden at render with `--variables` (or `--variables-file`), with `--strict-variables` to enforce types.
- **Fixed a bottom-edge glitch.** Hugo spotted a thin cream line along the bottom during scene 3 (about 6 to 7s), roughly 86px, most visible where the linen background is pale. Diagnosed by frame-sampling: the source images have no cream edge, so it was a coverage gap. During a scene the Ken Burns zoom/pan can expose the frame edge, and behind that scene the page background (was cream) showed through. Fix: over-cover the scene images (`position:absolute; top/left -6%; width/height 112%`) so no transform state can reach an edge, and set the page background to the on-brand peach #F0CDB3 as a safety net. Re-rendered both variants; frame-sampling confirms 0px band across scenes 3 and 4. Lesson for HyperFrames Ken Burns: always over-cover the image past the frame, and make the page/root background a safe on-brand colour, never leave a bright default showing.

### Open questions / next
- [ ] Optional: re-render the 3 backgrounds at TRUE high via a native terminal (or after org verification), then rebuild tiles, re-copy, re-render the Reel. Not required for Friday.
- [ ] Lucy feedback still pending: four tagline-row directions, three banner colourways, hero-concept pick (v5/v6/v7), blocker email reply.
- [ ] Friday posting plan: banner row, tagline row, teaser Reel as the first Reel.
- [ ] Carried: blocker email send, Shopify coming-soon, ambassador shortlist, trademark, materials, Stage 3/4 templates, PDF generators still on Poppins, optional teaser voiceover.

## Session 015 (2026-07-08, Cowork): SPORTIF 3-tile Instagram grid banner, posting recipe proven on a mock account

Lucy asked Hugo for a bottom-row grid banner like the old LE SPORT COLLECTIF mockup (the LSC mockup is a layout reference only, LSC remains dead as a name). Hugo also wanted to learn the Photoshop build himself.

### What we did
- **Built the 3-tile SPORTIF grid banner** with a parametrised Pillow script at `clients/sportif/scripts-local/build_grid_banner.py`. One 3240x1440 canvas, real Glacial Indifference Regular, letter-spaced (0.28 em tracking) with the short underline, split into three 1080x1440 tiles (3:4, the current grid ratio). Filenames carry post order (tile 1 = rightmost, posted first).
- **Three colourways generated** in `clients/sportif/generated/images/grid-banner/`: cream bg + blush wordmark (default), white bg + blush (`-white`), blush bg + white (`-peach`). The peach one matches the existing @sportifcollection identity (wordmark on blush peach), recommended first pick for Lucy.
- **Gave Hugo a point-form Photoshop 2026 walkthrough** (canvas, guide layout, tracking ~280 in the Character panel, slice and export, posting order) so he can rebuild it by hand.
- **Tested live on Hugo's mock IG account and debugged a real failure:** first post came out as "SP POR IF" with letters eaten at tile edges.

### What we learned
- **Instagram's photo picker defaults to a 1:1 crop.** That square then gets side-cropped by the 3:4 grid thumbnail, which eats any letter near a tile edge. The fix is tapping **Original** on the crop screen (or the expand arrows on mobile); with 1080x1440 (3:4) source tiles the post ratio then equals the grid ratio and nothing is cropped. Verified working, the mock grid reads SPORTIF cleanly.
- **Instagram added manual grid reordering (June 2026):** long-press a post, Reorder grid, drag. Posting order for banners no longer needs to be perfect, it can be fixed after the fact. (Web-verified: Fast Company, Social Media Today, 9to5Mac.)
- Pillow has no native letter tracking; draw glyph by glyph with a per-glyph advance (bbox width + tracking) as done in the script.

### Decisions
- Banner tiles are 1080x1440 (3:4) as the standard for grid-spanning art, not 1080x1350 (4:5), because the grid thumbnail is 3:4.
- Peach background variant is the lead option to show Lucy (matches the confirmed wordmark-on-blush identity).

### Follow-up (same day, continued): tagline row (4 directions), action imagery, teaser Reel composition

Hugo revealed the timeline: **the Sportif Instagram launches THIS FRIDAY (2026-07-10).**

- **Tagline row built** (row above the banner): "Everyday training, elevated." / "Too fashionable not to WEAR!" (Lucy's line, centre) / "For your morning ritual." All from the approved say-list. Four directions produced in `generated/images/grid-banner/`: flat terracotta, terracotta gradient + text shadow (v2), AI linen texture, AI plaster texture, and the lead: **action imagery** (pilates bridge with band under tension, fashion still life with pouch and gold jewellery, morning ritual vignette), taglines overlaid in reserved negative space.
- **Two prompt-engineering fixes worth reusing** (also logged for image-prompts.md): (1) exercise poses come out anatomically wrong unless described joint by joint (head/shoulders/arms flat, knees bent, hips lifted); (2) the band form needs "wide flat continuous closed loop, like an oversized fabric headband, not folded, not twisted, not a coiled tube" or it melts into ribbons/pastry shapes.
- **All versions sent to Lucy for feedback.** Hugo has creative control; awaiting her reaction.
- **Teaser Reel composition built in HyperFrames** at `compositions/sportif-teaser/` (first real HyperFrames project in the workspace). 13s, 1080x1920: wordmark letter-by-letter reveal on blush, three action-image scenes with taglines and Ken Burns, cream end card "Launching September 2026" + @sportifcollection. Glacial Indifference converted to woff2 in `fonts/` (fonttools). design.md captures the brand for video. Lint passes 0/0.
- **Cowork limit learned:** hyperframes validate/inspect/preview/render need headless Chrome, unavailable on the ARM sandbox. Division of labour: author + lint in Cowork, validate + render in Claude Code.

### Open questions / next
- [ ] Lucy feedback on the four tagline-row directions (and the three banner colourways).
- [ ] CLAUDE CODE (tonight, before Friday): re-render the 3 action backgrounds at quality high (prompts in `gen_action_bg.py`), rebuild tiles via `overlay_action_tiles.py`, swap the images in `compositions/sportif-teaser/images/`, then `npm run check` and render the Reel.
- [ ] Optional teaser voiceover (TTS via hyperframes-media) - Hugo has not decided.
- [ ] Decide Friday grid posting plan: banner row first, tagline row second, teaser Reel as first Reel.
- [ ] Show Lucy the three colourways, get her pick before anything goes on the real @sportifcollection grid.
- [ ] Carried: Lucy hero-concept pick (v5/v6/v7), blocker email send, Shopify, ambassador shortlist, trademark, materials, PDF generators still on Poppins.

## Session 014 (2026-07-07, Claude Code): GitHub sync (pushed the Session 013 backlog)

Short startup-and-sync session on the Mac, right after Cowork closed out Session 013 the same day.

### What we did
- Ran the session-start sync protocol: read the CURRENT STATE block and the Session 013 entry plus its follow-up, confirmed the Session 013 close-out commits in the log, and verified a clean working tree.
- **Pushed the local backlog to GitHub** (`535032c..49aa5de`, 10 commits). Cowork had committed Sessions 007 to 013 locally but could not push from the sandbox; that is why the tree was ahead. Local and origin/main are now in sync.
- Reviewed current state with Hugo and confirmed both Lucy-dependent items are still pending.

### What we learned
- The push backlog is the expected shape of the two-environment split: Cowork commits but does not push from the sandbox, so Claude Code on the Mac is where the sync to GitHub happens. Worth doing at the start of every Claude Code session.

### Decisions
- No content work this session. Both live jobs (render Lucy's hero pick at quality high, start the Shopify coming-soon page) are blocked until Lucy responds, so we synced and closed out rather than starting unblocked busywork.

### Open questions / next
- [ ] Lucy has NOT picked a hero concept yet (v5 unboxed / v6 set / v7 flat) and has NOT replied to the blocker email. Both are the gates.
- [ ] When Lucy picks: render the chosen 4:5 hero at quality high in Claude Code (text-free, then overlay the wordmark with `scripts/overlay_wordmark.py`).
- [ ] When Lucy replies to the blocker email: start the Shopify coming-soon page step-by-step (research done).
- [ ] Unblocked and available anytime: build the ambassador/instructor seeding shortlist (main growth engine, not started).
- [ ] Carried: trademark clearance, materials question, Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins.

## Session 013 (2026-07-07): Workspace review and cleanup, git caught up, Lucy blocker email drafted

Hugo asked for a full project review (improvements, holes, integration opportunities), then approved working through every fix.

### What we did
- **Full workspace review.** Strongest parts: the two-doc client-cut methodology, devil's advocate passes, memory log, reusable generators. Biggest holes: the critical-path revenue blocker (band due July, no store), 5 weeks of uncommitted git work, superseded PDFs still live, stale CLAUDE.md, doc-drift risk, workspace clutter.
- **Archived 9 superseded Lucy-facing PDFs** into `clients/sportif/_archive/superseded-pdfs-2026-07/`. Client root now holds exactly three: Brand-Value-Plan (strategy), Launch-Plan (operations), Brand-Kit (reference). Lucy's questionnaire moved to `intake/`, the product board PDF into `competitor-analyses/`.
- **Git caught up.** Removed a stale `.git/index.lock` (needed the `allow_cowork_file_delete` tool first, plain rm fails on the mount). Updated `.gitignore` (product-images, logs/, .git-broken/, *.log). Committed Sessions 007 to 012 (62 files) plus this session's changes.
- **Fixed CLAUDE.md.** Replaced the wrong nohup research workflow with the `pplx_async.py` pattern, and added the learned gotchas: weasyprint per-sandbox install, Lora/Poppins fonts, PNG montage for PDF previews, outputs dir is throwaway, file deletion tool, the two-PDF client set, and the two-doc drift rule.
- **Added a CURRENT STATE block** to the top of memory.md (12-line snapshot a cold session reads first). Convention: update it every session.
- **Added drift guardrails.** Source-of-truth + last-synced headers in `brand-value-plan-client.md` and `launch-plan-client.md` (verified the generators only render the last blockquote group, so headers stay out of the PDFs).
- **Drafted the bundled Lucy blocker email** (`email-to-lucy-blockers.md`, supersedes `email-to-lucy-next-steps.md`) and created a Gmail draft to lucy@lucywayne.com.au. Four asks: open Shopify + staff access, lock prices + $70 threshold, pick fabric, decide who answers customers. Hugo must attach the two PDFs manually (draft tool cannot attach) and send.
- **Created `clients/sportif/voice-guidelines.md`**, a per-piece checklist distilled from brand.md (voice in one line, say/never-say, imagery rules, the no-dash rule).
- **Set up a scheduled task** `sportif-blocker-check` (Mondays 9am): reads CURRENT STATE, reports what is blocked on Lucy and for how long, what Hugo can do without her, one recommended action.

### Decisions
- Archive, not delete, the superseded PDFs (reversible).
- Competitor product-images (54MB) stay out of git; they live locally only.
- Old June 18 email superseded: it referenced five now-archived attachments.

### Integration opportunities flagged (need Hugo to authorize connectors in settings)
- **Klaviyo MCP:** build the welcome flow, coming-soon capture, back-in-stock waitlist directly once Shopify is open.
- **Canva:** re-auth for coming-soon page and social templates.
- **Airtable:** ambassador/instructor seeding tracker when outreach starts.

### Open questions / next
- [ ] Hugo: attach the two PDFs to the Gmail draft and SEND the Lucy blocker email. Highest-leverage action in the workspace.
- [ ] Confirm whether the 500 bands have landed; if yes, get the unboxing filmed.
- [ ] Build the ambassador/instructor seeding shortlist (not started, main growth engine).
- [ ] Write the Shopify coming-soon step-by-step (research done, waiting on the account).
- [ ] Carried: trademark clearance, materials, Stage 3/4 pipeline templates and adapters, Stage 4 launch imagery, memory.md archive split if it keeps growing.

### Follow-up (same day, continued): sync protocol, memory split, image pipeline live

- **Two-environment sync protocol written into CLAUDE.md** (Claude Code + Cowork on the same folder): read CURRENT STATE + git log at session start, close-out ritual at session end, continuous session numbers, builder/sounding-board rule when both are open. Added `.claude/commands/close-out.md` so Claude Code closes out with one command. Trigger phrases for mid-chat capture: "log this for Claude Code" / "close out the session".
- **Memory architecture finished.** Built `scripts/archive_memory.py` (moves oldest session entries to `memory-archive.md` when memory.md crosses 90KB, keeps newest 6 sessions + all weekly reviews; no-op below threshold; runs at every close-out). First split done: 141KB to 69KB, Sessions 001 to 007 archived.
- **OpenAI API key wired into .env** (was pasted on a commented line, fixed) and gpt-image-2 confirmed working after Hugo loaded credit. **The 45s Cowork shell cap only fits quality low; medium/high time out. Division of labour: iterate low in Cowork, render finals in Claude Code.**
- **First Sportif images generated** (coming-soon hero concepts): v1 to v4 at 3:2, then recomposed v5 to v7 at 4:5 portrait for Instagram (1088x1360). Sizing rule logged: 4:5 feed, 9:16 stories, 3:2 web. Hugo is texting Lucy the three 4:5 options to pick a direction. Known model quirks logged in image-prompts.md: band drifts to basket-coil (name the form explicitly), labels drift to leather (forbid it), casting/props drift across runs.
- **Generated-media structure created:** `clients/<client>/generated/images|videos/` (binaries gitignored), prompts logged in the client's `image-prompts.md` (the prompt is the source of truth). Template added to `clients/_template/`. Convention in CLAUDE.md.
- **Glacial Indifference (real Sportif font, 3 weights, OFL) now at `brand/fonts/glacial-indifference/`** and loads by path in BOTH environments. **Production pattern established: generate images text-free, overlay the real wordmark with `scripts/overlay_wordmark.py`** (defaults to Sportif). AI-rendered text is for internal comps only. The two PDF generators still use Poppins; switch on next edit.
- **Connector reality check:** Klaviyo account does not exist yet (create after Shopify opens, then authorize the connector), Canva not needed (gpt-image-2 + generators cover it), Airtable deferred until ambassador outreach starts.
- New open items: [ ] Lucy's hero pick, then high-quality final in Claude Code. [ ] Hugo to `git push` from the Mac (local is ~10 commits ahead of GitHub). [ ] Consider adding `git push` to the close-out ritual once he confirms credentials work.

---

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

## Session 012 (2026-07-01): Brand Value Plan redesign, new cover, full PDF rebuild, dev notes stripped

Hugo resumed to work the Brand Value Plan. He had reviewed the exported PDF and meant to bring content changes, but had lost his notes, so we started from the cover, which he flagged as too generic (default font, flat peach, templatey).

### What we did
- **Redesigned the cover.** Built three concepts in HTML rendered with weasyprint (editorial photo-top, magazine split, framed type-only). Hugo chose **B, the magazine split**: the FLOW band photo full-height on the right, a Lora serif "Brand Value Plan" title on the left, letter-spaced Poppins SPORTIF wordmark, brand palette, footer. First render exposed that the FLOW reference image has old experiment text ("FLOW / move with ease") baked in, so we crop the top ~268px off before use.
- **Rebuilt the whole PDF, not just the cover.** The old `Sportif-Brand-Value-Plan.pdf` (dated 2026-06-17) predated the 06-18 strategy update, so its body was stale (still "validate the pattern", three calls open). Regenerated the entire document from the current `brand-value-plan.md` in a new editorial card style (numbered lever cards, italic idea line, DO NOW callout boxes, closing sections).
- **Added a customer-facing cleaning pass.** The generator strips internal dev notes and dates for Lucy's copy (the "2026-06-18" dates, "Session 011", "Hugo confirmed", the Lever 1 "Note:" hedge sentence) while the source `brand-value-plan.md` keeps its provenance intact. Trade-off flagged to Hugo: clean at export time, do not gut the source of truth. Verified via pdftotext that no internal markers survive.
- **Saved and de-cluttered.** Final `Sportif-Brand-Value-Plan.pdf` written into `clients/sportif/`, overwriting the stale one (same filename, so only one version). Saved a reusable, location-independent generator `clients/sportif/build-brand-value-plan.py` (paths derived from `__file__`), so a future re-export is one command: `python3 build-brand-value-plan.py`.

### What we learned / gotchas
- **Sandbox rebooted mid-session and switched VM session id**, which wiped the pip-installed weasyprint and all working files in the outputs dir, and changed the host outputs path. Re-pinned the host outputs path with a probe file. Lesson: keep deliverables in the mounted `hyperframes` folder (stable host path), treat the outputs dir as throwaway, and expect to reinstall weasyprint per fresh sandbox.
- **Fonts:** only Lora (serif) and Poppins (geometric sans) are installed in the sandbox. No Glacial Indifference, so Poppins letter-spaced stands in for the wordmark and Lora carries the titles. Good enough and looks intentional.
- **Deleting files in the mount** now works via the `allow_cowork_file_delete` tool (used it to remove a stray `_wtest`), rather than being impossible.
- **present_files with a PDF did not show a preview for Hugo**; a combined PNG montage of the pages is the reliable way to let him see multi-page output in chat.

### Restructure after Hugo's screenshot review (same session)
- Hugo reviewed the refreshed PDF and asked for a real client cut: make "the idea in one line" actually one line, tighten every lever hard, use bullet points, move **Lucy to lever 1**, fix ambiguous titles, and stop showing the internal "DO NOW" boxes to Lucy.
- Two decisions he made: (1) reframe the action boxes as **"What we'll implement"** and keep them in the PDF (forward-looking, client-appropriate), and (2) **keep two docs**: `brand-value-plan.md` stays the detailed internal source, and a new condensed `brand-value-plan-client.md` drives the PDF.
- Built `clients/sportif/brand-value-plan-client.md` (Lucy #1, tight bullets, clearer titles, one-line intro, "What we'll implement" bullets) and repointed the generator at it. Dropped "Three calls this plan depends on" from the client cut (internal, resolved). Softened jargon: removed "devil's advocate review", "from the brief", "White Fox register", and "ACCC exposure". Result: **5 pages, down from 7**, saved over the client PDF.
- Generator note: `build-brand-value-plan.py` now reads the client md, renders bullet lists and a relabelled implement box. Two markdown files can drift, so if the internal plan changes, remember to reflect it in the client cut too.
- Hugo then asked to tie the plan to the Shopify build. Added a section, **"The Sportif store, where it all comes together"**, that connects the levers to the concrete store (one hub at sportifcollection.com.au, product pages carrying Lucy's story, Klaviyo email capture including the pre-launch coming-soon page, one store with Shopify Markets for AU/US, founding drop plus back-in-stock waitlist). Grounded in `shopify-setup-info-from-lucy.md` and `digital-ecosystem-action-plan.md`, not invented. Generator updated so sections (not just levers) can carry an italic lead line. Still 5 pages.

### Consolidated four overlapping plans into two (same session)
- Hugo flagged that four Lucy-facing PDFs (Brand Value Plan, Action Plan, Digital Plan for Lucy, Socials-to-Shop) overlapped and were confusing. Nothing sent to Lucy yet. Analysed them: three real topics spread across four files (WHY = Brand Value Plan; HOW IT CONNECTS = Digital Plan + Socials-to-Shop, duplicates; WHAT NEXT = Action Plan + repeated in the Digital phases and BVP "where to start").
- His two decisions: **two docs, strategy and operations, split apart**, both **Lucy-facing and polished** (owner tags and working notes stay out).
- Result, four client PDFs become two:
  - **Sportif-Brand-Value-Plan.pdf (strategy):** slimmed to idea + six levers + "What winning looks like." Removed the store section and the 90-day list (moved to the Launch Plan). Source: `brand-value-plan-client.md`.
  - **Sportif-Launch-Plan.pdf (operations):** "How it all connects" (a new single SVG hub-and-funnel diagram replacing the Digital Plan and Socials-to-Shop), "The Shopify store," "The plan, phase by phase" (Now / Build / Lead-up / Launch / After, absorbing the Action Plan), and "What we need from you." Source: `launch-plan-client.md`, generator `build-launch-plan.py`.
- The detailed internal working docs stay as the source of truth and were not gutted: `brand-value-plan.md`, `digital-ecosystem-action-plan.md` (owners, budget, content ideas, sources), `action-plan-checklist.md`.
- **Superseded client PDFs to remove/archive** (pending Hugo's ok): `Sportif-Action-Plan.pdf`, `Sportif-Digital-Plan-for-Lucy.pdf`, `Sportif-Socials-to-Shop.pdf`. File deletion is enabled for the hyperframes folder.

### Open questions / next
- Decide whether to archive or delete the three superseded client PDFs above.
- Hugo may send further tweaks to either client cut; apply to `brand-value-plan-client.md` or `launch-plan-client.md` and re-run the matching generator.
- Still open from before this session: write the Shopify coming-soon page step-by-step (already researched), the items waiting on Lucy (prices, fabric, opening Shopify), and the customer-comms setup.

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
