---
name: ideation-engine
description: >
  Generate prioritized product ideas from a problem statement and score them with RICE.
  Use when someone says brainstorm, generate ideas, what should we build, prioritize concepts, or explore adjacent bets.
  Produce 10 ideas by default, support divergent, convergent, contrarian, and adjacent modes, and expand a selected idea into stories, objections, and scope.
license: Apache-2.0
metadata:
  author: pm-pilot
  version: "1.0.0"
  tags: [product-management, brainstorming, prioritization, rice, ideation]
---

# Ideation Engine

## When to Use This Skill

Use this skill when the user wants solution options, prioritization support, or exploration of a product opportunity.

Read `references/rice-framework.md` and `references/brainstorm-modes.md` before generating ideas.

Default to `divergent` mode if the user does not specify a mode.

## Instructions

1. Restate the problem to anchor the session.
2. Choose the brainstorming mode:
   `divergent`, `convergent`, `contrarian`, or `adjacent`.
3. Generate exactly 10 ideas unless the user requests a different count.
4. For each idea, provide:
   title, summary, target user, key assumption, and RICE score.
5. Score ideas with explicit components:
   Reach, Impact, Confidence, Effort, and computed priority.
6. Do not fabricate precision.
   Use relative estimates when exact numbers are unavailable.
7. Sort ideas from strongest to weakest by RICE score unless the user requests another ordering.
8. If the user selects one idea for a deep dive, expand it with:
   user stories, likely objections, dependency notes, and a rough scope estimate.
9. Label whether a deep-dive idea is likely `small`, `medium`, or `large`.

## Output Format

### Problem Frame

- Problem:
- Primary user:
- Mode:
- Constraints:

### Idea Table

| Rank | Idea | Summary | Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|---|---|---|

### Idea Details

For each idea:

- Idea:
- Target user:
- Why it could work:
- Key risk:

### Recommended Next Bets

- Top 3 ideas with one-line rationale each

### Deep Dive

Only include this section when the user selects an idea.

- Chosen idea:
- User stories:
- Objections:
- Scope estimate:
- Suggested first release boundary:

## Examples

### Example Input

`Brainstorm ways to reduce failed checkout recovery for subscription customers.`

### Example Output

Generate 10 ideas in divergent mode, score them with RICE, recommend the top three, and be ready to expand the chosen concept into stories, objections, and scope.
