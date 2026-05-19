from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List
import os

'''
Recipe Generator
The pydantic models are used to define the structure of the response we want from the model. 
The Recipe model defines the structure of a single recipe, while the Response model defines the structure of the entire 
response, which includes a list of ingredients and a list of recipe suggestions.

We are giving instruction to langchain through pydantic and langchain will take care of the rest. 
It will convert the pydantic models into a format that the model can understand and will also handle the parsing of the 
response from the model back into the pydantic models.
'''
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Recipe(BaseModel):
    name: str = Field(description="Name of the recipe")
    description: str = Field(description = "Brief description of the recipe")
    prep_time: str = Field(description="Estimated preparation time of the recipe")

class Response(BaseModel):
    """A single recipe"""
    ingredients: List[str] = Field(description="List of main ingredients")
    recipes: List[Recipe] = Field(description="List of 3 recipe suggestions")



# Initialize the model
model = ChatOpenAI(
    model="gpt-4o",
    api_key=api_key
)
structured_model = model.with_structured_output(Response)
# The with_structured_output method is used to specify that we want the model to return a response 
# that matches the structure defined by the Response pydantic model. This allows us to easily parse the 
# response from the model into a structured format that we can work with in our code.

system_prompt = """
"You are a helpful chef. Identify the main ingredients. Suggest 3 recipes based those ingredients."
"""

# Create message
message = [{"role": "system", "content": system_prompt},
           {"role": "user", "content": "I have broccoli, butter, and eggs."}]

# Get and print the response
response = structured_model.invoke(message)
'''
In this code, we are initializing a ChatOpenAI model with the gpt-4o model and our API key. We then create a structured model 
using the with_structured_output method, specifying that we want the output to match the structure defined by the Response pydantic model.
'''

print(response.model_dump())