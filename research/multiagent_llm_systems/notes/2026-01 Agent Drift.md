---
title: Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions
authors: Abhishek Rath
date: 2026-01
arxiv: 2601.04170
url: https://arxiv.org/abs/2601.04170
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2601.04170.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "role-based agent teams", "agent system failure analysis"]
---
# Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions

## One line
Names "agent drift" (multi-agent systems slowly degrading over hundreds of interactions with no weight change), proposes a 12-part stability score to monitor it and three mitigations, all supported only by simulation.

## Method
The problem: multi-agent systems are tested over short runs (typically under 50 turns), but in production they run for months. Behaviour can shift gradually through accumulated context, with no parameter update and no crash, so isolated checks miss it.

The paper defines three kinds of drift. Semantic drift is outputs moving away from the original intent while staying well-formed (for example, a financial report shifting from risk language to opportunity language). Coordination drift is consensus breaking down (for example, a router favouring some sub-agents and creating bottlenecks). Behavioral drift is new strategies appearing (for example, an agent caching results in chat history instead of the memory tool).

The measure is the Agent Stability Index (ASI). It is a weighted average of 12 normalised metrics in four groups: response consistency (0.30), tool usage (0.25), inter-agent coordination (0.25) and behavioral boundaries (0.20). The first 20 interactions set the baseline. Drift is flagged when ASI stays below 0.75 for three consecutive 50-interaction windows. The weights are given without justification.

Three mitigations:
- Episodic memory consolidation: a summariser compresses history every 50 turns.
- Drift-aware routing: the router prefers stable agents and resets drifting ones to their baseline prompt.
- Adaptive behavioral anchoring: baseline-period few-shot exemplars are added, and more are added when drift is higher.

The author's proposed causes are context pollution, distribution shift in a narrow domain, and autoregressive feedback, where an agent's own outputs become its future inputs. The paper does not test these causes.

## Evaluated on
Everything comes from simulated workflows (847 across enterprise automation, finance and compliance) that imitate GPT-4 and Claude behaviour. No real agent runs are reported.
- Drift is claimed to start early and speed up. Detectable drift (ASI below 0.85) appears after a median of 73 interactions, and the ASI decline rate rises from 0.08 to 0.19 points per 50 interactions between interactions 0-100 and 300-400.
- Drift is claimed to be costly. Drifted systems (ASI below 0.70) against stable ones (ASI above 0.85): task success 87.3% to 50.6%, human interventions 0.31 to 0.98 per task, inter-agent conflicts 0.08 to 0.47 per task, tokens 12,400 to 18,900.
- Susceptibility is claimed to track task ambiguity. Incidence by 500 interactions is 53.2% for finance, 39.7% for compliance and 31.8% for enterprise automation.
- Every mitigation is claimed to help. ASI after 200 interactions is 0.67 for controls, 0.81 for consolidation, 0.84 for routing, 0.86 for anchoring and 0.89 for all three combined (81.5% drift reduction). The combination adds 23% compute and 9% completion time.
- Architecture is claimed to matter. Two-level router-plus-specialist hierarchies beat flat and 3+ level ones, and explicit long-term memory gives 21% higher ASI retention. Mixed-model teams are "slightly" more stable, with no figure given. Sync versus async shows no significant difference (p = 0.13).

## Limitations admitted by the authors
- Domain: the author states the data come from enterprise and financial settings, so creative or research tasks may drift differently.
- Model coverage: only GPT-4 and Claude 3 behaviour is covered, and newer or open models may differ.
- Timescale: the longest window is 18 months, so it is unknown whether drift levels off or continues.
- Mitigation space: only three interventions were tried.
- Causality: the author says the evidence is correlational and the mechanisms are "partially speculative". No ablations were run.

## Limitations found by others

## What it leaves untried
- Measuring drift in real deployed agents. The paper's own numbers (the "42%" success drop, "67-81%" error reduction) are projections from a simulator whose parameters presumably encode the effects being claimed. The simulator, code and data are promised only "upon request" or "upon publication".
- Validating ASI against human judgment of degradation. The paper does not show that the 12 metrics, weights and 0.75 threshold track real quality loss, and the author concedes that embedding-based consistency is less sensitive to subtle semantic shifts.
- Testing the three proposed causes in isolation, for example by comparing growing context with periodically reset context at equal interaction counts. Without that, the claimed fit between each mitigation and its cause is argument, not evidence.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - role-based agent teams]] · [[Topic - agent system failure analysis]]
