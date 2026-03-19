---
name: spec-diagrams
description: >
  Generate Mermaid diagrams from product specs, flows, and system descriptions.
  Use when someone says draw a flow, map the journey, sequence diagram, architecture diagram, or visualize a spec.
  Produce clean Mermaid code for flowchart, sequence, state, user journey, architecture, or entity relationship diagrams with short explanatory notes.
license: Apache-2.0
metadata:
  author: pm-pilot
  version: "1.0.0"
  tags: [product-management, diagrams, mermaid, specifications, visualization]
---

# Spec Diagrams

## When to Use This Skill

Use this skill when a PM needs a visual representation of a workflow, state machine, interaction sequence, or simple architecture.

Read `references/diagram-types.md` before choosing a diagram type.

If the source description is vague, ask the user: "What process, actors, and decision points should the diagram include?"

## Instructions

1. Infer the best Mermaid diagram type from the request.
2. Prefer clarity over exhaustive detail.
3. Name actors, systems, and states consistently.
4. Output runnable Mermaid fenced code first.
5. Add a short note after the diagram that explains what the diagram covers and any assumptions.
6. If the user asks for revision, update the existing structure instead of redrawing from scratch.

## Output Format

```mermaid
<diagram>
```

Notes:

- Scope:
- Assumptions:
- Suggested next refinement:
