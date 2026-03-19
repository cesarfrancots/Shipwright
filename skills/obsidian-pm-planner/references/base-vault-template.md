# Shipwright Vault Template

Use this structure for the Shipwright-managed area of an Obsidian vault.

```text
Shipwright/
  00-Hub/
  01-Initiatives/
  02-PRDs/
  03-Decisions/
  04-Research/
  05-Sprints/
  06-Releases/
  07-Metrics/
  08-Stakeholders/
  09-Risks/
  10-Archive/
Templates/
  Shipwright/
```

## Required Starter Notes

- `Shipwright/00-Hub/Shipwright Hub.md`
- `Shipwright/01-Initiatives/Initiatives Index.md`
- `Shipwright/02-PRDs/PRD Index.md`
- `Shipwright/03-Decisions/Decision Log.md`
- `Shipwright/05-Sprints/Sprint Board.md`
- `Shipwright/06-Releases/Release Notes Index.md`
- `Shipwright/07-Metrics/Metrics Dashboard.md`
- `Shipwright/09-Risks/Risk Register.md`

## Safety Boundary

Shipwright should only read and write inside:

- `Shipwright/`
- `Templates/Shipwright/`

Do not treat the rest of the vault as writable workspace content.

## Linking Conventions

- Initiative notes link to PRD, ADR, metrics plan, sprint notes, release notes, and risks.
- PRD notes link back to the initiative and forward to decisions and releases.
- Sprint notes link to active initiatives and current risks.
- Release notes link to shipped PRDs and stakeholder updates.
- Metrics plans link to both initiative and PRD.
