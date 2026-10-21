---
title: Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution
authors: Xing Zhang et al.
date: 2026-03
arxiv: 2603.11445
url: https://arxiv.org/abs/2603.11445
venue: ICLR 2026 Workshop on MALGAI
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2603.11445.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "self-refinement and critique loops"]
---
# Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution

## One line
VMAO splits a complex query into a dependency graph of sub-questions for specialised agents, has a separate LLM check whether the collected answers are complete, and replans the gaps until a stop condition fires.

## Method
The problem: market-research-style questions need data from many sources and several kinds of analysis. A single agent misses aspects, and static multi-agent pipelines cannot react when an early agent returns too little. The authors say earlier frameworks (debate, role-play, AutoGen, MetaGPT) lack verification of whether the group's combined results answer the original query. Self-refinement work checks only one response at a time.

The loop has five phases: plan, execute, verify, replan, synthesize.

- **Plan.** A planner LLM turns the query into sub-questions. Each has an agent type, dependencies, a priority and its own verification criteria. Agents sit in three tiers: data gathering (RAG, web, financial, competitor), analysis, and output (document, visualisation). They reach 42 tools through MCP servers.
- **Execute.** An executor runs every sub-question whose dependencies are done, three at a time. Upstream results are prepended to dependent questions. Tool-call caps and a 600 s timeout per run guard against loops.
- **Verify.** A verifier scores each result for completeness (0-1) and lists missing aspects and contradictions. It recommends accept, retry or escalate. It runs on a different, stronger model (Opus 4.5) than the executors (Sonnet 4.5), which the authors say reduces self-evaluation bias. Complete results are reused, not re-verified.
- **Replan.** Incomplete sub-questions are retried, and new ones are added for named gaps. Earlier partial results are merged with retries, not discarded.
- **Stop.** The loop ends on any of five conditions:
  - 80% of sub-questions complete;
  - 75% confidence with at least 50% complete;
  - less than 5% improvement between rounds;
  - a 1M-token budget;
  - 3 iterations.
- **Synthesize.** Large result sets are summarised per agent group, then merged with source citations.

The claim is that verification at the orchestration level works as a coordination signal that is independent of how each agent is built.

## Evaluated on
On 25 expert-written market-research queries, scored 1-5 by an LLM judge and then adjusted by human experts:

- **Completeness and source quality rise.** VMAO scores 4.2 and 4.1 against 3.1 and 2.6 for one agent holding all tools. A fixed pipeline (RAG, Web, Financial, Analysis, Synthesis) scores 3.5 and 3.2.
- **The cost is large.** VMAO uses 850K tokens and 900 s per query, against 100K and 165 s for the single agent and 350K and 420 s for the pipeline.
- **Gains depend on query type.** Open-ended strategic queries gain most (+53% completeness, 4.3 against 2.8 for the single agent as read from the figure). Performance-analysis queries gain less, because their data sources are well defined and a single agent finds them.
- **Most replanning is retry.** Retries of incomplete sub-questions outnumber new sub-questions. The authors read this as execution variance (tool failures, thin search results) causing more gaps than bad decomposition. No count is given.
- **Cost-based stops dominate.** Over 75% of queries ended on diminishing returns, max iterations or the token budget, not on the completeness threshold.

## Limitations admitted by the authors
- 25 queries and no confidence intervals, so the 3.1 to 4.2 gap has no stated uncertainty.
- The judge (Opus 4.5) and the executors (Sonnet 4.5) are the same model family, so shared bias may inflate the scores. Humans changed under 15% of LLM scores, typically by 0.5 points.
- No component ablation. The pipeline baseline lacks verification and replanning together, so their separate contributions are unknown.
- The verifier checks completeness, not truth. It can accept a claim that is present and sourced but wrong or hallucinated.
- A planner that misframes a sub-question can pass a well-sourced but irrelevant answer through the verifier.
- Tokens rise 8.5x over a single agent (850K against 100K), which may rule it out where latency or cost matters.
- Only Claude models were tested.

## Limitations found by others

## What it leaves untried
- A component-level ablation (verification alone, replanning alone, DAG alone). Without one, the central claim that verification drives the gain rests on a single comparison.
- A fixed token budget for the single-agent baseline. VMAO spends 8.5x the tokens, so the paper does not show that the gain is more than extra compute.
- Stop thresholds learned from execution traces. More than 75% of queries stop on the conservative cost-based thresholds, which suggests the hand-set values are not tuned. The authors name this as future work.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - self-refinement and critique loops]]
