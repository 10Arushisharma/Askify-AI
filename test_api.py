from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

response = client.chat.completions.create(
    model="meta-llama/llama-3-8b-instruct",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.choices[0].message.content)