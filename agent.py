"""
Order Pipeline Root Agent

Orchestrates a complete order processing pipeline using multiple agent patterns.
- SequentialAgent: Order receiver → Availability → Scheduling → QA
- ParallelAgent: Parallel enrichment for market/competitive data
- LoopAgent: Quality inspector iterates until approval
"""

from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent

from agents.order_receiver import order_receiver_agent
from agents.availability_checker import availability_checker_agent
from agents.production_scheduler import production_scheduler_agent
from agents.quality_inspector import quality_inspector_agent
from agents.parallel_enrichment import enrichment_agent


# Sequential pipeline: Each agent runs after previous completes
# This ensures order dependencies are maintained
sequential_pipeline = SequentialAgent(
    name="order_processing_pipeline",
    agents=[
        order_receiver_agent,
        availability_checker_agent,
        production_scheduler_agent,
        quality_inspector_agent,
    ],
    description="Sequential order processing from intake to scheduling",
)

# Parallel enrichment: Market and competitive analysis happens concurrently
# This enriches order context without blocking critical path
parallel_enrichment = ParallelAgent(
    name="parallel_enrichment",
    agents=[enrichment_agent],  # Can add more agents to run in parallel
    description="Concurrent enrichment of order with market/competitive data",
)

# LoopAgent pattern in quality inspector handles iterative checks
# Quality Inspector internally uses loop: Check → Pass/Fail → (Fail → Rework → Recheck)

# Root orchestrator brings everything together
root_agent = Agent(
    name="order_orchestrator",
    model="gemini-3-flash-preview",
    description="Master orchestrator for complete order processing pipeline",
    instruction="""You are the order orchestration specialist.
You oversee the complete order lifecycle:
1. Receive and validate customer order
2. Check availability and feasibility
3. Schedule production efficiently
4. Ensure quality standards
5. Enrich context with market insights

Use your teams strategically:
- Sequential agents for dependent tasks
- Parallel agents for concurrent work
- Loop agents for iterative validation

Final responsibility: Ensure order meets all criteria before fulfillment.""",
)
