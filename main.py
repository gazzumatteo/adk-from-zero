"""
Main entry point for Article 12: Production Deployment.

Usage:
    python main.py [--eval] [--demo] [--host 0.0.0.0] [--port 8080]

This runs a production-grade agent with:
- Safety guardrails
- Evaluation framework
- OpenTelemetry observability
- Cloud Run ready
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agent import create_production_agent, evaluate_agent, main as demo_main


def main() -> None:
    """
    Run the production agent.
    """
    parser = argparse.ArgumentParser(
        description="Article 12: Production Deployment",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run full demonstration",
    )
    parser.add_argument(
        "--eval",
        action="store_true",
        help="Run evaluation only",
    )
    parser.add_argument(
        "--project-id",
        default="your-project-id",
        help="GCP project ID for tracing",
    )

    args = parser.parse_args()

    if args.eval:
        # Run evaluation only
        agent = create_production_agent(project_id=args.project_id)
        evaluate_agent(agent)

    elif args.demo:
        # Run full demo
        demo_main()

    else:
        # Default: run demo
        demo_main()


if __name__ == "__main__":
    main()
