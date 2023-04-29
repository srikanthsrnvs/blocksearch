#!/bin/bash

# Load environment variables from the .env file
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export $(grep -v '^#' .env | xargs)

# Install requirements
pip3 install -r requirements.txt

# Run the app.py script (server) in a new terminal window
osascript -e "tell app \"Terminal\" to do script \"python3 '${BASE_DIR}/src/app.py'\""

# Navigate to the client directory and start the client in a new terminal window
osascript -e "tell app \"Terminal\" to do script \"cd '${BASE_DIR}/frontend' && npm start\""