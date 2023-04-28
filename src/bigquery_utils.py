import os
from google.cloud import bigquery

# Set up Google BigQuery client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
client = bigquery.Client()

def execute_bigquery(sql_query):
    try:
        query_job = client.query(sql_query)
        results = query_job.result()
        return results, None
    except Exception as e:
        error_message = f'Error executing query: {e}'
        print(error_message)
        return None, error_message
