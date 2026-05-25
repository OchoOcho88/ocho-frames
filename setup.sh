#!/usr/bin/env bash
# ============================================================
# setup.sh — restore the reference repos that aren't in git
# ============================================================
# Why this exists:
#   main-source/hyperframes, examples/launch-video, and
#   examples/student-kit are reference clones (~940MB total)
#   that are excluded from this repo via .gitignore. This script
#   pulls them down on demand.
#
# Run from the workspace root:
#   ./setup.sh
# ============================================================

set -e  # exit on any error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "================================================"
echo "  Restoring reference repos for ocho-frames"
echo "================================================"
echo ""

# 1. Main HyperFrames source (skip LFS to save ~240MB)
if [ ! -d "main-source/hyperframes/.git" ]; then
  echo "→ Cloning heygen-com/hyperframes (without LFS)..."
  rm -rf main-source/hyperframes
  GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 \
    https://github.com/heygen-com/hyperframes.git \
    main-source/hyperframes
  echo "  ✓ main-source/hyperframes (~122MB)"
else
  echo "✓ main-source/hyperframes already exists, skipping"
fi
echo ""

# 2. Launch video example
if [ ! -d "examples/launch-video/.git" ]; then
  echo "→ Cloning heygen-com/hyperframes-launch-video..."
  rm -rf examples/launch-video
  git clone --depth 1 \
    https://github.com/heygen-com/hyperframes-launch-video.git \
    examples/launch-video
  echo "  ✓ examples/launch-video (~256MB)"
else
  echo "✓ examples/launch-video already exists, skipping"
fi
echo ""

# 3. Student kit (12 GSAP teaching projects)
if [ ! -d "examples/student-kit/.git" ]; then
  echo "→ Cloning nateherkai/hyperframes-student-kit..."
  rm -rf examples/student-kit
  git clone --depth 1 \
    https://github.com/nateherkai/hyperframes-student-kit.git \
    examples/student-kit
  echo "  ✓ examples/student-kit (~560MB)"
else
  echo "✓ examples/student-kit already exists, skipping"
fi
echo ""

echo "================================================"
echo "  Reference repos restored (~940MB)"
echo "================================================"
echo ""

# 4. Install the video-analyzer Claude Code skill (lives outside this workspace
#    at ~/.claude/skills/video-analyzer/ because the skill hardcodes that path)
if [ ! -d "$HOME/.claude/skills/video-analyzer" ]; then
  echo "→ Installing video-analyzer skill into ~/.claude/skills/..."
  mkdir -p "$HOME/.claude/skills"
  git clone --depth 1 https://github.com/mikefutia/claude-vision.git "$HOME/.claude/skills/video-analyzer"
  echo "  ✓ video-analyzer skill installed"
else
  echo "✓ video-analyzer skill already installed at ~/.claude/skills/video-analyzer"
fi
echo ""

# 5. Install Python dependency for video-analyzer
echo "→ Installing google-genai Python SDK (Gemini)..."
pip3 install google-genai 2>/dev/null || pip3 install google-genai --break-system-packages 2>/dev/null || echo "  ⚠ pip3 install failed — install manually with: pip3 install google-genai"
echo ""

echo "================================================"
echo "  All automated setup complete!"
echo "================================================"
echo ""
echo "Manual next steps:"
echo "  1. Get a Gemini API key (free): https://aistudio.google.com/apikey"
echo "     Tip: create a project named 'Hyperframes' to track usage separately."
echo ""
echo "  2. Set the key as a shell env var (paste the key when prompted):"
echo "     printf \"Paste Gemini key: \" && read -s K && echo && printf 'export GEMINI_API_KEY=\"%s\"\\n' \"\$K\" >> ~/.zshrc && source ~/.zshrc && unset K"
echo ""
echo "  3. Copy and fill in your other API keys:"
echo "     cp .env.example .env"
echo ""
echo "  4. Install the starter project's deps:"
echo "     cd my-projects/starter && npm install && npm run dev"
echo ""
echo "  See skills/video-analyzer/README.md for full details."
echo ""
