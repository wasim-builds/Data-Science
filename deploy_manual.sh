#!/bin/bash

# Configuration
BOOK_DIR="data-analyst-roadmap"
BUILD_DIR="$BOOK_DIR/_build/html"

echo "Building the Data Analyst Roadmap..."

# Build the book
jupyter-book build $BOOK_DIR

if [ $? -eq 0 ]; then
    echo "Build successful! Deploying to GitHub Pages..."
    
    # Check if ghp-import is installed
    if ! command -v ghp-import &> /dev/null; then
        echo "ghp-import not found. Installing..."
        pip install ghp-import
    fi
    
    # Deploy using ghp-import
    ghp-import -n -p -f $BUILD_DIR
    
    echo "Deployment complete! Visit your GitHub Pages URL."
else
    echo "Build failed. Please check the errors above."
    exit 1
fi
