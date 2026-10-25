
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool

root_agent = Agent(
    name="google_search_agent",
    model="gemini-2.0-flash",
    description="An agent that searches the web",
    tools=[google_search],
    instruction="""
    You are a helpful assistant with access to Google Search.
    Search for factual or up-to-date information.
    Summarize results in simple language.
    Include source citations when available.
    """
)
