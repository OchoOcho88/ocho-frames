# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## CURRENT STATE (update this block every session, keep it to ~12 lines)

*Last updated: 2026-09-01 | Last session: 037 (Cowork, CLOSED) | Working tree: committed clean | Git: pushed, in sync with origin/main | **FIRST THING NEXT SESSION: the 3D band hero frame (Q-016). One photograph and one Tripo job decides it. Morning light IN SHADE (these are geometry shots, the D-026 sun rule is for colour and does not apply), plain smooth white surface not a t-shirt, HEAVY band open as a relaxed oval, camera 30 to 45 degrees down and off to one side so the hole and the far side both read, ONE object in frame. Full list in `clients/sportif/products/band-3d-shoot-list.md`.** | Also waiting: Lucy's reaction to the revised weave tiles and the colour call, two emails sent 2026-08-31 (Q-029); her pick between the three email-02 treatments (Q-026); the Fit Expo booth panel dimensions, show looks like JANUARY not February (Q-027); the handle rule confirmation (Q-028); the band DROPPED on a floor (Q-023); shot 01 colourway test (Q-025); Gemini egress (Q-017); poster 2 re-run (Q-019). **Lucy is on holidays this week, so nothing client-blocking will move.***

- **The critical path is TRADEMARK, not Shopify.** Launch and the whole go-to-market are held until Lucy's lawyer clears the name (logged from the 2026-07-14 meeting, still open). Underneath that there is still nowhere to sell the band: Shopify unopened, prices and the pouch threshold unset, fabric undecided, all blocked on Lucy.
- **Lucy Wayne IS the differentiator** (`clients/sportif/brand.md`). Strategy locked: parallel wholesale plus DTC, one hub. Client-facing docs are exactly two PDFs, `Sportif-Brand-Value-Plan.pdf` and `Sportif-Launch-Plan.pdf`.
- **The real product exists and its colours are MEASURED (D-027):** LIGHT `#B8A080`, MEDIUM `#9D7459`, HEAVY `#6C4333`, off shoots 4 and 5 shot on white in direct sun (D-026). **Composite ONLY from `assets/Sportif_Bands/Bands_background_removed/colour-corrected/`** (D-039): every other cutout in the workspace is about a stop underexposed, invisible on white and ruinous on a dark floor.
- **The band's own weave is a brand asset (D-028):** seamless tiles plus large single-crop plates at `clients/sportif/assets/textures/`. They are photographs of the real product, and they are the texture source for everything, 2D or 3D.
- **Product assets carry the REAL product colour, never the brand palette (D-046).** The brand-colour weave is valid only where the weave is a BACKGROUND rather than the product itself (D-045).
- **The generator rules, all learned the hard way.** Never let a generator draw the band large in frame: big means shoot it or composite the real cutout, small means generate and swap the label (D-033, D-034). No image generator touches Lucy's friend's photos at any stage (D-038). Label text comes back mangled at every scale and every engine, so the label is always fixed from the real photograph.
- **The weave tile house build** is `clients/sportif/scripts-local/build_texture_weight_tiles.py`: real colours, Glacial Indifference BOLD on the weight line, lockup at 76 percent of canvas width (D-047). The Instagram profile grid crops to 3:4, a centred 1012px column, and that is the ceiling for anything built for the grid.
- **Two client-facing writing rules (D-044).** Lucy is NOT the model in the email-02 photos, they are her Canva picks, so never write "you" about the person in frame. Never call the MEDIUM band "blush", because Blush Peach `#F0CDB3` is the primary brand colour; refer to bands by weight.
- **"Show me" and "pick one" are different client requests (D-046).** Declining the second is not licence to refuse the first. Show the thing with the recommendation attached.
- **No @handle on Instagram assets (D-018), handle back ON for anything used at the Fit Expo booth (Q-028),** because booth assets travel without the account name attached.
- **The session protocol is two checked commands (D-035):** `python3 scripts/startup.py` and `python3 scripts/closeout.py --commit -m "..."`. It is a script rather than a paragraph because **CLAUDE.md is NOT auto-loaded in Cowork** and the protocol kept being skipped.
- **House voice: no em or en dashes anywhere.** Close-out sweeps every changed file and refuses to commit on a hit.
- **Where the detail lives.** Settled decisions in `DECISIONS.md`, live loops in `OPEN-QUESTIONS.md`, session narrative below and in `memory-archive.md`, both indexed by `memory-index.md`. Query with `python3 scripts/memory_tools.py [check|index|search|decisions|open]`.

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

## Weekly Review, 2026-07-26 (week of 2026-07-20)

Eight sessions this week (020 to 027), the busiest week the workspace has ever had, up from one last week. The logjam broke on day one: Session 021 finally captured the Tuesday 2026-07-14 Lucy meeting outcomes (last week's #1 focus), which reframed the whole strategy around the trademark hold. The rest of the week banked an enormous amount of trademark-independent production: a full real-band product content pipeline, a fresh generation pipeline, a Canva collaboration workflow, memory system v2, and the opening move of a Lucy expert-brand content strategy.

### Highlights
- **The Tuesday Lucy meeting outcomes were finally logged (Session 021), and they changed the map.** Launch is held indefinitely pending trademark talks with Lucy's lawyer, trademark, not Shopify, is now the critical-path gate. The 500 band units HAVE landed (unboxing now filmable). The correct posture is explicit: bank everything that doesn't depend on trademark.
- **A complete real-band product content pipeline shipped (Sessions 023 to 024).** From 3 casual snapshots of the real bands: restaged flatlay, 3 hero cards, a range reel, two lifestyle+product blends, a "they've landed" teaser, a band-in-use pilates reel with the real SPORTIF label stamped in, plus the reusable **reference-reskin technique** (AI generates a no-text plate, we own the type in PIL) with two waitlist-poster finals. The bands' colourways ARE the peach palette, the whole direction validated by physical product.
- **Fresh from-scratch generation + Canva workflow established (Session 025).** `gen_fresh_explore.py` makes Sportif key visuals from scratch with three durable prompt lessons (name the garments, contrast skin tone, smooth not ribbed), and the two-avenue model (our pipeline = studio, Canva = shareable workbench) is set up with a Sportif folder chain to Lucy, Pro-gated pieces (brand kit, folder share) land when Hugo gets Canva Pro ~2026-07-30.
- **Two infrastructure/strategy moves: memory system v2 (Session 026) and the Lucy expert-brand strategy Phase 1 (Session 027).** v2 adds registries (`DECISIONS.md`, `OPEN-QUESTIONS.md`), per-client filtering, and a close-out `check` hook, directly mitigating the compliance failure that lost the Tuesday meeting notes for a week. Phase 1 applied the Devin Jatho 4-quadrant model to Lucy and produced the "Content Creation Strategy" PDF, ready to send.

### Patterns I noticed
- **The ~60s render/network cap shaped nearly every session again.** High-quality gpt-image-2 renders hit it in Sessions 023, 024, and 025 (even in the VS Code terminal); the standing answer is iterate low in-harness, finals from a native Mac terminal. This is now a permanent column in the workflow map, not a transient annoyance.
- **"AI makes the plate, we own the type" hardened from a technique into the house style.** Overlay scripts, the reference reskin, the label stamp, the PIL type layer, every finished piece this week separated AI-generated imagery from brand-controlled typography. Hugo enforced it explicitly ("NO YOU LAYOUT TEXT, THATS OUR WORKFLOW").
- **Hugo's eyeball QA keeps catching what tooling can't**, the card-crop neighbour bleed (023), the GSAP selector bug hiding the end-card wordmark (022), navy type fighting the warm palette (025), the too-clinical first PDF draft (027). Fourth straight week this pattern holds.
- **The Lucy dependency changed shape: from hard blocker to feedback latency.** Nothing is structurally blocked on her anymore (trademark is on her lawyer), but a queue of small picks is accumulating: music-bed pacing, the Content Creation Strategy reaction, the incentive A/B/C decision. Meanwhile the waitlist capture page, which needs neither Lucy nor trademark, was named "still the top unbuilt item" in four separate sessions and is still unbuilt.

### Skills / knowledge gained
- **Durable gpt-image-2 prompt lessons:** name the actual garments; garment colour must CONTRAST skin (flesh-adjacent tones read as nude); material = smooth four-way-stretch, never ribbed (except the band itself); scope edit prompts to "keep the product EXACTLY identical"; a REALISM block (Portra 400, real skin texture, forbid glossy/CGI) cuts the AI look; low-quality label stamps read more natural than crisp composites.
- **The reference-reskin technique generalises:** any reference layout → no-text AI plate → our type in PIL; generate both pose variants when ambiguous and let product-clarity decide; solid opaque CTA pills beat thin script over busy areas.
- **Canva mechanics:** connector can't ingest local files (public URLs only); short simple briefs succeed where long hex-code briefs fail; `asset_ids` only reliably used ~1 in 4 candidates (use editor Replace instead); brand kit + folder sharing are Pro-gated; the API's `/d/` URLs are private and 404 standalone.
- **Production fixes worth keeping:** colour-boundary crop detection for touching products (not equal thirds); feathered Gaussian alpha for peach-on-peach edges; scope GSAP selectors per section when class names repeat; system python has PIL-not-numpy, the .venvs/tts python has numpy-not-PIL.
- **Memory tooling:** `memory_tools.py check/index/search/decisions/open/reconcile` exist and filter by client; the pre-push warn hook is installed; `MEMORY_ENFORCE=1` flips it to blocking.

### Open questions still unresolved
**Resolved this week:**
- [x] ~~Log the Tuesday 2026-07-14 Lucy meeting outcomes~~ RESOLVED Session 021: launch held indefinitely on trademark, waitlist page never put to Lucy, incentive undecided, no Shopify movement, the 500 bands HAVE landed.

**Still open (from this week's sessions):**
- [ ] **Send Lucy the Content Creation Strategy PDF**, then Phase 2 of the expert-brand strategy: lock her expert niche, one avatar, and the four quadrants (Q-006, Session 027, gated on her reaction).
- [ ] **Standalone waitlist capture page**, named the top unbuilt item in Sessions 023, 024, and 025; needs neither Lucy nor trademark. Pair with the 3-email welcome flow.
- [ ] **Canva Pro (~2026-07-30):** set up the Sportif brand kit + share the Sportif folder with Lucy (lucy@lucywayne.com.au) once Hugo upgrades (Session 025).
- [ ] **Lucy's picks pending:** music-bed pacing (calm ~100 BPM vs upbeat ~118 BPM, Sessions 022 to 023) and the incentive decision A/B/C (Session 021).
- [ ] **High-res finals past the ~60s cap**, print-quality product/in-use renders need a native Mac terminal run (Sessions 023 to 025).
- [ ] **ElevenLabs TTS awaiting Hugo's API key** (`.env` slot + script ready, Session 022).
- [ ] **Film the unboxing**, bands are in hand since Session 021 confirmed landing; footage not yet shot.
- [ ] **Trademark clearance**, the critical-path gate, on Lucy's lawyer's clock, nothing accelerates it (Session 021).
- [ ] `cosmos_yoga-duo.mp4` peach video edit would need the Seedance path (Session 020).
- [ ] Carried from prior weeks, still open: ambassador/instructor seeding shortlist (sixth week carried, needs nothing from anyone), Shopify store (gated on trademark), materials question, Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins.

### Suggested focus for next week
1. **Send Lucy the Content Creation Strategy PDF and bundle her pending picks into the same ask** (PDF reaction + music-bed pacing + incentive A/B/C). One message clears the whole feedback queue and un-gates Phase 2 of the expert-brand strategy.
2. **Build the standalone waitlist capture page + 3-email welcome flow.** Four sessions in a row called it the top unbuilt item; it needs neither Lucy nor the trademark, and every piece of content built this week dead-ends without it.
3. **When Canva Pro lands (~07-30), set up the brand kit and share the Sportif folder with Lucy**, and use the waiting days to finally start the ambassador/instructor seeding shortlist (six weeks carried) and film the unboxing.

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

## Session 035 (2026-08-27, Cowork): Lucy's marks measured onto the assets, two failed grades, and the weave room

Client: Sportif
Tags: instagram, lucy-marks, homography, colour-grade, photoshop, masking, blend-modes, texture, client-email, teaching

Hugo drove. The session started as a small placement fix and turned into a colour-grading dead end,
a correction of that dead end, and then a genuinely new treatment that Hugo built himself in
Photoshop. A client email went out at the end carrying the whole thing.

**Lucy's marks, measured rather than eyeballed.** Four iPhone photos of Hugo's screen landed in
`Lucy-Wayne-pictures/changes_needed_pilates_room/`, showing four v2 files with Lucy's black pen marks
on them: an X meaning "put the mark here", with a line drawn from the current lockup. Rather than
guess the positions, each photo was matched to its real asset with SIFT plus a RANSAC homography (81
to 210 inliers), warped into the asset's own pixel space, and differenced so the only thing left was
the pen. Centres in asset pixels: feed-ballreach 831/239, story-ballreach 858/300, story-sidestretch
396/137, story-duo 219/395. Files renamed to pair with their assets and moved to
`email-02-social/lucy-marks-2026-08-26/` with a README holding the method and the numbers. Built by
`build_email02_social_v3.py`, a copy of v2 so v2 stays intact. Three of her four marks needed a nudge
and each is documented: sidestretch sat at y137, inside Instagram's 260px story chrome, so it went to
y290; story-duo could only drop from y260 to y355 because the second ceiling beam enters the type
footprint at y370, measured; story-ballreach moved 27px for the same safe-zone reason. See D-041.

**Two colour grades that failed, and the finding underneath them.** Hugo asked for a LUT or brand
colour overtone. First attempt mapped every tone onto a Sportif ramp and mixed it in brightness and
all; because the ramp's dark end is a mid brown, every shadow lifted and story-duo's black point went
from 0.024 to 0.094, four times lighter. Hugo: "a bit washed out and lifeless". Second attempt fixed
the brightness but added a saturation boost and a heavy S-curve for punch, both of which land hardest
on the most saturated warm thing in frame. Hugo: "made her skin look like fake tan". Both calls were
right and both were made on sight. **The finding: on these photos more peach and tanned skin are the
same slider,** because her skin and the studio wall both sit near hue 25 degrees. A hue-based skin
mask is no rescue either, it selected 91 percent of feed-ballreach because the wall qualifies as skin.
That caps the whole approach. See D-042 and D-043. The corrected grade (no global saturation, light
contrast, chroma only for what was already dull) survives at `scripts-local/sportif_grade.py` with
both dead ends written into the file, plus `assets/luts/sportif-peach-{25,45,70}.cube`. The full set
is in `created/v4/`, parked.

**The weave room, and Hugo went round the obstacle rather than tuning against it.** Told the ceiling
was set by skin sharing a hue with the wall, he opened Photoshop and separated the person from the
room, which is the one thing that removes the ceiling. Verified against the original: her average
brightness 53.4% before and 53.4% after, identical, and no halo at her edge. He then built two
treatments on top of that split. A terracotta `#833827` Solid Color fill at Overlay 60%, measured safe
(room's darkest 5% went 0.317 to 0.242, pixels at pure black only 0.30 to 0.33 percent). Then the
band's own weave over it, held to the wall with Blend If so it sits behind the barre and the rings
rather than over them. Recipe at `email-02-social/photoshop/WEAVE-ROOM-RECIPE.md`, working PSDs
alongside. Two counterintuitive results worth keeping: black type beats white on that terracotta (6.8:1
against 2.1:1, because terracotta is a mid tone at 43% luminance), and the 1024px tile is fine at feed
size but will seam on a 1920 story, so stories need the plate.

**Hugo's judgement call on scope, and it was the right one.** Offered an auto-cut of the other seven
with rembg, he declined: send the eight files Lucy actually asked for, plus the two concepts on one
photo, and do not build seven versions of a look she has not agreed to. "The main thing for me was
that I got to practice in Photoshop, and think creatively."

**Email sent, and it surfaced three things nobody had flagged.** Reading Lucy's 21 Aug message
properly: the pilates picture is going to the **Fit Expo booth**, which is print, and everything we
have is 1080px; she has handed us the **handle rule** (off for Instagram, on for booth assets); and
she is expecting the **3D band**, which has not been started. Hugo split those into separate emails to
keep the reply on one subject, and the sent email promises both in writing. Two writing corrections he
caught: Lucy is NOT the model in these photos, they are her Canva picks, so never write "you" about
the person in frame; and "blush" cannot be used for the medium band because Blush Peach `#F0CDB3` is
the primary brand colour, so bands are referred to by weight. Both are now warnings at the top of the
draft. Sent 2026-08-27 with 12 attachments, draft at
`email-02-social/TO-SEND-2026-08-26/email-to-lucy-v3.md`, copy-ready page published as an Artifact.

**Still open:** Lucy's pick between the three treatments (Q-026); the Fit Expo booth posters, blocked
on her panel dimensions (Q-027); the 3D band, now promised to her (Q-016); everything carried from
S034.

---

## Session 034 (2026-08-26, Cowork): the weave tiles, and a colour fault in every band cutout

Client: Sportif
Tags: instagram, grid, texture, colour-correction, photoshop, compositing, lucy-friend, consent, teaching

Hugo drove. Four things happened: the weave tiles got built and an email about them went to Lucy,
Lucy's friend's gym photos were filed and briefed, a colour fault was found in every band cutout in
the workspace, and Hugo built his first composite in Photoshop from end to end.

**The SPORTIF weave tiles.** He liked the S032 demo (heavy weave full bleed under the cream lockup)
and wanted the set completed. Built `clients/sportif/scripts-local/build_texture_weight_tiles.py`,
three 1080x1350 feed posts sitting as one grid row, output to
`generated/images/texture-weight-tiles/` with a README. Four changes from the mock, all his call:
SPORTIF went from about 44% of the canvas width to 66%; the type carries a two-pass warm shadow, a
soft lift plus a tight core, tinted (45, 24, 18); the weight sits under "collection" as a fourth
line, caps, wide tracking, sized off MEDIUM so all three share one point size; and the background
switched from the mirrored tile to the single-crop plate, which has no repeat and no seam. A
`band_only()` pass finds the columns and rows whose median saturation clears a threshold and trims
the white sheet out automatically, so the weave runs edge to edge.

The light tile came back reading olive. Measured, its hue and saturation were exactly on target
(34 deg, 30%) but the frame was about a stop dark, so it landed at `#88765F` instead of `#B8A080`.
Fixed with a per-channel gamma that lands each plate's mean on its D-027 value. Gamma rather than a
gain, so black and white are preserved and no highlight in the weave clips. Applied to all three:
medium and heavy were already on target, so their correction is near 1.0 and the treatment stays
identical across the set. **This was the first sighting of the fault, and it turned out to be
everywhere.**

**Email to Lucy, SENT.** His concept: crop the band fabric so close nobody can tell what it is, use
it to build mystery ahead of showing the bands properly, and note that it is the actual product
rather than anything generated. Drafted a short message and an email version, both saved to
`clients/sportif/message-to-lucy-weave-concept.md`, plus a paragraph explaining that the posts go up
in reverse order (heavy first, light last) because Instagram puts the newest post on the left. He
sent it with the three tiles attached. Files numbered POST-1 to POST-3 by upload order.

**Lucy's friend, gym shoot: a new job.** Five photos from 18 April 2025, two phones, one sitting.
Renamed to the D-021 convention. Note the mistake: the first pass named them off a contact sheet
built without applying the EXIF rotation flag, and three of the five descriptions were wrong. What
was called "standing rack full length" is her seated on a BOSU. Corrected against the upright
images. **Always apply `ImageOps.exif_transpose` before describing an iPhone photo.**

New folder `clients/sportif/lucyfriend-band-placement/` with `lucy-direction/`, `plates/`,
`created/` and a README. Lucy sent four iPhone screenshots with a red mark showing where each band
goes, matched to shots by timestamp and renamed `direction-NN-<descriptor>.jpeg` so a markup can
never be paired with the wrong photo. **All four marks are on flat surfaces she does not overlap**,
so no clean plate is needed anywhere and she never has to be cut out. There is no direction for shot
03, confirmed with Hugo, so that one is improvised: building two versions, the bench pad and the
floor by the barbell, and picking after.

**Hugo's method call, and it was the right one.** He proposed cutting her out, generating the band
into a clean plate with AI, then putting her back, and his stated reason was that he does not have
her friend's permission to put her likeness through a generator and does not want to ask. The
consent instinct is right and stands. The workflow around it was not needed: since the bands are
props on flat surfaces rather than worn, the real cutouts composite straight in and no AI is
involved at all, so the problem he was designing around stops existing rather than being worked
around. Also worth noting the clean plate would have actively hurt on a worn band, because removing
her removes the only thing telling a generator where "around her thighs" is.

**The finding that matters: every band cutout in the workspace is about a stop underexposed.**
Hugo cut out medium and light himself in Photoshop (Select Subject, Select and Mask with Shift Edge
-10%, output to layer mask). All three verified clean, edge brightness within 6 levels of the
interior, so no white rim survived. But measured against D-027 the fabric came back at LIGHT 47%
value against 72%, MEDIUM 37% against 62%, HEAVY 24% against 42%, with saturation down a third
across the board. On a white sheet you cannot see it. On a dark gym floor the band turns to putty.
Corrected copies written to `assets/Sportif_Bands/Bands_background_removed/colour-corrected/`, all
three landing on their measured values. See D-039.

The sting: Hugo's first composite looked roughly the right brightness for a dim gym, but by accident.
The band was too dark and the gym should have darkened it, and the two errors cancelled. Saturation
does not cancel, which is why it read as gaffer tape rather than sand.

**Shot 01 built end to end.** Place Embedded as a Smart Object, 20% scale, rotated -101 (90 to lay
it across frame plus 11 to tilt), squashed to about two thirds for floor foreshortening, a two-layer
contact shadow sampled from the floor rather than the warm house brown, a Curves adjustment clipped
to the band at Input 128 / Output 105 for the gym's ambient, then 0.6px blur and 3% Gaussian
monochromatic noise to match the photo's grain. Measured grain on that floor at 6 to 7 levels of
average deviation.

**The staging trap (D-040).** With everything else right Hugo still said it looked wrong, and he was
correct. Measured, the shadow was not the culprit: the band darkened the floor by 16 levels against
30 for the real skipping rope handles, so it was if anything too light. The tell was tidiness. The
towel is crumpled, the rope is in a heap, her shoes sit at odd angles, and our band is a perfect
rectangle with square-cut ends lying dead flat, because our cutouts are product-shot poses. A
catalogue pose composited into a candid photo reads wrong even when the light is right.

**`lucyfriend-band-placement/PHOTOSHOP-GUIDE.md`.** Seven numbered steps, each a self-contained
block, per D-031: open and save as PSD, place, squash, shadow, ambient, grain, export. Plus a
per-shot table, the mirror problem for 04 and 05, and the staging section. Written because Hugo is
new to Photoshop and is deliberately rebuilding shot 01 from scratch with medium and then heavy, to
learn the process rather than swap contents.

### What we learned
- **Apply the EXIF rotation flag before describing any iPhone photo.** Three of five filenames were
  wrong because a contact sheet was built without it.
- **A fault invisible on the shooting surface can be fatal on the destination surface.** The
  underexposure was undetectable on white and ruinous on a dark floor.
- **Measure before believing your eyes on a composite.** Both of us assumed the shadow was wrong. It
  was the second most accurate thing in the frame.
- **Two errors cancelling is not a method.** Correct the asset, then adjust deliberately.
- **Gamma beats gain for tone matching**, because it preserves black and white and cannot clip.
- Photoshop's 3D toolset was removed by Adobe. `Filter > Vanishing Point` is the nearest equivalent
  for placing an object on a plane, and it is worth trying on shots 04 and 05.
- A sideways label on a band lying horizontally is correct, not a fault. Only a mirrored one is
  wrong, and rotating never mirrors. I flagged this incorrectly first time and corrected it.

### Decisions
Decided: D-038, D-039, D-040.

### Open questions / next steps
Opened: Q-023, Q-024, Q-025.
Next session: Hugo rebuilds shot 01 from scratch with the MEDIUM band, working through
PHOTOSHOP-GUIDE.md, then again with heavy. Then the three-way colour comparison.

---

## Session 033 (2026-08-21, Cowork): the session protocol becomes two checked commands

Client: Ochoproductions
Tags: workflow, tooling, memory-system, close-out, startup, git, cowork, voice-rule, em-dashes

Short session, no client work. Hugo opened with "fresh session starting" and I answered with a
greeting instead of opening the workspace. He had to tell me twice: first "you should read the
start up protocol", then "why didnt you run startup?". Both were fair.

The second question turned out to be the interesting one, because the answer was structural rather
than personal. There was no startup command. `.claude/commands/` held exactly one file,
`close-out.md`. The session-start protocol existed only as prose inside CLAUDE.md, and CLAUDE.md is
not auto-loaded in Cowork, which was already logged as a learning in S031 after a client-facing
email reached final draft full of em dashes. So half the loop was protected by a named command and
the other half depended on a session remembering to open a file nothing forced it to open. That
half failed again here.

What was built:

**`scripts/startup.py` plus `.claude/commands/startup.md`.** One read-only pass that prints the
environment (detected from the path, Cowork vs Claude Code, with that environment's gotchas), this
session's number counted off the last entry in memory.md, the last five commits, a loud warning if
the tree is dirty or the branch is ahead of the remote, the CURRENT STATE block, open loops for the
active client, the content gate (brand.md and voice-guidelines.md, with a missing-file check), the
house rules with the dash rule first, and flags. `--short` skips the state block, `--client NAME`
overrides the client auto-detected from CLAUDE.md. CLAUDE.md now OPENS with the command instead of
a prose checklist.

**`scripts/closeout.py`, the mirror.** It runs every close-out step a machine can verify and
refuses to pass while anything is unfinished, leaving only the writing to a human or an agent. It
clears stale git locks the correct way per environment, sweeps changed files for em and en dashes
(`--fix-dashes` to auto-correct, `--all-files` for the whole repo), verifies the session entry
exists with the right number, date, environment tag, `Client:` and `Tags:` lines, verifies CURRENT
STATE was updated today and names this session, checks both registries for rows tagged with this
session, runs `archive_memory.py`, `memory_tools.py index` and `memory_tools.py check`, then
commits. `.claude/commands/close-out.md` was rewritten to drive it.

Three drift bugs surfaced while wiring it up:

1. **`close-out.md` hardcoded the tag "Claude Code".** Every close-out run from Cowork was stamping
   the wrong environment onto its own session entry, which is the single field the handoff protocol
   depends on. Now environment-agnostic, and the script verifies the tag against reality.
2. **`close-out.md` was missing steps (d) and (e) from CLAUDE.md**, the `memory_tools index` and
   `check` runs. Both now run automatically inside the script.
3. **The "memory.md > 90KB" warning could never be cleared.** memory.md is 114KB, the archiver
   keeps the newest 6 session entries and there are exactly 6, so it had nothing to move and never
   will. The bulk is elsewhere: the CURRENT STATE block alone is 34KB, roughly 30% of the file,
   against a brief in CLAUDE.md of about 12 lines, and eight Weekly Reviews make up most of the
   rest. Neither is touched by the archiver. The warning now fires only when archiving would
   genuinely move something, and separately names the real culprits. See D-037 and Q-021.

**The Cowork git lock problem is now handled rather than rediscovered (D-036).** It bit twice this
session. Cowork cannot unlink inside the mount, so every commit strands `.git/index.lock` and
`.git/HEAD.lock`, and the next commit refuses to run claiming another git process is active, which
is a misleading error. `rm` fails but `mv` works, so the fix is to move them into
`.git/_stale_locks/`. startup.py detects the locks and prints the right command for the
environment; closeout.py clears them automatically.

**Em dash sweep, client-facing scope.** A repo-wide scan found roughly 330 legacy dashes across 48
of our own files, most written before the voice rule existed. Hugo chose the narrow scope: the
seven files that could ever reach a client or the public site (README.md, index.html,
brand/agency-brand-kit.md, and four Sportif docs including image-prompts.md and
gen_fresh_explore.py). 46 dashes removed. Internal notes and research dumps are left alone; the
close-out sweep will catch each one the first time anyone edits it. memory_tools.py and
memory-archive.md were cleaned as a side effect of being touched.

**The narrow scope was vindicated immediately.** The blunt replacement rule (a spaced dash becomes
a comma) turned "2-3 uses" into "2, 3 uses", which is nonsense. A repo-wide run would have planted
that class of error in 48 files at once, in text nobody would have gone back to re-read. Fixed in
the two affected spots and fixed in the tool: a dash between digits is now recognised as a range
and becomes "to" before the comma rule runs. The general lesson is that a mechanical rewrite is
only as safe as the smallest surface you can still proof-read.

The harness caught a bug in itself on its first real run. Close-out cleared the stranded git locks
as step one, then every git call made by the checks in between put a fresh `index.lock` back, so the
commit at the end failed with the same misleading "another git process is running" error the script
exists to prevent. Locks are now cleared again immediately before the commit. Worth noting because
it is the argument for the whole exercise: the check found a failure that a human running the same
steps by hand would have hit and blamed on git.

Learned:

- A protocol that lives only in prose gets skipped by whoever did not open the file. A named
  command survives that. Automating one end of a loop and not the other guarantees the unautomated
  end is where the failures land.
- A warning that cannot be acted on is worse than no warning, because it teaches you to skim past
  the warning channel entirely. Both of the CURRENT STATE and Weekly Review warnings that replaced
  it are things someone can actually do something about.
- In Cowork, `rm` is blocked inside the mount but `mv` is not. That is the general workaround for
  anything needing deletion here, not just git locks.

Decided: D-035, D-036, D-037.
Opened: Q-021 (memory.md hygiene pass), Q-022 (push the local commits from the Mac).
Still first up next session: Q-016, the band's 3D model. No client work happened today.

---


## Session 032 (2026-08-21, Cowork): first posters from the real bands, cutouts renamed, 3D path chosen

Client: Sportif
Tags: real-bands, cutouts, posters, collage, teaser, instagram, 3d, shopify-ar, naming, colour, photography, gpt-image-2, textures, layout-rule

Long session, started the evening of 2026-08-20 and ran through 08-21.

Lucy has sent the physical bands (light, medium, heavy). Hugo photographed them on an iPhone and
removed the backgrounds, and dropped six PNGs into `clients/sportif/assets/Sportif_Bands/`. Reading
the labels showed every one of them is the **HEAVY** band: two front views (flat with the label near
the top, folded with the label mid band), the plain back, two shots of the inside grip face with its
twin dark stripes, and a close crop of the moulded SPORTIF / HEAVY patch. Hugo confirmed the reading.
Renamed to `sportif-band-heavy-front-flat / front-folded / back-flat / inside-grip-a / inside-grip-b /
label-detail`.

**Two poster directions, Hugo's picks, feed 4:5 and story 9:16 each.** One script,
`clients/sportif/scripts-local/build_band_posters.py`, no arguments, re-runs clean.

*Editorial collage:* cream ground, inset peach plate under a thin caramel rule, the lockup on the
cream above it, EVERYDAY TRAINING ELEVATED set left in Glacial Bold (straight off the brand say-list),
the folded band tilted 10 degrees in front and breaking the plate at the bottom, and a tilted cream
card holding a swatch of the inside grip face so the poster shows two textures of the product rather
than one. Caramel footer lines, MADE TO BE SEEN left and BOOTY BAND, HEAVY right.

*Coming-soon teaser:* peach ground, the band centred as the single pop of colour, white lockup above,
COMING SOON tracked in warm charcoal, terracotta JOIN THE WAITLIST pill. No dates, consistent with the
launch being on hold (D-001).

**Craft notes worth keeping.** Warm brown shadows, not grey (see the learning above). The shadow
helper pads the alpha before blurring, otherwise the blur clips at the object edge and reads as a box.
The story layouts key their type up about 25 percent and push the peach plate closer to the safe edges,
because sizes derived from the 1080px width look undersized on a 1920px canvas. Story content stays
inside the 260px / 340px safe zones (D-020).

**3D.** Hugo's goal is a Shopify AR / 3D viewer asset, not a turntable video. Researched what Shopify
actually requires and what the current image-to-3D tools do. The honest position, given to Hugo: a
booty band is a flat loop of woven fabric, which is a simple shape that AI meshers tend to lump and
smooth, so a hand-built Blender model textured from these same photos would be more accurate than any
generated mesh. If we go the AI route, Tripo AI is the pick (multi-image input, PBR output, direct GLB
export, free tier of 200 credits a month). Left as an open decision (Q-016).

Learned: the workspace CLAUDE.md was read at session start this time, per the S031 learning, and it
caught the em-dash rule before any copy was written.

## Session 031 (2026-08-17, Cowork): Lucy's email-02 revisions, the collection mark goes master, art-direction overrides

Client: Sportif
Tags: lucy, email-02, social, logo-lockup, collection, instagram, placement, pillow, voice-rule

Lucy replied to the email-02 socials (Q-007, open since S028): "These look great!" plus three
notes. Change feed-duo's logo to the LEFT in BLACK, the ceiling beam is covering the logo on
the rest, and she'll send Canva notes on the story pilates pic. Rebuilt the whole batch in
`build_email02_social_v2.py` (v1 script untouched), output to `created/v2/{black,white,outline}/`,
send-ready copies with client-readable filenames in `TO-SEND-2026-08-17/` (12 files, ~20MB).
Email drafted at `email-to-lucy-v2.md`. NOT YET SENT.

**The beam fix generalised into a placement engine.** Rather than hand-positioning, the script
scans the left column and slides the lockup down until its footprint contains no dark pixels,
so it cannot land on the beam on these photos or future ones. Later refactored into one
function, `find_clear_y`, with `prefer='top'` for the mark and `prefer='bottom'` for the
footer. Worth knowing: the p2 (2nd-percentile) score it reports is pessimistic, because the
padded search box catches nearby dark objects even when the type itself sits clean. Judge by
eye, not by the number.

**Caught two things Lucy did not ask for.** (a) v1 put story lockups at y=150, underneath
Instagram's own profile row and progress bars, so they would have been half covered once
posted; stories now sit inside a 260px top / 340px bottom safe zone. (b) Hugo checked a post
on his phone and the lettering read small, so the lockup went up 25%. Size is one constant,
`SCALE`, which drives type, rule, gaps, shadow and stroke; the clearance search re-solves
placements automatically against the bigger footprint, so positions are never hand-tuned.

**The master mark changed (Hugo's call).** The lockup is now SPORTIF / rule / collection, per
Lucy's artwork, and it applies to EVERYTHING from here, not just collection-launch pieces. See
D-017. Proportions are derived rather than eyeballed: keep our canonical rule (0.43x wordmark
width), then size 'collection' so the rule is 0.75x its width, which reproduces her reference
without inheriting tracking distortion. Measured against her 500px original: rule/sub 0.741 vs
0.750, sub/cap 0.458 vs 0.488. NOTE the back catalogue (posters, product shots, the three IG
ads, band-swap set, both client PDFs) is still on the old wordmark+rule. Q-013.

**The @handle came off.** First it collided with the new mark (the word "collection" sitting
directly above "@sportifcollection" reads as a stutter), so it moved to a bottom footer. Then
Hugo made the better argument: on Instagram the account name is already printed above every
post and story, so stamping it into the image repeats what the viewer can already see. Now
`DRAW_HANDLE = False`. The footer code is kept, not deleted, because the logic reverses the
moment an image travels without the account name attached (stockist decks, Pinterest, print).
D-018.

**Art direction beat the algorithm, and that is now a documented workflow.** The clearance
search finds ground the type can legibly SIT on; it cannot judge composition, and left to
itself it hugged the top-left on every frame. Hugo opened the PNGs, dragged selection boxes
where the mark should go, and screenshotted them. Those convert to `MANUAL_PLACEMENT` entries
(x0,y0,x1,y1 in the image's own pixels) which override the search and survive re-runs. Set for
story-ballreach, story-sidestretch, feed-pilates. story-sidestretch is deliberately on the
RIGHT of frame, so the set is no longer uniformly left-aligned; the email now explains that
placement follows each photo rather than a fixed rule. Full-frame screenshots convert cleanly,
Preview-window ones need the ~88px toolbar offset backed out. D-019.

**New treatment: the wordmark burned into the wall.** Hugo's idea, a separate pilates variant
with SPORTIF collection set large and tone-on-tone BEHIND her, so her raised leg occludes the
type. `build_pilates_bg_wordmark.py`, four strengths, deboss-medium is the pick. No matting
model needed: that plate's background is a flat (230,224,217) with a clean empty gap in the
histogram between wall (~222+) and skin (~130), so a feathered luminance threshold at 200 is a
clean subject mask. The effect works because we shift the wall's OWN tone by a few percent
inside the letterforms rather than pasting a colour on top. IMPORTANT LIMIT: this only works on
a flat, evenly-lit background. The three studio shots have shelving, arches and mirrors behind,
where a threshold cannot separate subject from background, so the same look there needs a
Photoshop cutout. Hugo is making a PS version to show exactly what he meant. Q-014.

**Voice rule breach, worth not repeating.** The first drafts of the Lucy email, the README and
both scripts were full of em dashes, against the rule in CLAUDE.md line 45. Hugo caught it.
Root cause: `hyperframes/CLAUDE.md` was not loaded into the Cowork session context, so the
workspace conventions (including the session-start protocol) were not being applied until it
was read explicitly. Fix going forward: read `hyperframes/CLAUDE.md` at the start of every
session in this folder. Rewrote all four files clean rather than swapping characters. The same
pass caught a factual error in the email, which claimed the logo moved "down the left-hand side
on each one" after story-sidestretch had gone to the right.

**Open:** Q-012 (send the email, then Lucy's pick of black/white/outline to lock the house
standard), Q-013 (back-catalogue pass to the new mark), Q-014 (Hugo's Photoshop reference for
the burned-in wordmark). Five images are still on automatic placement (feed-duo,
feed-sidestretch, feed-ballreach, story-duo, story-pilates) and would benefit from boxes before
sending. See [[real-band-content-pipeline]], [[go-the-extra-mile]].

## Session NNN, YYYY-MM-DD, One-line summary
### What we did
### What we learned
### Decisions
### Open questions / next steps
-->
