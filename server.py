"""
FastAPI server with SSE streaming endpoint for agent responses.

This server demonstrates:
- FastAPI integration with ADK agents
- Server-Sent Events for streaming
- Real-time response handling
"""

import json
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from agent import create_agent

# Create FastAPI app
app = FastAPI(
    title="AG-UI Streaming Demo",
    description="Article 10: AG-UI Frontend with Streaming",
    version="1.0.0",
)

# Initialize agent
agent = create_agent()


@app.get("/")
async def root() -> FileResponse:
    """
    Serve the main HTML frontend.
    """
    return FileResponse("frontend/index.html", media_type="text/html")


@app.post("/api/run")
async def run_agent(request_body: dict) -> StreamingResponse:
    """
    Run agent with streaming response via SSE.

    Args:
        request_body: Dictionary with 'prompt' key

    Returns:
        StreamingResponse: Server-Sent Events stream
    """
    if "prompt" not in request_body:
        raise HTTPException(status_code=400, detail="Missing 'prompt' in request body")

    prompt = request_body["prompt"]

    async def event_generator() -> AsyncGenerator[str, None]:
        """
        Generate SSE events from agent response.
        """
        try:
            # Start event
            yield f"data: {json.dumps({'type': 'start', 'message': 'Processing your request...'})}\n\n"

            # Run agent and collect response
            response = agent.run(prompt)

            # Send tool calls and reasoning (simulated for demo)
            yield f"data: {json.dumps({'type': 'tool_call', 'tool': 'thinking', 'status': 'Processing request'})}\n\n"

            # Send response in chunks (simulated streaming)
            response_text = str(response)
            chunk_size = 50

            for i in range(0, len(response_text), chunk_size):
                chunk = response_text[i : i + chunk_size]
                yield f"data: {json.dumps({'type': 'response_chunk', 'chunk': chunk})}\n\n"

            # Send completion event
            yield f"data: {json.dumps({'type': 'done', 'message': 'Processing complete'})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )


@app.get("/api/status")
async def status() -> dict:
    """
    Get server status.
    """
    return {
        "status": "running",
        "agent": agent.name,
        "model": agent.model,
    }


# Mount static files for frontend
try:
    app.mount("/static", StaticFiles(directory="frontend"), name="static")
except RuntimeError:
    # Directory may not exist in dev environments
    pass
