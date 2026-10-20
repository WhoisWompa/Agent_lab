---
title: How we evaluate AI models and LLMs for GitHub Copilot
org: GitHub (Connor Adams, Klint Finley)
date: 2025-01
url: https://github.blog/ai-and-ml/generative-ai/how-we-evaluate-models-for-github-copilot/
kind: production-practice
category: production-practice
---
# How we evaluate AI models and LLMs for GitHub Copilot

## One line
GitHub's 17 Jan 2025 description of Copilot's offline evaluation: 4,000+ tests mostly in CI, ~100 containerised repos with broken-then-repaired tests, 1,000+ chat questions with an audited LLM judge, then internal canary use.

## What they do
- "We run more than 4,000 offline tests, most of them as part of our automated CI pipeline."
- Completion: ~100 containerised repos that pass CI; team breaks them and checks whether the model's code makes tests pass; metrics = % unit tests passing and similarity to original code.
- Chat: >1,000 technical questions; simple true/false auto-graded; complex answers graded by "a model with known good performance" whose outputs are "routinely audit[ed]"; acknowledges difficulty keeping the judge "aligned with human reviewers."
- Daily runs against production models; quality drops trigger audits and sometimes prompt changes.
- Live internal evaluation like canary: internal users switched to a new model for all major changes.
- Token usage a main efficiency metric; acceptance rate and latency used in adoption decisions; metrics conflict (higher latency can raise acceptance because users see fewer suggestions).
- Infra: proxy to swap backend model; GitHub Actions; Kafka + Azure; dashboards.

## Evidence
Counts above; no comparison results or judge-human agreement figures. Hamel's FAQ adds that Copilot's team regenerated removed function bodies, ran tests, and A/B tested acceptance.

## Limitations and criticisms
Pre-agent era (completion and chat); no description of coding-agent PR evaluation. Judge audit frequency and agreement unstated.

## Relevance to agent evaluation
Shows a large-company stack: deterministic test-based evals in CI, LLM judge for open-ended answers with human audit, internal dogfooding canary, then online acceptance. Template for coding-agent evals built from real repos.
