"""
Main entry point for Article 10: AG-UI Frontend with Streaming.

Usage:
    python main.py [--host 0.0.0.0] [--port 8000]

This runs a FastAPI server with:
- SSE streaming endpoint for agent responses
- Interactive HTML frontend with real-time updates
"""

import argparse
import sys

import uvicorn

from server import app


def main() -> None:
    """
    Run the FastAPI server with streaming support.
    """
    parser = argparse.ArgumentParser(
        description="Article 10: AG-UI Frontend with Streaming",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind to",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to run on",
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload on code changes",
    )

    args = parser.parse_args()

    print(f"Starting AG-UI Streaming Server...")
    print(f"Open http://localhost:{args.port} in your browser")
    print(f"Press Ctrl+C to stop\n")

    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level="info",
    )


if __name__ == "__main__":
    main()
