---
name: prd-builder
description: >
  Generate complete product requirements documents from a feature idea or product brief.
  Use when someone says write a PRD, spec this feature, define requirements, draft acceptance criteria, or turn an idea into a plan.
  Produce a full PRD with goals, non-goals, user stories, requirements, metrics, risks, timeline, and clarifying questions when context is incomplete.
license: Apache-2.0
metadata:
  author: pm-pilot
  version: "1.0.0"
  tags: [product-management, prd, requirements, specification, planning]
---

# PRD Builder

## When to Use This Skill

Use this skill when the user needs a production-ready PRD from a raw idea, initiative, or problem statement.

Read `references/prd-template.md` before drafting.

Support `$ARGUMENTS` as the default source for the feature description.

If the idea is underspecified, ask clarifying questions first.
If the user still wants a draft immediately, include an `Open Questions` section and mark assumptions explicitly.

## Instructions

1. Parse the feature description from `$ARGUMENTS` or the user message.
2. Identify missing context across five areas:
   product context, target user, business goal, constraints, and rollout expectations.
3. If critical context is missing, list the clarifying questions you would ask before drafting.
4. Draft the PRD using the structure in `references/prd-template.md`.
5. State assumptions plainly.
   Do not hide uncertainty inside authoritative language.
6. Write user stories in the format:
   `As a <persona>, I want <capability>, so that <outcome>.`
7. Attach acceptance criteria to every user story.
   Make criteria observable and testable.
8. Separate requirements into functional and non-functional where useful.
9. Keep goals and non-goals distinct.
   Non-goals should narrow scope, not repeat goals negatively.
10. Recommend metrics that can realistically be measured.
11. Include timeline guidance even when dates are unknown.
    Use phases, dependencies, and review checkpoints.
12. Avoid implementation over-specification unless the user asks for a technical spec.

## Clarifying Questions

Ask questions like these when context is insufficient:

- What product or workflow does this feature belong to?
- Who is the primary user or buyer affected by the feature?
- What business outcome matters most: adoption, conversion, retention, revenue, or support reduction?
- What constraints already exist: compliance, platform, timeline, team capacity, or dependencies?
- What should be explicitly out of scope for the first release?
- Is this intended for all users, a specific segment, or a phased rollout?
- Are there existing metrics, baselines, or target numbers we should use?

## Output Format

Use markdown with these sections, in this order:

1. Title
2. Status
3. Feature Summary
4. Clarifying Questions
5. Overview
6. Problem Statement
7. Goals
8. Non-Goals
9. Target Users and Use Cases
10. User Stories and Acceptance Criteria
11. Requirements
12. Success Metrics
13. Risks and Mitigations
14. Timeline and Milestones
15. Open Questions

## Examples

### Example Input

`/prd $ARGUMENTS="Add shared saved views for team dashboards"`

### Example Output

Produce a complete PRD that explains why shared saved views matter, who uses them, how sharing works, what is out of scope for V1, which acceptance criteria govern create, edit, and share flows, and which adoption plus collaboration metrics define success.
