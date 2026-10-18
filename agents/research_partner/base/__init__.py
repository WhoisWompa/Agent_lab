"""The base. Fixed, never edited; synced from agent_template/base/ by sync.py at the repo root.

src/ imports model and tools from here. main.py calls start(), then on_start(), on_message() and on_stop().
Each piece lives in its own file; this one only puts them in order.
"""
from .config import settings
from .models import model
from .mcp import tools
from .turn import start, on_start, on_message, on_stop
