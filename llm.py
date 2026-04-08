import time
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="ssk-proj-J4dCs9Nt57uPedFacORGAcNmd14AowqoNoK8KaXu39fTU7_VSEtykcy9p_6h912AdfRne_hXkqT3BlbkFJZHY_nupyCX5D7n1G2jmoupQ29k7myf1Re3u_DKA2NdqZGsxaqJAf03iJypC589JaPEuQdaiBMA",
    default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Askify-AI"
    }
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