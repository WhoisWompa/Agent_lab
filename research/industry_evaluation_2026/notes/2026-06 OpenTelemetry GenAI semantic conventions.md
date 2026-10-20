---
title: OpenTelemetry GenAI (and MCP) semantic conventions
org: OpenTelemetry GenAI SIG
date: 2026-06
url: https://github.com/open-telemetry/semantic-conventions-genai
kind: standard-or-regulation
category: eval-tooling
---
# OpenTelemetry GenAI (and MCP) semantic conventions

## One line
The OTel GenAI semantic conventions (model, agent, tool, MCP spans) are the de facto tracing interchange for LLM/agent observability but remain 'Development' status as of mid/late 2026, and moved to their own repo in June 2026.

## What they do
- GenAI conventions deprecated in main semantic-conventions v1.42.0 (12 Jun 2026) and moved to open-telemetry/semantic-conventions-genai (https://www.greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions ; https://www.dash0.com/knowledge/opentelemetry-genai-semantic-conventions-explained).
- v1.41 changed agent spans, e.g. splitting invoke_agent into CLIENT/INTERNAL (Greptime).
- MCP conventions: W3C trace context carried in MCP `_meta` field (also SEP-414, https://modelcontextprotocol.io/seps/414-request-meta.md); span names like `tools/call get_invoice` (third-party blog https://mcpplaygroundonline.com/blog/mcp-observability-opentelemetry).

## Evidence
TrueFoundry (22 Aug 2026) and Klu (Aug 2026) say all GenAI spans/attributes still 'Development'; one outlier (Business Tech Navigator, Jun 2026) claims stabilisation — unconfirmed and contradicted.

## Limitations and criticisms
Instability forces pinning versions; attribute renames break dashboards.

## Relevance to agent evaluation
Every cloud (Foundry, AgentCore code evaluators get OTel spans) and most vendors ingest OTel — an agent-judge consuming OTel GenAI spans is portable across backends.

