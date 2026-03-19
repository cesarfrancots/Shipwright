#!/usr/bin/env python3
"""Minimal repository harness for structure and skill validation.

This script uses only the Python standard library so it can run locally and in
CI without extra dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT_PATHS = [
    ("dir", ROOT / "skills"),
    ("dir", ROOT / "docs"),
    ("dir", ROOT / "examples"),
    ("dir", ROOT / "shipwright_obsidian_mcp"),
    ("file", ROOT / "install.sh"),
    ("file", ROOT / "README.md"),
    ("file", ROOT / "RULES.md"),
]

REQUIRED_FRONTMATTER_KEYS = ("name", "description", "license", "metadata")
REQUIRED_MCP_MODULE_FILES = (
    "__init__.py",
    "__main__.py",
    "config.py",
    "models.py",
    "templates.py",
    "vault.py",
    "server.py",
)
REQUIRED_TEMPLATE_FILES = (
    "initiative.md",
    "prd.md",
    "adr.md",
    "research-note.md",
    "sprint-plan.md",
    "release-note.md",
    "metrics-plan.md",
    "stakeholder-update.md",
    "daily-log.md",
)
OBSIDIAN_INTEGRATION_FILES = (
    ROOT / "docs" / "integrations" / "obsidian-mcp.md",
    ROOT / "skills" / "obsidian-pm-planner" / "SKILL.md",
    ROOT / "skills" / "obsidian-pm-planner" / "references" / "base-vault-template.md",
    ROOT / "skills" / "obsidian-pm-planner" / "references" / "note-templates.md",
)


@dataclass(frozen=True)
class Issue:
    path: Path
    message: str

    def render(self) -> str:
        return f"{self.path.relative_to(ROOT)}: {self.message}"


def main() -> int:
    issues: list[Issue] = []
    issues.extend(validate_root_structure())
    issues.extend(validate_skills())
    issues.extend(validate_mcp_subsystem())
    issues.extend(validate_markdown_placeholders())

    if issues:
        print("Validation failed:")
        for issue in issues:
            print(f"- {issue.render()}")
        return 1

    print("Validation passed.")
    return 0


def validate_root_structure() -> list[Issue]:
    issues: list[Issue] = []
    for kind, path in REQUIRED_ROOT_PATHS:
        if kind == "dir" and not path.is_dir():
            issues.append(Issue(path, "missing required directory"))
        if kind == "file" and not path.is_file():
            issues.append(Issue(path, "missing required file"))
    return issues


def validate_skills() -> list[Issue]:
    issues: list[Issue] = []
    skills_root = ROOT / "skills"
    if not skills_root.is_dir():
        return issues

    for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            issues.append(Issue(skill_file, "missing SKILL.md"))
            continue

        frontmatter, frontmatter_issues = parse_frontmatter(skill_file)
        issues.extend(frontmatter_issues)
        missing = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in frontmatter]
        if missing:
            issues.append(
                Issue(
                    skill_file,
                    f"missing required frontmatter keys: {', '.join(missing)}",
                )
            )

        references_dir = skill_dir / "references"
        tests_dir = skill_dir / "tests"
        refs_count = count_regular_files(references_dir)
        tests_count = count_regular_files(tests_dir)

        if refs_count < 1:
            issues.append(
                Issue(
                    references_dir,
                    "must contain at least 1 file",
                )
            )
        if tests_count < 2:
            issues.append(
                Issue(
                    tests_dir,
                    "must contain at least 2 files",
                )
            )

    return issues


def validate_markdown_placeholders() -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            issues.append(Issue(path, "could not be read as UTF-8"))
            continue
        for lineno, line in enumerate(content.splitlines(), start=1):
            if "your-org" in line.lower():
                issues.append(Issue(path, f"placeholder 'your-org' found on line {lineno}"))
    return issues


def validate_mcp_subsystem() -> list[Issue]:
    issues: list[Issue] = []
    package_root = ROOT / "shipwright_obsidian_mcp"
    for filename in REQUIRED_MCP_MODULE_FILES:
        path = package_root / filename
        if not path.is_file():
            issues.append(Issue(path, "missing required MCP module file"))

    template_root = package_root / "assets" / "templates"
    for filename in REQUIRED_TEMPLATE_FILES:
        path = template_root / filename
        if not path.is_file():
            issues.append(Issue(path, "missing required MCP template asset"))

    for path in OBSIDIAN_INTEGRATION_FILES:
        if not path.is_file():
            issues.append(Issue(path, "missing Obsidian integration file"))
            continue
        content = path.read_text(encoding="utf-8")
        if "Shipwright" not in content:
            issues.append(Issue(path, "must reference canonical Shipwright naming"))
        if "PM Pilot/" in content:
            issues.append(Issue(path, "must not reference stale 'PM Pilot/' vault paths"))

    skill_file = ROOT / "skills" / "obsidian-pm-planner" / "SKILL.md"
    if skill_file.is_file():
        content = skill_file.read_text(encoding="utf-8")
        for required_text in ("bootstrap-vault", "mcp-managed-templates", "Shipwright/"):
            if required_text not in content:
                issues.append(Issue(skill_file, f"missing required Obsidian skill text: {required_text}"))

    return issues


def count_regular_files(path: Path) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for child in path.rglob("*") if child.is_file())


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[Issue]]:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {}, [Issue(path, "could not be read as UTF-8")]

    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [Issue(path, "missing YAML frontmatter start marker")]

    try:
        end_index = lines[1:].index("---") + 1
    except ValueError:
        return {}, [Issue(path, "missing YAML frontmatter end marker")]

    frontmatter_lines = lines[1:end_index]
    parsed, errors = parse_frontmatter_lines(path, frontmatter_lines)
    return parsed, errors or []


def parse_frontmatter_lines(path: Path, lines: Iterable[str]) -> tuple[dict[str, str], list[Issue]]:
    data: dict[str, str] = {}
    current_key: str | None = None
    current_block: list[str] = []
    in_metadata = False
    metadata_lines: list[str] = []
    errors: list[Issue] = []

    def flush_description_block() -> None:
        nonlocal current_key, current_block
        if current_key == "description" and current_block:
            data[current_key] = "\n".join(current_block).strip()
        current_key = None
        current_block = []

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            if current_key == "description":
                current_block.append("")
            elif in_metadata:
                metadata_lines.append("")
            continue

        if line.startswith(" ") or line.startswith("\t"):
            if in_metadata:
                metadata_lines.append(line)
                continue
            if current_key == "description":
                current_block.append(line.strip())
                continue
            errors.append(Issue(path, f"unexpected indented line in frontmatter: {line.strip()}"))
            continue

        if ":" not in line:
            errors.append(Issue(path, f"invalid frontmatter line: {line}"))
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if current_key == "description" and key != "metadata":
            flush_description_block()

        if key == "metadata":
            if value:
                data[key] = value
            else:
                in_metadata = True
            continue

        if current_key == "description":
            flush_description_block()

        if value == ">":
            current_key = key
            current_block = []
            continue

        data[key] = value

    if current_key == "description":
        flush_description_block()

    if in_metadata:
        parsed_metadata = parse_metadata_block(path, metadata_lines)
        if parsed_metadata is None:
            errors.append(Issue(path, "invalid metadata block"))
        else:
            data["metadata"] = "present"
    elif "metadata" not in data:
        errors.append(Issue(path, "metadata frontmatter block is required"))

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key in data and not data[key].strip():
            errors.append(Issue(path, f"frontmatter key '{key}' is empty"))

    if errors:
        return data, errors
    return data, []


def parse_metadata_block(path: Path, lines: Iterable[str]) -> dict[str, str] | None:
    metadata: dict[str, str] = {}
    current_key: str | None = None
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            return None
        metadata[key] = value
        current_key = key
    return metadata if current_key is not None else None


if __name__ == "__main__":
    raise SystemExit(main())
