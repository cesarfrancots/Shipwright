---
name: obsidian-pm-planner
description: >
  Create and maintain an Obsidian workspace for product planning, execution tracking, and PM documentation.
  Use when someone says Obsidian notes, build a planning vault, project note template, sprint planning, meeting notes, or knowledge base.
  Produce a base vault structure, reusable note templates, and a weekly operating rhythm that connects PRDs, decisions, risks, and releases.
license: Apache-2.0
metadata:
  author: pm-pilot
  version: "1.0.0"
  tags: [product-management, obsidian, planning, documentation, knowledge-management]
---

# Obsidian PM Planner

## When to Use This Skill

Use this skill when a PM wants to set up or improve an Obsidian vault as a system of record for product work.

Read `references/base-vault-template.md` and `references/note-templates.md` before generating outputs.

If the user does not provide a vault path or context, ask:
"Do you want a new vault scaffold, or only templates to paste into an existing vault?"

## Instructions

1. Identify the operating mode:
   `bootstrap` for creating a full base vault structure, or `templates-only` for adding markdown templates.
2. Collect minimum context:
   product name, team cadence, current initiatives, and preferred planning granularity (weekly or sprint).
3. Generate a base structure using the reference layout.
   Include folders for initiatives, PRDs, decisions, meetings, sprint plans, release notes, and dashboards.
4. Generate reusable templates with frontmatter and linking conventions.
   Keep templates short and easy to fill during real meetings.
5. Define a linking workflow:
   every initiative links to a PRD, decision records, risks, and release artifacts.
6. Add a weekly operating rhythm note:
   planning, mid-week check, risk review, and sprint close.
7. Preserve portability.
   Output plain markdown files and folder paths; do not require Obsidian plugins by default.
8. If the user cannot write files from the current environment, output copy-paste-ready file blocks.

## Output Format

### Setup Mode

- Mode: bootstrap | templates-only
- Product:
- Cadence:

### Vault Structure

Provide a folder tree for the vault.

### Files to Create

For each file:

- Path:
- Purpose:
- Content (markdown):

### Working Conventions

- Linking rules
- Tagging rules
- Weekly ritual

## Examples

### Example Input

`Set up an Obsidian planning vault for PM Pilot with sprint cadence and decision tracking.`

### Example Output

A complete folder tree plus starter files for initiatives, PRDs, decisions, meeting notes, sprint plans, and release notes, with clear wiki-link conventions between artifacts.
