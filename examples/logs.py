import logging
import os
import platform

from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggingHandler, LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource, ResourceAttributes


def get_resource():
    return Resource.create({
        ResourceAttributes.DEPLOYMENT_ENVIRONMENT: "local",
        ResourceAttributes.HOST_NAME: platform.node(),
        ResourceAttributes.PROCESS_PID: os.getpid(),
        ResourceAttributes.SERVICE_NAME: "test_service_name",
        ResourceAttributes.SERVICE_NAMESPACE: "test_service_namespace",
        ResourceAttributes.SERVICE_VERSION: "",
        ResourceAttributes.SERVICE_INSTANCE_ID: "",
    })


class OTLPHandler(LoggingHandler):

    def __init__(self, level: int):
        resource = get_resource()
        provider = LoggerProvider(resource=resource)
        provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporter()))
        super().__init__(level=level, logger_provider=provider)


if __name__ == "__main__":
    print("execution started")

    logger = logging.getLogger(__name__)
    logger.addHandler(OTLPHandler(logging.INFO))
    logger.setLevel(logging.INFO)

    logger.info("test_log")
    print("log spawned")