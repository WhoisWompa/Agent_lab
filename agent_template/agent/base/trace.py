"""The trace: every model call and tool call becomes an OpenInference span, appended to this run's file as it ends."""
from openinference.instrumentation import TracerProvider
from openinference.instrumentation.langchain import LangChainInstrumentor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

from .config import LOG_PATH

_file = open(LOG_PATH, "a", encoding="utf-8")
provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter(out=_file, formatter=lambda s: s.to_json(indent=None) + "\n")))
LangChainInstrumentor().instrument(tracer_provider=provider)
tracer = provider.get_tracer("agent")
