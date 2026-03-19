# GitHub Copilot Setup

## Install location

GitHub Copilot agent skills are typically project-scoped under `.github/skills/`.

## Recommended setup

1. Clone `pm-pilot`.
2. Run `./install.sh`.
3. Open the target workspace in VS Code or your Copilot-enabled environment.

## Usage

Reference the skill naturally in Copilot Chat or use the slash-command style prompts documented in this repository.

## Notes

- Copilot setup is often workspace-specific, so the installer links skills into `.github/skills/` for the current repository by default.
- Keep the PM Pilot clone accessible from the workspace that consumes the symlinks.
