# Base Vault Template

Use this structure for a PM-focused Obsidian vault.

```text
00-Home/
01-Initiatives/
02-PRDs/
03-Decisions/
04-Meetings/
05-Sprints/
06-Releases/
07-Metrics/
08-Risks/
09-Archive/
Templates/
```

## Suggested Core Files

- `00-Home/PM-Command-Center.md`
- `01-Initiatives/Initiative-Index.md`
- `02-PRDs/PRD-Index.md`
- `03-Decisions/Decision-Log.md`
- `05-Sprints/Sprint-Board.md`
- `06-Releases/Release-Notes-Index.md`
- `08-Risks/Risk-Register.md`

## Linking Conventions

- Initiative note links to one PRD note:
  `[[PRD - <feature-name>]]`
- PRD note links to decision notes:
  `[[ADR - <decision-title>]]`
- Sprint notes link to active initiatives and risks.
- Release notes link back to PRD and initiative.

## Weekly Operating Rhythm

1. Monday:
   Update `Sprint-Board`, top risks, and weekly priorities.
2. Mid-week:
   Add decision notes and unresolved blockers.
3. Friday:
   Publish release note summary and archive completed sprint items.
