from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    contents="파이썬을 한 문장으로 설명해줘"
)
print(response.text)
