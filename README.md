# blocksearch
An Ethereum search engine

<img width="1460" alt="Screen Shot 2023-04-28 at 5 44 38 PM" src="https://user-images.githubusercontent.com/25404406/235273897-b4f8a155-b915-43b1-811b-bab4aba67054.png">

## Setup
To run blocksearch, you need to create a `.env` file in the project directory. The `.env` file should contain the following environment variables:
```
OPENAI_API_KEY=<your_openai_api_key>
GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_google_application_credentials_json_file>
```

Replace `<your_openai_api_key>` with your actual OpenAI API key and `<path_to_your_google_application_credentials_json_file>` with the path to your Google Application Credentials JSON file.

## Running the Application
After setting up the `.env` file, you need to make the `run.sh` script executable. You can do this by running the following command:
`chmod +x setup.sh`

Once the script is executable, you can run the application using the following command:
`./setup.sh`

## Making Requests
After the application is running, you can make a curl request to the localhost to interact with the search engine. Here's an example of how to make a request:
`curl "http://127.0.0.1:5000?query=Show%20me%20the%20last%2020%20transfers%20made%20with%20token%3A%200xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"`

This request asks the search engine to show the last 20 transfers made with a specific token.

### Running the repo
First you'll want to start the server using `python3 src/app.py` or `python src/app.py`.
Next, in another terminal, run `cd frontend && npm start`

This will run the server and client, you should be able to now type in your queries
