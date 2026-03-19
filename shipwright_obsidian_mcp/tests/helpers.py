from __future__ import annotations

from pathlib import Path
import shutil
import uuid


FIXTURES = Path(__file__).resolve().parent / "fixtures"
TMP_ROOT = Path(__file__).resolve().parent / ".tmp"


def make_temp_vault(fixture_name: str | None = None) -> Path:
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    temp_dir = TMP_ROOT / f"shipwright-mcp-test-{uuid.uuid4().hex}"
    temp_dir.mkdir(parents=True, exist_ok=False)
    if fixture_name:
        source = FIXTURES / fixture_name
        if source.exists():
            _copy_tree(source, temp_dir)
    return temp_dir


def _copy_tree(source: Path, destination: Path) -> None:
    for item in source.rglob("*"):
        relative = item.relative_to(source)
        target = destination / relative
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
