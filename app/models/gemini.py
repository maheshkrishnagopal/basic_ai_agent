from langchain.chat_models import init_chat_model
from app.config.settings import settings, require_env

def get_gemini_model(model_name: str = "gemini-2.5-flash"):
    require_env("GOOGLE_API_KEY", settings.google_api_key)
    # unified initializer via LangChain
    model = init_chat_model(model_name, model_provider="google_genai")
    return model
