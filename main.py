"""
Main entry point for Article 09: A2UI Generative UI.

Demonstrates generative UI generation through structured agent output.

Usage:
    python main.py [--output FILE] [--pretty]
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agent import create_dashboard_agent


def main() -> None:
    """
    Run dashboard agent and optionally save output.
    """
    parser = argparse.ArgumentParser(
        description="Article 09: A2UI Generative UI",
    )
    parser.add_argument(
        "--output",
        help="Save UI blueprint to file",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output",
    )

    args = parser.parse_args()

    agent = create_dashboard_agent()

    prompt = """
    Create a modern operations dashboard UI with these sections:

    1. Top row: KPI cards showing Revenue, Orders, Customers Online, and Conversion Rate
    2. Middle section: Production metrics table with hourly throughput data
    3. Bottom left: Order status pie chart (Pending, Processing, Ready to Ship, Shipped)
    4. Bottom right: Customer satisfaction metrics with NPS score card

    Each component should have a meaningful ID, title, and proper styling hints.
    Generate the complete UIBlueprint JSON structure.
    """

    print("Generating Operations Dashboard UI...")
    print("-" * 70)

    try:
        response = agent.run(prompt)

        # Convert to JSON if needed
        if hasattr(response, "model_dump_json"):
            json_output = response.model_dump_json(indent=2 if args.pretty else None)
        else:
            json_output = json.dumps(response, indent=2 if args.pretty else None)

        # Display output
        print(json_output)

        # Save to file if requested
        if args.output:
            output_path = Path(args.output)
            output_path.write_text(json_output)
            print(f"\nUI Blueprint saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
