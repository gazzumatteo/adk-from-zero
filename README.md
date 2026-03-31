# Part 2 — Teaching Agents to Act

> From the series [Google ADK: From 0 to Agentic AI](https://github.com/gazzumatteo/adk-from-zero)

Give your agent real capabilities with tools and function calling. Build a procurement specialist that checks inventory, gets supplier quotes, places orders, and notifies the team — with full observability through callback hooks.

## What You'll Learn

- How to create tools with `Tool.from_function()`
- How the LLM decides which tool to call and with what arguments
- How to implement before/after callbacks for audit logging
- The tool execution lifecycle in ADK

## Project Structure

```
.
├── agent.py             # Procurement agent with 4 tools + callbacks
├── main.py              # Interactive CLI with tool demo
├── __init__.py          # Package initialization
├── .env.example         # Environment variable template
├── requirements.txt     # Python dependencies
└── tools/
    ├── __init__.py      # Tool exports
    ├── procurement.py   # 4 tool implementations
    └── callbacks.py     # Before/after execution hooks
```

## Quick Start

```bash
# 1. Setup environment
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY (get one at https://ai.google.dev/)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the agent
python main.py
```

## The Agent

A **procurement specialist** at Acme Manufacturing with 4 tools:

| Tool | Purpose |
|------|---------|
| `check_inventory` | Query current stock levels for a product |
| `get_supplier_quotes` | Get pricing from multiple suppliers |
| `place_order` | Create a purchase order with a supplier |
| `notify_team` | Send notifications about procurement status |

## Key Concepts

### Tool Definition (`agent.py`)

Tools are created from regular Python functions using `Tool.from_function()`. The LLM reads the function's name, description, and parameter types to decide when and how to call it.

### Callbacks (`tools/callbacks.py`)

Before/after callbacks hook into every tool execution, providing audit trails and logging without modifying tool logic. In production, you'd use these for metrics, alerting, and compliance.

### Mock Data (`tools/procurement.py`)

All tools use mock data for demonstration. Each function includes comments on what a real implementation would connect to (databases, APIs, ERP systems).

## Previous & Next

← [Part 1: Your First AI Agent](https://github.com/gazzumatteo/adk-from-zero/tree/01-hello-adk)
→ [Part 3: Building Agent Teams](https://github.com/gazzumatteo/adk-from-zero) — Orchestrate multiple agents working together.

## Article

📖 Read the full article on Medium: *coming soon*

---

**Author:** [Matteo Gazzurelli](https://linkedin.com/in/matteogazzurelli) — Fractional CTO & Agentic AI Consultant
