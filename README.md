# Part 1 — Your First AI Agent

> From the series [Google ADK: From 0 to Agentic AI](https://github.com/gazzumatteo/adk-from-zero)

Build a conversational receptionist agent in ~30 lines of code using Google ADK. This is the foundation everything else in the series builds on.

## What You'll Learn

- How to set up a Google ADK project from scratch
- The core mental model: **Runner → Agent → Events → Session**
- How to create an agent with custom instructions
- How to manage conversation state with `InMemorySessionService`
- How to test your agent with ADK's built-in web interface

## Project Structure

```
.
├── agent.py           # Agent definition — the receptionist
├── main.py            # Interactive CLI runner
├── __init__.py        # Package initialization
├── .env.example       # Environment variable template
└── requirements.txt   # Python dependencies
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

A friendly receptionist at **Acme Manufacturing** that:

- Greets visitors and understands their needs
- Directs them to the right department (Sales, Engineering, Production, HR)
- Provides general company information
- Maintains conversation context across turns

## Key Concepts

### Agent Definition (`agent.py`)

The `Agent` class is the core building block in ADK. You configure it with a name, model, description, and instructions — the LLM handles the rest.

### Session Management (`main.py`)

`InMemorySessionService` tracks conversation state so the agent remembers what was said earlier in the conversation. In later parts of the series, we'll swap this for persistent session services.

## Using ADK Web Interface

You can also test this agent with ADK's built-in web UI:

```bash
adk web
```

This launches a local web interface where you can interact with the agent visually and inspect events, session state, and more.

## Next Steps

→ [Part 2: Teaching Agents to Act](https://github.com/gazzumatteo/adk-from-zero) — Add tools and function calling to give your agent real capabilities.

## Article

📖 Read the full article on Medium: *coming soon*

---

**Author:** [Matteo Gazzurelli](https://linkedin.com/in/matteogazzurelli) — Fractional CTO & Agentic AI Consultant
