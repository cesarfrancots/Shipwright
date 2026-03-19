from __future__ import annotations

import asyncio
import unittest

from shipwright_obsidian_mcp.config import ServerConfig
from shipwright_obsidian_mcp.server import create_server

from shipwright_obsidian_mcp.tests.helpers import make_temp_vault


def structured(result):
    if isinstance(result, tuple) and len(result) == 2:
        return result[1]
    return result


class ServerToolTests(unittest.TestCase):
    def test_tool_flow_acceptance_path(self) -> None:
        vault_path = make_temp_vault("vault_with_unrelated")
        server = create_server(ServerConfig(vault_path=vault_path))

        status = structured(asyncio.run(server.call_tool("get_workspace_status", {})))
        self.assertFalse(status["scaffold_exists"])

        scaffold = structured(asyncio.run(server.call_tool("scaffold_workspace", {})))
        self.assertIn("workspace_status", scaffold)

        initiative = structured(asyncio.run(server.call_tool(
            "create_from_template",
            {
                "template_key": "initiative",
                "destination_path": "01-Initiatives/Initiative - Sprint Risk Radar",
                "variables": {"title": "Sprint Risk Radar", "owner": "PM"},
            },
        )))
        self.assertTrue(initiative["created"])

        prd = structured(asyncio.run(server.call_tool(
            "create_from_template",
            {
                "template_key": "prd",
                "destination_path": "02-PRDs/PRD - Sprint Risk Radar",
                "variables": {
                    "title": "Sprint Risk Radar",
                    "owner": "PM",
                    "initiative": "Initiative - Sprint Risk Radar",
                },
            },
        )))
        self.assertTrue(prd["created"])

        adr = structured(asyncio.run(server.call_tool(
            "create_from_template",
            {
                "template_key": "adr",
                "destination_path": "03-Decisions/ADR - Alert Threshold",
                "variables": {
                    "title": "Alert Threshold",
                    "owner": "PM",
                    "initiative": "Initiative - Sprint Risk Radar",
                    "prd": "PRD - Sprint Risk Radar",
                },
            },
        )))
        self.assertTrue(adr["created"])

        linked = structured(asyncio.run(server.call_tool(
            "link_artifacts",
            {
                "initiative_path": "01-Initiatives/Initiative - Sprint Risk Radar",
                "prd_path": "02-PRDs/PRD - Sprint Risk Radar",
                "adr_paths": ["03-Decisions/ADR - Alert Threshold"],
            },
        )))
        self.assertTrue(linked["updated_files"])

        searched = structured(asyncio.run(server.call_tool("search_notes", {"query": "Sprint Risk Radar"})))
        self.assertTrue(searched["hits"])

        read_back = structured(asyncio.run(server.call_tool(
            "read_note",
            {"path": "01-Initiatives/Initiative - Sprint Risk Radar"},
        )))
        self.assertIn("[[PRD - Sprint Risk Radar]]", read_back["content"])
