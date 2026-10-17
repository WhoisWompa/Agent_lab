"""The base. Fixed, never edited.

src/ imports model, tools and settings from here. main.py calls on_start(), on_message() and on_stop().
Each piece lives in its own file; this one only puts them in order.
"""
from .config import settings
from .models import model
from .mcp import tools
from .turn import on_start, on_message, on_stop     # last: turn imports src, and src does `from base import model, ...`
