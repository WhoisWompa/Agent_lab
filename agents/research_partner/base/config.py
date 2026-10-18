"""Paths, .env and base_settings.json, and the one shape for a failure line. Runs once, on import."""
import importlib.util
import json
import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")   # Windows consoles default to cp1252; a non-ASCII print() would crash
sys.stdin.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     # the agent folder: base/ and src/ sit in it
ENV_PATH = os.path.join(HERE, ".env")
SETTINGS_PATH = os.path.join(HERE, "base_settings.json")
DATA_DIR = os.path.join(HERE, "data")
AGENT = os.path.basename(HERE)                                # the Phoenix project every span of this agent lands in
RUN_ID = datetime.now().strftime("%Y%m%d-%H%M%S")            # one per process start: the Phoenix session every span of this run carries
os.makedirs(DATA_DIR, exist_ok=True)

KNOWN = {"providers", "max_retries", "mcpServers", "phoenix"}  # every key base_settings.json may hold
BLOCK = {"provider", "base_url", "key", "models"}              # every key a provider block must hold


def error(msg):
    """The one shape for a failure line on stdout: {"error": "<kind>: <message>"}."""
    return json.dumps({"error": msg})


def die(msg):
    """Startup failure: say it on stdout, where the app can show it, then exit."""
    print(error(f"startup: {msg}"), flush=True)
    raise SystemExit(1)


def warn(msg):
    print(f"[base] {msg}", file=sys.stderr, flush=True)


def _load_env(path):
    """Read KEY=value lines into os.environ. No dependency."""
    if not os.path.exists(path):
        die(f"missing {path}")
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()


def _load_settings(path):
    """base_settings.json as a dict, checked. Any shape error is a startup failure with a named reason."""
    if not os.path.exists(path):
        die(f"missing {path}")
    with open(path, encoding="utf-8") as f:
        settings = json.load(f)
    unknown = set(settings) - KNOWN
    if unknown:
        die(f"base_settings.json has unknown key(s) {sorted(unknown)}; allowed: {sorted(KNOWN)}")
    settings.setdefault("max_retries", 2)
    settings.setdefault("mcpServers", {})
    settings.setdefault("phoenix", "http://localhost:6006")   # where the trace goes; absent means a local Phoenix
    providers = settings.get("providers") or {}
    if not providers:
        die("base_settings.json has no providers; add one with provider.py at the repo root")
    for label, block in providers.items():
        missing = BLOCK - set(block)
        if missing:
            die(f"provider '{label}' is missing {sorted(missing)}")
        if not isinstance(block["models"], list) or not block["models"]:
            die(f"provider '{label}' lists no models")
    settings["providers"] = providers
    return settings


def _blocks(providers):
    """Model name -> the one provider block that serves it, with its label. A name under two blocks is a startup failure."""
    blocks = {}
    for label, block in providers.items():
        for name in block["models"]:
            if name in blocks:
                die(f"model '{name}' is listed under both '{blocks[name]['label']}' and '{label}'; a model belongs to one provider")
            blocks[name] = {"label": label, **block}
    return blocks


def _check_keys(providers):
    """Every block's env var is filled in and its LangChain package is installed."""
    for label, block in providers.items():
        if not os.environ.get(block["key"], ""):
            die(f"{block['key']} is blank in .env (provider '{label}')")
        package = "langchain_" + block["provider"]
        if importlib.util.find_spec(package) is None:
            die(f"provider '{label}' needs {package.replace('_', '-')} in src/requirements.txt")


_load_env(ENV_PATH)
settings = _load_settings(SETTINGS_PATH)
PHOENIX_URL = settings["phoenix"].rstrip("/")
blocks = _blocks(settings["providers"])      # models.py looks a name up here to find its key
_check_keys(settings["providers"])
