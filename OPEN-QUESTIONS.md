# Open questions / open loops

The things still needing an answer or an action, extractable (not buried in prose).
Query with `python3 scripts/memory_tools.py open [--client Sportif] [--stale 5]`.
Aging is measured from the `opened Sxxx` tag vs the latest session number.

**Open row:**     `- [ ] [Q-NNN] YYYY-MM-DD | Client | question/action (opened Sxxx)`
**Resolved row:** `- [x] [Q-NNN] YYYY-MM-DD | Client | ... RESOLVED Sxxx: outcome`
(Keep resolved rows for the record; flip `[ ]` to `[x]` and append the outcome.)

- [ ] [Q-017] 2026-08-20 | Ochoproductions | GEMINI_API_KEY is now in `.env` (Hugo copied it from his Mac shell, S032). Before Nano Banana Pro can be called from Cowork, open Settings, Capabilities, Network Egress and allow `generativelanguage.googleapis.com`, then START A NEW CHAT (egress changes only apply to a freshly booted sandbox). Then build the gen script alongside the gpt-image-2 ones. (opened S032)
- [ ] [Q-016] 2026-08-20 | Sportif | Decide the 3D route for the band and produce a Shopify-ready GLB (about 4MB total, textures optimised JPG at or under 2048x2048, diffuse + normal + combined occlusion/roughness/metalness, real-world scale, origin at the product base). Tripo AI is the AI pick (multi-image, PBR, GLB export); a hand-built Blender loop textured from Hugo's photos is the accuracy option. (opened S032)
- [ ] [Q-015] 2026-08-20 | Sportif | RESHOOT all three bands. Shoot 2 (2026-08-20) covered every face of all three weights in one sitting, but on a BLUE card: the heavy came back at hue 258 deg / 22% sat against a true 17 deg / 50%, and a white balance correction only recovers to 28% sat, so the colour is gone from the file. No neutral was in frame to correct against. Shoot 2 is still fine for shape, texture, labels and AI reference. Reshoot on WHITE with a sheet of white paper in one frame. Blocks the colourway strips (ref 06), the range card and the wholesale line sheet. Files renamed and filed in `assets/Sportif_Bands/Originals/`. (opened S032)
- [ ] [Q-014] 2026-08-17 | Sportif | Hugo to send his Photoshop version of the "wordmark burned into the wall" pilates treatment (ideally with the layers panel: blend mode, opacity, whether the type is split around her) so the exact recipe can be reproduced rather than approximated. (opened S031)
- [ ] [Q-013] 2026-08-17 | Sportif | Back-catalogue pass to the new SPORTIF / rule / collection master mark: posters, product shots, the three finished IG ads, the band-swap set, and both Lucy-facing PDFs are all still on the old wordmark+rule. (opened S031)
- [ ] [Q-012] 2026-08-17 | Sportif | SEND the email-02 v2 batch to Lucy (draft + 12 staged attachments ready in TO-SEND-2026-08-17/, not yet sent; optionally box the five still on automatic placement first). Then her pick of black / white / black-with-white-edge to lock as the house standard. (opened S031)
- [ ] [Q-011] 2026-08-11 | Sportif | Collection grid tiles sent to Lucy: awaiting her sign-off, and whether she wants a cream or white colourway as well as the peach. (opened S030)
- [ ] [Q-010] 2026-07-28 | Sportif | Email 03: run the high-quality band-swap + branded-flatlay renders in Terminal (band_swap_test.py high, add_stitched_branding.py high) for crisp text, PIL-patch any stragglers, then finalise the attach set and send Lucy the email. (opened S029)
- [x] [Q-009] 2026-07-28 | Sportif | Email 03 from Lucy: same flow (ask questions, folder, build). RESOLVED S029: built email-03-band-photo set (hero, draped, flat-lay, in-use) + the band-swap labelling method; email to Lucy drafted. (opened S028)
- [ ] [Q-008] 2026-07-28 | Sportif | Layered poster (poster-lucy-layered): awaiting Hugo's Photoshop cutout of the ball-overhead hero, saved as hero-ball-cut.png, to finalise (ball+bra too low-contrast to auto-matte). (opened S028)
- [x] [Q-007] 2026-07-28 | Sportif | Email 02 socials sent to Lucy: awaiting her reply on the light-touch treatment. RESOLVED S031: she approved ("These look great!") with three notes (feed-duo logo LEFT + BLACK, the beam covers the logo on the rest, Canva notes to follow on the story pilates pic); full batch rebuilt as v2. (opened S028)
- [ ] [Q-006] 2026-07-24 | Sportif | Lucy expert-brand strategy (Devin Jatho 4-quadrant model, authority-first): Phase 1 profile done + sent to Lucy for feedback; Phase 2 (expert niche, one avatar, 4 quadrants) pending her reaction. (opened S026)
- [ ] [Q-005] 2026-07-23 | Sportif | Get Canva Pro (~2026-07-30), then set up the Sportif brand kit and share the Sportif folder with Lucy. (opened S025)
- [ ] [Q-004] 2026-07-22 | Sportif | Lucy to pick music-bed pacing (calm ~100 BPM vs upbeat ~118 BPM). (opened S023)
- [ ] [Q-003] 2026-07-21 | Sportif | Incentive decision A/B/C (monthly group session / capped 1:1 / video series) — Lucy to get back. (opened S021)
- [ ] [Q-002] 2026-07-18 | Sportif | Trademark clearance with Lucy's lawyer — the critical-path gate for launch, Shopify, go-to-market. (opened S021)
- [ ] [Q-001] 2026-07-11 | Sportif | Build the standalone waitlist capture page — top unbuilt item, needs neither Lucy nor trademark. (opened S017)
