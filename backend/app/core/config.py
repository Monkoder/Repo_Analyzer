"""Global Configuration Module

Purpose:
    Defines the Pydantic Settings class to load and validate environment variables
    from the .env file (e.g. project name, API prefixes, secrets, rate-limit thresholds).
"""
from functools import lru_cache
from typing import List, Literal
from pydantic import Field
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    """app settings with runtime env validation"""
    model_config= SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    PROJECT_NAME: str=Field(
        default="Repo_Analyzer Backend",
        description="Name of the backend service",
    )
    PROJECT_DESCRIPTION: str= Field(
        default="Automated GitHub Repository System Design, Flaw Detection, and Architecture Synthesis Engine.",
        description="Description shown in Swagger API documentation",
    )
    VERSION: str=Field(
        default="1.0.0",
        description="current semantic Version"
    )
    API_V1_STR: str=Field(
        default="/api/v1",
        description="Global prefix for version 1 API endpoints",
    )

    #server runtime config
    ENVIRONMENT: Literal["development","staging","production"] = Field(
        default="development",
        description="exec env tier",
    )
    DEBUG: bool = Field(
        default=True,
        descrition="Enable debug logs and auto reload"
    )
    HOST: str = Field(
        default="127.0.0.1",
        description="host IP to bind asgi server to"
    )
    PORT: int = Field(
        default=8000,
        description="Port no. to listen for incoming HTTP connections",
    )

    #security & CORS settings
    CORS_ORIGINS: List[str] = Field(
        default=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        description="permitted cross-origin resource sharing (CORS) origins",
    )
    SECRET_KEY: str = Field(
        default="super-secret-default-key-change-in-production-min32chars",
        description="Master secret used for cryptographic signing and HMAC operations",
    )

    #github ingestion limits
    GITHUB_MAX_FILE_SIZE_BYTES: int = Field(
        default=1_048_576, #1mb limit/manifest
        description="Maximum File size in bytes to fetch from Git tree"
    )
    GITHUB_REQUEST_TIMEOUT_SECONDS: int = Field(
        default=15.0,
        description="HTTP request timeout for external git api calls",
    )

@lru_cache 
def get_settings() -> Settings:
    """Returns a cached singleton instance of application settings."""
    return Settings()

settings = get_settings()