# Codex CLI Setup

## Install location

Codex CLI reads skills from `~/.codex/skills/`.

## Recommended setup

1. Clone `pm-pilot`.
2. Run `./install.sh`.
3. Start Codex CLI with skills enabled if your environment requires it.

Example:

```bash
codex --enable skills
```

## Usage

Prompt normally and reference the installed skills by name or natural language trigger.

## Notes

- Keep the cloned repository on disk because the installer uses symlinks.
- If your Codex environment lacks browsing, `pm-briefing` and `competitive-intel` should label outputs as contextual rather than current.
