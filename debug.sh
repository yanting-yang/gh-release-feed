#!/bin/bash
# Debug script to mimic the GitHub Actions workflow locally

set -e  # Exit on error

echo "================================================"
echo "Debug script for RSS feed generation"
echo "================================================"
echo ""

# Check if required dependencies are installed
echo "Checking dependencies..."
if ! python3 -c "import markdown, requests" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install markdown requests
fi

echo ""
echo "================================================"
echo "Generating RSS feeds..."
echo "================================================"
python3 run.py

echo ""
echo "================================================"
echo "Checking for changes..."
echo "================================================"

# Show what changed
if git diff --quiet output/; then
    echo "No changes detected in output/"
else
    echo "Changes detected:"
    git diff --stat output/
    echo ""
    echo "To commit and push these changes, run:"
    echo "  git add output/"
    echo "  git commit -m 'Update RSS feeds [$(date -u +%Y-%m-%d)]'"
    echo "  git push"
fi

echo ""
echo "================================================"
echo "Done!"
echo "================================================"
