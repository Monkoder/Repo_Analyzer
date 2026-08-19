"""API Endpoints & Router Module

Purpose:
    Defines the APIRouter and handles incoming HTTP requests for health checks,
    metadata discovery, repository analysis, and interactive architectural Q&A.
"""
import time
from datetime import datetime,timezone
from fastapi import APIRouter, status
from app.core.config import settings
from app.schemas import (
    HealthResponse,
    HealthStatusEnum,
    ModuleCapability,
    SystemInfoResponse,
)

SERVER_START_TIME= time.time()
router=APIRouter()

@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Service Health Check",
    description="Returns the runtime operational health, semantic version, and uptime.",
    tags=["system diagnostics"],
)
async def get_health_status() -> HealthResponse:
    """ Returns Operational metrics and uptime for container health probes """
    current_time=time.time()
    uptime = round(current_time - SERVER_START_TIME, 2)

    return HealthResponse(
        status=HealthStatusEnum.HEALTHY,
        app_name=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
        timestamp=datetime.now(timezone.utc),
        uptime_seconds=uptime,
    )

@router.get(
    "/info",
    response_model=SystemInfoResponse,
    status_code=status.HTTP_200_OK,
    summary="System Capabilities & Metadata",
    description="Provides an overview of supported tech ecosystems and architectural engine capabilities. ",
    tags=["system Diagnostics"],
)

async def get_system_info() -> SystemInfoResponse:
    """Returns repo analyzer capabilities and roadmap sprint mileston."""
    supported_ecosystems = [
        "Node.js (package.json, pnpm, yarn, turbo)",
        "Python (requirements.txt, pyproject.toml, Pipfile)",
        "Go (go.mod)",
        "Rust (Cargo.toml)",
        "Java (pom.xml, build.gradle)",
        "Docker & Compose (Dockerfile, docker-compose.yml)",
        "Kubernetes & Terraform (k8s/*.yaml, *.tf)",
    ]

    roadmap_sprints = [
        ModuleCapability(
            name="FastAPI Core & Swagger UI",
            sprint=1,
            status="ACTIVE",
            description="High-performance async ASGI server, CORS, Pydantic v2 schemas, and interactive OpenAPI documentation.",
        ),
        ModuleCapability(
            name="HMAC-SHA256 Security Engine",
            sprint=2,
            status="PLANNED",
            description="Cryptographic request signature validation, timing-attack prevention, and commit-tree fingerprinting.",
        ),
        ModuleCapability(
            name="GitHub Ingestion Service",
            sprint=3,
            status="PLANNED",
            description="Asynchronous recursive Git tree extraction and selective manifest file download via GitHub REST API.",
        ),
        ModuleCapability(
            name="Tech Stack Parser",
            sprint=4,
            status="PLANNED",
            description="Multi-ecosystem dependency classification across 10 architectural categories.",
        ),
        ModuleCapability(
            name="Architecture & Paradigm Classifier",
            sprint=5,
            status="PLANNED",
            description="Directory pattern analysis identifying Clean Architecture, MVC, Microservices, and Monorepos.",
        ),
        ModuleCapability(
            name="Route & Schema Extractor",
            sprint=6,
            status="PLANNED",
            description="API catalog generator and ORM/SQL entity-relationship schema extractor.",
        ),
        ModuleCapability(
            name="Flaw & Anti-Pattern Detector",
            sprint=7,
            status="PLANNED",
            description="Static heuristic engine flagging Single Points of Failure, blocking I/O, security smells, and DB indexing flaws.",
        ),
        ModuleCapability(
            name="Actionable Remediation Engine",
            sprint=8,
            status="PLANNED",
            description="Before/After code refactoring snippet generator, health score computation, and technical debt index.",
        ),
        ModuleCapability(
            name="AI System Design Synthesizer",
            sprint=9,
            status="PLANNED",
            description="LLM-powered High-Level Design (HLD) & Low-Level Design (LLD) narrative generator and interactive Q&A.",
        ),
        ModuleCapability(
            name="Mermaid C4 Diagram Synthesizer",
            sprint=10,
            status="PLANNED",
            description="Automatic generation of C4 Context/Container/Component, Sequence, and ER Mermaid diagrams.",
        ),
    ]
    return SystemInfoResponse(
        project_name=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.VERSION,
        docs_url="/docs",
        supported_ecosystems=supported_ecosystems,
        roadmap_sprints=roadmap_sprints,
        server_time_utc=datetime.now(timezone.utc),
    )