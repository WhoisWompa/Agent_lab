---
title: Agent evaluators (Microsoft Foundry docs)
org: Microsoft
date: 2026
url: https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators
kind: tooling-product
category: production-practice
---
# Agent evaluators (Microsoft Foundry docs)

## One line
Microsoft's built-in LLM-judge evaluators for agents (task adherence, intent resolution, tool call accuracy) and continuous evaluation on production traffic.

_Added by eval-tooling researcher (2026-10-20):_ Microsoft Foundry ships the most granular built-in set of agent evaluators of any cloud: system-level (task completion, adherence, intent, navigation efficiency, customer satisfaction) and process-level (tool selection, input accuracy, output utilization, call success), mostly LLM-judged pass/fail.

## What they do
Task adherence (pass/fail vs system message, rules and prior steps; preview), intent resolution (preview), tool call accuracy (selection, parameter correctness, efficiency) with narrower tool-selection/tool-input evaluators; recommended bundle: tool call accuracy + task adherence + intent resolution + rubric + content safety. Continuous evaluation on production traffic with thresholds and automatic regression surfacing (https://azure.microsoft.com/en-us/products/ai-foundry/control-plane).

_Added by eval-tooling researcher (2026-10-20):_ Page ms.date 2026-09-30, updated 2026-10-08. Evaluators "function like unit tests" returning binary pass/fail (or 1-5 scores thresholded). Two best practices: system evaluation (end-to-end outcome) and process evaluation (step-by-step).
- System: Task Completion (preview, pass/fail), Customer Satisfaction (preview, 1-5 over six dimensions: helpfulness, completeness, clarity, tone, resolution, adaptability), Task Adherence (preview; rules, procedures, policy constraints from system message), Task Navigation Efficiency (deterministic, needs ground-truth expected_actions; matching modes exact_match / in_order_match / any_order_match; returns precision, recall, F1), Intent Resolution (preview, 1-5 thresholded).
- Process: Tool Call Accuracy (1-5), Tool Selection, Tool Input Accuracy (six strict criteria: groundedness, type compliance, format compliance, required params, no unexpected params, value appropriateness), Tool Output Utilization, Tool Call Success.
- Composite (preview): Output Quality and Tool Use Quality batch 5-6 evaluators into ONE LLM-judge call "to reduce cost and latency"; primary result passes only if all applicable components pass. Recommended judge: "a model from the GPT-5.6 family … For the lowest-cost option … use gpt-5.6-luna." The older single "Quality Grader" is deprecated.
- Turn-level vs conversation-level evaluation; inputs in OpenAI message schema with tool_definitions.
- Supported tools: File Search, function tools, MCP, knowledge-based MCP. Limited support (avoid tool evaluators) for Azure AI Search, Bing Grounding, Bing Custom Search, SharePoint Grounding, Code Interpreter, Fabric Data Agent, Web Search.

## Evidence
Docs; no agreement data for these judges.

_Added by eval-tooling researcher (2026-10-20):_ - All quotes from the Learn page above. Many evaluators still "preview" (no SLA, not recommended for production).
- No published human-agreement numbers for any agent evaluator on this page.

## Limitations and criticisms
Generic off-the-shelf judges are exactly what Husain/Shankar warn against without per-application validation. Naming differs across doc versions.

_Added by eval-tooling researcher (2026-10-20):_ - Built-in tool evaluators do not work on Microsoft's own hosted tools (Bing, Code Interpreter, Azure AI Search) — a notable gap.
- Composite evaluators trade per-dimension independence for cost; one judge call scoring six dimensions risks correlated errors (inference, not stated by Microsoft).
- Learn "foundry-classic" page says agent evaluation remains in public preview while model/dataset evaluation is GA (https://learn.microsoft.com/en-my/Azure/foundry-classic/concepts/observability).

## Relevance to agent evaluation
Represents the platform trend: canned agent judges applied to live traffic; their validity for a specific agent is left to the user.

_Added by eval-tooling researcher (2026-10-20):_ - A ready taxonomy for agent judging: outcome (task completion), policy (adherence), process (tool selection/inputs/output use/success), efficiency (trajectory vs expected). Task Navigation Efficiency's three matching modes are the industry-standard deterministic trajectory metrics (same as Vertex and AWS).

