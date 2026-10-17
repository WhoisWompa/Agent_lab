"""Paths, .env and settings.json, and the one shape for a failure line. Runs once, on import."""
import json
import os
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")   # Windows consoles default to cp1252; a non-ASCII print() would crash
sys.stdin.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     # the agent/ folder
ENV_PATH = os.path.join(HERE, ".env")
SETTINGS_PATH = os.path.join(HERE, "settings.json")
DATA_DIR = os.path.join(HERE, "data")
LOGS_DIR = os.path.join(HERE, "logs")
RUN_ID = datetime.now().strftime("%Y%m%d-%H%M%S")            # one per process start
LOG_PATH = os.path.join(LOGS_DIR, f"trace_{RUN_ID}.jsonl")    # one trace per run: OpenInference spans, one per line
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)


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
    if not os.path.exists(path):
        die(f"missing {path}")
    with open(path, encoding="utf-8") as f:
        settings = json.load(f)
    settings.setdefault("provider", "openai")
    settings.setdefault("base_url", "")
    settings.setdefault("max_retries", 2)
    models = settings.get("models") or {}
    if not models.get("default"):
        die("settings.json is missing models.default")
    models.setdefault("allowed", [])
    settings["models"] = models
    settings.setdefault("mcpServers", {})
    return settings


def _require_env(key):
    value = os.environ.get(key, "")
    if not value:
        die(f"{key} is blank in .env")
    return value


_load_env(ENV_PATH)
settings = _load_settings(SETTINGS_PATH)     # src/ may import this for any extra knobs
api_key = _require_env("API_KEY")
