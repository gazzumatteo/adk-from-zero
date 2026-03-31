"""
Agent registry for discovery and management.

Maintains a registry of all created agents with their
capabilities, configurations, and metadata.
"""

from typing import Any

from google.adk.agents import Agent


class AgentRegistry:
    """
    Registry for managing dynamically created agents.

    Provides:
    - Agent registration and discovery
    - Capability lookup
    - Configuration management
    """

    def __init__(self) -> None:
        """Initialize the agent registry."""
        self._agents: dict[str, dict[str, Any]] = {}

    def register(
        self,
        agent: Agent,
        role: str,
        description: str,
        capabilities: list[str],
        config: dict[str, Any],
    ) -> None:
        """
        Register an agent in the registry.

        Args:
            agent: The Agent instance
            role: Role of the agent (e.g., 'quality_monitor', 'analyst')
            description: Human-readable description
            capabilities: List of capabilities
            config: Configuration dictionary
        """
        self._agents[agent.name] = {
            "agent": agent,
            "role": role,
            "description": description,
            "capabilities": capabilities,
            "config": config,
            "created_at": str(__import__("datetime").datetime.now()),
        }

    def discover(self, role: str) -> list[dict[str, Any]]:
        """
        Discover agents by role.

        Args:
            role: Role to search for

        Returns:
            List of matching agent entries
        """
        return [
            {
                "name": name,
                **entry,
            }
            for name, entry in self._agents.items()
            if entry["role"] == role
        ]

    def find_by_capability(self, capability: str) -> list[dict[str, Any]]:
        """
        Find agents with a specific capability.

        Args:
            capability: Capability to search for

        Returns:
            List of matching agent entries
        """
        return [
            {
                "name": name,
                **entry,
            }
            for name, entry in self._agents.items()
            if capability in entry["capabilities"]
        ]

    def list_all(self) -> dict[str, dict[str, Any]]:
        """
        List all registered agents.

        Returns:
            Dictionary of all agents with their metadata
        """
        return {
            name: {
                "role": entry["role"],
                "description": entry["description"],
                "capabilities": entry["capabilities"],
                "created_at": entry["created_at"],
            }
            for name, entry in self._agents.items()
        }

    def get(self, name: str) -> Agent | None:
        """
        Get an agent by name.

        Args:
            name: Agent name

        Returns:
            Agent instance or None if not found
        """
        entry = self._agents.get(name)
        return entry["agent"] if entry else None

    def get_config(self, name: str) -> dict[str, Any] | None:
        """
        Get an agent's configuration.

        Args:
            name: Agent name

        Returns:
            Configuration dictionary or None
        """
        entry = self._agents.get(name)
        return entry["config"] if entry else None
