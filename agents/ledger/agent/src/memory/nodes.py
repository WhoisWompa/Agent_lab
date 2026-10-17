"""The two node kinds of the ledger's memory.

An Entity is a person or thing. A Context is something that happened or was
agreed, and it is what links entities together: every entity it names is
connected to every other through it.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Entity:
    """A person or thing the ledger knows about."""

    id: str                              # stable key, e.g. "sam"
    name: str                            # how the user refers to them
    aliases: list[str] = field(default_factory=list)   # other names seen in chats


@dataclass
class Context:
    """Something read from a chat that links entities: an event, a promise, a reply owed.

    `created` is when the ledger read it. `start` and `end` are when it happens
    or is due; either may be None. `done` is set only on things that linger
    until closed (a promise, a reply owed); an event just passes.
    """
    id: str
    kind: str                            # "event", "promise", "reply", ...
    text: str                            # the thing itself, in a sentence
    entities: list[str]                  # Entity ids this context connects
    created: datetime
    start: datetime | None = None
    end: datetime | None = None
    done: datetime | None = None         # when it was closed; None = still open
    source: str = ""                     # where it came from, e.g. "telegram:sam:1042"
