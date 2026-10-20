---
title: AI red-teaming tools: Lakera, HiddenLayer, Mindgard, Giskard, garak, PyRIT, DeepTeam
org: various
date: 2026-07
url: https://confident-ai.com/knowledge-base/compare/best-ai-red-teaming-tools-2026
kind: tooling-product
category: eval-tooling
---
# AI red-teaming tools: Lakera, HiddenLayer, Mindgard, Giskard, garak, PyRIT, DeepTeam

## One line
Red-teaming for LLM apps/agents splits into OSS frameworks (garak, PyRIT, Promptfoo, DeepTeam, Giskard) and commercial security platforms (Lakera—now Check Point, HiddenLayer, Mindgard), with consolidation into security vendors and model labs.

## What they do
- garak (NVIDIA, 9,622 stars, Apache-2.0): LLM vulnerability scanner, 120+ probe categories; criticised as model-level single-turn.
- PyRIT (Microsoft AI Red Team; microsoft/PyRIT 4,658 stars, MIT): orchestration framework; underlies Foundry's AI Red Teaming Agent (GA 2026).
- Giskard (giskard-oss 5,911 stars, Apache-2.0, "Open-Source Evaluation & Testing library for LLM Agents") + enterprise Hub: agent tool-call and multi-turn attacks (https://www.giskard.ai/knowledge/giskard-alternatives-ai-red-teaming).
- Lakera: Guard runtime prompt-injection API + Lakera Red; acquired by Check Point in 2025 (https://appsecsanta.com/lakera-alternatives).
- HiddenLayer: enterprise AI security incl. automated red teaming (AutoRT), model-file supply-chain scanning.
- Mindgard: commercial automated AI red teaming SaaS for security teams.
- DeepTeam (Confident AI, 3,030 stars) and Promptfoo red team (OpenAI-owned).

## Evidence
Stars from GitHub API 2026-10-20. Most comparison pages are vendor-authored (Giskard, Confident AI).

## Limitations and criticisms
Vendor self-ranking; no independent head-to-head attack-success benchmarks found.

## Relevance to agent evaluation
Red-team tools increasingly target agents (tool misuse, indirect injection, multi-turn); they act as adversarial user simulators — a complement to judge-based evaluation.

