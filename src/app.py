from flask import Flask, request, jsonify
from dotenv import load_dotenv
from openai_utils import generate_sql_query
from bigquery_utils import execute_bigquery
from utils import lowercase_ethereum_addresses

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Define the route for the main endpoint
@app.route('/', methods=['GET'])
def query_bigquery():
    query_string = request.args.get('query', '')

    if not query_string:
        return jsonify({'error': 'Missing query parameter'}), 400

    query_string = lowercase_ethereum_addresses(query_string)

    # Generate SQL query using OpenAI API
    sql_query, error_message = generate_sql_query(query_string)

    if error_message:
        return jsonify({'error': error_message}), 500

    # Execute SQL query on BigQuery
    results, error_message = execute_bigquery(sql_query)

    if error_message:
        return jsonify({'error': error_message}), 500

    # Return the results as JSON
    return jsonify([dict(row.items()) for row in results])

if __name__ == '__main__':
    app.run(debug=True)