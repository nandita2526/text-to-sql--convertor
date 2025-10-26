import google.generativeai as genai

# Configure your API Key
genai.configure(api_key="AIzaSyB3HAIz-gBUCdtQNfYzQmF9kvhy4r4rLjo")

# Input: user's question and database schema
user_query = input("Ask your database question: ")

schema = """
Tables:
1. students(id, name, age, department)
2. marks(student_id, subject, marks)
"""

# Generate SQL using Gemini
prompt = f"""
You are an expert SQL generator. Convert the following natural language question into a syntactically correct SQL query.

Schema:
{schema}

Question: {user_query}

Return only the SQL query. No explanation.
"""

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content(prompt)

print("\nGenerated SQL Query:\n")
print(response.text)
