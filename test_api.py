from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="ssk-proj-J4dCs9Nt57uPedFacORGAcNmd14AowqoNoK8KaXu39fTU7_VSEtykcy9p_6h912AdfRne_hXkqT3BlbkFJZHY_nupyCX5D7n1G2jmoupQ29k7myf1Re3u_DKA2NdqZGsxaqJAf03iJypC589JaPEuQdaiBMA",
)

response = client.chat.completions.create(
    model="meta-llama/llama-3-8b-instruct",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.choices[0].message.content)