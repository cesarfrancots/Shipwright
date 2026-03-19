---
name: pm-briefing
description: >
  Curate a PM briefing from industry, competitor, product, and technology context.
  Use when someone says morning briefing, catch me up, industry update, competitor news, or product news digest.
  Produce a structured digest with relevance scoring, key developments, implications, and follow-up questions, while degrading gracefully if live web research is unavailable.
license: Apache-2.0
metadata:
  author: pm-pilot
  version: "1.0.0"
  tags: [product-management, briefing, market-research, competitors, news]
---

# PM Briefing

## When to Use This Skill

Use this skill when the user wants a concise briefing on an industry, market, competitor set, or technology stack.

Read `references/briefing-config-example.yaml` if the user wants persistent topics or a saved configuration.

If live web research is unavailable, state: `Based on available context and training data; may be outdated.`

## Instructions

1. Identify the requested topics, competitors, and time horizon.
2. If browsing is available, prioritize recent developments and cite sources.
3. If browsing is unavailable, provide a clearly labeled contextual briefing without pretending it is current.
4. Organize findings by category and relevance.
5. Close with why the PM should care and what to watch next.

## Output Format

### Briefing Scope

- Topics:
- Time horizon:
- Research mode: live research | contextual only

### Key Developments

| Item | Category | Summary | Relevance | Why it matters |
|---|---|---|---|---|

### Implications

### Watch List
