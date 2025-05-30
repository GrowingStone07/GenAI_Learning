from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-4.1-mini",
    messages = [
        {"role":"user", "content":"Hi, My name is Asutosh"},
        {"role":"assistant", "content":"Hello Asutosh! How can I assist you today?"},
        {"role":"user", "content":"Whats my name?"},
        {"role":"assistant", "content":"Your name is Asutosh. How can I help you further?"},
        {"role":"user", "content":"How are you?"}
        
    ]
)


print(response.choices[0].message.content)