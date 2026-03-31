"""
Start the A2A server to expose the logistics agent.

Usage:
    python main_expose.py [--port 8001]

This script:
1. Creates the logistics agent
2. Converts it to A2A service
3. Starts the FastAPI server
"""

import argparse
import json
import sys
from pathlib import Path

import uvicorn

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from remote_agents.logistics_agent import create_logistics_agent


def main() -> None:
    """
    Start the A2A server exposing the logistics agent.
    """
    parser = argparse.ArgumentParser(
        description="Article 08: A2A Protocol - Expose Logistics Agent",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8001,
        help="Port to run the A2A server on",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind the server to",
    )

    args = parser.parse_args()

    # Create the logistics agent
    print("Creating logistics agent...")
    logistics_agent = create_logistics_agent()

    # Convert to A2A service
    print("Converting agent to A2A service...")
    a2a_app = to_a2a(logistics_agent, port=args.port)

    # Log the agent card URL
    agent_card_url = f"http://localhost:{args.port}/.well-known/agent-card.json"
    print(f"Agent Card available at: {agent_card_url}")

    # Start the server
    print(f"Starting A2A server on {args.host}:{args.port}...")
    uvicorn.run(
        a2a_app,
        host=args.host,
        port=args.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
