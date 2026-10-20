---
title: OpenInference semantic conventions and instrumentation
org: Arize AI
date: 2026-10
url: https://github.com/Arize-ai/openinference
kind: standard-or-regulation
category: eval-tooling
---
# OpenInference semantic conventions and instrumentation

## One line
OpenInference is Arize's OTel-compatible semantic convention and instrumentation set (span kinds LLM, TOOL, AGENT, RETRIEVER, etc.), used by Phoenix/AX and accepted by Weave and others.

## What they do
Adds AI-specific span-kind taxonomy on top of OTel; traces are valid OTLP; MCP instrumentation propagates context client→server (https://arize.com/docs/phoenix/release-notes/04.18.2025-tracing-for-mcp-client-server-applications).

## Evidence
GitHub 1,272 stars, Apache-2.0 (GitHub API 2026-10-20).

## Limitations and criticisms
Competes/overlaps with OTel GenAI conventions; two schemas to map.

## Relevance to agent evaluation
Listed; tracing interchange layer.

