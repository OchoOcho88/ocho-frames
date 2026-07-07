# Workspace fonts

Font files (.otf or .ttf) live here so BOTH environments (Claude Code and the Cowork sandbox) can load them directly by file path. Fonts installed on the Mac via Font Book are invisible to the Cowork sandbox; a file in this folder is not.

## Wanted

- **Glacial Indifference** (Regular and Bold): Sportif's brand font. Free, open licence (OFL), from fontsquirrel.com. Until it lands here, sandbox PDFs substitute letter-spaced Poppins.

## Usage

- weasyprint / HTML: `@font-face { font-family: 'Glacial Indifference'; src: url('brand/fonts/GlacialIndifference-Regular.otf'); }`
- Pillow text overlays: `ImageFont.truetype('brand/fonts/GlacialIndifference-Bold.otf', size)`

Per-client fonts also go here (one folder per client if it gets crowded).
