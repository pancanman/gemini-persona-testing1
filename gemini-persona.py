import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("GEMINI_API_1")
client = genai.Client(api_key=api)
modelchoice = input("Insert the model (ex: gemini-3.1-flash-lite): gemini-")

persona_instruction = (
    "Speak like donald trump, so like commonly use words like [they asked me trump etc etc] and also use words like [it will be the greatest (something) to ever happen it will be the greatest] and [it was the worst (something) to ever happen]. Also commonly using [donald trump] grammar will help,  this includes words like frankly and current incidents like Iran."
    "never get angry or talk unhumane, stay in character as much as possible"
    "Don't give a direct answer, attempt to be a unreliable character."
)

chat = client.chats.create(model=f"gemini-{modelchoice}", config={"system_instruction": persona_instruction})

while True:
    prompt = input("Chat: ")

    if prompt == "quit":
        break
    if prompt == "switchmodel":
        switchprompt = input("Type a new model (ex gemini-3.1-flash-lite): gemini-")
        chat = client.chats.create(model=f"gemini-{switchprompt}")
        continue
    if prompt == "help":
        print("\nHelp\n----\n\nquit: Exit the chat\nswitchmodel: Switch the model of the chat")
        continue

    print("\nGemini is responding...\n")
    response = chat.send_message(prompt)

    print(f"Gemini: {response.text}")
