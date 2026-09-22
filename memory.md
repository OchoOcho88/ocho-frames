# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## CURRENT STATE (update this block every session, keep it to ~12 lines)

*Last updated: 2026-09-22 | Last session: 044 (Claude Code, CLOSED) | Working tree: committed clean | Git: push from the Mac | Next: two emails went to Lucy on 2026-09-22 (the ball photo with the logo in 162 C, then the room in 162 C, own threads, D-060), so Q-026 waits on two yes-or-no answers and nothing is owed to her. Still waiting on her: the February phone photos via WhatsApp and the PR team's poster size in October (Q-027), the show date (Q-043), her LA footage (Q-041), a filming date 1 to 10 October (Q-042). The Double Bay shot list is the one thing that needs nobody; three unlogged Tripo GLBs sit ignored in `generated/3D/`.*

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
## Session 044 (2026-09-22, Claude Code): Lucy's picture arrived, the ball photo built two ways and sent as two emails

Client: Sportif
Tags: sportif, lucy, email, peach-concept, pantone-162c, ball-photo, psd-tools, cutout, weekly-review, 3d-band

**Done.** Startup found the tree dirty: the 2026-09-20 weekly review sat uncommitted in `memory.md`, and three raw Tripo GLBs (170MB, written 21 Sep, unlogged) sat in `clients/sportif/generated/3D/`. Committed the review, flipped Q-039 to resolved (it was still printing), gitignored `generated/3D/*` with a `.gitkeep`. Lucy answered on 21 Sep with `1-as-it-is.png`, the ball reach: "use this picture here with the peach pantone colour". First build read that as the ROOM in 162 C (concept 2 with the fill swapped): her refined cutout pulled out of the concept PSD with `psd-tools` in a scratch venv and saved as `email-02-social/photoshop/feed-ballreach-cutout.png`, six room recipes compared, `scripts-local/build_ballreach_162c.py`. Hugo read it as the LOGO in 162 C on the untouched photo, which her 18 Sep line also says: `scripts-local/build_ballreach_peachmark.py`, four peach treatments, `peach` chosen. Hugo sent both as two separate emails, each its own thread, one version each (D-060). Registry rows Q-026 and Q-027 updated.

**Learned.**
- Lucy's February booth photos are phone shots coming via WhatsApp, and the PR team owns the booth design; the poster size arrives after she speaks to them in October. Panel size is now her handoff, not our ask.
- The wall under the ball photo's mark is in shadow (`#98806C`), so 162 C sits at 2.32:1 against it and reads with the white recipe's shadow. Black was 5.09:1.
- Recolouring the room to a pale Pantone is not the terracotta recipe with the fill swapped: Overlay 60 goes orange, Color and the tone map go muddy, and plain Multiply drifts orange because the raw wall is already warm. Neutralise the wall to its own reference first, then multiply, and the wall lands on the chip with its shading kept.
- The feed source is exactly 1080x1350 (no crop) and the story is the same frame at 1.4222 cropped 228px a side, so one mask serves both formats.
- `psd-tools` is not on the system Python; a venv in the scratchpad with `psd-tools pillow numpy` reads the PSD, and the extracted cutout is saved so the build scripts need only Pillow.
- Type rendering drift (`docs/gotchas.md`) does not matter here: these are new files, not refreshes of the delivered set.

**Decided.** D-060 (when her line has two honest readings, build both, send her ask first and our idea second, own threads, one version each, no options).

**Open.** Q-026 now waits on two yes-or-no answers. Q-027 carries the phone-photo and PR-team facts. The three GLBs in `generated/3D/` are unlogged: which run, which input, Hugo to say. Everything else unchanged and waiting on Lucy (Q-041, Q-042, Q-043, Q-028).

**Next.** On a yes to email 1, the peach mark on the other seven is a treatment swap in the v3 script. On a yes to email 2, the other seven need cutouts (`rembg` is on the Mac; the duo shot may need Hugo's hand). The Double Bay shot list (Q-042) is still the one thing owed to her that needs nothing from her.

---
## Weekly Review, 2026-09-20 (week of 2026-09-14)

Two sessions this week (042 on 09-18 and 043 on 09-20), both in Claude Code, both driven by Hugo. The shape of the week: one long build session that took the signature from a font name to a finished write-on and four renders, then one morning session that sent three replies and deliberately built nothing. Four things left the building, three emails and a WhatsApp, and the WhatsApp is the one that closed a loop. Underneath it a new workstream opened that nobody had planned for, behind-the-scenes founder-facing content, and with it the first job in months where Hugo is holding a camera rather than a mouse. The board did not get shorter, but for the first time in a while the reason is entirely on the client's side: every open Sportif loop is now waiting on Lucy.

### Highlights
- **The signature is finished, delivered, and turned out to be ours rather than hers (Q-034, Q-040, D-055, D-056, D-059).** Two sessions took it from "she says yes and here is my Canva file" to five rendered files. Her free Canva made PDF Print the only vector route out, so `scripts-local/extract_lucy_signature.py` flattens PyMuPDF's glyph refs into real paths and emits a font-free artboard; Hugo then built the write-on in After Effects across a whole session from hand-drawn pen paths used as an alpha matte. The delivery was the interesting part. Hugo sent the renders on WhatsApp on 09-20, she loved them, and they are of no direct use to her because she cannot place a video file herself. So they became our asset to apply to her content (D-059), which quietly changed what the whole job was for.
- **Lucy's placement note was measured onto the frame rather than eyeballed (Q-039).** She asked for the mark above the model's hand with its middle on her middle finger. Her middle finger measured x=340 off the finger creases, the wordmark went to x=343 with the ink bottom 26px clear of the fingertips, applied to both colourways and both build scripts, knowingly above `STORY_SAFE_TOP` because above the hand and inside the story safe zone are mutually exclusive on that frame. She posted it two days later. The mark sat near Instagram's chrome exactly as the 17 Sep email warned, and that was her call to make.
- **Three chains answered in one morning, and nothing was built (S043).** The 27 Aug set is accepted and live on her grid. She asked for "the three concepts" in the brand peach and a poster from her February 2026 shoot; we hold neither the picture she means nor the shoot files, so the reply asked for both rather than guessing at candidates. Hugo's call, and it is the correct one: an ambiguous client phrase is not fixed by naming candidates.
- **A new workstream opened on her ask, not ours (Q-041, Q-042, Q-043).** She wants her footage cut with effects and branding in Kia Buckley's founder-facing format, she is sending LA trip footage including her new supplier meeting, and she asked whether Hugo and Lauren would film a day of her in Double Bay. Answered yes for 1 to 10 October, phone by default with camera hire only against a quote (D-057), shot list first. A booth announcement was asked for in the same thread and is blocked on the show date.

### Patterns I noticed
- **The channel that works with Lucy is not always email.** Q-040 sat unsent through three other replies going out, then closed in one WhatsApp message the same day, and her answer reshaped the job. Meanwhile D-058 was written in the other direction: one topic per thread, one question per email, fresh subject per job, because the mixed chains are what made her 18 Sep messages ambiguous in the first place. Both moves are the same instinct, match the message to what it is actually for.
- **Delivering a thing tells you what it is, and you cannot learn that beforehand.** The signature was built as something to hand Lucy and turned out to be something we apply for her. Same family as last week's "settled is not the same as wanted now", one step further along: the record was not wrong, the assumption about who the asset was for was.
- **Measure, then place; and zoom out before judging.** The finger position, the contrast pairings, the terracotta render verified against a reference composite within four levels of solid ink and one level of frame mean. Against that, at 800 percent three of the four faults Hugo flagged in the write-on were correct behaviour. Zoom in to fix, zoom out to decide, and the second half is the one that is easy to forget.
- **Q-027 accumulates blockers instead of closing, and this is the fourth consecutive review saying so.** It was owed in writing on 08-27. This week it gained two more dependencies (her February shoot files, the show date) and shed one worry (Canva licensing, now that the source is her own shoot). Panel size has been asked three times. The handle line (Q-028) was cut from the sent email again, so a one-line confirmation has now survived four separate opportunities to be made.
- **The workspace produced no generated imagery at all this week.** Two sessions of After Effects, ffmpeg, measurement and email. Worth noting only because it is the first week in a long run where D-038 and the generator rules never came up.

### Skills / knowledge gained
- **Trim Paths on a glyph OUTLINE traces the edge of a letter, not the pen stroke.** A write-on needs hand-drawn open paths down the centre of each letter, used as an alpha matte over the real artwork.
- **Trim Paths runs at constant speed along total path length,** so a long letter eats the animation. Fix with a keyframe at each stroke boundary, stroke weights of length^0.55, and explicit pen-lift holds.
- **Illustrator stacks newest on top, so drawing in writing order always imports into After Effects backwards.** Group order is trim order.
- **A shape layer from Create Shapes from Vector Layer anchors at 0,0, while AI footage anchors at its centre.** Typing the same Position into both breaks the matte.
- **The finished signature is five disconnected islands** and the `u` never touches anything, because Amsterdam Two is a typeface rather than joined handwriting. Every letter is meant to look detached.
- **Contrast pairings for the signature are settled.** White on the brand peach is 1.60:1, a ghost. Black covers peach, cream and the LIGHT and MEDIUM bands; white exists for the HEAVY terracotta at 8.44:1 and for dark photography.
- **`psd-tools` can read Hugo's refined cutout and mask straight out of the concept PSD,** so the three-concept rebuild in 162 C is scriptable from the source photo rather than dependent on a Photoshop sitting.
- **A saved PSD is not the recipe.** The concept file sits at Soft Light 10 and 25 percent against the Overlay 60 written in `WEAVE-ROOM-RECIPE.md`, and the cutout layer carries the mark, so any rebuild starts from the source photo.
- **`sportif_grade.py` still maps mid tones to the retired `#F0CDB3`,** and the 26 Aug "peach" folder is old peach. Both untouched, both a trap for anyone reaching for them.
- **QuickTime Animation is effectively dead;** modern QuickTime Player refuses it. ProRes 4444 is the alpha delivery format, verified identical within two levels and smaller.
- **The only photograph of Lucy the workspace holds is 214x320, inside her Canva PDF.** Anything full frame from it is a six times upscale.
- **Booth facts now on record:** TheFitExpo Los Angeles 2027 is 23 to 24 January, South Hall, and a 10 by 10 booth is $3,150 with a skirted table. Panel size is still unknown.
- **Kia Buckley is the founder of Kikiva,** the brand already named in `brand.md`. Founder-facing, phone-shot, bad days included, which is the format the behind-the-scenes edits are being measured against.

### Open questions still unresolved
**Resolved (by a later session this week):**
- [x] ~~Q-034: the signature original, file or font name~~ RESOLVED Session 042: she shared the Canva file, the face is Amsterdam Two as live text, extracted via PDF Print and animated in After Effects (D-055, D-056).
- [x] ~~Q-039: where the side stretch story is going~~ RESOLVED Session 043: she posted it on 18 Sep as a Story, mark near the chrome as warned. No lower version needed. Note: the row in `OPEN-QUESTIONS.md` still carries a `[ ]` marker despite its own RESOLVED text, so it is still printing at startup and should be flipped.
- [x] ~~Q-040: the signature animation built and unseen~~ RESOLVED Session 043: sent on WhatsApp, she loved it, and it is our asset to apply rather than hers to place (D-059). The drafted email is not needed. White-on-terracotta flat rendered afterwards.
- Note: Session 043 is the most recent session, so nothing in its own open loops can be flipped yet.

**Still open, opened this week:**
- [ ] **Q-041: the behind-the-scenes edits.** Her LA footage has not arrived; originals were asked for via Drive, Dropbox or WeTransfer rather than Instagram or WhatsApp. The promise in the 09-20 reply is cuts for Reels and Stories carrying the mark, 162 C and her signature write-on, so the assets exist and the footage does not.
- [ ] **Q-042: the Double Bay filming day,** 1 to 10 October, Lauren unavailable, phone by default (D-057). Waiting on her dates. The shot list is owed to her BEFORE the day and needs nobody to write.
- [ ] **Q-043: the LA booth announcement,** blocked on her confirming TheFitExpo LA and 23 to 24 January 2027, plus a booth number. When it lands it settles the Q-027 date correction too.

**Still open, carried from before:**
- [ ] **Q-026: the three concepts in 162 C.** Unparked this week. She said yes to the idea in the brand peach; which picture she means is ambiguous and was asked back on 09-20. Nothing built, deliberately.
- [ ] **Q-027: the Fit Expo booth poster,** owed in writing since 08-27 and now carrying three open dependencies: the picture, her February 2026 shoot originals, and panel size with bleed. The show date moved into Q-043.
- [ ] **Q-028: the handle rule,** off for Instagram, on for booth assets. One line, cut from the sent email again, still unconfirmed to her.
- [ ] **Q-036: the animated inspiration board,** her four answers then the loop build. Untouched this week; not raised in any of her three chains.
- [ ] **Q-038: composition end cards** still carry the old mark, the handle and a "Launching September 2026" line. Needs nobody, and the first decision is whether those compositions are still live at all.
- [ ] **Q-013: back catalogue to 162 C and the master mark.** Remainder on the row; delivered ads and posters explicitly excluded until Hugo asks.
- [ ] **Q-016, Q-023, Q-020: the 3D band, the dropped band and the label close-ups.** One phone sitting closes all three. Untouched for five weeks now.
- [ ] **Q-001: the standalone waitlist page plus 3-email welcome flow.** Top unbuilt item in twelve separate sessions. Needs neither Lucy nor the trademark.
- [ ] **Colourway strips, range card and wholesale line sheet.** Unblocked on colour since August, still unbuilt.
- [ ] **Q-002: trademark clearance,** still the critical-path gate on Lucy's lawyer's clock.
- [ ] **Q-017: Gemini egress; Q-014: Hugo's Photoshop reference.**
- [ ] **Parked behind `[p]`:** Q-001 to Q-010, visible with `open --parked`.
- [ ] Carried: ambassador and instructor seeding shortlist (fifteenth week, needs nothing from anyone), film the unboxing, ElevenLabs API key, Shopify store, materials question, Stage 3 synthesis template.

### Suggested focus for next week
1. **Write the Double Bay shot list and send it (Q-042).** It is the only thing owed to Lucy that needs nothing from her, the window she was offered starts in eleven days, and the list is what lets her add her own places and moments rather than being followed around. Lean on the Kikiva founder-facing format, which is already the agreed reference. Sending it also puts a date question in front of her without opening another thread.
2. **Twenty minutes with the phone to close Q-016, Q-023 and Q-020.** Geometry shot in shade as an open oval so the hole reads, then direct sun for the dropped band and the label close-ups per D-026, then one Tripo run with the real image. This has now been the number one or two recommendation in four consecutive reviews, and it is still the largest unblock available for the smallest effort. If it is not going to happen, the honest move is to park all three rather than carry them a fifth week.
3. **Build one thing that does not need Lucy.** Everything on the client side is now waiting on her, which makes this the right week for the work that never has been: the colourway strips, range card and line sheet on the settled 162 C with the measured band colours, or the waitlist page and welcome flow. Both have been unblocked for over a month and neither needs an answer from anyone.

---
## Session 043 (2026-09-20, Claude Code): three of Lucy's emails answered, nothing built

Client: Sportif
Tags: sportif, lucy, email, peach-concept, fit-expo, behind-the-scenes, kikiva, double-bay, psd-tools, weave-room

**Done.** Committed the After Effects project found dirty at start (saved after the S042 close-out, contents unknown). Read three Lucy chains, all 18 Sep, drafted three replies, all sent the same morning, nothing built on Hugo's call. **Chain 1 (email 02 thread):** the 27 Aug set is accepted and the pilates post is live on her grid; she wants "the three concepts" tried in the brand peach, and the poster built from her February 2026 shoot. Reply asks for the picture she means, the shoot originals (we hold none) and the panel size. Handle line cut, Q-028 still unconfirmed. **Chain 2 (grid tiles thread):** behind-the-scenes edits with effects and branding, reference Kia Buckley, LA footage coming, and would Hugo and Lauren record a day of her in Double Bay; the 16 Sep email also asked for a booth announcement. Reply says yes to the day (1 to 10 October, Lauren unavailable, phone, shot list first, camera hire quoted first) and asks her to confirm the show dates. **Chain 3:** she posted the side stretch, Q-039 resolved. `psd-tools` reads Hugo's refined cutout out of the concept PSD, so a scripted rebuild is possible.

**Learned.**
- Kia Buckley is the founder of Kikiva, the brand already in `brand.md`. Founder-facing, phone-shot, bad days included.
- TheFitExpo Los Angeles 2027 is 23 to 24 January, South Hall; a 10 by 10 booth is $3,150 with a skirted table. Panel size still unknown.
- An ambiguous client phrase ("the three concepts") is not fixed by naming candidates; ask her to send back the picture (Hugo's call).
- The saved concept PSD is not the recipe: Soft Light 10 and 25 percent, against Overlay 60 in `WEAVE-ROOM-RECIPE.md`. The cutout layer carries the mark, so rebuild from the source photo.
- `sportif_grade.py` still maps mid tones to the retired `#F0CDB3`; the 26 Aug "peach" folder is old peach. Untouched.
- The side stretch went up as a Story, mark near Instagram's chrome as the 17 Sep email warned. Her choice.
- The S042 handoff line contradicted the loop rows; the rows were right.

**Decided.** D-057 (behind-the-scenes is shot on a phone by default; camera hire a quoted cost). D-058 (one topic per thread, one question per email, fresh subject per job). D-059 (motion assets are ours to apply, not hers to use).

**Open.** Q-039 resolved. Q-026 unparked, waiting on which picture. Q-027 gains two blockers (her shoot files, the show date). Q-028 still unconfirmed. Q-040 resolved on WhatsApp, our asset to apply (D-059). New: Q-041 (behind-the-scenes edits, LA footage incoming), Q-042 (the Double Bay day, 1 to 10 October, shot list to write), Q-043 (the booth announcement, blocked on the date). *(Weekly review 2026-09-20: this is the most recent session, so no later session exists to resolve anything here. Q-026, Q-027, Q-028 and the three new loops all carry forward unchanged. One registry fix noted for Hugo: the Q-039 row in `OPEN-QUESTIONS.md` still has a `[ ]` marker although its own text records it RESOLVED S043, so it keeps printing at startup.)*

**Next.** When Lucy answers: the peach concept build, the Double Bay shot list, the booth announcement. Terracotta flat rendered, `lucy-signature-writeon-terracotta.mp4` (detail on the Q-040 row). Strays cleared; `studio-reformer-sidestretch.mp4` kept as the signature-over-content preview.

---
## Session 042 (2026-09-18, Claude Code): Lucy's placement on the side stretch, and her signature turned into a write-on

Client: Sportif
Tags: sportif, lucy, signature, amsterdam-two, canva, after-effects, trim-paths, track-matte, prores, alpha, contrast, story-safe-zone, email

**Done.** Committed three carry-over items found dirty at start (the 2026-09-13 weekly review, `AGENTS.md`, the Codex `.agents/` skills). **Q-039, the side stretch story:** Lucy asked for the mark moved above the model's hand, its middle on her middle finger. Measured her middle finger at x=340 off the finger creases, placed the wordmark at x=343, ink bottom 26px clear of the fingertips, applied to `build_email02_social_v3/v4.py` and both colourways. Email sent under its own subject. **Q-034, the signature, closed end to end.** Lucy said yes and shared her Canva file; the signature is live text in `Amsterdam Two`, so she does not need her PR team, and it is a typeface not handwriting (D-055). Her Canva is free, so PDF Print was the only vector route out. Wrote `scripts-local/extract_lucy_signature.py`: flattens PyMuPDF's glyph `<use>` refs into real paths, inverts the composite for true transparency, and emits a font-free 1080x1920 artboard. Hugo then built the write-on in After Effects across the whole session (D-056) and rendered four files.

**Learned.**
- Trim Paths on a glyph OUTLINE traces the edge of a letter, not the pen stroke. A write-on needs hand-drawn open paths down the centre of each letter, used as an alpha matte.
- Illustrator stacks newest on top, so drawing in writing order always imports into AE backwards. Group order is trim order.
- Trim Paths runs at constant speed along total length, so the `W` (32.6% of the path) ate a third of the animation while `u` and `c` got three frames each. Fixed with a keyframe at each stroke boundary, weights of length^0.55, and pen-lift holds.
- The finished signature is FIVE disconnected islands; the `u` never touches anything. Every letter must appear detached, because that is the typeface.
- A shape layer from Create Shapes from Vector Layer anchors at 0,0; AI footage anchors at its centre. Typing the same Position into both breaks the matte. Cost us twenty minutes and my wrong instruction.
- White on the brand peach is 1.60:1, a ghost. Black covers peach, cream and the light and medium bands; white exists for the heavy terracotta at 8.44:1 and for dark photography.
- The only photograph of Lucy we hold is 214x320, inside her Canva pdf. Anything full-frame from it is a 6x upscale.
- Zoom in to fix, zoom out to decide. At 800% three of the four things Hugo flagged were correct behaviour.

**Decided.** D-055 (the signature is Amsterdam Two, animate the outlines, never install the font). D-056 (the write-on is built from pen paths, with the measured numbers).

**Open.** Q-039 new, waiting on Lucy. Q-034 resolved. Q-040 new: the animation is built and Lucy has not seen it, email drafted.

**Next.** Send both drafted emails. Then the white-on-terracotta render, and clear three stray files out of `generated/videos/`.

---
## Weekly Review, 2026-09-13 (week of 2026-09-07)

Three sessions this week (039 on 09-11, then 040 and 041 both on 09-12), all in Claude Code, all driven by Hugo. The shape of the week: the primary brand colour finally got settled by the client's own printer and propagated through every forward source in a day; Lucy then asked for something nobody had planned for and got a working mock back the same afternoon; and the workspace turned on itself and cut what it costs to start a session by more than half. Two of the three sessions ended with something in Lucy's inbox. The one thing that did not happen, again, is the Fit Expo booth email, now deferred by Hugo rather than blocked, which is a different and worse status than it had last week.

### Highlights
- **Pantone 162 C is the brand colour, and it came from her printer rather than from an argument (D-051).** Q-033 had been the sharpest open question on the board: her Pantone chip contradicted two of her own files and her intake form. The answer settled it in the direction the measurement could not, because New Directions matched her Canva `#f0cdb3` to 162 C as the closest printable colour. Screen hex is Pantone's own `#FFBE9F`. The weave tiles she is already posting measure `#FFC09F`, close enough that nothing delivered had to be reissued or apologised for. Forward sources moved the same day: `brand.md`, `voice-guidelines.md`, both client PDFs, the synthesis brief and eight build scripts.
- **Lucy asked "do you happen to know how to do something like this inspiration board?" and got a finished mock the same day (D-053).** She forwarded SABO's stop-motion cork board GIF. Rather than answer in prose, the reference was measured off a screen recording into a real spec (4.8 s loop, about 34 frames at roughly 140 ms, hold times and cut points all recovered from frame differences) and a 1200x1500 final-frame mock was built from assets the workspace already held: the weave tiles as fabric, the three colour-corrected cutouts, the 162 C chip with the three measured band colours, the master mark, polaroids from her own screenshots, and her real signature lifted off an email crop. Three passes, no generator touched it, so D-038 stayed clean. The mock and the four questions went in the same send.
- **The token diet cut the cost of existing (Q-037, D-054).** Startup print 4,709 to 2,003 tokens, CLAUDE.md 2,810 to 1,289, close-out entry 1,106 to about 700. The mechanism matters more than the numbers: loops print one brief line each, dormant loops park behind `[p]`, gotchas moved to a file that is named but never printed, and `closeout.py` now warns on a fat entry, a missing heading or a long handoff. The workspace now has a written policy against its own sprawl instead of a periodic cleanup.
- **Three loops that needed nobody were closed in one sitting, and one thing was overreached.** Q-025 got a colourway compare built out of Hugo's own shot 01 placement with colour as the only variable; Q-019 got the poster re-run right first time once the band was described as "one closed loop that encircles BOTH thighs"; Q-013 got the band posters and three compositions rebuilt in 162 C. Then the three Lucy posters and three IG ads were moved to the master mark on the strength of a settled decision nobody had asked to apply, and Hugo reverted the lot.

### Patterns I noticed
- **Settled is not the same as wanted now, and that is the sharpest lesson of the week.** The master mark has been house standard since D-017 and Q-013 has sat open for weeks, so moving delivered creative onto it was defensible on paper and still wrong. Delivered work has a different status from unbuilt work. This is the first time this review has had to record the workspace overstepping rather than Hugo overturning it, and the correct rule is narrow: ask before touching anything already in the client's hands.
- **Reproduce the delivered file before changing one variable in it.** Used twice, both times to convert a claim into a fact: the collection grid was rebuilt in the OLD peach first and matched the posted August files pixel for pixel, so the new set provably differs only in colour; and the colourway compare lifts Hugo's existing placement out of the PSD rather than re-placing it, so the three builds are actually comparable. Same family as last week's "measure the thing you care about, not the tool's own label".
- **When a client asks a capability question, the answer is an artefact.** D-053 generalises what happened with the inspiration board: a "can you do this" gets a yes, a mock built from her own assets, and short answerable questions, not a menu of methods. Hugo cut the first draft's choice between a real shoot and a computer build for exactly this reason. It is the same instinct as D-046's "show me and pick one are different requests", now applied one step earlier in the conversation.
- **Two client-facing edits by Hugo were both about earned familiarity.** "It is so you" came out of the signature email as a claim to know her that he has not earned; the Canva ask was softened from instruction to suggestion. Both are now feedback memories. The house voice for Lucy is praise the work, suggest rather than instruct, never claim to know the person.
- **The board keeps getting more specific rather than shorter.** Q-033 closed and produced the colour that unblocks the commercial assets. Q-035 closed and immediately became Q-036, a build with four client answers in front of it. Q-025 closed as a build and became a one-line decision waiting on Hugo. Q-019 and Q-037 closed outright, Q-038 opened. Net movement is real; the count barely moved.

### Skills / knowledge gained
- **When a client colour comes from a printer, screen follows print.** Use the Pantone's own sRGB value rather than an eyeballed chip or a Canva hex.
- **A whole-logo overlay cannot tell fonts apart at 500px** (one pixel of drift halves the overlap), but a per-letter shape match against lookalike fonts can. Glacial Indifference Regular scored 0.82 against her artwork, ahead of Avenir 0.76, Poppins 0.75, Futura 0.67 and Glacial Bold 0.61, which confirms our file and hers are the same face and weight.
- **A screen recording of a GIF is enough to recover its frame timing.** Extract every frame, threshold the mean frame difference, and the change list gives the hold times and the loop period directly. No need for the original file.
- **A close-up plate tiled at its own scale reads as rope, not fabric.** What reads as the same material is the seamless tile scaled so the weave pitch matches the product cutout in the same frame, 0.2 scale in this build.
- **Photoshop's rotation sign is the reverse of Pillow's,** and the PSD layer is the check: +101 in Pillow matched Hugo's -101 at 20/255, the other sign at 88/255.
- **Post-grade band separations against the floor are LIGHT +19, MEDIUM +9, HEAVY minus 4.** The S034 numbers (42/31/12) were pre-grade against a bare floor and should not be quoted any more.
- **Environment overrides beat forked scripts.** `build_collection_grid.py` and `build_inspiration_board_mock.py` both took `SPORTIF_*` overrides this week (D-050), so a reissue is one command and the defaults still reproduce the delivered set byte for byte.
- **Toolchain facts now on record:** weasyprint cannot load Homebrew's pango from `/usr/bin/python3`, so it lives in `.venvs/pdf` on Homebrew Python 3.11; opacity on SVG text makes weasyprint clip the line; gpt-image-2 at high quality cannot be called from the Claude Code shell because the connection drops at 60 seconds, low works and high is a native Terminal job; macOS puts a narrow no-break space before am and pm in screenshot names, so match with a glob rather than a pasted path; images pasted into chat cannot be saved to disk, ask for the file in the folder.
- **Hugo is not on Gmail.** The Gmail connector is not his client mailbox. Lucy's mail arrives as pasted text, screenshots, or files dropped in the client folder. Two empty searches were spent learning this; it is now an auto-memory.
- **A first-sentence cap needs a floor,** or a brief reads "THE 3D BAND." and says nothing. The rule is keep taking sentences until past half the cap.

### Open questions still unresolved
**Resolved (by a later session this week):**
- [x] ~~Q-033: which peach is the logo peach~~ RESOLVED Session 039: Pantone 162 C, screen `#FFBE9F`, on her printer's match (D-051).
- [x] ~~Q-011: collection grid colourway sign-off~~ RESOLVED Session 039: she signed off by posting it.
- [x] ~~Q-035: Lucy's answer on what to work on next~~ RESOLVED Session 040: she asked for a stop-motion inspiration board, which became Q-036.
- [x] ~~Q-019: poster 2 re-run~~ RESOLVED Session 041: `gen_poster_1b.py` with the band written as a closed loop crossing both thighs, two correct low candidates, high plate dropped as not needed.
- [x] ~~Q-037: the token diet~~ RESOLVED Session 041: all five moves plus Hugo's three additional calls, measured, and written up as standing policy (D-054).
- [x] ~~Q-025: build the shot 01 colourway test~~ RESOLVED Session 041 as a build: `build_colourway_compare_shot01.py` rebuilds Hugo's own placement in all three colours. The decision half is still open below.
- Note: Session 041 is the most recent session and no later session exists, so nothing in its own open loops can be flipped yet.

**Still open, opened this week:**
- [ ] **Q-036: Lucy's four answers on the inspiration board,** then the loop build. Where it will live, what the board is about, what goes on it, whether it carries words. The build is `scripts-local/build_inspiration_board_mock.py` extended to about 34 frames at 140 ms, out as a 600px GIF for email and 1080x1350 MP4 for Instagram. Blocked on her only.
- [ ] **Q-034: the signature original,** file or font name. The 156x70 email crop is fine for a card and not good enough for an animated write-on.
- [ ] **Q-038: composition end cards** still carry the old mark, the handle, and a "Launching September 2026" line. Opened S041, needs nobody.
- [ ] **Q-025, decision half: Hugo picks the shot 01 colourway** from `lucyfriend-band-placement/plates/colourway-compare/`. One look, one answer. Prediction on the post-grade separations is MEDIUM, with HEAVY at minus 4 confirming it sinks into the floor.

**Still open, carried from before:**
- [ ] **Q-027: the Fit Expo booth email.** Owed in writing since 08-27, now deferred by Hugo rather than blocked, and the date correction (TheFitExpo LA listed 23 to 24 January 2027, not February) makes the runway three weeks shorter than Lucy's intake assumes. Should carry panel dimensions and bleed, the handle rule (Q-028), the Canva print and event licence check, and the four older picks.
- [ ] **Q-013: back catalogue to 162 C and the master mark.** Mostly done in S041 for the band posters and three compositions; the remainder is on the row. The delivered ads and posters are explicitly NOT part of this until Hugo asks.
- [ ] **Q-016: the 3D band, still one photograph away.** Shape proven (D-048), shoot list validated, and it shares a sitting with Q-023 (band dropped on a floor) and Q-020 (label close-ups). Untouched for three weeks.
- [ ] **Q-028: the handle rule** (off for Instagram, on for booth assets). One line, confirm back to Lucy.
- [ ] **Q-001: standalone waitlist capture page plus 3-email welcome flow.** Top unbuilt item in ten separate sessions now. Needs neither Lucy nor the trademark.
- [ ] **Colourway strips, range card and wholesale line sheet.** Unblocked by the measured colours four weeks ago and now, finally, by a settled brand colour. Still unbuilt.
- [ ] **Q-002: trademark clearance,** still the critical-path gate on Lucy's lawyer's clock, with Shopify, prices, the pouch threshold and the fabric all behind it.
- [ ] **Parked behind `[p]`:** Q-001 to Q-010 and Q-026, visible with `open --parked`. Includes Q-010 (native-terminal band-swap renders, then email-03), Q-008, Q-005, Q-006, Q-004, Q-003, Q-026 (Lucy's email-02 treatment pick).
- [ ] Carried: ambassador and instructor seeding shortlist (thirteenth week, needs nothing from anyone), film the unboxing, ElevenLabs API key, Shopify store, materials question, Stage 3 synthesis template, Q-017 Gemini egress, Q-014 Hugo's Photoshop reference.

### Suggested focus for next week
1. **Send the Fit Expo booth email.** It is the only item on the board with an external deadline, it has been owed in writing for seventeen days, and it is now deferred rather than blocked, which means it is a choice being made weekly. One message asking for show confirmation and dates, panel dimensions and bleed, the Canva licence for print and event display, confirming the handle goes back on, and folding in the four older picks. One message has beaten five every time it has been tried.
2. **Spend twenty minutes with the phone and close three loops at once (Q-016, Q-023, Q-020).** Geometry shot in shade as an open oval so the hole reads, then step into direct sun for the dropped band and the label close-ups per D-026. Then one Tripo run with the real image. This has been the number one or two recommendation for three consecutive reviews and is the largest unblock available for the smallest effort.
3. **Build the commercial assets on the settled colour.** Colourway strips, range card and wholesale line sheet have been unblocked by the measured band colours since August and were missing only a settled primary brand colour, which 162 C now is. The measured colours, the corrected cutouts and the tight parallel trios from shoot 5 are all already in the workspace, so this is a build with no external dependency and nothing left to decide.

---
## Session 041 (2026-09-12, Claude Code): The token diet, then the three loops the workspace could close alone

Client: Ochoproductions, Sportif
Tags: ochoproductions, sportif, memory-system, token-diet, startup, closeout, band-placement, colourway, poster, ig-ads, master-mark, pantone-162c, hyperframes

**Done.** Part one, the token diet (Q-037, all five moves). `memory_tools.py open --brief` prints one line per loop and `startup.py` uses it; Q-001 to Q-010 parked with `[p]`, which `memory_tools.py` now understands; "Tools and gotchas" moved to `docs/gotchas.md`, named by startup and never printed; the top-entry read dropped from CLAUDE.md and `/startup`; the handoff line cut to three sentences; five-heading template in `docs/memory-system.md` with `closeout.py` warning past 500 words, a missing heading, or a four-sentence handoff. Then, on Hugo's calls: CURRENT STATE cut to 10 D-number pointers, the oldest weekly review archived, Q-026 parked. Part two, the three loops needing nobody. Q-025: `build_colourway_compare_shot01.py` lifts Hugo's placement out of the shot 01 PSD and rebuilds it with LIGHT, MEDIUM and HEAVY, colour the only variable. Q-019: `gen_poster_1b.py` with the band written as a closed loop crossing both thighs; two low candidates both correct. Q-013: band posters rebuilt and the three compositions re-rendered in 162 C. The three Lucy posters and three IG ads were also moved to the master mark through a new shared `house_lockup.py`, and Hugo had that reverted when he saw it: scripts and files restored, the module kept unused.

**Measured** (characters divided by four). Startup print 4,709 to 2,003 tokens (open loops 2,845 to about 480 with the cap at 100, CURRENT STATE 1,144 to 722). CLAUDE.md, paid every turn, 2,810 to 1,289. Close-out entry 1,106 to about 700.

**Learned.**
- A first-sentence cap needs a floor: "THE 3D BAND." says nothing, so the brief keeps taking sentences until it passes half the cap (50 characters at the 100 cap).
- Photoshop's rotation sign is the reverse of Pillow's. The PSD layer is the check: +101 in Pillow matched Hugo's -101 at 20/255, the other sign at 88/255.
- Post-grade, band against the floor around it, the separations are LIGHT +19, MEDIUM +9, HEAVY minus 4. The S034 numbers (42/31/12) were pre-grade against the bare floor.
- gpt-image-2 at high quality cannot be called from the Claude Code shell, the connection drops at 60 seconds. Low works; high is a native Terminal job.
- Ask before touching delivered creative. The ad and poster rebuilds followed settled decisions, but Hugo had not asked for them and reverted the lot. Settled is not the same as wanted now.
- The band geometry failure was wording, not references: "one closed loop that encircles BOTH thighs, perpendicular to the legs" fixed it first time.

**Decided.** D-054, the token diet rules as standing policy.

**Open.** Q-038 new (composition end cards: old mark, handle, and a "Launching September 2026" line). Q-025 resolved, Hugo picks the colourway. Q-019 resolved, the high plate dropped as not needed. Q-013 mostly done, remainder listed on the row. Q-037 resolved. *(Weekly review 2026-09-13: this is the most recent session, so no later session exists to resolve anything here. Q-025's decision half, Q-038 and the Q-013 remainder all carried forward unchanged.)*

**Next.** Lucy's replies (Q-036, Q-034); then Hugo's colourway pick.

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

## Session NNN, YYYY-MM-DD, One-line summary
### What we did
### What we learned
### Decisions
### Open questions / next steps
-->
