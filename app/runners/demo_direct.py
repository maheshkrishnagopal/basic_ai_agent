"""Direct tool-calling example (no LangGraph state machine)."""
from app.core.logging import setup_logging
from app.models.gemini import get_gemini_model
from app.tools.tavily_search import get_tavily_tool

def main():
    log = setup_logging()
    model = get_gemini_model()
    search = get_tavily_tool()
    model_with_tools = model.bind_tools([search])

    # Plain chat
    resp = model_with_tools.invoke([{"role": "user", "content": "Hi!"}])
    log.info("[Direct] Plain chat: %s", resp.text())

    # Ask to use the tool
    prompt = "Search for weather in Bangalore"
    resp = model_with_tools.invoke([{"role": "user", "content": prompt}])
    log.info("[Direct] Message: %s", resp.text())
    log.info("[Direct] Tool calls: %s", getattr(resp, "tool_calls", None))

if __name__ == "__main__":
    main()
