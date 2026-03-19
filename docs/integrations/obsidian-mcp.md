# Shipwright Obsidian MCP

## What it does

The Shipwright Obsidian MCP server is a local Python MCP server that lets an agent create, read, search, and update Shipwright-managed notes inside an Obsidian vault.

It is intentionally limited to two writable areas:

- `Shipwright/`
- `Templates/Shipwright/`

The rest of the vault is out of scope for writes.

## Install

```bash
python -m pip install -r requirements-mcp.txt
```

## Local startup

```bash
python -m shipwright_obsidian_mcp --vault-path "C:\Users\<you>\Documents\Obsidian Vault"
```

Optional flags:

- `--root-folder Shipwright`
- `--templates-folder Templates/Shipwright`
- `--transport stdio`

## Codex example

Example `~/.codex/config.toml` entry for a local stdio server:

```toml
[mcp_servers.shipwrightObsidian]
command = "python"
args = ["-m", "shipwright_obsidian_mcp", "--vault-path", "C:\\Users\\<you>\\Documents\\Obsidian Vault"]
```

## VS Code / Copilot example

Example `.vscode/mcp.json`:

```json
{
  "servers": {
    "shipwrightObsidian": {
      "type": "stdio",
      "command": "python",
      "args": [
        "-m",
        "shipwright_obsidian_mcp",
        "--vault-path",
        "C:\\Users\\<you>\\Documents\\Obsidian Vault"
      ]
    }
  }
}
```

## AGENTS.md snippet

Use the Shipwright Obsidian MCP server for any note operation that targets the Obsidian vault.
Only read or write inside `Shipwright/` and `Templates/Shipwright/`.
Prefer MCP actions over raw markdown file output when the server is available.

## Example workflows

### Create initiative

- `scaffold_workspace`
- `create_from_template` with `template_key=initiative`
- `ensure_indexes`

### Create PRD from template

- `create_from_template` with `template_key=prd`
- `link_artifacts` to connect initiative and PRD

### Append ADR

- `create_from_template` with `template_key=adr`
- `link_artifacts` to connect ADR back to initiative and PRD

### Update sprint board

- `create_from_template` with `template_key=sprint-plan`
- `link_artifacts` to connect sprint note with initiative and risks
- `ensure_indexes`

### Generate stakeholder update note

- `create_from_template` with `template_key=stakeholder-update`
- `link_artifacts` to connect release note and stakeholder update

## Future work

This v1 is local-only.
Remote HTTP or SSE transport for OpenAI Responses API style MCP usage is intentionally deferred to a later phase.
