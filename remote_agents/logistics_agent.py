"""
Logistics agent exposed via A2A protocol.

This agent demonstrates:
- Specialized agent for logistics operations
- Shipping/delivery planning
- A2A exposure for remote consumption
"""

from datetime import datetime, timedelta
from typing import Any

from google.adk.agents import Agent


def create_logistics_agent() -> Agent:
    """
    Create a specialized logistics agent.

    Returns:
        Agent: Logistics agent with specialized tools
    """
    agent = Agent(
        name="Logistics-Agent",
        model="gemini-3-flash-preview",
    )

    # Define logistics tools
    def plan_shipment(
        order_id: str,
        destination_address: str,
        item_count: int,
    ) -> dict[str, Any]:
        """Plan shipment logistics."""
        return {
            "status": "planned",
            "order_id": order_id,
            "destination": destination_address,
            "items": item_count,
            "carrier": "FastShip Express",
            "tracking_number": f"FS{order_id.replace('-', '')[:8]}",
            "estimated_days": 3,
            "cost": 29.99,
        }

    def get_tracking_status(tracking_number: str) -> dict[str, Any]:
        """Get current tracking status."""
        return {
            "tracking_number": tracking_number,
            "status": "in_transit",
            "current_location": "Distribution Center, Chicago, IL",
            "last_update": datetime.now().isoformat(),
            "estimated_delivery": (datetime.now() + timedelta(days=2)).date().isoformat(),
        }

    def calculate_delivery_date(
        origin: str,
        destination: str,
        service_level: str = "standard",
    ) -> dict[str, Any]:
        """Calculate expected delivery date."""
        base_days = 3
        if service_level == "express":
            base_days = 1
        elif service_level == "overnight":
            base_days = 0

        delivery_date = datetime.now() + timedelta(days=base_days)

        return {
            "origin": origin,
            "destination": destination,
            "service_level": service_level,
            "estimated_delivery": delivery_date.date().isoformat(),
            "business_days": base_days,
            "guaranteed": True,
        }

    # Add tools to agent
    agent.add_tool(
        plan_shipment,
        description="Plan shipment for an order",
    )
    agent.add_tool(
        get_tracking_status,
        description="Get current tracking status for a shipment",
    )
    agent.add_tool(
        calculate_delivery_date,
        description="Calculate expected delivery date",
    )

    return agent


def main() -> None:
    """
    Run the logistics agent standalone for testing.
    """
    agent = create_logistics_agent()

    prompt = """
    I have an order for delivery to New York, NY with 5 items.
    Please plan the shipment and calculate the delivery date.
    """

    print("Testing Logistics Agent...")
    print("-" * 60)

    response = agent.run(prompt)
    print(f"Response:\n{response}")


if __name__ == "__main__":
    main()
