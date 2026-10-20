---
title: DeepEval (open source) and Confident AI (hosted platform)
org: Confident AI
date: 2026-10
url: https://deepeval.com/docs/metrics-introduction
kind: tooling-product
category: eval-tooling
---
# DeepEval (open source) and Confident AI (hosted platform)

## One line
DeepEval is the most-starred pytest-style open-source LLM eval library (~19k stars, Apache-2.0) with a large catalogue of LLM-judged metrics including agent trajectory and tool metrics; Confident AI is its paid hosted layer.

## What they do
- Metrics (docs): custom G-Eval (criteria → generated steps → score), DAG (decision-tree, can be deterministic), JevEval (questions answered by "Jev, a System One model" with calibrated probabilities), Arena G-Eval.
- Agent trajectory metrics (full trace): Task Completion, Step Efficiency, Plan Adherence, Plan Quality. Component: Tool Correctness, Argument Correctness.
- Multi-turn: Knowledge Retention, Role Adherence, Conversation Completeness, Conversation Relevancy, ConversationalGEval; ConversationSimulator with personas (https://www.lyzr.ai/?p=140045).
- RAG, safety (Bias, Toxicity, PIILeakage, Role Violation...), image metrics. Every metric returns 0–1 + reason, threshold 0.5. Eval modes llm/hybrid/system_one; flaky metrics can be tracked without gating.
- DeepTeam red-teaming sibling (3,030 stars, Apache-2.0). Offered inside AWS AgentCore as a third-party evaluator library.
- GitHub: deepeval 18,972 stars (GitHub API 2026-10-20).

## Evidence
- Docs: "We CANNOT guarantee that evaluations will work as expected when using a custom model."
- A 2026 guide notes DeepEval/Confident AI "Judge metrics go unchecked against human labels" (https://shurco.ai/guides/best-ai-agent-evaluation-tools/).

## Limitations and criticisms
- Generic prebuilt metrics are exactly what Hamel Husain criticises (see Hamel note). Shared dashboards require paid Confident AI. Vendor-authored comparison pages (deepeval.com/blog) should be discounted.

## Relevance to agent evaluation
- Plan Adherence / Plan Quality / Step Efficiency are rare process-level agent metrics; DAG metrics show a way to make a judge more deterministic.

