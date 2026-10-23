"""Trace: every model call and tool call becomes an OpenInference span, sent to Phoenix as it ends, under this agent's project and this run's session."""
import logging

from openinference.instrumentation import TracerProvider
from openinference.instrumentation.langchain import LangChainInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import SpanProcessor
from opentelemetry.sdk.trace.export import BatchSpanProcessor

logging.getLogger("opentelemetry").setLevel(logging.CRITICAL)   # Phoenix down: the run goes on, the trace is lost, stderr stays quiet


class _Session(SpanProcessor):
    """Stamps every span with the run id, so Phoenix shows one run as one session."""
    def __init__(self, run_id):
        self.run_id = run_id

    def on_start(self, span, parent_context=None):
        span.set_attribute("session.id", self.run_id)


class Trace:
    """Needs self.name, self.run_id and self.settings. Sets self.tracer."""
    _instrumented = False          # LangChain is instrumented once per process, by whichever agent is built first

    def _make_tracer(self):
        """Returns: the tracer for this agent's project, exporting to the phoenix address in settings."""
        url = self.settings["phoenix"].rstrip("/") + "/v1/traces"
        provider = TracerProvider(resource=Resource({"openinference.project.name": self.name}))
        provider.add_span_processor(_Session(self.run_id))
        provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=url, timeout=2)))
        if not Trace._instrumented:
            LangChainInstrumentor().instrument(tracer_provider=provider)
            Trace._instrumented = True
        return provider.get_tracer("agent")
