import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load .env.example from project root when imported
load_dotenv()

@dataclass(frozen=True)
class Settings:
    google_api_key: str | None = os.environ.get("GOOGLE_API_KEY")
    tavily_api_key: str | None = os.environ.get("TAVILY_API_KEY")
    langsmith_api_key: str | None = os.environ.get("LANGSMITH_API_KEY")
    langsmith_tracing: str | None = os.environ.get("LANGSMITH_TRACING")

settings = Settings()

def require_env(var_name: str, value: str | None):
    if not value:
        raise EnvironmentError(f"{var_name} not set. Ensure it exists in your .env")
