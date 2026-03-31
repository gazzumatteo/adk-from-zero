"""
Main entry point for Article 07: MCP Tools Integration examples.

Usage:
    python main.py [--remote] [--mcp-url URL]
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from agent import create_mcp_agent, main as agent_main
from agent_remote import create_remote_mcp_agent


def main() -> None:
    """
    Run MCP integration examples.
    """
    parser = argparse.ArgumentParser(
        description="Article 07: MCP Tools Integration",
    )
    parser.add_argument(
        "--remote",
        action="store_true",
        help="Use remote MCP server instead of local",
    )
    parser.add_argument(
        "--mcp-url",
        default="http://localhost:8000",
        help="Remote MCP server URL (requires --remote)",
    )

    args = parser.parse_args()

    if args.remote:
        print("Starting Remote MCP Agent Demo...")
        print(f"Connecting to: {args.mcp_url}")
        agent = create_remote_mcp_agent(args.mcp_url)
    else:
        print("Starting Local MCP Agent Demo...")
        agent_main()
        return

    # Run remote agent
    prompt = """
    Please use the remote ERP system to:
    1. Show all available furniture
    2. Check the stock level of the most expensive item
    3. Create a summary of findings
    """

    print("-" * 60)
    print(f"Prompt: {prompt}\n")

    try:
        response = agent.run(prompt)
        print("-" * 60)
        print(f"Response:\n{response}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
