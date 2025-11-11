#!/bin/bash

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r vercel-requirements.txt --target ./python

# Make sure the artifacts directory exists
mkdir -p artifacts

# Make the script executable
chmod +x vercel-build.sh
