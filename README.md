# Part 4 — Visual Workflows with ADK 2.0

> From the series [Google ADK: From 0 to Agentic AI](https://github.com/gazzumatteo/adk-from-zero)

Move from code-defined agents to declarative YAML configuration. Define agents and workflow graphs with conditional branching — no Python required.

## What You'll Learn

- How to define agents in YAML configuration files
- How to build workflow graphs with nodes and edges
- How to implement conditional branching logic
- How to separate agent configuration from code

## Project Structure

```
.
├── agent.py                              # YAML-based agent loader
├── main.py                               # Demonstrates YAML config loading
├── __init__.py                           # Package initialization
├── .env.example                          # Environment variable template
├── requirements.txt                      # Python dependencies
└── configs/
    ├── planning_agent.yaml               # Agent configuration
    └── availability_workflow.yaml         # Workflow graph with branching
```

## Quick Start

```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
pip install -r requirements.txt
python main.py
```

## Previous & Next

← [Part 3: Building Agent Teams](https://github.com/gazzumatteo/adk-from-zero/tree/03-multi-agent-teams)
→ [Part 5: Agents That Remember](https://github.com/gazzumatteo/adk-from-zero) — Session management, memory persistence, and context building.

## Article

📖 Read the full article on Medium: *coming soon*

---

**Author:** [Matteo Gazzurelli](https://linkedin.com/in/matteogazzurelli) — Fractional CTO & Agentic AI Consultant
