---
title: Towards a Science of Scaling Agent Systems
authors: Yubin Kim et al.
date: 2025-12
arxiv: 2512.08296
url: https://arxiv.org/abs/2512.08296
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2512.08296.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "orchestration and delegation"]
---
# Towards a Science of Scaling Agent Systems

## One line
A controlled comparison of one single-agent and four multi-agent coordination structures shows that adding agents helps or hurts depending on task structure and the single-agent baseline, and fits a regression that picks the best architecture for 87% of held-out configurations.

## Method
The problem: claims that "more agents is all you need" come from studies that vary prompts, tools and budgets together with architecture, and mostly use static benchmarks where voting fixes errors. Nobody can say when coordination pays.

The paper fixes prompts, tools and total reasoning budget (about 4,800 tokens per trial) and varies only the coordination structure: single agent (SAS), Independent (parallel agents, outputs concatenated, no communication), Centralized (orchestrator over workers, which checks work before aggregating), Decentralized (all-to-all debate rounds), and Hybrid (orchestrator plus peer links). Each is crossed with nine models from three families on six agentic benchmarks (260 configurations). Agentic means sequential interaction with an environment under partial observability.

It then measures coordination from execution traces: overhead relative to the single agent, message density, redundancy, efficiency (success divided by relative turns), and error amplification (extra work caused by coordination failures). A regression on model capability, tool count, single-agent baseline and these measures predicts performance without dataset-specific parameters.

The mechanism offered: a fixed budget split across agents leaves each too little for tool-heavy or sequential reasoning, while an orchestrator that checks outputs before aggregation catches errors that parallel agents pass through.

## Evaluated on
- Gains depend on task structure: Finance Agent (decomposable) rises +80.8% under Centralized (0.631 vs 0.349), while PlanCraft (sequential) falls 39% to 70% under every multi-agent variant. The mean multi-agent change across all benchmarks is -0.3%, with a 95% interval of -58.7% to +77.2%.
- Capability saturation is the most robust effect: when the single agent already scores above about 45%, extra agents give negative returns (interaction coefficient -0.236, p=0.004). It is the only predictor that survives both cluster-robust inference (p=0.004) and Holm correction (p=0.018). On SWE-bench Verified and Terminal-Bench the threshold matches 94% of 16 model-benchmark cells.
- Tool-heavy tasks pay a coordination tax: efficiency-by-tool-count interaction -0.096 (p=0.002). Single-agent efficiency is 0.466 against 0.074 to 0.234 for multi-agent, a 2 to 6 times penalty.
- Centralized verification contains errors: trace-level amplification is 17.2x for Independent and 4.4x for Centralized (Decentralized 7.8x, Hybrid 5.1x). Multi-agent variants that check work cut factual errors by 22.7% on average.
- Cost grows fast: turns scale as roughly (n+0.5)^1.72. Hybrid needs 6.2x the single agent's turns (44.3 vs 7.2) and 5.0x worse success per token, with no significant gain over Centralized.
- Prediction: cross-validated R2 is 0.373 (0.413 when capability is measured as the model's own mean single-agent score across the six benchmarks). The model picks the best architecture for 87% of held-out configurations, against 54% for a capability-only model and 20% for random choice.

## Limitations admitted by the authors
- Absolute performance transfers poorly across domains: leave-one-dataset-out validation is weak, and only the ranking of architectures transfers (87%).
- Only six benchmarks, so six clusters. Several predictors lose significance under cluster-robust errors (standard errors up to 2.9 times larger), including the tool-efficiency effect, so they are reported as directional.
- SWE-bench Verified and Terminal-Bench use 20-instance subsets with bootstrap intervals about +/-20 points per cell, so single comparisons there are underpowered.
- Prompts were identical rather than tuned per model, so architecture-specific tuning could change the picture.
- Teams are mostly same-family models. A 13-configuration mixing test found no escape from saturation: centralized mixes underperformed strong-model teams by 12.6 points on average.
- Team size beyond nine and non-text domains are untested. Family differences (Google, OpenAI, Anthropic) are stated as signatures with no isolated cause.

## Limitations found by others

## What it leaves untried
- Larger teams and emergent specialisation: the authors measure a super-linear overhead but stop at nine agents, so whether scale ever pays is open.
- Cheaper channels than natural-language tokens (latent or activation sharing, sparse communication). The authors suggest these could change the cost curve but do not test them.
- Protocols built for tool-heavy tasks (tool scheduling, capability-aware routing), where the tax is largest. This is named as a direction only.

## Topics
[[Topic - communication topology and channels]] · [[Topic - orchestration and delegation]]
