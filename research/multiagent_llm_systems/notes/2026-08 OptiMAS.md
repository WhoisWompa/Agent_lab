---
title: OptiMAS: Automatically Optimize Multi-Agent System
authors: Yuxin Cheng et al.
date: 2026-08
arxiv: 2608.21918
url: https://arxiv.org/abs/2608.21918
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2608.21918.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "orchestration and delegation"]
---
# OptiMAS: Automatically Optimize Multi-Agent System

## One line
An LLM optimizer agent evolves a multi-agent system by reading its failed trajectories as a "textual gradient" and editing prompts, skills, tools and the agent graph step by step, instead of searching over branching candidates.

## Method
The problem: automated MAS design faces a trade-off. Widening what is evolved (prompts, topology, tools, agent roles) makes evolution unstable, and branch-and-discard search (ADAS, AFlow style) leaves insights stranded in separate lineages. The authors say hand-built systems still win in production for this reason (the claim is cited, not measured here).

The solution has three parts.

- **Shared infrastructure.** Every agent, in the evolving MAS and in the optimizer, is a ReAct agent. Delegation is a tool call: a parent assigns work to a sub-agent and receives the answer as an observation ("proactive assign-deliver"), so no workflow is hard-coded. The only constraint on the agent graph is that it is acyclic, which guarantees termination. Tools come from a predefined library, not generated code, to keep systems executable. The evolvable scope is the agent set, the graph, and each agent's backbone, prompt, skills and tools.
- **Training-style loop.** Queries are split into train, validation and test. Each step runs the current MAS on a batch of training queries and records full trajectories plus intermediate artifacts in a workspace. The optimizer reads that workspace, diagnoses root causes, and edits the configuration in one pass (diagnosis and update are not separated). It sees only the scalar validation accuracy, never validation trajectories, as an overfitting guard. Adaptive sampling re-draws earlier failures into the next batch (a fixed retry ratio) and re-weights queries by whether they were solved.
- **Dual-track memory.** Short-term: a plan whose items move through waiting, executing, completed or dropped; items cannot be erased, only dropped with a reason, and a programmatic check forces every item to a terminal status before the step ends. Long-term: a ledger of hypotheses (observation, proposed change, falsifiable expectation) moving through propose, enact, validate, refute or suspend. Every edit must cite a hypothesis, so a later step can verify or revert it. This addresses the optimizer forgetting, repeating failed edits, or mistaking noise for signal over million-token contexts.

## Evaluated on
- **Beats its own single-agent start in all 12 benchmark-backbone cells**, from +2.8 points (BrowseComp, GPT-5-Nano) to +45.4 (WorkBench, GPT-5-Nano: 18.6 to 64.0), with one task-agnostic configuration.
- **Gains shrink as the backbone gets stronger**: WorkBench +45.4 (GPT-5-Nano) versus +15.5 and +18.9 for the other two models; SWE-Bench +12.3 versus +4.4 (Gemini-3-Flash). Evolved orchestration mostly compensates for a weak model.
- **Matches or beats domain-specialised hand-built systems in most cells**: GAIA 87.1 vs 75.8 and BrowseComp 58.3 vs 48.3 against Tongyi-DeepResearch on Gemini-3-Flash; ahead of SWE-Agent on all three backbones.
- **Beats other evolutionary methods by wide margins**, e.g. up to 58.9 points over ADAS on SWE-Bench with Gemini-3-Flash. These baselines often fall below the plain single-agent start (ADAS on GAIA with Qwen 27.4 vs 73.1), which the paper does not explain.
- **Hypothesis memory matters most**: removing it drops SWE-Bench below the start (-7.2 on GPT-5-Nano, -7.8 on Qwen); removing adaptive sampling does the same on GPT-5-Nano (-5.0).
- **Smooth, small train-test gap** on WorkBench over 10 epochs (train +43 points on GPT-5-Nano), read as evidence against overfitting.

## Limitations admitted by the authors
- The framework needs a backbone with solid instruction following and tool calling; weaker models may not run it. Not tested on small models.
- Optimizer context length limits quality: a Qwen optimizer gains only +1.6 and +1.1 on GAIA and BrowseComp versus +8.1 and +9.9 for the Gemini optimizer, since long web trajectories degrade diagnosis.
- Cost is high: 1.4M to 3.2M tokens per optimization step, over 98% input. The evolved system then runs at normal cost.
- Only part of the design space was explored: curricula, dataset curation, agent diversity, and making prompt templates and tool creation optimization targets.

## Limitations found by others

## What it leaves untried
- No test of whether an evolved system transfers to a different task or domain; each was evolved and scored on its own benchmark split.
- Does not compare token cost against search-based baselines, so "sample-efficient" is unsupported by a measured cost comparison. Test sets are 100-query subsets for SWE-Bench and BrowseComp, so small gaps there (e.g. 11.1 vs 10.0 on BrowseComp) are within plausible noise.
- Tool creation is excluded (a fixed macro-library), leaving open whether the stability depends on that restriction.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - orchestration and delegation]]
