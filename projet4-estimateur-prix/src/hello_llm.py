from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="dit moi qui tu est et quesque tu peux faire, en français",
)

print(response.text)
print(response.usage_metadata)