#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate || . .venv/Scripts/activate
pip install --upgrade pip
pip install -e .
echo "Bootstrapped. Edit configs under configs/ and run make targets."
