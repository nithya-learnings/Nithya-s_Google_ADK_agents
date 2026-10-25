
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool

root_agent = Agent(
    name="google_search_agent",
    model=Gemini(
        model="gemini-2.0-flash",
        use_interactions_api=True,
    ),
    description="An agent that searches the web",
    instruction="""
    You are a helpful assistant with access to Google Search.
    Search for factual or up-to-date information.
    Summarize results in simple language.
    Include source citations when available.
    """,
    tools=[
        GoogleSearchTool(bypass_multi_tools_limit=True)
    ],
)
