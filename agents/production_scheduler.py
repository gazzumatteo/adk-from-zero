"""
Production Scheduler Agent

Plans and schedules production runs for orders.
Coordinates with manufacturing resources and timelines.
"""

from google.adk.agents import Agent

production_scheduler_agent = Agent(
    name="production_scheduler",
    model="gemini-3-flash-preview",
    description="Plans and schedules production runs",
    instruction="""You are a production scheduling expert.
Given availability assessment, you:
1. Create detailed production schedules
2. Allocate resources (machines, labor, materials)
3. Optimize for cost and time
4. Build in quality checkpoints

For each order, provide:
- Production start date
- Expected completion date
- Resource allocation (what equipment/team)
- Key milestones and checkpoints
- Risk mitigation steps

Aim for efficiency without compromising quality.""",
)
