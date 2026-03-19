from __future__ import annotations

from dataclasses import asdict
from pathlib import Path, PurePosixPath
import re
from typing import Iterable

from .config import ServerConfig
from .models import NoteSummary, SearchHit, WorkspaceStatus
from .templates import starter_note_contents, workspace_folders


AUTOGEN_START = "<!-- SHIPWRIGHT:AUTOGEN START -->"
AUTOGEN_END = "<!-- SHIPWRIGHT:AUTOGEN END -->"


class VaultError(Exception):
    pass


class VaultSafetyError(VaultError):
    pass


class NoteCollisionError(VaultError):
    pass


class HeadingResolutionError(VaultError):
    pass


class ShipwrightVault:
    def __init__(self, config: ServerConfig):
        self.config = config

    def get_workspace_status(self) -> dict[str, object]:
        status = WorkspaceStatus(
            vault_path=str(self.config.vault_path),
            root_folder=self.config.root_folder,
            templates_folder=self.config.templates_folder,
            scaffold_exists=self.config.root_path.exists() and self.config.templates_path.exists(),
        )
        return status.to_dict()

    def scaffold_workspace(self, overwrite: bool = False) -> dict[str, object]:
        created_folders: list[str] = []
        written_files: list[str] = []

        self.config.vault_path.mkdir(parents=True, exist_ok=True)
        for folder in workspace_folders(self.config.root_folder, self.config.templates_folder):
            full_path = self._resolve_workspace_relative(folder)
            if not full_path.exists():
                full_path.mkdir(parents=True, exist_ok=True)
                created_folders.append(str(full_path.relative_to(self.config.vault_path)).replace("\\", "/"))

        for relative_path, content in starter_note_contents(self.config.root_folder).items():
            target = self._resolve_workspace_relative(relative_path)
            if target.exists() and not overwrite:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            written_files.append(str(target.relative_to(self.config.vault_path)).replace("\\", "/"))

        return {
            "created_folders": created_folders,
            "written_files": written_files,
            "workspace_status": self.get_workspace_status(),
        }

    def list_notes(self, folder: str = "", recursive: bool = False) -> dict[str, object]:
        base = self._resolve_root_relative(folder) if folder else self.config.root_path
        iterator = base.rglob("*.md") if recursive else base.glob("*.md")
        notes = [
            NoteSummary(
                path=self._as_vault_relative(path),
                title=self._title_for_path(path),
            ).to_dict()
            for path in sorted(iterator)
            if path.is_file()
        ]
        return {"notes": notes}

    def read_note(self, path: str) -> dict[str, object]:
        note_path = self._resolve_root_relative(path, ensure_md=True)
        if not note_path.is_file():
            raise FileNotFoundError(path)
        content = note_path.read_text(encoding="utf-8")
        return {
            "path": self._as_vault_relative(note_path),
            "title": self._title_for_path(note_path),
            "content": content,
        }

    def search_notes(
        self,
        query: str,
        folder: str = "",
        recursive: bool = True,
        case_sensitive: bool = False,
        max_results: int = 20,
    ) -> dict[str, object]:
        if not query.strip():
            raise ValueError("query must be non-empty")

        base = self._resolve_root_relative(folder) if folder else self.config.root_path
        iterator = base.rglob("*.md") if recursive else base.glob("*.md")
        query_cmp = query if case_sensitive else query.lower()
        hits: list[dict[str, str]] = []

        for path in sorted(iterator):
            if not path.is_file():
                continue
            rel_path = self._as_vault_relative(path)
            stem = path.stem
            haystack_name = stem if case_sensitive else stem.lower()
            content = path.read_text(encoding="utf-8")
            haystack_content = content if case_sensitive else content.lower()
            match_type = None
            snippet = ""
            if query_cmp in haystack_name:
                match_type = "filename"
                snippet = stem
            else:
                index = haystack_content.find(query_cmp)
                if index >= 0:
                    match_type = "content"
                    start = max(0, index - 60)
                    end = min(len(content), index + len(query) + 60)
                    snippet = content[start:end].replace("\n", " ").strip()
            if match_type:
                hits.append(
                    SearchHit(
                        path=rel_path,
                        title=stem,
                        match_type=match_type,
                        snippet=snippet,
                    ).to_dict()
                )
            if len(hits) >= max_results:
                break
        return {"hits": hits}

    def create_note(self, path: str, content: str, overwrite: bool = False) -> dict[str, object]:
        note_path = self._resolve_root_relative(path, ensure_md=True)
        if note_path.exists() and not overwrite:
            raise NoteCollisionError(f"note already exists: {path}")
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(content, encoding="utf-8")
        return {"path": self._as_vault_relative(note_path), "created": True}

    def update_note(
        self,
        path: str,
        mode: str,
        content: str,
        heading: str | None = None,
    ) -> dict[str, object]:
        note_path = self._resolve_root_relative(path, ensure_md=True)
        if not note_path.exists():
            raise FileNotFoundError(path)

        existing = note_path.read_text(encoding="utf-8")
        if mode == "append":
            new_content = existing.rstrip() + "\n\n" + content.strip() + "\n"
        elif mode == "replace_full":
            new_content = content
        elif mode == "replace_section":
            if not heading:
                raise ValueError("heading is required for replace_section")
            new_content = self._replace_section(existing, heading, content)
        else:
            raise ValueError("mode must be append, replace_section, or replace_full")

        note_path.write_text(new_content, encoding="utf-8")
        return {"path": self._as_vault_relative(note_path), "updated": True, "mode": mode}

    def create_from_template(
        self,
        destination_path: str,
        rendered_content: str,
        overwrite: bool = False,
    ) -> dict[str, object]:
        return self.create_note(destination_path, rendered_content, overwrite=overwrite)

    def ensure_indexes(self) -> dict[str, object]:
        self.scaffold_workspace(overwrite=False)
        updated = {
            f"{self.config.root_folder}/01-Initiatives/Initiatives Index.md": self._links_for_folder(f"{self.config.root_folder}/01-Initiatives", "Initiatives Index.md"),
            f"{self.config.root_folder}/02-PRDs/PRD Index.md": self._links_for_folder(f"{self.config.root_folder}/02-PRDs", "PRD Index.md"),
            f"{self.config.root_folder}/03-Decisions/Decision Log.md": self._links_for_folder(f"{self.config.root_folder}/03-Decisions", "Decision Log.md"),
            f"{self.config.root_folder}/05-Sprints/Sprint Board.md": self._links_for_folder(f"{self.config.root_folder}/05-Sprints", "Sprint Board.md"),
            f"{self.config.root_folder}/06-Releases/Release Notes Index.md": self._links_for_folder(f"{self.config.root_folder}/06-Releases", "Release Notes Index.md"),
            f"{self.config.root_folder}/07-Metrics/Metrics Dashboard.md": self._links_for_folder(f"{self.config.root_folder}/07-Metrics", "Metrics Dashboard.md"),
        }

        changed: list[str] = []
        for relative_path, links in updated.items():
            target = self._resolve_workspace_relative(relative_path)
            current = target.read_text(encoding="utf-8")
            replacement = "\n".join(f"- {link}" for link in links) if links else "- No linked notes yet."
            next_content = self._replace_autogen_block(current, replacement)
            if next_content != current:
                target.write_text(next_content, encoding="utf-8")
                changed.append(self._as_vault_relative(target))

        return {"updated_files": changed}

    def link_artifacts(
        self,
        initiative_path: str | None = None,
        prd_path: str | None = None,
        adr_paths: list[str] | None = None,
        sprint_path: str | None = None,
        release_note_path: str | None = None,
        metrics_plan_path: str | None = None,
        stakeholder_update_path: str | None = None,
        risk_paths: list[str] | None = None,
    ) -> dict[str, object]:
        changed: list[str] = []
        adr_paths = adr_paths or []
        risk_paths = risk_paths or []

        if initiative_path:
            changed.extend(
                self._apply_links(
                    initiative_path,
                    {
                        "Linked PRD": [self._wikilink(prd_path)] if prd_path else [],
                        "Linked Decisions": [self._wikilink(path) for path in adr_paths],
                        "Metrics Plan": [self._wikilink(metrics_plan_path)] if metrics_plan_path else [],
                        "Current Risks": [self._wikilink(path) for path in risk_paths],
                        "Sprint Notes": [self._wikilink(sprint_path)] if sprint_path else [],
                        "Release Notes": [self._wikilink(release_note_path)] if release_note_path else [],
                    },
                )
            )
        if prd_path:
            changed.extend(
                self._apply_links(
                    prd_path,
                    {
                        "Related Initiative": [self._wikilink(initiative_path)] if initiative_path else [],
                        "Linked Decisions": [self._wikilink(path) for path in adr_paths],
                        "Metrics Plan": [self._wikilink(metrics_plan_path)] if metrics_plan_path else [],
                        "Release Notes": [self._wikilink(release_note_path)] if release_note_path else [],
                    },
                )
            )
        for adr_path in adr_paths:
            changed.extend(
                self._apply_links(
                    adr_path,
                    {
                        "Related Initiative": [self._wikilink(initiative_path)] if initiative_path else [],
                        "Related PRD": [self._wikilink(prd_path)] if prd_path else [],
                    },
                )
            )
        if sprint_path:
            changed.extend(
                self._apply_links(
                    sprint_path,
                    {
                        "Linked Initiatives": [self._wikilink(initiative_path)] if initiative_path else [],
                        "Current Risks": [self._wikilink(path) for path in risk_paths],
                    },
                )
            )
        if release_note_path:
            changed.extend(
                self._apply_links(
                    release_note_path,
                    {
                        "Shipped PRDs": [self._wikilink(prd_path)] if prd_path else [],
                        "Stakeholder Update": [self._wikilink(stakeholder_update_path)] if stakeholder_update_path else [],
                    },
                )
            )
        if metrics_plan_path:
            changed.extend(
                self._apply_links(
                    metrics_plan_path,
                    {
                        "Related Initiative": [self._wikilink(initiative_path)] if initiative_path else [],
                        "Related PRD": [self._wikilink(prd_path)] if prd_path else [],
                    },
                )
            )
        if stakeholder_update_path and release_note_path:
            changed.extend(
                self._apply_links(
                    stakeholder_update_path,
                    {"Related Release": [self._wikilink(release_note_path)]},
                )
            )

        return {"updated_files": sorted(set(changed))}

    def _resolve_workspace_relative(self, relative_path: str) -> Path:
        normalized = PurePosixPath(relative_path)
        if normalized.is_absolute() or ".." in normalized.parts:
            raise VaultSafetyError("workspace paths must be relative and stay within the vault")
        return (self.config.vault_path / Path(*normalized.parts)).resolve()

    def _resolve_root_relative(self, relative_path: str, ensure_md: bool = False) -> Path:
        normalized = PurePosixPath(relative_path)
        if normalized.is_absolute() or ".." in normalized.parts:
            raise VaultSafetyError("path must be relative and stay within Shipwright root")
        if ensure_md and normalized.suffix != ".md":
            normalized = PurePosixPath(*normalized.parts).with_suffix(".md")
        target = (self.config.root_path / Path(*normalized.parts)).resolve()
        self._assert_within(target, self.config.root_path)
        return target

    @staticmethod
    def _assert_within(target: Path, root: Path) -> None:
        if not target.is_relative_to(root):
            raise VaultSafetyError("resolved path escapes allowed root")

    def _replace_section(self, content: str, heading: str, new_body: str) -> str:
        pattern = re.compile(rf"^(#+)\s+{re.escape(heading)}\s*$", re.MULTILINE)
        matches = list(pattern.finditer(content))
        if len(matches) != 1:
            raise HeadingResolutionError(f"heading must resolve to exactly one section: {heading}")
        match = matches[0]
        level = len(match.group(1))
        section_start = match.end()
        next_heading = re.compile(rf"^#{{1,{level}}}\s+", re.MULTILINE).search(content, section_start)
        section_end = next_heading.start() if next_heading else len(content)
        before = content[:section_start].rstrip()
        after = content[section_end:].lstrip("\n")
        replacement = before + "\n\n" + new_body.strip() + "\n"
        if after:
            replacement += "\n" + after
        return replacement

    def _apply_links(self, relative_path: str, heading_map: dict[str, Iterable[str]]) -> list[str]:
        note_path = self._resolve_root_relative(relative_path, ensure_md=True)
        if not note_path.exists():
            raise FileNotFoundError(relative_path)
        content = note_path.read_text(encoding="utf-8")
        original = content
        for heading, links in heading_map.items():
            cleaned = sorted({link for link in links if link})
            if not cleaned:
                continue
            content = self._ensure_heading_links(content, heading, cleaned)
        if content != original:
            note_path.write_text(content, encoding="utf-8")
            return [self._as_vault_relative(note_path)]
        return []

    def _ensure_heading_links(self, content: str, heading: str, links: list[str]) -> str:
        pattern = re.compile(rf"^(##)\s+{re.escape(heading)}\s*$", re.MULTILINE)
        if not pattern.search(content):
            content = content.rstrip() + f"\n\n## {heading}\n"
        try:
            current = self._extract_section_links(content, heading)
            merged = sorted(set(current) | set(links))
            body = "\n".join(f"- {link}" for link in merged)
            return self._replace_section(content, heading, body)
        except HeadingResolutionError:
            raise

    def _extract_section_links(self, content: str, heading: str) -> list[str]:
        pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
        matches = list(pattern.finditer(content))
        if len(matches) != 1:
            raise HeadingResolutionError(f"heading must resolve to exactly one section: {heading}")
        match = matches[0]
        next_heading = re.compile(r"^##\s+", re.MULTILINE).search(content, match.end())
        section = content[match.end(): next_heading.start() if next_heading else len(content)]
        return [line[2:].strip() for line in section.splitlines() if line.strip().startswith("- ")]

    def _links_for_folder(self, folder: str, index_name: str) -> list[str]:
        base = self._resolve_workspace_relative(folder)
        links = []
        for path in sorted(base.glob("*.md")):
            if path.name == index_name:
                continue
            links.append(self._wikilink(self._as_vault_relative(path)))
        return links

    @staticmethod
    def _replace_autogen_block(content: str, body: str) -> str:
        pattern = re.compile(
            rf"{re.escape(AUTOGEN_START)}.*?{re.escape(AUTOGEN_END)}",
            re.DOTALL,
        )
        replacement = f"{AUTOGEN_START}\n{body}\n{AUTOGEN_END}"
        if not pattern.search(content):
            return content.rstrip() + "\n\n" + replacement + "\n"
        return pattern.sub(replacement, content)

    @staticmethod
    def _wikilink(relative_path: str | None) -> str:
        if not relative_path:
            return ""
        stem = Path(relative_path).stem
        return f"[[{stem}]]"

    @staticmethod
    def _title_for_path(path: Path) -> str:
        return path.stem

    def _as_vault_relative(self, path: Path) -> str:
        return str(path.relative_to(self.config.vault_path)).replace("\\", "/")
