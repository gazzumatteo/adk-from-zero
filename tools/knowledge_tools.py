"""
Knowledge Base Search Tools

Custom tools for searching enterprise knowledge base.
Wraps Vertex AI Search for semantic document retrieval.
"""

from typing import Any, Optional


def search_knowledge_base(
    query: str, max_results: int = 5, confidence_threshold: float = 0.5
) -> dict[str, Any]:
    """
    Search the company knowledge base using semantic search.

    Args:
        query: Search query (natural language)
        max_results: Maximum number of results to return
        confidence_threshold: Minimum confidence score for results

    Returns:
        Dictionary with search results including documents and confidence scores.

    In production, this integrates with Vertex AI Search to:
    - Perform semantic similarity search
    - Return relevant documents from knowledge base
    - Include confidence scores for ranking
    - Handle complex queries and entity recognition
    """
    # Mock knowledge base for demonstration
    knowledge_base = {
        "company_policies": [
            {
                "id": "POL-001",
                "title": "Remote Work Policy",
                "content": """
                Employees may work remotely up to 3 days per week.
                Remote work requires manager approval.
                Must maintain regular communication with team.
                """,
                "category": "HR",
                "last_updated": "2024-01-15",
            },
            {
                "id": "POL-002",
                "title": "Data Security Policy",
                "content": """
                All company data must be encrypted at rest and in transit.
                Two-factor authentication required for all systems.
                Quarterly security training mandatory for all staff.
                """,
                "category": "IT",
                "last_updated": "2024-02-01",
            },
        ],
        "technical_docs": [
            {
                "id": "DOC-001",
                "title": "System Architecture Overview",
                "content": """
                Our system uses microservices architecture with:
                - API Gateway for routing
                - Multiple service clusters
                - PostgreSQL for data storage
                - Redis for caching
                - Kubernetes for orchestration
                """,
                "category": "Engineering",
                "last_updated": "2024-03-01",
            },
            {
                "id": "DOC-002",
                "title": "API Documentation",
                "content": """
                REST API endpoints for all services.
                Rate limiting: 1000 requests per minute per API key.
                All requests must include authentication header.
                Response format: JSON
                """,
                "category": "Engineering",
                "last_updated": "2024-03-10",
            },
        ],
        "best_practices": [
            {
                "id": "BP-001",
                "title": "Code Review Guidelines",
                "content": """
                All code must be reviewed before merging.
                Minimum 2 reviewers required for production code.
                Comments must explain WHY, not WHAT.
                Automated tests must pass before review.
                """,
                "category": "Development",
                "last_updated": "2024-02-15",
            },
        ],
    }

    # Flatten all documents for search
    all_documents = []
    for category_docs in knowledge_base.values():
        all_documents.extend(category_docs)

    # Simple keyword matching (production would use semantic search)
    query_lower = query.lower()
    results = []

    for doc in all_documents:
        title_match = query_lower in doc["title"].lower()
        content_match = query_lower in doc["content"].lower()
        category_match = query_lower in doc["category"].lower()

        if title_match or content_match or category_match:
            # Score based on match type
            score = 0.9 if title_match else (0.7 if content_match else 0.5)

            if score >= confidence_threshold:
                results.append(
                    {
                        "document_id": doc["id"],
                        "title": doc["title"],
                        "excerpt": doc["content"][:200] + "...",
                        "category": doc["category"],
                        "confidence": score,
                        "last_updated": doc["last_updated"],
                    }
                )

    # Sort by confidence and limit results
    results.sort(key=lambda x: x["confidence"], reverse=True)
    results = results[:max_results]

    return {
        "query": query,
        "results_found": len(results),
        "results": results,
        "total_in_knowledge_base": len(all_documents),
    }


def get_document_details(document_id: str) -> dict[str, Any]:
    """
    Get full details of a specific document.

    Args:
        document_id: Document identifier

    Returns:
        Dictionary with full document content and metadata.

    Used when user needs the complete text of a referenced document.
    """
    # Mock document store
    documents = {
        "POL-001": {
            "title": "Remote Work Policy",
            "content": """
            REMOTE WORK POLICY

            1. ELIGIBILITY
            - Open to employees at level 3 and above
            - Manager approval required
            - Trial period of 30 days recommended

            2. WORK SCHEDULE
            - Up to 3 days per week remote
            - Must coordinate with team schedule
            - Core hours: 10 AM - 3 PM

            3. EQUIPMENT
            - Company provides laptop and peripherals
            - Internet must be broadband (min 50 Mbps)
            - VPN required for all connections

            4. PERFORMANCE EXPECTATIONS
            - Same productivity expectations as office
            - Regular check-ins with manager
            - Availability for team meetings

            5. LOCATION RESTRICTIONS
            - Must be within country
            - Cannot work from client offices without approval
            """,
            "category": "HR",
            "version": "2.1",
            "effective_date": "2024-01-15",
        },
    }

    if document_id not in documents:
        return {
            "found": False,
            "error": f"Document {document_id} not found",
        }

    doc = documents[document_id]
    return {
        "found": True,
        "document_id": document_id,
        "title": doc["title"],
        "category": doc["category"],
        "content": doc["content"],
        "version": doc["version"],
        "effective_date": doc["effective_date"],
    }


def list_knowledge_categories() -> dict[str, Any]:
    """
    List all available knowledge base categories.

    Returns:
        Dictionary with available categories and document counts.

    Helps users understand what information is available.
    """
    categories = {
        "HR": {
            "count": 5,
            "description": "Human Resources policies and procedures",
        },
        "IT": {
            "count": 8,
            "description": "Information Technology and security policies",
        },
        "Engineering": {
            "count": 12,
            "description": "Technical documentation and architecture",
        },
        "Development": {
            "count": 10,
            "description": "Development best practices and guidelines",
        },
        "Finance": {
            "count": 7,
            "description": "Financial policies and procedures",
        },
    }

    return {
        "total_categories": len(categories),
        "categories": categories,
    }
