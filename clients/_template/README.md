# Client Template

Copy this entire folder when onboarding a new client:

```bash
cd ~/Desktop/hyperframes
cp -R clients/_template clients/<client-kebab-slug>
```

Then walk through these steps in order.

## Onboarding sequence

1. **Send the questionnaire.** Open `intake/questionnaire.md`, paste the body (everything below the first `---`) into an email, customize the greeting and signoff to your voice, and send to the client.
2. **While they're answering, do the SWOT.** Open `intake/swot-analysis.md` and fill it in. Use the research-helper prompt at the bottom of that file to have Claude surface category data, then bring your own judgment to the synthesis.
3. **When the questionnaire comes back, populate `brand.md`** from their answers + your SWOT conclusions. This is the brand kit + identity in one file. Split it into two only if/when it gets unwieldy.
4. **Set up products.** For each product/SKU the client is launching, copy `products/_template-product.md` to `products/<product-slug>.md` and fill it in.
5. **When you're ready to plan a campaign,** create `campaigns/<campaign-slug>.md` from the campaign-brief schema in `docs/pipeline-architecture.md` Stage 0.
6. **Run Stage 2 competitor analyses** and save outputs to `competitor-analyses/`.

## What NOT to do

- Don't put client work directly in `_template/`. That's the reusable starter. Always copy first.
- Don't skip the questionnaire/SWOT. `brand.md` is much harder to fill from a blank page.
- Don't track client binary assets in git. `assets/` is gitignored except `.md` files.

## When this template doesn't fit

This template is intentionally simple. If a client engagement needs more (e.g., multiple campaigns running in parallel, multiple brands under one umbrella), grow the structure as needed and update this README to document the new pattern.
