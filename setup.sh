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
echo "  Done! Total reference material: ~940MB"
echo "================================================"
echo ""
echo "Next steps:"
echo "  1. cp .env.example .env   # then fill in your API keys"
echo "  2. cd my-projects/starter && npm install"
echo "  3. npm run dev            # preview the starter project"
echo ""
