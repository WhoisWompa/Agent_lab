---
title: Arize AX (commercial) and Arize Phoenix (open source)
org: Arize AI
date: 2026-08
url: https://arize.com/resources/llm-and-agent-evaluation-platforms/
kind: tooling-product
category: eval-tooling
---
# Arize AX (commercial) and Arize Phoenix (open source)

## One line
Arize splits into Phoenix (ELv2 source-available, OTel/OpenInference-native tracing and evals, ~11.9k stars) and Arize AX (managed enterprise platform with Alyx, an AI agent that builds and refines evaluators), and documents a 'Human vs AI' judge-alignment workflow.

## What they do
- Arize's own comparison (updated 13 Aug 2026) of AX, Phoenix, LangSmith, Braintrust, Langfuse, W&B Weave, Opik: AX does span, trace, trajectory and session evals online and offline; Phoenix OTel-native with OpenInference schema, Elastic License 2.0, prompt management (Apr 2025), plugin system for custom judges.
- Alyx: "Arize's AI agent for working with application telemetry and evaluations" — finds failing examples, builds/refines/tests evaluators; on Google Cloud Marketplace.
- Judge alignment cookbook (https://arize.com/docs/ax/cookbooks/evaluate/align-llm-evals-with-human-judgment): labelled dataset from agent traces, human annotations as ground truth, "Human vs AI" evaluator to measure judge accuracy, iterate.
- MCP tracing: openinference-instrumentation-mcp propagates context client→server so both join one trace (Phoenix release notes 18 Apr 2025, https://arize.com/docs/phoenix/release-notes/04.18.2025-tracing-for-mcp-client-server-applications).
- Acquired Velvet (Mar 2025, https://siliconangle.com/2025/03/13/arize-ai-acquires-velvet-expand-support-ai-observability-llm-evaluation/).

## Evidence
- Comparison page is vendor-authored; it ranks AX first for enterprise and claims Phoenix offers "deeper support for agent evaluation" than Langfuse without benchmark; inconsistently rates Phoenix online eval as "Limited" in table vs supported in text.
- Phoenix: 11,910 stars; GitHub reports license NOASSERTION (ELv2) (GitHub API 2026-10-20).

## Limitations and criticisms
- License confusion: some third-party sources call Phoenix Apache 2.0, others ELv2 (consolidation article flags ELv2 as less forkable, https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026). SSO/RBAC/audit only in AX.

## Relevance to agent evaluation
- OpenInference + trajectory/session evals + an agent (Alyx) that writes evaluators — again the "agent builds the judge" pattern.

