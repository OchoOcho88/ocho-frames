# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## CURRENT STATE (update this block every session, keep it to ~12 lines)

*Last updated: 2026-07-07 | Last session: 014 (Claude Code) | Working tree: committed clean | Git synced with GitHub (Session 014 pushed the backlog)*

- **Client: Sportif.** Strategy LOCKED: Lucy Wayne is the differentiator, parallel wholesale + DTC, one hub (sportifcollection.com.au + @sportifcollection + email). Launch September 2026; 500 band units due early July (may have already landed, confirm with Lucy).
- **Current Lucy-facing docs: exactly two PDFs**, `Sportif-Brand-Value-Plan.pdf` (strategy) + `Sportif-Launch-Plan.pdf` (operations). Everything else archived in `clients/sportif/_archive/superseded-pdfs-2026-07/`.
- **CRITICAL PATH: nowhere to sell the band.** Blocked on Lucy: open Shopify, lock prices + ~$70 pouch threshold, decide fabric, agree who answers customers. Bundled ask email is IN HUGO'S GMAIL DRAFTS (to lucy@lucywayne.com.au); he attaches the two PDFs and sends.
- **Image pipeline is LIVE (Stage 4 started).** OpenAI key in .env, gpt-image-2 working. Production pattern: generate text-free, overlay real Glacial Indifference via `scripts/overlay_wordmark.py`. Fonts at `brand/fonts/glacial-indifference/`. Prompts logged in `clients/sportif/image-prompts.md`. Iterate low quality in Cowork (45s cap), finals high quality in Claude Code.
- **Waiting on Lucy:** her pick of the three 4:5 Instagram hero concepts (v5 unboxed / v6 set / v7 flat, Hugo texting her); then a high-quality final render in Claude Code.
- **Next build steps once unblocked:** Shopify coming-soon page (research done), store build, Klaviyo flows (account to be created after Shopify), ambassador/instructor seeding shortlist (main growth engine, not started).
- **Also open:** trademark clearance (with lawyer), materials question (gates sustainability copy), Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins (switch to real font on next edit).

---

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
