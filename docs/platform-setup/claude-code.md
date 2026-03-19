# Claude Code Setup

## Install location

Claude Code loads skills from `~/.claude/skills/`.

## Recommended setup

1. Clone `pm-pilot` locally.
2. Run `./install.sh`.
3. Confirm that symlinks were created under `~/.claude/skills/`.

## Usage

Load or invoke a skill naturally in chat, or use the slash command examples from the README.

## Notes

- Claude Code supports project-level composition well, so keep the repository cloned somewhere stable.
- If a skill needs web access and your session does not provide it, the skill should degrade gracefully.
