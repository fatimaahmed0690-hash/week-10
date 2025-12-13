import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return None, "OPENAI_API_KEY not found. Check your .env file."

    if "your_key" in api_key.lower():
        return None, "Invalid API key detected (placeholder key)."

    try:
        client = OpenAI(api_key=api_key)
        return client, None
    except Exception as e:
        return None, str(e)


def ask_ai(question: str):
    client, error = get_openai_client()

    if error:
        return f"AI Error: {error}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful cybersecurity assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {e}"
