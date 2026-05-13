from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai",
    api_key=os.getenv
)

with open("wood.txt", "r") as file:
    woods_content = file.read()


response = model.invoke(f"Which of the item is best for making a table? {woods_content}")
clear_text = response.content.replace('**', '')

print(clear_text)

