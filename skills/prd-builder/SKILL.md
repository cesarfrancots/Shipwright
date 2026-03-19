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

Support `$ARGUMENTS` as the default source for the feature description. Treat it as the primary input when present, and fall back to the user message only if `$ARGUMENTS` is empty or incomplete.

If the idea is underspecified, ask clarifying questions first.
If the user still wants a draft immediately, include an `Open Questions` section and mark assumptions explicitly.

## Instructions

1. Parse the feature description from `$ARGUMENTS` or the user message.
2. Identify missing context across five areas:
   product context, target user, business goal, constraints, and rollout expectations.
3. Ask clarifying questions only when the missing context changes scope, audience, success criteria, constraints, or rollout decisions.
   If the remaining ambiguity is not decision-critical, stop asking and proceed with explicit assumptions.
4. If you ask questions, keep them high-signal and limited.
   Prefer a short set of the most leverageable questions over exhaustive interrogation.
5. If the user asks for a draft now, or if the context is still partially missing after the first pass, draft the PRD anyway and list assumptions in `Open Questions`.
6. Draft the PRD using the structure in `references/prd-template.md`.
7. State assumptions plainly.
   Do not hide uncertainty inside authoritative language.
8. Write user stories in the format:
   `As a <persona>, I want <capability>, so that <outcome>.`
9. Attach acceptance criteria to every user story.
   Make criteria observable and testable.
10. Separate requirements into functional and non-functional where useful.
    Also distinguish MVP requirements from future-phase enhancements so the first release boundary is obvious.
11. Keep goals and non-goals distinct.
   Non-goals should narrow scope, not repeat goals negatively.
12. Recommend metrics that can realistically be measured.
13. Include timeline guidance even when dates are unknown.
    Use phases, dependencies, and review checkpoints.
14. Avoid implementation over-specification unless the user asks for a technical spec.
15. Keep the tone concise and decision-oriented.
    A compact PRD is better than a long one when the source input is simple.

## Clarifying Questions

Ask questions like these when context is insufficient:

- What product or workflow does this feature belong to?
- Who is the primary user or buyer affected by the feature?
- What business outcome matters most: adoption, conversion, retention, revenue, or support reduction?
- What constraints already exist: compliance, platform, timeline, team capacity, or dependencies?
- What should be explicitly out of scope for the first release?
- Is this intended for all users, a specific segment, or a phased rollout?
- Are there existing metrics, baselines, or target numbers we should use?

Stop asking once the unanswered items would only refine wording or edge cases rather than change the PRD shape.
At that point, write the draft with stated assumptions and an `Open Questions` section.

## Example Output

Minimal expected tone:

`Status: draft`

`MVP: summarize unresolved tickets for workspace admins via email once per week.`

`Future phases: per-team digests, custom schedules, and Slack delivery.`

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

Within `Requirements`, make the MVP boundary explicit before listing future-phase ideas.

## Examples

### Example Input

`/prd $ARGUMENTS="Add shared saved views for team dashboards"`

### Example Output

Produce a complete PRD that explains why shared saved views matter, who uses them, how sharing works, what is out of scope for V1, which acceptance criteria govern create, edit, and share flows, and which adoption plus collaboration metrics define success.
