# Tools and gotchas

Environment and tool learnings, moved out of `CLAUDE.md` in S041 so they stop costing
tokens on every turn. `scripts/startup.py` names this file; nobody prints it. Read the
section for the environment you are in when a tool misbehaves, and add new learnings
here, labelled with the environment they apply to.

Which environment am I in? Shell paths like `/sessions/<name>/mnt/hyperframes/` mean
Cowork. Paths like `/Users/hugobrizuela/...` mean Claude Code.

## Cowork (Claude desktop app, sandboxed Linux)

- **Read `CLAUDE.md` at session start (S031).** It is not loaded into the Cowork context automatically, so the conventions (voice rule, handoff protocol, close-out ritual) are invisible unless read explicitly. A client-facing email reached final draft full of em dashes because of this. `python3 scripts/startup.py` is the fix; run it first.
- **Background processes do not survive across tool calls.** The sandbox reaps them and each call caps at about 45s, so nohup-and-poll does not work. For Perplexity deep research use `scripts/pplx_async.py`: it submits async jobs that run server-side, persists request ids to a registry file on disk, and polls them in later short calls. Perplexity rate-limits async submissions (HTTP 429), so stagger submits (12 to 18s) and resubmit failures. Quick synchronous queries with sonar-pro can still use `python3 scripts/perplexity_search.py "..." --model sonar-pro`. (The nohup workflow only works on the Mac via Claude Code.)
- **Network egress:** scripts that call the internet need the sandbox Domain allowlist open (Settings, Capabilities, Network Egress). A change only applies to a freshly booted sandbox, so a NEW chat is required after changing it.
- **PDF generation:** weasyprint must be pip-installed per fresh sandbox (`pip install weasyprint --break-system-packages`). System sandbox fonts are limited to Lora (serif) and Poppins (geometric sans), BUT brand font files live in `brand/fonts/` and load by path in both environments (see Fonts below).
- **Images:** iterate at quality low in Cowork (45s cap), render finals in Claude Code.
- **File locations:** keep all deliverables in the mounted hyperframes folder (stable path). Treat the sandbox outputs dir as throwaway; it gets wiped when the sandbox reboots mid-session.
- **File deletion in the mount** requires the `allow_cowork_file_delete` tool first; plain `rm` fails with Operation not permitted. Overwriting in place (`cp -f`) works fine and avoids the whole problem when refreshing a staged folder.
- **Committing from Cowork leaves stale git locks on the Mac (S031).** Because the sandbox cannot unlink inside the mount, `git commit` succeeds but cannot clean up `.git/HEAD.lock`, `.git/index.lock` or its `tmp_obj_*` files. Commit and push still work, but `git gc` fails with "cannot lock ref 'HEAD' ... File exists" and wrongly implies another git process is running. Fix on the Mac: `rm -f .git/HEAD.lock .git/index.lock && git gc --prune=now`. `closeout.py` and `startup.py` both handle this now, but it is worth knowing why.
- **Showing PDFs to Hugo:** present_files does not reliably preview a PDF in chat. Render pages to PNG and show a combined montage instead.

## Claude Code (Hugo's Mac)

- **PDF builds (S039).** `/usr/bin/python3` cannot load Homebrew's pango, so weasyprint lives in `.venvs/pdf` on Homebrew Python 3.11 (gitignored). Rebuild with `.venvs/pdf/bin/python clients/sportif/build-launch-plan.py` (and `build-brand-value-plan.py`). If the venv is missing:

    ```
    brew install pango
    /opt/homebrew/bin/python3.11 -m venv .venvs/pdf && .venvs/pdf/bin/pip install weasyprint pymupdf
    ```

- **Never put `opacity` on SVG text in the PDF generators:** weasyprint clips the line (it ate "powered by" in the Launch Plan diagram).
- **Git push happens here.** Cowork cannot push reliably, so a Mac session pushes after close-out so GitHub and the Mac agree.
- **macOS screenshot and screen recording names** carry a narrow no-break space before am and pm. A pasted path fails on `cp`; match with a glob (`*12.02.43*`) or `Path.glob` instead (S040).
- **Two Pythons, two jobs (S047).** `.venvs/pdf/bin/python` has Pillow and numpy but NOT `requests`; system `python3` has `requests` and Pillow. Scripts that call the OpenAI API run on `python3`.
- **Getting an image off Instagram or a WordPress site that blocks curl (S047).** Instagram's page and `/embed/` hide the post image from curl, and magnateview.com answers curl with a Mod_Security 406. Open the page in the in-app browser and read `document.images` (`naturalWidth`, `currentSrc`) with the JavaScript tool, then curl that signed URL; it downloads fine. Article text the same way (`innerText` of the paragraphs).
- **Dropbox folder invites (S047).** An invite to edit a folder needs a Dropbox account on the invited address (free 2GB is enough for a phone shoot). Download from All files, row menu, Download: one zip, stored uncompressed. Never move or delete inside a shared folder; it happens in the owner's copy too.
- **iPhone video is HLG HDR (S047).** `color_transfer=arib-std-b67` in ffprobe; tone-map to SDR before an edit or the colours wash out.

## Both environments

- **Fonts.** Glacial Indifference (Sportif's real font, all three weights) is at `brand/fonts/glacial-indifference/`. Use it via @font-face (weasyprint) or ImageFont.truetype (Pillow) for wordmarks and overlays instead of the old Poppins stand-in. Both PDF generators load Glacial Indifference by path for body AND titles (switched S039; Lora is not on the Mac, and brand.md puts headlines in Glacial anyway). Glacial reads about 10 percent smaller than Poppins at the same size, so the reading sizes were scaled up to match.
- **Images:** the proven engine for our warm-neutral look is **gpt-image-2** (OpenAI API key in `.env`, or run the prompts in ChatGPT). Pixa is a different engine; if you use it, flag the mismatch to Hugo. gpt-image-2 prompt format is in `docs/platform-prompt-formats.md`.
- **Hugo is not on Gmail.** The Gmail connector is not his client mailbox. Lucy's emails arrive as pasted text, screenshots, or files dropped in the client folder, never via Gmail search (S040).
- **Images pasted into the chat cannot be saved to disk.** Ask for the file in the folder (S040).

## Sportif client files

- **Client PDF set:** exactly two Lucy-facing PDFs are current, `Sportif-Brand-Value-Plan.pdf` (strategy) and `Sportif-Launch-Plan.pdf` (operations), regenerated via `build-brand-value-plan.py` and `build-launch-plan.py` from the `-client.md` sources. Everything else lives in `clients/sportif/_archive/`. Do not resurrect archived PDFs.
- **Two-doc drift rule:** internal source docs (e.g. `brand-value-plan.md`) drive condensed client cuts (e.g. `brand-value-plan-client.md`). Any change to an internal doc must be reflected in its client cut and the PDF re-exported. Each client cut carries a "Source of truth" header; update its synced date when you sync.

- **Type rendering is NOT reproducible across toolchain versions (S042).** Re-running `build_email02_social_v3/v4.py` on Pillow 11.3.0 / FreeType 2.13.3 does not reproduce the 26 Aug renders: every frame drifts by roughly 2,000 pixels inside the lockup, 1,625 of them by only 1 to 3 levels. The cause is per-character tracking, the scripts advance `x += charwidth + track` so a sub-pixel `textlength` difference accumulates left to right, which is why the diff bounding box starts partway into the wordmark rather than at its left edge. Invisible on screen, but it means a rebuild cannot be used to refresh a delivered folder. Copy ONLY the files that are meant to change, and verify with a pixel diff against the delivered copies, never with a checksum.
- **`STORY_SAFE_TOP` and a client placement can be mutually exclusive (S042).** On `story-sidestretch` Lucy asked for the mark above her raised hand; her fingertips top out at y=306 and the safe line is y=260, and the story already uses the full height of the 1080x1350 source (upscaled 1.42x, cropped horizontally only) so there is no crop headroom to borrow. Hugo took the trade. If this comes up again, say so before building rather than silently picking one.

- **Canva on a FREE account: PDF Print is the only vector route out (S042).** SVG export and Transparent Background are Pro, and PNG is capped at the design's own canvas (400x200 for Lucy's email signature, useless for a 1080 asset). PDF Print is free, keeps live text live, and embeds a subset of the font, so the artwork comes out as real outlines at any size.
- **PyMuPDF `get_svg_image(text_as_path=True)` does NOT emit flat paths (S042).** It writes each glyph once into `<defs>` and instances it with `<use xlink:href>`. Illustrator imports that as symbol instances, and a font it cannot find is flagged as missing. Resolve the `<use>` elements into real `<path>` elements yourself, carrying each use's transform. `scripts-local/extract_lucy_signature.py` does it.
- **`get_pixmap(alpha=True)` gives you an OPAQUE png when the PDF has background rects (S042).** Canva pages carry two full-page white rects, so every pixel comes back solid. For single-ink artwork over white, invert the composite instead: measure the ink colour C from the core, then `alpha = (255-P)/(255-C)`. Exact, and the anti-aliased edges stay honest.
- **A PDF page cropped with `show_pdf_page` still carries the source page's resources (S042).** The clip is visual only: fonts, images and drawings from outside the crop travel with it. To get a genuinely clean artboard, build it from the flattened SVG and convert that, then check with `page.get_fonts()`.
- **After Effects "Lossless with Alpha" renders PREMULTIPLIED over black (S042),** whatever you set Color to. Detect it by measuring edge pixels: straight alpha holds RGB near the ink colour at every alpha level, premultiplied scales RGB proportionally with alpha. It only matters when the artwork is LIGHT against a dark matte; for near-black ink the worst-case error is about 3 levels out of 255, so do not re-render for it. Separately, **do not use that template at all: it picks QuickTime Animation (`qtrle`), which modern QuickTime Player will not open.** Render alpha as Format QuickTime, Codec Apple ProRes 4444, Channels RGB + Alpha instead: it plays natively, is hardware accelerated on Apple silicon, and came out 9.5MB against qtrle's 15MB on the same 4 second 1080x1920 clip. An existing qtrle file transcodes losslessly with `ffmpeg -i in.mov -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le out.mov`.

- **A flat background behind a finished alpha render is an ffmpeg job, not an After Effects re-export (S043).** The ProRes 4444 alpha files carry the whole write-on (timing and shape) in their pixels, so any background colour is one command from inside `clients/sportif/generated/videos/`:

  ```
  ffmpeg -f lavfi -i "color=c=0x6C4333:s=1080x1920:r=30" -i lucy-signature-writeon-white-alpha.mov -filter_complex "[0:v][1:v]overlay=shortest=1:format=auto,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p" -c:v libx264 -profile:v main -crf 18 -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 -movflags +faststart -an lucy-signature-writeon-terracotta.mp4
  ```

  Change the hex after `color=c=0x` for the background; use the black alpha file on light backgrounds, the white one on dark. Output matches the AE-exported peach flat in every setting (H.264 Main, yuv420p, 30fps, BT.709 tags). TWO GOTCHAS INSIDE IT. (1) Without `scale=out_color_matrix=bt709:out_range=tv` ffmpeg converts RGB to YUV with the BT.601 matrix while tagging the file BT.709, and the background decodes about five levels off (measured 103,65,46 against a 108,67,51 target; with the fix 105,67,51, the same drift the AE export has). (2) Ink colour is baked into the alpha render's RGB, alpha only carries shape, so a new ink colour still needs After Effects. Verify by compositing the source frame over the colour in Python and diffing against the decoded MP4 frame, not by eye: solid ink within 4 levels and a frame mean near 1 level is a pass; edge pixels differ more because of 4:2:0 chroma, on both files alike.

## Token spend inside a session (both environments, S041)

The token diet trimmed what loads every turn. What dominates a session is tool output,
so these four habits save more than the diet did:

- **Bound every read.** `cut -c1-N` and `head` on command output, line ranges on file reads. A full read of a long script or registry costs more than the whole CLAUDE.md saving on a turn.
- **One montage, not six images.** An image read is the most expensive single call there is. Tile the candidates into one contact sheet and read that once.
- **Read a file once.** Edit and Write report their own success; do not re-read a file to check an edit landed. Re-read only when something else may have changed it.
- **Close out once.** Each close-out re-runs every check and prints them. Batch the changes and close out at the end, unless a commit is needed mid-session for the other environment to see it.
