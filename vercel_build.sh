#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r data-analyst-roadmap/requirements_docs.txt

echo "Building the book..."
jupyter-book build data-analyst-roadmap
