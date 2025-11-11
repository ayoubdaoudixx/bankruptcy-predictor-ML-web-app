#!/usr/bin/env bash
set -euo pipefail

echo "Upgrading pip, setuptools and wheel..."
python -m pip install --upgrade pip setuptools wheel

echo "Installing only minimal runtime dependencies for Vercel..."
# Install minimal runtime deps into ./python so Vercel includes them in the serverless function
python -m pip install --no-cache-dir --upgrade -r vercel-requirements.txt --target ./python

# Ensure artifacts folder exists (if your app needs it)
mkdir -p artifacts

# Make this script executable (safe to run idempotently)
chmod +x vercel-build.sh

echo "Build script finished."