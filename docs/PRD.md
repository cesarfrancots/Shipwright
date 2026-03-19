# PM Pilot Product Requirements Document

## Executive Summary

PM Pilot is an open-source collection of Agent Skills for product managers.
It turns AI coding assistants into practical PM copilots for sprint reviews, PRDs, ideation, metrics, communication, diagrams, briefings, and competitive research.

## Problem

Product managers work close to engineering artifacts but lack tooling that translates technical detail into product decisions and reusable PM workflows.
Most assistant ecosystems optimize for developers, not PMs.

## Solution

Ship a portable skill pack that works across multiple assistant platforms and covers eight common PM jobs:

- translating PRs and commit ranges
- building PRDs
- brainstorming and prioritizing ideas
- drawing diagrams
- adapting stakeholder communications
- defining metrics
- preparing PM briefings
- analyzing competitors

## Phase 1 Launch Skills

- `pr-translator`
- `prd-builder`
- `ideation-engine`

These three skills should be the highest-quality launch assets and set the repository standard for the rest of the pack.

## User Outcomes

- Reduce time spent decoding technical artifacts.
- Standardize product documents and update formats.
- Give PMs repeatable frameworks inside the tools engineering already uses.

## Non-Goals

- Building a proprietary PM SaaS product.
- Requiring a hosted backend or package manager.
- Locking the skill pack to a single assistant platform.

## Quality Bar

- Skills must be usable as-is, not placeholders.
- Instructions must stay concise and composable.
- References should hold templates and frameworks.
- Tests should validate expected behavior.
- Installation must be simple and reversible.
