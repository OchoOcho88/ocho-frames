# Decisions log

Settled decisions, extractable (not buried in the session prose). One per line, newest at top.
Query with `python3 scripts/memory_tools.py decisions [--client Sportif]`.

**Row format:** `- [D-NNN] YYYY-MM-DD | Client | decision text (Sxxx)`
(Client = client name, or `Ochoproductions` for workspace-wide. Sxxx = session it was made.)

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
