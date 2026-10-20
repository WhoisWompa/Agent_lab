---
title: LangSmith: Insights Agent, multi-turn evals and Align Evaluator
org: LangChain
date: 2025-10
url: https://blog.langchain.com/insights-agent-multiturn-evals-langsmith
kind: tooling-product
category: eval-tooling
---
# LangSmith: Insights Agent, multi-turn evals and Align Evaluator

## One line
LangSmith is the default observability+eval platform for LangChain/LangGraph stacks; in Oct 2025 it added thread-level multi-turn online evals and an Insights Agent that clusters production traces, and it offers an 'Align Evaluator' workflow to calibrate LLM judges against human labels.

## What they do
- 23 Oct 2025: threads (multi-turn sessions) as first-class; Insights Agent auto-categorises agent usage/failure patterns (GA for Plus/Enterprise cloud); Multi-turn Evals = online evaluators scoring whole conversations for semantic intent, semantic outcome and agent trajectory (https://changelog.langchain.com/announcements/ann_bQMixWmJXuD4s).
- Judge alignment (https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback): send runs to an annotation queue, have experts label, test judge prompt against labels, revise where it disagrees; works for offline and online evaluators. The Potato annotator docs describe LangSmith Align Evals as the standard 100–200 gold-label workflow (https://potatoannotator.readthedocs.io/en/latest/agent-evaluation/judge_alignment/).
- OSS libraries: openevals (1,226 stars, MIT) and agentevals (752 stars, MIT, last push Jul 2026) provide prebuilt LLM-as-judge and trajectory-match evaluators (GitHub API, 2026-10-20).
- Pricing: free tier; paid by trace volume plus seats (Arize comparison, https://arize.com/resources/llm-and-agent-evaluation-platforms/). One 2026 guide reports LangSmith's calculator at $5 per 1k base traces with 14-day retention vs $0.50/1k on its 2025 list (https://shurco.ai/guides/best-ai-agent-evaluation-tools/ — secondary, unverified).

## Evidence
- Feature claims from LangChain's own blog/docs. Competitor Latitude says Insights clusters failures but lacks issue lifecycle, frequency tracking, or automatic eval generation (https://latitude.so/blog/langsmith-alternatives-agent-observability-2026 — vendor marketing).

## Limitations and criticisms
- Closed source; weaker outside LangChain (instrumentation effort); seat pricing painful with many occasional reviewers (comparison sources above).

## Relevance to agent evaluation
- Trajectory-level online evaluators on threads plus judge alignment against expert labels = the standard feature set an agent-judge must match.

