"""
Dynamic orchestrator for coordinating multiple agents.

This component:
- Discovers available agents
- Routes tasks to appropriate agents
- Coordinates multi-agent workflows
"""

from typing import Any

from google.adk.agents import Agent

from agent_registry import AgentRegistry


class DynamicOrchestrator:
    """
    Orchestrates coordination between dynamically created agents.

    Provides:
    - Task routing to appropriate agents
    - Multi-agent workflow coordination
    - Result aggregation
    """

    def __init__(self, registry: AgentRegistry) -> None:
        """
        Initialize the orchestrator.

        Args:
            registry: AgentRegistry instance for agent lookup
        """
        self.registry = registry
        self.orchestrator_agent = Agent(
            name="Orchestrator",
            model="gemini-3-flash-preview",
        )

    def route_task(self, task: str) -> dict[str, Any]:
        """
        Route a task to the most appropriate agent.

        Args:
            task: Task description

        Returns:
            Dictionary with result and agent used
        """
        # Find best agent for task
        agents = self.registry.list_all()

        if not agents:
            return {
                "status": "error",
                "message": "No agents available",
            }

        # Simple routing: use first agent with matching capability
        for agent_name, agent_info in agents.items():
            agent = self.registry.get(agent_name)
            if agent:
                try:
                    result = agent.run(task)
                    return {
                        "status": "success",
                        "agent": agent_name,
                        "agent_role": agent_info["role"],
                        "result": result,
                    }
                except Exception as e:
                    continue

        return {
            "status": "error",
            "message": "Could not execute task with available agents",
        }

    def coordinate_workflow(
        self,
        workflow: list[dict[str, str]],
    ) -> dict[str, Any]:
        """
        Coordinate a multi-step workflow across agents.

        Args:
            workflow: List of workflow steps with 'task' and optional 'agent_role'

        Returns:
            Dictionary with workflow results
        """
        results = []

        for step in workflow:
            task = step.get("task")
            agent_role = step.get("agent_role")

            # Find agent for this step
            if agent_role:
                agents = self.registry.discover(agent_role)
                if agents:
                    agent = self.registry.get(agents[0]["name"])
                else:
                    result = {"status": "error", "message": f"No agent with role {agent_role}"}
                    results.append(result)
                    continue
            else:
                # Use any available agent
                all_agents = list(self.registry.list_all().keys())
                if all_agents:
                    agent = self.registry.get(all_agents[0])
                else:
                    result = {"status": "error", "message": "No agents available"}
                    results.append(result)
                    continue

            # Execute step
            try:
                step_result = agent.run(task)
                results.append(
                    {
                        "status": "success",
                        "step": task[:50] + "..." if len(task) > 50 else task,
                        "result": step_result,
                    }
                )
            except Exception as e:
                results.append(
                    {
                        "status": "error",
                        "step": task[:50] + "...",
                        "error": str(e),
                    }
                )

        return {
            "workflow_status": "complete",
            "steps_completed": len([r for r in results if r["status"] == "success"]),
            "total_steps": len(workflow),
            "results": results,
        }

    def discover_agents_for_capability(
        self,
        capability: str,
    ) -> list[dict[str, Any]]:
        """
        Discover agents with a specific capability.

        Args:
            capability: Capability to search for

        Returns:
            List of matching agents
        """
        return self.registry.find_by_capability(capability)
