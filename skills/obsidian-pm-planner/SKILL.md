---
name: obsidian-pm-planner
description: >
  Create and maintain a Shipwright-managed Obsidian workspace for product planning, execution tracking, and PM documentation.
  Use when someone says Obsidian notes, Shipwright vault, planning workspace, sprint planning, project note template, or knowledge base.
  Produce a Shipwright folder structure, MCP-friendly note templates, and linked documentation workflows for PRDs, decisions, sprints, releases, metrics, and stakeholder updates.
license: Apache-2.0
metadata:
  author: pm-pilot
  version: "1.1.0"
  tags: [product-management, obsidian, shipwright, planning, knowledge-management]
---

# Obsidian PM Planner

## When to Use This Skill

Use this skill when a PM wants Shipwright to manage product documentation inside an Obsidian vault.

Read `references/base-vault-template.md` and `references/note-templates.md` before generating outputs.

Default to Shipwright naming:

- workspace root: `Shipwright/`
- templates root: `Templates/Shipwright/`

If the Shipwright Obsidian MCP server is available, prefer MCP operations over raw markdown file blocks.
If the MCP server is unavailable, fall back to copy-paste-ready markdown files.

## Modes

### bootstrap-vault

Use this mode when the user wants to scaffold a Shipwright workspace into an existing or new vault.

### mcp-managed-templates

Use this mode when the user wants Shipwright to create or update notes through the MCP server using the canonical template set.

## Instructions

1. Identify the mode:
   `bootstrap-vault` or `mcp-managed-templates`.
2. Confirm the minimum context:
   vault path, team cadence, active initiatives, and whether the MCP server is available.
3. In `bootstrap-vault` mode:
   generate the canonical Shipwright folder tree and starter notes under `Shipwright/`.
4. In `mcp-managed-templates` mode:
   prefer MCP tools to scaffold the workspace, create notes from templates, ensure indexes, and link artifacts.
5. Keep the workspace constrained to Shipwright-owned areas:
   `Shipwright/` and `Templates/Shipwright/`.
6. Use the canonical document set:
   initiative, PRD, ADR, research note, sprint plan, release note, metrics plan, stakeholder update, and daily log.
7. Preserve portability.
   Do not require Obsidian plugins by default.
8. If the environment cannot call MCP tools, output file paths and markdown blocks that match the canonical Shipwright template schema.

## MCP Tool Contract

When the MCP server is available, prefer these operations in plain language:

- check workspace status
- scaffold the Shipwright workspace
- create notes from canonical templates
- read and search existing Shipwright notes
- update notes by appending or replacing a section
- ensure indexes stay current
- link initiatives, PRDs, ADRs, sprints, releases, metrics, and stakeholder updates

## Output Format

### Setup Mode

- Mode: bootstrap-vault | mcp-managed-templates
- Product:
- Cadence:
- MCP available: yes | no

### Workspace Structure

Provide the Shipwright folder tree.

### Files or MCP Actions

If MCP is available:

- Tool:
- Inputs:
- Expected result:

If MCP is unavailable:

- Path:
- Purpose:
- Content (markdown):

### Working Conventions

- Linking rules
- Metadata rules
- Weekly ritual

## Examples

### Example Input

`Bootstrap a Shipwright Obsidian workspace for a biweekly product team and keep PRDs plus ADRs linked through MCP if available.`

### Example Output

A Shipwright workspace plan that scaffolds canonical folders, templates, starter notes, and link conventions, while preferring MCP-managed note operations when the server is available.
