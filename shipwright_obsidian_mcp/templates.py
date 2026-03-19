from __future__ import annotations

from datetime import date
from importlib.resources import files
import re


PACKAGE = "shipwright_obsidian_mcp"
TEMPLATE_FILES = {
    "initiative": "initiative.md",
    "prd": "prd.md",
    "adr": "adr.md",
    "research-note": "research-note.md",
    "sprint-plan": "sprint-plan.md",
    "release-note": "release-note.md",
    "metrics-plan": "metrics-plan.md",
    "stakeholder-update": "stakeholder-update.md",
    "daily-log": "daily-log.md",
}
STARTER_FILES = {
    "00-Hub/Shipwright Hub.md": "starter_notes/shipwright_hub.md",
    "01-Initiatives/Initiatives Index.md": "starter_notes/initiatives_index.md",
    "02-PRDs/PRD Index.md": "starter_notes/prd_index.md",
    "03-Decisions/Decision Log.md": "starter_notes/decision_log.md",
    "05-Sprints/Sprint Board.md": "starter_notes/sprint_board.md",
    "06-Releases/Release Notes Index.md": "starter_notes/release_notes_index.md",
    "07-Metrics/Metrics Dashboard.md": "starter_notes/metrics_dashboard.md",
    "09-Risks/Risk Register.md": "starter_notes/risk_register.md",
}
WORKSPACE_SUBFOLDERS = [
    "00-Hub",
    "01-Initiatives",
    "02-PRDs",
    "03-Decisions",
    "04-Research",
    "05-Sprints",
    "06-Releases",
    "07-Metrics",
    "08-Stakeholders",
    "09-Risks",
    "10-Archive",
]


class UnknownTemplateKeyError(KeyError):
    pass


def list_template_keys() -> list[str]:
    return sorted(TEMPLATE_FILES)


def render_template(template_key: str, variables: dict[str, object] | None = None) -> str:
    variables = {k: str(v) for k, v in (variables or {}).items()}
    if template_key not in TEMPLATE_FILES:
        raise UnknownTemplateKeyError(template_key)

    content = _read_asset(f"templates/{TEMPLATE_FILES[template_key]}")
    merged = {
        "today": date.today().isoformat(),
        "title": variables.get("title", ""),
        "owner": variables.get("owner", ""),
        "initiative": variables.get("initiative", ""),
        "prd": variables.get("prd", ""),
        "sprint": variables.get("sprint", ""),
        "tags": variables.get("tags", ""),
    }
    merged.update(variables)

    def replace(match: re.Match[str]) -> str:
        key = match.group(1).strip()
        return merged.get(key, "")

    return re.sub(r"\{\{\s*([^}]+)\s*\}\}", replace, content)


def starter_note_contents(root_folder: str) -> dict[str, str]:
    return {
        f"{root_folder}/{path}": _read_asset(asset_path) for path, asset_path in STARTER_FILES.items()
    }


def workspace_folders(root_folder: str, templates_folder: str) -> list[str]:
    return [f"{root_folder}/{folder}" for folder in WORKSPACE_SUBFOLDERS] + [templates_folder]


def _read_asset(relative_path: str) -> str:
    return files(PACKAGE).joinpath("assets").joinpath(relative_path).read_text(encoding="utf-8")
