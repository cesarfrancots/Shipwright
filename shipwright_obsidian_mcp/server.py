from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .config import ServerConfig
from .templates import list_template_keys, render_template
from .vault import ShipwrightVault


def create_server(config: ServerConfig) -> FastMCP:
    workspace = ShipwrightVault(config)
    server = FastMCP(
        name="shipwright-obsidian",
        instructions=(
            "Use this server to read and write Shipwright-managed Obsidian notes only "
            "inside the configured Shipwright workspace folders."
        ),
    )

    @server.tool(description="Return vault path, configured folders, and scaffold status.")
    def get_workspace_status() -> dict[str, object]:
        return workspace.get_workspace_status()

    @server.tool(description="Create the Shipwright folder structure and starter notes.")
    def scaffold_workspace(overwrite: bool = False) -> dict[str, object]:
        return workspace.scaffold_workspace(overwrite=overwrite)

    @server.tool(description="List markdown notes under the Shipwright root.")
    def list_notes(folder: str = "", recursive: bool = False) -> dict[str, object]:
        return workspace.list_notes(folder=folder, recursive=recursive)

    @server.tool(description="Read a single markdown note under the Shipwright root.")
    def read_note(path: str) -> dict[str, object]:
        return workspace.read_note(path=path)

    @server.tool(description="Search Shipwright notes by filename or content.")
    def search_notes(
        query: str,
        folder: str = "",
        recursive: bool = True,
        case_sensitive: bool = False,
        max_results: int = 20,
    ) -> dict[str, object]:
        return workspace.search_notes(
            query=query,
            folder=folder,
            recursive=recursive,
            case_sensitive=case_sensitive,
            max_results=max_results,
        )

    @server.tool(description="Create a markdown note inside the Shipwright root.")
    def create_note(path: str, content: str, overwrite: bool = False) -> dict[str, object]:
        return workspace.create_note(path=path, content=content, overwrite=overwrite)

    @server.tool(
        description="Update a markdown note using append, replace_section, or replace_full."
    )
    def update_note(
        path: str,
        mode: str,
        content: str,
        heading: str | None = None,
    ) -> dict[str, object]:
        return workspace.update_note(path=path, mode=mode, content=content, heading=heading)

    @server.tool(
        description=(
            "Create a note from a named Shipwright template key. Available keys: "
            + ", ".join(list_template_keys())
        )
    )
    def create_from_template(
        template_key: str,
        destination_path: str,
        variables: dict[str, object] | None = None,
        overwrite: bool = False,
    ) -> dict[str, object]:
        content = render_template(template_key, variables=variables)
        return workspace.create_from_template(
            destination_path=destination_path,
            rendered_content=content,
            overwrite=overwrite,
        )

    @server.tool(description="Rebuild Shipwright index notes without duplicating links.")
    def ensure_indexes() -> dict[str, object]:
        return workspace.ensure_indexes()

    @server.tool(description="Link related Shipwright artifacts across initiative, PRD, ADR, sprint, release, metrics, and stakeholder notes.")
    def link_artifacts(
        initiative_path: str | None = None,
        prd_path: str | None = None,
        adr_paths: list[str] | None = None,
        sprint_path: str | None = None,
        release_note_path: str | None = None,
        metrics_plan_path: str | None = None,
        stakeholder_update_path: str | None = None,
        risk_paths: list[str] | None = None,
    ) -> dict[str, object]:
        return workspace.link_artifacts(
            initiative_path=initiative_path,
            prd_path=prd_path,
            adr_paths=adr_paths,
            sprint_path=sprint_path,
            release_note_path=release_note_path,
            metrics_plan_path=metrics_plan_path,
            stakeholder_update_path=stakeholder_update_path,
            risk_paths=risk_paths,
        )

    return server


def main() -> None:
    parser = ServerConfig.build_arg_parser()
    args = parser.parse_args()
    config = ServerConfig.from_sources(args)
    create_server(config).run(transport=config.transport)
