#!/bin/bash
set -e

echo "Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r data-analyst-roadmap/requirements_docs.txt

echo "Building the book..."
jupyter-book build data-analyst-roadmap
