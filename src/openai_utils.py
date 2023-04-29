import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_completion(data, query) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an Ethereum blockchain expert. You will be given stuctured data, and must condense the information succintly. You do not need to output all the data, just a brief overview of the content, and a simple summary."},
            {'role': 'user', 'content': f"I want to know {query}. Here are the results: {data}. Explain the results to me"}
        ],
        temperature=0.3,
        max_tokens=512,
        n=1,
    )
    return response.choices[0].message.content.strip()

def generate_sql_query(query_string, previous_error=None):
    with open('src/prompt.txt', 'r') as file:
        prompt_template = file.read()

    user_message = f'''Query: {query_string}\nSQL Query:'''
    if previous_error:
        user_message = f"Previous error: {previous_error}\nPlease provide a corrected SQL query for the following question:\n{query_string}"

    # Use OpenAI API to parse the natural language query
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt_template},
            {'role': 'user', 'content': user_message}
        ],
        temperature=0.3,
        max_tokens=512,
        n=1,
    )

    sql_query = response.choices[0].message.content.strip()
    print("SQL query:", sql_query)
    return sql_query, None

    return None, error_message