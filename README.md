# Part 5 — Agents That Remember

> From the series [Google ADK: From 0 to Agentic AI](https://github.com/gazzumatteo/adk-from-zero)

Build agents that maintain context across conversations. Implement session management, memory banks, and context building for a customer support agent.

## What You'll Learn

- How to persist session state across conversation turns
- How to implement memory banks for long-term context
- How to build context from multiple sources
- How to design multi-turn conversational agents

## Project Structure

```
.
├── agent.py                       # Customer support agent with 3 tools
├── main.py                        # Multi-turn conversation with session management
├── __init__.py                    # Package initialization
├── .env.example                   # Environment variable template
├── requirements.txt               # Python dependencies
├── tools/
│   └── customer_tools.py          # Customer lookup, history, ticket tools
└── services/
    ├── session_config.py          # Session management
    └── memory_config.py           # Memory and context building
```

## Quick Start

```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
pip install -r requirements.txt
python main.py
```

## Previous & Next

← [Part 4: Visual Workflows with ADK 2.0](https://github.com/gazzumatteo/adk-from-zero/tree/04-adk-2-workflows)
→ [Part 6: The Company Knowledge Base](https://github.com/gazzumatteo/adk-from-zero) — Retrieval-Augmented Generation and knowledge base search.

## Article

📖 Read the full article on Medium: *coming soon*

---

**Author:** [Matteo Gazzurelli](https://linkedin.com/in/matteogazzurelli) — Fractional CTO & Agentic AI Consultant
