"""Turn: one hook call inside one AGENT span, its output printed as the string it is. Used by run() for on_start, on_message and on_stop."""


class Turn:
    """Needs self.tracer and self.loop."""

    def _checked(self, output):
        """A string is printed as is, whatever it holds. Anything else is a bug in src/, shown as an error line."""
        if not isinstance(output, str):
            return self._error("empty: agent returned nothing to show")
        return output

    def _hook(self, name, coro, text=None):
        """Run one hook coroutine inside one AGENT span, which holds every model and tool span it causes.
        Returns: (output, done), the output checked. An exception is recorded on the span, an error line printed, then it still dies."""
        with self.tracer.start_as_current_span(name, openinference_span_kind="agent") as span:
            if text is not None:
                span.set_input(text)
            try:
                output, done = self.loop.run_until_complete(coro)
            except Exception:
                print(self._error("crash: agent stopped, see the trace in Phoenix"), flush=True)
                raise
            output = self._checked(output)
            span.set_output(output)
            span.set_attribute("done", done)
            return output, done
