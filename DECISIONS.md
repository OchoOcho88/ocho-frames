# Decisions log

Settled decisions, extractable (not buried in the session prose). One per line, newest at top.
Query with `python3 scripts/memory_tools.py decisions [--client Sportif]`.

**Row format:** `- [D-NNN] YYYY-MM-DD | Client | decision text (Sxxx)`
(Client = client name, or `Ochoproductions` for workspace-wide. Sxxx = session it was made.)

- [D-024] 2026-08-20 | Sportif | Depth posters have TWO build routes and both are house-standard: Hugo cuts hard mattes and builds hero pieces in Photoshop (extends D-012), and the scripted PIL route handles anything needing several sizes at once. They share one type spec, at `clients/sportif/depth-poster-photoshop-guide.md` (Photoshop tracking values: wordmark -59, headline -20, small caps +160). (S032)
- [D-023] 2026-08-20 | Ochoproductions | Depth between type and subject is built, never generated. Sharp subjects get a cutout; blurred subjects cannot be matted and use the S031 luminance burn-in instead. Either way the plate must be shot against a flat, evenly lit, plain background. (S032)
- [D-022] 2026-08-20 | Ochoproductions | Drop shadows on the warm palette are tinted warm brown (122, 78, 56), never neutral grey, which goes muddy against blush peach. Pad the alpha before blurring so the blur is not clipped at the object's own edge. (S032)
- [D-021] 2026-08-20 | Sportif | Real product cutouts are named `sportif-band-<weight>-<face>.png` (weight = light/medium/heavy, face = front-flat, front-folded, back-flat, inside-grip-a/b, label-detail). Camera roll names are never kept. (S032)
- [D-020] 2026-08-17 | Ochoproductions | Instagram story safe zone: keep all type out of the top 260px and bottom 340px of a 1080x1920 story (profile row + progress bars above, reply bar below). (S031)
- [D-019] 2026-08-17 | Ochoproductions | Social lockup placement is PHOTO-LED, not a fixed corner. An automatic clearance search (`find_clear_y`) puts type on calm light ground; Hugo's marked boxes (`MANUAL_PLACEMENT`, x0/y0/x1/y1 in image pixels) override it and win. Sets are no longer required to be uniformly aligned. (S031)
- [D-018] 2026-08-17 | Sportif | The @sportifcollection handle comes OFF on-platform Instagram assets (IG already prints the account name above every post and story). It stays available for anything travelling without the account name attached: stockist decks, Pinterest, print, press. (S031)
- [D-017] 2026-08-17 | Sportif | The MASTER brand mark is now SPORTIF / rule / collection, per Lucy's artwork, for EVERYTHING from here (not just collection-launch pieces). Proportions derived: rule = 0.43x wordmark width, then 'collection' sized so rule = 0.75x its width. Back catalogue still on the old wordmark+rule and needs a pass. (S031)
- [D-016] 2026-08-11 | Sportif | The sub-brand line is "SPORTIF collection" (the word is collection, not collective). "Le Sport Collectif" stays retired. (S030)
- [D-015] 2026-08-11 | Ochoproductions | In a multi-tile grid banner, size sub-lines and rules off the CENTRE TILE width (sub = 0.55 tile width, rule = 0.75x sub), never off the tracked wordmark's cap height, or they run into the Instagram gutters. (S030)
- [D-014] 2026-07-28 | Sportif | Competitor reference photos are STYLE-ONLY; never edit them (swap product, reuse model) into Sportif assets (their copyright + model release). Real-model content = a real shoot, or AI models we generate/own. (S029)
- [D-013] 2026-07-28 | Sportif | To brand AI-generated bands, prefer the TWO-IMAGE gpt swap (pass the scene + our finished hero bands) so the real SPORTIF label drops in naturally; render high for crisp text, or PIL-patch small garbles. Beats a flat PIL label composite. (S029)
- [D-012] 2026-07-28 | Ochoproductions | Hard mattes (white-on-light, e.g. white ball/bra on a light wall) are cut in Photoshop by Hugo; automatic matting (rembg) is only for clean plain-background subjects. (S028)
- [D-011] 2026-07-28 | Sportif | Light-touch social branding = the real logo lockup (SPORTIF Glacial Regular tracking -0.059 + underline rule) top-right, @sportifcollection centred beneath, over a soft corner scrim. (S028)
- [D-010] 2026-07-28 | Ochoproductions | Canva MCP here only does search + generate + export; it cannot read/edit and cannot export Lucy's view-only shared designs. Workflow: Hugo downloads from Canva -> we process locally -> he re-uploads. (S028)
- [D-009] 2026-07-28 | Ochoproductions | Per-request folder convention: clients/<client>/email-NN-<topic>/ with downloads/ + created/ + README (+ email-to-<person>.md). Keeps each client request self-contained. (S028)
- [D-008] 2026-07-23 | Ochoproductions | Content runs on TWO avenues: our pipeline (studio, exact/flat) + Canva (workbench, editable/shareable), chained pipeline -> Canva -> client. (S025)
- [D-007] 2026-07-23 | Sportif | Ad type colour: warm charcoal #4A433C or cream; never navy on a warm background. (S025)
- [D-006] 2026-07-23 | Sportif | Fresh-generation prompt rules: name the actual garments; garment colour must CONTRAST skin; garment material = SMOOTH four-way-stretch (not ribbed). (S025)
- [D-005] 2026-07-22 | Sportif | Reference reskin = no-text AI plate + our own PIL type layer (we always own the type). (S024)
- [D-004] 2026-07-22 | Sportif | Real SPORTIF label onto AI-generated bands via the two-image gpt-image-2 stamp; low quality reads most natural. (S023)
- [D-003] 2026-07-22 | Sportif | Lifestyle+product BLEND is the strongest content format. (S023)
- [D-002] 2026-07-22 | Ochoproductions | Scratch/synth music is internal preview only, never publish (unlicensed). (S022)
- [D-001] 2026-07-21 | Sportif | Launch is on HOLD indefinitely pending trademark talks with Lucy's lawyer. (S021)
