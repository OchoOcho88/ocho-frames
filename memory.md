# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## CURRENT STATE (update this block every session, keep it to ~12 lines)

*Last updated: 2026-09-12 | Last session: 041 (Claude Code, CLOSED) | Working tree: committed clean | Git: pushed 2026-09-12 | Next: Check for Lucy's replies first (she is not on Gmail, Hugo pastes or screenshots them): the animated inspiration board email went out 2026-09-12 with four questions pending (Q-036), and the signature original is still wanted (Q-034). When her answers land, extend `scripts-local/build_inspiration_board_mock.py` to paste the layers in over about 34 frames at 140 ms, a 600px GIF for email and a 1080x1350 MP4 for Instagram. Everything else waiting is in the open loops that startup prints, the Fit Expo booth email (Q-027) at the top of them.*

- **The critical path is TRADEMARK, not Shopify (D-001, Q-002 parked).** Launch and go-to-market wait on Lucy's lawyer. Shopify, prices, the pouch threshold and the fabric are all blocked on her.
- **Lucy Wayne IS the differentiator** (`clients/sportif/brand.md`). Parallel wholesale plus DTC, one hub. Exactly two client PDFs, `Sportif-Brand-Value-Plan.pdf` and `Sportif-Launch-Plan.pdf`.
- **Brand colour is Pantone 162 C, screen `#FFBE9F` (D-051).** The old `#F0CDB3` is retired for new work; rendered back catalogue still to move (Q-013).
- **Product colours are measured (D-027):** LIGHT `#B8A080`, MEDIUM `#9D7459`, HEAVY `#6C4333`. Composite ONLY from `assets/Sportif_Bands/Bands_background_removed/colour-corrected/` (D-039). Product assets carry the real colour, never the brand palette (D-046); the brand-colour weave is a background only (D-045).
- **The weave is a brand asset (D-028):** tiles and plates at `clients/sportif/assets/textures/`, the texture source for everything, 2D or 3D. House tile build is `scripts-local/build_texture_weight_tiles.py` (D-047). The Instagram grid crops to 3:4, a centred 1012px column.
- **Generator rules (D-033, D-034, D-038).** Never let a generator draw the band large: big means shoot or composite the real cutout, small means generate and swap the label from the real photo. No generator touches Lucy's friend's photos.
- **Client writing rules (D-044, D-046).** Lucy is not the model in the email-02 photos, so never "you" about the person in frame. Bands are named by weight, never "blush". "Show me" and "pick one" are different requests: show the thing with a recommendation attached.
- **Handle OFF on Instagram assets (D-018), ON for Fit Expo booth assets (Q-028).**
- **Protocol and voice (D-035, D-054).** `startup.py` and `closeout.py --commit` ARE the session, because CLAUDE.md is not auto-loaded in Cowork. No em or en dashes anywhere; close-out refuses to commit on a hit.
- **Where the detail lives.** `DECISIONS.md`, `OPEN-QUESTIONS.md` (dormant loops parked `[p]`, `open --parked`), `docs/gotchas.md`, `memory-archive.md`, all via `python3 scripts/memory_tools.py`.

---
## Session 041 (2026-09-12, Claude Code): The token diet, Q-037 done in five moves

Client: Ochoproductions
Tags: ochoproductions, memory-system, token-diet, startup, closeout, memory-tools, claude-md, housekeeping

**Done.** All five Q-037 moves in order, nothing else touched. (1) `memory_tools.py open --brief` prints one line per loop, the first sentence capped at 160 characters; `startup.py` uses it and the footer says where the full rows are. (2) Q-001 to Q-010 parked with `[p]` in `OPEN-QUESTIONS.md` (eight rows, two were already resolved); `memory_tools.py` hides them unless `--parked` and `reconcile` skips them. Q-002, the trademark gate, is parked too, but the first CURRENT STATE bullet still carries it. (3) "Tools and gotchas" and the PDF venv recipe moved to `docs/gotchas.md`, grouped by environment, with three S040 learnings that belonged there; startup names the file in its own section and never prints it; CLAUDE.md rewritten around the protocol and the conventions. (4) The "read the top session entry" step dropped from CLAUDE.md and `/startup`; the handoff line rewritten to three sentences. (5) Five-heading template in `docs/memory-system.md` (v2.1 note, em dashes swept out); `closeout.py` warns past 500 words, on a missing heading, and past three handoff sentences. Its commit trailer now names the current model. Then, on Hugo's call after the first close-out, the 13 CURRENT STATE bullets were cut to 10, each pointing at its D-number instead of restating it, and the session closed out a second time.

**Measured** (chars divided by 4, tiktoken is not installed):

| | before | after |
|---|---|---|
| startup print | 4,709 | 2,090 (final, clean tree) |
| of which open loops | 2,845 | 588 |
| of which CURRENT STATE | 1,144 | 722 (10 bullets) |
| CLAUDE.md, paid every turn | 2,810 | 1,289 |
| close-out entry | 1,106 (741 words) | 670 (430 words, this entry) |

**Learned.**
- After the five moves startup still sat at about 2,500 because the 13 CURRENT STATE bullets were 1,091 tokens on their own. Cutting them to 10 D-number pointers was the second half of the saving; the numbers above are the final ones.
- A first-sentence cap needs a floor. "THE 3D BAND." says nothing, so the brief keeps taking sentences until the line passes 80 characters.
- Size caps warn rather than block (D-037), otherwise they get bypassed.

**Decided.** D-054, the five rules as standing policy.

**Open.** Q-037 resolved, nothing new opened. The five-weekly-reviews warning is gone: on Hugo's call the 2026-07-26 review moved to `memory-archive.md` (third close-out). Q-026 parked on Hugo's call (fourth close-out): waiting on Lucy since 27 August, unpark when she answers. Everything else is in the loops startup prints.

**Next.** Check for Lucy's replies on the inspiration board (Q-036) and the signature original (Q-034); the Fit Expo booth email (Q-027) is still owed.

---
## Session 040 (2026-09-12, Claude Code): Lucy asks for an animated inspiration board, and a mock goes back the same day

Client: Sportif
Tags: sportif, lucy, inspiration-board, stop-motion, mock, signature, email, gmail, pillow

**Q-035 answered by Lucy herself.** She forwarded SABO's "Tropic Muse" marketing email (a stop-motion cork board GIF) and asked "do you happen to know how to do something like this inspiration board?". Hugo's read, correct: can we make a stop-motion loop for Sportif. That is the next job.

**The reference was measured, not eyeballed.** Hugo screen-recorded the GIF (two full loops, `clients/sportif/inspiration-board/reference-sabo-tropic-muse-screenrec.mov`, gitignored). A frame-difference pass over every frame gave the spec in `reference-notes.md`: 4.8 s loop, about 34 frames at roughly 140 ms each (about 7 fps, uniform), empty board held 0.3 s, four big frames for the fabric laying down, then one or two items a frame, full board held 0.2 s, hard cut back to empty. No easing, no slides; each item simply exists in the next frame. Staging: board in a white frame leaning on a pale wall, sunglasses in the foreground that never move, a collection-name caption under the board on every frame.

**A final-frame mock, real assets only.** `scripts-local/build_inspiration_board_mock.py` (Pillow) builds a 1200x1500 board from what the workspace already holds: the seamless weave tiles as the fabric layer (tiled at 0.2 scale so the pitch matches the band cutouts; the plates at native scale read as rope), the three colour-corrected band cutouts hanging from pins, a Pantone 162 C chip plus LIGHT, MEDIUM and HEAVY chips in the measured band colours down the right edge SABO style, the master mark on a card, polaroids (three of Lucy from her Instagram screenshots, two of her friend from the gym set, one Canva pick), a note card with her signature, a placeholder caption in Glacial Italic, and a band lying on the table in front. Cork is procedural. Three passes: v1 (weave too magnified, cork blotchy, a polaroid over two chips), v2 (Hugo's three edits: band centred, Lucy polaroids added, signature card), v3 (her real signature, from a 156x70 crop Hugo screenshotted from her email and dropped in the folder; the script lifts the ink off the paper and tints it chocolate). No generator touched anything, so D-038 is clean. Caption, weave scale, output and signature path are environment overrides (D-050).

**Email sent 2026-09-12** on her thread with the v3 mock attached, draft at `inspiration-board/email-to-lucy-2026-09-12.md`. Two calls by Hugo shaped it: the first draft offered her a choice between a real shoot and a computer build, and he cut that ("just tell her I can do it, and here is a reference I made up for her"), and the mock went in the same send as the questions rather than after them. Four questions remain for her: where it will live, what the board is about, what goes on it, whether it carries words. Recorded as D-053.

**Learned.**
- Hugo is not on Gmail. Two empty searches for an email he had open in another client. The Gmail connector is not his client mailbox; Lucy's mail arrives as pasted text, screenshots, or files dropped in the client folder. Saved as an auto-memory so no session repeats it.
- macOS puts a narrow no-break space before am and pm in screenshot and screen recording names. A pasted path fails on `cp`; match with a glob (`*12.02.43*`) or `Path.glob` instead.
- A screen recording of a GIF is enough to recover its frame timing: extract every frame, threshold the mean frame difference, and the change list gives the hold times and the loop period directly.
- A close-up plate tiled at its own scale reads as rope, not fabric. The seamless tile scaled so the weave pitch matches the product cutout in the same frame is what reads as the same material.
- Images pasted into the chat cannot be saved to disk from here. Ask for the file in the folder.

**Decided:** D-053 (a client "can you do this" gets a yes, a mock from her own assets, and short answerable questions; no menu of methods).

**Open:** Q-036 (her four answers, then the loop build: same script pasting the layers in over about 34 frames, 600px GIF for email and 1080x1350 MP4 for Instagram), Q-034 (the signature original is still wanted; the crop is fine for a card, not for a write-on), Q-027 (the booth email, still owed), and every loop carried in CURRENT STATE.

---
## Session 039 (2026-09-11, Claude Code): Lucy picks Pantone 162 C, the brand colour moves, and two emails go out

Client: Sportif
Tags: sportif, lucy, brand-colour, pantone, logo, master-mark, collection-grid, pdf, glacial-indifference, weasyprint, email, housekeeping

**Housekeeping first.** The 2026-09-07 weekly review had been written into memory.md but never committed; committed it. Cleared the stale `.git/HEAD.lock` and 33 orphaned `tmp_obj` files left by the S038 Cowork commit with `git gc --prune=now`. The startup flag on `RESUME-NOTE.md` was a false positive: the note was rewritten in S033 but still mentions "Session 013" as history, and the check matches the first "Session N" anywhere. Reworded the line. The "Lucy has responded" auto-memory also fired on a routine email; its research plan finished in June, so the memory was rewritten to say so.

**Q-033 closed: the brand colour is Pantone 162 C (D-051).** Lucy replied 2026-09-11 that her packaging printer, New Directions, matched her Canva `#f0cdb3` to Pantone 162 C as the closest print colour, and asked for the brand colour to become that Pantone. Screen hex is Pantone's own `#FFBE9F`. The weave tiles she is posting measure `#FFC09F`, an invisible difference, so nothing delivered was reissued. Forward sources updated: `brand.md`, `voice-guidelines.md`, `brand-value-plan.md` (client cut checked, synced date bumped, no content change needed), the synthesis brief, and eight build and generation scripts. Left on the old peach on purpose: the two scripts that reproduce comparisons already sent to her, the three HyperFrames compositions, and all rendered media, which join Q-013.

**Both client PDFs rebuilt, and moved onto the real font.** The Mac had no weasyprint: `/usr/bin/python3` cannot load Homebrew's pango, so it now lives in `.venvs/pdf` on Homebrew Python 3.11 (recipe in CLAUDE.md). Body AND titles are Glacial Indifference now: Lora is not on the Mac, and `brand.md` puts headlines in Glacial anyway. Glacial reads about 10 percent smaller than Poppins at the same size, so reading sizes were scaled up; page counts held at 4 and 5. Fixed three faults in the Launch Plan diagram along the way: the loop arrow landed on the "A little paid" pill and "it becomes" sat under its own arrowhead (both there since the first build), and "powered by Shopify" came out clipped, because opacity on SVG text makes weasyprint clip the line. Worth knowing: only the Launch Plan shows the peach at all; the Brand Value Plan defines `--peach` and never uses it. Not resent to Lucy.

**Logos (D-052).** First recoloured her existing peach files (`recolour_logos_162c.py`, a per-pixel projection that keeps anti-aliased edges, originals untouched). Hugo then spotted that her logo files have no "collection", which has been the master mark since D-017. Rebuilt the SPORTIF / rule / collection logo at 2000x2000 with `build_master_mark_logos.py`, which imports the house lockup helpers rather than copying them. Compared the house lockup against a reproduction of her own Canva artwork; Hugo picked her artwork, which matches her 500px original within a pixel. Hugo then asked to double check the font: a per-letter shape match against her artwork scored Glacial Indifference Regular 0.82, ahead of Avenir 0.76, Poppins 0.75, Futura 0.67 and Glacial Bold 0.61, so our file and hers are the same face and weight. Also corrected the stale `brand/fonts/README.md`.

**Collection grid reissued in 162 C.** `build_collection_grid.py` gained `SPORTIF_BG`, `SPORTIF_OUT` and `SPORTIF_SUFFIX` overrides (D-050). Rebuilt in the OLD peach first and it matched the posted August files pixel for pixel, so the new set differs only in colour. New set in `Sportif_Collection/grid-pantone-162c/`, August set untouched. Q-011 closed: she signed off by posting it.

**Two emails sent.** (1) The brand colour reply, 6 attachments (both collection logos, three grid tiles, preview). Hugo cut the monogram and swatch from it, softened the Canva ask into a suggestion, and added a thank you plus "let me know what we want to work on next" (Q-035). (2) A new thread offering an animated version of the handwritten "Lucy Wayne" on her new email signature, asking for the original file or the font name (Q-034). Hugo cut "It is so you" before sending, as familiarity he has not earned yet; saved as a feedback memory.

**Learned.**
- When a client colour comes from a printer, screen follows print: use the Pantone's own sRGB value, not an eyeballed chip.
- Before changing one variable in a delivered build, reproduce the delivered file byte for byte first. It turns "only the colour changed" from a claim into a fact.
- A whole-logo overlay cannot tell fonts apart at 500px (one pixel of drift halves the overlap); a per-letter shape match against lookalike fonts can.
- Emails for Hugo: praise the work, never claim to know the client, and suggest rather than instruct.

**Decided:** D-051 (Pantone 162 C, `#FFBE9F`), D-052 (logo files follow her artwork). **Deferred by Hugo:** the Fit Expo booth email (Q-027).

**Open:** Q-034 (animated signature, waiting on her), Q-035 (her answer on what next), Q-013 now also covers moving rendered media to the new peach, and every loop carried in CURRENT STATE.

---
## Weekly Review, 2026-09-07 (week of 2026-08-31)

Three sessions this week (036 on 08-31, 037 running from 036 across midnight into 09-01, and 038 on 09-03), all in Cowork, all driven by Hugo. The shape of the week: one client thread answered, shipped and re-answered with a new question underneath it; one full day of infrastructure that made the workspace lighter, faster to start and correctly dated for the first time; and, after three weeks of being carried, the 3D band finally produced the right shape. Nothing new was generated for its own sake. Every asset built this week was either a direct answer to Lucy or a diagnostic to settle an argument, and two of the week's three biggest results came from Hugo overturning something already written down.

### Highlights
- **The 3D band is a loop (D-048).** Run 1 came back as four flat straps and a floating plaque, and the first diagnosis blamed the prompt. Hugo pushed back that Tripo had used the photographs, and he was right: every band photo in the workspace shows the band pressed flat, so the hole is never visible and a flattened loop from above is a strap. Run 2, fed one gpt-image-2 image of the band lying open as an oval, returned a closed loop rendered six ways. One variable, proven in both directions in one evening, and the shoot list at `products/band-3d-shoot-list.md` was validated before a frame was shot. What remains is the real photograph and a clean run without the invented peach, the pouch bag and the 2M triangles.
- **Q-029 closed and Q-024 closed, and the real-product-colour position held under pressure (D-046).** Lucy loves the weave tiles and wants to post them. She asked to see them in her brand colour; three directions were built and measured, and Hugo declined the change on the grounds that a close-up of the fabric at that scale is a colour promise the customer must receive. Then she replied asking for the TYPE in her logo peach, not the plates, which is exactly the outcome that keeps the plates honest. The peach type costs about a quarter of the contrast (LIGHT 2.47:1 cream against 1.86:1 peach) and the existing warm halo at 1.55x buys it back on all three.
- **The workspace lost 1.4GB and gained a correct clock (S037).** memory.md went from 164KB to 81KB with CURRENT STATE rewritten as 13 live bullets (Q-021 closed), 30 commits pushed from the Mac (Q-022 closed), 227MB of raw Tripo GLBs stripped from all 104 commits with `git filter-repo` and gitignored going forward (Q-030 opened and closed), three cloned reference repos deleted, and the whole folder 3.4GB to 2.0GB. Under all that, a real bug: the container runs UTC and Hugo is UTC+10, so every morning session before 10am thought it was yesterday. All four scripts now pin today to `Australia/Sydney`.
- **The close-out harness caught its own author.** The timezone patch orphaned six callers in `memory_tools.py` and left one line calling itself; `closeout.py` saw the traceback and refused to commit. Built in S033 for exactly this, and this is the first time it stopped an infrastructure change that would otherwise have shipped broken.

### Patterns I noticed
- **Hugo's eye and Hugo's pushback overturned the written record five times in three sessions, and every one was right.** The tint call on the weave tiles, the thin weight line, the prompt diagnosis on Tripo, the "show me" versus "pick one" distinction, and the reasoning behind sending both peach sets in one email. This is now the fourth consecutive review where the same pattern holds. The workspace's role is increasingly to measure and to build the test, and Hugo's is to judge; the arrangement works and should not be argued with.
- **Render it at the size it will be seen.** The thumbnail test decided the weight line (Regular vanished at 128px while reading fine at 1080), and the grid mockup answered Lucy's sizing question faster than a paragraph would have. Same family as last week's "check the asset against its destination, not the surface it was made on", now with a repeatable move attached.
- **The tool's own label is not a measurement, and this week it bit twice in the same session.** `git count-objects` reported 391MB of "garbage" and gc recovered 87MB; the GLBs were 225MB on disk and about 103MB in the pack. The same shape as last week's underexposed cutouts and the olive tile: read the number the way the tool defines it, then measure the thing you actually care about.
- **"Show me" and "pick one" are different requests (D-046).** The first reply to Lucy declined the colour change and did not show her, which answers a question she did not ask. Fixed in ten minutes with one comparison image and a recommendation attached. Hugo then generalised it in S038: front-load every version in one send so the client can answer and use the work off the same email. Two client emails this week were built on that rule.
- **Every closed question opened a sharper one.** Q-029 closed and Q-033 (which peach is the logo peach) opened in its place, because her Pantone chip contradicts two of her own files. Q-024 closed and became the brand-colour ask. The Tripo shape problem closed and became a photography problem. The board is not getting shorter; it is getting more specific, which is the better of the two.

### Skills / knowledge gained
- **A mesher can only build what the references show.** Pressed-flat product photos are strap photos. For any closed-loop object the reference must show the hole: relaxed oval, camera 30 to 45 degrees down and off to one side, one object in frame, plain smooth surface, geometry shots in shade rather than the D-026 sun rule, which is for colour.
- **Instagram profile grid crops to 3:4 and shows a centred 1012px column;** anything for the grid must keep its lockup inside that. The house build now sits at 0.76 of canvas width and clears by 96px each side.
- **Glacial Indifference Regular does not survive a 128px thumbnail on a light plate; Bold with its own halo does (D-047).** One number scales the lockup and every blur and shadow scales with it.
- **Peach type on the weave plates:** cream to peach drops contrast about 25 percent on all three weights; a 1.55x halo lift restores legibility without touching the plate. `build_texture_weight_tiles.py` now takes `SPORTIF_TYPE_COL`, `SPORTIF_HALO` and `SPORTIF_OUT` as environment overrides, defaults reproduce the delivered set byte for byte.
- **Pantone 162 C is roughly `#FFC0A0`, and it is not `#F0CDB3`.** Two of Lucy's own files and her intake questionnaire agree on the latter. When a client-supplied colour contradicts the client's own artwork, stop and ask rather than apply, because the answer sets `brand.md` line 105.
- **Git weight lives in the pack, not on disk.** Float-heavy binaries like GLB compress well; PNG does not. Across history this repo is 295MB PNG, 209MB PSD, and that is the real work, so 472MB is the floor. `git filter-repo` plus a force push is the clean way to remove a class of file from history; gitignore the run folder and keep the final deliverable folder trackable.
- **Cowork has no GitHub credentials** (confirmed by trying), so pushing is permanently a Mac job. `rm` is blocked in the mount but `mv` is not, still the workaround for stranded `.git/*.lock` files.
- **Containers run UTC.** Any script that stamps a date needs a pinned local timezone; `today_local()` is the shared helper and the pre-push hook inherits it.
- **TheFitExpo Los Angeles 2027 is listed for 23 to 24 January**, not February as Lucy's intake says. If that is her show the print runway is three weeks shorter than assumed.

### Open questions still unresolved
**Resolved (by a later session this week):**
- [x] ~~Q-024: Lucy's reply on the weave close-up concept~~ RESOLVED Session 036: she loves it and wants to post it; the reply carried the sizing ask (answered with a grid mockup) and the brand-colour ask (declined, D-046).
- [x] ~~Q-029: Lucy's answer on the weave tile colour~~ RESOLVED Session 038: she wants the lockup TYPE in her logo peach, not the plates. Real product colour holds. Replaced by Q-033.
- [x] ~~Q-021: memory.md hygiene pass~~ RESOLVED Session 037: CURRENT STATE 41KB to 13 bullets, 70 retired bullets and 6 older reviews to `memory-archive.md`, check passes clean.
- [x] ~~Q-022: push the local commits from the Mac~~ RESOLVED Session 037: 30 commits pushed. Cowork cannot push at all, so this stays a Mac job permanently.
- [x] ~~Q-030: raw Tripo GLBs in the repo~~ opened and RESOLVED in Session 037: gitignored under `**/3d-band/runs-in/`, stripped from all history, force pushed.
- Note: Session 038 is the most recent session and carries its open loops in prose rather than checkboxes, so there is nothing in it to flip. Q-033 was opened there and no later session exists.

**Still open, opened this week:**
- [ ] **Q-033: which peach is the logo peach.** Lucy's Pantone 162 C chip (about `#FFC0A0`) against `#F0CDB3` from her own logo file, her swatch and her intake. Both postable sets are already in her hands. Her answer rewrites `brand.md` line 105 and the reissue is one command. She is back Thursday 10 September.
- [ ] **Q-016 (the 3D band), now reduced to one photograph.** Shape is proven (D-048). Take the shot per `products/band-3d-shoot-list.md`, run Tripo once with the real image, then decimate, apply the weave plates as material, set real-world scale and origin at the base, and export GLB at about 4MB for Shopify. First thing next session.
- [ ] **Q-027 has a date problem attached.** TheFitExpo LA looks like 23 to 24 January 2027, not February. Confirm the show and the dates with Lucy in the booth email, alongside panel dimensions and bleed.

**Still open, carried from before:**
- [ ] **Q-027: the Fit Expo booth posters.** Still blocked on panel dimensions and bleed, still owed an email that was promised in writing on 08-27, and now possibly three weeks shorter on runway. Check the Canva stock licence covers print and event display in the same message.
- [ ] **Q-028: the handle rule.** `DRAW_HANDLE=True` for booth assets, off for Instagram. One line; confirm it back to Lucy in the booth email.
- [ ] **Q-026: Lucy's pick between the three email-02 treatments** (as-is, terracotta room, weave room), sent 08-27. The other seven are deliberately unbuilt until she answers.
- [ ] **Q-025: the shot 01 colourway test.** MEDIUM then HEAVY, then compare all three. Prediction: HEAVY sinks into the dark floor, MEDIUM is the recommendation.
- [ ] **Q-023: photograph the band DROPPED on a floor.** White sheet, direct sun, D-026. Can share a sitting with the Q-016 geometry shot, which is the same band on a similar surface in different light.
- [ ] **Q-017: Gemini egress from Cowork**; **Q-019: poster 2 re-run**; **Q-020: dedicated label close-ups** (also shootable in the same sitting); **Q-013: back-catalogue pass to the SPORTIF / rule / collection mark**; **Q-014: Hugo's Photoshop reference** for the burned-in wordmark.
- [ ] **Colourway strips, range card and wholesale line sheet.** Unblocked by the measured colours three weeks ago, still unbuilt.
- [ ] **Q-001: standalone waitlist capture page + 3-email welcome flow.** Top unbuilt item in nine separate sessions. Needs neither Lucy nor the trademark.
- [ ] **Q-010: high-quality band-swap renders in a native Mac terminal**, then finalise and send email-03.
- [ ] **Lucy's older picks:** Q-011 (collection grid colourway), Q-006 (Content Creation Strategy reaction, gates Phase 2), Q-004 (music-bed pacing), Q-003 (incentive A/B/C). Fold into the booth email.
- [ ] **Q-008: Photoshop cutout of the ball hero**; **Q-005: Canva Pro** brand kit and folder share; **Q-002: trademark clearance**, still the critical-path gate on Lucy's lawyer's clock.
- [ ] Carried: ambassador/instructor seeding shortlist (twelfth week, needs nothing from anyone), film the unboxing, ElevenLabs API key, Shopify store, materials question, Stage 3 synthesis template, PDF generators still on Poppins.

### Suggested focus for next week
1. **One shooting session that closes three loops (Q-016, Q-023, Q-020).** The 3D band now needs exactly one photograph, and it is the same band on a similar white surface as the dropped-band shot and the label close-ups. Geometry shot in shade as an open oval, then step into direct sun for the dropped band and the labels per D-026. Twenty minutes with the phone, then one Tripo run with the real image. If the mesh is clean, finish the GLB; if it lumps, the Blender loop is the fallback and the decision is made the same day rather than carried a fourth week.
2. **Send the Fit Expo booth email before Lucy is back on Thursday, so it is waiting for her.** It has been owed since 08-27 and the January date correction makes it urgent rather than overdue. Ask for the show confirmation and dates, panel dimensions and bleed, confirm the handle goes back on for booth assets (Q-028), check the Canva licence for print and event display, and fold in the four older picks (Q-011, Q-006, Q-004, Q-003). One message has beaten five every time it has been tried.
3. **When Q-033 lands, reissue the tiles the same day and then build the colourway strips, range card and line sheet on the settled peach.** The reissue is one environment variable and one command. The commercial assets have been unblocked for three weeks and have never had a settled primary brand colour to be built against; once she names the peach they do, and the measured band colours plus the tight parallel trios from shoot 5 are already the source.

---
## Weekly Review, 2026-08-31 (week of 2026-08-24)

Two sessions this week (034 on 08-26 and 035 on 08-27), both in Cowork, both driven by Hugo, back to back on consecutive days and then nothing for four days. Smaller count than last week, but the character changed: less generating, more measuring, and for the first time in a long while things actually LEFT the building. Two client emails went to Lucy in two days, and Q-012, which had been sitting packed and unsent since 08-17 and was the number one focus of the last two reviews, is finally closed. The week's real work was Hugo learning Photoshop properly and, in the middle of that, inventing a treatment that is better than anything the scripts have produced.

### Highlights
- **The weave room, and Hugo went ROUND the obstacle instead of tuning against it.** Told that the peach grade was capped because her skin and the studio wall both sit near hue 25 degrees, he opened Photoshop and separated the person from the room, which is the one move that removes the collision entirely. Verified rather than assumed: her average brightness 53.4% before and 53.4% after, no halo at the edge. On that split he built a terracotta `#833827` fill at Overlay 60%, measured safe, then held the band's own weave to the wall with Blend If so it sits behind the barre and rings. Recipe and PSDs at `email-02-social/photoshop/`. It is the best thing produced this week and he built it himself.
- **Lucy's marks were MEASURED onto the assets, not eyeballed.** Four phone photos of her pen marks were matched to the real files with SIFT plus a RANSAC homography (81 to 210 inliers), warped into asset pixel space and differenced until only the pen remained. Three of the four then needed a documented nudge, for Instagram's 260px story chrome and for a ceiling beam that enters the type footprint at y370. Built into `created/v3/`, method and numbers at `email-02-social/lucy-marks-2026-08-26/README.md`. See D-041.
- **A colour fault was found in EVERY band cutout in the workspace (D-039).** All of them about a stop underexposed against the D-027 measured values: LIGHT 47% value against 72%, MEDIUM 37% against 62%, HEAVY 24% against 42%, saturation down about a third across the board. Invisible on the white shooting sheet, ruinous on a dark gym floor, where the band turns to putty. Corrected copies at `assets/Sportif_Bands/Bands_background_removed/colour-corrected/`, and that folder is now the only one to composite from. Caught because one weave tile read olive.
- **Two emails sent in two days, and reading Lucy's 21 Aug message properly surfaced three things nobody had flagged.** The weave tiles went out on 08-26 as a complete three-colourway grid row; the email-02 v3 batch went out on 08-27 with 12 attachments. Underneath it: the pilates picture is going to the **Fit Expo booth**, which is PRINT and everything we hold is 1080px (Q-027); Lucy has handed us the **handle rule**, off for Instagram and on for booth assets (Q-028); and she is expecting the **3D band**, which has not been started (Q-016). Three live obligations that had been sitting unread in an email for five days.

### Patterns I noticed
- **A fault that is invisible on the surface you author on can be fatal on the surface you deliver to, and that same shape showed up three separate times this week.** The cutout underexposure is undetectable on white and ruinous on a dark floor. The 1024px weave tile is clean at feed size and will seam on a 1920 story. And 1080px is fine on Instagram and nowhere near a printed booth panel. Different problems, one lesson: check the asset against its destination, not against the surface it was made on.
- **Measurement kept overturning the intuitive answer, and it did it in both directions.** The composite looked wrong and both of us blamed the shadow; measured, the shadow was the second most accurate thing in the frame (16 levels of floor darkening against 30 for the real rope handles) and the actual tell was TIDINESS. The light tile looked olive and turned out to be exactly on hue and saturation, just a stop dark. A hue-based skin mask sounded like the rescue for the grade and selected 91% of the frame because the wall qualifies as skin. Same move as the last two weeks; it is now the default on any contested question.
- **Hugo's eye is the deciding gate and it was right every time this week.** He called both failed grades on sight and named them exactly ("washed out and lifeless", then "fake tan"), and the measurements agreed afterwards. He declined the offer to auto-cut the other seven photos, on the grounds that Lucy has not agreed to the look yet, which is correct. And his consent instinct on Lucy's friend's photos (D-038) stands even though the workflow he designed around it turned out not to be needed.
- **Two errors cancelling is not a method.** His first composite happened to read at roughly the right brightness because the band was too dark and the gym should have darkened it. Value cancelled; saturation did not, which is why it read as gaffer tape rather than sand. Correct the asset first, then adjust deliberately.
- **The client queue moved, and immediately grew.** Two emails out, one long-carried item closed, and three new waits opened in their place (Q-026, Q-027, Q-028). Sending clears the backlog and starts the clock; it does not empty the board.

### Skills / knowledge gained
- **Client pen marks on a phone photo can be turned into exact asset coordinates.** SIFT features plus a RANSAC homography maps a photo of a screen back into the asset's own pixel space; difference the warped photo against the original and only the pen survives. This replaces guessing at "put it about here" for good.
- **On these photos, more peach and tanned skin are the same slider (D-042, D-043).** Skin and the studio wall both sit near hue 25 degrees, so any warm push lands on both, and a hue-based skin mask cannot separate them. That caps the whole grading approach; the corrected grade at `scripts-local/sportif_grade.py` carries both dead ends written into the file, and the v4 set is parked.
- **Black type beats white on terracotta `#833827`, 6.8:1 against 2.1:1**, because terracotta is a mid tone at 43% luminance. Worth checking rather than assuming on any mid-tone brand fill.
- **Tile versus plate is a size decision:** the 1024px seamless tile holds at feed size, seams on a 1920 story, so stories take the large single-crop plate.
- **Gamma beats gain for tone matching**, because it preserves black and white and cannot clip a highlight. Used to land each weave plate's mean on its D-027 value.
- **The staging trap (D-040):** our cutouts are catalogue poses, flat and square-cut, and composited into a candid photo they read pasted even when light, shadow and colour are all correct. Fix in Photoshop with a small Warp; fix properly by photographing the band actually dropped (Q-023).
- **Always apply `ImageOps.exif_transpose` before describing an iPhone photo.** Three of five filenames were wrong because a contact sheet skipped it; "standing rack full length" was actually her seated on a BOSU.
- **Photoshop specifics now on record:** Select Subject plus Select and Mask with Shift Edge -10% gives a clean cutout with no white rim (verified, edge within 6 levels of interior); Adobe removed the 3D toolset, so `Filter > Vanishing Point` is the nearest equivalent for placing an object on a plane; a sideways label on a horizontal band is correct, only a mirrored one is wrong, and rotating never mirrors.
- **Two writing rules for Lucy-facing work:** she is NOT the model in the email-02 photos, they are her Canva picks, so never write "you" about the person in frame; and "blush" cannot be used for the MEDIUM band, because Blush Peach `#F0CDB3` is the primary brand colour, so bands are referred to by weight.

### Open questions still unresolved
**Resolved (by a later session this week):**
- [x] ~~Q-012: SEND the email-02 v2 batch to Lucy~~ RESOLVED Session 035: sent 2026-08-27 as v3 with Lucy's measured marks applied, 12 attachments. Carried in three consecutive weekly reviews before it moved.
- Note: Session 035 is the most recent session and no later session exists, so its own open loops (Q-026, Q-027, Q-028) could not be resolved by anything. Session 034's three items (Q-023, Q-024, Q-025) are all still genuinely open; S035 went to the email-02 socials rather than the placement job, so it touched none of them.

**Still open, opened this week:**
- [ ] **Q-027: the Fit Expo booth posters. Highest-priority item in the workspace.** Lucy wants the pilates picture on a PRINTED booth panel and everything we hold is 1080px. Not a redo (the build script takes a different canvas), but BLOCKED on panel dimensions and bleed from her or the expo organisers, and Hugo owes her that email, promised in writing on 08-27. Also check the Canva stock licence covers print and event display before anyone pays for panels.
- [ ] **Q-028: apply the handle rule.** `@sportifcollection` OFF for Instagram (D-018 holds), ON for booth assets, because those travel without the account name attached. One-line change, `DRAW_HANDLE=True`. Confirm it back to Lucy in the booth email so it is on the record.
- [ ] **Q-026: Lucy's pick between the three treatments** (as-is, terracotta room, weave room), sent 08-27. The other seven are deliberately not built until she answers. `rembg` is on the Mac if she says yes; the duo shot has two people and may need Hugo's hand.
- [ ] **Q-025: the shot 01 colourway test.** Hugo rebuilds shot 01 with MEDIUM then HEAVY, then all three compare. Prediction from the contrast numbers: every surface Lucy picked is dark, so LIGHT separates by about 42 points, MEDIUM by 31, HEAVY by only 12 and will sink into the floor. Medium is the recommendation.
- [ ] **Q-024: Lucy's reply on the weave close-up concept**, sent 08-26 with the three tiles attached.
- [ ] **Q-023: photograph the band actually DROPPED on a floor.** White surface, direct sun, house setup (D-026). Ten minutes of shooting removes the warping step from all five placements and gives a real in-use asset for the range card and line sheet. Highest leverage item on the placement job.

**Still open, carried from before:**
- [ ] **Q-016: the 3D band**, now promised to Lucy in writing, which changes it from a nice-to-have to a commitment. Tripo account exists, plates ready, weave plates are the material source, Blender loop is the fallback.
- [ ] **Q-017: Gemini egress from Cowork** (settings change plus a fresh sandbox); **Q-019: poster 2 re-run** with "horizontally across both thighs"; **Q-020: dedicated label close-ups** for the swap; **Q-021: memory.md hygiene pass**, now more overdue than last week; **Q-022: push 24-plus local commits from the Mac**; **Q-013: back-catalogue pass to the SPORTIF / rule / collection mark**; **Q-014: Hugo's Photoshop reference** for the burned-in wordmark.
- [ ] **Colourway strips, range card and wholesale line sheet.** Unblocked by the measured colours two weeks ago, still unbuilt.
- [ ] **Q-001: standalone waitlist capture page + 3-email welcome flow.** Now the top unbuilt item in eight separate sessions. Needs neither Lucy nor the trademark.
- [ ] **Q-010: high-quality band-swap renders in a native Mac terminal**, then finalise and send email-03.
- [ ] **Lucy's older picks:** Q-011 (collection grid colourway), Q-006 (Content Creation Strategy reaction, gates Phase 2), Q-004 (music-bed pacing), Q-003 (incentive A/B/C). All four are candidates to fold into the booth email rather than chased separately.
- [ ] **Q-008: Photoshop cutout of the ball hero**; **Q-005: Canva Pro** brand kit and folder share; **Q-002: trademark clearance**, still the critical-path gate on Lucy's lawyer's clock.
- [ ] Carried: ambassador/instructor seeding shortlist (eleventh week, needs nothing from anyone), film the unboxing, ElevenLabs API key, Shopify store, materials question, Stage 3 synthesis template, PDF generators still on Poppins.

### Suggested focus for next week
1. **Send the Fit Expo booth email, and send it first (Q-027, Q-028).** It is the only item in the workspace with an external deadline attached, it is blocked on nothing but an email Hugo already promised, and until the panel dimensions arrive no booth asset can be built at the right size. Ask for dimensions and bleed, confirm the handle goes back on, and check the Canva licence covers print and event display in the same pass. Fold Lucy's four older unanswered picks (Q-011, Q-006, Q-004, Q-003) into that message rather than chasing them separately, since one message has consistently beaten five.
2. **Spend ten minutes shooting the band DROPPED on a floor (Q-023).** White sheet, direct sun, house setup. It is the smallest task on the board with the widest unblock: it removes the warping step from all five placements, kills the staging trap at source rather than patching around it, and produces a real in-use asset the range card and line sheet both need. Then do the shot 01 colourway comparison (Q-025) with a clean Replace Contents pass so the three builds are actually comparable.
3. **Start the 3D band (Q-016), timeboxed to one sitting.** It is now promised in writing, which is a different obligation from the last three weeks of carrying it. Give Tripo one session, judge the mesh honestly, and switch to a hand-built Blender loop if it comes back lumpy. Unblock Gemini egress (Q-017) in the same session so the default engine is callable from here while the mesh runs.

---
## Weekly Review, 2026-08-23 (week of 2026-08-17)

Three sessions this week (031 on 08-17, 032 running from the evening of 08-20 through 08-21, and 033 on 08-21), against one last week. Throughput came back, and it went almost entirely into one place: the real product. The physical bands arrived, were shot four separate times, had a colour problem diagnosed and fixed, and by the end of the week every colourway is measured, every face is photographed, the weave is a brand asset, and two finished posters exist that were built from the actual band rather than around it. The workspace also finally closed a protocol hole it had been falling through for three sessions. What did not move is the queue waiting on Lucy, including a batch that has been packed and ready to send since Monday.

### Highlights
- **The real product is now the source of truth, and the colour is measured rather than guessed.** Four shoots in three days. Shoot 2 failed on a blue card and the failure was worth more than the frames: open outdoor shade is lit by blue sky, so a blue surface plus a blue sky stacked two casts and the heavy band came back at hue 258 with 22% saturation against a known-good hue 17 at 50%. Direct sun on a white sheet fixed it, verified rather than assumed (corrected heavy lands hue 17 / 53% against 17 / 50%). Measured colourways are now house canon (D-027): LIGHT `#B8A080`, MEDIUM `#9D7459`, HEAVY `#6C4333`, all noticeably deeper than the palette in brand.md. Colourway strips, the range card and the wholesale line sheet are unblocked as a direct result.
- **Two finished posters built from the real bands, plus a head to head that settled the generator question.** `build_band_posters.py` produced an editorial collage and a coming-soon teaser, each in feed 4:5 and story 9:16. Separately, Hugo ran all three poster prompts through gpt-image-2 and Gemini: **Gemini held the band colour, rendered the knit as fabric rather than a smooth strap, and actually followed the placement instruction, so it is now the default (D-032)**. The strongest single output of the week is `p3-blur-gemini-TYPED.png`, the SPORTIF lockup burned into the wall behind a blurred figure using the S031 luminance trick, with no cutout needed at all.
- **Hugo invented a brand asset mid-shoot.** He shot three texture close-ups on his own initiative, one per band. Those became `assets/textures/`: a seamless 1024px tile per colourway plus a large single-crop plate that needs no tiling for full-bleed use (D-028). The demo, heavy weave full bleed under the cream lockup, reads genuinely expensive, and the texture frames turned out to be the most accurate colour samples in the whole project because the band fills the frame with nothing else in it.
- **Lucy approved the email-02 socials and the master mark changed on the back of it.** Her three notes were addressed, and three things changed beyond her ask: the lockup is now SPORTIF / rule / collection everywhere (D-017), the @handle came off on-platform assets (D-018), and placement became photo-led through a clearance search plus Hugo's marked override boxes (D-019). Two bugs she never saw were also caught: story lockups sitting under Instagram's own profile row, and type reading small on a real phone.
- **The session protocol became two commands that check themselves (D-035).** `scripts/startup.py` and `scripts/closeout.py`, both wired to slash commands. Close-out verifies the session entry, the CURRENT STATE block, both registries, the dash sweep and the git state, and refuses to commit while anything fails. It caught a bug in itself on its first run, which is the argument for the whole exercise.

### Patterns I noticed
- **Controlled tests keep beating opinions, and they keep overturning the intuitive answer.** The blue card was blamed for the colour failure until a sun versus shade test showed open shade was the bigger culprit. Hugo's hunch that a label close-up in the references would fix label rendering was tested as a matched pair and was wrong: the reference made no difference, crop scale did (D-033). Same method as last week's brute-force tracking search. This is now the workspace's default move on a contested question.
- **Hugo's eye remains the last QA gate, and this week it rejected my work twice.** The texture transplant got "that looks bad" and was recorded as a dead end rather than defended (D-034). The first prompt doc was unfollowable and had to be rewritten into self-contained paste blocks (D-031). Both rejections produced better rules than the original work did.
- **Every protocol that lived only in prose got skipped.** The em-dash breach in S031 and the skipped startup in S033 have the same root cause: CLAUDE.md is not auto-loaded in Cowork, so anything documented only there depends on a session choosing to open a file nothing forces it to open. Both halves are now named commands. The general shape is that automating one end of a loop guarantees the failures land on the other end.
- **One rule emerged from all the AI work and it is a constraint, not a technique: never let a generator draw the band at large scale.** Big in frame means shoot it or composite the real cutout; small and incidental means generate it and swap the label. Every band failure this week (smooth suede strap, towelling weave, blank label, band along the leg instead of across the thighs) is downstream of asking a generator to render the product.
- **The Lucy queue did not move, and this time it is on our side.** The email-02 v2 batch has been staged, drafted and send-ready since 08-17 and is still sitting on disk six days later. Sending is not blocked by anything.

### Skills / knowledge gained
- **Product photography, now settled house method:** shoot on a white surface in DIRECT SUN, never open shade (shade is lit by blue sky, which stacks with any coloured surface); a white bounce card just outside frame on the shadow side; expose for the BAND, not the sheet; iPhone Photographic Styles must be Standard or a second invisible colour shift is baked into every frame; AE/AF Lock does NOT lock white balance in stills, so the in-frame neutral is what makes correction possible. Full setup at `clients/sportif/products/iphone-camera-setup.md`.
- **File handling:** `pillow-heif` reads HEIC directly, so the JPEG conversion step was never needed and was discarding EXIF; background removal strips EXIF, so originals must live alongside cutouts.
- **Generation craft:** describe a physical object by negation as well as description, and dress the model in a contrasting colour so the product is the only accent; more references improve PLACEMENT but not label legibility; label legibility is a function of how many pixels the label occupies, roughly 300px works and roughly 60px does not; Nano Banana Pro accepts up to 14 references while gpt-image-2 drifts past three or four.
- **Compositing details worth reusing:** drop shadows on the warm palette must be tinted warm brown (122, 78, 56), never grey, and the alpha must be padded before blurring or the blur clips at the object edge; a tall thin cutout rotated 14 degrees returns a bounding box nearly twice the object's width, so place by intended size and cap against the neighbour rather than trusting the box.
- **Cowork environment mechanics:** `rm` is blocked inside the mount but `mv` is not, which is the general workaround for anything needing deletion, and specifically for the stranded `.git/*.lock` files that make every second commit fail with a misleading error (D-036).
- **Two tooling lessons that generalise:** a warning that can never be cleared is worse than no warning, because it trains you to skim the whole warning channel; and a mechanical rewrite is only as safe as the smallest surface you can still proof-read, proven when a blunt dash rule turned "2-3 uses" into "2, 3 uses".
- **3D target spec (for Q-016):** Shopify wants GLB, about 4MB total, textures as optimised JPG at or under 2048x2048, diffuse plus normal plus a combined occlusion/roughness/metalness map, real-world scale, origin centred at the product's base.

### Open questions still unresolved
**Resolved (by a later session this week):**
- [x] ~~Q-015: reshoot the bands on white so the colour is usable~~ RESOLVED Session 032 (shoot 4): 12 frames on a white sheet in direct sun, corrected heavy at hue 17 / 53% against a known-good 17 / 50%, measured colourways recorded.
- [x] ~~Q-018: complete the band set~~ RESOLVED Session 032 (shoot 5, same afternoon): all three bands now carry all five faces, plus three texture close-ups and two tight parallel trios.
- [x] ~~Q-007: Lucy's reply on the email-02 socials~~ RESOLVED Session 031: approved with three notes, whole batch rebuilt as v2.
- Note: Session 033 opened Q-021 and Q-022 and no later session exists, so neither could be resolved. Nothing in the most recent session's open loops needed flipping.

**Still open:**
- [ ] **Q-016: build the band's 3D model.** Flagged as the first task of the next session. Tripo AI account exists, multi-view plates are ready in `products/band-reference-plates-v2/`, weave plates in `assets/textures/` are the material source. Fall back to a hand-built Blender loop if the mesh comes back lumpy.
- [ ] **Q-012: SEND the email-02 v2 batch to Lucy.** Drafted, 12 attachments staged in `TO-SEND-2026-08-17/`, not sent. Then her pick of black / white / outline to lock the house standard.
- [ ] **Q-017: Gemini is wired but not callable from Cowork.** `GEMINI_API_KEY` is in `.env`; needs `generativelanguage.googleapis.com` allowed in Network Egress plus a NEW chat, because egress changes only apply to a freshly booted sandbox.
- [ ] **Q-019: poster 2 needs a re-run.** Both engines put the band diagonally along the leg; the prompt needs "horizontally across both thighs, perpendicular to the legs".
- [ ] **Q-020: shoot dedicated label close-ups** of all three bands, tight and high-res, for the two-image swap. Not as AI references (D-033 settled that), for the swap itself.
- [ ] **Q-021: memory.md hygiene pass.** CURRENT STATE is about 35KB against a brief of roughly 12 lines, and there are 8 Weekly Reviews when 4 is the useful window. Fold settled items into DECISIONS.md and archive the older reviews.
- [ ] **Q-022: push the local commits from the Mac.** 24 commits unpushed; Cowork cannot push reliably.
- [ ] **Q-013: back-catalogue pass to the SPORTIF / rule / collection mark** (posters, product shots, the three IG ads, the band-swap set, both Lucy-facing PDFs).
- [ ] **Q-014: Hugo's Photoshop reference** for the burned-in wordmark treatment, ideally with the layers panel.
- [ ] **Build the colourway strips, range card and wholesale line sheet.** Newly unblocked by the measured colours; the tight parallel trios from shoot 5 are the intended source.
- [ ] **Q-001: standalone waitlist capture page + 3-email welcome flow.** Now named the top unbuilt item in seven separate sessions. Needs neither Lucy nor the trademark.
- [ ] **Q-010: high-quality band-swap renders in a native Mac terminal**, then finalise and send email-03. Fifth week carried.
- [ ] **Lucy's outstanding picks:** Q-011 (collection grid sign-off and whether she wants cream or white), Q-006 (Content Creation Strategy reaction, which gates Phase 2), Q-004 (music-bed pacing), Q-003 (incentive A/B/C).
- [ ] **Q-008: Hugo's Photoshop cutout of the ball hero**, which blocks the layered poster.
- [ ] **Q-005: Canva Pro**, brand kit and folder share with Lucy. Expected ~2026-07-30, still not done.
- [ ] **Q-002: trademark clearance**, the critical-path gate, on Lucy's lawyer's clock.
- [ ] Carried: ambassador/instructor seeding shortlist (tenth week, needs nothing from anyone), film the unboxing, ElevenLabs API key, Shopify store, materials question, Stage 3 synthesis template, PDF generators still on Poppins.

### Suggested focus for next week
1. **Send Lucy ONE message that clears the whole queue.** The email-02 v2 batch is packed and has been for six days (Q-012); fold in the collection-grid colourway (Q-011), the Content Creation Strategy reaction (Q-006), music-bed pacing (Q-004) and the incentive A/B/C (Q-003). Five threads have been waiting in parallel and one message is far likelier to get answered than five. This was also last week's number one focus and it did not happen.
2. **Do Q-016 in one timeboxed sitting, and unblock Gemini while waiting on the mesh.** Tripo is signed up and the plates are ready, so the only real decision is when to abandon it for a hand-built Blender loop. Give it one session, judge the mesh honestly, and switch if it lumps. Q-017 is a settings change plus a new chat and should be done at the same time so the default engine is actually callable from here.
3. **Turn the measured colours into the commercial assets they unblocked:** colourway strips, the range card, the wholesale line sheet. Four shoots were spent getting to trustworthy colour and nothing has yet been built on top of it. If there is time after that, the waitlist page, seventh session running.

---

## Weekly Review, 2026-08-17 (week of 2026-08-10)

One session this week (030, 2026-08-11, Cowork), and, worth saying plainly, one session in the last twenty days: the log jumps from 2026-07-28 (Sessions 028/029) straight to 2026-08-11. The single session that did run was a clean, self-contained client deliverable that went out the door the same day, which is the right shape for a low-volume week, but the backlog underneath it has not moved.

### Highlights
- **The SPORTIF "collection" grid banner was built AND sent to Lucy in one session.** Lucy supplied a square reference lockup (peach `#F0CDB3`, white SPORTIF, rule, lowercase "collection"); `build_collection_grid.py` turned it into a 3240x1440 master split into three 1080x1440 tiles named by posting order, with `POST-ORDER.md` alongside. Build → email → sent, same day, no round trip lost.
- **A real typographic problem was diagnosed rather than fudged.** Reproducing the reference's cap-height ratio blew "collection" out to 1030px inside a 1080px tile. The fix, size the sub-line off the CENTRE TILE (0.55 of tile width) and the rule off the sub (0.75x), preserves the reference hierarchy while restoring ~245px of clear space either side. That's a reusable rule for any future multi-tile lockup.
- **The clipped-letter question was settled by brute force, not opinion.** Tracking 0.24 to 0.34 × sizes 440 to 560 were searched exhaustively: with 7 letters across 3 tiles, no combination avoids a seam landing inside a glyph. The clipped T crossbar is inherent to the format, not a bug, and is now something to state proactively in client emails rather than defend after the fact.
- **Ambiguity was resolved before building, not after.** "Collective" vs "collection" was checked against the artwork and confirmed with Hugo up front, as were tile shape and colourway (peach/white only, with cream and white offered to Lucy as options in the email rather than pre-built). Cheap clarification beat expensive rework.

### Patterns I noticed
- **The per-request folder convention is now fully habitual.** Sessions 028, 029 and 030 all produced a self-contained request folder (downloads + created + README + email-to-lucy). It has survived three sessions across two different environments without anyone re-deciding it.
- **"We own the type" continues to hold as the house rule.** Session 030's deliverable is 100% PIL-composited Glacial Indifference on a flat peach master, no AI in the loop at all. When the brief is pure typography, the house rule collapses to "just build it ourselves," and that's the fastest path.
- **Reference artwork is a proportion trap.** Twice now (S028's logo lockup, S030's sub-line) matching a reference's literal ratios produced a wrong result, because the reference was authored at a different canvas scale. The durable lesson: derive proportions from the OUTPUT frame, not the reference's absolute ratios.
- **Cadence dropped hard and the carried backlog didn't.** From eight sessions in the week of 07-20 to one in nearly three weeks. Everything the last review flagged as "needs neither Lucy nor trademark" is untouched, which means the constraint this month is throughput, not blockers.

### Skills / knowledge gained
- **Multi-tile lockup sizing rule:** size sub-lines and rules as a share of the CENTRE TILE width, never off the primary wordmark's cap height, wide tracking on the primary word inherits into anything scaled from it.
- **Seam math for grid banners:** with N letters spanning 3 tiles, seam-vs-glyph collision is combinatorially unavoidable for odd letter counts like 7; verified by exhaustive search across tracking and size, so stop looking for a setting that fixes it.
- **Practical checks worth repeating:** sample the reference background rather than eyeballing the hex (it came out as (241,205,179), effectively the brand blush); verify lockup balance with an ink-bounds scan (307 top / 340 bottom = a deliberate optical lift).
- **Client-comms habit:** name known format artefacts (the clipped crossbar) in the email that ships the asset, rather than waiting to be asked.

### Open questions still unresolved
**Resolved (by a later session):**
- [x] ~~Q-009: email 03 pending Lucy's screenshot (Session 028)~~ RESOLVED Session 029, the request arrived as a 6-reference PDF and was built out in full (`clients/sportif/email-03-band-photo/`).
- Note: Session 030 has no `[ ]` items of its own to reconcile, its single open thread (Lucy's reply) is still outstanding, so nothing there could be marked resolved.

**Still open:**
- [ ] **Lucy's reply on the collection grid**, including whether she wants a cream or white colourway alongside the peach (Session 030).
- [ ] **Q-010: run the high-quality band-swap / branded renders in Terminal**, then finalise the email-03 attachment set and send to Lucy (Session 029). Third week carried; the ~60s harness cap is the reason, a native Mac terminal is the fix.
- [ ] **Lucy's other replies:** email-02 socials (Q-007) and the expert-brand "Content Creation Strategy" PDF (Q-006, which gates Phase 2, her expert niche, one avatar, four quadrants).
- [ ] **Q-008: Hugo's Photoshop cutout of the ball hero**, which blocks `poster_lucy_layered.py` (white-on-light mattes fail in rembg).
- [ ] **Standalone waitlist capture page + 3-email welcome flow**, needs neither Lucy nor trademark, now named the top unbuilt item in six separate sessions.
- [ ] **Canva Pro** (was expected ~2026-07-30, still not logged as done): Sportif brand kit + share the Sportif folder with Lucy.
- [ ] **Lucy's picks still pending:** music-bed pacing (calm ~100 BPM vs upbeat ~118 BPM) and the incentive decision A/B/C.
- [ ] **Film the unboxing**, bands in hand since Session 021, footage still not shot.
- [ ] **Ambassador/instructor seeding shortlist**, ninth week carried, designated the main growth engine, requires nothing from anyone.
- [ ] **Trademark clearance**, the critical-path gate, on Lucy's lawyer's clock.
- [ ] Carried: ElevenLabs TTS awaiting Hugo's API key, `cosmos_yoga-duo.mp4` Seedance path, Shopify store (trademark-gated), materials question, Stage 3 synthesis template, PDF generators still on Poppins.

### Suggested focus for next week
1. **Send Lucy ONE consolidated message that clears the entire feedback queue**, collection-grid colourway, email-02 socials, the Content Creation Strategy PDF, music-bed pacing, and the incentive A/B/C. Five separate threads have been waiting on her in parallel; one message is far more likely to get answered than five, and it un-gates Phase 2 of the expert-brand strategy.
2. **Do one native-Mac-terminal render session and close Q-010.** The high-quality band-swap/branded renders are the only thing standing between the email-03 work (already built) and it actually reaching Lucy. It is a single uninterrupted hour, not a project.
3. **Build the standalone waitlist capture page.** Six sessions have now called it the top unbuilt item; it depends on neither Lucy nor the trademark, and every asset built since July, grids, reels, posters, product shots, dead-ends without it. If throughput is the constraint this month, spend it here.

---

## Session 038 (2026-09-03, Cowork): Lucy says peach type, and the peach itself is now the question

Client: Sportif
Tags: sportif, lucy, weave-tiles, brand-colour, pantone, contrast, email, instagram

**Q-029 closed, and it closed the right way.** Lucy replied 2026-09-02 asking for "the branding
colour like the font colour to be in my logo peach colour". Read plainly that is the TYPE, not the
plates. She did not choose the brand-colour weave, so D-039 and D-046 hold and the real product
colour stays on the plates. She is away until Thursday 10 September.

**She attached a Pantone chip and it does not match our records, which is the new loop (Q-033).**
Her chip is Pantone 162 C, about `#FFC0A0`. Two independent sources say her logo peach is
`#F0CDB3`: her own logo artwork `assets/05-logo-sportif-white-on-peach.png` and her swatch
`assets/11-swatch-peach-nude.png` both measure `#F0CDB4`, and her intake questionnaire of
2026-06-13 lists "Light Orange (in Canva #f0cdb3)". The Pantone chip is the outlier. Her answer
sets the primary brand colour in `brand.md` line 105, not just these tiles, so it was worth
stopping for rather than just applying the chip.

**Peach type costs a quarter of the contrast, and the halo buys it back.** Measured behind the
lockup: LIGHT 2.47:1 cream against 1.86:1 peach, MEDIUM 3.84 against 2.90, HEAVY 5.93 against
4.47. Darkening the LIGHT plate was already off the table, so the lever was the existing warm
halo, lifted 1.55x on every peach build. The wordmark, rule, subline and weight line all hold on
all three at that setting.

**`build_texture_weight_tiles.py` is now parameterised instead of forked.** Three environment
overrides: `SPORTIF_TYPE_COL`, `SPORTIF_HALO`, `SPORTIF_OUT`. Defaults reproduce the set Lucy has
already seen, byte for byte. Five builds this session came out of one script rather than five
copies of it, and when she names the colour the reissue is one command.

**Everything went out in one email, deliberately.** 8 attachments: two comparison rows, one per
peach, plus BOTH finished postable sets, three tiles each at 1080x1350, numbered in upload order
(post 1 heavy, then medium, then light, so the grid row reads LIGHT MEDIUM HEAVY). Hugo's reasoning,
now a standing rule: front-load every version in one send so the client can answer the question and
use the work off the same email, with no round trip. It also removed the objection that she might
post live in a colour that turns out to be wrong, since she now holds the files for either answer.
Draft at `clients/sportif/email-grid-tiles/peach-confirm-to-lucy-2026-09-03.md`. Sent 2026-09-02.

**Housekeeping.** The stranded `.git/HEAD.lock` from a previous Cowork commit is cleared.

---

## Session 037 (2026-09-01, Cowork): the workspace itself gets cleaned up

Client: Ochoproductions
Tags: housekeeping, memory, git, filter-repo, gitignore, disk, timezone, infrastructure

No client work. This ran straight on from Session 036 across midnight and is entirely
infrastructure, which is why it is its own entry.

**Q-021 closed: memory.md was carrying its own history.** The CURRENT STATE block had
accumulated every session's bullets from 015 to 035 and reached 41,338 bytes, roughly a third of
the file, and every session was reading all of it at startup. Rewritten as 13 live bullets, each
pointing at its D-number rather than restating it. All 70 retired bullets went to
`memory-archive.md` verbatim, along with 6 older Weekly Reviews, keeping the newest 4. memory.md
164,103 to 81,246 bytes and the check passes with zero warnings for the first time since S033.
Also fixed a contradiction: the archive header claimed Weekly Reviews stay in memory.md
permanently, which is the opposite of what `memory_tools.py` warns about, and is probably why
that warning was ignored for three sessions.

**Q-022 closed: 30 commits pushed.** Cowork has no GitHub credentials, confirmed by trying, so
this stays a Mac job.

**Q-030 opened and closed: the repo was carrying raw 3D binaries.** The four Tripo GLBs filed in
S036 went into git with no `.gitignore` rule, 227MB for four models rejected on sight. Now
excluded under `**/3d-band/runs-in/`, with `3d-band/final/` deliberately left trackable because
the finished Shopify deliverable is about 4MB and belongs in git. Then `git filter-repo` stripped
every `.glb` from all 104 commits and the result was force pushed. **Whole folder 3.4GB to 2.0GB,
`.git` 664MB to 483MB.**

**Two estimates I got wrong, both worth remembering.** I read `git count-objects` reporting 391MB
of "garbage" as pure waste; most were real objects not yet packed, and gc returned 87MB, not
391MB. And I quoted the GLBs at 225MB, which was FILE size: in the pack they cost about 103MB,
because GLB mesh data is float arrays that compress well. **The lesson is the same both times:
size on disk and size in a pack are different numbers, and the tool's own label is not a
measurement.** What the survey did settle correctly is where the weight actually is: across
history it is 295MB PNG, 209MB PSD, 69MB extensionless, 19MB JPG. The PNGs are 36 sessions of
generated posters, tiles and cutouts, which is the actual work, so 472MB is the floor and no
further rewrite is worth doing.

**938MB of the folder turned out to be three public repos cloned inside it**, `student-kit`,
`launch-video` and `hyperframes`, all clean, all re-clonable by `setup.sh`, none of them what
actually runs a render. Every composition pulls HyperFrames from npm at 0.7.64. Deleted the two
pure-reference ones. On the student kit, deleted only the 280MB of finished MP4s and kept the
3.1MB of code, because you learn from the code and it restores offline with `git checkout .`.

**A real bug found at the end: the scripts thought it was yesterday.** The Cowork container runs
UTC and Hugo is UTC+10, so any Sydney session before 10am sees the previous day. That is what had
been failing the pre-push hook all morning and it would have forced a wrongly dated session entry.
`startup.py`, `closeout.py`, `memory_tools.py` and `archive_memory.py` now pin "today" to
`Australia/Sydney` through a shared `today_local()` helper. The pre-push hook calls
`memory_tools.py check`, so it is fixed by the same change.

**Also untracked `.git-broken`**, a corrupted git directory from May that had been sitting in the
repo committed, 19 files.

**The timezone fix broke close-out on its first run, and that is the good news.** The patch
renamed every `today` it found, but `memory_tools.py` already HAD its own `today()` helper, so six
callers were orphaned and one line ended up calling itself. `closeout.py` caught the traceback and
refused to commit. The harness built in S033 did exactly what it was built to do: an infrastructure
change that would have shipped broken was stopped at the gate rather than discovered three sessions
later. Fixed by keeping the pinned helper as `today_local()` and restoring the file's own `today()`
on top of it, then smoke testing all four scripts.

## Session 036 (2026-08-31, Cowork): Lucy answers on the grid, the weave tiles get bolder, and the 3D band finally makes a loop

Client: Sportif
Tags: instagram, weave-tiles, typography, client-email, colour-accuracy, 3d, tripo, photogrammetry, diagnosis

Hugo drove, from a standing start of "where are we at". The day ran in two halves: a client
thread answered and shipped in the morning, and an evening spent diagnosing why the 3D band kept
coming back wrong, ending with the first result that was actually the right shape.

**Lucy replied on the weave grid tiles, and the reply carried two asks.** She loves the concept
and wants to post it, which closes Q-024. She asked for them sized for the Instagram tiles, and
for the tiles in her brand colour.

The sizing ask needed no work. The tiles were already 1080x1350, which IS the feed size. The one
real thing behind it is the profile grid, which crops thumbnails to 3:4 and shows a centred
1012px column; the lockup is 820px, so it clears by 96px each side. Answered with a mockup rather
than a paragraph, at `generated/images/texture-weight-tiles/grid-preview-for-lucy.jpg`.

**The colour ask was declined, and Hugo's reasoning is the one that matters (D-046).** Three
directions were built and measured first (as-shot, 50 percent tinted, full brand ramp), then he
called it: these tiles are a close-up of the actual fabric at a scale where colour is the only
thing a buyer can judge, so tinting them sells a colour the customer does not receive. A returns
problem and a trust problem on a launch where Lucy is the brand. The experiments are parked at
`brand-colour-options/` as a dead end that was tried.

**Then Hugo caught a second mistake, and it is the more interesting one.** Her words were "can
you please SHOW ME what it would look like in my brand colour". The first reply declined the
colour change and did not show her, which answers a question she did not ask and declines the one
she did. "Show me" and "pick one" are different requests, and the earlier advice collapsed them.
Fixed with a follow-up ten minutes later carrying one comparison image, real colour against full
brand colour, with the recommendation attached. Showing something with a clear recommendation is
not the same as offering a choice. Both rows are built by the CURRENT house build so colour is
the only variable, and the halfway tinted version was deliberately withheld because it fails the
same accuracy test by half.

**The weight line was too thin, and a thumbnail test settled it (D-047).** Hugo flagged that
LIGHT / MEDIUM / HEAVY was getting lost. Rendered down to 128px, roughly a real profile-grid
thumbnail, the Regular line was gone entirely on the light tile. Glacial Indifference BOLD fixes
it, plus an extra halo under that line alone. Separately the whole lockup went 0.66 to 0.76 of
canvas width, since type reads smaller on Instagram; one number scales the block and holds every
proportion, and the blurs and shadow offset scale with it. Folded into
`build_texture_weight_tiles.py` as the house build and the delivered set regenerated. Two emails
went to Lucy, both sent (Q-029).

**A date correction nobody had noticed.** Her intake says "LA Fitness Expo in February next
year". TheFitExpo Los Angeles 2027 is listed as 23 to 24 January. If that is her show, the runway
is three weeks shorter than the workspace has been assuming, and print deadlines land well before
the show. Noted against Q-027, needs confirming with her.

**The 3D band: two runs, one dead end and one breakthrough (D-048).** Run 1 came back as four
flat open straps, one a standalone gold plaque, at 1.9M triangles and no real world scale. The
first diagnosis blamed the prompt, which said "strap" and "metal label". Hugo pushed back that it
had used the photographs, and he was right. Looking properly at the references settled it:
**every band photo in the workspace shows the band pressed FLAT**, so the hole is never visible,
and a flattened loop from above is the same picture as a strap. The mesher was never given the
information.

Then Hugo tested it himself. Run 2 used a gpt-image-2 image showing a band lying open as an oval,
hole visible, and Tripo returned a genuine closed loop, rendered six ways at
`3d-band/renders/band-run2-contact-sheet.jpg`. One variable, proven in both directions in one
evening. It still carries the pouch bag from the same input image, invented peach colour, 2M
triangles and no scale, but the shape question is answered and the shoot list is validated before
a frame is shot.

**Working method worth keeping: the thumbnail test.** Twice today the decisive evidence came from
rendering an asset down to the size it will actually be seen at and looking at that, rather than
judging it at full size. The weight line failed at 128px while looking fine at 1080. Same shape
of move as the S035 measurement work: build the test that answers the question rather than
arguing about it.

**Hugo's eye was the deciding gate again, three times.** The colour call, the thin weight line,
and the push back on my prompt diagnosis. All three were right and all three overturned something
I had written down.

## Session NNN, YYYY-MM-DD, One-line summary
### What we did
### What we learned
### Decisions
### Open questions / next steps
-->
