import os

from base import model
from langchain.agents import create_agent # type: ignore

HERE = os.path.dirname(os.path.abspath(__file__))     # the src/ folder: instructions/ is in it, data/ is one level up


def instructions(name):
    """The text of instructions/<name>.md."""
    with open(os.path.join(HERE, "instructions", name + ".md"), encoding="utf-8") as f:
        return f.read()


async def on_message(text):
    """`text` is one line from the user. Build the agent with model() and tools(), prompts via instructions(), run it on text.
    Return (line, done): the reply to show, and True to end the run or False to wait for the next message."""
    return 


async def on_stop():
    """The user pressed Stop. Save anything worth keeping, then return the last line to show. The process exits after."""
    return
