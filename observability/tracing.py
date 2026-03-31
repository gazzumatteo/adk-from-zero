"""
OpenTelemetry observability setup for production agents.

Provides:
- Distributed tracing with Cloud Trace
- Custom metrics
- Logging integration
"""

import logging
from typing import Any

from opentelemetry import metrics, trace
from opentelemetry.exporter.gcp_trace import CloudTraceExporter
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class ProductionTracing:
    """
    Production-grade tracing and observability setup.

    Integrates with:
    - Google Cloud Trace
    - Prometheus metrics
    - Structured logging
    """

    def __init__(self, project_id: str) -> None:
        """
        Initialize production tracing.

        Args:
            project_id: GCP project ID
        """
        self.project_id = project_id
        self.tracer = self._setup_tracing()
        self.meter = self._setup_metrics()

    def _setup_tracing(self) -> trace.Tracer:
        """
        Set up distributed tracing with Cloud Trace.

        Returns:
            Tracer instance
        """
        try:
            # Export traces to Cloud Trace
            cloud_trace_exporter = CloudTraceExporter(project_id=self.project_id)

            trace_provider = TracerProvider()
            trace_provider.add_span_processor(BatchSpanProcessor(cloud_trace_exporter))
            trace.set_tracer_provider(trace_provider)

            logger.info(f"Cloud Trace configured for project {self.project_id}")

        except Exception as e:
            logger.warning(f"Could not configure Cloud Trace: {e}")
            # Fall back to default tracer
            trace_provider = TracerProvider()
            trace.set_tracer_provider(trace_provider)

        return trace.get_tracer(__name__)

    def _setup_metrics(self) -> metrics.Meter:
        """
        Set up metrics with Prometheus.

        Returns:
            Meter instance
        """
        try:
            # Set up Prometheus metrics reader
            prometheus_reader = PrometheusMetricReader()

            meter_provider = MeterProvider(metric_readers=[prometheus_reader])
            metrics.set_meter_provider(meter_provider)

            logger.info("Prometheus metrics configured")

        except Exception as e:
            logger.warning(f"Could not configure Prometheus: {e}")
            # Fall back to default meter
            meter_provider = MeterProvider()
            metrics.set_meter_provider(meter_provider)

        return metrics.get_meter(__name__)

    def record_agent_execution(
        self,
        agent_name: str,
        prompt: str,
        response_time_ms: float,
        success: bool,
        error: str | None = None,
    ) -> None:
        """
        Record agent execution metrics.

        Args:
            agent_name: Name of the agent
            prompt: Input prompt
            response_time_ms: Response time in milliseconds
            success: Whether execution was successful
            error: Error message if failed
        """
        with self.tracer.start_as_current_span(f"{agent_name}_execution") as span:
            span.set_attribute("agent_name", agent_name)
            span.set_attribute("prompt_length", len(prompt))
            span.set_attribute("response_time_ms", response_time_ms)
            span.set_attribute("success", success)

            if error:
                span.set_attribute("error", error)

            logger.info(
                f"Agent execution: {agent_name}, "
                f"time={response_time_ms}ms, "
                f"success={success}",
            )

    def record_tool_call(
        self,
        tool_name: str,
        execution_time_ms: float,
        success: bool,
        error: str | None = None,
    ) -> None:
        """
        Record tool call metrics.

        Args:
            tool_name: Name of the tool
            execution_time_ms: Execution time in milliseconds
            success: Whether call was successful
            error: Error message if failed
        """
        with self.tracer.start_as_current_span(f"{tool_name}_call") as span:
            span.set_attribute("tool_name", tool_name)
            span.set_attribute("execution_time_ms", execution_time_ms)
            span.set_attribute("success", success)

            if error:
                span.set_attribute("error", error)

            logger.info(
                f"Tool call: {tool_name}, "
                f"time={execution_time_ms}ms, "
                f"success={success}",
            )

    def record_safety_check(
        self,
        check_type: str,
        passed: bool,
        details: str | None = None,
    ) -> None:
        """
        Record safety check results.

        Args:
            check_type: Type of safety check
            passed: Whether check passed
            details: Additional details
        """
        with self.tracer.start_as_current_span(f"safety_{check_type}") as span:
            span.set_attribute("check_type", check_type)
            span.set_attribute("passed", passed)

            if details:
                span.set_attribute("details", details)

            logger.info(f"Safety check: {check_type}, passed={passed}")
