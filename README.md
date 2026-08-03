# Google ADK: From 0 to Agentic AI

A hands-on, 12-part article series that walks you through building production-grade AI agents with [Google Agent Development Kit (ADK)](https://adk.dev/).

Each article has its own branch with complete, runnable code. Start from Part 1 and build your way up — or jump to any topic that interests you.

> [!NOTE]
> **2026 platform naming update:** Google ADK kept its name and code-first role. Google Cloud introduced Gemini Enterprise Agent Platform as the evolution of Vertex AI and the wider managed layer for building, scaling, governing and optimizing agents. Read [Google ADK in 2026: Where It Fits in Gemini Enterprise Agent Platform](https://gazzurelli.com/blog/google-adk-gemini-enterprise-agent-platform) for the current architecture map, including ADK Runtime versus managed Agent Runtime and the Cloud Run deployment path.

## The Series

| Part | Title | Branch | Article |
|------|-------|--------|---------|
| 01 | Your First AI Agent | [`01-hello-adk`](https://github.com/gazzumatteo/adk-from-zero/tree/01-hello-adk) | [Read on Medium](https://blog.gazzurelli.com/how-to-build-your-first-ai-agent-with-google-adk-6c5027fda111) |
| 02 | Teaching Agents to Act | [`02-tools-and-functions`](https://github.com/gazzumatteo/adk-from-zero/tree/02-tools-and-functions) | *coming soon* |
| 03 | Building Agent Teams | [`03-multi-agent-teams`](https://github.com/gazzumatteo/adk-from-zero/tree/03-multi-agent-teams) | *coming soon* |
| 04 | Visual Workflows with ADK 2.0 | [`04-adk-2-workflows`](https://github.com/gazzumatteo/adk-from-zero/tree/04-adk-2-workflows) | *coming soon* |
| 05 | Agents That Remember | [`05-memory-and-context`](https://github.com/gazzumatteo/adk-from-zero/tree/05-memory-and-context) | *coming soon* |
| 06 | The Company Knowledge Base | [`06-enterprise-rag`](https://github.com/gazzumatteo/adk-from-zero/tree/06-enterprise-rag) | *coming soon* |
| 07 | The Universal Tool Protocol | [`07-mcp-tools`](https://github.com/gazzumatteo/adk-from-zero/tree/07-mcp-tools) | *coming soon* |
| 08 | Cross-Company Agent Collaboration | [`08-a2a-protocol`](https://github.com/gazzumatteo/adk-from-zero/tree/08-a2a-protocol) | *coming soon* |
| 09 | Beyond Chat: Generative UI | [`09-a2ui-generative-ui`](https://github.com/gazzumatteo/adk-from-zero/tree/09-a2ui-generative-ui) | *coming soon* |
| 10 | Streaming Agents to Your Frontend | [`10-ag-ui-frontend`](https://github.com/gazzumatteo/adk-from-zero/tree/10-ag-ui-frontend) | *coming soon* |
| 11 | Agents That Create Agents | [`11-dynamic-agent-factory`](https://github.com/gazzumatteo/adk-from-zero/tree/11-dynamic-agent-factory) | *coming soon* |
| 12 | From Laptop to Cloud | [`12-production-deploy`](https://github.com/gazzumatteo/adk-from-zero/tree/12-production-deploy) | *coming soon* |

## Quick Start

Each branch contains a self-contained project. To run any part:

```bash
# Clone the repo
git clone https://github.com/gazzumatteo/adk-from-zero.git
cd adk-from-zero

# Switch to a specific part
git checkout 01-hello-adk

# Setup
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY (get one at https://ai.google.dev/)

# Install and run
pip install -r requirements.txt
python main.py
```

## What You'll Build

This series uses a **manufacturing company scenario** as a running example. You start with a simple receptionist agent and progressively add capabilities — tools, multi-agent orchestration, memory, RAG, protocol integrations, and production deployment — until you have a complete, enterprise-grade agentic system.

## Prerequisites

- Python 3.11+
- A Google API Key ([get one here](https://ai.google.dev/))
- Basic Python knowledge

## Tech Stack

- [Google ADK](https://adk.dev/) — Agent framework
- [Gemini](https://ai.google.dev/) — LLM backbone
- Python 3.11+

## Author

**Matteo Gazzurelli** — Fractional CTO & Agentic AI Consultant

- [gazzurelli.com](https://gazzurelli.com)
- [LinkedIn](https://linkedin.com/in/matteogazzurelli)
- [Medium](https://medium.com/@matteogazzurelli)
- [X/Twitter](https://x.com/gazzumatteo)

## License

This project is licensed under the Apache 2.0 License — see the [LICENSE](LICENSE) file for details.
