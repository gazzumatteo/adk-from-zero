"""
Root agent consuming remote logistics agent via A2A.

Usage:
    python main_consume.py [--logistics-url http://localhost:8001]

This script:
1. Creates the root orchestrator agent
2. Connects to the remote logistics A2A agent
3. Runs a coordinated workflow
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agent import create_root_agent


def main() -> None:
    """
    Run the root orchestrator agent consuming remote A2A agents.
    """
    parser = argparse.ArgumentParser(
        description="Article 08: A2A Protocol - Root Orchestrator",
    )
    parser.add_argument(
        "--logistics-url",
        default="http://localhost:8001",
        help="URL of the logistics A2A agent",
    )

    args = parser.parse_args()

    # Create root agent with remote A2A logistics agent
    print("Creating root orchestrator agent...")
    agent = create_root_agent(logistics_agent_url=args.logistics_url)

    # Example workflow: process a customer order
    prompt = """
    Process a new customer order with these details:
    - Order ID: ORD-20260321-001
    - Customer: Alice Johnson
    - Items: 3x Laptop, 2x Monitor, 1x Desk
    - Delivery Address: 456 Oak Ave, Portland, OR 97201
    - Service Level: Express

    Please:
    1. Engage the logistics agent to plan the shipment
    2. Get the estimated delivery date
    3. Create a shipping confirmation summary
    4. Provide tracking information format

    Use the A2A protocol to coordinate with the logistics agent.
    """

    print("Starting Order Processing Workflow...")
    print("-" * 70)
    print(f"Prompt:\n{prompt}\n")

    try:
        response = agent.run(prompt)
        print("-" * 70)
        print(f"Response:\n{response}")
        print("-" * 70)
        print("Order processing completed successfully!")

    except ConnectionError as e:
        print(f"Error: Could not connect to logistics agent at {args.logistics_url}")
        print(f"Details: {e}")
        print("\nMake sure to start the A2A server first:")
        print("  python main_expose.py --port 8001")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
