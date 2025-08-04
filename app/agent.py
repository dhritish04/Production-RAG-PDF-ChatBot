# app/agent.py

from langchain.agents import initialize_agent, AgentType
from app.tools import get_tools
from app.model import get_llm

def get_agent():
    tools = get_tools()
    llm = get_llm()

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
