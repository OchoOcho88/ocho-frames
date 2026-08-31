# Workspace Memory Archive

Older session entries moved out of memory.md to keep it light.
Same format, same rules, nothing deleted. Newest archived batch at the top.
The newest 4 Weekly Reviews stay in memory.md; older ones are archived here.

---

<!-- CURRENT STATE bullets retired 2026-08-31, session 036 -->

## Retired CURRENT STATE bullets (as at 2026-08-31)

These accumulated in memory.md's CURRENT STATE block from Session 015 to Session 035
until it reached 41KB against a brief of about 12 lines (Q-021). Moved here verbatim,
nothing deleted. The settled parts of each are in DECISIONS.md; the narrative is in the
session entries; the live loops are in OPEN-QUESTIONS.md.

- **NEW (Session 035): Lucy's second round of marks is in, and the positions were MEASURED, not eyeballed.** Four phone photos of her pen marks on the v2 files were matched to the real assets with SIFT plus a RANSAC homography, warped into asset pixel space and differenced so only the pen remained. Built by `build_email02_social_v3.py` into `created/v3/`; her marks and the method are at `email-02-social/lucy-marks-2026-08-26/README.md`. Three of the four needed a documented nudge, for Instagram's 260px story chrome and for the ceiling beam that enters the type footprint at y370. See D-041.
- **NEW (Session 035): the peach grade hit a hard ceiling, and the ceiling is the answer (D-042, D-043).** Two attempts failed and Hugo called both on sight: the first lifted every shadow (story-duo black point 0.024 to 0.094) and read "washed out and lifeless"; the second added saturation and contrast and read "fake tan". **On these photos more peach and tanned skin are the same slider**, because skin and the studio wall both sit near hue 25 degrees, and a hue-based skin mask selects 91% of the frame. The corrected grade, both dead ends, and the reasoning live in `scripts-local/sportif_grade.py`; LUTs at `assets/luts/`; the set is parked in `created/v4/`.
- **NEW (Session 035): THE WEAVE ROOM. Hugo built it himself in Photoshop and it is the best thing produced today.** Separating the person from the room removes the ceiling entirely, verified (her average brightness 53.4% before and after, no halo). On that split he built a terracotta `#833827` Solid Color fill at Overlay 60%, measured safe, then the band's own weave over it held to the wall with Blend If. Recipe and PSDs at `email-02-social/photoshop/`. Two results worth keeping: black type beats white on terracotta 6.8:1 against 2.1:1, and the 1024px tile is fine at feed size but will seam on a 1920 story, so stories need the plate. Not house method until Lucy reacts.
- **NEW (Session 035): email SENT to Lucy, and reading her 21 Aug message properly surfaced three things nobody had flagged.** The pilates picture is going to the **Fit Expo booth**, which is PRINT, and everything we have is 1080px (Q-027). She has handed us the **handle rule**, off for Instagram and on for booth assets (Q-028). And she is expecting the **3D band**, which has not been started (Q-016). Split into separate emails to keep the reply on one subject; both are promised to her in writing. 12 attachments, draft at `email-02-social/TO-SEND-2026-08-26/email-to-lucy-v3.md`. **Q-012 is closed.**
- **Two writing rules from Session 035, both caught by Hugo.** Lucy is NOT the model in the email-02 photos, they are her Canva picks, so never write "you" about the person in frame. And "blush" cannot be used for the MEDIUM band, because Blush Peach `#F0CDB3` is the primary brand colour: refer to bands by weight, one colour name each per document. Both are warnings at the top of the draft.
- **NEW (Session 034): the SPORTIF weave tiles are a complete set, and an email about them has gone to Lucy.** Three 1080x1350 Instagram feed posts, one per colourway, sitting as one grid row, built by `clients/sportif/scripts-local/build_texture_weight_tiles.py` into `generated/images/texture-weight-tiles/`. Full-bleed single-crop weave plate (no mirror seam), the canonical SPORTIF / rule / collection lockup at 66% of canvas width, a two-pass warm drop shadow, and the WEIGHT as a fourth line in caps with wide tracking, sized off MEDIUM so all three share one point size. The white shooting sheet is trimmed out automatically by a median-saturation scan. Each plate is tone-matched to its D-027 colourway with a per-channel gamma. Files numbered POST-1 (heavy) to POST-3 (light) by upload order, because Instagram puts the newest post on the left. Email SENT with all three attached, draft at `clients/sportif/message-to-lucy-weave-concept.md` (Q-024).
- **NEW (Session 034): EVERY band cutout in the workspace was about a stop underexposed, and is now fixed (D-039).** Measured against D-027: LIGHT 47% value against 72%, MEDIUM 37% against 62%, HEAVY 24% against 42%, saturation down about a third across the board. Invisible on the white shooting sheet, ruinous on a dark gym floor. Corrected copies live at `assets/Sportif_Bands/Bands_background_removed/colour-corrected/` and **that folder is the only one to composite from**. Hugo cut out medium and light himself in Photoshop this session; all three cutouts verified clean at the edges, no white rim.
- **NEW (Session 034): the Lucy-friend band placement job is set up and shot 01 is built.** `clients/sportif/lucyfriend-band-placement/` holds `lucy-direction/` (her four marked-up screenshots, renamed to pair with each photo), `plates/`, `created/`, a README and `PHOTOSHOP-GUIDE.md`. Five source photos renamed and filed. **The bands are PROPS on flat surfaces, not worn, and Lucy's marks never overlap her, so no clean plate is needed and she is never cut out.** No direction for shot 03, so that one is improvised in two versions. Shots 04 and 05 sit against a mirrored wall and need a flipped, dimmed reflection or they will read wrong.
- **DECISION (Session 034, D-038): Lucy's friend's photos go through no image generator at any stage.** She has not consented to her likeness being used that way and Hugo is not asking. His call and it stands. It costs nothing, because the props method needs no AI.
- **Learning (Session 034, D-040): the staging trap.** Our cutouts are catalogue poses, laid out flat and squared up. Composite one into a candid photo and it reads pasted even when light, shadow and colour are all correct. Proven by measurement: the band darkened the floor by 16 levels against 30 for the real skipping rope handles, so the shadow was too light rather than too heavy. The tell was tidiness. Fix in Photoshop with a small Warp; fix properly by photographing the band actually dropped on a floor (Q-023).
- **Learning (Session 034): apply the EXIF rotation flag before describing any iPhone photo.** Three of five filenames were wrong because a contact sheet was built without `ImageOps.exif_transpose`. What was called "standing rack full length" is her seated on a BOSU.
- **NEW (Session 033): the session protocol is now two commands, and both halves are checked.** `python3 scripts/startup.py` (`/startup` in Claude Code) and `python3 scripts/closeout.py --commit -m "..."` (`/close-out`). Startup reads the state, close-out checks and writes it. Startup prints the environment, this session's number, git state with a dirty-tree warning, CURRENT STATE, open loops for the active client, the content gate, house rules and flags. Close-out clears stale git locks, sweeps changed files for em and en dashes, verifies the session entry and CURRENT STATE block are real and correct for THIS session, runs the archiver, index and check, and refuses to commit while anything fails. The reason it is a script and not a paragraph: CLAUDE.md is not auto-loaded in Cowork (S031), and the protocol was skipped again at the top of this session. See D-035.
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
- **Hugo spotted the next problem in the same frame and my fix did not land (D-034, REJECTED).** With the label finally legible, he flagged that the WEAVE was wrong. He is right: side by side, the generated fabric is fuzzy towelling while the real band is a fine interlocking knit with a diagonal rib. Rather than re-prompting, wrote `clients/sportif/scripts-local/retexture_band.py`, a **texture transplant**: isolate the band (saturated, mid-dark, largest blob, widest rows only, which is what stops leg shadows being swallowed), tile the real texture plate over it at the correct physical scale, then multiply by the generated plate's own blurred luminance so the model's shading, curve and cast shadow all survive. The moulded label is masked out and untouched. Before and after at `generated/images/band-posters/gpt-plates/retexture-before-after.jpg`. **The rule this settles: band LARGE in frame means transplant the weave; band SMALL means swap the label and leave the weave alone.** Both halves of the product are now recoverable from any decent plate.
- **Hugo's verdict on the transplant: "that looks bad".** Recorded as rejected rather than argued with. The weave problem is real, but tiling the real texture over a generated band reads flat and pasted, so it is not the answer. **The rule that survives: never let a generator draw the band at large scale.** Big in frame means shoot it or composite the real cutout. Small and incidental means generate and swap the label. The script stays on disk as a dead end that was tried, not as house method.
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
- **Open for Lucy:** two scratch music beds on the band-in-use reel (calm ~100 BPM vs upbeat ~118 BPM), Hugo showing her both for beat-pacing pick. All scratch music is unlicensed preview only.
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

<!-- Weekly Reviews archived 2026-08-31, session 036, second pass -->

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

---

<!-- Weekly Reviews archived 2026-08-31, session 036 -->

## Weekly Review, 2026-07-19 (week of 2026-07-13)

One session this week (019, 2026-07-18), a sharp drop from last week's six. The week's planned centre of gravity, the Tuesday 2026-07-14 Lucy meeting, happened off-workspace and its outcomes were never logged, so nearly the entire open backlog is still hanging in the air five days later. The one session that did run was a clean, self-contained production win on the image pipeline.

### Highlights
- **First production use of the gpt-image-2 `images/edits` endpoint (Session 019).** The Cosmos reference editorial (backbend pose) was edited to a baby blue outfit with the FORM wordmark replaced by the real SPORTIF lockup, no mask needed, a "two changes only" prompt held pose, grain, and backdrop. Three keepers saved to `clients/sportif/generated/images/`, including a reusable text-free base.
- **A second overlay tool joined the pipeline: `scripts/overlay_logo.py`** stamps the full Sportif lockup (Glacial Indifference Regular, -0.059 em tracking, short underline, geometry measured from the reference logo asset). Rule established: `overlay_logo.py` for the logo lockup, `overlay_wordmark.py` for plain headline text only.
- **A third environment flavour was identified and characterised: the Cowork CLOUD sandbox** (Anthropic container + device bridge). Shell calls are NOT capped at 45s, the ~70s high-quality render completed in one call, but files only reach the Mac via an explicit commit step. Recognisable by `/mnt/user-data/uploads/` paths and `device_*` tools.

The week's big miss: **the Tuesday Lucy meeting outcomes (launch slip reason, new launch date, waitlist page approval, incentive decision) are still not captured anywhere.** Last week's #1 suggested focus was "make the Tuesday meeting count", whether it did is currently unknowable from the workspace.

### Patterns I noticed
- **Human eyeball review keeps catching what tooling can't.** Hugo spotted the wrongly styled first-pass wordmark (hand-styled Bold, wide tracking, no rule) just as he caught the Reel's bottom-edge glitch and the IG crop bug in prior weeks. Verification on the real output by a human remains the last, essential QA gate.
- **Environment constraints keep reshaping the workflow map.** Last week it was the 45s Cowork cap and the ~60s Claude Code cap; this week a third flavour (cloud sandbox, uncapped shell but explicit file commit) joined. The division-of-labour table now has three columns, and recognising which environment a session is in is becoming a session-start skill.
- **The Lucy bottleneck has evolved into a logging gap.** For weeks the pattern was "waiting on Lucy"; this week the meeting apparently happened but the workspace has no record of what was decided. The blocker is no longer only external, un-logged decisions block exactly like un-made ones.

### Skills / knowledge gained
- **gpt-image-2 edits endpoint:** works mask-free when the prompt is scoped to explicit, enumerated changes ("two changes only"); validate at quality low, final at high.
- **Output-stage moderation can false-positive [sexual] at quality high** on poses like backbends even when low passes; appending "tasteful, professional athletic fitness editorial photograph... modest full-coverage sportswear" clears it. Keep that sentence for bodysuit/backbend imagery.
- **Logo-lockup stamping specifics:** tracking -0.059 em, underline rule, geometry measured from `assets/05-logo-sportif-white-on-peach.png`, colour sampled from the source image being replaced (cream #F4F2EA from the FORM letters).
- **Cloud-sandbox mechanics:** uncapped shell calls, live reads via the device bridge, explicit commit step to persist files to the Mac.

### Open questions still unresolved
- [ ] **Log the Tuesday 2026-07-14 Lucy meeting outcomes** (launch slip reason, new launch date, standalone waitlist page approval, incentive decision A/B/C, Shopify blocker movement). From Session 019; still open, most of the backlog below hangs off this.
- [ ] Carried from last week, all still open pending the meeting outcomes: standalone waitlist capture page build, 3-email welcome flow, Lucy blocker email (still in Gmail drafts), Lucy feedback backlog (taglines, colourways, hero pick), confirm whether the 500 band units landed, ambassador/instructor seeding shortlist (fifth week carried, needs nothing from Lucy), Shopify coming-soon/store build, trademark clearance, materials question, Stage 3 synthesis template + Seedance adapter, PDF generators still on Poppins, optional true-high background re-render, optional teaser voiceover, git push from Claude Code (local ahead again).

### Suggested focus for next week
1. **Capture the Lucy meeting outcomes first, before anything else.** The meeting is now 5+ days past and memory decays; one short session logging the slip reason, new launch date, waitlist page verdict, and incentive pick would re-anchor the whole backlog and un-gate items 2 and 3.
2. **Ship the standalone waitlist capture page + 3-email welcome flow** the moment the meeting notes confirm approval. It's the one workstream that routes around Shopify, the Funnel 1 spec is written, and every piece of built content is dead-ended until it exists.
3. **Start the ambassador/instructor seeding shortlist.** Now carried five straight weeks, designated the main growth engine, needs lead time before any launch date, and requires nothing from Lucy or the meeting outcomes, it can start today.

---

## Weekly Review, 2026-07-12 (week of 2026-07-06)

Six sessions this week (013, 014, 015, 016, 017, 018), the busiest week the workspace has had. It split into two halves: an early-week production sprint for the planned Friday Instagram launch (grid banner, tagline row, teaser Reel), then a strategy pivot after the launch slipped, with the Australian Marketing Summit notes turned into a permanent funnel layer. The week ends staged for the Tuesday 2026-07-14 Lucy meeting.

### Highlights
- **The teaser Reel is rendered and launch-ready in two variants (Session 016).** 15s, 1080x1920, brand-colour end card holding ~3s, plus a CTA variant driven by a HyperFrames composition variable. A subtle bottom-edge glitch Hugo spotted was diagnosed by frame-sampling and fixed with the over-cover pattern. This was the workspace's first real HyperFrames production piece taken all the way to a shippable render.
- **The full Friday grid package was built and the posting recipe proven on a mock account (Session 015).** 3-tile SPORTIF banner in three colourways, a tagline row in four directions with action imagery, and a live debug of Instagram's 1:1 default crop that was eating letters at tile edges. The recipe (tap Original, 1080x1440 tiles, post right tile first) is verified working.
- **A permanent funnel layer landed (Sessions 017 to 018).** Summit notes became `docs/funnel-playbook.md` (reusable, research-cross-checked) plus `clients/sportif/funnel-plan.md` (3 funnels, Klaviyo flow spine, budget), and an audit bound content to funnel: every post now carries exactly one CTA to the waitlist, FAQ is the fourth content lane, signups per post is a scorecard metric.
- **Key strategic unlock: the waitlist capture page does not need Shopify.** A standalone landing page can go live now, un-deadending every post and partially bypassing the months-long Lucy/Shopify blocker. This reframes the critical path and tops the Tuesday agenda.
- **Workspace hygiene caught up (Sessions 013 to 014).** Full review and cleanup, 9 superseded PDFs archived, five weeks of git work committed and pushed to GitHub, the CURRENT STATE block and two-environment sync protocol established, memory auto-archiving built, and the gpt-image-2 pipeline went live with the real Glacial Indifference font overlay pattern.

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
- **Funnel method fundamentals** (Donati): one page one choice, the "How to [outcome] without [objection]" headline formula, honest scarcity, and the content x funnel mapping discipline, plus 2026 conversion benchmarks to sanity-check it.
- **Pillow has no letter tracking;** draw glyph by glyph with per-glyph advance.

### Open questions still unresolved

**Resolved this week (settled by a later session):**
- [x] ~~Did the Friday 2026-07-10 IG launch happen?~~ RESOLVED Session 018: it did NOT happen; reason to be captured at the Tuesday meeting.
- [x] ~~Re-render the 3 action backgrounds at quality high before Friday (Session 015).~~ RESOLVED Session 016: rendered at medium (60s cap blocked true-high), Reel launch-ready; true-high remains an optional upgrade.
- [x] ~~Hugo to git push from the Mac (~10 commits ahead).~~ RESOLVED Session 014: pushed, in sync at the time (local is ahead again after 017 to 018; push at next Claude Code session).
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

---

<!-- archived batch, moved 2026-08-31 -->

## Session 030 (2026-08-11, Cowork): SPORTIF collection grid tiles (Lucy's reference lockup across 3 IG tiles)

Client: Sportif
Tags: lucy, instagram, grid-banner, collection, wordmark, glacial-indifference, pillow

Lucy asked for the Instagram grid banner again, this time with "collection" underneath the wordmark, and gave a square reference lockup (peach background, white SPORTIF, short rule, lowercase "collection") which Hugo saved to `clients/sportif/Sportif_Collection/Sportif_Collection_wordmark.jpg`. Note the word is **collection**, not "collective" (Hugo typed collective, the artwork says collection, confirmed with him before building). "Le Sport Collectif" remains the retired old name.

**Confirmed with Hugo before building:** wording = collection; tile shape = 3:4 portrait 1080x1440 (same as the first grid); colourway = peach `#F0CDB3` with white type only, matching the reference. Cream and white variants were offered to Lucy in the email rather than built up front.

**Built:** `clients/sportif/scripts-local/build_collection_grid.py`, adapted from `build_grid_banner.py`. One 3240x1440 peach master, SPORTIF in Glacial Indifference Regular tracked at 0.28em to 80% of canvas width, a rule, then "collection" at 0.06em tracking, split into three 1080x1440 tiles whose file numbers ARE the posting order (rightmost posts first). Deliverables + `POST-ORDER.md` in `clients/sportif/Sportif_Collection/grid/`. Sampled the reference background as (241,205,179), effectively the brand blush, so used `#F0CDB3`.

**The one real design problem, and the fix.** Reproducing the reference proportions literally (sub ascender = 0.48x the SPORTIF cap height, taken off the 500px reference: cap 41, sub ascender 20, rule 90 wide vs sub 120 wide) blew "collection" out to 1030px inside a 1080px tile, hard against both gutters. The cause is that SPORTIF is tracked enormously wide to span three tiles, so anything sized off ITS cap height inherits that stretch. Fix: size the sub as a share of the CENTRE TILE (0.55 of tile width) and the rule as 0.75x the sub width (the reference's own rule-to-sub ratio). Result reads like the reference and keeps roughly 245px of clear space either side. Lockup vertical balance checked by ink-bounds scan: top margin 307, bottom 340, i.e. a slight optical lift.

**Also settled:** brute-forced tracking 0.24 to 0.34 and sizes 440 to 560 and found NO combination where a tile seam misses every letter. A 7-letter word across 3 tiles always has a seam land inside a glyph, so the clipped T crossbar is inherent to the format (the first grid had it too and Lucy accepted it). Worth saying out loud in future client emails rather than being asked about it.

**Sent:** email drafted at `clients/sportif/email-to-lucy-collection-grid.md` and Hugo sent it with the attachments the same session.

<!-- archived batch, moved 2026-08-27 -->

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

<!-- archived batch, moved 2026-08-26 -->

## Session 028 (2026-07-28, Claude Code): Lucy's Canva requests (emails 01 + 02) + poster experiments + matting/inpaint tooling

Client: Sportif
Tags: lucy, canva, social, posters, cutouts, rembg, cv2, logo-lockup

Multi-day session working Lucy's Canva design requests, one self-contained folder per request.

**Email 01 (finished the pilates reskin ad):** Lucy asked to add the band + logo and remove the ankle straps on the hip-raise model. Clarified with Hugo: band shown as a PRODUCT PLACEMENT (not worn) + the SPORTIF logo, original raised-leg pose kept (not the glute-bridge variant). `reskin_clean_plate.py` retouches the worn band off the plate; `layout_reskin_clean.py` lays the type + band card. Final `reskin-clean.png`.

**Lucy's 4 photos cleaned** into `reference-images/lucy-canva-picks/` (NON-AI where possible): downloaded the "Use these Pictures only for Social Media" Canva pages, cropped the sky/hills Canva bg off the reformer-duo, cleaned the pilates ref (removed the PILATES watermark by flattening the background beige + the "First class is free!" navy text via cv2.inpaint). Black ankle weights removed with a gpt patch-composite (pad to 2:3 to avoid distortion, then feather ONLY the two ankle patches back onto the native-res original), cv2 inpaint smudged the ankles, gpt was needed.

**Email 02 (light-touch social batch):** folder `clients/sportif/email-02-social/` (downloads/ + created/ + README + email-to-lucy.md). 4 feed (4:5) + 4 stories (9:16) from the 4 cleaned photos, `build_email02_social.py`. Branding = the REAL logo lockup (SPORTIF Glacial Regular tracking -0.059 + underline rule) top-right, @sportifcollection centred beneath, over a soft top-right corner scrim. Hugo QA caught two logo bugs: the underline was missing (I'd used bare wide-spaced text) and the handle was right-aligned (skewed) not centred under the wordmark, both fixed.

**Poster experiments** (Hugo loved a JANNAYON collage poster; borrow the LAYOUT, keep our warm palette not periwinkle, own the type):
- gpt-image-2 poster (`gen_poster_jannayon.py`) then a pixel-perfect pass: cv2.inpaint lifts gpt's baked-in headline/wordmark off Hugo's high-res ChatGPT render, we lay real Glacial (`poster_final_type.py`).
- `poster_lucy_real.py` flat grid from Lucy's real photos (parametrised: headline + output name as args; made an "IT'S PARTY TIME" demo for Hugo's brother-in-law).
- `poster_lucy_depth.py` cut-out pilates hero pops forward over the headline with a soft cast shadow; cv2 painted out a second person's stray forearms before matting.
- `poster_lucy_layered.py` SPORTIF wordmark sandwiched between a faded legs-in-air background and the ball hero in front. BLOCKED on a clean ball cutout (Q-008).

**New Mac tooling installed:** rembg (isnet-general-use) + onnxruntime + opencv (cv2) + scipy + numpy = matting, cv2.inpaint (text/object removal), distance-transform defringe (also used for `band_cutouts.py`: transparent light/medium/heavy + joined-set band PNGs for Hugo's Photoshop).

**Learnings:** (a) Canva MCP here = search + generate + export only; can't read/edit, export fails "Not allowed to access" on view-only shared designs -> manual download flow (D-010). (b) White-on-light mattes fail in rembg (white ball + bra on a light wall smeared); Hugo cuts those in Photoshop, plain-bg subjects matte perfectly (D-012). (c) gpt poster: prompt craft was equal, quality tier is the differentiator (Hugo's full-quality ChatGPT > my harness-capped low) -> he runs hero finals in ChatGPT, I iterate + do exact-type production. (d) Saved the [[go-the-extra-mile]] feedback memory (fix obvious imperfections before showing, do not ask).

**Open:** Q-007 (Lucy's reply on the email-02 socials), Q-008 (Hugo's PS cutout of the ball hero), Q-009 (email 03 pending screenshot). See [[real-band-content-pipeline]], [[go-the-extra-mile]].

---

<!-- archived batch, moved 2026-08-21 -->

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

<!-- archived batch, moved 2026-08-20 -->

## Session 026 (2026-07-24, Claude Code): memory system v2, hardening for scale (multi-client)

Client: Ochoproductions (workspace infrastructure)
Tags: memory-system, tooling, scaling

Hugo asked for an honest rating of our memory system, then to implement the fixes since the workspace will scale to more clients. Rated it ~8.5/10 for a solo/single-client setup, ~6/10 unmodified at team/multi-client scale; the real ceilings are RETRIEVAL (linear grep, decays with size) and COMPLIANCE (close-out is manual, a single point of failure, we already lost the Tuesday-meeting outcomes once). Built four fixes, all low-tech + stdlib, preserving the plain-markdown legibility.

- **DECISION: adopted memory system v2.** New tool `scripts/memory_tools.py` with subcommands: `check` (verifies close-out: CURRENT STATE dated today + a session entry today + registries well-formed), `index` (regenerates `memory-index.md`, a TOC of every session hot+archived), `search` (grep across memory+registries+docs), `decisions`, `open` (both filter by `--client`; `open` flags questions aged >= N sessions), `reconcile` (flags dead file refs in CURRENT STATE, stale date, aged questions), `install-hooks` (git pre-push warn hook, `MEMORY_ENFORCE=1` to block).
- **DECISION: decisions and open-questions are now first-class registries** (`DECISIONS.md`, `OPEN-QUESTIONS.md`) with a parseable one-line schema incl. a Client field, the two things we re-query most are extractable, not buried in prose, and filter by client.
- **DECISION: multi-client convention.** Session entries now carry `Client:` and `Tags:` lines; registries carry a Client column. One unified chronological log (keeps cross-client learnings) but everything filterable per client. CURRENT STATE will split into per-client mini-blocks once >1 client is active.
- Installed the pre-push hook (warn-only) and regenerated `memory-index.md`. `archive_memory.py` unchanged (still the size-triggered archiver).
- Updated `CLAUDE.md` (close-out ritual now runs `memory_tools.py check` + `index` and updates the registries) and rewrote `docs/memory-system.md` to v2 (Hugo will share that once updated).

LESSON: the compliance SPOF is the biggest real risk as we scale, the `check` hook is the mitigation, but it's warn-only by choice to avoid friction; flip `MEMORY_ENFORCE=1` if close-outs start slipping.

---

<!-- archived batch, moved 2026-08-17 -->

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

<!-- archived batch, moved 2026-08-11 -->

## Session 024 (2026-07-22, Claude Code): reference-layout reskin (Lucy's pilates-studio ad to a Sportif waitlist poster)

Lucy sent a reference: a pilates-studio "WE'RE OPEN / First class is free" launch ad (tan colour block + oversized PILATES watermark + two models, one glute-bridge with black ankle weights, one on a reformer). She asked us to reskin it as Sportif: keep the layout, put OUR band on the model, change the wording, add the logo. Saved to `clients/sportif/products/reference-layouts/pilates-open-ref.png`.

**Established the "reference reskin" technique = AI plate + our own type layer** (Hugo: "NO YOU LAYOUT TEXT, THATS OUR WORKFLOW"):
1. **No-text plate via gpt-image-2 edits** (`scripts-local/reskin_pilates_ref.py`): edit the reference to a CLEAN plate, strip ALL text and the watermark, add a blush booty band, remove the black ankle weights, keeping layout/poses/palette. Generated TWO pose variants to compare: `asis` (keep her raised leg; AI looped the band on the single raised thigh = ambiguous) and `bridge` (convert to a standard two-foot glute bridge; band loops both thighs = clear "in use"). Bridge won.
2. **Our type layer in PIL** (`scripts-local/layout_reskin.py`, system python): all copy in Glacial Indifference, matched navy #13253D / cream #F4EEE5 sampled from the reference. Copy set "Find your resistance": kicker `meet` (small) over `SPORTIF` (bigger, real logotype = Regular + -0.059 lockup tracking), headline `FIND YOUR / RESISTANCE` (cream, soft drop-shadow so it stays crisp where it crosses the photo), faint oversized `SPORTIF` watermark, a solid terracotta `JOIN THE WAITLIST` CTA pill (with lift shadow), the SPORTIF lockup, and `@sportifcollection`.

**Design iterations Hugo drove (each a one-line tweak in the layout script):** first CTA was a wobbly hand-drawn arc, rejected as bad design, replaced with a proper opaque terracotta pill; filled the left cream void with a framed single-band product card (the blush MEDIUM card, `place_band_card`, rounded + shadow + cream border) so product ties to the lifestyle shot (the blend insight, now inside one still); split "meet sportif" onto two lines; switched the kicker to the real logotype font; opened the meet/SPORTIF gap and made SPORTIF bigger; raised the headline ~15% to clear the doorway.

Two finals kept in `clients/sportif/generated/images/reference-reskin/`: `reskin-bridge.png` (the lead piece, with the band card) and `reskin-asis.png` (dramatic raised-leg alt, no room for the card). Both are soft waitlist teasers with NO dates (respecting the trademark hold). Scripts are the source of truth (finals gitignored). Copy/colour/logo font all editable in one line.

**Key learnings:** (a) the reskin technique generalises, hand any reference layout, get a no-text AI plate, own the type in PIL; (b) generate BOTH plate variants when a pose is ambiguous and let the product-clarity decide; (c) a solid opaque CTA pill sits cleanly over any busy area where a thin script line looks amateur; (d) dropping a matching single-band product card into negative space delivers the lifestyle+product blend inside a single still. See [[real-band-content-pipeline]].

**Still open (unchanged):** standalone waitlist capture page (needs neither Lucy nor trademark, still the top unbuilt item); Lucy's music-bed pick; high-res finals past the ~60s cap; trademark gate.

---

<!-- archived batch, moved 2026-07-28 -->

## Session 023 (2026-07-22, Claude Code): real-band product content pipeline (restage, cards, range reel, 2 blends)

Lucy sent Hugo 3 real photos of the bands she received (saved to `clients/sportif/products/real-bands/`). They were casual counter snapshots (clutter, harsh light, all three folded label-end) BUT the product is bang-on brand: the three colourways (HEAVY terracotta / MEDIUM dusty blush / LIGHT sand-cream) ARE the peach palette, and the rubber labels carry the real SPORTIF lockup + resistance tier. This validated the whole peach direction and meant real product could intercut with the AI lifestyle shots seamlessly.

Built a staged product-content suite (Hugo directed "we do in stages"):
1. **Restaged flatlay** via gpt-image-2 `images/edits` (`scripts-local/gen_band_product.py`): scoped "keep the product EXACTLY identical, only change surroundings" prompt strips clutter and drops the bands onto clean peach, holding the labels crisp **even at quality low**. High quality hits the ~60s Claude Code cap (RemoteDisconnected, background doesn't help) -> run from a native Terminal.
2. **3 individual hero cards** (`scripts-local/make_band_cards.py`): cropped each band from the flatlay. Hugo caught a left-edge artifact -> the bands TOUCH, so equal-thirds cropping bled a neighbour sliver onto each card. Fixed by detecting true edges (texture variance for outer, colour/brightness boundary at x~592 for the H/M seam) and cropping inset off the seams.
3. **Range reel** `compositions/sportif-band-range/` (calm Light/Medium/Heavy). Feathered the flatlay edge (Gaussian border alpha) so its peach melts into the peach frame (no rectangle) -- Hugo asked to fix that before viewing.
4. **Two lifestyle+product blends** (Hugo's idea, wanted BOTH): `sportif-blend-cuts` (rhythmic beat-cut, lifestyle cover + product contain, 120 BPM) and `sportif-blend-calm` (editorial card-on-peach story with taglines). Both got mood-matched scratch music. Hugo: "they both look great as concept pieces."

Full reusable pipeline + gotchas written up at `clients/sportif/products/real-bands-content-process.md`. See also [[real-band-content-pipeline]] and [[hyperframes-0-7-tooling]].

Key process learnings (also in the pipeline doc): scope gpt-image-2 edit prompts to keep-product-identical; low quality is fine for social; touching products need colour-boundary crop detection not equal thirds; feather peach-on-peach edges with a blurred alpha mask; the lifestyle+product BLEND is the strongest format (desire + product, but juxtaposition not literal use -- literal-use is the unbuilt Stage 5 composite); system python has PIL-not-numpy, the .venvs/tts python has numpy-not-PIL.

**Stage 4 (they've landed teaser) and Stage 5 (band-in-use pilates reel) both DONE this session.** Stage 4: `compositions/sportif-they-landed/`, announcement teaser, bouncy pop-in headline (+wiggle), popping product reveals, "Find your resistance." band line, "Join our community" CTA pill. Stage 5: `compositions/sportif-band-inuse/`, three pilates poses (standing abduction / squat / lateral walk, barefoot) with the real SPORTIF label stamped via the two-image gpt trick, CTA pill, two music beds (calm + upbeat) for Lucy to pick pacing.

**Stage 5 detours worth remembering:** client gym shots were off-brand (black weights gym, glam register) and even tripped AI `[sexual]` moderation, so we GENERATED fresh modest pilates scenes instead; the real-label two-image stamp at LOW quality looked natural (Hugo preferred it over a pixel-perfect but pasted-looking composite); high-quality label re-render kept hitting the ~60s cap even in the VS Code terminal. Full pipeline + all scripts documented in `real-bands-content-process.md` and each comp's design.md. See [[real-band-content-pipeline]].

**Still open:** print-quality high-res product/in-use finals (need a real macOS Terminal or cloud to beat the ~60s cap); Lucy's pick between the two music beds; and the ORIGINAL top item, the standalone waitlist capture page, still unbuilt (needs neither Lucy nor trademark).

---

## Session 022 (2026-07-22, Claude Code): peach beat-cut montage + scratch music + ElevenLabs setup

Continuation of the Session 021 chat into the next day. Hugo asked for a "quick cut" beat-synced montage from the peach images (different energy from the calm lookbook reel).

**Built `compositions/sportif-peach-cuts/`** (15s, 1080x1920, one file for IG Reels + TikTok). Generated from `build_cuts.py`: a 120 BPM grid of hard cuts with a per-image zoom-punch. Structure: SPORTIF wordmark flash (0-1s), 14 cuts on the beat (1.0-7.5s), a double-time build through the punchiest shots (8-11s), date-free "Coming soon" end card holding ~3.5s to 15s. Full-bleed (punchier than the lookbook's cards) but center-crops the group shots at the edges (acceptable at cut speed). Keeper: `renders/sportif-peach-cuts_v3_high.mp4`.

**Iteration notes (all Hugo feedback):** he liked the cut length + acceleration + zoom-out immediately. Two fixes: (1) extended the end-card hold from ~0.2s readable to ~3.5s (total 12s -> 15s) because the logo only flashed; (2) real bug found by the snapshot QA: the intro's shared `.wm`/`.rule` GSAP selectors also grabbed the end-card wordmark and left it hidden, so the end card showed only "Coming soon" without the SPORTIF lockup. Fixed by scoping the intro selectors to `#intro`. Lesson: scope GSAP selectors per section when class names repeat across scenes.

**Music.** Hugo needed audio to judge the edit. Can't generate licensed music locally (that's HeyGen, which he declined). Synthesized a SCRATCH 120 BPM bed via `scratch_music.py` (numpy/soundfile in the .venvs/tts python: kick on the beat, offbeat hats double-timing through the build, A-minor pad + sub bass), muxed on as `_MUSICDEMO.mp4`. Hugo: "nailed it, the sound helps match the cuts." He is showing the MUSICDEMO to Lucy as a future-feel preview. IMPORTANT: scratch track is unlicensed, internal preview only, never publish it. Real posts get a licensed track (in-app on upload, or send a file and mux + `hyperframes beats` for exact sync).

**ElevenLabs wired (Hugo asked "would elevenlabs be better?", yes, far more natural than Kokoro).** Promoted the `.env.example` slot to active, added `ELEVENLABS_API_KEY=` to the gitignored `.env`, and wrote `scripts/elevenlabs_tts.py` (zero-dep urllib helper: text -> mp3, reads key from .env, `--list` voices, default warm-female "Sarah" voice). Ready the moment Hugo pastes a key. Best for future narrated content (founder story, product explainer), not beat-cut montages.

**Close-out:** committed both compositions' source (renders/audio/snapshots gitignored), the ElevenLabs setup, and this log. See [[hyperframes-0-7-tooling]].

---

<!-- archived batch, moved 2026-07-28 -->

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

**Second half of the session: Hugo asked for a HyperFrames video from the peach images.** Built `compositions/sportif-peach-reel/` (15s, 1080x1920, one file for IG Reels + TikTok) reusing the sportif-teaser engine. Decisions (Hugo picked): card-on-peach framing (each 4:5 shot whole on the blush ground, no crop, premium lookbook feel), proven Lucy-voice taglines, date-free "Coming soon" end card (launch on hold, so no date). Three cosmos-peach text-free bases: studio-yellow-frame / portrait-sage-tank / beach-run-shoreline. Keeper: `renders/sportif-peach-reel_v2_high.mp4` (silent, add a soft music bed in-app on upload). It is a brand-MOOD piece, not product (no band/strap, not real Lucy), fine for the pre-launch hold; a product-forward cut waits on real Lucy + product footage (bands have landed, unboxing filmable).

**HyperFrames upgraded 0.6.37 to 0.7.64 (new features explored):**
- The stricter one-shot `check` gate caught a latent bug our old lint missed: full-frame scene overlays that start visible before their fade (`gsap_fullscreen_overlay_starts_visible`). Fixed with explicit `opacity:0` + `.to()` reveals. Real robustness win, applies to the teaser too if we ever touch it.
- `snapshot` = built-in frame verification; auto-builds a contact sheet AND runs Gemini vision over each frame (descriptions.md) to flag blank/black frames. Replaces manual ffmpeg frame-pulling. Snapshots are regenerable QA, now gitignored.
- Rendered at `-q high` (7.9MB vs 4.6MB standard).
- `tts` (Kokoro-82M, local, free, offline) PROVEN but NOT used: Hugo found the voice "very AI." Needed a Python 3.11 venv (system python 3.9 too old for kokoro-onnx); venv at `.venvs/tts` (gitignored), point `HYPERFRAMES_PYTHON` at it. Full recipe in the composition's design.md. For a natural read, use a real voice or HeyGen cloud voices, not Kokoro.
- `cloud` (HeyGen server-side render, kills the local render-cap problem) NOT adopted: needs a HeyGen account (`auth login`, billed). Hugo declined, local high-quality is good enough for 1080p social. Revisit only if we need 4K or hit local caps.
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

<!-- archived batch, moved 2026-07-24 -->

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

<!-- archived batch, moved 2026-07-21 -->

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

<!-- archived batch, moved 2026-07-11 -->

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

<!-- archived batch, moved 2026-07-07 -->

## Session 007, 2026-06-13, Lucy's assets + questionnaire, brand.md populated, research queued (blocked on egress)

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

## Session 004, 2026-05-26, First successful video-analyzer run (+ Python 3.9 fix)

### What we did
- **Ran the video-analyzer skill end-to-end for the first time**, the open item flagged "first thing for session 004" in Session 003. Analyzed `examples/student-kit/video-projects/linear-promo-30s/final.mp4` (the Linear 30s promo from Nate Herkai's student kit).
- **Saved the report** to `outputs/video-analyses/student-kit-linear-promo-30s-2026-05-26.md` and prepended a small provenance header (source / date / tool / model) so each file in the competitive-intel library is self-documenting going forward.
- **Hit and fixed a Python-version blocker** before it could run (see below).

### What we learned
- **The skill is `disable-model-invocation: true`**, it is NOT in the Skill-tool list and can't be auto-invoked. You run it by calling the script directly: `python3 ~/.claude/skills/video-analyzer/scripts/analyze_video.py <video> [--prompt …] [--fps N] [--model …]`. Report → stdout, progress → stderr.
- **This Mac only has system Python 3.9.6**, no 3.10/3.11/3.12/3.13 anywhere on PATH, and `google-genai` (1.47.0) is installed only for 3.9. So the Homebrew upgrade deferred in Session 003 is still pending, and 3.9 is what we have to run on.
- **The script was incompatible with 3.9 out of the box.** It uses PEP-604 `float | None` annotations (lines for `build_video_part` / `analyze`) with no `from __future__ import annotations`, so 3.9 raised `TypeError` at function-definition time, before any upload. SKILL.md claims "Python 3.10+", which is why this surfaced.
- **The default model `gemini-3-flash-preview` works.** 2.9MB file → inline upload path (≤18MB). Two benign noises in stderr: the Python-3.9-EOL `FutureWarning` and a `thought_signature` "non-text parts" warning, text still returned cleanly.
- **Report quality was good and honest**, all 5 sections, accurate `MM:SS` scene breakdown, verbatim on-screen text, and it correctly reported "No speech detected / cinematic music + whooshes" instead of inventing a narrator (the anti-hallucination guardrails held).

### Decisions
- **Fixed the installed skill in place** by adding `from __future__ import annotations` to `~/.claude/skills/video-analyzer/scripts/analyze_video.py` (one line, behavior-preserving, works on 3.9 AND 3.10+). Chose this over a throwaway `/tmp` copy so the validation reflects the real skill and every future run on this machine just works.
- Used the skill's **default prompt and default model** for this first run (no `--prompt`/`--fps`/`--model` overrides), wanted a clean baseline of stock behavior.

### Open questions / next steps
- [ ] **The `from __future__` fix is local-only and `setup.sh` will lose it.** `setup.sh` re-clones the skill from upstream (mikefutia/claude-vision) on fresh machines, which does NOT have the fix → a fresh clone on a 3.9 box will hit the same `TypeError`. Either (a) PR the one-liner upstream, or (b) have `setup.sh` re-apply it after install, or (c) just upgrade Python to 3.10+ (makes the shim unnecessary, though harmless to keep).
- [ ] **First *real competitor* analysis still untested.** This run was a student-kit teaching asset, not a competitor, and used the script directly, `prompts/competitor-analysis.md` (which routes output to `outputs/video-analyses/`) hasn't been exercised yet.
- [ ] Upgrade Python via Homebrew (`brew install python@3.13`) + reinstall google-genai for it, still from Session 003; would retire the 3.9 shim need.
- [ ] Carry-over from prior sessions: OpenAI + HeyGen keys, verify starter project `npm install && npm run dev`, brand-kit customization, repo-visibility/Pages decision.

### Session 004 addendum, architectural pivot (later in the same session)

After the test passed, Hugo shared the real end goal, this isn't a "competitor analyzer," it's a **creative-strategy pipeline**: ingest competitor content (video OR static) → extract patterns → synthesize a brief adapted to a *client's* brand → output production-ready prompts for AI media platforms (Seadance for video, ChatGPT Image 2.0 for static). That reframe changed the rest of the session from "run the test" to "design the pipeline."

**What we did (addendum):**
- Reviewed a YouTuber's 12-section marketing-conversion framework (Format / Hook / Audience / Pain / Angle / Product Intro / Proof / Beat-by-Beat / CTA / What Works / What's Weak / Steal-Worthy Patterns), strictly better than the workspace's prior 7-section creative-pattern prompt for ad analysis.
- **Rewrote `prompts/competitor-analysis.md`** from a 7-section human-fill-in template into a 12-section `--prompt-file`-ready prompt. Folded the OLD prompt's visual-craft and audio-craft elements into Section 1 of the new one so the creative lens isn't lost. Added a "Critical rules" block (verbatim quotes, no invented narrators, label inferences, N/A allowed).
- **Updated `recipes/analyze-video-with-gemini.md`** Variations section with a real bash invocation for `--prompt-file prompts/competitor-analysis.md` (replaced the "still open" placeholder).
- **Wrote `docs/pipeline-architecture.md`**, the new source of truth for the full 5-stage pipeline. Locks decisions and lists open questions per stage.

**What we learned (addendum):**
- **Default 5-section skill output ≠ marketing analysis.** The YouTuber's 12-section output is a custom prompt, not the skill default. Two different lenses on the same video: default = "describe what's there"; custom = "explain why it converts." For ads work, marketing-conversion is the right lens.
- **The "What's next?" closing offer is a great UX pattern.** YouTuber's outputs end with offered next-steps. Generalizing this into a Stage 5 pipeline convention so every stage ends with offered next moves the user picks from.
- **The competitor-analysis workflow has 5 stages, not 1.** Stage 0 client brief → Stage 1 ingestion → Stage 2 pattern extraction (current 12-section prompt) → Stage 3 strategic synthesis → Stage 4 platform-specific production prompts. Only Stage 2 (for video) is built today.

**Decisions locked (addendum), 4 pipeline-architecture decisions, all documented in `docs/pipeline-architecture.md`:**
1. **Client context lives in per-project brief files** at `projects/<client>/brief.md` (new top-level `projects/` folder, sibling of `my-projects/`).
2. **Static image analysis gets a sibling image-analyzer skill**, deferred to Session 005 for build.
3. **Pipeline shape: modular stages with "What's Next?" handoffs.** Stage 2 always runs; Stages 3-4 are user-triggered from offered options.
4. **Primary AI media platforms: Seadance (video) + ChatGPT Image 2.0 (static).** Runway / Higgsfield deferred but listed for future expansion.
5. **Stopped at architecture for Session 004** rather than start building Stages 0/3/4. The pivot was significant enough that locking the plan in writing > rushing into half-built scaffolding. Session 005 starts from a clean architectural map.

**Open questions / next steps (Session 005 entry point):**

Pipeline build queue:
- [ ] **Stage 0, Set up `projects/` folder + `_template/brief.md`.** Smallest blocking dependency for everything else. Convention documented in `docs/pipeline-architecture.md`.
- [ ] **Stage 5 first half, add "What's Next?" closing block** to `prompts/competitor-analysis.md` so analysis outputs end with offered next moves.
- [ ] **End-to-end smoke test**, pick a real client, drop a competitor video into the project folder, run Stage 2 with the new 12-section prompt, validate the whole flow works. **(Supersedes the "first real competitor analysis still untested" item from earlier in this entry.)**
- [ ] **Research Seadance + ChatGPT Image 2.0 current prompt formats** before writing Stage 4 prompts. Their formats have evolved, old templates won't work.
- [ ] **Write Stage 3** (`prompts/synthesis-creative-brief.md`). Takes client brief + analyses → produces adapted creative direction.
- [ ] **Write Stage 4 prompts** (`prompts/production-seadance.md` + `prompts/production-chatgpt-image.md`). Each takes the synthesis brief → outputs a paste-ready platform prompt.
- [ ] **Add image-analyzer skill** for static-image competitor analysis (Stage 1 second path). Standalone build, likely its own session.

Per-stage design questions (full list in `docs/pipeline-architecture.md`):
- Stage 0: free-form vs. strictly structured `brief.md`? One per client or one per *campaign*?
- Stage 1: image-analyzer via Gemini API (script) vs. Claude native vision (chat-only)?
- Stage 3: single synthesis output vs. multiple creative directions?
- Stage 4: character-count caps for Seadance? Batch variations for A/B testing?
- Stage 5: hardcoded offers per stage vs. dynamically generated from prior output?

### Session 004 second addendum, Devil's Advocate pass + Stage 0 built + Sportif onboarded

After the architecture was documented, ran a Devil's Advocate pass (using the installed skill) to pressure-test the plan before committing more to it. Seven challenges raised. Five led to material changes; two held up (one we kept, one was minor).

**Devil's Advocate outcomes:**

| Challenge | Outcome |
|---|---|
| 1: Building scaffolding for clients you don't have yet? | **Resolved by reality:** Hugo HAS a real client, **Sportif**, fitness accessories, brand new company, launching September 2026. Needs brand identity, brand kit, and launch content for Instagram, TikTok, Facebook. No content or brand kit yet. Concrete deadline (~4 months) reshaped priorities. |
| 2: Is competitor-first pipeline ordering backwards? | **Pipeline now supports two modes:** brand-first (established clients) and competitor-first (net-new launches like Sportif). Picked per client, documented in client README. |
| 3: Stage 0 over-engineered for actual needs? | **Simplified.** Combined brand-kit + brand-identity into ONE `brand.md` file. Template now ~6 meaningful files instead of 12. Grow as needed. |
| 4: Platform lock-in to Seadance + ChatGPT Image is fragile? | **Adopted platform-agnostic structure.** Stage 4 split into `prompts/production-brief.md` (platform-agnostic intermediate format) + thin platform adapters at `prompts/adapters/<platform>.md`. Adapters can swap without touching the brief format. |
| 5: No quality-control / review checkpoint? | **Added Stage 5: Review & Iterate** as a real stage in the architecture. Feedback maps to a specific upstream stage and re-runs that stage. Per-campaign review notes file. |
| 6: Two-Claude workflow is more overhead than value? | **Kept by Hugo's choice**, he's used the pattern before successfully, and needs an explainer (Cowork advisor) for what Opus is producing in VS Code while he learns. Net positive for his learning curve. |
| 7: `projects/` vs. `my-projects/` collision waiting to happen? | **Renamed both:** `my-projects/` → `compositions/`, `projects/` → `clients/`. Updated 16 references across 12 files. |

**New: Pre-Stage 0 intake layer.** Hugo asked for a questionnaire he can email Sportif to gather brand intake data, plus a SWOT analysis template (with research-helper prompt) for his own strategic read. Built both. The questionnaire is what the client says; the SWOT is what Hugo concludes as the expert. Together they feed `brand.md`.

**What we built (advisor session, one-off exception to Opus-writes pattern):**

- **Renamed `my-projects/` → `compositions/`** (preserved content). Updated `setup.sh`, all READMEs, all prompts referencing the old path.
- **`clients/README.md`**, top-level explanation of the clients/ folder convention.
- **`clients/_template/`** with:
  - `README.md`, onboarding sequence for new clients
  - `brand.md`, combined brand kit + identity skeleton
  - `intake/questionnaire.md`, 10-question email-ready intake (~30 min for client to complete)
  - `intake/swot-analysis.md`, SWOT template with Sportif-style research-helper prompt
  - `products/_template-product.md`, one-per-SKU product skeleton
  - `campaigns/`, `competitor-analyses/`, `_archive/`, `assets/` empty folders with `.gitkeep`
- **`clients/sportif/`** populated as the first real client:
  - `README.md`, engagement status + onboarding checklist
  - `brand.md`, skeleton with known facts (name, category, launch date, platforms) + TBD fields tagged to questionnaire question numbers
  - `intake/questionnaire.md`, Sportif-customized, ready to email (placeholders for founder name + deadline)
  - `intake/swot-analysis.md`, Sportif-customized with research-helper prompt pre-filled for fitness accessories DTC, Sept 2026, Instagram/TikTok/Facebook
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

**Open questions / next steps (Session 005 entry point, revised):**

Sportif-driven:
- [ ] Customize Sportif's questionnaire (founder name, deadline date) and email it.
- [ ] Run the SWOT research-helper prompt (it's pre-filled, just paste into Claude). Populate Sportif's SWOT Opportunities + Threats from the research output.
- [ ] When questionnaire returns, populate `clients/sportif/brand.md` from answers + SWOT conclusions.

Pipeline build (in priority order):
- [ ] Add "What's Next?" closing block to `prompts/competitor-analysis.md` (Stage 6, cheap, immediately useful).
- [ ] End-to-end smoke test with a real fitness-accessory competitor video for Sportif, save to `clients/sportif/competitor-analyses/`.
- [ ] Research Seadance + ChatGPT Image 2.0 current prompt formats (Stage 4 prerequisite).
- [ ] Write `prompts/synthesis-creative-brief.md` (Stage 3, mode-aware).
- [ ] Write `prompts/production-brief.md` + first adapter (Seadance OR ChatGPT Image, pick whichever Sportif needs first).
- [ ] Add image-analyzer skill for static-image analysis (Stage 1 second path).

Carry-over:
- [ ] `from __future__` shim resilience (still applies, fresh clone via `setup.sh` loses it).
- [ ] Python 3.10+ upgrade via Homebrew, would retire the shim need.
- [ ] OpenAI + HeyGen keys + brand-kit customization + repo-visibility decision (from prior sessions).
- [x] ~~Rename `brand/brand-kit.md` to `brand/agency-brand-kit.md`~~ DONE (Session 004 cleanup). Path references updated across docs, prompts, and this file.

### Session 004 third addendum, voice rules + agency identity + Sportif onboarding email fully ready

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

**Open questions / next steps (Session 005 entry point, updated):**

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

## Session 003, 2026-05-25, video-analyzer skill installed, Gemini API key live

### What we did
- **Installed the video-analyzer Claude Code skill** at `~/.claude/skills/video-analyzer/` (from https://github.com/mikefutia/claude-vision by Mike Futia, MIT license)
  - Uses Gemini's vision API to "watch" videos and return structured markdown reports
  - Strong anti-hallucination guardrails (won't invent narrators/voiceovers)
  - 220KB skill, single Python script (`scripts/analyze_video.py`)
- **Installed Python dependency:** `google-genai` 1.47.0 via `pip3 install google-genai` (no `--break-system-packages` needed because Hugo's pip is old enough not to enforce PEP 668)
- **Created Gemini API key** on Google AI Studio, scoped to a new project called "Hyperframes" so usage/billing stays separated from other projects
- **Set `GEMINI_API_KEY` in `~/.zshrc`**, system-wide shell env var, available in every Terminal session
- **Verified no conflict with Altarize project:** Altarize Active Campaign (`~/Desktop/OrbitAll/Altarize Active Campaign`) uses ActiveCampaign, Railway, Supabase, Metabase, Claude, Resend, Perplexity, but NOT Gemini. Zero risk of the new hyperframes key being picked up by Altarize.
- **Documented the install in `skills/video-analyzer/README.md`**, the workspace has a pointer doc even though the actual skill lives outside the workspace (at `~/.claude/skills/`)
- **Updated `setup.sh`** to install the video-analyzer skill + google-genai automatically on fresh clones
- **Added `outputs/` folder** at workspace root for everything the AI/pipeline produces (vs `scripts/` which is for inputs):
  - `outputs/video-analyses/`, markdown reports from video-analyzer (tracked in git, builds a competitive intel library over time)
  - `outputs/downloads/`, competitor videos (gitignored, copyright + size)
  - `outputs/generated-images/`, AI image generations (gitignored)
  - `outputs/voiceovers/`, AI narration audio (gitignored)
  - Updated `prompts/competitor-analysis.md` to route output to `outputs/video-analyses/` instead of `scripts/`
  - Updated `README.md` to document the inputs-vs-outputs distinction

### What we learned
- **Two ways to manage API keys, each appropriate for different things:**
  - **Shell env var (`~/.zshrc`):** system-wide, always-on. Good for tools that expect env vars (like the video-analyzer skill). Bad for project-scoped secrets, anything else on your Mac can read it.
  - **Project `.env` file:** project-scoped, loaded on demand via `python-dotenv` (`load_dotenv()`) or `dotenv.config()` in Node. Good for keeping projects isolated. Standard best practice.
- **`load_dotenv()` default is NOT override.** By default, if the shell already has `MY_VAR` set, `load_dotenv()` will NOT replace it with the `.env` value. To force `.env` to win, use `load_dotenv(override=True)`. This is a subtle conflict source, flagged so future Altarize work (or any project adding `GEMINI_API_KEY` to its `.env`) doesn't get the wrong key.
- **Claude Code skills live at `~/.claude/skills/`**, separate from workspace `skills/` and project `.agents/skills/`. Three scopes:
  - **Cowork Personal skills** (Customize panel in Cowork), across all Cowork sessions
  - **Claude Code skills** (`~/.claude/skills/`), across all Claude Code sessions
  - **Workspace skills** (`~/Desktop/hyperframes/skills/`), only when working in this workspace
  - **Project skills** (`<project>/.agents/skills/`), only inside that project
- **Pip 21.x is OLD** but works fine for our purposes. Decided NOT to upgrade Python via Homebrew right now to avoid mid-flow disruption. Worth doing later as its own focused task: `brew install python@3.13` + reinstall google-genai for the new Python.
- **Gemini free tier limits:** 15 requests/min, 1,500 requests/day. Plenty for personal use.

### Decisions
- **Did NOT upgrade Python via Homebrew this session**, added to open questions for later. Reasoning: validating skill works on current setup first, then doing clean upgrade as its own session.
- **Did NOT touch Altarize's `load_dotenv()` calls** to add `override=True`, only an issue IF Altarize ever adds `GEMINI_API_KEY` to its `.env`, which it currently doesn't. Documented in open questions in case it ever does.
- **Skill installed at `~/.claude/skills/` (NOT in workspace `skills/`)**, required by the skill's hardcoded path. Workspace `skills/video-analyzer/README.md` is a pointer doc only.
- **Created separate Google AI Studio project** ("Hyperframes") for the new key so usage/billing tracks separately from the existing "Altarize analysis" project.

### Open questions / next steps
- [ ] **First test of video-analyzer skill**, pick a video file, run end-to-end, validate the output (this is the first thing for session 004)
- [ ] First competitor analysis using `prompts/competitor-analysis.md` + the new skill
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`), still from session 001
- [ ] Get OpenAI API key and add to `.env`, still from session 001
- [ ] Get HeyGen API key and add to `.env`, still from session 001
- [ ] Find out where the "Altarize analysis" Gemini key (from Mar 2026) is actually being used, might be `~/Desktop/Altarize-Content-Pipeline/`, `~/Desktop/Altarize-Landscape-Analysis/`, or `~/Documents/Claude/Projects/Altarize Active Campaign/`. Not blocking, just curiosity.
- [ ] Upgrade Python via Homebrew (`brew install python@3.13`) once video-analyzer is validated working. Includes reinstalling google-genai for the new Python.
- [ ] If future Altarize work adds `GEMINI_API_KEY` to its `.env`, change `load_dotenv()` → `load_dotenv(override=True)` in all `tools/*.py` files
- [ ] Decide repo visibility for GitHub Pages (private requires Pro; public is free), still from session 002
- [ ] Enable Pages in repo Settings → Pages once visibility decision is made, still from session 002

---

## Session 002, 2026-05-23, Framework additions + GitHub repo live

### What we did
- Added three new top-level folders to the workspace:
  - `prompts/`, reusable prompt templates with starter content for CSV→chart, PDF→summary, TikTok hook, product intro, and competitor analysis
  - `recipes/`, workflows we've proven and want to repeat, with a `_template.md` to copy from
  - `skills/`, workspace-level custom skills (different from the project-scoped `.agents/skills/`)
- Scheduled a weekly memory reflection task: every Sunday at 6pm, Claude reads `memory.md`, writes a "Weekly Review" section at the top, identifies patterns, and cleans up resolved open questions
- Documented the distinction between project-scoped vs workspace-scoped skills in `skills/README.md`
- Added `GEMINI_API_KEY` slot to `.env.example` for the incoming video-analyzer skill (uses Gemini Vision because Claude can't natively watch video yet)
- **Initialized git, made first commit (197 files, 2.7MB), pushed to GitHub at https://github.com/OchoOcho88/ocho-frames (private repo)**
- Created `setup.sh` so future clones can restore the ~940MB of reference repos that are excluded via `.gitignore`
- Added Contributing section to README + `index.html` + `docs/PAGES_SETUP.md` for when we enable GitHub Pages

### What we learned
- **Skills can be scoped two ways:**
  - Project-scoped (`my-projects/<project>/.agents/skills/`), auto-loaded by AI agents when the project is opened, ideal for project-specific or framework-specific skills (this is where the 15 HyperFrames skills live)
  - Workspace-scoped (`skills/`), manually referenced, useful for reusable third-party or custom skills like a video-analyzer skill for competitor research
- **Prompts ≠ Recipes ≠ Memory:**
  - Prompts are reusable *starting points* (templates to fill in)
  - Recipes are proven *workflows* (step-by-step sequences that produce known good outputs)
  - Memory is the *historical log* (what we did and why, ordered by time)
- **Competitor analysis is a use case worth investing in early.** Studying what works in the wild is faster than guessing, Hugo has a video-analyzer skill incoming that will plug into the workflow.

### Decisions
- Saved all five starter prompt templates with explicit `[bracket]` placeholders so they're impossible to use without filling in specifics
- Recipes folder starts empty (with template + README), we only add recipes after a workflow has been proven 2 to 3 times
- Scheduled reflection runs Sundays at 6pm local time (cron: `0 18 * * 0`), chosen so the new week starts Monday with clarity
- The reflection task only writes a "Weekly Review" header at the top, never deletes prior session entries (history matters)

### Open questions / next steps
- [ ] Install Hugo's incoming video-analyzer skill into `skills/` and document it
- [ ] First competitor analysis as a real test of the prompt + skill combo
- [ ] Verify the starter project runs end-to-end on Hugo's Mac (`npm install && npm run dev`), still from session 001
- [ ] Get OpenAI API key and add to `.env`, still from session 001
- [ ] Get HeyGen API key and add to `.env`, still from session 001
- [ ] Get Gemini API key once we install the video-analyzer skill
- [ ] **Decide repo visibility for Pages:** GitHub Pages only works free on PUBLIC repos. To enable Pages on the current private repo, either (a) flip the repo to public when ready to share, or (b) upgrade to GitHub Pro ($4/mo)
- [ ] Enable Pages in repo Settings → Pages once the visibility decision is made (see `docs/PAGES_SETUP.md`)

---

## Session 001, 2026-05-23, Initial workspace setup

### What we did
- Created `~/Desktop/hyperframes/` as the workspace root
- Upgraded Node from v20.11.0 → v22.22.3 via Homebrew (`brew install node@22`)
  - Needed a manual PATH override in `~/.zshrc` because an older Node install was winning the PATH fight: `export PATH="/opt/homebrew/opt/node@22/bin:$PATH"`
- Cloned three reference repos:
  - `main-source/hyperframes/`, official HyperFrames source (heygen-com/hyperframes, 18.6k stars, ~122MB without LFS)
  - `examples/launch-video/`, HeyGen's actual launch video (~256MB)
  - `examples/student-kit/`, Nate Herkai's 12-project teaching kit with GSAP (~560MB)
- Initialized a starter project at `my-projects/starter/` via `npx hyperframes init`
- Installed all 15 HyperFrames AI skills into `my-projects/starter/.agents/skills/`
- Created folder structure: `assets/{audio,video,images,fonts}`, `brand/`, `scripts/`
- Created supporting files: `README.md`, this `memory.md`, `.env.example`, `.gitignore`, `brand/agency-brand-kit.md`

### What we learned
- **HyperFrames is "video as code"**, write HTML/CSS/JS, render to MP4. Same input = same output (deterministic). Built for AI agents to generate compositions because they're already fluent in HTML.
- **Why HyperFrames over Remotion:** Apache 2.0 open source (no per-render fees, no seat caps), pure HTML (no React build step), and library-clock animations like GSAP are seekable/frame-accurate.
- **The 15 skills cover everything:** main hyperframes, CLI, media preprocessing (TTS via Kokoro, Whisper transcription, background removal via u2net), animation runtimes (GSAP, Anime.js, CSS, Lottie, Three.js, WAAPI), and conversion helpers (Remotion-to-HF, website-to-HF).
- **The catalog has 50+ pre-built blocks**, `npx hyperframes add data-chart`, `flash-through-white`, `instagram-follow`, etc. Don't build from scratch what already exists.
- **Sandbox limitation:** Claude's sandboxed shell can't run `git clone` directly into the macOS Desktop mount because git's atomic file locking doesn't work over the bridge. Workaround: clone in sandbox `/tmp`, then `cp -R` to Desktop.

### Decisions
- Skipped Git LFS on the main repo (saved ~240MB of test baseline `.mp4` files we don't need for reference)
- Kept all three repos at `--depth 1` (latest commit only) to save space and time
- Brand kit set to modern default, will customize when Hugo has specifics
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

## Session 005, 2026-05-28 to 2026-05-29, Sportif onboarding fired, marketing fundamentals doc, Perplexity integration, post-Lucy trigger system

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
