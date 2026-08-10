import os
from dotenv import load_dotenv
from google import genai

# Load the API key from .env
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Jarvis is online. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_input
    )

    reply = response.text
    print(f"Jarvis: {reply}\n")