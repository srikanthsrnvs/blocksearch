import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sql_query(query_string):
    with open('src/prompt.txt', 'r') as file:
        prompt_template = file.read()

    max_attempts = 5
    attempt = 0
    error_message = None

    while attempt < max_attempts:
        attempt += 1

        if attempt == 1:
            user_message = f'''Query: {query_string}\nSQL Query:'''
        else:
            user_message = f"Previous error: {error_message}\nPlease provide a corrected SQL query for the following question:\n{query_string}"

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