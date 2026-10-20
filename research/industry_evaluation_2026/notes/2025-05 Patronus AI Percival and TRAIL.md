---
title: Patronus AI: Percival agent debugger and TRAIL trace-error benchmark
org: Patronus AI
date: 2025-05
url: https://patronus.ai/blog/introducing-trail-a-benchmark-for-agentic-evaluation
kind: tooling-product
category: eval-tooling
---
# Patronus AI: Percival agent debugger and TRAIL trace-error benchmark

## One line
Patronus markets Percival, an agent that reads full agent traces to localise 20+ failure modes, and published TRAIL, a benchmark showing frontier LLMs are poor at finding errors in agent traces (best Gemini 2.5 Pro ~11%).

## What they do
- TRAIL (arXiv 2505.08638): 148 annotated traces (from GAIA and SWE-Bench Lite), 841 errors across reasoning, execution, planning; best model gemini-2.5-pro "a mere 11%" (https://arxiv.org/html/2505.08638v2 ; https://huggingface.co/datasets/PatronusAI/TRAIL).
- Percival (https://venturebeat.com/ai/patronus-ai-debuts-percival-to-help-enterprises-monitor-failing-ai-agents-at-scale): detects 20+ failure modes in four categories; framed as an agent (tracks all events across the trajectory) rather than an LLM-as-judge; customer claim: analysis time from ~1 hour to 1–1.5 minutes (vendor).
- Earlier products: Lynx hallucination judge, Glider judge model, hosted judges billed per call (per https://shurco.ai/guides/best-ai-agent-evaluation-tools/).

## Evidence
- No published Percival accuracy on TRAIL. By 2026 Patronus's homepage reportedly focuses on RL research (developersdigest consolidation article).

## Limitations and criticisms
- Time-saving claims are vendor marketing. Pivot suggests eval-only positioning was hard to sustain.

## Relevance to agent evaluation
- TRAIL is the key evidence that judging agent traces is hard: an 11% localisation score means a single LLM call is not a reliable trace judge; argues for agentic judges with tools/memory.

