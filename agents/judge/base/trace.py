"""The trace: every model call and tool call becomes an OpenInference span, sent to Phoenix as it ends, under this agent's project and this run's session."""
import logging

from openinference.instrumentation import TracerProvider
from openinference.instrumentation.langchain import LangChainInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import SpanProcessor
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from .config import AGENT, PHOENIX_URL, RUN_ID

logging.getLogger("opentelemetry").setLevel(logging.CRITICAL)   # Phoenix down: the run goes on, the trace is lost, stderr stays quiet


class _Session(SpanProcessor):
    """Stamps every span with this run's id, so Phoenix shows one run as one session."""
    def on_start(self, span, parent_context=None):
        span.set_attribute("session.id", RUN_ID)


provider = TracerProvider(resource=Resource({"openinference.project.name": AGENT}))
provider.add_span_processor(_Session())
provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=PHOENIX_URL + "/v1/traces", timeout=2)))
LangChainInstrumentor().instrument(tracer_provider=provider)
tracer = provider.get_tracer("agent")
