---
title: AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent (TEA) Protocol
authors: Wentao Zhang et al.
date: 2025-06
arxiv: 2506.12508
url: https://arxiv.org/abs/2506.12508
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2506.12508.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation"]
---
# AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent (TEA) Protocol

## One line
A protocol that treats tools, environments and agents as versioned, lifecycle-managed components, plus a hierarchical planner-and-sub-agents system built on it that reaches 89.04% on the GAIA test set.

## Method
The paper argues that MCP (tools) and A2A (agent messaging) leave three gaps: context and versions are scattered across prompts and logs, nothing in the protocol lets components improve from execution feedback, and environments (browser, file system, code runtime) are not first-class, so switching or isolating them becomes glue code.

The TEA protocol fills these gaps with three context protocols (Tool, Environment, Agent), each with a context manager (lifecycle, versioning, embedding-based retrieval) and a server. Six basic managers sit underneath: model, prompt, memory, dynamic code, version and tracer. Six transformations (agent-to-tool, tool-to-agent, environment-to-tool, tool-to-environment, agent-to-environment, environment-to-agent) let a component take another role. For example, a deep-research workflow is packaged as a search tool, or a toolkit is promoted to an environment. A self-evolution module treats prompts, component code and successful solutions as variables. It refines them with textgrad or self-reflection and registers each result as a new version, so later tasks use it and old versions can be rolled back.

AgentOrchestra is the instantiation. A central planning agent decomposes the goal, keeps a plan it can create, update or mark complete, and delegates to five sub-agents: deep researcher, browser use, deep analyzer, tool generator and reporter. The claimed advantage over flat orchestration is that the planner makes localized routing decisions. Each sub-agent exposes only a curated toolset and local context, so the planner does not choose from a growing global pool or collect irrelevant context. The planner replans on errors. The tool generator writes new tools when it finds a capability gap and reuses them later.

## Evaluated on
- Leading GAIA results. The evolved variant scores 89.04% on test, with 85.53% on Level 2 and 81.63% on Level 3. On validation it scores 93.33%, against 87.27% for agent-2030 and Alita, and 89.70% for the variant without self-evolution.
- Competitive on HLE. It scores 59.6, up from 55.2 without evolution. It is above GPT-5.4 Pro (58.7) and below Claude Mythos Preview (64.7).
- Each sub-agent adds measurable accuracy in a cumulative GAIA test ablation. The planner alone scores 36.54, adding the researcher gives 57.14, the browser agent 72.76, the analyzer 79.07, and the tool generator 89.04. The tool generator's gain is largest at Level 3, from 61.22 to 81.63.
- Self-evolution helps even with only the analyzer agent. GPQA improves on all five backbones. AIME25 improves on four of five, and AIME24 improves on four of five (grok-4.1-fast is flat). The largest gains are on weaker models: gpt-4.1 gains 71.38% on AIME24 and gpt-4o doubles its AIME25 score from 6.67 to 13.34.
- Cost scales with difficulty. Simple tasks take about 30 s and 5k tokens, and complex ones about 10 min and 100k tokens.
- The tool generator produced over 50 tools with a 30% reuse rate.

## Limitations admitted by the authors
- Learning curve. The abstraction layer is heavier than ad-hoc scripting. The paper gives no measurement of this.
- Protocol overhead. Standardized interaction may add latency for real-time use. No overhead figure is reported.
- Dependence on the base model. Orchestration cannot fix hallucinations or poor tool use. Weaker backbones start much lower in the reasoning tests (gpt-4o 13.34 on AIME24 versus 96.67 for grok-4.1-fast).
- Security and misuse. Browser and terminal control could leak private data or take irreversible actions. The authors advise sandboxing and human-in-the-loop checks, and the paper does not evaluate any safeguard.

## Limitations found by others

## What it leaves untried
- No test of the hierarchy against a flat orchestrator with the same sub-agents. The localized-routing benefit is argued and never measured, since the ablation only adds agents cumulatively.
- No measurement of what the protocol layer itself contributes. All results are for one system, with no run of the same agents on plain MCP/A2A glue. The comparison with other protocols is a feature table.
- No ablation of the evolution methods or of the leaderboard comparisons' cost and step budgets. Evolved and vanilla variants are compared, but textgrad versus self-reflection is not, and the main tables use self-reflection. Rival systems use different backbones, so the system-versus-model contribution is unclear.

## Topics
[[Topic - orchestration and delegation]]
