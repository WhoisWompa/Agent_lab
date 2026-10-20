---
title: Building effective agents
org: Anthropic (Erik Schluntz, Barry Zhang)
date: 2024-12
url: https://www.anthropic.com/engineering/building-effective-agents
kind: lab-practice
category: production-practice
---
# Building effective agents

## One line
Anthropic's Dec 2024 guide to agent architectures (workflows vs agents, simple composable patterns); listed only, not re-read in this pass.

## What they do
Recommends starting with the simplest solution and adding agentic complexity only when it demonstrably helps, measured by evaluation; describes evaluator-optimizer workflow (one LLM generates, another critiques in a loop).

## Evidence
Not fetched in this pass; content from prior knowledge of the post, so treat as unverified here.

## Limitations and criticisms
Architecture guidance rather than eval methodology; superseded on evals by the Jan 2026 "Demystifying evals" post.

## Relevance to agent evaluation
Source of the evaluator-optimizer pattern, the in-loop version of an agent judging an agent.
