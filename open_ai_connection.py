import openai


client = openai.OpenAI(api_key = "private_api_key")

response = client.chat.completions.create(
    model= "gpt-4o",
    messages=[
        {
            "role":"user",
            "content":"Say me about cats"
        }
    ],
    temperature=0.6,
    max_tokens=150
)
print(response.choices[0].message.content)