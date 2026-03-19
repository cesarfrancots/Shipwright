"""Shipwright Obsidian MCP server package."""

from .config import ServerConfig
from .server import create_server

__all__ = ["ServerConfig", "create_server"]
