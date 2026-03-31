"""
Order Receiver Agent

Captures and validates initial order details from customers.
This agent normalizes customer requests into structured order data.
"""

from google.adk.agents import Agent

order_receiver_agent = Agent(
    name="order_receiver",
    model="gemini-3-flash-preview",
    description="Captures and validates customer order details",
    instruction="""You are an order reception specialist.
Your job is to:
1. Listen to customer requirements
2. Extract key order details (product name, quantity, delivery date)
3. Validate basic feasibility
4. Format order data clearly

Always confirm the customer has provided:
- Product name/type
- Desired quantity
- Any specific requirements or timeline

Be clear and organized in your response.""",
)
