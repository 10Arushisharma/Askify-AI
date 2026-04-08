import time
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

def generate_answer(query, docs):
    context = "\n".join([doc.page_content for doc in docs])

    for _ in range(3):  # retry 3 times
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