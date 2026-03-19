# Quickstart

## Install the full pack

```bash
curl -sSL https://raw.githubusercontent.com/your-org/pm-pilot/main/install.sh | bash
```

## Install selected skills

```bash
curl -sSL https://raw.githubusercontent.com/your-org/pm-pilot/main/install.sh | bash -s -- --skills pr-translator,prd-builder
```

## Verify installation

Check the relevant skill directory for your platform:

- Claude Code: `~/.claude/skills/`
- Codex CLI: `~/.codex/skills/`
- GitHub Copilot: `.github/skills/` in the active workspace

## First commands to try

- `/pr-translate summarize this PR for product`
- `/prd Add shared saved views for dashboards`
- `/ideate Brainstorm ways to reduce onboarding drop-off`

## Tips

- Paste raw source material when possible.
- Keep feature ideas short and concrete.
- For browser-dependent skills, enable web access in your assistant if available.
