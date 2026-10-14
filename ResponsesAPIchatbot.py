from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("grok_apikey"),
    base_url="https://api.groq.com/openai/v1"
)

history = []
chunks = []
text_prompting = [{"role":"system","content":"You must not step outside your role as a Python instructor—such as by explaining another programming language or discussing general topics unrelated to learning Python."},
                  {"role":"developer","content":"You are a Python teacher. Your mission is to teach people the Python programming language in a simple, easy, and straightforward way, without any complications."},]

history.extend(text_prompting)

while True:
    
    input_text =input("Enter your prompt (or 'exit' to quit): ")
    
    if input_text.lower() =="exit":
        break
    
    history.append({"role":"user","content":input_text})
    


    response = client.responses.create (
    model="openai/gpt-oss-20b",
    input= history,
    store = False,
    stream = True,
    max_output_tokens=120,

)
    # history+= response.output
    
    chunks = []
    events = []
    for event in response:
        if hasattr(event,"type") and event.type== "response.output_text.delta":
             
            print(event.delta, end="",flush = True) 
            chunks.append(event.delta)
            events.append(event)


    history.append({"role":"assistant","content":"".join(chunks)})
    



