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

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.9
)

agent = create_agent(model=llm)

response = agent.invoke({
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Which wood is best for tables?"
        }
    ]
})

print(response["messages"][-1].content)