"""
Agent for the streaming demo.

This agent provides:
- Text generation capabilities
- Integration with dashboard tools
- Support for streaming responses
"""

from typing import Any

from google.adk.agents import Agent


def create_agent() -> Agent:
    """
    Create an agent for streaming dashboard operations.

    Returns:
        Agent: Configured agent with tools
    """
    agent = Agent(
        name="Streaming-Dashboard-Agent",
        model="gemini-3-flash-preview",
    )

    # Define tools for dashboard operations
    def generate_report(report_type: str) -> str:
        """Generate a business report."""
        reports = {
            "daily": """
            Daily Operations Report
            ========================
            - Total Revenue: $45,230.50
            - Orders Processed: 342
            - Conversion Rate: 3.45%
            - Customer Satisfaction: 4.6/5.0
            """,
            "weekly": """
            Weekly Operations Report
            ========================
            - Total Revenue: $287,456.00
            - Orders Processed: 2,145
            - Average Daily Revenue: $41,065.14
            - Top Product Category: Electronics
            """,
            "monthly": """
            Monthly Operations Report
            =========================
            - Total Revenue: $1,245,678.00
            - Orders Processed: 8,920
            - Average Order Value: $139.87
            - Customer Retention: 87.3%
            """,
        }
        return reports.get(
            report_type,
            "Unknown report type. Use: daily, weekly, or monthly",
        )

    def get_alerts() -> str:
        """Get current operational alerts."""
        return """
        Active Alerts:
        - 12 orders overdue (>24 hours)
        - 3 machines below efficiency threshold
        - Supply shortage for Component X (estimated 2 days)
        - 2 critical support tickets pending response
        """

    def analyze_trend(metric: str, period: str) -> str:
        """Analyze metric trends."""
        return f"Analyzing {metric} trend over {period}: Shows 12.5% growth with positive momentum."

    # Add tools to agent
    agent.add_tool(
        generate_report,
        description="Generate operational reports (daily, weekly, monthly)",
    )
    agent.add_tool(
        get_alerts,
        description="Get current operational alerts and warnings",
    )
    agent.add_tool(
        analyze_trend,
        description="Analyze trends for specific metrics",
    )

    return agent
