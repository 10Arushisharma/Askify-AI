from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your api key here",
)

response = client.chat.completions.create(
    model="meta-llama/llama-3-8b-instruct",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.choices[0].message.content)