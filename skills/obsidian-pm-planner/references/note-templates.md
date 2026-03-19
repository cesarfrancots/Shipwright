# Note Templates

Use these templates as the initial content for files under `Templates/`.

## Template: Initiative

```markdown
---
type: initiative
status: active
owner: ""
review_cadence: weekly
---

# Initiative - <name>

## Outcome

## Success Metrics

## Linked PRD
- [[PRD - <name>]]

## Current Risks

## Next Milestone
```

## Template: PRD

```markdown
---
type: prd
status: draft
owner: ""
---

# PRD - <feature-name>

## Problem

## Goals

## Non-Goals

## MVP Scope

## Future Phases

## Acceptance Criteria

## Linked Decisions
- [[ADR - <decision-title>]]
```

## Template: Decision Record (ADR)

```markdown
---
type: adr
status: proposed
date: YYYY-MM-DD
---

# ADR - <title>

## Context

## Decision

## Consequences

## Related PRD
- [[PRD - <feature-name>]]
```

## Template: Sprint Plan

```markdown
---
type: sprint
sprint_id: ""
start: YYYY-MM-DD
end: YYYY-MM-DD
---

# Sprint - <id>

## Goals

## Planned Scope

## Risks

## Mid-Sprint Update

## End-of-Sprint Outcome
```

## Template: Stakeholder Update

```markdown
---
type: stakeholder-update
audience: leadership
date: YYYY-MM-DD
---

# Weekly Product Update

## What shipped

## Impact

## Risks / dependencies

## Next week
```
