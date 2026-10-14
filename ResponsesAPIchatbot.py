from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("grok_apikey"),
    base_url="https://api.groq.com/openai/v1"
)

id = None
while True:
    input_text =input("Enter your prompt (or 'exit' to quit): ")
    if input_text.lower() =="exit":
        break

    response = client.responses.create (
    model="openai/gpt-oss-20b",
    input=input_text,
    previous_response_id = id

)
    print(response.output_text)

    id = response.id  