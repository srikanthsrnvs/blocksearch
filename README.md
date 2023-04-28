# blocksearch
An Ethereum search engine

## Setup
To run blocksearch, you need to create a `.env` file in the project directory. The `.env` file should contain the following environment variables:
```
OPENAI_API_KEY=<your_openai_api_key>
GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_google_application_credentials_json_file>
```

Replace `<your_openai_api_key>` with your actual OpenAI API key and `<path_to_your_google_application_credentials_json_file>` with the path to your Google Application Credentials JSON file.

## Running the Application
After setting up the `.env` file, you need to make the `run.sh` script executable. You can do this by running the following command:
`chmod +x run.sh`

Once the script is executable, you can run the application using the following command:
`./run.sh`

## Making Requests
After the application is running, you can make a curl request to the localhost to interact with the search engine. Here's an example of how to make a request:
`curl "http://127.0.0.1:5000?query=Show%20me%20the%20last%2020%20transfers%20made%20with%20token%3A%200xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"`

This request asks the search engine to show the last 20 transfers made with a specific token.