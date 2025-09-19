from typing import Sequence, Mapping, Any
from langgraph.prebuilt import create_react_agent
from app.models.gemini import get_gemini_model

def create_agent(tools: Sequence[Any], *, with_memory=False, checkpointer=None):
    model = get_gemini_model()
    if with_memory and checkpointer is None:
        raise ValueError("If with_memory=True, provide a checkpointer (MemorySaver or SqliteSaver).")
    agent = create_react_agent(model, tools, checkpointer=checkpointer)
    return agent

def default_config(thread_id: str = "default-thread") -> Mapping[str, Any]:
    return {"configurable": {"thread_id": thread_id}}
