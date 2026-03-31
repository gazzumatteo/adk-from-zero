"""
Dashboard agent that generates structured UI blueprints.

This agent demonstrates:
- Structured output using Pydantic models
- Generating A2UI component definitions
- Using output_schema for deterministic JSON output
"""

import json
import sys
from pathlib import Path

from google.adk.agents import Agent

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from models.ui_components import DashboardLayout, KPI, Table, UIBlueprint
from tools.dashboard_tools import (
    get_customer_satisfaction,
    get_kpi_data,
    get_order_backlog,
    get_production_metrics,
)


def create_dashboard_agent() -> Agent:
    """
    Create an agent that generates UI blueprints.

    Returns:
        Agent: Dashboard agent with UI generation capability
    """
    agent = Agent(
        name="Dashboard-Generator",
        model="gemini-3-flash-preview",
    )

    # Add tools for data collection
    agent.add_tool(
        get_kpi_data,
        description="Retrieve key performance indicator metrics",
    )
    agent.add_tool(
        get_production_metrics,
        description="Get production and efficiency metrics",
    )
    agent.add_tool(
        get_order_backlog,
        description="Retrieve order backlog and status data",
    )
    agent.add_tool(
        get_customer_satisfaction,
        description="Get customer satisfaction and NPS metrics",
    )

    # Configure structured output using UIBlueprint schema
    agent.output_schema = UIBlueprint

    return agent


def main() -> None:
    """
    Run the dashboard agent to generate a UI blueprint.
    """
    agent = create_dashboard_agent()

    prompt = """
    Generate a comprehensive operations dashboard UI blueprint that includes:
    1. A section with KPIs showing revenue, orders, and conversion metrics
    2. A table with production hourly metrics
    3. Order status breakdown with pending, processing, and shipped counts
    4. Customer satisfaction KPIs including NPS score

    Structure the output as a properly formatted UIBlueprint JSON with
    appropriate components (KPI cards, tables, and metrics).

    Make sure each component has a unique ID and meaningful title.
    """

    print("Starting Dashboard Generator Agent...")
    print("-" * 70)
    print(f"Prompt: {prompt}\n")

    try:
        response = agent.run(prompt)

        print("-" * 70)
        print("Generated UI Blueprint:\n")

        # If response is already a UIBlueprint object
        if isinstance(response, UIBlueprint):
            print(response.model_dump_json(indent=2))
        else:
            # Try to parse as JSON
            try:
                blueprint_data = json.loads(str(response))
                print(json.dumps(blueprint_data, indent=2))
            except json.JSONDecodeError:
                print(response)

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
