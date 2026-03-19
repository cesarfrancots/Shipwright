from __future__ import annotations

import unittest

from shipwright_obsidian_mcp.config import ServerConfig
from shipwright_obsidian_mcp.templates import render_template
from shipwright_obsidian_mcp.vault import (
    HeadingResolutionError,
    NoteCollisionError,
    ShipwrightVault,
    VaultSafetyError,
)

from shipwright_obsidian_mcp.tests.helpers import make_temp_vault


class VaultTests(unittest.TestCase):
    def test_scaffold_is_idempotent(self) -> None:
        vault_path = make_temp_vault()
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        first = vault.scaffold_workspace()
        second = vault.scaffold_workspace()
        self.assertTrue(first["written_files"])
        self.assertFalse(second["written_files"])

    def test_path_traversal_is_rejected(self) -> None:
        vault_path = make_temp_vault()
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        vault.scaffold_workspace()
        with self.assertRaises(VaultSafetyError):
            vault.read_note("../outside.md")

    def test_create_read_list_and_search_notes(self) -> None:
        vault_path = make_temp_vault()
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        vault.scaffold_workspace()
        vault.create_note("01-Initiatives/Initiative - Sprint Risk Radar", "# Initiative - Sprint Risk Radar")
        note = vault.read_note("01-Initiatives/Initiative - Sprint Risk Radar")
        self.assertIn("Sprint Risk Radar", note["content"])
        listed = vault.list_notes("01-Initiatives", recursive=False)
        self.assertEqual(len(listed["notes"]), 2)
        hits = vault.search_notes("Risk Radar")
        self.assertEqual(hits["hits"][0]["match_type"], "filename")

    def test_create_collision_requires_overwrite(self) -> None:
        vault_path = make_temp_vault("collision_vault")
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        with self.assertRaises(NoteCollisionError):
            vault.create_note("01-Initiatives/Initiative - Existing", "new content")

    def test_replace_section_requires_unique_heading(self) -> None:
        vault_path = make_temp_vault()
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        vault.scaffold_workspace()
        vault.create_note("01-Initiatives/Test", "# Test\n\n## Outcome\n\nOld")
        updated = vault.update_note(
            "01-Initiatives/Test",
            mode="replace_section",
            heading="Outcome",
            content="New outcome",
        )
        self.assertEqual(updated["mode"], "replace_section")
        self.assertIn("New outcome", vault.read_note("01-Initiatives/Test")["content"])
        with self.assertRaises(HeadingResolutionError):
            vault.update_note(
                "01-Initiatives/Test",
                mode="replace_section",
                heading="Missing",
                content="Nope",
            )

    def test_ensure_indexes_avoids_duplicates(self) -> None:
        vault_path = make_temp_vault("preexisting_shipwright")
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        vault.scaffold_workspace()
        first = vault.ensure_indexes()
        second = vault.ensure_indexes()
        self.assertTrue(first["updated_files"] or first["updated_files"] == [])
        self.assertEqual(second["updated_files"], [])

    def test_unrelated_notes_are_untouched(self) -> None:
        vault_path = make_temp_vault("vault_with_unrelated")
        journal = (vault_path / "Personal" / "Journal.md").read_text(encoding="utf-8")
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        vault.scaffold_workspace()
        self.assertEqual(journal, (vault_path / "Personal" / "Journal.md").read_text(encoding="utf-8"))

    def test_link_artifacts_updates_sections(self) -> None:
        vault_path = make_temp_vault()
        vault = ShipwrightVault(ServerConfig(vault_path=vault_path))
        vault.scaffold_workspace()
        vault.create_note(
            "01-Initiatives/Initiative - Radar",
            render_template("initiative", {"title": "Radar"}),
        )
        vault.create_note(
            "02-PRDs/PRD - Radar",
            render_template("prd", {"title": "Radar", "initiative": "Initiative - Radar"}),
        )
        result = vault.link_artifacts(
            initiative_path="01-Initiatives/Initiative - Radar",
            prd_path="02-PRDs/PRD - Radar",
        )
        self.assertTrue(result["updated_files"])
        initiative = vault.read_note("01-Initiatives/Initiative - Radar")["content"]
        self.assertIn("[[PRD - Radar]]", initiative)
