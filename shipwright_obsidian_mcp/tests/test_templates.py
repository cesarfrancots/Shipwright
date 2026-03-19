from __future__ import annotations

import unittest

from shipwright_obsidian_mcp.templates import (
    list_template_keys,
    render_template,
    starter_note_contents,
    workspace_folders,
)


class TemplateTests(unittest.TestCase):
    def test_all_expected_template_keys_exist(self) -> None:
        self.assertEqual(
            list_template_keys(),
            [
                "adr",
                "daily-log",
                "initiative",
                "metrics-plan",
                "prd",
                "release-note",
                "research-note",
                "sprint-plan",
                "stakeholder-update",
            ],
        )

    def test_render_template_replaces_title(self) -> None:
        content = render_template("initiative", {"title": "Sprint Risk Radar", "owner": "PM"})
        self.assertIn("# Initiative - Sprint Risk Radar", content)
        self.assertIn("owner: PM", content)

    def test_starter_notes_and_folders_exist(self) -> None:
        starters = starter_note_contents("Shipwright")
        self.assertIn("Shipwright/00-Hub/Shipwright Hub.md", starters)
        self.assertIn("Templates/Shipwright", workspace_folders("Shipwright", "Templates/Shipwright"))
