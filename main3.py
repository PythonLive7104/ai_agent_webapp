import warnings
from langchain_core._api.deprecation import LangChainPendingDeprecationWarning

warnings.filterwarnings(
    "ignore",
    category=LangChainPendingDeprecationWarning
)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()

def get_weather_info(location: str) -> str:
    '''Gets weather information for a given location.'''
    return f"The weather in {location} is sunny with temperatures around 25°C."

def get_user_location() -> str:
    '''Gets the user's location.'''
    return "northern Italy, eastern Italy, southern Italy, western Italy"

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.9
)

system_prompt = """
You are a helpful assistant. You have access to the following tools:
1. get_weather_info(location: str) -> str: Gets weather information for a given location.
2. get_user_location() -> str: Gets the user's location.    
"""
agent = create_agent(
    model=llm,
    tools=[get_weather_info, get_user_location],    
    system_prompt=system_prompt
)

response = agent.invoke({
    "messages": [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "How is the weather in northern Italy?"
        }
    ]
})

print(response["messages"][-1].content)