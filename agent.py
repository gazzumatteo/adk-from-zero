"""
Root orchestrator agent for the dynamic agent factory.

Demonstrates:
- Creating agents from natural language
- Registering and discovering agents
- Coordinating multi-agent workflows
"""

import sys
from pathlib import Path

from google.adk.agents import Agent

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from factory.agent_builder import AgentBuilder
from factory.agent_registry import AgentRegistry
from factory.agent_templates import get_template, list_available_roles
from factory.dynamic_orchestrator import DynamicOrchestrator


def create_factory_orchestrator() -> tuple[Agent, AgentRegistry, DynamicOrchestrator]:
    """
    Create the factory orchestrator with registry and builder.

    Returns:
        Tuple of (root_agent, registry, orchestrator)
    """
    registry = AgentRegistry()
    builder = AgentBuilder()

    root_agent = Agent(
        name="Factory-Orchestrator",
        model="gemini-3-flash-preview",
    )

    # Store registry and builder for use
    root_agent._registry = registry
    root_agent._builder = builder

    orchestrator = DynamicOrchestrator(registry)

    return root_agent, registry, orchestrator


def create_agent_from_description(
    registry: AgentRegistry,
    builder: AgentBuilder,
    description: str,
    agent_id: str,
) -> Agent | None:
    """
    Create an agent from natural language description.

    Args:
        registry: Agent registry
        builder: Agent builder
        description: Natural language description
        agent_id: Unique agent identifier

    Returns:
        Created Agent or None if failed
    """
    # Build configuration from description
    config = builder.build_from_description(description)

    # Create agent instance
    agent_name = f"{config['role']}-{agent_id}"
    agent = Agent(
        name=agent_name,
        model=config.get("model", "gemini-3-flash-preview"),
    )

    # Register in registry
    registry.register(
        agent=agent,
        role=config["role"],
        description=description,
        capabilities=config.get("capabilities", []),
        config=config,
    )

    return agent


def main() -> None:
    """
    Demonstrate dynamic agent factory capabilities.
    """
    print("Starting Dynamic Agent Factory...")
    print("=" * 70)

    # Initialize factory
    root_agent, registry, orchestrator = create_factory_orchestrator()

    # Example 1: Create a quality monitor agent
    print("\n1. Creating Quality Monitor Agent from description...")
    quality_agent = create_agent_from_description(
        registry,
        AgentBuilder(),
        "Monitor production quality and detect defects in real-time",
        "prod-001",
    )
    print(f"   Created: {quality_agent.name}")

    # Example 2: Create a data analyst agent
    print("\n2. Creating Data Analyst Agent from description...")
    analyst_agent = create_agent_from_description(
        registry,
        AgentBuilder(),
        "Analyze sales trends and provide business insights",
        "analyst-001",
    )
    print(f"   Created: {analyst_agent.name}")

    # Example 3: Create a customer service agent
    print("\n3. Creating Customer Service Agent from description...")
    service_agent = create_agent_from_description(
        registry,
        AgentBuilder(),
        "Handle customer support inquiries and resolve issues",
        "support-001",
    )
    print(f"   Created: {service_agent.name}")

    # List all registered agents
    print("\n4. Registered Agents:")
    print("-" * 70)
    all_agents = registry.list_all()
    for agent_name, agent_info in all_agents.items():
        print(f"\n   {agent_name}:")
        print(f"      Role: {agent_info['role']}")
        print(f"      Description: {agent_info['description']}")
        print(f"      Capabilities: {', '.join(agent_info['capabilities'][:2])}...")

    # Example task routing
    print("\n5. Routing Task to Quality Monitor...")
    print("-" * 70)
    task = "Check the defect rates for today and alert if above threshold"
    result = orchestrator.route_task(task)
    print(f"   Task: {task}")
    print(f"   Agent Used: {result.get('agent')}")
    print(f"   Role: {result.get('agent_role')}")
    print(f"   Status: {result.get('status')}")

    # Example workflow coordination
    print("\n6. Coordinating Multi-Agent Workflow...")
    print("-" * 70)
    workflow = [
        {
            "task": "Analyze sales data from last week",
            "agent_role": "data_analyst",
        },
        {
            "task": "Check quality metrics",
            "agent_role": "quality_monitor",
        },
        {
            "task": "Generate executive summary",
        },
    ]

    workflow_result = orchestrator.coordinate_workflow(workflow)
    print(f"   Steps Completed: {workflow_result['steps_completed']}/{workflow_result['total_steps']}")
    print(f"   Status: {workflow_result['workflow_status']}")

    # Discover capabilities
    print("\n7. Discovering Agents by Capability...")
    print("-" * 70)
    agents_with_monitoring = orchestrator.discover_agents_for_capability("monitor_defect_rates")
    print(f"   Agents with 'monitor_defect_rates': {len(agents_with_monitoring)}")

    print("\n" + "=" * 70)
    print("Dynamic Agent Factory Demo Complete!")


if __name__ == "__main__":
    main()
