# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## Weekly Review — 2026-07-05 (week of 2026-06-29)

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

## Weekly Review — 2026-06-21 (week of 2026-06-15)

Four sessions this week (008, 009, 010, 011), all on Sportif. This was the week Sportif went from "research and assumptions" to "real client, real meeting, locked decisions" — and the positioning narrowed twice under real-world constraints.

### Highlights
- **First in-person meeting with Lucy, and three big open calls finally settled (Session 011).** Hugo met her face to face and folded her answers into all three source-of-truth docs (`brand.md`, `synthesis-brief.md`, `brand-value-plan.md`). Name LOCKED as **Sportif** (open since Session 007), hero product LOCKED as **the band sold inside a giftable set**, and go-to-market LOCKED as **parallel wholesale + DTC** (not "wholesale-first"). The pouch was reclassified as a gift-with-purchase over ~$70, not a product to sell.
- **The entire Sportif research run executed end to end (Session 008).** All 5 Perplexity passes (segment + 8 competitor deep-dives + references + cultural-lane + budget), synthesized into `brand.md`, with the Stage 3 synthesis brief drafted. This cleared the Session 007 egress blocker and required building a brand-new async tooling pattern to do it.
- **The hands-on competitor audit produced the week's biggest strategic correction (Session 009).** Hugo photographed all 8 named competitors and we built a visual product board from live Shopify `/products.json` data. The finding: the colourful band/strap space is NOT empty (Move Active, Your Reformer, Avara, Kikiva already sell colour) — correcting the original desk-research belief. The "real gap is pattern" thesis was born here.
- **Positioning pivoted from product-led to founder-led (Session 011 follow-up).** Once we learned the manufacturer's real constraints (China, ~35-day turnaround, predefined colourways only, no custom pattern), the pattern bet was deferred and the differentiator moved decisively to **Lucy Wayne herself** — her brand, eye, and the community/experience around a standard factory product. Lever 2 of the Brand Value Plan was elevated to THE primary lever.

### Patterns I noticed
- **Reality kept overriding desk research, every single time.** The colourful-space-isn't-empty correction came from Hugo actually browsing competitor sites, not from more analysis. The pattern-is-impossible / colours-are-constrained correction came from learning the manufacturer's real terms. The differentiator hunt narrowed three times in one week — **colour → pattern → Lucy herself** — each step forced by a constraint we didn't know before. Lesson: hold product-based differentiators loosely until manufacturing is confirmed.
- **Devil's advocate passes keep earning their keep.** The digital-plan pass in Session 011 surfaced that **@lucywayne__ has only ~900 followers**, which reframed the entire growth plan from "borrow her audience" to "build one" and promoted ambassador/instructor seeding to the main growth engine.
- **"A mum can read it" is a recurring requirement.** Hugo flagged jargon in Session 009, asked for Claude's own extra questions to be stripped from Lucy's meeting guide (Session 010), and wanted a non-technical WhatsApp guide for the email setup (Session 011). Anything Lucy-facing must be jargon-free.
- **Em-dash leakage, again.** Session 008 had to sweep em/en dashes out of the Perplexity research outputs. Same recurring problem flagged in prior weeks — automated outputs reintroduce them.

### Skills / knowledge gained
- **Cowork environment limit + the fix.** Background shell processes do NOT survive across separate tool calls (the sandbox reaps them; ~45s per call). So the "launch deep-research with nohup and poll" workflow from CLAUDE.md does not work here. Fix built: `scripts/pplx_async.py` submits async Perplexity jobs server-side, persists request IDs to disk, and polls in later short calls. Perplexity rate-limits async submissions (HTTP 429) — stagger submits and resubmit-on-fail.
- **Manufacturing reality (the constraint that reshaped strategy).** Lucy's manufacturer is in China, ~35-day turnaround from order, predefined colourways only, no custom pattern. This single fact killed the pattern bet and constrained the palette.
- **Market price anchors are now documented:** booty bands ~$29, ankle straps $30–39, grip socks $9–39, towels $26–79, pouches $70–249. Branded pouches do sell (Anine Bing $249 sold out, ODE $70). Towels are in demand.
- **Tooling gotchas captured:** public Shopify `/products.json` gives live prices/images (use `?limit=`); remote images don't render in local HTML so embed base64; local screenshots embed fine but remote binaries can't be downloaded; macOS screenshot filenames contain a no-break space (rename by glob order); deletions are blocked in the mounted folder (overwrite instead); the Read tool can't see brand-new files at the workspace path (copy to outputs to view).
- **2026 digital best practices:** IG product tags now live in Reels (link-in-bio dying), TikTok Shop AU launching 2026, Facebook is an ads/tracking engine not an organic channel, Klaviyo welcome-flow timing matters.

### Open questions still unresolved

**Resolved this week (settled by a later session):**
- [x] ~~Settle the three devil's-advocate calls (hero product, go-to-market, pattern).~~ RESOLVED Session 011: hero = band-in-set, go-to-market = parallel wholesale + DTC, pattern = deferred.
- [x] ~~Lock the brand name.~~ RESOLVED Session 011: name LOCKED as **Sportif** (trademark clearance still pending separately — see below).
- [x] ~~Decide whether the band, strap, pouch, or set should be the hero.~~ RESOLVED Session 011: the band leads, presented inside a giftable set.
- [x] ~~Validate the pattern bet / confirm pattern is manufacturable.~~ RESOLVED Session 011 follow-up: manufacturer offers predefined colourways only, no custom pattern — Step 0 pattern gate closed as DEFERRED.
- [x] ~~Confirm Lucy's custom colours are distinct from Kikiva / Your Reformer.~~ SUPERSEDED Session 011: colours are constrained to the manufacturer's predefined range, so colour is no longer the differentiator; Lucy is.
- [x] ~~Set up the EA's (Lauren's) lucywayne.com.au mailbox.~~ RESOLVED Session 011 follow-up: Workspace already exists, domain at GoDaddy, so it's an add-a-user job; a non-tech WhatsApp guide was produced.

**Still open (carried into next week):**
- [ ] **Trademark clearance** — name is chosen but legal clearance is still in progress with Lucy's lawyer. Hold logo/label-dependent finals until clear.
- [ ] **Materials** — which of recycled / organic / hemp Lucy can actually use. Still being chosen; gates any sustainability claim in copy.
- [ ] **One Shopify store or two** — recommendation logged (one store with Shopify Markets, split later only if forced); confirm with Lucy.
- [ ] **Execute the build workstreams** — Shopify store build, Instagram Shopping setup, content posting calendar, unboxing content ideas for Lucy to self-film, podcast outreach. (EA email is done; the rest are open.)
- [ ] **Ambassador / instructor seeding shortlist** — build it ready for the early-July band delivery; this is now the main growth engine.
- [ ] **Tight Lucy-facing competitor snapshot** — open since Session 009 (the full internal board is too big to send her).
- [ ] **Session 008 Step 11** — fold Sportif AUD budget numbers into `docs/marketing-fundamentals.md` Part 8.
- [ ] **Session 008 Step 12** — the "where we are" summary email to Lucy (largely superseded by the in-person meeting; decide whether it's still needed or can be closed).
- [ ] **Validate low-confidence competitor prices** (Leelo, Avara, Kikiva, Your Reformer) — partially addressed by Session 009's live-Shopify capture, but not all confirmed.
- [ ] **Lucy's Leelo quality-check notes** — add when her ordered Leelo item arrives (open since Session 008).
- [ ] **Document the `pplx_async.py` async pattern** in the workspace gotchas so future Cowork sessions use it by default.
- [ ] **Stage 4 production** — pick the first production need from the winning angle and write the gpt-image-2 prompt(s).

### Suggested focus for next week
1. **Start the build workstreams now that strategy is locked — Shopify first.** The band ships early July and there is currently nowhere to sell it. Confirm the one-store decision with Lucy, then stand up the store and Instagram Shopping. This is the critical-path revenue blocker.
2. **Build the ambassador / instructor seeding shortlist before the July delivery.** It's now the primary growth engine (per the devil's advocate revision) and needs lead time to seed before product lands.
3. **Close the materials question with Lucy (recycled / organic / hemp).** It's the last gate on whether any sustainability story can be told, and it's currently blocking copy.

---

## Session 011 (2026-06-18): First in-person meeting with Lucy, three open calls settled, docs folded

### What we did
- Hugo met Lucy face to face. Folded her answers into the three source-of-truth docs: `clients/sportif/brand.md`, `campaigns/launch-2026-09/synthesis-brief.md`, and `brand-value-plan.md`. Verified the reference to "440 Bronte" (it is the 440 Run Club @the_440, the Bronte Beach community run club) by web search before writing it in.
- Asked Hugo four clarifying questions before editing (go-to-market, hero product, the blank community note, and the 440 reference) rather than assuming.

### What changed versus what we assumed
- **Name LOCKED: Sportif.** Le Sport Collectif / LSC were placeholders, not the brand. Closes the naming question open since Session 007. (Trademark registration still in progress with Lucy's lawyer; the name choice is settled, the legal clearance is not.)
- **Go-to-market is now PARALLEL wholesale plus DTC, not "wholesale-first."** Hugo told Lucy to run both: she places product into gyms she already has relationships with (warm wholesale) while we build the DTC engine (Shopify, content, email) at the same time. This rewrites the "wholesale-led, light DTC" framing from Session 010.
- **The pouch is a GIFT BAG, not a product to sell.** Lucy's words. So the giftable set (band, strap, pouch) is the unit and the unboxing is content, not a revenue line. Softened all "sell the pouch as a hero product" language across brand.md and the brief. A separately sold pouch stays open as a possible later extension.
- **Pattern is gated EARLIER than we thought.** Materials (recycled, organic, hemp) are still being chosen, so neither the pattern bet nor any sustainability claim can be confirmed until a material is locked. Step 0 gate reinforced; make no material claim in copy yet.
- **Hero product SETTLED: the band leads.** It is her first product and what is arriving (500 units, early July), and her first content is self-filming the unboxing. We mitigate the band's commoditisation by presenting it inside a giftable set in the custom palette with the founder story, never bare band-versus-band on price.
- **Community mechanic SETTLED: ambassador and instructor seeding,** built the way the 440 Run Club built its Bronte beach-culture community (emulate the model, do not necessarily partner with them). (Meeting note #5 came through blank in the paste; Hugo confirmed it via the follow-up question.)

### New workstreams the meeting created (captured in brand.md "Build and setup workstreams")
- Google Workspace email for Lucy (she needs help setting it up).
- Shopify store build, plus the one-store-vs-two (AU and US) decision. Recommendation logged: start with ONE store using Shopify Markets, split later only if forced.
- Instagram Shopping setup (tagged, shoppable products).
- Two landing pages: a Lucy Wayne personal page funnelling to a Sportif brand page.
- A content posting calendar (soft launch now), unboxing and content ideas for Lucy to self-film, and a content funnel from Instagram and TikTok into email and store.
- PR: get Lucy onto podcasts. She also has a small existing contact list to seed the email waitlist.

### Decisions
- Settled two of the three devil's-advocate calls (hero product = band-in-set, go-to-market = parallel). Left the pattern call OPEN on purpose because it depends on the unchosen material and the supplier.
- Kept the creative direction and three test angles intact; they still hold under the new decisions.

### Open questions / next
- [ ] **Materials:** which of recycled / organic / hemp Lucy can use. Unblocks both the sustainability story and the pattern bet.
- [x] ~~**Pattern (Step 0):** once material is locked, confirm with the supplier that a woven texture or print is makeable, durable, affordable.~~ RESOLVED later this same session (Follow-up correction): the China manufacturer offers predefined colourways only with no custom pattern, so the Step 0 pattern gate is closed as DEFERRED and the differentiator moved to Lucy herself.
- [ ] **Trademark clearance** (hold logo- and label-dependent finals until clear).
- [ ] **One Shopify store or two** (recommend one with Shopify Markets, confirm with Lucy).
- [ ] Execute the build workstreams: Google Workspace email, Shopify, Instagram Shopping, the two landing pages, the content calendar, unboxing content ideas, podcast outreach.
- [ ] Build the ambassador / instructor seeding shortlist ready for the July band delivery.
- [ ] Carried: tight Lucy-facing competitor snapshot, Session 008 Steps 11 and 12, Lucy's Leelo quality-check notes when her order arrives. (Pattern mockups dropped, see correction below.)

### Follow-up correction (2026-06-18, later same session): the product is not the differentiator, Lucy is

After the first doc pass, Hugo clarified three things that change the positioning, now folded into all three docs:

- **Pouch is a gift-with-purchase, not a "gift bag".** Customers who spend over a threshold (about $70) get the pouch free. It is an incentive / add-on that lifts average order value and makes the order feel like a gift, not packaging on every order and not a product to sell.
- **Pattern is DEFERRED and colour is constrained.** The manufacturer is in China, roughly a 35-day turnaround from order placement, and offers predefined colourways only. So no custom pattern any time soon, and the colours are a selection from a standard range, not bespoke. Neither is a defensible differentiator.
- **The differentiator is now Lucy Wayne herself** (her personal brand, experience, styling eye, and the experience plus community around the product), because the product is a standard factory item. Repointed brand.md, synthesis-brief.md (creative direction is now "By Lucy. For your morning ritual."; Angle C "Made by Lucy" is the lead angle; the "validate the pattern" Step 0 gate is closed as deferred), and brand-value-plan.md (Lever 2 elevated to THE primary lever; Lever 1 recognition now rests on Lucy plus consistent warm-neutral styling, not a pattern).
- **New task: set up the EA's email.** Lucy wants her EA Lauren on a lucywayne.com.au mailbox via Google Workspace (workspace.google.com). Domain is www.LucyWayne.com.au. Resolved: Workspace already exists, domain at GoDaddy, so it is an add-a-user job. Produced a non-tech WhatsApp guide for Lucy (`clients/sportif/lauren-email-guide-for-lucy.txt`).

### Follow-up (2026-06-18, continued): email-list kit, digital ecosystem plan, and a devil's advocate revision

- **Email list / subscriber kit.** Lucy's GoDaddy signup captured emails but had nothing to give subscribers. Built `campaigns/launch-2026-09/email-list-starter-kit.md` (signup copy, a welcome email from Lucy, a mini list plan) and a designed lead-magnet PDF `campaigns/launch-2026-09/lucys-morning-edit.pdf` (Lucy's Morning Edit, lifestyle framed, no health claims). Clarified the pouch is a gift-with-purchase over a ~$70 spend threshold (an incentive), not packaging-for-all.
- **Digital ecosystem action plan.** Researched 2026 best practices (IG product tags in Reels and the death of link-in-bio, TikTok Shop AU launching 2026, Facebook = ads/tracking engine not organic posting, Klaviyo welcome-flow timing). Built `clients/sportif/digital-ecosystem-action-plan.md` (working checklist) and `clients/sportif/Sportif-Digital-Plan-for-Lucy.pdf` (2-page approval doc with an ecosystem map). Folded our own research files (au-segment-profile, brand-references, budget-benchmarks) in for AUD budget bands, content archetypes, and posting times.
- **Devil's advocate review (ran the skill).** Saved at `clients/sportif/digital-plan-devils-advocate.md`. The big surfaced fact: **@lucywayne__ has about 900 followers**, so we are building an audience, not funneling one. Seven challenges, all held up, all folded into the plan and the PDF:
  1. Lucy is a single point of failure (capacity is moderate/structured) → batch-film, Hugo writes shot lists, keep a 2 to 3 week buffer, ambassador/product/customer content carries half the feed.
  2. Personal audience is ~900 → reframe from "borrow her audience" to "build one"; she is the trust/face, not the reach.
  3. Too many properties → **collapse to one hub (@sportifcollection), no separate Lucy Wayne website** (walks back a meeting idea, flag to Lucy).
  4. "Paid later" starves reach → **ambassador/instructor seeding is the main growth engine** plus a **small paid layer brought forward** for follows and email; retire the vanity 10k goal for an honest one.
  5. 500 units + 35-day reorder → **founding drop + back-in-stock/pre-order waitlist + early batch-2 reorder** (cash call for Lucy).
  6. Over-betting on TikTok → **Instagram + email is the spine, TikTok light** (repurposed), TikTok Shop is upside (Claude's call, Hugo deferred).
  7. Wholesale was barely in the plan → **elevated to a real front-loaded workstream** (line sheet, lookbook, gym list, pricing, outreach Lucy runs); likely the faster near-term revenue (Claude's call, Hugo deferred).

### Follow-up (2026-06-18, continued): account reconnaissance, the responsiveness flag, and simple Lucy-facing docs

Hugo browsed Lucy's real accounts and shared screenshots. Findings folded into `brand.md` and the digital plan:

- **Brand handles all secured and on-brand** (SPORTIF wordmark on blush peach): domain `sportifcollection.com.au`, **Instagram `@sportifcollection`** (0 posts, 10 followers, "Australian owned luxury activewear & fitness accessories brand. Launching 2026!", and Lucy's personal account follows it), and **TikTok `@sportifcollection`** (empty, bio "Affordable luxury fitness equipment and active wear"). The earlier "secure the handle" action is DONE; remaining job is to align the bios and start posting.
- **Lucy's personal presence (a warm asset, used as a light bridge, NOT rebuilt):** `@lucywayne___` (826 followers, **verified**, "Personal Stylist & Certified Trainer"), the GoDaddy site `lucywayne.com.au`, a **Stan Store**, a personal **TikTok `@lucywayne_`** (32 followers, bio credits "Founder/Designer: @sportifcollection"), and two Calendly links. Verified and on-topic helps; tiny follower counts confirm we are building an audience, not borrowing one.
- **Responsiveness / operations risk (important).** An inquiry through her personal website went **unanswered for 7 days**, and her bio links are fragmented. Implication: Sportif must not depend on Lucy answering fast, and must not route customers through her personal channels. Added an "Operational note: who answers customers" section to the digital plan (one monitored Sportif inbox, Lauren owns replies, Klaviyo automates confirmations). Raise with Lucy: who replies to customers, and how fast.
- **Architecture confirmed:** one brand hub (`sportifcollection.com.au` + `@sportifcollection` + email), her personal accounts a light bridge. NOT building a separate Lucy Wayne website. Added a "Secure and align the accounts" checklist to Phase 0.
- **New simple deliverables built:** a Lucy-facing "how it all works" one-pager (`Sportif-The-Plan-Simply.pdf`), a 15-step "What we do, and why" roadmap (`Sportif-Roadmap.pdf`), and a Shopify-setup info checklist to send Lucy (`shopify-setup-info-from-lucy.md`).

### Close-out (end of 2026-06-18 session)

**Where we are:** strategy is locked and folded into the source docs (`brand.md`, `synthesis-brief.md`, `brand-value-plan.md`). The digital plan is built, devil's-advocate-revised, and explained to Lucy in plain-English visuals. All three brand handles are secured and on-brand (Instagram + TikTok `@sportifcollection`, domain `sportifcollection.com.au`). Waiting on Lucy to start the build.

**Lucy-facing deliverables produced (all on-brand PDFs unless noted, warm palette, Shopify green on the hub):**
- `Sportif-The-Plan-Simply.pdf` (one-page "how it works" loop)
- `Sportif-Socials-to-Shop.pdf` (3-page flowchart, real handles, green Shopify hub)
- `Sportif-Digital-Plan-for-Lucy.pdf` (2-page map + phases; map shows handles plus Lucy's accounts and website)
- `Sportif-Roadmap.pdf` (15-step "what we do and why")
- `Sportif-Action-Plan.pdf` (prioritised checklist + the why)
- `Sportif-Setup-Info-for-Lucy.pdf` (the "what I need from you" form)
- `lucys-morning-edit.pdf` (lead-magnet gift) + `email-list-starter-kit.md` (signup copy, welcome email, list plan)
- `email-to-lucy-next-steps.md` (copy-paste email for Hugo to send Lucy with the attachments)
- `lauren-email-guide-for-lucy.txt` (WhatsApp guide for the EA mailbox)

**Internal working docs:** `digital-ecosystem-action-plan.md` (executable checklist + operational note on customer comms), `digital-plan-devils-advocate.md`, `action-plan-checklist.md`, `shopify-setup-info-from-lucy.md`.

**Open / next (resume note at `clients/sportif/RESUME-NOTE.md`):**
- [ ] **Hugo is reviewing `Sportif-Brand-Value-Plan.pdf`** and will bring thoughts to a fresh session. That is the NEXT focus: update `brand-value-plan.md` (and re-export the PDF) per his notes.
- [ ] Still to write: the **Shopify coming-soon page step-by-step** (2026 best practices already researched and captured; waiting until Lucy opens the account).
- [ ] Waiting on Lucy: open Shopify and send the setup info, lock prices + the ~$70 pouch threshold, decide the fabric, OK a little early paid, commit to the batch-2 reorder timing.
- [ ] Operational: agree who answers customers (the 7-day no-reply flag); set up the Sportif inbox + Lauren + Klaviyo automations.
- [ ] Housekeeping: the auto weekly-review (dated 2026-06-21) at the very top of `memory.md` reintroduced em/en dashes; sweep when convenient.

---

## Session 010 (2026-06-17): Client deliverables for Lucy's first meeting, plain-English Q&A, and the Brand Value Plan

### What we did
- Built and sent Lucy (ahead of the first face-to-face) a set of on-brand PDFs: the market-and-insight PDF (`Sportif-Brand-and-Market-Insight.pdf`), the Brand Kit (`Sportif-Brand-Kit.pdf`), the Plan-to-September (`Sportif-Plan-to-September.pdf`), and the competitor product board as a PDF. All in the warm palette, written in a soft, additive voice (we are adding insight, not telling her what to do), since Lucy never asked for a market analysis (Hugo is the designer).
- Made a phone-friendly meeting guide for Hugo (`Sportif-Meeting-Guide.pdf`): his 7 questions only (vegan ankle strap, cotton pouch purpose, recycled/organic/hemp, email + client list, community, integrate @lucywayne__, name lock + trademark), plus Email and Community idea bullets and a "What is Klaviyo?" note box. Removed all of Claude's own extra questions per Hugo's request so they don't confuse him.
- Answered plain-English questions in chat: what Klaviyo is, the advantages of a Shopify website, and an assessment of Lucy's wholesale-first approach (verdict: smart fit for her, but run it wholesale-LED with a light DTC/email layer, because long-term brand equity is built direct).
- **Built the Brand Value Plan** (Hugo: "build long-term brand value is key, need a clear plan"). Six levers, each matched to Sportif: (1) instantly recognisable look + the pattern, (2) Lucy as the face, (3) stand for something + named sustainability, (4) community that feels ownership (colour/print vote), (5) own the customer via email/Shopify not just wholesale shelves, (6) consistency + quality + hold prices. Saved as `clients/sportif/brand-value-plan.md` (source of truth) and `clients/sportif/Sportif-Brand-Value-Plan.pdf` (on-brand, 4pp, verified by PNG render).

### What we learned / decided
- The throughline tying the wholesale answer to brand value: wholesale gets reach and credibility, but the email list and DTC store are the owned assets where value compounds. So the plan is wholesale-led for revenue, light DTC + email for equity.
- The pattern (Step 0 validation) is reframed not just as a product feature but as the most recognisable, least copyable BRAND asset, which is why it is worth validating.

### Open questions / next (carried, plus new)
- [ ] Fold Lucy's meeting answers (when they come back) into the brand docs: settle the three open calls (pattern feasibility, hero product, wholesale-vs-consumer), and lock the name once trademark clears.
- [ ] Carried from 009: validate the pattern bet (mockups + side-by-side panel + supplier confirmation), confirm custom colours are distinct from Kikiva/Your Reformer, build the tight Lucy-facing competitor snapshot, Session 008 Steps 11 and 12, and Lucy's Leelo quality-check notes when her order arrives.

---

## Session 009 (2026-06-16, same day, continued): Hands-on competitor product audit, big strategic correction, positioning sharpened to colour + pattern

### What we did
- Rewrote the research-derived sections of `brand.md` in plain language (Hugo flagged jargon; target is "a mum can read it").
- Built a visual **competitor product board** at `clients/sportif/competitor-analyses/competitor-product-board.html`: a single self-contained HTML file (warm-neutral themed, grouped by brand, with a plain-English "What this means for Sportif" note per brand). Data came from each brand's public Shopify `/products.json` (live prices) plus, crucially, Hugo's own hands-on screenshots of every named brand.
- Hugo photographed all 8 named brands (Avara, Move Active, Leelo, Kikiva, P.E Nation, Anine Bing, AJE, Your Reformer). I identified, renamed and embedded each shot (base64, downscaled via PIL) so the board always shows the photos. Folders under `competitor-analyses/product-images/<brand>/`. Board ended at ~100 products, ~5 MB.
- Started a **demand-signals tracker** (`competitor-analyses/demand-signals.md`): sold-out items and market finds.
- Wrote a Lucy-facing **positioning note** (`positioning-note-for-lucy.md`), a fuller **research-findings-and-options** synthesis (`research-findings-and-options.md`), and **patterned-band image prompts** (`patterned-bands-image-prompts.md`).
- Consolidation pass: updated `campaigns/launch-2026-09/synthesis-brief.md` and `brand.md` so the strategy reflects what we learned (colour + pattern + accessory-first + pouch).

### What we learned (the big strategic correction)
- **Sportif's exact launch products already exist at established rivals, in colour.** Booty bands: Move Active ($19.60 to $28) and Your Reformer ($29, multiple colour sets). Ankle straps: Avara ($39, neutral) and Kikiva ($29.99, pink and baby blue). This corrected the original desk-research belief that the colourful band/strap space was empty. Each correction came from Hugo actually browsing, not the data.
- **The real, unclaimed gap is PATTERN (Hugo's spot).** Every competitor's band, strap and weighted band is a flat solid colour. Patterns only appear on their grip socks. Nobody patterns a band. This plus a distinctive custom palette, accessory-first focus, a premium pouch and the founder story is the defensible wedge. "We are the colourful one" is not enough on its own.
- **The pouch is a sellable hero, not packaging.** Anine Bing's branded pouch ($249) and a card holder ($249) are sold out; ODE sells a woven pouch at $70. Branded pouches sell.
- **Towels are in demand** (Move Active mat and terry towels sold out). Caps + a small-to-large bag range are the standard low-risk accessory extension (Anine Bing, AJE, Move Active). NikeSKIMS sells a pilates grip sock at $50 (big players validating premium pilates accessories).
- **Price anchors:** booty bands ~$29, ankle straps $30 to $39, grip socks $9 to $39, towels $26 to $79, pouches $70 to $249.
- **Tooling and environment:** the public Shopify `/products.json` gives live prices and image URLs (use a small `?limit=` so web_fetch returns inline; big responses get saved to a temp file). Linked competitor images do NOT render reliably in a local HTML file, so embed images (we cannot download remote binaries, but Hugo's local screenshots embed fine via base64). macOS screenshot filenames contain a narrow no-break space, so rename by glob order, not by typing the name. Deletions are blocked in the mounted folder (overwrite instead). The Read tool cannot see brand-new files at the workspace path, so copy images into outputs to view them.

### Decisions
- Positioning sharpened and locked in the docs: the wedge is **distinctive custom palette + a pattern/texture on the band and strap (which nobody does) + accessory-first + pouch-as-hero + premium feel + founder story**, not "colour" alone.
- The full product board is now an internal research tool (too big to send Lucy as-is); a tight Lucy-facing snapshot is still to be built.
- Pattern is the new product bet to validate with Lucy and her supplier.

### Open questions / next
- [ ] Validate the pattern bet: generate the patterned-band concept mockups (`patterned-bands-image-prompts.md`), build a side-by-side panel vs competitors' flat-colour bands, and confirm with Lucy and her supplier that pattern or woven texture on the band is manufacturable.
- [ ] Confirm Lucy's custom colours are genuinely distinct from Kikiva's and Your Reformer's, and discuss whether the band, the strap, the pouch or a giftable set should be the hero.
- [ ] Build the tight Lucy-facing competitor snapshot (vs the big internal board).
- [ ] Still pending from Session 008: Step 11 (fold Sportif budget numbers into `docs/marketing-fundamentals.md` Part 8) and Step 12 (send Lucy the "where we are" email).
- [ ] Lucy's quality check: she ordered a Leelo item (Sculpt Wide Leg Pants + Mystery Grip Socks) to assess quality in person; add notes when it arrives.

---

## Session 008 (2026-06-16): Sportif research run executed end to end (all 5 passes, brand.md synthesized, Stage 3 brief drafted)

### What we did
- Resumed the post-Lucy research run. Re-tested connectivity: egress is open (Perplexity reachable), so the Session 007 blocker is cleared.
- Transcribed Lucy's questionnaire PDF into `clients/sportif/intake/lucy-responses.md` (verbatim Q1 to Q12 plus flags vs the SWOT).
- Ran ALL 5 research passes:
  - Pass 1 segment profile and Pass 2 all 8 competitor deep dives via sonar-deep-research.
  - Pass 3 brand references (sonar-pro), Pass 4 cultural-lane validation (sonar-reasoning-pro), Pass 5 budget benchmarks (sonar-pro).
- Synthesized into `clients/sportif/brand.md`: new Customer section, a Strategic positioning (cultural lane) lock, a competitor differentiation and whitespace read, a fuller Voice section, and launch budget bands.
- Drafted the Stage 3 synthesis brief at `clients/sportif/campaigns/launch-2026-09/synthesis-brief.md`: one creative direction ("Your colour. Your ritual.") with three angles to test.
- Swept all new files for em and en dashes (the research outputs carried them; the 3 canonical deliverables were already clean).
- Updated `RESEARCH-RUN-STATUS.md` to COMPLETE and ticked steps 1 to 10 in `post-lucy-research-plan.md`.

### What we learned
- **Big environment finding: in Cowork, background shell processes do NOT survive across separate tool calls.** The sandbox reaps them when a call returns, and each call caps at ~45s. So the CLAUDE.md workflow "launch sonar-deep-research with nohup and poll across calls" does NOT work here (it works on Hugo's Mac via Claude Code, a different environment). Verified with a controlled survival test.
- **Fix built: `scripts/pplx_async.py`.** Submits async deep-research jobs to Perplexity (which run server-side), persists request ids to a registry file on disk (disk survives across calls), and polls them in later short calls, writing each answer when COMPLETED. This is the reusable pattern for deep-research in Cowork. Registry/manifest for this run live in `clients/sportif/research/`.
- **Perplexity rate-limits async submissions (HTTP 429).** Submitting 9 jobs at once only let ~4 through; the rest needed staggered resubmits (sleeps of 12 to 18s). 3 of the 8 competitor jobs also FAILED server-side on the first attempt and were resubmitted cleanly. Build staggering and resubmit-on-fail into any future batch.
- **The cultural-lane verdict has a sharp caveat.** The macro pilates/morning-movement category is growing in AU through 2026, but the "pretty pastel pilates girl" aesthetic is visually saturated. The win is NOT another pastel band set; it is colour-as-signature plus accessory-as-hero plus a named ritual. No accessories-first design-led AU brand owns bands and straps yet (the Lululemon-owns-yoga-tights gap).
- **Every competitor profile flagged the same structural hole:** accessories are an afterthought (generic, white-labelled, merch). That is exactly Sportif's wedge. Founder-led and community content is table-stakes (Kikiva, PE Nation, AJE, Anine Bing all do it), so Lucy's visibility is necessary but not the differentiator.
- **Two competitor files were low-confidence** (Leelo Active, Avara Athletics; Your Reformer and Kikiva partly). Prices quoted there are inferred and should be validated by direct site checks before use.

### Decisions
- Ran all 8 competitors at deep-research depth (Hugo had waved off cost in Session 007). Kept full sonar-deep-research fidelity by switching execution to the submit/poll helper rather than downgrading to sonar-pro.
- Locked Sportif's positioning lane in `brand.md`: feminine, colour-led, affordable-luxury, accessory-first, ritual-anchored.
- Channel plan recommendation (for the Lucy call): Instagram Reels first as the proving ground, add TikTok once an angle wins, email from day one. Lean-to-mid budget envelope, not scale, given the 500-unit first run and wholesale-first model.

### Open questions / next
- [ ] Send Lucy the "where we are" summary email (Step 12): proposed positioning, channel-sequencing recommendation, budget envelope, next-call agenda. Not drafted yet.
- [ ] Optional Step 11: fold the Sportif AUD budget numbers into `docs/marketing-fundamentals.md` Part 8.
- [ ] Stage 4: pick the first production need from the winning angle and write the gpt-image-2 prompt(s). Use next week's pilates-instructor shoot as the real-motion source for the ritual angle.
- [ ] Validate the low-confidence competitor prices (Leelo, Avara, Kikiva, Your Reformer) by direct site check before quoting externally.
- [ ] Carry-over from Lucy's side: naming and trademark lock, platform-sequencing call, script-accent font, activewear-range timing.
- [ ] Consider documenting the `pplx_async.py` pattern in the workspace gotchas so future Cowork sessions use it by default.

---

## Session 007 — 2026-06-13 — Lucy's assets + questionnaire, brand.md populated, research queued (blocked on egress)

### What we did
- Processed 14 brand reference assets Lucy shared (Canva screenshots). Renamed them descriptively in `clients/sportif/assets/` (`01-moodboard.png` through `14-instagram-grid-mockup.png`).
- Pulled Lucy's Canva design via the Canva connector (design `DAHKXomW0Fk`). It is her personal catch-all and contains a private to-do list; extracted only brand-relevant content and set the rest aside. No Canva Brand Kit exists.
- Sampled exact brand colours. Confirmed primary blush peach `#F0CDB3` (Lucy's "Light Orange"), plus the FLOW tones: caramel `#C6926E`, terracotta `#833827`, chocolate `#2D1814`, linen `#F6EEE5`, type warm charcoal `#4A433C`.
- Lucy reviewed the BAHE FLOWLOOPS `FLOW.png` and said "I love this picture." Made it the visual anchor for launch creative.
- Wrote the visual half of `clients/sportif/brand.md`. Then Lucy's questionnaire arrived (`intake/SPORTIF_questionaire_response.pdf`) and we populated the full brand.md from her answers.
- Generated 3 Sportif image concepts via Pixa (nano-banana-2, ideogram-v3) as a test. NOTE: these were NOT gpt-image-2; flagged the engine mismatch to Hugo. The proven engine for the FLOW look is gpt-image-2.
- Walked Hugo through getting an OpenAI API key (separate billing from his ChatGPT sub) for gpt-image-2.

### What we learned (key facts from Lucy)
- Positioning is "affordable luxury", not pure luxury. Founder is Lucy Wayne (Sydney PT and stylist, has press).
- September launch is ACCESSORIES: Booty Bands + Vegan Ankle Strap, cotton pouch, custom colours. 500 units arriving this month. Apparel range is a later phase. Wholesale-first (AU this year, US next), Shopify.
- Font confirmed: Glacial Indifference. Primary colour `#f0cdb3`.
- Customer: women 18 to 45, early-morning pilates and walks, sustainable. Channels: Instagram Reels, TikTok, newsletters. Build content now, slow ramp to September.
- Competitors (8): PE Nation, AJE, Your Reformer, Move Active, Avara Athletics, Anine Bing, Leelo Active, Kikiva.
- Anti-reference: White Fox Boutique (tacky, lots of skin). Keep imagery tasteful, not skin-heavy.
- Naming and trademark still open on Lucy's side (domain + lawyer in progress). SPORTIF vs Le Sport Collectif / LSC unresolved.

### Decisions
- Run the post-Lucy research plan on ALL 8 competitors (Hugo waved off cost).
- brand.md narrative populated now; research layer to follow.

### Blocker
- Sandbox network egress blocked `api.perplexity.ai`, `api.openai.com`, and `pixa.com` (403 from proxy). Hugo then set Domain allowlist to "All domains", but the running sandbox had booted earlier, so it stayed blocked. The new policy only applies to a freshly booted sandbox, i.e. a NEW chat. Resume note: `clients/sportif/intake/RESEARCH-RUN-STATUS.md`.

### Open questions / next
- New chat: re-test connectivity, then run the 5 research passes (all 8 competitors), synthesize into brand.md, draft the Stage 3 launch brief at `clients/sportif/campaigns/launch-2026-09/synthesis-brief.md`.
- Naming/TM lock and platform sequencing need a call with Lucy.
- Send Lucy a "where we are" summary once research is in.
- Memory did NOT auto-load in Cowork this session. Until fixed, new sessions must be told to read `memory.md` + `brand.md` + the resume note.

---

## Weekly Review — 2026-05-31 (week of 2026-05-25)

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
- **Pilates is the dominant 2026 fitness cultural tailwind** — three years atop the ClassPass charts, 15M bookings, 66% YoY growth on reservations. Stronger than expected. A lead positional lever if Sportif's mix touches it.
- **Australian paid-media benchmarks are now documented:** Meta CPM ~$9.80 AUD (23% below US, 18% above UK), TikTok in AU ~30% cheaper than Meta with Health & Fitness as the cheapest vertical (~$6.50 AUD CPM), Sydney premium 20-50% in peaks, November $24.80 vs January $10.68 seasonality. Plan around Australian summer.
- **The Bala playbook is the proven template for design-led fitness accessories DTC** — multi-million brand built without paid marketing for years, design-as-jewelry, color/aesthetic-led, heavy UGC and influencer seeding. Sportif's reference template (not Gymshark or Alo).
- **Klaviyo is the clear default for ecom email** — 3.8x revenue per subscriber vs Mailchimp at $5K-contact scale, ecom automation included at $100/mo vs Mailchimp's $160/mo Premium tier.
- **Perplexity `sonar-deep-research` cannot run as a sync HTTP call** — long autonomous jobs get RemoteDisconnected by the gateway. Must use the async endpoint (`/async/chat/completions` + polling). Other models 400 there, so routing is automatic. `scripts/perplexity_search.py` now handles this transparently.
- **Stage 4 platform specs (current as of Session 006):**
  - **Seedance 2.0:** directorial prompt (Subject, Action, Environment, Camera, Style, Constraints), accepts text + up to 9 images + 3 video + 3 audio via `@image1/@video1/@audio1` syntax, 4-15s, 480p-1080p (+2K/4K upscale), strong physics, weak human biomechanics, unreliable audio (auto-generates regardless of prompt).
  - **gpt-image-2:** near-pixel-perfect multilingual in-image text (quote exactly, keep short), up to 4K, DOES NOT support transparent backgrounds (use gpt-image-1.5 or white-bg cutout), DO NOT set `input_fidelity` (errors), no API-level "thinking mode" param.
- **The self-improving prompt loop works as a methodology.** Closed-loop produce → generate → analyze → learn, with findings promoted back into reference docs. First worked example (BAHE FLOWLOOPS) shipped ~12 promoted findings in one session. This is now a workspace pattern, not a one-off.

### Open questions still unresolved

From Session 004 (carry-over, still open):
- [ ] `from __future__` annotations shim resilience for the video-analyzer skill on fresh clones (setup.sh re-clones from upstream and loses the fix).
- [ ] Python 3.10+ upgrade via Homebrew — would retire the shim need.
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
2. **Write `prompts/synthesis-creative-brief.md` (Stage 3) while waiting.** This is the bridge between Lucy's intake + Perplexity research and the Stage 4 production prompts. Template scaffold doesn't need Sportif specifics — it just needs the mode-aware (brand-first vs competitor-first) structure. Unblocks the rest of the pipeline for Sportif's launch content the moment her answers arrive. Estimated 1-2 hour focused task.
3. **Pick a Seedance reseller and write the first Stage 4 adapter.** Decision (fal.ai vs Pollo vs Wavespeed vs Dreamina direct) gates the adapter shape. Once chosen, the gpt-image-2 OR Seedance adapter (whichever Sportif's first content need points to from Lucy's Q12 answer) becomes the first end-to-end production prompt in the workspace. Pairs naturally with #2.

---

## Weekly Review — 2026-05-24 (week of 2026-05-18)

### Highlights
- **Workspace went from zero to fully scaffolded in a week.** Created `~/Desktop/hyperframes/`, upgraded Node to v22, cloned the three reference repos (official HyperFrames source, HeyGen launch video, Nate Herkai's 12-project student kit), spun up a starter project, and installed all 15 HyperFrames AI skills into `.agents/skills/`.
- **Got everything under version control and pushed to GitHub** — `OchoOcho88/ocho-frames` (private), first commit at 197 files / 2.7MB. Added a `setup.sh` so future clones can restore the ~940MB of `.gitignore`'d reference repos.
- **Built the organizational layer on top of the code** — added top-level `prompts/`, `recipes/`, and `skills/` folders with starter content, clear READMEs, and a documented distinction between project-scoped vs. workspace-scoped skills.
- **Set up automated institutional memory** — scheduled this weekly reflection task so the workspace gets reviewed every Sunday at 6pm without anyone having to remember to do it.

### Patterns I noticed
- **Local environment friction keeps showing up.** First the Node PATH fight (older Node winning over the new v22 install, needing a manual `~/.zshrc` override), then the sandboxed shell's inability to `git clone` directly into the Desktop mount. Tooling that touches macOS bridges/mounts needs a workaround mindset, not a "should just work" assumption.
- **API keys are the biggest unblocking dependency.** Three keys (OpenAI, HeyGen, soon Gemini) have been on the open-questions list across both sessions. Nothing real can be tested end-to-end until at least the first two are in place.
- **Conscious structure for AI-agent use.** Every choice this week — auto-loaded skills, bracketed prompt placeholders that force specificity, prompts vs. recipes vs. memory separation — was made with the assumption that an AI agent (not just a human) would be reading and using these files.

### Skills / knowledge gained
- HyperFrames is "video as code": HTML/CSS/JS rendered to MP4, deterministic, Apache 2.0 (no per-render fees, no seat caps), and frame-accurate seekable for libraries like GSAP — clear win over Remotion for AI-driven video work.
- The 15-skill HyperFrames ecosystem covers main + CLI + media preprocessing (Kokoro TTS, Whisper, u2net) + animation runtimes (GSAP, Anime.js, CSS, Lottie, Three.js, WAAPI) + conversion helpers.
- The catalog has 50+ pre-built blocks via `npx hyperframes add <block>` — checking the catalog first is faster than building from scratch.
- Skill scoping has two distinct modes: project-scoped (`<project>/.agents/skills/`, auto-loaded) vs. workspace-scoped (`skills/`, manually referenced).
- GitHub Pages is free only on public repos — keeping `ocho-frames` private + using Pages requires GitHub Pro ($4/mo) or flipping the repo to public when sharing.
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
1. **Unblock the workspace by collecting API keys.** OpenAI and HeyGen first — those two alone unlock the ability to actually test the starter project end-to-end. Until that happens, every other build task is theoretical.
2. **Install the video-analyzer skill and run the first real competitor analysis.** This is the proof that the prompt + skill + recipe framework delivers value, not just structure. It also feeds back into what HyperFrames work to prioritize.
3. **Customize the brand kit before producing any real videos.** Modern defaults are fine as a placeholder, but anything shipped this week with the default kit will need redoing later.

---

## Session 004 — 2026-05-26 — First successful video-analyzer run (+ Python 3.9 fix)

### What we did
- **Ran the video-analyzer skill end-to-end for the first time** — the open item flagged "first thing for session 004" in Session 003. Analyzed `examples/student-kit/video-projects/linear-promo-30s/final.mp4` (the Linear 30s promo from Nate Herkai's student kit).
- **Saved the report** to `outputs/video-analyses/student-kit-linear-promo-30s-2026-05-26.md` and prepended a small provenance header (source / date / tool / model) so each file in the competitive-intel library is self-documenting going forward.
- **Hit and fixed a Python-version blocker** before it could run (see below).

### What we learned
- **The skill is `disable-model-invocation: true`** — it is NOT in the Skill-tool list and can't be auto-invoked. You run it by calling the script directly: `python3 ~/.claude/skills/video-analyzer/scripts/analyze_video.py <video> [--prompt …] [--fps N] [--model …]`. Report → stdout, progress → stderr.
- **This Mac only has system Python 3.9.6** — no 3.10/3.11/3.12/3.13 anywhere on PATH, and `google-genai` (1.47.0) is installed only for 3.9. So the Homebrew upgrade deferred in Session 003 is still pending, and 3.9 is what we have to run on.
- **The script was incompatible with 3.9 out of the box.** It uses PEP-604 `float | None` annotations (lines for `build_video_part` / `analyze`) with no `from __future__ import annotations`, so 3.9 raised `TypeError` at function-definition time — before any upload. SKILL.md claims "Python 3.10+", which is why this surfaced.
- **The default model `gemini-3-flash-preview` works.** 2.9MB file → inline upload path (≤18MB). Two benign noises in stderr: the Python-3.9-EOL `FutureWarning` and a `thought_signature` "non-text parts" warning — text still returned cleanly.
- **Report quality was good and honest** — all 5 sections, accurate `MM:SS` scene breakdown, verbatim on-screen text, and it correctly reported "No speech detected / cinematic music + whooshes" instead of inventing a narrator (the anti-hallucination guardrails held).

### Decisions
- **Fixed the installed skill in place** by adding `from __future__ import annotations` to `~/.claude/skills/video-analyzer/scripts/analyze_video.py` (one line, behavior-preserving, works on 3.9 AND 3.10+). Chose this over a throwaway `/tmp` copy so the validation reflects the real skill and every future run on this machine just works.
- Used the skill's **default prompt and default model** for this first run (no `--prompt`/`--fps`/`--model` overrides) — wanted a clean baseline of stock behavior.

### Open questions / next steps
- [ ] **The `from __future__` fix is local-only and `setup.sh` will lose it.** `setup.sh` re-clones the skill from upstream (mikefutia/claude-vision) on fresh machines, which does NOT have the fix → a fresh clone on a 3.9 box will hit the same `TypeError`. Either (a) PR the one-liner upstream, or (b) have `setup.sh` re-apply it after install, or (c) just upgrade Python to 3.10+ (makes the shim unnecessary, though harmless to keep).
- [ ] **First *real competitor* analysis still untested.** This run was a student-kit teaching asset, not a competitor, and used the script directly — `prompts/competitor-analysis.md` (which routes output to `outputs/video-analyses/`) hasn't been exercised yet.
- [ ] Upgrade Python via Homebrew (`brew install python@3.13`) + reinstall google-genai for it — still from Session 003; would retire the 3.9 shim need.
- [ ] Carry-over from prior sessions: OpenAI + HeyGen keys, verify starter project `npm install && npm run dev`, brand-kit customization, repo-visibility/Pages decision.

### Session 004 addendum — architectural pivot (later in the same session)

After the test passed, Hugo shared the real end goal — this isn't a "competitor analyzer," it's a **creative-strategy pipeline**: ingest competitor content (video OR static) → extract patterns → synthesize a brief adapted to a *client's* brand → output production-ready prompts for AI media platforms (Seadance for video, ChatGPT Image 2.0 for static). That reframe changed the rest of the session from "run the test" to "design the pipeline."

**What we did (addendum):**
- Reviewed a YouTuber's 12-section marketing-conversion framework (Format / Hook / Audience / Pain / Angle / Product Intro / Proof / Beat-by-Beat / CTA / What Works / What's Weak / Steal-Worthy Patterns) — strictly better than the workspace's prior 7-section creative-pattern prompt for ad analysis.
- **Rewrote `prompts/competitor-analysis.md`** from a 7-section human-fill-in template into a 12-section `--prompt-file`-ready prompt. Folded the OLD prompt's visual-craft and audio-craft elements into Section 1 of the new one so the creative lens isn't lost. Added a "Critical rules" block (verbatim quotes, no invented narrators, label inferences, N/A allowed).
- **Updated `recipes/analyze-video-with-gemini.md`** Variations section with a real bash invocation for `--prompt-file prompts/competitor-analysis.md` (replaced the "still open" placeholder).
- **Wrote `docs/pipeline-architecture.md`** — the new source of truth for the full 5-stage pipeline. Locks decisions and lists open questions per stage.

**What we learned (addendum):**
- **Default 5-section skill output ≠ marketing analysis.** The YouTuber's 12-section output is a custom prompt, not the skill default. Two different lenses on the same video: default = "describe what's there"; custom = "explain why it converts." For ads work, marketing-conversion is the right lens.
- **The "What's next?" closing offer is a great UX pattern.** YouTuber's outputs end with offered next-steps. Generalizing this into a Stage 5 pipeline convention so every stage ends with offered next moves the user picks from.
- **The competitor-analysis workflow has 5 stages, not 1.** Stage 0 client brief → Stage 1 ingestion → Stage 2 pattern extraction (current 12-section prompt) → Stage 3 strategic synthesis → Stage 4 platform-specific production prompts. Only Stage 2 (for video) is built today.

**Decisions locked (addendum) — 4 pipeline-architecture decisions, all documented in `docs/pipeline-architecture.md`:**
1. **Client context lives in per-project brief files** at `projects/<client>/brief.md` (new top-level `projects/` folder, sibling of `my-projects/`).
2. **Static image analysis gets a sibling image-analyzer skill** — deferred to Session 005 for build.
3. **Pipeline shape: modular stages with "What's Next?" handoffs.** Stage 2 always runs; Stages 3-4 are user-triggered from offered options.
4. **Primary AI media platforms: Seadance (video) + ChatGPT Image 2.0 (static).** Runway / Higgsfield deferred but listed for future expansion.
5. **Stopped at architecture for Session 004** rather than start building Stages 0/3/4. The pivot was significant enough that locking the plan in writing > rushing into half-built scaffolding. Session 005 starts from a clean architectural map.

**Open questions / next steps (Session 005 entry point):**

Pipeline build queue:
- [ ] **Stage 0 — Set up `projects/` folder + `_template/brief.md`.** Smallest blocking dependency for everything else. Convention documented in `docs/pipeline-architecture.md`.
- [ ] **Stage 5 first half — add "What's Next?" closing block** to `prompts/competitor-analysis.md` so analysis outputs end with offered next moves.
- [ ] **End-to-end smoke test** — pick a real client, drop a competitor video into the project folder, run Stage 2 with the new 12-section prompt, validate the whole flow works. **(Supersedes the "first real competitor analysis still untested" item from earlier in this entry.)**
- [ ] **Research Seadance + ChatGPT Image 2.0 current prompt formats** before writing Stage 4 prompts. Their formats have evolved — old templates won't work.
- [ ] **Write Stage 3** (`prompts/synthesis-creative-brief.md`). Takes client brief + analyses → produces adapted creative direction.
- [ ] **Write Stage 4 prompts** (`prompts/production-seadance.md` + `prompts/production-chatgpt-image.md`). Each takes the synthesis brief → outputs a paste-ready platform prompt.
- [ ] **Add image-analyzer skill** for static-image competitor analysis (Stage 1 second path). Standalone build — likely its own session.

Per-stage design questions (full list in `docs/pipeline-architecture.md`):
- Stage 0: free-form vs. strictly structured `brief.md`? One per client or one per *campaign*?
- Stage 1: image-analyzer via Gemini API (script) vs. Claude native vision (chat-only)?
- Stage 3: single synthesis output vs. multiple creative directions?
- Stage 4: character-count caps for Seadance? Batch variations for A/B testing?
- Stage 5: hardcoded offers per stage vs. dynamically generated from prior output?

### Session 004 second addendum — Devil's Advocate pass + Stage 0 built + Sportif onboarded

After the architecture was documented, ran a Devil's Advocate pass (using the installed skill) to pressure-test the plan before committing more to it. Seven challenges raised. Five led to material changes; two held up (one we kept, one was minor).

**Devil's Advocate outcomes:**

| Challenge | Outcome |
|---|---|
| 1: Building scaffolding for clients you don't have yet? | **Resolved by reality:** Hugo HAS a real client — **Sportif**, fitness accessories, brand new company, launching September 2026. Needs brand identity, brand kit, and launch content for Instagram, TikTok, Facebook. No content or brand kit yet. Concrete deadline (~4 months) reshaped priorities. |
| 2: Is competitor-first pipeline ordering backwards? | **Pipeline now supports two modes:** brand-first (established clients) and competitor-first (net-new launches like Sportif). Picked per client, documented in client README. |
| 3: Stage 0 over-engineered for actual needs? | **Simplified.** Combined brand-kit + brand-identity into ONE `brand.md` file. Template now ~6 meaningful files instead of 12. Grow as needed. |
| 4: Platform lock-in to Seadance + ChatGPT Image is fragile? | **Adopted platform-agnostic structure.** Stage 4 split into `prompts/production-brief.md` (platform-agnostic intermediate format) + thin platform adapters at `prompts/adapters/<platform>.md`. Adapters can swap without touching the brief format. |
| 5: No quality-control / review checkpoint? | **Added Stage 5: Review & Iterate** as a real stage in the architecture. Feedback maps to a specific upstream stage and re-runs that stage. Per-campaign review notes file. |
| 6: Two-Claude workflow is more overhead than value? | **Kept by Hugo's choice** — he's used the pattern before successfully, and needs an explainer (Cowork advisor) for what Opus is producing in VS Code while he learns. Net positive for his learning curve. |
| 7: `projects/` vs. `my-projects/` collision waiting to happen? | **Renamed both:** `my-projects/` → `compositions/`, `projects/` → `clients/`. Updated 16 references across 12 files. |

**New: Pre-Stage 0 intake layer.** Hugo asked for a questionnaire he can email Sportif to gather brand intake data, plus a SWOT analysis template (with research-helper prompt) for his own strategic read. Built both. The questionnaire is what the client says; the SWOT is what Hugo concludes as the expert. Together they feed `brand.md`.

**What we built (advisor session, one-off exception to Opus-writes pattern):**

- **Renamed `my-projects/` → `compositions/`** (preserved content). Updated `setup.sh`, all READMEs, all prompts referencing the old path.
- **`clients/README.md`** — top-level explanation of the clients/ folder convention.
- **`clients/_template/`** with:
  - `README.md` — onboarding sequence for new clients
  - `brand.md` — combined brand kit + identity skeleton
  - `intake/questionnaire.md` — 10-question email-ready intake (~30 min for client to complete)
  - `intake/swot-analysis.md` — SWOT template with Sportif-style research-helper prompt
  - `products/_template-product.md` — one-per-SKU product skeleton
  - `campaigns/`, `competitor-analyses/`, `_archive/`, `assets/` empty folders with `.gitkeep`
- **`clients/sportif/`** populated as the first real client:
  - `README.md` — engagement status + onboarding checklist
  - `brand.md` — skeleton with known facts (name, category, launch date, platforms) + TBD fields tagged to questionnaire question numbers
  - `intake/questionnaire.md` — Sportif-customized, ready to email (placeholders for founder name + deadline)
  - `intake/swot-analysis.md` — Sportif-customized with research-helper prompt pre-filled for fitness accessories DTC, Sept 2026, Instagram/TikTok/Facebook
- **`docs/pipeline-architecture.md`** rewritten end-to-end to reflect all revised decisions: two modes, Pre-Stage-0 intake layer, simplified Stage 0, platform-agnostic Stage 4 with adapters, new Stage 5 Review & Iterate, renumbered Stage 6 "What's Next?" offer.
- **`.gitignore`** updated: `my-projects/` → `compositions/` reference fix, plus `clients/*/assets/*` ignored except `.gitkeep` and `.md` files (so client binary assets like logos/fonts don't bloat the repo).

**Decisions locked in this addendum:**
- **Folder rename:** `my-projects/` → `compositions/`, `projects/` (planned) → `clients/` (built).
- **Two pipeline modes:** brand-first vs competitor-first, chosen per client.
- **Simplified Stage 0:** combined `brand.md`, minimal starter, grow as needed.
- **Platform-agnostic Stage 4:** production-brief + thin adapters.
- **New Stage 5:** Review & Iterate.
- **Pre-Stage-0 intake layer** added (questionnaire + SWOT).
- **Sportif is the first real client.** Engagement at intake stage. Questionnaire ready to email.
- **One-off exception confirmed:** advisor built Stage 0 because hot context outweighed pattern purity. Resume Opus-writes from Session 005.

**Open questions / next steps (Session 005 entry point — revised):**

Sportif-driven:
- [ ] Customize Sportif's questionnaire (founder name, deadline date) and email it.
- [ ] Run the SWOT research-helper prompt (it's pre-filled — just paste into Claude). Populate Sportif's SWOT Opportunities + Threats from the research output.
- [ ] When questionnaire returns, populate `clients/sportif/brand.md` from answers + SWOT conclusions.

Pipeline build (in priority order):
- [ ] Add "What's Next?" closing block to `prompts/competitor-analysis.md` (Stage 6 — cheap, immediately useful).
- [ ] End-to-end smoke test with a real fitness-accessory competitor video for Sportif, save to `clients/sportif/competitor-analyses/`.
- [ ] Research Seadance + ChatGPT Image 2.0 current prompt formats (Stage 4 prerequisite).
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3, mode-aware).
- [ ] Write `prompts/production-brief.md` + first adapter (Seadance OR ChatGPT Image — pick whichever Sportif needs first).
- [ ] Add image-analyzer skill for static-image analysis (Stage 1 second path).

Carry-over:
- [ ] `from __future__` shim resilience (still applies — fresh clone via `setup.sh` loses it).
- [ ] Python 3.10+ upgrade via Homebrew — would retire the shim need.
- [ ] OpenAI + HeyGen keys + brand-kit customization + repo-visibility decision (from prior sessions).
- [x] ~~Rename `brand/brand-kit.md` to `brand/agency-brand-kit.md`~~ DONE (Session 004 cleanup). Path references updated across docs, prompts, and this file.

### Session 004 third addendum — voice rules + agency identity + Sportif onboarding email fully ready

The longest session yet. After Stage 0 was built, focus shifted from architecture to operationalizing the first real client engagement (Sportif) end-to-end. By session close, the entire onboarding email is ready to send to Lucy (the Sportif founder).

**What we did (third addendum):**

Voice and identity:
- **Locked a no-em-dash rule** as a hard, non-negotiable workspace voice rule. Em dashes are an AI tell and violate the friendly-professional-to-the-point voice. Documented in `brand/agency-brand-kit.md` with explicit punctuation substitutes (period, comma, colon, parens). The rule applies to ALL workspace copy: client emails, prompts, generated content, docs.
- **Locked agency identity:** Ochoproductions, domain ochoproductions.com, owner Hugo, contact hugo@ochoproductions.com. Captured in `brand/agency-brand-kit.md`. Logo, landing page, brand colors, typography all explicitly marked TBD (modern defaults are placeholders).
- **Renamed `brand/brand-kit.md` → `brand/agency-brand-kit.md`** to disambiguate the agency's own brand kit from client brand kits (which live at `clients/<client>/brand.md`). Six other files updated with the new path.
- **Em-dash sweep across 13 high-priority files** (intake questionnaires, SWOTs, brand templates, READMEs, the competitor-analysis prompt, the agency brand kit). Initial mechanical sed pass created some awkward fragments which we then rewrote thoughtfully (em dashes serve four different grammatical jobs and need context-appropriate replacements, not one mechanical substitution).
- **Updated `prompts/competitor-analysis.md` Critical Rules** to include "No em dashes" as an explicit rule, so any analysis Claude generates from this prompt inherits the rule.

Sportif onboarding (the real deliverable of the session):
- **Added Q12 (Timeline & rollout)** to both questionnaires (Sportif and template). Covers timeline cadence (single launch drop vs build-up), platform rollout (parallel vs sequenced), and an explicit "open to discuss" option that signals Hugo has ideas. Q11 trimmed to remove the now-redundant Platforms line.
- **Pre-filled questionnaire signoff** with "Kind regards, Hugo, hugo@ochoproductions.com" in both Sportif and template versions.
- **Wrote a warm intro email** for Lucy referencing the mutual connection (Lauren). Frames the no-fee engagement honestly: real portfolio work + practice on a live launch in exchange for word-of-mouth referrals IF the work delivers. Capital-IF used deliberately to signal the referral is conditional on quality.
- **Merged the intro into the Sportif questionnaire file** so it now reads as the complete email body (greeting through signoff). The workspace meta block stays at the top, separated by `---`, as Hugo-facing send instructions.
- **Subject line recommended:** "Lauren put me in touch about Sportif". Lauren's name is the social proof that drives the open rate; Hugo's name is redundant (it's in the sender field).
- **Added a P.S.** about sending work samples in a follow-up email. Replaced the cliché "our only limit is our imagination" with "whatever you can picture, we can build it" (same meaning, less AI-tell-y, more confident).
- **Offered Lucy three answer formats:** type the answers, share a Google Doc, or send WhatsApp voice memos. Voice memos flagged as usually the fastest. This dramatically lowers her friction (speaking is faster than typing 30 minutes of answers).

**Decisions locked in this addendum:**
- **No em dashes** is a hard rule, applies workspace-wide, no exceptions in client-facing or AI-generated copy.
- **Agency name is "Ochoproductions"** (no space). Email is hugo@ochoproductions.com.
- **Questionnaires are 12 questions** (was 11, added timeline/rollout).
- **Voice memo option** is part of the standard intake offering for every client, not just Sportif.
- **Subject line convention** for warm intros: lead with the mutual connection's name.

**Sportif: where we are at session close:**
- `clients/sportif/intake/questionnaire.md` is the complete email body, copy-pasteable.
- Hugo needs to: customize "[Founder name]" line (replace with Lucy), confirm the deadline date, then send.
- After sending: run the SWOT research-helper prompt while waiting for Lucy's response.
- Send a follow-up email with work samples (referenced in the P.S.).

**Open questions / next steps (Session 005 entry point — updated):**

Sportif (active):
- [ ] **Send the Sportif intake email to Lucy.** Subject: "Lauren put me in touch about Sportif". Body is the merged file at `clients/sportif/intake/questionnaire.md`. Customize the founder name placeholder before sending.
- [ ] **Send Hugo's work samples** in a separate follow-up email (the P.S. promised this).
- [ ] **Run the SWOT research helper** for Sportif while Lucy is filling in her questionnaire. Prompt is pre-filled at the bottom of `clients/sportif/intake/swot-analysis.md`.
- [ ] **Populate `clients/sportif/brand.md`** from Lucy's responses + SWOT conclusions when intake is done.
- [ ] **Run first competitor analyses** on competitors Lucy names in Q4, save to `clients/sportif/competitor-analyses/`.

Pipeline build (Session 005 priority order):
- [ ] Add "What's Next?" closing block to `prompts/competitor-analysis.md` (Stage 6, cheap, immediately useful).
- [ ] Research Seadance + ChatGPT Image 2.0 current prompt formats (Stage 4 prerequisite).
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3, mode-aware).
- [ ] Write `prompts/production-brief.md` + first adapter (Seadance or ChatGPT Image, pick based on Sportif's first content need).
- [ ] Add image-analyzer skill for static-image competitor analysis (Stage 1 second path).
- [ ] Build a recipe for transcribing voice memos to questionnaire format (Whisper is already installed per Session 001). Will be needed when Lucy sends voice memos back.

Workspace housekeeping (Session 005 or later):
- [ ] Wider em-dash sweep: `docs/pipeline-architecture.md`, top-level `README.md`, older starter prompts (csv-to-chart, pdf-to-summary, etc.), recipes, skills READMEs. None are client-facing this week so not urgent.
- [ ] `from __future__` shim resilience (still applies on fresh clones).
- [ ] Python 3.10+ upgrade via Homebrew.
- [ ] OpenAI + HeyGen keys.
- [ ] Repo-visibility decision for GitHub Pages.

**Working pattern for Session 005:**
Resume Opus-writes from here (advisor mode does brainstorming and reviews only). Cowork session opens with the Opus startup prompt that briefs Opus on the current state and the top priority.

---

## Session 003 — 2026-05-25 — video-analyzer skill installed, Gemini API key live

### What we did
- **Installed the video-analyzer Claude Code skill** at `~/.claude/skills/video-analyzer/` (from https://github.com/mikefutia/claude-vision by Mike Futia, MIT license)
  - Uses Gemini's vision API to "watch" videos and return structured markdown reports
  - Strong anti-hallucination guardrails (won't invent narrators/voiceovers)
  - 220KB skill, single Python script (`scripts/analyze_video.py`)
- **Installed Python dependency:** `google-genai` 1.47.0 via `pip3 install google-genai` (no `--break-system-packages` needed because Hugo's pip is old enough not to enforce PEP 668)
- **Created Gemini API key** on Google AI Studio, scoped to a new project called "Hyperframes" so usage/billing stays separated from other projects
- **Set `GEMINI_API_KEY` in `~/.zshrc`** — system-wide shell env var, available in every Terminal session
- **Verified no conflict with Altarize project:** Altarize Active Campaign (`~/Desktop/OrbitAll/Altarize Active Campaign`) uses ActiveCampaign, Railway, Supabase, Metabase, Claude, Resend, Perplexity — but NOT Gemini. Zero risk of the new hyperframes key being picked up by Altarize.
- **Documented the install in `skills/video-analyzer/README.md`** — the workspace has a pointer doc even though the actual skill lives outside the workspace (at `~/.claude/skills/`)
- **Updated `setup.sh`** to install the video-analyzer skill + google-genai automatically on fresh clones
- **Added `outputs/` folder** at workspace root for everything the AI/pipeline produces (vs `scripts/` which is for inputs):
  - `outputs/video-analyses/` — markdown reports from video-analyzer (tracked in git, builds a competitive intel library over time)
  - `outputs/downloads/` — competitor videos (gitignored — copyright + size)
  - `outputs/generated-images/` — AI image generations (gitignored)
  - `outputs/voiceovers/` — AI narration audio (gitignored)
  - Updated `prompts/competitor-analysis.md` to route output to `outputs/video-analyses/` instead of `scripts/`
  - Updated `README.md` to document the inputs-vs-outputs distinction

### What we learned
- **Two ways to manage API keys, each appropriate for different things:**
  - **Shell env var (`~/.zshrc`):** system-wide, always-on. Good for tools that expect env vars (like the video-analyzer skill). Bad for project-scoped secrets — anything else on your Mac can read it.
  - **Project `.env` file:** project-scoped, loaded on demand via `python-dotenv` (`load_dotenv()`) or `dotenv.config()` in Node. Good for keeping projects isolated. Standard best practice.
- **`load_dotenv()` default is NOT override.** By default, if the shell already has `MY_VAR` set, `load_dotenv()` will NOT replace it with the `.env` value. To force `.env` to win, use `load_dotenv(override=True)`. This is a subtle conflict source — flagged so future Altarize work (or any project adding `GEMINI_API_KEY` to its `.env`) doesn't get the wrong key.
- **Claude Code skills live at `~/.claude/skills/`**, separate from workspace `skills/` and project `.agents/skills/`. Three scopes:
  - **Cowork Personal skills** (Customize panel in Cowork) — across all Cowork sessions
  - **Claude Code skills** (`~/.claude/skills/`) — across all Claude Code sessions
  - **Workspace skills** (`~/Desktop/hyperframes/skills/`) — only when working in this workspace
  - **Project skills** (`<project>/.agents/skills/`) — only inside that project
- **Pip 21.x is OLD** but works fine for our purposes. Decided NOT to upgrade Python via Homebrew right now to avoid mid-flow disruption. Worth doing later as its own focused task: `brew install python@3.13` + reinstall google-genai for the new Python.
- **Gemini free tier limits:** 15 requests/min, 1,500 requests/day. Plenty for personal use.

### Decisions
- **Did NOT upgrade Python via Homebrew this session** — added to open questions for later. Reasoning: validating skill works on current setup first, then doing clean upgrade as its own session.
- **Did NOT touch Altarize's `load_dotenv()` calls** to add `override=True` — only an issue IF Altarize ever adds `GEMINI_API_KEY` to its `.env`, which it currently doesn't. Documented in open questions in case it ever does.
- **Skill installed at `~/.claude/skills/` (NOT in workspace `skills/`)** — required by the skill's hardcoded path. Workspace `skills/video-analyzer/README.md` is a pointer doc only.
- **Created separate Google AI Studio project** ("Hyperframes") for the new key so usage/billing tracks separately from the existing "Altarize analysis" project.

### Open questions / next steps
- [ ] **First test of video-analyzer skill** — pick a video file, run end-to-end, validate the output (this is the first thing for session 004)
- [ ] First competitor analysis using `prompts/competitor-analysis.md` + the new skill
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`) — still from session 001
- [ ] Get OpenAI API key and add to `.env` — still from session 001
- [ ] Get HeyGen API key and add to `.env` — still from session 001
- [ ] Find out where the "Altarize analysis" Gemini key (from Mar 2026) is actually being used — might be `~/Desktop/Altarize-Content-Pipeline/`, `~/Desktop/Altarize-Landscape-Analysis/`, or `~/Documents/Claude/Projects/Altarize Active Campaign/`. Not blocking — just curiosity.
- [ ] Upgrade Python via Homebrew (`brew install python@3.13`) once video-analyzer is validated working. Includes reinstalling google-genai for the new Python.
- [ ] If future Altarize work adds `GEMINI_API_KEY` to its `.env`, change `load_dotenv()` → `load_dotenv(override=True)` in all `tools/*.py` files
- [ ] Decide repo visibility for GitHub Pages (private requires Pro; public is free) — still from session 002
- [ ] Enable Pages in repo Settings → Pages once visibility decision is made — still from session 002

---

## Session 002 — 2026-05-23 — Framework additions + GitHub repo live

### What we did
- Added three new top-level folders to the workspace:
  - `prompts/` — reusable prompt templates with starter content for CSV→chart, PDF→summary, TikTok hook, product intro, and competitor analysis
  - `recipes/` — workflows we've proven and want to repeat, with a `_template.md` to copy from
  - `skills/` — workspace-level custom skills (different from the project-scoped `.agents/skills/`)
- Scheduled a weekly memory reflection task: every Sunday at 6pm, Claude reads `memory.md`, writes a "Weekly Review" section at the top, identifies patterns, and cleans up resolved open questions
- Documented the distinction between project-scoped vs workspace-scoped skills in `skills/README.md`
- Added `GEMINI_API_KEY` slot to `.env.example` for the incoming video-analyzer skill (uses Gemini Vision because Claude can't natively watch video yet)
- **Initialized git, made first commit (197 files, 2.7MB), pushed to GitHub at https://github.com/OchoOcho88/ocho-frames (private repo)**
- Created `setup.sh` so future clones can restore the ~940MB of reference repos that are excluded via `.gitignore`
- Added Contributing section to README + `index.html` + `docs/PAGES_SETUP.md` for when we enable GitHub Pages

### What we learned
- **Skills can be scoped two ways:**
  - Project-scoped (`my-projects/<project>/.agents/skills/`) — auto-loaded by AI agents when the project is opened, ideal for project-specific or framework-specific skills (this is where the 15 HyperFrames skills live)
  - Workspace-scoped (`skills/`) — manually referenced, useful for reusable third-party or custom skills like a video-analyzer skill for competitor research
- **Prompts ≠ Recipes ≠ Memory:**
  - Prompts are reusable *starting points* (templates to fill in)
  - Recipes are proven *workflows* (step-by-step sequences that produce known good outputs)
  - Memory is the *historical log* (what we did and why, ordered by time)
- **Competitor analysis is a use case worth investing in early.** Studying what works in the wild is faster than guessing — Hugo has a video-analyzer skill incoming that will plug into the workflow.

### Decisions
- Saved all five starter prompt templates with explicit `[bracket]` placeholders so they're impossible to use without filling in specifics
- Recipes folder starts empty (with template + README) — we only add recipes after a workflow has been proven 2–3 times
- Scheduled reflection runs Sundays at 6pm local time (cron: `0 18 * * 0`) — chosen so the new week starts Monday with clarity
- The reflection task only writes a "Weekly Review" header at the top — never deletes prior session entries (history matters)

### Open questions / next steps
- [ ] Install Hugo's incoming video-analyzer skill into `skills/` and document it
- [ ] First competitor analysis as a real test of the prompt + skill combo
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`) — still from session 001
- [ ] Get OpenAI API key and add to `.env` — still from session 001
- [ ] Get HeyGen API key and add to `.env` — still from session 001
- [ ] Get Gemini API key once we install the video-analyzer skill
- [ ] **Decide repo visibility for Pages:** GitHub Pages only works free on PUBLIC repos. To enable Pages on the current private repo, either (a) flip the repo to public when ready to share, or (b) upgrade to GitHub Pro ($4/mo)
- [ ] Enable Pages in repo Settings → Pages once the visibility decision is made (see `docs/PAGES_SETUP.md`)

---

## Session 001 — 2026-05-23 — Initial workspace setup

### What we did
- Created `~/Desktop/hyperframes/` as the workspace root
- Upgraded Node from v20.11.0 → v22.22.3 via Homebrew (`brew install node@22`)
  - Needed a manual PATH override in `~/.zshrc` because an older Node install was winning the PATH fight: `export PATH="/opt/homebrew/opt/node@22/bin:$PATH"`
- Cloned three reference repos:
  - `main-source/hyperframes/` — official HyperFrames source (heygen-com/hyperframes, 18.6k stars, ~122MB without LFS)
  - `examples/launch-video/` — HeyGen's actual launch video (~256MB)
  - `examples/student-kit/` — Nate Herkai's 12-project teaching kit with GSAP (~560MB)
- Initialized a starter project at `my-projects/starter/` via `npx hyperframes init`
- Installed all 15 HyperFrames AI skills into `my-projects/starter/.agents/skills/`
- Created folder structure: `assets/{audio,video,images,fonts}`, `brand/`, `scripts/`
- Created supporting files: `README.md`, this `memory.md`, `.env.example`, `.gitignore`, `brand/agency-brand-kit.md`

### What we learned
- **HyperFrames is "video as code"** — write HTML/CSS/JS, render to MP4. Same input = same output (deterministic). Built for AI agents to generate compositions because they're already fluent in HTML.
- **Why HyperFrames over Remotion:** Apache 2.0 open source (no per-render fees, no seat caps), pure HTML (no React build step), and library-clock animations like GSAP are seekable/frame-accurate.
- **The 15 skills cover everything:** main hyperframes, CLI, media preprocessing (TTS via Kokoro, Whisper transcription, background removal via u2net), animation runtimes (GSAP, Anime.js, CSS, Lottie, Three.js, WAAPI), and conversion helpers (Remotion-to-HF, website-to-HF).
- **The catalog has 50+ pre-built blocks** — `npx hyperframes add data-chart`, `flash-through-white`, `instagram-follow`, etc. Don't build from scratch what already exists.
- **Sandbox limitation:** Claude's sandboxed shell can't run `git clone` directly into the macOS Desktop mount because git's atomic file locking doesn't work over the bridge. Workaround: clone in sandbox `/tmp`, then `cp -R` to Desktop.

### Decisions
- Skipped Git LFS on the main repo (saved ~240MB of test baseline `.mp4` files we don't need for reference)
- Kept all three repos at `--depth 1` (latest commit only) to save space and time
- Brand kit set to modern default — will customize when Hugo has specifics
- HeyGen will be used for AI avatars + template videos (decide exact workflows once we start making content)
- Image model: OpenAI GPT Image 2.0 (will look up current API docs when we wire it up; not in Claude's May 2025 training data)

### Open questions / next steps
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`)
- [ ] Get OpenAI API key and add to `.env`
- [ ] Get HeyGen API key and add to `.env`
- [ ] Customize `brand/agency-brand-kit.md` with Hugo's actual colors, fonts, and voice
- [ ] Pick the first real project to build (suggestions: animated chart from a CSV, or a 15-second product intro)
- [ ] Decide on a naming convention for projects in `my-projects/` (e.g., `YYYY-MM-DD-project-name`?)

---

## Session 005 — 2026-05-28 to 2026-05-29 — Sportif onboarding fired, marketing fundamentals doc, Perplexity integration, post-Lucy trigger system

The longest session so far. The Sportif intake email went out, the Perplexity API got wired into the workspace, and the agency-wide marketing knowledge base was written. Two new auto-memory entries created in the memory directory so future Claude sessions auto-load Sportif context and the "Lucy responded" trigger.

### What we did

**Sportif intake fired (2026-05-28).**
- Confirmed the questionnaire at `clients/sportif/intake/questionnaire.md` was effectively ready (Lucy in greeting, signoff set, no bracketed placeholders left).
- Hugo sent the intake email to Lucy with subject "Lauren put me in touch about Sportif". Decision: kept the deadline open-ended ("at your earliest convenience so we stay on track for September") to match the no-fee/favor framing rather than create a transactional feel.
- Lucy responded same-day confirming she'll return answers in ~5 days. Expected return: ~2026-06-03.

**SWOT research and synthesis (Opportunities + Threats populated).**
- Ran 9 WebSearch queries: category dynamics, top brands, underserved segments, DTC failures, regulatory restrictions, Bala content strategy, insurgent brands, Pilates trend, Bala competitors.
- Wrote 8 Opportunities into `swot-analysis.md` (Pilates as cultural tailwind topping fitness charts three years running, the vanity-to-sanity positioning gap, underserved older-adult and women-specific niches, the Bala design-led playbook proven to work without paid ads for years, FitTok format alignment with accessories, sustainability as a real purchase signal in this category, clean-slate launch advantage).
- Wrote 10 Threats with the heaviest emphasis on the 2026 Meta/TikTok ad enforcement changes, paid-acquisition CPM inflation (Meta CPM up from $34 in 2021 to $57 in 2024), undercapitalization killing 45% of failed DTC brands, Amazon dupes destroying margins on commoditizable accessories, channel concentration risk across Meta/TikTok, and rising body-image backlash.
- Added 23 source links grouped by research bucket so every claim is traceable.
- Wrote a preliminary Strategic Synthesis (3 priorities, initially 4 then 5 don'ts, 4 ninety-day hypotheses) flagged as pre-questionnaire and to be hardened once Lucy responds.

**Critical nuance found on the Meta restriction (mid-session pivot).**
- Initial threat #1 read "Meta restricts fitness/wellness brands from optimizing on lower-funnel events and flags audiences whose metadata implies sensitive traits."
- Hugo asked for deeper explanation. WebFetched the AuditSocials and Accelerated Digital Media sources directly. Discovered the trigger is claim-making language, NOT product category. "Fitness accessories" is NOT automatically in Meta's Restricted Health and Wellness bucket. It enters that bucket only if the brand makes a specific health-outcome claim ("improves cardiovascular performance," "burns X calories," "reduces soreness by Y%").
- Rewrote threat #1 with the nuance, added "no specific health-outcome claims in product copy or ads" as a fifth do-not-do rule. Reframed the threat as a creative-positioning lever Sportif controls, not a fixed external constraint. This is now a hard rule across all Sportif creative.

**Built `clients/sportif/intake/swot-summary.md` as a pullable distillation.**
- Self-contained (jargon cheat sheet baked in for DTC, FitTok, UGC, CPM, CAGR, SKU, ACSM, lookalike audience, lower-funnel events, pre-launch waitlist).
- Headline takeaway in one sentence at the top.
- Top 3 opportunities, top 3 threats, 3 strategic priorities, 5 don'ts, hypotheses.
- Cross-link footer pointing back to the full SWOT, questionnaire, brand.md skeleton, and architecture doc.
- Designed for two uses: Hugo can pull it out as a screenshotable artifact, and future Claude sessions can use it as a quick reference without loading the full SWOT.

**Locked in: Sportif is Australian.**
- During the marketing-fundamentals doc scoping, Hugo confirmed Sportif is an Australian business. Previously the SWOT placeholder said "[TBD: assume UK/US until told otherwise]".
- Saved as auto-memory at `~/.claude/projects/-Users-hugobrizuela-Desktop-hyperframes/memory/sportif-australia.md` (first project auto-memory created in this workspace). Future Claude sessions will auto-load this context.
- Implications captured: AUD-denominated benchmarks, AEST/AEDT timing, the Australian fitness creator ecosystem (Kayla Itsines, Tammy Hembrow, Chloe Ting, Ashy Bines, Chontel Duncan, Lauren Simpson, plus TikTok's fastest-growing AU fitness creator Eddie Williams). Australian competitors to consider beyond what Lucy names: Tropeaka, Bondi Sands, Bared Footwear, Pillar Performance.

**Wrote `docs/marketing-fundamentals.md` (9,084 words, agency-wide knowledge base).**
- Scope confirmed via four scoping questions: thorough reference depth, Australia primary plus UK/US sections, AI stack woven through, one combined doc.
- 4 additional WebSearch queries for Australian Meta CPMs (~$9.80 AUD), Australian TikTok CPMs (~$4-10 AUD with Health & Fitness as the cheapest vertical at ~$6.50), Australian fitness creators by tier with AUD rates, and email tool comparison (Klaviyo wins for ecom at 3.8x revenue per subscriber vs Mailchimp).
- Nine parts: lay of the land (the five channels, the funnel, the flywheel, what changed since 2021), paid ads platform-by-platform (Meta auction mechanics, account structure, targeting, formats, the Restricted Health and Wellness trap recap; TikTok Spark Ads with AU benchmarks; brief Google and YouTube coverage), organic content per platform (Instagram Reels-first, TikTok FYP mechanics, the truth about FB organic, YouTube Shorts vs long-form, the repurposing system), email (why post-iOS-14 it's the most reliable channel, the five core flows, Klaviyo vs Mailchimp vs ConvertKit vs Beehiiv with AUD pricing, deliverability basics), creators (the four tiers with AU follower bands and rates, terminology decoded, top AU fitness creators by name, briefing template, compensation models, AI stack integration), metrics stack (all acronyms defined in one table, attribution challenges since iOS 14, post-purchase surveys as the affordable attribution layer, MER as the integrating metric), campaign structure (pre-launch/launch/sustain phasing), Sportif applied blueprint (four phases mapped to dates from now to September to year-end, KPIs per phase, three budget bands lean $5-10K/mid $15-30K/scale $50K+ AUD for launch month, channel-mix table across phases, AI stack integration per phase, risk register), and staying current (newsletters, podcasts, operators, signals your playbook needs updating).
- Zero em dashes (voice rule maintained throughout). Word count 9,084.

**Perplexity integration set up.**
- Honest discussion of Perplexity vs WebSearch tradeoffs. Decision: don't re-run SWOT/marketing-fundamentals (sufficient quality already), save Perplexity for Lucy's research where source quality matters most (AU industry reports, regional segment data).
- Hugo provided his API key. Initial path was `~/.zshrc` (matching the GEMINI_API_KEY video-analyzer pattern). Hugo redirected to project-scoped `.env` for security. Updated approach accordingly.
- Wrote `scripts/perplexity_search.py` (dependency-free Python helper that auto-loads `.env` from workspace root, supports all four models: sonar, sonar-pro, sonar-reasoning-pro, sonar-deep-research). Output to stdout, progress to stderr.
- Created `skills/perplexity-search/README.md` as a pointer doc with setup steps, model cheat sheet, usage examples, and cost guidance.
- Updated `.env.example` with the Perplexity slot and instructions.
- **Security incident caught:** Hugo pasted the real API key into `.env.example` (which is tracked in git). Caught before any commit. Cleaned up: created `.env` with the real key, restored `.env.example` to placeholder, verified `.gitignore` correctly excludes `.env`. Recommended rotation; Hugo rotated the key as the conservative move. Confirmed the new key authenticates with a small smoke test.

**Added "What's Next?" Section 13 to `prompts/competitor-analysis.md` (Stage 6 build).**
- New Section 13 instructs the model to end every competitor analysis with a numbered list of 3 to 4 specific next moves, each tied to something concrete from THIS analysis (a pattern name from Section 12, the hook from Section 2, a specific proof moment, the next competitor in the client list, etc.). Ends with the line "Or tell me something else you want."
- Includes a worked example using Sportif/Pilates language so future runs anchor on the right tone.
- Added a rule to the Critical Rules block: "Section 13 closing offer is required. Never end with Section 12."
- Updated `docs/pipeline-architecture.md` Stage 2 and Stage 6 statuses to reflect built state.

**Built the post-Lucy trigger system (the big institutional artifact).**
- Wrote `clients/sportif/intake/post-lucy-research-plan.md`. Contains: a 12-step to-do list for processing Lucy's responses end-to-end, 5 ready-to-run Perplexity passes (segment profile, per-competitor deep dives, brand-reference reverse-engineering, cultural lane validation, budget benchmarking) with exact bash commands and template prompts, save locations per output, estimated cost per pass (total ~$7 AUD), what's blocked vs unblocked, and the "why Perplexity for AU segment" rationale baked in so it's not lost.
- Saved auto-memory at `~/.claude/projects/-Users-hugobrizuela-Desktop-hyperframes/memory/sportif-post-lucy-trigger.md`. Lists trigger phrases ("Lucy has responded" / "Lucy's answers are in" / "the questionnaire is back" / etc.). When Hugo says one of those phrases in any future session, Claude auto-loads the plan and executes rather than improvising.
- Updated workspace MEMORY.md index at the auto-memory directory with both entries (sportif-australia + sportif-post-lucy-trigger). Em-dash sweep applied.
- Cross-linked `swot-summary.md`'s "Where everything lives" footer to point at the new plan. So anyone reading the SWOT lands on the research queue naturally.

### What we learned

- **The Meta Restricted Health and Wellness trigger is claim-making language, not product category.** "Stylish wrist weights" stays outside the bucket. "Wrist weights proven to boost cardio" goes inside. This makes the threat manageable rather than fatal, and aligns the creative-positioning answer with the cultural shift away from transformation language. Critical for Sportif copy.
- **Pilates is the dominant 2026 fitness cultural tailwind.** Topped global charts three years running, 15M ClassPass bookings, 66% YoY reservation growth. Stronger than expected. If Sportif's product mix touches Pilates at all, that becomes the lead positional lever.
- **Bala built a multi-million-dollar fitness accessories brand without paid marketing for years.** Their template (design-led product treated as jewelry, color/aesthetic, heavy UGC, influencer seeding) is the proven reference for new accessory brands. Confirmed via Shopify case study. Sportif's reference template should be Bala (not Gymshark or Alo, which are too big and apparel-led).
- **The default 2026 fitness-DTC ad playbook is broken.** TikTok bans before-and-after transformation imagery in paid regardless of claims. Meta's Restricted Health and Wellness bucket restricts lower-funnel optimization plus flags audiences/conversions with sensitive-trait metadata. Anyone selling "we'll just run Meta ads" is selling 2022 advice.
- **Klaviyo is the clear default for ecom email.** 3.8x revenue per subscriber vs Mailchimp at $5K-contact scale. Mailchimp requires $160/mo Premium for ecom automation; Klaviyo includes it at $100/mo.
- **Australian Meta CPM (~$9.80 AUD) runs 23% below US, 18% above UK.** TikTok in AU is 30% cheaper than Meta with Health & Fitness as the cheapest vertical (~$6.50 AUD CPM). Sydney CPM premium is 20-50% during peaks. Seasonality is significant: November AU CPM hits $24.80 vs January $10.68. Plan around Australian summer for Sportif.
- **Perplexity's edge over WebSearch is largest on AU and regional segment research.** It surfaces IBISWorld AU, Roy Morgan, Statista AU, ABS, Nielsen AU as primary sources where WebSearch returns US-centric SEO content. Cross-source synthesis with line-by-line citations. The advantage compounds in `sonar-deep-research` mode where it runs 30+ autonomous queries on a single segment question.
- **Project-scoped `.env` beats `~/.zshrc` for workspace-internal scripts.** The video-analyzer pattern was specific to skills installed at `~/.claude/skills/` (system-wide). For helpers that live inside the workspace, project-scoped `.env` is the correct security pattern. Established this clearly for any future API key.
- **API keys can leak through `.env.example` if you're not careful.** It's a tracked file. The placeholder pattern (`pplx-...`) needs to stay placeholder. Real keys go only in `.env` (gitignored). Caught a paste-mistake in this session and rotated the key. Process now clear for future keys.
- **Em dashes leak in when you're not paying attention.** Caught several in my own output across the session, especially in templated sections (link titles, table cells). Manual grep after every multi-edit is necessary. Workspace voice rule holds firm.

### Decisions

- **Sportif's intake deadline:** open-ended. No specific date in Lucy's email. Matches the no-fee/favor framing.
- **Sportif is Australian.** AUD benchmarks, AEST timing, AU creator landscape. Recorded as auto-memory so future sessions auto-load.
- **Sportif's chosen cultural lane:** not yet locked. Will be decided after Lucy's Q1, Q2, Q3, Q7, Q8 answers. Candidate lanes from the SWOT remain: Pilates, longevity, design-led, inclusive-fitness.
- **Meta and TikTok creative rule for Sportif:** no health-outcome claims in any copy. Lead with aesthetic, lifestyle, and function. This is hard rule, applies workspace-wide.
- **Perplexity integration:** project-scoped `.env`, not `~/.zshrc`. Helper at `scripts/perplexity_search.py` is dependency-free (no `python-dotenv` install needed).
- **Perplexity usage strategy:** don't re-run already-shipped research. Save Perplexity for Lucy's questionnaire processing where the source quality differential is largest.
- **Per-competitor Pass 2 not capped.** Run Perplexity sonar-deep-research on every competitor Lucy names in Q4. Judgment call applied at the time if she names 6+.
- **Post-Lucy trigger phrases:** "Lucy has responded" / "Lucy's answers are in" / "the questionnaire is back" / "Lucy sent the questionnaire back" / "we got Lucy's intake" all activate the queued research plan. Documented in auto-memory.
- **Section 13 "What's Next?" closing offer:** now mandatory for every competitor analysis output. Stage 6 of the pipeline is built for Stage 2 (design-only for the rest until they exist).
- **Marketing fundamentals doc** (`docs/marketing-fundamentals.md`) is the agency knowledge base, not a Sportif-specific doc. Part 8 IS Sportif-specific. Refresh structural Parts (1, 6, 7) less often than channel Parts (2, 3, 4, 5) which need updating ~every 6 months as platforms evolve.

### Open questions / next steps

**Top of queue for Session 006:**

1. **Research Seadance + ChatGPT Image 2.0 current prompt formats.** Stage 4 prerequisite. Use Perplexity sonar-deep-research now that it's wired in (prompt-engineering doc changes fast, Perplexity's source quality matters here). Output target: a reference doc at `docs/platform-prompt-formats.md` or similar that captures current spec for both, with examples, character limits, format quirks, and what's changed in the last 6 months. ~30-60 minute focused task.

2. **Write `prompts/synthesis-creative-brief.md`** (Stage 3, mode-aware brand-first vs competitor-first template). Template scaffold can be written without Lucy's specifics; the actual synthesis runs after her responses + Perplexity passes.

3. **Build voice-memo-to-questionnaire transcription recipe.** Whisper is already installed (Session 001). Likely needed when Lucy sends voice memos (one of the three answer formats we offered). Save at `recipes/transcribe-voice-memos.md`.

4. **Add image-analyzer skill (Stage 1 second path).** Static image competitor analysis. Standalone build, likely its own session.

**Sportif-active (waiting on Lucy):**

- [ ] Lucy returns questionnaire ~2026-06-03. Trigger phrase activates the queued plan at `clients/sportif/intake/post-lucy-research-plan.md`.
- [ ] Run the 5 Perplexity passes (~$7 AUD total).
- [ ] Populate `clients/sportif/brand.md` from responses + research.
- [ ] Draft Stage 3 synthesis brief at `clients/sportif/campaigns/launch-2026-09/synthesis-brief.md`.
- [ ] Update `docs/marketing-fundamentals.md` Part 8 budget bands with Sportif-specific AUD numbers.
- [ ] Send Lucy a "where we are" summary email after research is in.
- [ ] Hugo to send work-samples follow-up email (promised in intake P.S.).

**Workspace housekeeping (deferred, not urgent):**

- Wider em-dash sweep: `docs/pipeline-architecture.md` (still has em dashes in the Stage 6 example block), top-level `README.md`, older starter prompts (`csv-to-chart.md`, `pdf-to-summary.md`, etc.), recipes, skills READMEs.
- `from __future__ annotations` shim resilience for the video-analyzer skill on fresh clones. Either PR upstream, modify setup.sh to re-apply, or upgrade Python.
- Python 3.10+ upgrade via Homebrew. Would retire the shim need.
- OpenAI + HeyGen keys still pending (Session 001 carryover). HeyGen needed before any avatar work.
- Repo visibility decision for GitHub Pages (private requires Pro; public is free).
- The "Subject line convention" pattern from Session 004 (lead with mutual connection's name) worked for Lucy. Confirmed pattern. No action needed.

**Pipeline build queue (per architecture doc):**

- Stage 4 production-brief prompt + first adapter (Seadance or ChatGPT Image, pick based on Sportif's first content need from Lucy's Q12 timeline answer).
- Second Stage 4 adapter once first is proven.
- Stage 5 review-and-iterate workflow (design exists, no code yet; build when first synthesis brief gets reviewed by Hugo or Lucy).

### Two-Claude sync note

For the Cowork advisor catching up via this entry: the working pattern for Session 005 was Opus-writes (this session) with no advisor brainstorm needed mid-session. The post-Lucy trigger system means the advisor can also recognize trigger phrases when Hugo brings them up in advisor mode. Both sessions should now use the same auto-memory directory at `~/.claude/projects/-Users-hugobrizuela-Desktop-hyperframes/memory/` and the same MEMORY.md index. The plan file at `clients/sportif/intake/post-lucy-research-plan.md` is the single source of truth for what runs the moment Lucy responds.

---

## Session 006 (2026-05-29): Platform prompt-format research (Stage 4 prerequisite)

Short, focused session. Lucy had not responded yet (expected ~2026-06-03, no trigger phrase used), so the post-Lucy plan stayed parked. Executed the top Session 006 priority: researched current Seedance and GPT-4o image prompt formats and wrote the Stage 4 reference doc.

### What we did

**Wrote `docs/platform-prompt-formats.md` (the Stage 4 prerequisite).**
- Covers both primary platforms: Seedance (video) and GPT-4o image generation / gpt-image-1 (static).
- Per platform: at-a-glance spec table, prompt structure, length guidance, camera/motion vocab (Seedance) or text-rendering (gpt-image-1), style/quality modifiers (what helps vs what is noise), failure-mode table with fixes, supported parameters, one Sportif-shaped fitness-accessory worked example, and a "what changed in the last 90 days" section.
- Added a naming-reconciliation table at the top, a cross-platform cheat sheet, an "open items for Stage 4 build" section, and 21 cited sources. Confidence levels marked [official] vs [inferred] throughout.
- Em-dash AND en-dash swept clean (zero of both).

**Research method: deep-research failed, fell back to split sonar-pro.**
- Ran 3 `sonar-deep-research` calls (2 platforms + 1 retry). All 3 failed with `http.client.RemoteDisconnected: Remote end closed connection without response`. This is a gateway/timeout drop: the synchronous urllib call in `scripts/perplexity_search.py` (600s timeout) gets cut before deep-research finishes its long autonomous run. Consistent 3/3 failure, not transient.
- Pivoted to 4 `sonar-pro` calls (2 focused queries per platform: structure/params, then quality/failures/changes). All 4 completed cleanly and gave rich, well-cited output.
- Raw outputs preserved at `outputs/research/` (seedance-a/b.md, chatgpt-a/b.md) and referenced from the doc footer.

### What we learned

- **`sonar-deep-research` does not work through our current helper.** The synchronous POST gets dropped on the long-running deep-research job (RemoteDisconnected, no HTTP status). Until the script is hardened, deep-research is effectively unavailable via `scripts/perplexity_search.py`. The post-Lucy plan assumes deep-research for the 5 passes, so this needs a fix BEFORE Lucy responds (see open items). `sonar-pro` works fine.
- **Splitting one broad question into 2 focused `sonar-pro` queries is a good substitute for deep-research depth** and far more reliable. Cost stayed tiny.
- **Naming: "Seadance" is really Seedance (ByteDance), "ChatGPT Image 2.0" is really GPT-4o image gen / gpt-image-1 (OpenAI).** There is no product literally called "ChatGPT Image 2.0." Recorded in the doc's naming table so the workspace stops targeting the wrong names.
- **Both platforms reward natural-language prose over keyword stacks, one-primary-subject discipline, and iterative refinement.** Generic quality-stacker buzzwords ("8k, masterpiece, trending on artstation") are noise on both.
- **gpt-image-1's standout is accurate in-image text** (quote it exactly, keep it short). Seedance's standout is multi-shot narrative coherence in a single prompt ("Shot 1 / Shot 2 / Shot 3").
- **Watch for Seedance 2.0.** A Seed-site "seedance2_0" page reference surfaced but is not yet backed by official capability docs. If it goes live, the camera/multi-shot guidance needs a refresh.

### Decisions

- **Doc location and shape:** single combined reference at `docs/platform-prompt-formats.md` (not two files), matching how the architecture doc treats the two platforms together.
- **Research model:** `sonar-pro` split queries, given deep-research is broken via the helper. Did not burn more time retrying deep-research.
- **Worked examples honor the Sportif no-health-claims rule** (aesthetic/lifestyle/function only), so they double as Stage 4 pressure-test fixtures.
- **Cost:** ~14.7K total tokens across 4 sonar-pro calls, roughly $0.50 AUD. Well under the $2-3 AUD estimate because deep-research was abandoned (failed calls returned nothing billable).

### Open questions / next steps

**Newly surfaced (priority):**
- [x] ~~**Harden `scripts/perplexity_search.py` for deep-research BEFORE Lucy responds.**~~ RESOLVED in the first addendum of this same session. Script now auto-routes `sonar-deep-research` to Perplexity's async API (submit + poll) and adds retry-with-backoff to the sync path. Validated end-to-end (~40s, clean answer + 30 sources). The post-Lucy plan runs as written.
- [x] ~~**Confirm `gpt-image-1` live parameter set**~~ SUPERSEDED in the second addendum of this same session. `gpt-image-1` is no longer the target; `gpt-image-2` (snapshot `gpt-image-2-2026-04-21`, launched April 2026) is the live model and its parameters (size presets + custom, quality low/medium/high, output_format png/jpeg/webp, n) are captured in the rewritten `docs/platform-prompt-formats.md`. Live string confirmation against OpenAI API ref still pending (see "Carried" item below).
- [ ] **Pick the standard Seedance reseller** (fal.ai / Pollo / Wavespeed / Dreamina direct). Field names differ per host; the adapter should target one.

**Carried from Session 005 (still queued):**
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3 template, mode-aware).
- [ ] Build voice-memo-to-questionnaire transcription recipe (Whisper) at `recipes/transcribe-voice-memos.md`.
- [ ] Add image-analyzer skill (Stage 1 second path).
- [ ] Write Stage 4 adapters (`prompts/production-seadance.md`, `prompts/production-chatgpt-image.md`) now that the format spec exists. Pick first adapter from Lucy's Q12 timeline answer.
- [ ] Confirm gpt-image-2 live parameter strings against the OpenAI API reference before writing the adapter parameter block.

**Sportif-active (waiting on Lucy, ~2026-06-03):** unchanged from Session 005. Trigger phrase activates `clients/sportif/intake/post-lucy-research-plan.md`. The deep-research blocker noted above was FIXED later in this same session (see addendum).

### Session 006 addendum (same session): deep-research fixed + Seedance 2.0 discovered

**Fixed the deep-research blocker.** Hugo asked to fix the script immediately. Root cause: `sonar-deep-research` cannot run as a synchronous HTTP call (the long autonomous job gets dropped by the gateway, RemoteDisconnected). Fix: `scripts/perplexity_search.py` now auto-routes `sonar-deep-research` to Perplexity's async API (submit to `/async/chat/completions`, poll `/async/chat/completions/{id}` until COMPLETED), and added retry-with-backoff to the sync path for other models. Discovered the async endpoint ONLY accepts deep-research (other models 400 there), so routing is automatic, not a user flag (removed an initial `--async` flag that would always error).
- **Validated end-to-end:** a small deep-research query submitted, polled IN_PROGRESS x3, COMPLETED at ~40s, returned a clean answer plus 30 cited sources. Log/output preserved at `outputs/research/async-test.*`.
- Updated the post-Lucy plan with an operational note (deep-research now async, shows IN_PROGRESS, `>` redirects still clean). Updated auto-memory `perplexity-deep-research-broken.md` from "blocker" to "resolved / how it works."

**Seedance 2.0 has officially launched (new finding).** The validation deep-research run surfaced an official ByteDance Seed launch blog ("Official Launch of Seedance 2.0") plus a Seed 2.0 model page and 2.0-vs-Sora-2 comparisons. This corrects the sonar-pro reading in `docs/platform-prompt-formats.md`, which had only found an unconfirmed 2.0 page reference. Concrete proof of deep-research's source-quality edge over sonar-pro. Updated the platform doc's A8 and Part D to reflect the launch and flag that Part A (the 1.0 spec) needs a 2.0-focused refresh. The 1.0 spec stays valid as a baseline since 1.0 is still widely hosted.

**New next step (added):** run a `sonar-deep-research` pass on Seedance 2.0 prompt format and what changed vs 1.0, then refresh Part A of the platform doc. Now unblocked since deep-research works.

### Session 006 second addendum (same session): both platforms had shipped 2.0, doc rewritten

Hugo asked to research Seedance 2.0 AND "GPT Image 2.0." Ran 2 sonar-deep-research passes (via the now-working async path) plus 2 sonar-pro follow-ups for prompt mechanics. Both platforms turned out to have shipped major April 2026 flagships that the original doc completely missed. Rewrote `docs/platform-prompt-formats.md` to be 2.0-first.

**Seedance 2.0 (confirmed live, April 2026):** unified multimodal audio-video model (Dual-Branch Diffusion Transformer, ~4.5B params). Generates synchronized stereo audio (dialogue, SFX, music, phoneme-level lip-sync in 8+ languages) jointly with video. Accepts text + up to 9 images + 3 video + 3 audio as inputs via a new `@image1`/`@video1`/`@audio1` reference syntax (role-assigned in natural language, up to 12 assets). Directorial prompt format: Subject, Action, Environment, Camera, Style, Constraints. 4 to 15s, 480p/720p/1080p (+2K, 4K upscale), aspect 16:9/9:16/4:3/3:4/1:1/21:9. Strong physics. Editing/extension. 1.0 is now the legacy baseline (still hosted).

**GPT Image 2.0 IS REAL (Hugo was right).** The real model is `gpt-image-2` (API), snapshot `gpt-image-2-2026-04-21`, branded "ChatGPT Images 2.0," launched April 2026. Lineage: DALL-E 3 -> gpt-image-1 -> gpt-image-1.5 (late 2025) -> gpt-image-2. DALL-E 2/3 removed from the API 2026-05-12. New: near-pixel-perfect multilingual in-image text, up to 4K, better instruction following. Key gotchas captured in the doc: (1) NO "thinking mode" API parameter (it's ChatGPT-layer orchestration; use Responses API to plan); (2) gpt-image-2 does NOT support transparent backgrounds (regression vs gpt-image-1; use gpt-image-1.5 or white-bg-plus-cutout); (3) do not set `input_fidelity` (errors). Params: size presets + custom (multiples of 16, 655K to 8.29M px, aspect <3:1), quality low/medium/high, output_format png/jpeg/webp, n. Token-priced: ~$0.01 (low 1024) to ~$0.41 (high 4K) per image.

**Lesson reinforced:** deep-research caught two whole product generations that the sonar-pro round missed. Worth the cost when currency matters. Both completion bodies cut off mid-section at ~1.5-2.6K tokens though, so each needed a focused sonar-pro follow-up for the prompt mechanics. Pattern for future deep-research: expect a strong synthesis + sources but budget a follow-up for the long-tail detail.

**Stage 4 is now properly unblocked** with a current, 2.0-accurate format spec for both platforms. Open items live in Part D of the doc (pick resellers, confirm live param strings, transparent-asset path, which model tier Sportif starts on).

### Session 006 third addendum (same session): prompt-lab experiment, the self-improving loop, ran live

Hugo asked whether a closed produce -> generate -> analyze -> learn loop was a good idea. It was. Built `experiments/` (with a README explaining the loop and rigor rules) and ran the first experiment, `experiments/2026-05-29-bahe-flowloops/`, using a found competitor product (BAHE FLOWLOOPS LUXE, 3 flat fabric resistance loops) as a design-led Sportif stand-in. Hugo has live access to Seedance 2.0 and gpt-image-2 and generated everything; Claude wrote prompts and analyzed results (video via the Gemini video-analyzer skill, images via Claude vision since the image-analyzer skill is not built yet).

**Generated and analyzed:** image v1 (product flat-lay), image v2 (lifestyle in-use), image v3 (functional taut use), video v1 (text-only product clip), video v2 (reference-driven 15s logo reveal), and video-gpt (accidental: the v3 image prompt fed to Seedance text-to-video with no reference). All assets and per-asset analyses are in the experiment folder; the full record is in its iteration-log.md.

**~12 field-validated findings, all promoted into docs/platform-prompt-formats.md:**
- gpt-image-2 renders exact text reliably (confirmed 3x, including on busy lifestyle backgrounds).
- gpt-image-2 holds hand/feet anatomy when you add explicit anatomy constraints.
- gpt-image-2 treats "no clutter" as soft, needs hard constraints for pure product shots.
- RECIPE: to show real product use, name the exercise position + "stretched taut, clearly in use, not draped." No aesthetic penalty (v3 proved it; v2 had read as decorative).
- gpt-image-2 casting drifts across generations, specify it for consistency.
- gpt-image-2 does NOT support transparent backgrounds (use gpt-image-1.5 or white-bg cutout).
- Seedance renders SHORT invented wordmarks clean (the earlier "invented text garbles" fear was wrong; "FLOW" came out clean with no reference). Garble risk is longer/complex text.
- Seedance reproduces referenced text cleanly, and a finished hero reference OVERRIDES detailed shot direction (animate-the-poster vs cinematic-sequence tradeoff).
- Image-style prompts port to Seedance and still yield motion without beat direction.
- Single continuous shot avoids the mid-clip glitch (v2's multi-beat clip glitched at 5-7s; video-gpt single shot was smooth).
- Seedance human biomechanics are WEAK, specific equipment use looks awkward. Use @video1 motion reference, keep actions simple, or film real demos.
- Seedance audio is unreliable: it auto-generates regardless of the prompt, moderation BLOCKS specified music but PASSES auto-generated, and the prompt cannot force silence (UI toggle only). Plan music in post.
- Meta: the Gemini video-analyzer OVER-RATES motion (missed the glitch, praised the awkward exercise as "good form"). Judge motion and text with human eyes.

**Production workflow this points to (for Sportif):** gpt-image-2 for hero/lifestyle/product stills including text, Seedance for ambient motion and animate-the-hero clips, real footage or @video1 references for believable human exercise, music added in post. gpt-image-2 -> Seedance handoff (make the branded still, reference it in) preserves the wordmark.

**Process note caught and fixed:** mid-commit, found that gpt-image-v2.md and gpt-image-v3.md were never actually written (only pasted in chat) though analyses referenced them. Created both before committing so the record is accurate.

**Git:** committed as 4f8bbba and fast-forwarded onto `main`, pushed to origin/ocho-frames. 57 files, ~5,114 insertions. This commit also swept up the previously-uncommitted Session 005 deliverables (marketing-fundamentals, post-lucy-research-plan, swot-summary, Perplexity helper + skill). Session branch deleted. `.env` verified ignored, never staged; tree scanned for stray keys (clean). Decision: branch-per-session is fine for big/experimental work, but fast-forward to main promptly so the two-session memory.md sync stays current. Default to main for routine work.

### For the Cowork advisor (sync)
Everything above is on `main` and pushed, so a fresh pull is current. The big new artifacts to know about: `docs/platform-prompt-formats.md` (the 2.0 Stage 4 spec, now carrying all the live-tested findings) and `experiments/` (the self-improving prompt loop, with the BAHE FLOWLOOPS run as a worked example). Deep-research now works via async in `scripts/perplexity_search.py`, so the post-Lucy plan runs as written. Still waiting on Lucy (~2026-06-03).

---

<!-- Add new sessions ABOVE this line. Format:
## Session NNN — YYYY-MM-DD — One-line summary
### What we did
### What we learned
### Decisions
### Open questions / next steps
-->
