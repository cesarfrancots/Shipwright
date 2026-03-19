# Change Categories

Use these categories consistently when summarizing engineering changes for product managers.

## User-Facing Features

Use when the change creates a new capability, expands access, alters a workflow, or changes what a user sees.

Signals:

- New UI states, pages, forms, APIs, permissions, automations, or notifications
- New feature flags or rollout controls tied to user experience
- Expanded support for a persona, plan, region, or device

## Bug Fixes

Use when the change corrects behavior that previously failed, broke expectations, or created incorrect data.

Signals:

- Error handling fixes
- Edge-case logic corrections
- Dedupe, retry, validation, or state consistency fixes
- Incident or regression follow-ups

## Performance

Use when the main effect is speed, efficiency, stability under load, or lower infrastructure cost.

Signals:

- Faster queries, caching, batching, lazy loading
- Reduced payload size or render cost
- Queue throughput and job latency improvements
- Lower memory or CPU pressure

## Refactors

Use when the change reorganizes code without a meaningful intended product behavior change.

Signals:

- Renames, abstraction cleanup, module extraction, test reshaping
- Type improvements and internal API cleanup
- Dependency swaps with no user-visible outcome

## Infrastructure

Use when the change affects environments, deployment, observability, access, or platform foundations.

Signals:

- CI/CD, container, Terraform, Helm, secrets, runtime config
- Monitoring, alerts, dashboards, logging
- Background worker setup and environment variables
- Data migrations when the migration itself is the important change

## Classification Rules

1. Assign one primary category per change unit.
2. Prefer the category that best matches the intended outcome, not the implementation technique.
3. If a refactor unlocks a visible feature in the same diff, classify the net outcome as `user-facing features`.
4. If a migration supports a feature launch, mention it under risks or supporting evidence unless the migration is the main event.
5. If unsure between `bug fixes` and `performance`, ask:
   Was something incorrect before?
   If yes, choose `bug fixes`.
   If no, choose `performance`.
