import time
from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = st.secrets["OPENROUTER_API_KEY"].strip().replace("\n", "").replace(" ", "")
except Exception:
    api_key = os.getenv("OPENROUTER_API_KEY","dummy_key_so_app_doesnt_crash").strip()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,

default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Askify-AI"
    }
)

def generate_answer(query, docs):
    context = "\n".join([doc.page_content for doc in docs])

    for _ in range(3):
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-3-8b-instruct",
                messages=[
                    {
                        "role": "system",
                        "content": "Answer ONLY from the given context."
                    },
                    {
                        "role": "user",
                        "content": f"Context:\n{context}\n\nQuestion:\n{query}"
                    }
                ],
                max_tokens=300,
            )

            return response.choices[0].message.content

        except Exception as e:
            print("Retrying...", e)
            time.sleep(2)

    return "⚠️ API connection failed. Try again."
