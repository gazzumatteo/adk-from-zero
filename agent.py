"""
Procurement Agent with Tools and Callbacks

Demonstrates tool integration with an agent.
The agent can call tools to query inventory, get quotes, place orders, and notify teams.
Callbacks provide observability and audit logging for all tool calls.
"""

from google.adk.agents import Agent
from google.adk.agents.tool import Tool

from tools.procurement import (
    check_inventory,
    get_supplier_quotes,
    place_order,
    notify_team,
)
from tools.callbacks import before_tool_callback, after_tool_callback


# Define tools that the agent can use
# Each tool describes its purpose and parameters for the LLM
inventory_tool = Tool.from_function(
    check_inventory,
    name="check_inventory",
    description="Check current inventory levels and availability for a product",
)

quotes_tool = Tool.from_function(
    get_supplier_quotes,
    name="get_supplier_quotes",
    description="Get pricing quotes from multiple suppliers for a product",
)

order_tool = Tool.from_function(
    place_order,
    name="place_order",
    description="Place a purchase order with a supplier",
)

notify_tool = Tool.from_function(
    notify_team,
    name="notify_team",
    description="Send notifications to team members about procurement status",
)

# Create the procurement agent with all tools
root_agent = Agent(
    name="procurement_specialist",
    model="gemini-3-flash-preview",
    description="A procurement specialist that manages inventory, supplier quotes, and orders",
    instruction="""You are an experienced procurement specialist for Acme Manufacturing.
Your responsibilities include:
1. Checking inventory availability
2. Requesting and comparing supplier quotes
3. Placing orders when appropriate
4. Communicating with the team about procurement status

When handling procurement requests:
- Always check inventory first
- If not available internally, get supplier quotes
- Compare options based on price, lead time, and minimum orders
- Place orders through proper channels
- Keep the team informed of all decisions

Be efficient, cost-conscious, and communicative.""",
    tools=[inventory_tool, quotes_tool, order_tool, notify_tool],
)

# Configure callbacks for observability
# These are invoked for every tool call, providing audit trails and logging
root_agent.before_tool_callback = before_tool_callback
root_agent.after_tool_callback = after_tool_callback
