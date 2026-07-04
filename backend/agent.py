# agent.py

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from tools import TOOLS

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0
)

system_prompt = """
You are KrishiSetu AI, an agricultural assistant.

Always use available tools before answering.

If the user asks for farming advice:
- Get crop recommendations.
- Get market price information.
- Get fertilizer recommendations.
- Get irrigation advice.
- Get pest management advice.
- Get weather advice if relevant.

Combine all tool outputs into a single final answer.
Never skip tool usage when relevant tools exist.
"""

agent = create_react_agent(
    model=llm,
    tools=TOOLS,
    prompt=system_prompt
)

# agent.py

def run_agent(query: str):
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    # Get last AI message
    return result["messages"][-1].content