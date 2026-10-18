"""model(): a chat model for a listed model name, built with the key of the provider that serves it, with retries and an optional fallback."""
import os

from langchain.chat_models import init_chat_model

from .config import blocks, settings, warn


def model(name, fallback=None, **params):
    """A LangChain chat model for `name`. `fallback` names another listed model, used when a call to `name` fails.
    Raises ValueError if either name is not listed under any provider in base_settings.json."""
    m = _model(name, **params)
    if fallback is None:
        return m
    if _block(name)["label"] == _block(fallback)["label"]:
        warn(f"'{name}' and its fallback '{fallback}' both use {blocks[name]['key']}; a rate limit on one hits both")
    return m.with_fallbacks([_model(fallback, **params)])


def _block(name):
    if name not in blocks:
        raise ValueError(f"model '{name}' is not listed under any provider in base_settings.json")
    return blocks[name]


def _model(name, **params):
    block = _block(name)
    if block["base_url"]:
        params.setdefault("base_url", block["base_url"])
    params.setdefault("max_retries", settings["max_retries"])
    return init_chat_model(name, model_provider=block["provider"], api_key=os.environ[block["key"]], **params)
