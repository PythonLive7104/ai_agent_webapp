from urllib import response
import warnings
from langchain_core._api.deprecation import LangChainPendingDeprecationWarning
import os
import requests
'''
This is a weather AI assistant that uses the OpenWeatherMap API to fetch weather information based on the 
user's location. The assistant can determine the user's location using the ipapi service and provide weather 
updates accordingly. The assistant is designed to give temperature in Celsius for locations in Europe, Asia, 
Africa, and Australia, and in Fahrenheit for locations in North America and South America.

To assist the AI in providing accurate weather information, we have defined two functions:
1. get_weather_info(location: str) -> str: This function takes a location as input and returns the weather 
information for that location by making an API call to OpenWeatherMap.
2. get_location() -> str: This function retrieves the user's location by making a request to the ipapi service, 
which provides geolocation information based on the user's IP address.

3. Here will see how the AI agent can remember concersation and respond

4. Saving data using supabase database 
'''

warnings.filterwarnings(
    "ignore",
    category=LangChainPendingDeprecationWarning
)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.checkpoint.sqlite import SqliteSaver # for saving the agent's memory to a SQLite database
from langgraph.checkpoint.postgres import PostgresSaver # for saving the agent's memory to a PostgreSQL database

load_dotenv()
DB_URL = os.getenv("SUPABASE_DB_URL")

def get_weather_info(location: str) -> str:
    '''Gets weather information for a given location.'''    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    # Here you would typically make an API call to OpenWeatherMap
    base_url = f"http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    # Simulating an API response for demonstration purposes
    response = requests.get(base_url, params=parameters)
    return response.json()

def get_location() -> str:
    '''Gets the user's location.'''
    response = requests.get('https://ipapi.co/json', headers={'user-agent': 'your-bot 0.1'}).json()
    city = response['city']
    country = response['country_name']
    data = city + ", " + country

    return data

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.9
)

system_prompt = """
You are a helpful weather assistant. YOUR WORKFLOW:
1. If the user asks about the weather without specifying a location, you must:
   - Use the get_location() function to determine the user's location.
   - then call get_weather_info(location: str) with the determined location.

2. If the user provides a location, call get_weather_info(location: str) -> str: Gets weather 
    information for a given location.  
3. Use your knowlegde to decide the temperature unit base on locations.

4. Give temperature in Celsius for locations in Europe, Asia, Africa, and Australia.
5. Give temperature in Fahrenheit for locations in North America and South America.
"""

connection = SqliteSaver.from_conn_string('checkpoint.db')
checkpointer = connection.__enter__()

agent = create_agent(
    model=llm,
    tools=[get_weather_info, get_location],    
    system_prompt=system_prompt,
    checkpointer=checkpointer
)

