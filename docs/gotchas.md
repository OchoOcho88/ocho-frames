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

## Both environments

- **Fonts.** Glacial Indifference (Sportif's real font, all three weights) is at `brand/fonts/glacial-indifference/`. Use it via @font-face (weasyprint) or ImageFont.truetype (Pillow) for wordmarks and overlays instead of the old Poppins stand-in. Both PDF generators load Glacial Indifference by path for body AND titles (switched S039; Lora is not on the Mac, and brand.md puts headlines in Glacial anyway). Glacial reads about 10 percent smaller than Poppins at the same size, so the reading sizes were scaled up to match.
- **Images:** the proven engine for our warm-neutral look is **gpt-image-2** (OpenAI API key in `.env`, or run the prompts in ChatGPT). Pixa is a different engine; if you use it, flag the mismatch to Hugo. gpt-image-2 prompt format is in `docs/platform-prompt-formats.md`.
- **Hugo is not on Gmail.** The Gmail connector is not his client mailbox. Lucy's emails arrive as pasted text, screenshots, or files dropped in the client folder, never via Gmail search (S040).
- **Images pasted into the chat cannot be saved to disk.** Ask for the file in the folder (S040).

## Sportif client files

- **Client PDF set:** exactly two Lucy-facing PDFs are current, `Sportif-Brand-Value-Plan.pdf` (strategy) and `Sportif-Launch-Plan.pdf` (operations), regenerated via `build-brand-value-plan.py` and `build-launch-plan.py` from the `-client.md` sources. Everything else lives in `clients/sportif/_archive/`. Do not resurrect archived PDFs.
- **Two-doc drift rule:** internal source docs (e.g. `brand-value-plan.md`) drive condensed client cuts (e.g. `brand-value-plan-client.md`). Any change to an internal doc must be reflected in its client cut and the PDF re-exported. Each client cut carries a "Source of truth" header; update its synced date when you sync.

## Token spend inside a session (both environments, S041)

The token diet trimmed what loads every turn. What dominates a session is tool output,
so these four habits save more than the diet did:

- **Bound every read.** `cut -c1-N` and `head` on command output, line ranges on file reads. A full read of a long script or registry costs more than the whole CLAUDE.md saving on a turn.
- **One montage, not six images.** An image read is the most expensive single call there is. Tile the candidates into one contact sheet and read that once.
- **Read a file once.** Edit and Write report their own success; do not re-read a file to check an edit landed. Re-read only when something else may have changed it.
- **Close out once.** Each close-out re-runs every check and prints them. Batch the changes and close out at the end, unless a commit is needed mid-session for the other environment to see it.
