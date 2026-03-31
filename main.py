"""
Main entry point for Article 11: Dynamic Agent Factory.

Usage:
    python main.py [--demo] [--create DESCRIPTION] [--list]

This demonstrates:
- Creating agents dynamically from descriptions
- Agent registration and discovery
- Multi-agent orchestration
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agent import create_agent_from_description, create_factory_orchestrator, main as demo_main
from factory.agent_builder import AgentBuilder


def main() -> None:
    """
    Run the dynamic agent factory.
    """
    parser = argparse.ArgumentParser(
        description="Article 11: Dynamic Agent Factory",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run full demonstration",
    )
    parser.add_argument(
        "--create",
        metavar="DESCRIPTION",
        help="Create a new agent from natural language description",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all registered agents",
    )
    parser.add_argument(
        "--template",
        metavar="ROLE",
        help="Show template for a specific role",
    )

    args = parser.parse_args()

    if args.demo:
        demo_main()
    elif args.template:
        show_template(args.template)
    elif args.create:
        create_agent(args.create)
    elif args.list:
        list_agents()
    else:
        # Default: run demo
        demo_main()


def create_agent(description: str) -> None:
    """
    Create a new agent from description.

    Args:
        description: Natural language agent description
    """
    root_agent, registry, _ = create_factory_orchestrator()
    builder = AgentBuilder()

    print(f"Creating agent from description: '{description}'")
    print("-" * 70)

    agent = create_agent_from_description(
        registry,
        builder,
        description,
        "custom-001",
    )

    config = registry.get_config(agent.name)

    print(f"\nAgent Created Successfully!")
    print(f"  Name: {agent.name}")
    print(f"  Role: {config['role']}")
    print(f"  Capabilities: {json.dumps(config['capabilities'], indent=2)}")
    print(f"  Model: {config['model']}")


def list_agents() -> None:
    """
    List all registered agents.
    """
    root_agent, registry, _ = create_factory_orchestrator()

    all_agents = registry.list_all()

    if not all_agents:
        print("No agents registered yet.")
        return

    print("Registered Agents:")
    print("-" * 70)

    for agent_name, agent_info in all_agents.items():
        print(f"\n{agent_name}:")
        print(f"  Role: {agent_info['role']}")
        print(f"  Description: {agent_info['description']}")
        print(f"  Capabilities: {', '.join(agent_info['capabilities'])}")
        print(f"  Created: {agent_info['created_at']}")


def show_template(role: str) -> None:
    """
    Show template for a specific role.

    Args:
        role: Agent role
    """
    from factory.agent_templates import get_template

    template = get_template(role)

    if not template:
        print(f"Unknown role: {role}")
        print("Available roles:")
        from factory.agent_templates import list_available_roles

        for available_role in list_available_roles():
            print(f"  - {available_role}")
        return

    print(f"Template for {role}:")
    print("-" * 70)
    print(json.dumps(template, indent=2))


if __name__ == "__main__":
    main()
