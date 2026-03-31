"""
Customer Service Agent with Memory and Context

Maintains conversation state and customer context across interactions.
Demonstrates session management and memory persistence.
"""

from google.adk.agents import Agent
from google.adk.agents.tool import Tool

from tools.customer_tools import (
    lookup_customer,
    get_complaint_history,
    create_ticket,
)

# Define customer service tools
customer_lookup_tool = Tool.from_function(
    lookup_customer,
    name="lookup_customer",
    description="Look up customer information by email or ID",
)

history_tool = Tool.from_function(
    get_complaint_history,
    name="get_complaint_history",
    description="Retrieve customer's previous complaints and ticket history",
)

ticket_tool = Tool.from_function(
    create_ticket,
    name="create_ticket",
    description="Create a support ticket for a customer issue",
)

# Create the customer service agent
root_agent = Agent(
    name="customer_support",
    model="gemini-3-flash-preview",
    description="Customer support specialist with memory and context awareness",
    instruction="""You are an empathetic and knowledgeable customer support specialist.

Your approach:
1. Always start by looking up the customer to understand their profile
2. Review their complaint history to identify patterns
3. Leverage previous resolutions when applicable
4. Create tickets when needed, with appropriate priority
5. Offer proactive solutions and prevent future issues

Guidelines:
- Be warm and professional
- Show that you understand their history
- Take ownership of their problem
- Provide clear next steps
- Go above and beyond for loyal customers
- Track all issues in our system for continuity

Remember: The context you receive includes their history and profile.
Use this information to provide personalized, informed support.""",
    tools=[customer_lookup_tool, history_tool, ticket_tool],
)
