---
title: State of Agent Engineering
org: LangChain
date: 2025-12
url: https://langchain.com/state-of-agent-engineering
kind: third-party-evaluator
category: production-practice
---
# State of Agent Engineering

## One line
LangChain's survey of 1,340 practitioners (18 Nov - 2 Dec 2025) on agents in production, including how many evaluate them and how.

## What they do
Survey of agent builders on deployment, blockers, observability and evals.

## Evidence
- 57% have agents in production; quality is the top blocker (32%), latency second (20%); security 24.9% among 2k+ employee enterprises.
- Observability 89% overall; detailed step/tool tracing 62%; among production orgs 94% observability, 71.5% full tracing.
- Offline evals on test sets 52.4%; online evals 37.3% (44.8% among production orgs); not evaluating 29.5% overall, 22.8% among production orgs; nearly a quarter of eval-running orgs do both.
- Human review 59.8%; LLM-as-judge 53.3%.

## Limitations and criticisms
Vendor survey, self-selected LangChain audience; question wording not verified. Some secondary sources misdate it.

## Relevance to agent evaluation
Quantifies the gap: observability is near-universal, evals are not; roughly one in five production agent teams run no evals, and fewer than half run online evals.
