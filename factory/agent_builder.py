"""
Agent builder that creates agents from natural language descriptions.

This meta-agent:
- Accepts natural language descriptions of desired agents
- Generates YAML configurations
- Creates and registers agents dynamically
"""

from typing import Any

from google.adk.agents import Agent

from agent_templates import AGENT_TEMPLATES


class AgentBuilder:
    """
    Meta-agent that builds agents from natural language.

    Uses a builder agent to:
    1. Parse natural language description
    2. Determine agent role and capabilities
    3. Generate YAML configuration
    4. Create agent instance
    """

    def __init__(self) -> None:
        """Initialize the agent builder."""
        self.builder_agent = Agent(
            name="Agent-Builder",
            model="gemini-3-flash-preview",
        )

    def build_from_description(
        self,
        description: str,
    ) -> dict[str, Any]:
        """
        Build an agent configuration from natural language.

        Args:
            description: Natural language description of the desired agent

        Returns:
            Dictionary with agent configuration
        """
        # Analyze description to determine agent type
        prompt = f"""
        Based on this description, determine the best agent configuration:
        "{description}"

        Consider these agent roles:
        - quality_monitor: Monitors quality metrics and alerts
        - data_analyst: Analyzes data and provides insights
        - customer_service: Handles customer support interactions
        - inventory_manager: Manages inventory and stock levels

        Return a JSON configuration with:
        - role: The agent role
        - name: A good agent name
        - description: A refined description
        - capabilities: List of 3-5 key capabilities
        """

        response = self.builder_agent.run(prompt)

        # Parse response (in real implementation, use structured output)
        # For now, return a reasonable configuration
        return self._generate_config(description)

    def _generate_config(self, description: str) -> dict[str, Any]:
        """
        Generate configuration from description.

        Args:
            description: Agent description

        Returns:
            Configuration dictionary
        """
        # Determine role from keywords
        desc_lower = description.lower()

        if any(word in desc_lower for word in ["quality", "monitor", "defect"]):
            role = "quality_monitor"
            template = AGENT_TEMPLATES.get("quality_monitor")
        elif any(word in desc_lower for word in ["analyze", "insight", "trend"]):
            role = "data_analyst"
            template = AGENT_TEMPLATES.get("data_analyst")
        elif any(word in desc_lower for word in ["customer", "support", "service"]):
            role = "customer_service"
            template = AGENT_TEMPLATES.get("customer_service")
        elif any(word in desc_lower for word in ["inventory", "stock", "supply"]):
            role = "inventory_manager"
            template = AGENT_TEMPLATES.get("inventory_manager")
        else:
            role = "general"
            template = {"capabilities": ["analyze", "report", "recommend"]}

        return {
            "role": role,
            "description": description,
            "capabilities": template.get("capabilities", []),
            "model": "gemini-3-flash-preview",
            "temperature": 0.7,
            "tools": template.get("tools", []),
        }
