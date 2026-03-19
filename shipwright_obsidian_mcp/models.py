from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal


UpdateMode = Literal["append", "replace_section", "replace_full"]


@dataclass(frozen=True)
class WorkspaceStatus:
    vault_path: str
    root_folder: str
    templates_folder: str
    scaffold_exists: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class NoteSummary:
    path: str
    title: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class SearchHit:
    path: str
    title: str
    match_type: str
    snippet: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)
