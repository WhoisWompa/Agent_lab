"""`from agents import <name>; <name>.run()`. The instance is made inside run(), so importing starts nothing."""
from .src import Agent


def run():
    Agent().run()
