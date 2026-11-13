#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEPS="${ROOT}/.deps"
TARGET="${DEPS}/astro"

command -v git >/dev/null 2>&1 || { echo "Git is required." >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "Python 3 is required." >&2; exit 1; }

PY_VERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3,10) else 1)' || {
  echo "Python 3.10+ is required; found ${PY_VERSION}." >&2
  exit 1
}

mkdir -p "${DEPS}"
if [[ -d "${TARGET}/.git" ]]; then
  echo "Updating upstream Astro checkout..."
  git -C "${TARGET}" pull --ff-only
elif [[ -e "${TARGET}" ]]; then
  echo "Refusing to overwrite existing non-git path: ${TARGET}" >&2
  exit 1
else
  echo "Cloning upstream Astro engine..."
  git clone --depth 1 https://github.com/aryaminus/astro.git "${TARGET}"
fi

ENGINE="${TARGET}/skills/astrology/scripts/astro_engine.py"
if [[ ! -f "${ENGINE}" ]]; then
  echo "Expected engine script not found: ${ENGINE}" >&2
  exit 1
fi

echo "Astro engine installed at: ${ENGINE}"
echo "No third-party source was copied into this repository."
