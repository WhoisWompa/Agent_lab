---
title: Google Gen AI evaluation service (Vertex AI / Gemini Enterprise Agent Platform) and agent evaluation
org: Google Cloud
date: 2026-10
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview
kind: tooling-product
category: eval-tooling
---
# Google Gen AI evaluation service (Vertex AI / Gemini Enterprise Agent Platform) and agent evaluation

## One line
Google's evaluation service centres on LLM 'autoraters' driven by per-prompt adaptive rubrics, plus deterministic trajectory metrics for agents; since Next '26 (22 Apr 2026) it sits under the renamed Gemini Enterprise Agent Platform with simulation, evaluation, observability and optimizer.

## What they do
- Metric types (docs updated 2026-10-19): adaptive rubrics (recommended; unique pass/fail rubrics generated per prompt, "similar to unit tests"), static rubrics (fixed 1-5 criteria), computation-based (ROUGE/BLEU), custom Python function metrics. Console supports Gemini; SDK supports any model via LiteLLM. GenAI Client (`from vertexai import Client`, preview) is recommended; old EvalTask module is GA but "no longer actively developed" and lacks adaptive rubrics.
- Agent metrics (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-agents, updated 2026-10-19, "Pre-GA"): trajectory_exact_match, trajectory_in_order_match, trajectory_any_order_match, trajectory_precision, trajectory_recall, trajectory_single_tool_use; final-response metrics; default latency and failure; runnable agents (Agent Runtime/ADK templates, LangChain, custom functions returning response + trajectory).
- June 2025 blog (https://cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage): batch evaluation; "Evaluate your autorater's quality" against a benchmark of human-rated examples; improve alignment via criteria, CoT, scoring guidelines, and "bring and tune the autorater with your own reference data"; rubric-driven evaluation (generate rubrics per data point, then autorate); agent trajectory eval for ADK, LangGraph, CrewAI; "evaluate your agents in production" (no detail).
- Jan 2025 preview of agent evaluation: https://cloud.google.com/blog/products/ai-machine-learning/introducing-agent-evaluation-in-vertex-ai-gen-ai-evaluation-service/
- Next '26: Gemini Enterprise Agent Platform announced 22 Apr 2026 as evolution of Vertex AI, with an "Optimize" pillar: Simulation (simulated human interactions pre-launch), Evaluation (continuous scoring of multi-turn conversations on live traffic), Observability, Optimizer (clusters failure patterns, suggests system-prompt revisions) — secondary coverage only: https://pasqualepillitteri.it/en/news/1311/gemini-enterprise-agent-platform-google-next-2026 , https://twimlai.com/articles/google-cloud-next-26-recap

## Evidence
- Docs pages contain "Evaluate a judge model" and "Configure a judge model" pages (titles seen in nav). No public agreement numbers found.
- Next '26 feature claims come from secondary write-ups; Google's own docs not fetched for Simulation/Optimizer.

## Limitations and criticisms
- Agent evaluation still Pre-GA in docs as of Oct 2026. Trajectory metrics require reference trajectories (ground truth), which most teams lack. Product renaming (Vertex → Agent Platform) adds churn.

## Relevance to agent evaluation
- Adaptive rubrics = per-task generated checklists, the cloud-scale version of TICK/rubric-judge research; directly usable for an agent-judge that must generate its own criteria per task. Autorater-vs-human validation is a first-class workflow at Google.

