# Part 3 — Building Agent Teams

> From the series [Google ADK: From 0 to Agentic AI](https://github.com/gazzumatteo/adk-from-zero)

Orchestrate multiple specialized agents working together. Build an order processing pipeline using Sequential, Parallel, and Loop agent patterns.

## What You'll Learn

- How to compose agents with `SequentialAgent`, `ParallelAgent`, and `LoopAgent`
- How to design agent teams with clear responsibilities
- How to build complex workflows from simple agent building blocks

## Project Structure

```
.
├── agent.py                        # Root orchestrator with agent composition
├── main.py                         # Demo of Sequential/Parallel/Loop patterns
├── __init__.py                     # Package initialization
├── .env.example                    # Environment variable template
├── requirements.txt                # Python dependencies
└── agents/
    ├── __init__.py                 # Agent exports
    ├── order_receiver.py           # Order intake agent
    ├── availability_checker.py     # Feasibility checker
    ├── production_scheduler.py     # Production planner
    ├── quality_inspector.py        # QA validation (LoopAgent)
    └── parallel_enrichment.py      # Market analysis (ParallelAgent)
```

## Quick Start

```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
pip install -r requirements.txt
python main.py
```

## The Agents

5 specialized agents coordinating an order processing pipeline:

| Agent | Pattern | Role |
|-------|---------|------|
| Order Receiver | Sequential | Intake and validation |
| Availability Checker | Sequential | Feasibility assessment |
| Production Scheduler | Sequential | Production planning |
| Quality Inspector | Loop | Iterative QA validation |
| Parallel Enrichment | Parallel | Concurrent market analysis |

## Previous & Next

← [Part 2: Teaching Agents to Act](https://github.com/gazzumatteo/adk-from-zero/tree/02-tools-and-functions)
→ [Part 4: Visual Workflows with ADK 2.0](https://github.com/gazzumatteo/adk-from-zero) — Declarative YAML configuration and workflow graphs.

## Article

📖 Read the full article on Medium: *coming soon*

---

**Author:** [Matteo Gazzurelli](https://linkedin.com/in/matteogazzurelli) — Fractional CTO & Agentic AI Consultant
