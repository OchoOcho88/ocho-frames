# Sportif Post-Lucy Research Plan

> **What this is:** the queued research and synthesis plan that runs the moment Lucy returns the intake questionnaire. Uses Perplexity to read deeper than WebSearch, with Lucy's actual answers as the anchor.
>
> **Trigger phrases in chat (any of these activates this plan):**
> - "Lucy has responded"
> - "Lucy's answers are in"
> - "the questionnaire is back"
> - "Lucy sent the questionnaire back"
> - "we got Lucy's intake"
>
> **Expected trigger date:** ~2026-06-03 (5 days from intake send on 2026-05-28). Could be earlier if she voice-memos.
>
> **End state when this plan completes:** populated `clients/sportif/brand.md`, 3 to 5 competitor analyses in `clients/sportif/competitor-analyses/`, a working Stage 3 synthesis brief, refined platform-by-platform budget bands, all anchored to Lucy's actual answers + market research.
>
> _Written 2026-05-29 during the 5-day Lucy-response window. Author: Claude (Session 005)._

---

## TL;DR

When Lucy responds, run **5 Perplexity research passes** (estimated cost: **$3 to $7 AUD total**), then synthesize. Total elapsed time: ~2 hours of focused work. Output is decision-grade.

| Pass | Purpose | Perplexity model | Est. cost | Output saved to |
|---|---|---|---|---|
| 1 | Australian segment deep profile (Lucy's Q5 anchor) | `sonar-deep-research` | $1 to $2 | `clients/sportif/research/au-segment-profile.md` |
| 2 | Per-competitor deep dives (one per name in Q4) | `sonar-deep-research` | $1 per competitor | `clients/sportif/competitor-analyses/<brand>-perplexity-profile-2026-MM-DD.md` |
| 3 | Brand reference reverse-engineering (Q8) | `sonar-pro` | ~$0.10 each | `clients/sportif/research/brand-references.md` |
| 4 | Cultural lane validation (the chosen lane from SWOT) | `sonar-reasoning-pro` | ~$0.50 | `clients/sportif/research/cultural-lane-validation.md` |
| 5 | Budget benchmarking with channel mix locked | `sonar-pro` | ~$0.30 | `clients/sportif/research/budget-benchmarks.md` |

---

## The to-do list

When Lucy's answers arrive, execute in this order. Tick boxes as we go.

- [ ] **Step 1.** Process Lucy's raw responses. If voice memos, transcribe via Whisper (recipe at `recipes/transcribe-voice-memos.md`, to be built). If written, copy answers into `clients/sportif/intake/lucy-responses.md` as the source-of-truth.
- [ ] **Step 2.** Quick read-through: identify Lucy's stated cultural lane and tone direction. Flag any answer that surprises us vs. the SWOT assumptions.
- [ ] **Step 3.** Run **Pass #1** (Australian segment profile). Anchor: Lucy's Q5 customer description. See "Research Pass #1" below.
- [ ] **Step 4.** Run **Pass #2** (per-competitor deep dives). One Perplexity query per competitor Lucy names in Q4. See "Research Pass #2" below.
- [ ] **Step 5.** Run **Pass #3** (brand reference reverse-engineering). For each brand Lucy names in Q8 (what feels right) and Q9 (what feels wrong). See "Research Pass #3" below.
- [ ] **Step 6.** Run **Pass #4** (cultural lane validation). Lock the positioning lane (Pilates / longevity / design-led / inclusive-fitness / other). See "Research Pass #4" below.
- [ ] **Step 7.** Lock Sportif's channel mix based on Lucy's Q6 (where customer hangs out) and Q12 (timeline/rollout).
- [ ] **Step 8.** Run **Pass #5** (budget benchmarking with channel mix locked). Refine the Part 8 budget bands with Sportif-specific numbers. See "Research Pass #5" below.
- [ ] **Step 9.** Populate `clients/sportif/brand.md` from Lucy's answers + all research outputs. This is the canonical brand kit.
- [ ] **Step 10.** Draft Stage 3 synthesis creative brief at `clients/sportif/campaigns/launch-2026-09/synthesis-brief.md`.
- [ ] **Step 11.** Update Sportif's launch budget bands in `docs/marketing-fundamentals.md` Part 8 with the real numbers.
- [ ] **Step 12.** Send Lucy a summary email: here's where we are, here's the proposed positioning, here's the next call agenda.

---

## Research Pass #1: Australian segment deep profile

**Anchor:** Lucy's Q5 answer (the ideal customer described "like they're a real person").

**Why Perplexity, not WebSearch:** WebSearch returns SEO blog posts about general AU fitness trends. Perplexity in deep-research mode autonomously queries IBISWorld AU, Roy Morgan participation data, Statista AU, ABS demographic data, Nielsen AU, and synthesizes them into one customer profile with line-by-line citations. Concrete worked example: if Lucy says "32-year-old Sydney Pilates regular who values sustainability," Perplexity returns this segment's AU fitness spend, their sustainability purchase behavior, their platform consumption patterns, and the brands they already buy from. WebSearch can't synthesize across that many sources without me firing 20+ manual queries.

**Prompt to run (fill in [bracketed inputs] from Lucy's Q5 + Q6 answers):**

```bash
python3 scripts/perplexity_search.py "Build a deep customer segment profile for an Australian fitness accessories DTC brand. Target customer per founder: [PASTE Q5 ANSWER VERBATIM]. Primary platforms they use per founder: [PASTE Q6 ANSWER VERBATIM]. Geographic focus: Australia (specify cities if mentioned in Q5).

Research and return:

1. Demographic profile: age band, income, location concentration, household composition, employment patterns. Cite AU sources (IBISWorld, ABS, Roy Morgan, Nielsen AU) where possible.
2. Psychographic profile: values, aspirations, anxieties, daily routine, fitness habits, media consumption patterns, what they spend on.
3. Category behavior: what fitness products do they already buy, at what price points, from which brands. AU-specific.
4. Sustainability and ethics: how much does it actually influence their purchasing in this category (AU data).
5. Social platform behavior: what content do they engage with on Instagram, TikTok, Facebook in fitness specifically. What creators do they follow.
6. Purchase journey: how do they discover and buy fitness accessories. DTC vs retail vs Amazon AU. Average basket size.
7. Underserved needs: what does this segment complain about that competitors don't solve.

Output as structured markdown. Cite every claim. Distinguish high-confidence findings from inferences. Flag anything Australia-specific that differs from US/UK." --model sonar-deep-research --max-tokens 8000 > clients/sportif/research/au-segment-profile.md
```

**Estimated cost:** $1 to $2 AUD.

**What we'll do with it:** populate the "Customer archetype" section of `brand.md`, and feed it as input to the Stage 3 synthesis brief. Also inform creator-tier strategy (which AU fitness creators reach this exact segment).

---

## Research Pass #2: Per-competitor deep dives

**Anchor:** Lucy's Q4 answer (the 2 to 5 competitors she names).

**Why Perplexity:** for each competitor, we get a publication-grade profile (positioning, content style, ad creative, social presence, recent moves, vulnerabilities) instead of the WebSearch summary which is mostly marketing-blog SEO content. Perplexity sources from Crunchbase, LinkedIn, industry trade press, and the brand's own primary channels.

**Prompt to run (one per competitor named in Q4):**

```bash
# Replace [COMPETITOR] with each name from Lucy's Q4
python3 scripts/perplexity_search.py "Build a competitive intelligence profile on [COMPETITOR], an Australian fitness brand. Cover:

1. Brand snapshot: founding year, founders, headquarters, current size (revenue, team, retail presence), funding history if any.
2. Positioning: how do they describe themselves vs. how the market describes them. What single cultural lane do they own (Pilates, strength, longevity, design, sustainability, etc.).
3. Product mix: core SKUs, price tiers, hero product, recent launches.
4. Content style: dominant Instagram and TikTok aesthetic, posting cadence, hook style, top-performing post archetypes if visible.
5. Paid advertising: any Meta Ad Library evidence of current creative. What angles do they run.
6. Creator and influencer strategy: who do they partner with, tier mix, signs of long-term ambassador programs.
7. Email and retention: subscription, loyalty, anything visible about how they retain customers.
8. Distribution: DTC website, Amazon AU, retail partners.
9. Recent moves (last 12 months): launches, expansions, controversies, leadership changes.
10. Vulnerabilities: where are they weak, what do reviews complain about, where could a new entrant compete.

Output as structured markdown. Cite every claim with source. Distinguish high-confidence facts from inferences. Australia-specific focus." --model sonar-deep-research --max-tokens 8000 > clients/sportif/competitor-analyses/[competitor-slug]-perplexity-profile-2026-MM-DD.md
```

**Estimated cost:** $1 per competitor. If Lucy names 4 competitors, ~$4 total.

**What we'll do with it:** these are the Stage 2 outputs (alongside any video analyses we run later). They feed the Stage 3 synthesis brief and the "what we deliberately do differently" section of `brand.md`.

---

## Research Pass #3: Brand reference reverse-engineering

**Anchor:** Lucy's Q8 (what feels right) and Q9 (what feels wrong).

**Why Perplexity:** for each brand Lucy references, we want to understand WHY it feels right or wrong to her. Perplexity can pull that brand's positioning, voice, visual identity, and current campaigns in one synthesized response. WebSearch would require fetching their site, reading reviews, and finding press coverage manually.

**Prompt to run (one per brand in Q8 and Q9):**

```bash
# For each brand reference, replace [BRAND] and use right/wrong context
python3 scripts/perplexity_search.py "Reverse-engineer the brand identity of [BRAND]. The Sportif founder cited this brand as a reference for what feels [right / wrong] for Sportif. Cover:

1. Positioning: what they sell themselves as.
2. Voice and tone: pick 5 to 7 adjectives that capture how they sound.
3. Visual identity: color palette (provide hex codes if visible), typography, photography style.
4. Hook archetypes: what hooks do they use on social.
5. The reference signal: what about this brand likely 'feels right' (or wrong) for a fitness accessories launch. Be specific about the borrowable (or avoidable) elements.

Output as structured markdown. Cite sources. Focus on what Sportif can learn from or avoid." --model sonar-pro --max-tokens 3000 > clients/sportif/research/brand-references.md
```

**Note:** we'll append all references into the one `brand-references.md` file with clear section headings per brand. Easier to read side-by-side.

**Estimated cost:** ~$0.10 per brand. Lucy will likely name 6 to 8 total across Q8 and Q9, so ~$0.80.

**What we'll do with it:** feed into the "Voice and tone" and "Visual identity" sections of `brand.md`, and the synthesis brief's "what we deliberately borrow from" section.

---

## Research Pass #4: Cultural lane validation

**Anchor:** the SWOT identified four candidate cultural lanes (Pilates, longevity, design-led, inclusive-fitness). Lucy's answers (especially Q1, Q2, Q3, Q7, Q8) will point at one of them. This pass validates the chosen lane against current AU market data before we lock it.

**Prompt to run (replace [LANE] with the chosen lane after reading Lucy's answers):**

```bash
python3 scripts/perplexity_search.py "Validate the [LANE] positioning for a new Australian fitness accessories DTC brand launching September 2026. Specifically:

1. Is this lane growing, plateauing, or saturating in Australia in 2026? Cite participation data, search volume trends, ClassPass AU data, IBISWorld AU.
2. Who currently owns this lane in AU and how dominant are they.
3. What is the gap a new entrant could realistically own (sub-positioning).
4. What language and visual codes currently dominate this lane on Australian Instagram and TikTok.
5. What positioning has been overdone (where the lane is exhausted).
6. What proof points would make a new entrant in this lane credible to Australian buyers.

Output as structured markdown with citations. Be honest if the lane is already saturated and recommend an adjacent angle." --model sonar-reasoning-pro --max-tokens 5000 > clients/sportif/research/cultural-lane-validation.md
```

**Estimated cost:** ~$0.50.

**What we'll do with it:** finalize the cultural lane in `brand.md`. If the validation surfaces a saturated lane, regroup before writing the synthesis brief.

---

## Research Pass #5: Budget benchmarking with channel mix locked

**Anchor:** Lucy's Q6 (where customer hangs out) tells us which platforms to invest in. Q11 (off-limits + success definition) tells us the scale she expects. Q12 (timeline + rollout) tells us whether to phase spend or load-front. With those known, we can refine the budget bands in `docs/marketing-fundamentals.md` Part 8.

**Prompt to run (fill in channel mix from Lucy's Q6):**

```bash
python3 scripts/perplexity_search.py "Build a 2026 Australian fitness accessories DTC launch budget benchmark. Channel mix: [PASTE CHOSEN MIX from Lucy's Q6, e.g., Instagram + TikTok + Facebook]. Launch month: September 2026. Sydney/Melbourne primary geo. Specifically:

1. Realistic per-channel monthly ad spend bands (AUD) for: (a) lean launch ($5-10K total month), (b) mid launch ($15-30K), (c) scale launch ($50K+).
2. Realistic AU fitness creator costs by tier (nano, micro, mid). What does a 4-to-6-creator launch cohort actually cost.
3. Tool stack cost: Shopify + Klaviyo + email/SMS + attribution tooling. AUD monthly.
4. Production cost: what does it cost to produce one launch-grade video creative in AU (creator-led, not agency-led).
5. Seasonality: how much does September AU CPM differ from January and November in fitness.
6. Realistic ROAS expectations for a new AU fitness DTC brand in month 1 vs month 3 vs month 6.
7. The 'efficient frontier': at what total monthly spend does additional spend stop adding incremental revenue.

Output as structured markdown with AU-specific numbers and citations. Distinguish published benchmarks from estimates." --model sonar-pro --max-tokens 5000 > clients/sportif/research/budget-benchmarks.md
```

**Estimated cost:** ~$0.30.

**What we'll do with it:** rewrite the Part 8 Phase 2 budget table in `docs/marketing-fundamentals.md` with Sportif-specific AUD numbers. Send a tighter budget recommendation to Lucy as part of the proposal.

---

## After all 5 passes: synthesis

Once the research is in, the work shifts from research to synthesis:

1. **Populate `clients/sportif/brand.md`.** Use Lucy's answers as the primary input. Use the research as the validation and context layer. The brand kit should NOT just be the research outputs concatenated. It should be a sharp, opinionated articulation of Sportif's identity, voice, and visual direction.

2. **Draft `clients/sportif/campaigns/launch-2026-09/synthesis-brief.md`.** This is Stage 3 of the pipeline. Mode: competitor-first (Sportif has no existing voice). Inputs: brand.md + the competitor analyses + the cultural-lane validation. Output: ONE creative direction with three distinct creative angles to test.

3. **Update `docs/marketing-fundamentals.md` Part 8.** Replace the illustrative budget bands with Sportif-specific numbers from Pass #5. Update the channel-mix table with Lucy's confirmed platforms.

4. **Send Lucy a "where we are" summary.** Brief email summarizing the proposed positioning, channel mix, budget recommendation, and next call agenda. Concise. She doesn't need to read the research.

---

## What's blocked on Lucy's actual answers

Things we cannot research or write until she responds:

- The customer-archetype Section of `brand.md` (Q5 anchored).
- The competitor analyses (Q4 anchored).
- The voice and visual reference research (Q8 + Q9 anchored).
- The cultural lane lock (Q1, Q2, Q3, Q7, Q8 anchored).
- Channel mix priorities and budget tiers (Q6, Q11, Q12 anchored).

Things we CAN keep working on between now and her response (the rest of Session 005's to-do list):
- Research Seadance + ChatGPT Image 2.0 current prompt formats (Stage 4 prerequisite).
- Write `prompts/synthesis-creative-brief.md` (Stage 3, mode-aware template).
- Build voice-memo-to-questionnaire transcription recipe (will be needed if Lucy voice-memos).
- Add image-analyzer skill (Stage 1 second path).

---

## Total estimated Perplexity cost

| Pass | Model | Approx cost (AUD) |
|---|---|---|
| 1: Segment profile | sonar-deep-research | $1.00 to $2.00 |
| 2: Competitor profiles (×4 average) | sonar-deep-research | $4.00 |
| 3: Brand references (×6 to 8) | sonar-pro | $0.80 |
| 4: Cultural lane validation | sonar-reasoning-pro | $0.50 |
| 5: Budget benchmarking | sonar-pro | $0.30 |
| **Total** | | **~$6.60 to $7.60 AUD** |

Cheap. The synthesis work is where the real value is.

---

## Why Perplexity for THIS specific work (vs WebSearch)

Five concrete advantages that compound for Australian-market, segment-specific research:

1. **Better local and regional sources.** Perplexity surfaces IBISWorld AU, Roy Morgan, Statista AU, ABS, Nielsen AU, and AU industry trade press. WebSearch defaults to globally-indexed SEO content (US-heavy).
2. **Cross-source synthesis.** A question like "describe the Sydney Pilates regular's fitness spend" combines demographic data + participation data + purchase behavior + social listening. Perplexity returns one coherent profile. WebSearch returns 10 disconnected results that I'd manually fuse.
3. **Deep Research autonomous mode.** `sonar-deep-research` runs 30+ queries on a single question without me directing each one. WebSearch needs me to fire each query individually.
   - Operational note (added Session 006, 2026-05-29): `sonar-deep-research` now runs through Perplexity's async API automatically inside `scripts/perplexity_search.py`. It submits the job, then polls (you will see `IN_PROGRESS` lines on stderr) until `COMPLETED`, typically a few minutes. The commands in this plan work as written, the `>` redirects still capture only the answer. The earlier sync-call failure (RemoteDisconnected) is fixed.
4. **Citation precision.** Perplexity attaches a citation to each claim (line by line). WebSearch returns sources as a flat list with no claim-source mapping.
5. **Recency filtering and source reliability scoring.** Perplexity filters by recency natively and ranks source authority. WebSearch returns mixed-recency and mixed-authority results.

Worked example: if Lucy says her customer is "women 28-42 in Sydney/Melbourne who do Pilates twice a week and care about sustainability":

- **WebSearch returns:** 10 SEO blog posts ("Top 10 Pilates Trends in Australia 2026"), maybe one ABS link, mixed recency. I'd need 5+ follow-up queries to get spend data.
- **Perplexity sonar-deep-research returns:** a 2-to-3-page profile pulling AU fitness spend by age band (Roy Morgan), Pilates participation growth in Sydney/Melbourne (IBISWorld AU), sustainability purchase behavior in this segment (Statista AU), platform consumption patterns (Nielsen AU), and the brands this segment already buys from (industry trade press). All cited line by line.

That's the upgrade.

---

## Cross-links

- Sportif intake: [`questionnaire.md`](questionnaire.md) (sent 2026-05-28)
- Sportif strategic context: [`swot-analysis.md`](swot-analysis.md), [`swot-summary.md`](swot-summary.md)
- Pipeline architecture: [`../../../docs/pipeline-architecture.md`](../../../docs/pipeline-architecture.md)
- Marketing fundamentals (Part 8 = Sportif blueprint): [`../../../docs/marketing-fundamentals.md`](../../../docs/marketing-fundamentals.md)
- Perplexity helper: [`../../../scripts/perplexity_search.py`](../../../scripts/perplexity_search.py)
- Perplexity README and model guide: [`../../../skills/perplexity-search/README.md`](../../../skills/perplexity-search/README.md)
