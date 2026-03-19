from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


ENV_VAULT_PATH = "SHIPWRIGHT_OBSIDIAN_VAULT_PATH"
ENV_ROOT_FOLDER = "SHIPWRIGHT_OBSIDIAN_ROOT_FOLDER"
ENV_TEMPLATES_FOLDER = "SHIPWRIGHT_OBSIDIAN_TEMPLATES_FOLDER"
ENV_TRANSPORT = "SHIPWRIGHT_OBSIDIAN_TRANSPORT"


@dataclass(frozen=True)
class ServerConfig:
    vault_path: Path
    root_folder: str = "Shipwright"
    templates_folder: str = "Templates/Shipwright"
    transport: str = "stdio"

    def __post_init__(self) -> None:
        object.__setattr__(self, "vault_path", Path(self.vault_path).expanduser().resolve())

    @property
    def root_path(self) -> Path:
        return (self.vault_path / self.root_folder).resolve()

    @property
    def templates_path(self) -> Path:
        return (self.vault_path / self.templates_folder).resolve()

    @classmethod
    def from_sources(cls, args: argparse.Namespace | None = None) -> "ServerConfig":
        args = args or argparse.Namespace()
        vault_path = getattr(args, "vault_path", None) or os.getenv(ENV_VAULT_PATH)
        if not vault_path:
            raise ValueError(
                "vault path is required via --vault-path or SHIPWRIGHT_OBSIDIAN_VAULT_PATH"
            )

        root_folder = getattr(args, "root_folder", None) or os.getenv(
            ENV_ROOT_FOLDER, "Shipwright"
        )
        templates_folder = getattr(args, "templates_folder", None) or os.getenv(
            ENV_TEMPLATES_FOLDER, "Templates/Shipwright"
        )
        transport = getattr(args, "transport", None) or os.getenv(ENV_TRANSPORT, "stdio")

        cls._validate_relative_folder(root_folder, "root_folder")
        cls._validate_relative_folder(templates_folder, "templates_folder")
        if transport not in {"stdio", "sse", "streamable-http"}:
            raise ValueError("transport must be stdio, sse, or streamable-http")

        return cls(
            vault_path=Path(vault_path).expanduser().resolve(),
            root_folder=root_folder,
            templates_folder=templates_folder,
            transport=transport,
        )

    @staticmethod
    def build_arg_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Shipwright Obsidian MCP server")
        parser.add_argument("--vault-path", help="Path to the Obsidian vault root")
        parser.add_argument(
            "--root-folder",
            default=None,
            help="Relative folder under the vault used for Shipwright notes",
        )
        parser.add_argument(
            "--templates-folder",
            default=None,
            help="Relative folder under the vault used for Shipwright templates",
        )
        parser.add_argument(
            "--transport",
            default=None,
            choices=["stdio", "sse", "streamable-http"],
            help="MCP transport to run locally",
        )
        return parser

    @staticmethod
    def _validate_relative_folder(folder: str, label: str) -> None:
        parts = PurePosixPath(folder).parts
        if not folder or folder.strip() == ".":
            raise ValueError(f"{label} must be a non-empty relative folder")
        if any(part in {"..", ""} for part in parts):
            raise ValueError(f"{label} must not contain traversal segments")
        if Path(folder).is_absolute() or PurePosixPath(folder).is_absolute():
            raise ValueError(f"{label} must be relative, not absolute")
