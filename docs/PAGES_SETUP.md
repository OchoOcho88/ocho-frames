# GitHub Pages Setup

This workspace ships with `index.html` at the root, ready to be served as a public landing page via GitHub Pages.

## Important first

**GitHub Pages is free only for PUBLIC repos.** The `ocho-frames` repo is currently **private**, so you have two options before Pages will render:

1. **Flip the repo to public** when you're ready for the landing page to be visible to anyone. (Recommended once you have something you're proud of.) The README and folder structure don't contain anything sensitive — secrets live in `.env`, which `.gitignore` excludes.
2. **Upgrade to GitHub Pro** ($4/mo) — Pro lets you publish Pages from private repos.

Both work. Most people pick option 1.

## How to enable Pages

Once you've decided on visibility:

1. Go to https://github.com/OchoOcho88/ocho-frames
2. Click **Settings** (top nav)
3. In the left sidebar, click **Pages**
4. Under **Build and deployment** → **Source**, pick **Deploy from a branch**
5. Under **Branch**, pick **main** and **/ (root)** as the folder
6. Click **Save**
7. Wait 1–3 minutes — GitHub builds the page
8. Refresh the Pages section. You'll see "Your site is live at https://ochoocho88.github.io/ocho-frames/"

## What you'll get

The `index.html` at the workspace root renders as the homepage. It includes:

- A short description of what the workspace is for
- A "What lives here" section explaining the folder structure
- A "Set up on a new machine" code block for anyone (or future you) who needs to clone
- Links back to the GitHub repo and HyperFrames docs

The styling uses the same colors/typography as `brand/agency-brand-kit.md` so the page is on-brand.

## Updating the page

Any time you edit `index.html` and push to `main`, the page rebuilds automatically. No deploy step.

## Custom domain (optional, later)

If you want a custom domain like `ocho-frames.com`:

1. Buy the domain (Namecheap, Cloudflare, Google Domains)
2. In GitHub Settings → Pages → Custom domain, enter the domain
3. In your domain registrar's DNS settings, add a CNAME record pointing to `ochoocho88.github.io`
4. Wait for DNS to propagate (usually <1 hour, can take 24)
5. Enable "Enforce HTTPS" in Pages settings

## If something breaks

- **Page shows 404** → either Pages isn't enabled yet, or the repo is still private with no Pro plan
- **Page is blank** → check that `index.html` is in the repo root (not in a subfolder), and that you picked "/ (root)" as the source folder
- **Old version showing** → GitHub caches aggressively. Hard refresh (Cmd+Shift+R) or wait 5 minutes for the CDN to update
