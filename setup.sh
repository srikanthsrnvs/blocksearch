#!/bin/bash

# Load environment variables from the .env file
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export $(grep -v '^#' .env | xargs)

# Install requirements
pip3 install -r requirements.txt

cd frontend && npm install && cd ..