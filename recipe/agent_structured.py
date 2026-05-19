from dotenv import load_dotenv
import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

from pydantic import BaseModel, Field

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


# =========================
# STRUCTURED OUTPUT
# =========================

class EmailResponse(BaseModel):
    recipient: str = Field(description="Email address")
    subject: str = Field(description="Subject")
    body: str = Field(description="Body")
    status: str = Field(description="Status")
    summary: str = Field(description="Summary")


# =========================
# TOOL
# =========================

@tool
def send_email(
    email_address: str,
    sender_name: str,
    subject: str,
    body: str
):
    """Send an email"""

    print("Sending email...")

    return {
        "recipient": email_address,
        "subject": subject,
        "body": body,
        "status": "sent",
        "summary": "Email sent successfully"
    }


# =========================
# MODEL
# =========================

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=api_key
)


# =========================
# SYSTEM PROMPT
# =========================

system_prompt = """
My name is Olatunji.

You are a helpful assistant.

If the user asks to send an email:
- generate professional email content
- use the send_email tool
"""


# =========================
# AGENT
# =========================

agent = create_agent(
    model=llm,
    tools=[send_email],
    system_prompt=system_prompt,
    response_format=EmailResponse
)


# =========================
# USER QUERY
# =========================

user_query = """
Send an email to my manager,
graciousfx@gmail.com,
about the project update.
"""


# =========================
# INVOKE
# =========================

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": user_query
            }
        ]
    }
)

# print(response['messages'][-1].content)
print(response['structured_response'].model_dump())