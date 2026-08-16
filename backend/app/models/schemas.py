"""Pydantic Request & Response Schemas Module

Purpose:
    Defines strict type schemas for request validation and response serialization across
    all API endpoints (e.g. HealthResponse, RepoMetadata, TechStack, FlawReport, SystemDesignSpec).
"""
from datetime import datetime, timezone
from enum import Enum
from typing import Any , Dict, List , Optional
from pydantic import BaseModel, Field

class HealthStatusEnum(str,Enum):
    HEALTHY="healthy"
    DEGRADED="degraded"
    UNHEALTHY="unhealthy"

class HealthResponse(BaseModel):
    status: HealthStatusEnum = Field(
        default=HealthStatusEnum.HEALTHY,
        description="Overall service operational health status",
        examples=[HealthStatusEnum.HEALTHY],
    )
    app_name: str = Field(
        description="service application name",
        examples=["Repo_Analyzer Backend"],
    
    )
    version: str = Field(
        description="semantic application version",
        examples=["1.0.0"],

    )
    environment: str = Field(
        description="current execution environment",
        examples=["development"],
    )
    timestamp: datetime = Field(
        default_factory= lambda: datetime.now(timezone.utc),
        description="UTC timestamp when the health check was performed",
    )
    uptime_seconds: Optional[float]=Field(
        default=None,
        description="seconds elapsed since server startup",
        examples=[142.5],
    )

class ModuleCapability(BaseModel):
    """schema representing an individual engine/sprint capacity."""
    name: str =Field(description="engine or module name")
    sprint: int = Field(description="operational status (ACTIVE,IN_PROGRESS,PLANNED)")
    status: str = Field(description="brief overview of module functionality")
class SystemInfoResponse(BaseModel):
    """Structured response schema describing system capabilities and metadata."""
    project_name: str = Field(description="name of the project")
    description:str = Field(description="Project Description")
    version:str = Field(description="current release version")
    docs_url:str = Field(description="Relative URL to the OpenAPI documentation")
    supported_ecosystems:List[str]=Field(description="Programming languages and packaging formats supported by analyzer")
    roadmap_sprints: List[ModuleCapability]=Field(description="summary of the architecture capabilities")
    server_time_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="current UTC server time",
    )
class ErrorDetail(BaseModel):
    """Standardized error item detailing an issue."""
    code: str = Field(description="Unique machine-readable error code")
    message: str = Field(description="Human-readable explanation of the error")
    location: Optional[str] = Field(
        default=None,
        description="location of the error (eg. query param, header, body field)",
    )
class StandardErrorResponse(BaseModel):
    """unified error envelope returned for API failures."""
    
    success: bool = Field(
        default=False,
        description="indicates wether the request succeeded",
    )
    errors: List[ErrorDetail] = Field(
        description="List of error details explaining why the request failed"
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="UTC timestamp of the error occurence",
    )