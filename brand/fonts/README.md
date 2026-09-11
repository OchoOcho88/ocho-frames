# Workspace fonts

Font files (.otf or .ttf) live here so BOTH environments (Claude Code and the Cowork sandbox) can load them directly by file path. Fonts installed on the Mac via Font Book are invisible to the Cowork sandbox; a file in this folder is not.

## In here

- **Glacial Indifference** (Regular, Bold, Italic), Sportif's brand font, confirmed by Lucy (`clients/sportif/brand.md`). Free, SIL Open Font License (licence file alongside), from fontsquirrel.com. Files are in `glacial-indifference/`. Every Sportif build loads it from here: the grid and weave tiles, the master mark logos, and both client PDFs (switched off the Poppins stand-in in S039).

## Usage

- weasyprint / HTML: `@font-face { font-family: 'Glacial Indifference'; src: url('brand/fonts/glacial-indifference/GlacialIndifference-Regular.otf'); }`
- Pillow text overlays: `ImageFont.truetype('brand/fonts/glacial-indifference/GlacialIndifference-Bold.otf', size)`

Per-client fonts also go here (one folder per client if it gets crowded).
