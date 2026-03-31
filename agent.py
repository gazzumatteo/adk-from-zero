"""
Declarative Agent Configuration with YAML

Demonstrates ADK 2.0 workflow capabilities.
Agents are defined in YAML files, loaded at runtime.
This approach separates agent logic from code configuration.
"""

import os
import yaml
from pathlib import Path
from google.adk.agents import Agent


def load_agent_from_yaml(yaml_path: str) -> Agent:
    """
    Load and instantiate an agent from YAML configuration.

    Args:
        yaml_path: Path to YAML configuration file

    Returns:
        Configured Agent instance

    This pattern allows agents to be deployed and modified without
    changing code, enabling flexible agent management.
    """
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)

    agent_config = config.get("agent", {})

    # Create agent from YAML configuration
    agent = Agent(
        name=agent_config.get("name", "unnamed_agent"),
        model=agent_config.get("model", "gemini-3-flash-preview"),
        description=agent_config.get("description", ""),
        instruction=agent_config.get("system_instruction", ""),
    )

    return agent


def load_workflow_from_yaml(yaml_path: str) -> dict:
    """
    Load workflow definition from YAML.

    Args:
        yaml_path: Path to YAML workflow file

    Returns:
        Workflow configuration dictionary

    Workflow YAML files define:
    - Graph structure (nodes and edges)
    - Conditional branching logic
    - Sub-agent definitions
    - Execution parameters
    """
    with open(yaml_path, "r") as f:
        workflow = yaml.safe_load(f)

    return workflow


# Get config directory
config_dir = Path(__file__).parent / "configs"

# Load the planning agent from YAML
# This demonstrates declarative agent configuration
planning_agent_path = config_dir / "planning_agent.yaml"
root_agent = load_agent_from_yaml(str(planning_agent_path))

# Load the availability workflow configuration
# This defines a complex multi-agent workflow with conditional logic
workflow_path = config_dir / "availability_workflow.yaml"
availability_workflow = load_workflow_from_yaml(str(workflow_path))
