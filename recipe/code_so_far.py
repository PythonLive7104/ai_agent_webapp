import base64
import mimetypes

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

image_path = "images/ingredients.png"
mime_type, _ = mimetypes.guess_type(image_path) 
# Get the MIME type of the image file. 
# This is important for the model to understand how to process the image data. The mimetypes.guess_type function 
# returns a tuple where the first element is the MIME type and the second element is the encoding (if any). 
# We only need the MIME type for our purposes, so we ignore the second element with the underscore (_).

with open(image_path, 'rb') as file:
    raw_binary = file.read()
    base64_bytes = base64.b64encode(raw_binary)
    image_base64 = base64_bytes.decode("utf-8")

# Initialize the model
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
system_prompt = """
"You are a helpful chef. Identify the main ingredients. Suggest 3 recipes based those ingredients."
"""

# Create message
message = [{"role": "system", "content": system_prompt},
           {"role": "user", "content": [{"type": "image", "base64": image_base64, "mime_type": mime_type}]}]

# Get and print the response
response = model.invoke(message)
print(response.text)