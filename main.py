"""
Declarative Workflow - Main Entry Point

Demonstrates loading and executing agents from YAML configuration.
Run with: python main.py
"""

import os
import json
from google.adk.session import InMemorySessionService
from agent import root_agent, availability_workflow


def main() -> None:
    """
    Run the declaratively-configured agents and workflows.

    Demonstrates:
    - Loading agent from YAML
    - Accessing workflow graph structure
    - Using YAML-based configuration for deployment
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. See .env.example")

    session_service = InMemorySessionService()
    session_id = "workflow-session-001"

    print("\n" + "=" * 60)
    print("ADK 2.0 - DECLARATIVE WORKFLOW CONFIGURATION")
    print("=" * 60)
    print("\nAgents loaded from YAML configuration files\n")

    # Display loaded agent information
    print(f"Agent Name: {root_agent.name}")
    print(f"Agent Description: {root_agent.description}")
    print(f"Model: {root_agent.model}\n")

    # Display workflow structure
    print("-" * 60)
    print("AVAILABILITY WORKFLOW STRUCTURE")
    print("-" * 60)
    print(f"Workflow Name: {availability_workflow['workflow']['name']}")
    print(f"Version: {availability_workflow['workflow']['version']}")
    print(f"Description: {availability_workflow['workflow']['description']}\n")

    print("Workflow Nodes:")
    for node in availability_workflow["workflow"]["graph"]["nodes"]:
        print(f"  - {node['id']}: {node['type']} - {node['description']}")

    print("\nConditional Branching:")
    for node in availability_workflow["workflow"]["graph"]["nodes"]:
        if node["type"] == "condition":
            print(f"  Decision Point: {node['id']}")
            print(f"  Condition: {node['condition']}")
            print(f"  True Path: fulfill_immediately")
            print(f"  False Path: schedule_production\n")

    # Test the planning agent
    print("-" * 60)
    print("TESTING PLANNING AGENT")
    print("-" * 60 + "\n")

    sample_project = """
    Project: Build new e-commerce platform
    Requirements:
    - User authentication system
    - Product catalog with search
    - Shopping cart and checkout
    - Payment integration
    - Admin dashboard
    - Mobile responsive design
    Timeline: 6 months
    Budget: $500,000
    Team size: 8 people
    """

    print(f"Sample Project Request:{sample_project}\n")
    print("Processing with Planning Agent...\n")

    try:
        response = root_agent.generate_content(
            f"Create a detailed project plan for: {sample_project}",
            session=session_service.get_session(session_id),
        )

        print(f"Planning Agent Response:\n{response.text}\n")

    except Exception as e:
        print(f"Error: {e}")
        return

    # Interactive mode
    print("\n" + "=" * 60)
    print("Interactive Mode - Define Your Project")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input(
                "Describe your project (or 'quit' to exit): "
            ).strip()

            if user_input.lower() in ("quit", "exit"):
                print(
                    "\nThank you for using ADK 2.0 Workflow. Goodbye!"
                )
                break

            if not user_input:
                continue

            response = root_agent.generate_content(
                f"Plan this project: {user_input}",
                session=session_service.get_session(session_id),
            )

            print(f"\nPlanning Agent: {response.text}\n")

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
