"""Models: model(), a chat model for a listed name, built with the key of the provider that serves it, with retries and an optional fallback."""
import os

from langchain.chat_models import init_chat_model


class Models:
    """Needs self.blocks and self.settings from Config."""

    def model(self, name, fallback=None, **params):
        """A LangChain chat model for `name`. `fallback` names another listed model, used when a call to `name` fails.
        Returns: the model, with max_retries from settings and the fallback applied if given.
        Raises ValueError if either name is not listed under any provider in base_settings.json."""
        m = self._model(name, **params)
        if fallback is None:
            return m
        if self._block(name)["label"] == self._block(fallback)["label"]:
            self._warn(f"'{name}' and its fallback '{fallback}' both use {self.blocks[name]['key']}; a rate limit on one hits both")
        return m.with_fallbacks([self._model(fallback, **params)])

    def _block(self, name):
        if name not in self.blocks:
            raise ValueError(f"model '{name}' is not listed under any provider in base_settings.json")
        return self.blocks[name]

    def _model(self, name, **params):
        block = self._block(name)
        if block["base_url"]:
            params.setdefault("base_url", block["base_url"])
        params.setdefault("max_retries", self.settings["max_retries"])
        return init_chat_model(name, model_provider=block["provider"], api_key=os.environ[block["key"]], **params)
