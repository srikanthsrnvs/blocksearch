#!/bin/bash

# Load environment variables from the .env file
export $(grep -v '^#' .env | xargs)

# Install requirements
pip install -r requirements.txt

# Run the app.py script
python src/app.py