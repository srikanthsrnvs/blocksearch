from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from openai_utils import generate_sql_query, generate_completion
from bigquery_utils import execute_bigquery
from utils import lowercase_ethereum_addresses

app = Flask(__name__)
CORS(app)

# Load environment variables from .env file
load_dotenv()

# Define the route for the main endpoint
@app.route('/search/eth', methods=['GET'])
@cross_origin()
def search():
    query_string = request.args.get('query', '')

    if not query_string:
        return jsonify({'error': 'Missing query parameter'}), 400

    query_string = lowercase_ethereum_addresses(query_string)

    max_attempts = 5
    attempt = 0
    error_message = None

    while attempt < max_attempts:
        attempt += 1

        # Generate SQL query using OpenAI API
        sql_query, error_message = generate_sql_query(query_string, error_message)

        if error_message:
            continue  # Retry the OpenAI call

        # Execute SQL query on BigQuery
        results, error_message = execute_bigquery(sql_query)

        if error_message:
            continue  # Retry the OpenAI call

        # Return the results as JSON
        data = [dict(row.items()) for row in results]
        completion = generate_completion(data, query_string)
        return jsonify({'data': data, 'completion': completion, 'sql': sql_query})

    return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(port=5000)