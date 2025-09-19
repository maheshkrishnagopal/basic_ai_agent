# basic_ai_agent


## LangGraph ReAct Agent with Gemini + Tavily

This project demonstrates how to build a **ReAct agent** using [LangGraph](https://github.com/langchain-ai/langgraph), powered by **Google Gemini (via LangChain)** and enhanced with the **Tavily Search tool** for web retrieval.  
It includes optional **checkpointing/memory** support (in-memory or SQLite) so your agent can remember conversation history.

---

### 🚀 Features

- **Gemini 2.5 Flash** via LangChain’s `init_chat_model`
- **Tavily Search integration** for real-time web results
- **Direct tool-calling** (`model.bind_tools`)
- **ReAct agent** orchestration with `create_react_agent`
- **Streaming support** for token-level updates
- **Checkpointing** with either:
  - `MemorySaver` (ephemeral, in-memory)
  - `SqliteSaver` (persistent, across runs)
- **LangSmith optional tracing** for debugging & monitoring

---

### 📦 Installation

```bash
pip install -r requirements.txt
```

### 🔐 Configure Environment

Copy the example env and fill your keys:

```bash
cp .env.example .env
```

### 🏃 Running

Always run with -m from the repo root so Python treats app/ as a package.

A) Direct tool-calling demo

```bash
python -m app.runners.demo_direct
```

You’ll see:

    * A normal “Hi!” response
    * A tool-bound call that uses Tavily for: “Search for weather in Bangalore”
    (Reminder: Tavily is a search tool, not a live weather API.)

B) ReAct agent with memory/checkpointing

```bash
python -m app.runners.demo_agent
```

This uses LangGraph create_react_agent and streams two turns:

    1. “Hi, I’m Maheshkrishna”
    2. “What’s my name?” 

It sets a consistent thread_id so the second turn can use prior state.


### 🧰 Dev Tooling (Ruff)

```aiignore
# Lint
ruff check app/
ruff check app/ --fix

# Format
ruff format app/
```

Rules & settings live in pyproject.toml.

