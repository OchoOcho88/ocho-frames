# Clients

One folder per client. Each client folder is the source of truth for their brand, products, and creative work.

## Convention

- **Naming:** lowercase-kebab-case (e.g., `sportif/`, `jane-doe-coaching/`)
- **Onboarding a new client:** copy `_template/` to `<client-slug>/`
- **Archiving a wrapped campaign:** move the campaign-specific files into `<client>/_archive/<YYYY-MM-campaign-slug>/`

## What lives where

- `_template/`. The starter every new client copies. Do not put client work in here.
- `<client>/`. Actual client folder, populated from `_template/` + intake responses.

## Folder map (inside each client)

```
brand.md                  ← timeless brand context (kit + identity, combined)
intake/                   ← onboarding materials: questionnaire + SWOT
products/                 ← one .md file per product/SKU
campaigns/                ← active campaign briefs
competitor-analyses/      ← Stage 2 outputs for THIS client
_archive/                 ← wrapped campaigns moved here
assets/                   ← logos, fonts, sample imagery (gitignored)
```

See `docs/pipeline-architecture.md` for how this folder fits into the full creative-strategy pipeline.

## Related folders

- `compositions/`. HyperFrames code projects (HTML/CSS/JS rendered to MP4). Not client strategy.
- `brand/`. Your *agency's* own brand kit, not a client's.
