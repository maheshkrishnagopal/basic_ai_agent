from langchain_tavily import TavilySearch
from app.config.settings import settings, require_env

def get_tavily_tool(max_results: int = 3):
    require_env("TAVILY_API_KEY", settings.tavily_api_key)
    return TavilySearch(max_results=max_results)
