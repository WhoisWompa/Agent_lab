"""model(): a chat model from settings.json, allow-listed, with retries and optional fallback."""
from langchain.chat_models import init_chat_model

from .config import api_key, settings, warn


def model(name=None, fallback=False, **params):
    """A LangChain chat model from settings.json. Raises if `name` is not allowed, unless fallback=True."""
    default = settings["models"]["default"]
    allowed = settings["models"]["allowed"]
    name = name or default
    if allowed and name not in allowed and name != default:
        if not fallback:
            raise ValueError(f"model '{name}' is not in settings.json models.allowed")
        warn(f"model '{name}' not allowed, using '{default}'")
        name = default
    m = _model(name, **params)
    if fallback and name != default:
        m = m.with_fallbacks([_model(default, **params)])
    return m


def _model(name, **params):
    if settings["base_url"]:
        params.setdefault("base_url", settings["base_url"])
    params.setdefault("max_retries", settings["max_retries"])
    return init_chat_model(name, model_provider=settings["provider"], api_key=api_key, **params)
