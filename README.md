# Part 6 — The Company Knowledge Base

> From the series [Google ADK: From 0 to Agentic AI](https://github.com/gazzumatteo/adk-from-zero)

Ground your agents in real data with Retrieval-Augmented Generation (RAG). Build a librarian agent that searches a knowledge base, retrieves documents, and provides answers with source attribution.

## What You'll Learn

- How to implement the RAG pattern with ADK
- How to build knowledge base search tools
- How to provide source attribution in agent responses
- How to design agents that cite their sources

## Project Structure

```
.
├── agent.py                     # Librarian agent with knowledge tools
├── main.py                      # Knowledge base search demo
├── __init__.py                  # Package initialization
├── .env.example                 # Environment variable template
├── requirements.txt             # Python dependencies
└── tools/
    └── knowledge_tools.py       # Knowledge base search, document details, categories
```

## Quick Start

```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
pip install -r requirements.txt
python main.py
```

## Previous & Next

← [Part 5: Agents That Remember](https://github.com/gazzumatteo/adk-from-zero/tree/05-memory-and-context)
→ [Part 7: The Universal Tool Protocol](https://github.com/gazzumatteo/adk-from-zero) — Integrating MCP tools for universal agent capabilities.

## Article

📖 Read the full article on Medium: *coming soon*

---

**Author:** [Matteo Gazzurelli](https://linkedin.com/in/matteogazzurelli) — Fractional CTO & Agentic AI Consultant
