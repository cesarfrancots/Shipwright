from __future__ import annotations

import argparse
import os
import unittest
from pathlib import Path
from unittest.mock import patch
import uuid

from shipwright_obsidian_mcp.config import (
    ENV_ROOT_FOLDER,
    ENV_TEMPLATES_FOLDER,
    ENV_TRANSPORT,
    ENV_VAULT_PATH,
    ServerConfig,
)
from shipwright_obsidian_mcp.tests.helpers import TMP_ROOT


def _temp_dir() -> str:
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    temp_dir = TMP_ROOT / f"shipwright-config-test-{uuid.uuid4().hex}"
    temp_dir.mkdir(parents=True, exist_ok=False)
    return str(temp_dir)


class ServerConfigTests(unittest.TestCase):
    def test_cli_overrides_environment(self) -> None:
        temp_dir = _temp_dir()
        with patch.dict(
            os.environ,
            {
                ENV_VAULT_PATH: "C:/ignored",
                ENV_ROOT_FOLDER: "IgnoredRoot",
                ENV_TEMPLATES_FOLDER: "IgnoredTemplates/Shipwright",
                ENV_TRANSPORT: "sse",
            },
            clear=False,
        ):
            args = argparse.Namespace(
                vault_path=temp_dir,
                root_folder="Shipwright",
                templates_folder="Templates/Shipwright",
                transport="stdio",
            )
            config = ServerConfig.from_sources(args)
            self.assertEqual(config.vault_path, Path(temp_dir).resolve())
            self.assertEqual(config.root_folder, "Shipwright")
            self.assertEqual(config.transport, "stdio")

    def test_env_used_when_cli_missing(self) -> None:
        temp_dir = _temp_dir()
        with patch.dict(
            os.environ,
            {
                ENV_VAULT_PATH: temp_dir,
                ENV_ROOT_FOLDER: "Shipwright",
                ENV_TEMPLATES_FOLDER: "Templates/Shipwright",
                ENV_TRANSPORT: "stdio",
            },
            clear=False,
        ):
            config = ServerConfig.from_sources(argparse.Namespace())
            self.assertEqual(config.vault_path, Path(temp_dir).resolve())
            self.assertEqual(config.templates_folder, "Templates/Shipwright")

    def test_invalid_relative_folder_rejected(self) -> None:
        temp_dir = _temp_dir()
        args = argparse.Namespace(
            vault_path=temp_dir,
            root_folder="../escape",
            templates_folder="Templates/Shipwright",
            transport="stdio",
        )
        with self.assertRaises(ValueError):
            ServerConfig.from_sources(args)
