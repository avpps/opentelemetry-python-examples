from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import get_tracer, set_tracer_provider


if __name__ == "__main__":
    print("execution started")

    # based on example from https://opentelemetry.io/docs/instrumentation/python/exporters/#trace-1
    provider = TracerProvider()
    exporter = OTLPSpanExporter()
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)
    set_tracer_provider(provider)

    tracer = get_tracer(__name__)

    with tracer.start_as_current_span("test_span"):
        print("spawned")
