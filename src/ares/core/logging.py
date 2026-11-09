"""Structured logging setup (ARCHITECTURE §14).

Logs are structured (console in development, JSON in production). Sensitive values and
credentials must never be passed to the logger.
"""

from __future__ import annotations

import logging
import sys
from typing import cast

import structlog
from structlog.typing import FilteringBoundLogger, Processor


def configure_logging(*, level: str = "INFO", json_logs: bool = False) -> None:
    """Configure structlog for the whole process."""

    log_level = getattr(logging, level.upper(), logging.INFO)

    processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.StackInfoRenderer(),
    ]
    if json_logs:
        processors.append(structlog.processors.format_exc_info)
        processors.append(structlog.processors.JSONRenderer())
    else:
        processors.append(structlog.dev.ConsoleRenderer())

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        logger_factory=structlog.PrintLoggerFactory(file=sys.stderr),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str | None = None) -> FilteringBoundLogger:
    """Return a bound structured logger."""

    return cast(FilteringBoundLogger, structlog.get_logger(name))


__all__ = ["configure_logging", "get_logger"]
