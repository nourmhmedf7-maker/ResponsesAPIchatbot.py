from openai import OpenAI
import os 
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("grok_apikey"),
    base_url="https://api.groq.com/openai/v1"
)

def send_email(to,subject,body):
    print(f"Sending email to {to} with subject '{subject}' and body '{body}'")
    return f"Email sent to {to}"

tools = [
    {
        "type":"function",
        "name":"send_email",
        "description":"Send an email to a given recipient with a subject and message.",
        "parameters":{
            "type":"object",
            "properties":{
                "to":{"type":"string","description":"The recipient email address."},
                "subject":{"type":"string","description":"Email subject line."},
                "body":{"type":"string","description":"Body of the email message."},
            },
            "required":["to","subject","body"],
            "additionalProperties": False,

        }

    }
]



history = []
chunks = []
text_prompting = [{"role":"system","content":"Never fabricate information or claim that an email was sent unless the email tool confirms success. Never send an email if the recipient's email address is missing."},
                  {"role":"developer","content":"You are an AI email assistant. Your job is to write and send emails based on the user's instructions. When the user requests an email, determine the recipient, subject, and message body. Use the available send_email tool to send the email. If essential information is missing, ask the user for it."},]

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
    # stream = True,
    max_output_tokens=1000,
    tools = tools

)
    

    for item in response.output:

        if item.type == "reasoning":
            continue
        
        

        if item.type == "function_call":
          args = json.loads(item.arguments)    
          result = send_email(**args)        
          print(result)    
          history.append(item)  
          history.append({"type":item.type,"id":item.call_id,"output":result}) 

        else :
            history.append({"role":"assistant","content":response.output_text})
            print(response.output_text)
            
        

    #----------------------------------------------------------------------------------------------------



    
    print("output",response.output)
    
    print("history",history)
    #streaming
    # chunks = []
    # events = []
    # for event in response:
    #     if hasattr(event,"type") and event.type== "response.output_text.delta":
             
    #         print(event.delta, end="",flush = True) 
    #         chunks.append(event.delta)
    #         events.append(event)


    # history.append({"role":"assistant","content":"".join(chunks)})
    



