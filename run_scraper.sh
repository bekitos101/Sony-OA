#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment (Windows-friendly)
echo "Activating virtual environment..."
source venv/Scripts/activate

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Install Playwright browsers
echo "Installing Playwright browsers..."
playwright install

# Run the scraper
echo "Running the scraper..."
python scraper.py

# No need to deactivate manually — subshell ends here
echo "✅ Done!"
