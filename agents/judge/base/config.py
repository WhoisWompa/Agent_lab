"""Config: .env, base_settings.json, the model index and the one shape for a failure line. Every check names its reason and exits."""
import importlib.util
import json
import os
import sys

KNOWN = {"providers", "max_retries", "mcpServers", "phoenix"}  # every key base_settings.json may hold
BLOCK = {"provider", "base_url", "key", "models"}              # every key a provider block must hold


class Config:
    """Reads the agent folder's .env and base_settings.json into self.settings and self.blocks. Needs self.folder."""

    def _load_env(self):
        """Read .env's KEY=value lines into os.environ, so src/ reads a secret by its variable name. No dependency."""
        path = os.path.join(self.folder, ".env")
        if not os.path.exists(path):
            self._die(f"missing {path}")
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

    def _load_settings(self):
        """base_settings.json as a dict, checked. Any shape error is a startup failure with a named reason."""
        path = os.path.join(self.folder, "base_settings.json")
        if not os.path.exists(path):
            self._die(f"missing {path}")
        with open(path, encoding="utf-8") as f:
            settings = json.load(f)
        unknown = set(settings) - KNOWN
        if unknown:
            self._die(f"base_settings.json has unknown key(s) {sorted(unknown)}; allowed: {sorted(KNOWN)}")
        settings.setdefault("max_retries", 2)
        settings.setdefault("mcpServers", {})
        settings.setdefault("phoenix", "http://localhost:6006")   # where the trace goes; absent means a local Phoenix
        providers = settings.get("providers") or {}
        if not providers:
            self._die("base_settings.json has no providers; add one with provider.py at the repo root")
        for label, block in providers.items():
            missing = BLOCK - set(block)
            if missing:
                self._die(f"provider '{label}' is missing {sorted(missing)}")
            if not isinstance(block["models"], list) or not block["models"]:
                self._die(f"provider '{label}' lists no models")
        settings["providers"] = providers
        return settings

    def _index_blocks(self):
        """Model name -> the one provider block that serves it, with its label. A name under two blocks is a startup failure."""
        blocks = {}
        for label, block in self.settings["providers"].items():
            for name in block["models"]:
                if name in blocks:
                    self._die(f"model '{name}' is listed under both '{blocks[name]['label']}' and '{label}'; a model belongs to one provider")
                blocks[name] = {"label": label, **block}
        return blocks

    def _check_keys(self):
        """Every block's env var is filled in and its LangChain package is installed."""
        for label, block in self.settings["providers"].items():
            if not os.environ.get(block["key"], ""):
                self._die(f"{block['key']} is blank in .env (provider '{label}')")
            package = "langchain_" + block["provider"]
            if importlib.util.find_spec(package) is None:
                self._die(f"provider '{label}' needs {package.replace('_', '-')} in src/requirements.txt")

    @staticmethod
    def _error(msg):
        """The one shape for a failure line on stdout: {"error": "<kind>: <message>"}."""
        return json.dumps({"error": msg})

    def _die(self, msg):
        """Startup failure: say it on stdout, where the app can show it, then exit."""
        print(self._error(f"startup: {msg}"), flush=True)
        raise SystemExit(1)

    @staticmethod
    def _warn(msg):
        print(f"[base] {msg}", file=sys.stderr, flush=True)
