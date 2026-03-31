"""
Parallel Enrichment Agent

Demonstrates ParallelAgent pattern for concurrent data gathering.
Enriches order context with market analysis, competitor info, etc.
"""

from google.adk.agents import Agent

enrichment_agent = Agent(
    name="order_enrichment",
    model="gemini-3-flash-preview",
    description="Enriches order context with market and competitive data",
    instruction="""You are a business intelligence analyst.
For each order, gather enrichment data in parallel:
1. Market context: demand trends, market size
2. Competitive landscape: similar products, pricing
3. Risk assessment: supply chain, geopolitical factors
4. Customer insights: industry, growth potential

Using ParallelAgent pattern:
- Fetch market data concurrently
- Analyze competitive positioning
- Assess supply chain risks
- Profile customer opportunity

Provide a brief strategic summary that helps decision-making
without slowing down order processing.""",
)
