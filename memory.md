# Workspace Memory

Running log of what we've done, what we've learned, decisions made, and questions still open. Each session adds a new entry at the top. Old entries stay so we can trace our thinking over time.

---

## CURRENT STATE (update this block every session, keep it to ~12 lines)

*Last updated: 2026-08-21 | Last session: 032 (Cowork, CLOSED) | Working tree: committed clean | Git: committed locally | **FIRST THING NEXT SESSION: Gemini / Nano Banana Pro is wired but not callable. GEMINI_API_KEY is in `.env`; open Settings, Capabilities, Network Egress, allow `generativelanguage.googleapis.com`, and note that a NEW chat is required after the change (Q-017).** | Then: Hugo runs the three gpt-image-2 poster prompts at full quality in ChatGPT and sends the plates back for the label swap and the type; build the colourway strips (ref 06) now that Q-015 is closed and the colours are measured; four frames to finish the band set (label close-ups, Q-018); SEND the email-02 v2 batch to Lucy (still not sent); back-catalogue pass to the SPORTIF/collection mark; high-quality band-swap renders + email-03; waitlist page; Canva Pro*

- **NEW (Session 032): first posters built from the REAL product, and the band cutouts renamed.** Lucy sent the physical bands and Hugo shot them on an iPhone with the backgrounds removed. All six cutouts are the **HEAVY** band (front flat, front folded, back, two inside-grip faces, label close-up), renamed from `IMG_96xx Background Removed.png` to `sportif-band-heavy-<face>.png` in `clients/sportif/assets/Sportif_Bands/`. Two poster directions built by `clients/sportif/scripts-local/build_band_posters.py`, each in IG feed 4:5 and story 9:16, output to `clients/sportif/generated/images/band-posters/` with a README: an **editorial collage** (cream ground, peach plate, EVERYDAY TRAINING ELEVATED in Glacial Bold, band tilted in front breaking the plate, tilted cream card holding an inside-grip swatch) and a **coming-soon teaser** (peach ground, band as the one pop of colour, terracotta waitlist pill, no dates). Both use the SPORTIF / rule / collection master mark (D-017) and carry no handle (D-018). See [[real-band-content-pipeline]].
- **NEW (Session 032, second half): AI poster prompts written against the real product.** Hugo wants to feed the real band shots into gpt-image-2 and Nano Banana Pro as references rather than generate a band from scratch. Settled with him: **text-free plates** (we still own the type, D-005 holds) and the band must be **our exact product**. Four prompts at `clients/sportif/band-poster-prompts.md` (plinth still life, morning-ritual flat lay, in-use under tension, graphic poster plate with an empty type well), each carrying a hard product-accuracy and no-text block. Six clean white reference plates at 2048px in `clients/sportif/products/band-reference-plates/`. Nano Banana Pro (Gemini 3 Pro Image) takes up to 14 references, so product plates and style references go in the same run; gpt-image-2 drifts past three or four. Hugo is running this round in the Gemini app himself.
- **Shoot 2 done and it needs doing again (S032).** Hugo shot all three bands in one sitting, 22 frames, every face, all three weights confirmed off their labels, now renamed to the D-021 convention and filed in `assets/Sportif_Bands/Originals/` as HEIC. The one rule he was given (all three in one sitting) was followed and worked. The surface rule was not: he shot on a **blue card**, and the colour did not survive. Heavy came back `#736A88`, hue 258 deg, 22% saturation, against the first shoot's known-good `#8F5B47`, hue 17 deg, 50%. White balancing against the cream label pulls hue back to 7 deg but saturation only to 28%, because the red-channel separation was never recorded. No neutral was in frame (the sheet under the family shot is blue card, not white paper). **Shoot 2 stays useful for shape, weave, labels and AI product references; it cannot be used where colour is the point.** Evidence image at `clients/sportif/products/shoot-2-colour-problem.jpg`, diagnosis written into the shot list (Q-015).
- **Learning (S032): the three colourways are confirmed off the real product.** HEAVY caramel/terracotta, MEDIUM blush rose, LIGHT sand/oatmeal. Matches what S023 recorded. The family shot `sportif-bands-family-a.heic` shows all three together.
- **Solved (S032): the lighting setup is settled.** Hugo re-shot the light band on a white cloth in DIRECT SUN and asked if it beat the shaded set. It does, decisively: same band goes from hue 226 / 19% sat (blue card, shade) to hue 34 / 33% once corrected (white cloth, sun). The real culprit was never just the blue card, it was **open outdoor shade, which is lit by blue sky**, stacking two blue sources. Direct sun overwhelms the sky. And because the white surface is a genuine neutral sitting in every frame, the correction now verifies: the moulded label lands at hue 39 / 36% against a known-good 35 / 34%. Two refinements for the real shoot: a white bounce card just outside frame on the shadow side (direct sun leaves a hard, blue-filled shadow), and expose for the BAND not the sheet (the test frame is about a third of a stop dark). Shooting on white also retires the separate white-paper reference step. See D-026 and `clients/sportif/products/shoot-3-sun-vs-shade.jpg`.
- **DONE (S032): shoot 4 passed and Q-015 is closed.** Twelve frames on a white sheet in direct sun, filed in `assets/Sportif_Bands/Original_New_method/` and renamed to the D-021 convention. Corrected against the white sheet, the heavy band lands **hue 17 deg / 53% sat against a known-good 17 / 50%**: hue exact, saturation within three points. **Measured colourways, now the source of truth (D-027): LIGHT #B8A080, MEDIUM #9D7459, HEAVY #6C4333.** The real product runs DEEPER than brand.md's palette (heavy sits well below terracotta #833827), so strips and range cards key off the measured values. Swatch card at `clients/sportif/products/band-colourways.jpg`. Set covers front-folded, back-flat and both grip faces for medium and heavy, front-folded and back-flat for light, plus two family shots. Only gap is the LIGHT band's two grip shots (Q-018), which blocks nothing. **Colourway strips (ref 06), the range card and the wholesale line sheet are all unblocked.**
- **DONE (S032): shoot 5 completes the set, and Hugo invented the texture asset.** Eleven more frames the same afternoon: light grip A and B, front-flat for all three, two TIGHT PARALLEL TRIOS (the real source for the colourway strips, better than the spaced family shot), an angled trio, and **three texture close-ups, one per band, which he shot on his own initiative**. All three bands now carry all five faces. Only dedicated label close-ups remain unshot and they block nothing. Two re-exported duplicates moved to `_duplicates/`.
- **Hugo's idea, now a brand asset (D-028): the band's own weave as a background texture.** Built into `clients/sportif/assets/textures/` as a seamless 1024px tile per colourway (4-way mirrored) plus a large single-crop plate (~1700x3200, no repetition) so full-bleed backgrounds need no tiling at all. Demo at `generated/images/band-posters/demo-texture-background.jpg`: heavy weave full bleed with the cream SPORTIF/collection lockup over it, and it reads genuinely expensive. **The texture frames also turned out to be the most accurate colour samples in the project**, because the band fills the frame with nothing else in it (light 32/33%, medium 20/44%, heavy 16/52%, matching the family-shot values).
- **NEW (S032): gpt-image-2 poster plates generated and tested from Cowork.** OPENAI_API_KEY staged from `.env` via device_stage_files (never printed), `api.openai.com` reachable, `gpt-image-2` visible. Five low runs at 1088x1360, about 20s each. **All three first-pass prompts failed the same way and it was always the band**: a smooth suede strap around ONE thigh, or slung across a hip. Composition, wall, mood and cuttability were all fine. **Fixed by describing the object physically and by negation (D-029)** plus dressing her in CREAM so the band is the only dark accent. p1b and p3b are keepers; p3b (blur) is the best thing generated so far. **The moulded label still comes back blank and cannot be prompted away**, so the S029 two-image swap or a PIL patch stays mandatory. Also proved the **S031 burn-in end to end**: SPORTIF burned into the wall behind the blurred figure, she occludes the middle of it, at `generated/images/band-posters/gpt-plates/p3b-typed-burnin.png`. Plates and the updated prompt doc committed.
- **Hugo's format preference, now a rule (D-031).** The first version of the poster prompt doc wove the test findings through the prompts and he could not follow it. Rewritten to: heading, one self-contained paste block, upload files as bullets, three times, with all analysis reduced to four bullets at the end. His words: "this is much easier to follow". Applies to every prompt, instruction, checklist and setup doc from here. Also filed to his cross-surface preferences.
- **HEAD TO HEAD: Gemini beats gpt-image-2, and it is now the default (D-032).** Hugo ran all three prompts through both, Gemini on the PRO setting. Plates filed in `generated/images/band-posters/plates-in/`. Gemini held the band colour far closer to the real product, rendered the knit as fabric rather than a smooth strap, returned flatter cleaner backgrounds, and actually followed the placement instruction. gpt-image-2 washed the band out and put her dead centre. **On references: 4 beat 2 on COMPOSITION (correct lower-right placement with a type well) but 2 beat 4 on the LABEL (faint lettering vs blank). More references helped placement, not the label.** The label is blank on essentially every plate from both engines, so the swap stays mandatory.
- **Two finished posters exist now.** `p1-fullfigure-gemini-4refs-TYPED-keep.png` (EVERYDAY / TRAINING / ELEVATED in terracotta running behind her, cut with a border-connected flood fill since the wall is flat) and **`p3-blur-gemini-TYPED.png`, the strongest thing produced all session**: the SPORTIF / rule / collection lockup burned into the wall behind a blurred figure, no cutout needed, using the S031 luminance trick. Caveat on the first: the automatic matte swallowed her drop shadow, which Photoshop fixes in seconds.
- **Open (Q-019): poster 2 needs a re-run.** BOTH engines put the band running diagonally ALONG the leg instead of horizontally across both thighs. The stacked-knees wording is not enough; it needs 'horizontally across both thighs, perpendicular to the legs'.
- **Tested Hugo's hunch about the label, and it was the wrong variable (D-033).** He asked whether adding a tight label close-up to the references would make the label render cleanly. Ran a controlled pair on gpt-image-2, identical prompt, one with a label close-up and one without. **Both rendered SPORTIF and HEAVY legibly, and the one WITHOUT the reference was marginally better.** What actually changed was the crop: the test prompt asked for a tight thigh-height shot where the label fills roughly 300px, against about 60px in a full-figure poster. So label legibility is a function of scale in frame, not of reference quality. Practical upshot: wide shots always need the swap; if a poster needs the label to read, crop tighter. He should still shoot the label close-ups, but for the SWAP, which needs a clean high-res crop and shoot 5 never produced one (Q-020).
- **Learning (S032): HEIC needs no conversion.** Hugo had been converting to JPEG for us. `pip install pillow-heif --break-system-packages` (a few seconds, once per sandbox) makes HEIC read directly, and the original keeps its EXIF and full capture data that a JPEG conversion discards.
- **Correction (S032): AE/AF Lock on iPhone does NOT lock white balance.** It locks focus and exposure only; a white balance lock exists in video mode, not in the stills camera. The advice given earlier in the session was wrong on that point. It does not change the outcome, because the white surface is the reference and the correction happens per frame in the edit. Full iPhone 14 Pro Max setup written up at `clients/sportif/products/iphone-camera-setup.md`: Photographic Styles must be **Standard** (a Warm or Cool style bakes a second invisible colour shift into every frame), Grid ON for the straight-down crosshair level (align to yellow, which keeps 19 overhead frames consistent), Prioritise Faster Shooting OFF, 1x lens, expose off the BAND not the sheet. ProRAW is documented as the optional bulletproof route (no baked white balance at all, ~25MB per frame at 12MP, `.DNG`); `rawpy` reads it in the sandbox, verified.
- **NEW (S032): Hugo is doing the cutouts in Photoshop.** He asked to, as practice, and it is the better route for a hard matte anyway (D-012). So there are now two house routes for depth posters, sharing one type spec: `clients/sportif/depth-poster-photoshop-guide.md` (font install, canvas sizes, Photoshop tracking conversions, the layer order for the depth flip, the warm-brown shadow recipe matching D-022, and the Shift Edge note that kills the halo). Photoshop for hero pieces and hard mattes, the script for anything needing six sizes (D-024).
- **Learning (S032): the background removal strips EXIF.** The cutouts carry no camera data, so originals must be kept alongside them in `assets/Sportif_Bands/originals/`.
- **Learning (S032): drop shadows on the warm palette must be tinted warm brown, not grey.** A neutral shadow reads muddy and grey against blush peach. `shadow()` in the poster script uses (122, 78, 56) and pads the alpha before blurring so the blur is not clipped at the object's own edge.
- **Learning (S032): a rotated cutout's bounding box is much wider than the object.** A 1080px tall band rotated 14 degrees returns a box roughly 536px wide when the band itself is 283px, so placing by box edge ate two letters of the headline. Place tall thin cutouts by the size you want them to occupy, then cap the position against the neighbouring element, rather than trusting the expanded box.
- **Decision path for 3D (S032):** Hugo wants the band as a **Shopify AR / 3D viewer** asset. Shopify wants GLB, about 4MB total, textures as optimised JPG at or under 2048x2048, diffuse + normal + a combined occlusion/roughness/metalness map, real-world scale, origin centred at the product's base. Recommendation is Tripo AI (multi-image to 3D, PBR output, direct GLB export) with the honest caveat that a booty band is a simple loop of fabric and a hand-built Blender model textured from these photos would beat any AI mesh on accuracy (Q-016).
- **NEW (Session 031): Lucy approved the email-02 socials with revisions; the collection mark went MASTER; art-direction overrides added.** Lucy: "These look great!" + move feed-duo's logo LEFT and BLACK, the beam is covering the logo on the rest, Canva notes coming on the story pilates pic. Rebuilt via `clients/sportif/scripts-local/build_email02_social_v2.py` into `created/v2/{black,white,outline}/`, staged in `TO-SEND-2026-08-17/` (12 files, ~20MB), draft at `email-to-lucy-v2.md`, **NOT YET SENT**. Three things changed beyond her ask: the mark is now **SPORTIF / rule / collection** everywhere (D-017), the **@handle came off** on-platform assets (D-018, Instagram already prints the account name), and placement is now **photo-led** via a clearance search plus Hugo's marked boxes (D-019). Also fixed an IG story safe-zone bug from v1 (D-020) and sized the lockup up 25% after Hugo phone-tested it. See [[real-band-content-pipeline]].
- **Learning (S031): the workspace CLAUDE.md is NOT auto-loaded in Cowork.** The em-dash voice rule (line 45) and the session-start protocol were both missed until the file was read explicitly, and a client-facing email went to draft full of em dashes. Read `hyperframes/CLAUDE.md` at the start of every session in this folder.
- **Learning (S031): placement can be solved, not hand-tuned.** `find_clear_y` slides type until its footprint sits on calm, light ground (`prefer='top'` for a mark, `prefer='bottom'` for a footer), so resizing anything re-solves positions automatically. But it cannot judge composition: left to itself it hugged the top-left on every frame. `MANUAL_PLACEMENT` boxes (x0,y0,x1,y1, marked by Hugo on the actual PNG) override it and survive re-runs. The reported p2 score is pessimistic; judge by eye.
- **Learning (S031): type can be burned INTO a flat background without a matting model.** Shift the background's own tone a few percent inside the letterforms, masked by a feathered luminance threshold, and the subject occludes the type. Only works on flat, evenly-lit plates (the pilates shot); busy studio backgrounds need a Photoshop cutout.

- **NEW (Session 030): SPORTIF collection grid tiles built and SENT to Lucy.** Lucy asked for the 3-tile Instagram grid banner again, this time with "collection" under the wordmark, and supplied a square reference lockup (peach `#F0CDB3` bg, white SPORTIF, rule, lowercase "collection") saved at `clients/sportif/Sportif_Collection/`. Built `clients/sportif/scripts-local/build_collection_grid.py` (adapted from `build_grid_banner.py`): 3240x1440 peach master, white Glacial Indifference SPORTIF tracked to 80% of canvas width, rule, then "collection", split into three 1080x1440 tiles named by POST ORDER. Output + POST-ORDER.md in `clients/sportif/Sportif_Collection/grid/`. Email drafted and SENT with attachments (`clients/sportif/email-to-lucy-collection-grid.md`). Colourway confirmed with Hugo as peach/white only (cream and white offered to Lucy as options). See [[real-band-content-pipeline]].
- **Learning (S030): sub-lines in a multi-tile banner must be sized off the CENTRE TILE, not off the reference's cap-height ratio.** Matching the reference proportion (sub ascender = 0.48x SPORTIF cap height) made "collection" 1030px wide inside a 1080px tile, so it ran into the IG gutters. Fix: size the sub as a share of tile width (0.55) and the rule as 0.75x the sub width, which preserves the reference hierarchy and keeps clear space. Also confirmed by brute-force search that NO tracking/size combination avoids a tile seam cutting a letter of SPORTIF (7 letters across 3 tiles), so the clipped T crossbar is inherent to the format, not a bug.

- **NEW (Session 029): Email 03 (Lucy's "3 bands like this" request) + the band-swap labelling method.** Lucy shared 6 competitor STYLE refs (YR / Pilates Reformers Australia / moveactive), rendered from a PDF via PyMuPDF (poppler is not on the Mac). Folder `clients/sportif/email-03-band-photo/` (downloads/created/README/email-to-lucy). Built (all ownable, no competitor imagery): a 3-band product HERO from our cutouts (`band_hero_ref1.py`; also fixed the cutouts' leftover peach FLOOR strip via `trim_base` in `band_cutouts.py`); a range-concept FLATLAY with imaginary socks/pouch/towel (`gen_flatlay_concept.py`); a DRAPED-arm shot (`gen_draped_arm.py`); reused our in-use library. **Copyright call:** competitor reference photos are STYLE-ONLY, never edited into Sportif assets (their copyright + model release); real-model content needs a real shoot, or AI models we own (Lucy agreed, told via email). **Label breakthrough:** gpt garbles small brand text at low quality, so (a) reaffirmed the house rule (we own the type: PIL-composited labels `label_flatlay_pil.py`/`label_draped_pil.py`) and (b) found the WINNING method = a TWO-IMAGE gpt swap (`band_swap_test.py`, pass the scene + our finished hero bands) that drops our real caramel SPORTIF label in naturally, plus stitched SPORTIF on the soft goods (`add_stitched_branding.py`). Best deliverables in `created/band-swap-test/` (flatlay-branded-fixed, draped swapped); small garbles cleared by a high Terminal render or a PIL patch (`fix_towel_label.py`, `fix_light_word.py`). See [[go-the-extra-mile]], [[real-band-content-pipeline]].

- **NEW (Session 028): Lucy's Canva-request workflow (emails 01 + 02), poster experiments, new matting/inpaint tooling.** **Email 01 finished:** pilates reskin ad, band shown as PRODUCT PLACEMENT (not worn) + logo, ankle straps off, original raised-leg pose kept (`reskin-clean.png` via `reskin_clean_plate.py` + `layout_reskin_clean.py`). **Email 02 (light-touch social batch):** 4 feed 4:5 + 4 stories 9:16 from her 4 cleaned photos, real logo lockup (SPORTIF Glacial Regular tracking -0.059 + underline rule) top-right with @sportifcollection CENTRED below, soft corner scrim (`build_email02_social.py`; self-contained folder `clients/sportif/email-02-social/` = downloads/ + created/ + README + email-to-lucy.md). **Lucy's 4 photos cleaned** to `reference-images/lucy-canva-picks/` (removed the PILATES watermark + "First class is free!" text via cv2 inpaint, cropped the Canva sky/hills bg, removed the black ankle weights via a gpt patch-composite that keeps the rest native-res). **Poster experiments** (borrowing the JANNAYON collage layout, warm palette not periwinkle): `poster-lucy-real` (flat grid), `poster-lucy-depth` (cut-out pilates hero pops forward over the headline, cv2 painted out a second person's stray arms), `poster-lucy-layered` (SPORTIF wordmark sandwiched between a faded legs-in-air background and the ball hero in front). **New Mac tooling installed:** rembg (isnet-general-use) + onnxruntime + opencv (cv2) + scipy + numpy = background matting, cv2.inpaint text/object removal, distance-transform defringe. See [[go-the-extra-mile]], [[real-band-content-pipeline]].
- **Learnings (S028):** (a) The **Canva MCP here only exposes search-designs + generate + export**; the read/edit tools (get-design, pages, editing transactions) are NOT provisioned, and export-design returns "Not allowed to access" on Lucy's view-only shared designs, so the workflow is Hugo downloads from Canva manually -> I process locally -> he re-uploads. (b) **White-on-light mattes fail** (the white ball + white bra on a light wall smeared in rembg) -> cut those in Photoshop; plain-bg subjects (the pilates figure on flat beige) matte flawlessly. (c) **gpt-image-2 poster: my prompt vs Hugo's ChatGPT run were equal on craft; the differentiator was quality tier** (his full-quality ChatGPT beat my harness-capped low) -> for hero deliverables Hugo runs the final gen in ChatGPT, I do iteration + the exact-type production version (cv2.inpaint lifts baked type, we lay real Glacial). (d) **The real logo is a lockup** (wordmark + underline rule), never the bare/wide-spaced wordmark.

- **NEW (Session 027): Lucy expert-brand content strategy (Phase 1).** Applying the Devin Jatho expert-brand / 4-quadrant model to Lucy (authority-first, founder-led). Analysed her 3 editorials; her edge is the STYLE + STRENGTH fusion for REAL women. Deliverable: `clients/sportif/lucy-profile-for-review.pdf` ("Content Creation Strategy", a warm Ocho Productions letter) + internal `lucy-content-library.md` (taglines/quotes/mantras). Built via `build-lucy-profile.py` (headless Chrome). Sportif name is LOCKED (Le Sport Collectif was old). Next = Lucy reacts, then Phase 2 quadrants [[real-band-content-pipeline]].

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

## Weekly Review — 2026-08-17 (week of 2026-08-10)

One session this week (030, 2026-08-11, Cowork) — and, worth saying plainly, one session in the last twenty days: the log jumps from 2026-07-28 (Sessions 028/029) straight to 2026-08-11. The single session that did run was a clean, self-contained client deliverable that went out the door the same day, which is the right shape for a low-volume week, but the backlog underneath it has not moved.

### Highlights
- **The SPORTIF "collection" grid banner was built AND sent to Lucy in one session.** Lucy supplied a square reference lockup (peach `#F0CDB3`, white SPORTIF, rule, lowercase "collection"); `build_collection_grid.py` turned it into a 3240x1440 master split into three 1080x1440 tiles named by posting order, with `POST-ORDER.md` alongside. Build → email → sent, same day, no round trip lost.
- **A real typographic problem was diagnosed rather than fudged.** Reproducing the reference's cap-height ratio blew "collection" out to 1030px inside a 1080px tile. The fix — size the sub-line off the CENTRE TILE (0.55 of tile width) and the rule off the sub (0.75x) — preserves the reference hierarchy while restoring ~245px of clear space either side. That's a reusable rule for any future multi-tile lockup.
- **The clipped-letter question was settled by brute force, not opinion.** Tracking 0.24–0.34 × sizes 440–560 were searched exhaustively: with 7 letters across 3 tiles, no combination avoids a seam landing inside a glyph. The clipped T crossbar is inherent to the format, not a bug — and is now something to state proactively in client emails rather than defend after the fact.
- **Ambiguity was resolved before building, not after.** "Collective" vs "collection" was checked against the artwork and confirmed with Hugo up front, as were tile shape and colourway (peach/white only, with cream and white offered to Lucy as options in the email rather than pre-built). Cheap clarification beat expensive rework.

### Patterns I noticed
- **The per-request folder convention is now fully habitual.** Sessions 028, 029 and 030 all produced a self-contained request folder (downloads + created + README + email-to-lucy). It has survived three sessions across two different environments without anyone re-deciding it.
- **"We own the type" continues to hold as the house rule.** Session 030's deliverable is 100% PIL-composited Glacial Indifference on a flat peach master — no AI in the loop at all. When the brief is pure typography, the house rule collapses to "just build it ourselves," and that's the fastest path.
- **Reference artwork is a proportion trap.** Twice now (S028's logo lockup, S030's sub-line) matching a reference's literal ratios produced a wrong result, because the reference was authored at a different canvas scale. The durable lesson: derive proportions from the OUTPUT frame, not the reference's absolute ratios.
- **Cadence dropped hard and the carried backlog didn't.** From eight sessions in the week of 07-20 to one in nearly three weeks. Everything the last review flagged as "needs neither Lucy nor trademark" is untouched — which means the constraint this month is throughput, not blockers.

### Skills / knowledge gained
- **Multi-tile lockup sizing rule:** size sub-lines and rules as a share of the CENTRE TILE width, never off the primary wordmark's cap height — wide tracking on the primary word inherits into anything scaled from it.
- **Seam math for grid banners:** with N letters spanning 3 tiles, seam-vs-glyph collision is combinatorially unavoidable for odd letter counts like 7; verified by exhaustive search across tracking and size, so stop looking for a setting that fixes it.
- **Practical checks worth repeating:** sample the reference background rather than eyeballing the hex (it came out as (241,205,179), effectively the brand blush); verify lockup balance with an ink-bounds scan (307 top / 340 bottom = a deliberate optical lift).
- **Client-comms habit:** name known format artefacts (the clipped crossbar) in the email that ships the asset, rather than waiting to be asked.

### Open questions still unresolved
**Resolved (by a later session):**
- [x] ~~Q-009: email 03 pending Lucy's screenshot (Session 028)~~ RESOLVED Session 029 — the request arrived as a 6-reference PDF and was built out in full (`clients/sportif/email-03-band-photo/`).
- Note: Session 030 has no `[ ]` items of its own to reconcile — its single open thread (Lucy's reply) is still outstanding, so nothing there could be marked resolved.

**Still open:**
- [ ] **Lucy's reply on the collection grid**, including whether she wants a cream or white colourway alongside the peach (Session 030).
- [ ] **Q-010: run the high-quality band-swap / branded renders in Terminal**, then finalise the email-03 attachment set and send to Lucy (Session 029). Third week carried; the ~60s harness cap is the reason, a native Mac terminal is the fix.
- [ ] **Lucy's other replies:** email-02 socials (Q-007) and the expert-brand "Content Creation Strategy" PDF (Q-006, which gates Phase 2 — her expert niche, one avatar, four quadrants).
- [ ] **Q-008: Hugo's Photoshop cutout of the ball hero**, which blocks `poster_lucy_layered.py` (white-on-light mattes fail in rembg).
- [ ] **Standalone waitlist capture page + 3-email welcome flow** — needs neither Lucy nor trademark, now named the top unbuilt item in six separate sessions.
- [ ] **Canva Pro** (was expected ~2026-07-30, still not logged as done): Sportif brand kit + share the Sportif folder with Lucy.
- [ ] **Lucy's picks still pending:** music-bed pacing (calm ~100 BPM vs upbeat ~118 BPM) and the incentive decision A/B/C.
- [ ] **Film the unboxing** — bands in hand since Session 021, footage still not shot.
- [ ] **Ambassador/instructor seeding shortlist** — ninth week carried, designated the main growth engine, requires nothing from anyone.
- [ ] **Trademark clearance** — the critical-path gate, on Lucy's lawyer's clock.
- [ ] Carried: ElevenLabs TTS awaiting Hugo's API key, `cosmos_yoga-duo.mp4` Seedance path, Shopify store (trademark-gated), materials question, Stage 3 synthesis template, PDF generators still on Poppins.

### Suggested focus for next week
1. **Send Lucy ONE consolidated message that clears the entire feedback queue** — collection-grid colourway, email-02 socials, the Content Creation Strategy PDF, music-bed pacing, and the incentive A/B/C. Five separate threads have been waiting on her in parallel; one message is far more likely to get answered than five, and it un-gates Phase 2 of the expert-brand strategy.
2. **Do one native-Mac-terminal render session and close Q-010.** The high-quality band-swap/branded renders are the only thing standing between the email-03 work (already built) and it actually reaching Lucy. It is a single uninterrupted hour, not a project.
3. **Build the standalone waitlist capture page.** Six sessions have now called it the top unbuilt item; it depends on neither Lucy nor the trademark, and every asset built since July — grids, reels, posters, product shots — dead-ends without it. If throughput is the constraint this month, spend it here.

---

## Weekly Review — 2026-07-26 (week of 2026-07-20)

Eight sessions this week (020–027), the busiest week the workspace has ever had — up from one last week. The logjam broke on day one: Session 021 finally captured the Tuesday 2026-07-14 Lucy meeting outcomes (last week's #1 focus), which reframed the whole strategy around the trademark hold. The rest of the week banked an enormous amount of trademark-independent production: a full real-band product content pipeline, a fresh generation pipeline, a Canva collaboration workflow, memory system v2, and the opening move of a Lucy expert-brand content strategy.

### Highlights
- **The Tuesday Lucy meeting outcomes were finally logged (Session 021), and they changed the map.** Launch is held indefinitely pending trademark talks with Lucy's lawyer — trademark, not Shopify, is now the critical-path gate. The 500 band units HAVE landed (unboxing now filmable). The correct posture is explicit: bank everything that doesn't depend on trademark.
- **A complete real-band product content pipeline shipped (Sessions 023–024).** From 3 casual snapshots of the real bands: restaged flatlay, 3 hero cards, a range reel, two lifestyle+product blends, a "they've landed" teaser, a band-in-use pilates reel with the real SPORTIF label stamped in, plus the reusable **reference-reskin technique** (AI generates a no-text plate, we own the type in PIL) with two waitlist-poster finals. The bands' colourways ARE the peach palette — the whole direction validated by physical product.
- **Fresh from-scratch generation + Canva workflow established (Session 025).** `gen_fresh_explore.py` makes Sportif key visuals from scratch with three durable prompt lessons (name the garments, contrast skin tone, smooth not ribbed), and the two-avenue model (our pipeline = studio, Canva = shareable workbench) is set up with a Sportif folder chain to Lucy — Pro-gated pieces (brand kit, folder share) land when Hugo gets Canva Pro ~2026-07-30.
- **Two infrastructure/strategy moves: memory system v2 (Session 026) and the Lucy expert-brand strategy Phase 1 (Session 027).** v2 adds registries (`DECISIONS.md`, `OPEN-QUESTIONS.md`), per-client filtering, and a close-out `check` hook — directly mitigating the compliance failure that lost the Tuesday meeting notes for a week. Phase 1 applied the Devin Jatho 4-quadrant model to Lucy and produced the "Content Creation Strategy" PDF, ready to send.

### Patterns I noticed
- **The ~60s render/network cap shaped nearly every session again.** High-quality gpt-image-2 renders hit it in Sessions 023, 024, and 025 (even in the VS Code terminal); the standing answer is iterate low in-harness, finals from a native Mac terminal. This is now a permanent column in the workflow map, not a transient annoyance.
- **"AI makes the plate, we own the type" hardened from a technique into the house style.** Overlay scripts, the reference reskin, the label stamp, the PIL type layer — every finished piece this week separated AI-generated imagery from brand-controlled typography. Hugo enforced it explicitly ("NO YOU LAYOUT TEXT, THATS OUR WORKFLOW").
- **Hugo's eyeball QA keeps catching what tooling can't** — the card-crop neighbour bleed (023), the GSAP selector bug hiding the end-card wordmark (022), navy type fighting the warm palette (025), the too-clinical first PDF draft (027). Fourth straight week this pattern holds.
- **The Lucy dependency changed shape: from hard blocker to feedback latency.** Nothing is structurally blocked on her anymore (trademark is on her lawyer), but a queue of small picks is accumulating: music-bed pacing, the Content Creation Strategy reaction, the incentive A/B/C decision. Meanwhile the waitlist capture page — which needs neither Lucy nor trademark — was named "still the top unbuilt item" in four separate sessions and is still unbuilt.

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
- [ ] **Send Lucy the Content Creation Strategy PDF**, then Phase 2 of the expert-brand strategy: lock her expert niche, one avatar, and the four quadrants (Q-006, Session 027 — gated on her reaction).
- [ ] **Standalone waitlist capture page** — named the top unbuilt item in Sessions 023, 024, and 025; needs neither Lucy nor trademark. Pair with the 3-email welcome flow.
- [ ] **Canva Pro (~2026-07-30):** set up the Sportif brand kit + share the Sportif folder with Lucy (lucy@lucywayne.com.au) once Hugo upgrades (Session 025).
- [ ] **Lucy's picks pending:** music-bed pacing (calm ~100 BPM vs upbeat ~118 BPM, Sessions 022–023) and the incentive decision A/B/C (Session 021).
- [ ] **High-res finals past the ~60s cap** — print-quality product/in-use renders need a native Mac terminal run (Sessions 023–025).
- [ ] **ElevenLabs TTS awaiting Hugo's API key** (`.env` slot + script ready, Session 022).
- [ ] **Film the unboxing** — bands are in hand since Session 021 confirmed landing; footage not yet shot.
- [ ] **Trademark clearance** — the critical-path gate, on Lucy's lawyer's clock, nothing accelerates it (Session 021).
- [ ] `cosmos_yoga-duo.mp4` peach video edit would need the Seedance path (Session 020).
- [ ] Carried from prior weeks, still open: ambassador/instructor seeding shortlist (sixth week carried, needs nothing from anyone), Shopify store (gated on trademark), materials question, Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins.

### Suggested focus for next week
1. **Send Lucy the Content Creation Strategy PDF and bundle her pending picks into the same ask** (PDF reaction + music-bed pacing + incentive A/B/C). One message clears the whole feedback queue and un-gates Phase 2 of the expert-brand strategy.
2. **Build the standalone waitlist capture page + 3-email welcome flow.** Four sessions in a row called it the top unbuilt item; it needs neither Lucy nor the trademark, and every piece of content built this week dead-ends without it.
3. **When Canva Pro lands (~07-30), set up the brand kit and share the Sportif folder with Lucy** — and use the waiting days to finally start the ambassador/instructor seeding shortlist (six weeks carried) and film the unboxing.

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

---

## Session 030 (2026-08-11, Cowork): SPORTIF collection grid tiles (Lucy's reference lockup across 3 IG tiles)

Client: Sportif
Tags: lucy, instagram, grid-banner, collection, wordmark, glacial-indifference, pillow

Lucy asked for the Instagram grid banner again, this time with "collection" underneath the wordmark, and gave a square reference lockup (peach background, white SPORTIF, short rule, lowercase "collection") which Hugo saved to `clients/sportif/Sportif_Collection/Sportif_Collection_wordmark.jpg`. Note the word is **collection**, not "collective" (Hugo typed collective, the artwork says collection, confirmed with him before building). "Le Sport Collectif" remains the retired old name.

**Confirmed with Hugo before building:** wording = collection; tile shape = 3:4 portrait 1080x1440 (same as the first grid); colourway = peach `#F0CDB3` with white type only, matching the reference. Cream and white variants were offered to Lucy in the email rather than built up front.

**Built:** `clients/sportif/scripts-local/build_collection_grid.py`, adapted from `build_grid_banner.py`. One 3240x1440 peach master, SPORTIF in Glacial Indifference Regular tracked at 0.28em to 80% of canvas width, a rule, then "collection" at 0.06em tracking, split into three 1080x1440 tiles whose file numbers ARE the posting order (rightmost posts first). Deliverables + `POST-ORDER.md` in `clients/sportif/Sportif_Collection/grid/`. Sampled the reference background as (241,205,179), effectively the brand blush, so used `#F0CDB3`.

**The one real design problem, and the fix.** Reproducing the reference proportions literally (sub ascender = 0.48x the SPORTIF cap height, taken off the 500px reference: cap 41, sub ascender 20, rule 90 wide vs sub 120 wide) blew "collection" out to 1030px inside a 1080px tile, hard against both gutters. The cause is that SPORTIF is tracked enormously wide to span three tiles, so anything sized off ITS cap height inherits that stretch. Fix: size the sub as a share of the CENTRE TILE (0.55 of tile width) and the rule as 0.75x the sub width (the reference's own rule-to-sub ratio). Result reads like the reference and keeps roughly 245px of clear space either side. Lockup vertical balance checked by ink-bounds scan: top margin 307, bottom 340, i.e. a slight optical lift.

**Also settled:** brute-forced tracking 0.24 to 0.34 and sizes 440 to 560 and found NO combination where a tile seam misses every letter. A 7-letter word across 3 tiles always has a seam land inside a glyph, so the clipped T crossbar is inherent to the format (the first grid had it too and Lucy accepted it). Worth saying out loud in future client emails rather than being asked about it.

**Sent:** email drafted at `clients/sportif/email-to-lucy-collection-grid.md` and Hugo sent it with the attachments the same session.

## Session 029 (2026-07-28, Claude Code): Email 03 (Lucy's 3-band photo request) + the band-swap labelling method

Client: Sportif
Tags: lucy, email-03, bands, product-photo, band-swap, labels, copyright, gpt-image-2

Lucy's email 03: "create a picture of my 3 bands like this" with 6 competitor STYLE references (YR, Pilates Reformers Australia, moveactive), shared as a PDF. Rendered the PDF to images with PyMuPDF (installed; poppler/pdftoppm is not on the Mac). Folder `clients/sportif/email-03-band-photo/` (downloads/ + created/ + README + email-to-lucy.md), per the per-request convention. Clarified with Hugo: recreate each reference LOOK with OUR bands and assets, not edits of the competitor photos.

**Built (all ownable, no competitor imagery):**
- 3-band product HERO (`band_hero_ref1.py`): our 3 transparent band cutouts fanned/stacked on warm cream, SPORTIF labels visible. Fixed the cutouts at source too: `trim_base` in `band_cutouts.py` removes the leftover peach FLOOR strip rembg kept at the band bottoms (texture-based).
- Range-concept FLATLAY (`gen_flatlay_concept.py`, from scratch): the 3 bands + IMAGINARY Sportif pieces (ribbed grip socks, cotton pouch, rolled towel). pg-6 could not be copied faithfully (competitor full-range flat-lay with props that are not Sportif products).
- DRAPED-arm shot (`gen_draped_arm.py`, from scratch): photoreal model, bands draped over the forearm.
- In-use shots reused from our existing band-inuse library.

**Copyright (important):** the reference photos are competitor brands' OWN photos; we must not edit them (swap band, reuse model) into Sportif marketing (their copyright + the model's release is for their brand). Lucy also does not want AI models. Resolution (Hugo): use AI models we generate (fully owned) for now and TELL Lucy via email; the premium option is a real shoot (Lucy or a model with the actual bands), which we then style. Reference photos stay STYLE-ONLY.

**Label breakthrough (the reusable bit):** gpt-image-2 garbles small brand text at low quality (SPOTE, MEAVY, a garbled towel label). Two lessons:
- Reaffirmed the HOUSE RULE (AI makes the plate, WE own the type): PIL-composited clean SPORTIF labels (`label_flatlay_pil.py`, `label_draped_pil.py`) = guaranteed spelling, but a flat/pasted look.
- WINNING method (Hugo's idea): a TWO-IMAGE gpt swap (`band_swap_test.py`) = pass the scene + our finished hero bands, and gpt drops our real caramel SPORTIF label onto the scene bands NATURALLY (beats the PIL composite). Plus `add_stitched_branding.py` adds tonal stitched SPORTIF to the soft goods (pouch/socks/towel) so the whole flat-lay reads as one branded set. Remaining small-text garbles are cleared by a HIGH Terminal render or a quick PIL patch (`fix_towel_label.py` fixed the garbled towel label; `fix_light_word.py` fixed one band size word).

**Deliverables:** primary set in `created/` (hero, labelled draped, labelled flat-lay, 3 in-use); the stronger swap experiments in `created/band-swap-test/` (flatlay-branded-fixed, draped swapped). Email to Lucy drafted (`email-to-lucy.md`): what we did, the copyright heads-up, and the real-shoot option.

**Open:** Q-010 = run the high-quality swap/branded renders in Terminal for crisp text, then finalise the attach set and send Lucy. See [[real-band-content-pipeline]], [[go-the-extra-mile]].

---

## Session 028 (2026-07-28, Claude Code): Lucy's Canva requests (emails 01 + 02) + poster experiments + matting/inpaint tooling

Client: Sportif
Tags: lucy, canva, social, posters, cutouts, rembg, cv2, logo-lockup

Multi-day session working Lucy's Canva design requests, one self-contained folder per request.

**Email 01 (finished the pilates reskin ad):** Lucy asked to add the band + logo and remove the ankle straps on the hip-raise model. Clarified with Hugo: band shown as a PRODUCT PLACEMENT (not worn) + the SPORTIF logo, original raised-leg pose kept (not the glute-bridge variant). `reskin_clean_plate.py` retouches the worn band off the plate; `layout_reskin_clean.py` lays the type + band card. Final `reskin-clean.png`.

**Lucy's 4 photos cleaned** into `reference-images/lucy-canva-picks/` (NON-AI where possible): downloaded the "Use these Pictures only for Social Media" Canva pages, cropped the sky/hills Canva bg off the reformer-duo, cleaned the pilates ref (removed the PILATES watermark by flattening the background beige + the "First class is free!" navy text via cv2.inpaint). Black ankle weights removed with a gpt patch-composite (pad to 2:3 to avoid distortion, then feather ONLY the two ankle patches back onto the native-res original) — cv2 inpaint smudged the ankles, gpt was needed.

**Email 02 (light-touch social batch):** folder `clients/sportif/email-02-social/` (downloads/ + created/ + README + email-to-lucy.md). 4 feed (4:5) + 4 stories (9:16) from the 4 cleaned photos, `build_email02_social.py`. Branding = the REAL logo lockup (SPORTIF Glacial Regular tracking -0.059 + underline rule) top-right, @sportifcollection centred beneath, over a soft top-right corner scrim. Hugo QA caught two logo bugs: the underline was missing (I'd used bare wide-spaced text) and the handle was right-aligned (skewed) not centred under the wordmark — both fixed.

**Poster experiments** (Hugo loved a JANNAYON collage poster; borrow the LAYOUT, keep our warm palette not periwinkle, own the type):
- gpt-image-2 poster (`gen_poster_jannayon.py`) then a pixel-perfect pass: cv2.inpaint lifts gpt's baked-in headline/wordmark off Hugo's high-res ChatGPT render, we lay real Glacial (`poster_final_type.py`).
- `poster_lucy_real.py` flat grid from Lucy's real photos (parametrised: headline + output name as args; made an "IT'S PARTY TIME" demo for Hugo's brother-in-law).
- `poster_lucy_depth.py` cut-out pilates hero pops forward over the headline with a soft cast shadow; cv2 painted out a second person's stray forearms before matting.
- `poster_lucy_layered.py` SPORTIF wordmark sandwiched between a faded legs-in-air background and the ball hero in front. BLOCKED on a clean ball cutout (Q-008).

**New Mac tooling installed:** rembg (isnet-general-use) + onnxruntime + opencv (cv2) + scipy + numpy = matting, cv2.inpaint (text/object removal), distance-transform defringe (also used for `band_cutouts.py`: transparent light/medium/heavy + joined-set band PNGs for Hugo's Photoshop).

**Learnings:** (a) Canva MCP here = search + generate + export only; can't read/edit, export fails "Not allowed to access" on view-only shared designs -> manual download flow (D-010). (b) White-on-light mattes fail in rembg (white ball + bra on a light wall smeared); Hugo cuts those in Photoshop, plain-bg subjects matte perfectly (D-012). (c) gpt poster: prompt craft was equal, quality tier is the differentiator (Hugo's full-quality ChatGPT > my harness-capped low) -> he runs hero finals in ChatGPT, I iterate + do exact-type production. (d) Saved the [[go-the-extra-mile]] feedback memory (fix obvious imperfections before showing, do not ask).

**Open:** Q-007 (Lucy's reply on the email-02 socials), Q-008 (Hugo's PS cutout of the ball hero), Q-009 (email 03 pending screenshot). See [[real-band-content-pipeline]], [[go-the-extra-mile]].

---

## Session 027 (2026-07-25, Claude Code): Lucy expert-brand content strategy (Phase 1) + disk cleanup

Client: Sportif
Tags: content-strategy, lucy, expert-brand, devin-jatho

Hugo's idea: apply the Devin Jatho expert-brand / 4-quadrant model (transcript in `devin-jatho/`) to Lucy Wayne, so content builds her authority and converts to SALES not just followers. Devin's system: build an EXPERT brand (trust of expertise) not a personal brand; 3 switches = (1) expert niche defined by the problem your offer solves + one avatar, (2) four non-overlapping content quadrants, (3) give your best away free (positive reinforcement). We adapt it as founder-led authority marketing for a product brand.

**Direction locked (Hugo's calls):** authority-first (monetise later, perfect for the trademark hold), hybrid on-camera (Lucy's real presence + our produced content), editorials via links.

**Phase 1 done:**
- Fetched + analysed Lucy's 3 published interviews (voyagela, boldjourney, magnateview). She is a fashion-designer-turned-celebrity-stylist (Katy Perry, The Great Gatsby) AND certified PT + reformer Pilates devotee. Her unfair advantage = the STYLE + STRENGTH fusion, aimed at REAL women (size 14+, inclusive), the antidote to the White Fox world (reinforces existing brand.md positioning).
- **Le Sport Collectif was the OLD brand name; Sportif is LOCKED IN** (so the trademark issue is not the name). Confirmed by Hugo.
- Built `clients/sportif/lucy-content-library.md` (internal draw-from: taglines, her real quotes, DRAFT mantras clearly separated so we never misattribute) and `clients/sportif/lucy-profile.md` -> rendered to `lucy-profile-for-review.pdf` via `build-lucy-profile.py` (headless Chrome, since weasyprint is not on the Mac; Glacial fonts base64-embedded, warm palette).
- The PDF is titled **"Content Creation Strategy"** and written as a WARM STUDIO LETTER from Ocho Productions to Lucy (Hugo: the first draft read too AI/clinical). Carries the principle "every piece has a job, pointed at a sale" and the give-value-then-ask (jab) idea, and a "What happens next" list of 6 candidate topic directions for her to react to.

**Disk cleanup:** Hugo's Mac boot volume was full (121MB free of 460GB), which broke a file write. Cleared safe regenerable caches at his OK (Adobe media cache ~79GB, BorisFX ~10GB, Chrome ~2.2GB, VSCode ~1.5GB) -> freed ~93GB. Left NordVPN (23GB) and Claude app data (16GB) untouched (his data).

**Open:** Q-006 = Phase 2 (lock Lucy's expert niche, one avatar, and FOUR quadrants) pending Lucy's reaction to the PDF. See [[real-band-content-pipeline]].

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
