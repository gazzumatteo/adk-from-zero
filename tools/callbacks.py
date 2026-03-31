"""
Callback Hooks for Tool Execution

Demonstrates before/after callbacks for logging and audit trails.
Callbacks are invoked at specific lifecycle points during tool execution.
"""

from typing import Any
from datetime import datetime


def before_tool_callback(tool_name: str, args: dict[str, Any]) -> None:
    """
    Called before a tool is executed.

    Useful for:
    - Pre-validation of arguments
    - Logging request initiation
    - Rate limiting checks
    - Permission verification

    Args:
        tool_name: Name of the tool being called
        args: Arguments passed to the tool
    """
    timestamp = datetime.now().isoformat()
    print(f"\n[{timestamp}] TOOL CALLED: {tool_name}")
    print(f"  Arguments: {args}")


def after_tool_callback(
    tool_name: str, args: dict[str, Any], result: Any, error: Exception | None = None
) -> None:
    """
    Called after a tool completes execution.

    Useful for:
    - Logging results for audit trails
    - Updating metrics/analytics
    - Cleanup operations
    - Error handling and reporting

    Args:
        tool_name: Name of the tool that was executed
        args: Arguments that were passed to the tool
        result: The return value from the tool (None if error occurred)
        error: Exception if tool failed, None if successful
    """
    timestamp = datetime.now().isoformat()

    if error:
        print(f"\n[{timestamp}] TOOL ERROR: {tool_name}")
        print(f"  Error: {str(error)}")
    else:
        print(f"\n[{timestamp}] TOOL COMPLETED: {tool_name}")
        print(f"  Result: {result}")

    # In a real system, you might:
    # - Write to a database audit log
    # - Send metrics to monitoring system
    # - Trigger alerts on failures
    # - Update usage analytics
