"""Reliable recall demo: rolling mode first, then checkpointer mode."""
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent
from app.core.logging import setup_logging

from dotenv import load_dotenv
load_dotenv()

def rolling_mode():
    print("\n=== ROLLING MODE ===")
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    agent = create_react_agent(model, tools=[])

    messages = [
        SystemMessage(content="Use prior turns in this thread to answer follow-up questions."),
        HumanMessage(content="Hi, I'm Maheshkrishna"),
    ]
    # single invoke (easier to capture AI message)
    out1 = agent.invoke({"messages": messages})
    messages.append(out1["messages"][-1])  # append AI reply

    messages.append(HumanMessage(content="What's my name?"))
    out2 = agent.invoke({"messages": messages})
    for m in out2["messages"]:
        m.pretty_print()

def checkpoint_mode():
    print("\n=== CHECKPOINTER MODE ===")
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    from langgraph.checkpoint.memory import MemorySaver
    checkpointer = MemorySaver()
    agent = create_react_agent(model, tools=[], checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "abc123"}}

    agent.invoke({"messages": [SystemMessage(content="Use prior turns."), HumanMessage(content="Hi, I'm Maheshkrishna")]}, config)
    out = agent.invoke({"messages": [HumanMessage(content="What's my name?")]}, config)
    for m in out["messages"]:
        m.pretty_print()

if __name__ == "__main__":
    setup_logging()
    rolling_mode()
    checkpoint_mode()
