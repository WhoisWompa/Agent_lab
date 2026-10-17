import base

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
