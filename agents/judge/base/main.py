import os
import sys

sys.path[0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the agent folder, so `base` and `src` are its two packages
import base                                        # noqa: E402

base.start()                                       # import src/, start the MCP servers
output, end_process = base.on_start()              # the agent speaks first, if src/ defines on_start()
if output:
    print(output, flush=True)
try:
    while not end_process:
        reply = input()                            # what the user typed
        output, end_process = base.on_message(reply)   # the agent does its thing
        print(output, flush=True)                  # shows up in the chat
except EOFError:                                   # Stop was pressed
    print(base.on_stop(), flush=True)              # last words, then the script ends
