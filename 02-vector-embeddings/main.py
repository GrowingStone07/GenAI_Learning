from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

text = "I am chasing cat"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input = text
)

print(response)
print(len(response.data[0].embedding))

