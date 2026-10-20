---
title: Langfuse: open-source tracing + evals (2026 updates; acquired by ClickHouse)
org: Langfuse / ClickHouse
date: 2026-08
url: https://langfuse.com/changelog
kind: tooling-product
category: eval-tooling
---
# Langfuse: open-source tracing + evals (2026 updates; acquired by ClickHouse)

## One line
Langfuse is the most-starred open-source LLM observability/eval platform (36k stars), acquired by ClickHouse in Jan 2026, and through 2026 added categorical/boolean judges, GA code evaluators, a calibration skill, CI regression gating and evaluators exposed via MCP.

## What they do
- Acquisition announced 16 Jan 2026 (https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability ; https://github.com/orgs/langfuse/discussions/11593): "Same product, same endpoints, same contracts"; code outside ee/ stays MIT.
- 2026 changelog/blog items (https://langfuse.com/blog/2026-04-30-langfuse-april-update ; https://langfuse.com/blog/2026-05-31-langfuse-may-update ; https://langfuse.com/blog/2026-08-31-langfuse-august-update): categorical judge scores (23 Mar 2026), boolean scores (Apr); Experiments as top-level feature; an LLM-as-a-Judge calibration skill (with Codex) producing accuracy, F1, precision, recall and cost vs human labels; GitHub Actions experiments failing on score regression and posting to PRs; code evaluators GA 28 May 2026 ("code wins for objective checks, the judge wins for semantic quality"); multimodal evaluators (images, audio, PDFs) in Aug; stable v2 evaluator API (unstable API until 16 Nov 2026); evaluators and rules exposed via Langfuse MCP server (10 Jun 2026, https://langfuse.com/changelog/2026-06-10-evaluators-via-mcp). Annotation queues for traces/observations/sessions with API routing.
- Agent skills eval guide: https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills
- GitHub: 36,051 stars, last push 2026-10-20 (GitHub API).

## Evidence
- Pricing (beri.net, Aug 2026): Core $29/mo; $8 per 100k units to 1M; Teams add-on $300/mo; Enterprise $2,499/mo.
- CI: experiment-action should_fail_on_regression defaults true but only fails when your script raises RegressionError.

## Limitations and criticisms
- Self-hosting needs Postgres, ClickHouse, Redis/Valkey, S3 and two containers; RBAC/audit/masking need enterprise key (beri.net). A review says failure clustering and automatic eval generation are not native. Arize rates its trajectory support "partial".

## Relevance to agent evaluation
- Exposing evaluators and annotation queues over MCP means an agent can set up and run its own evals — infrastructure for agent-as-judge pipelines. The calibration skill operationalises judge-vs-human metrics.

