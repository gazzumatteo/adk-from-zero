"""
Availability Checker Agent

Checks stock and production capacity for ordered products.
Provides feasibility assessment for order fulfillment.
"""

from google.adk.agents import Agent

availability_checker_agent = Agent(
    name="availability_checker",
    model="gemini-3-flash-preview",
    description="Checks product availability and production capacity",
    instruction="""You are an inventory and capacity specialist.
Given an order, you analyze:
1. Current stock levels
2. Production capacity
3. Lead times
4. Resource constraints

Provide a feasibility assessment:
- Can we fulfill from stock? (Yes/No + quantity available)
- If not, can we produce in time? (Yes/No + estimated duration)
- Any constraints or risks?

Be realistic and data-driven in your assessment.""",
)
