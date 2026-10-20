---
title: Build 2026: From observability to ROI for AI agents on any framework
org: Microsoft
date: 2026-06
url: https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/
kind: tooling-product
category: eval-tooling
---
# Build 2026: From observability to ROI for AI agents on any framework

## One line
Microsoft's Build 2026 post (3 Jun 2026) declares Foundry tracing + evaluations GA and previews user simulation, multi-turn eval, a rubric evaluator, intelligent trace sampling, traces-to-dataset and an agent optimizer.

## What they do
- GA: tracing and evaluations core ("reached GA this spring"). A third-party blog dates GA to March 2026 (https://jannikreinhard.com/microsoft-foundry-agent-evaluations/); M365 message AZ525985 describes GA Observability in Foundry Control Plane with "evaluations (adhoc, continuous on production traffic and scheduled to detect drift)" (https://mc.merill.net/message/AZ525985). Tech Community says AI Red Teaming Agent is GA (https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/-/4467885).
- Public preview: tracing/evals for any framework via OpenTelemetry (LangChain, LangGraph, OpenAI SDK, Microsoft Agent Framework, custom); user simulation (multi-turn conversations and edge cases); multi-turn evaluation; rubric evaluator (context-aware criteria weighted across task success, tone, safety, cost, latency); intelligent trace sampling; trace replay/visualisation; traces to dataset.
- Private preview: Agent optimizer (searches configurations, ranks candidates against your rubric with diffs/lineage/rollback); ROI for agents.

## Evidence
- Vendor launch post; no judge accuracy data. No judge-calibration feature mentioned.

## Limitations and criticisms
- Many pieces preview-only; Microsoft also shipped "Evals for Agent Interop" starter kit (Jan 2026, https://devblogs.microsoft.com/microsoft365dev/?p=25113) — not examined in depth.

## Relevance to agent evaluation
- Shows hyperscalers now bundle the full "independent vendor" feature set (OTel tracing, online eval, simulation, rubric judges, optimizer) into the cloud console, framework-agnostic via OTel.

