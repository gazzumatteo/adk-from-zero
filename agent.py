"""
Root agent that orchestrates via A2A protocol.

This agent demonstrates:
- Using remote agents as specialized sub-agents
- A2A protocol for inter-agent communication
- Agent composition and delegation
"""

from typing import Any

from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


def create_root_agent(logistics_agent_url: str = "http://localhost:8001") -> Agent:
    """
    Create a root orchestrator agent that coordinates with remote A2A agents.

    Args:
        logistics_agent_url: URL of the remote logistics agent

    Returns:
        Agent: Root agent with remote A2A sub-agents
    """
    agent = Agent(
        name="Order-Orchestrator",
        model="gemini-3-flash-preview",
    )

    # Create remote A2A agent reference
    logistics_agent = RemoteA2aAgent(
        name="logistics",
        description="Handles logistics, shipment tracking, and delivery planning",
        agent_card_url=f"{logistics_agent_url}/.well-known/agent-card.json",
    )

    # Add remote agent to the root agent
    agent.add_sub_agent(logistics_agent)

    return agent


def main() -> None:
    """
    Run the root orchestrator agent with example A2A delegation.
    """
    agent = create_root_agent()

    prompt = """
    I need to process a customer order:
    - Order ID: ORD-2024-001
    - Customer: John Doe
    - Delivery Address: 123 Main St, Springfield, IL 62701
    - Items: 2x Laptop, 1x Monitor
    - Required delivery: March 28, 2026

    Please:
    1. Contact the logistics sub-agent to plan the shipment
    2. Get estimated delivery date
    3. Generate a delivery confirmation summary

    Use the A2A protocol to communicate with the logistics agent.
    """

    print("Starting Root Orchestrator Agent (A2A Protocol)...")
    print("-" * 60)
    print(f"Prompt: {prompt}\n")

    try:
        response = agent.run(prompt)
        print("-" * 60)
        print(f"Response:\n{response}")
    except ConnectionError as e:
        print(f"Error: Could not connect to logistics agent: {e}")
        print("Make sure the A2A server is running (python main_expose.py)")


if __name__ == "__main__":
    main()
