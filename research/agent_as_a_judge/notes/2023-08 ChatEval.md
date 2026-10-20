---
title: ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate
authors: Chi-Min Chan et al.
date: 2023-08
arxiv: 2308.07201
url: https://arxiv.org/abs/2308.07201
venue: ICLR 2024
category: alternative-paradigms
---
# ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate

## One line
Multi-agent referee team: several LLM agents with different personas debate the quality of a response before giving a verdict.

## Method
Several LLM judges with distinct role prompts (e.g. critic, psychologist, public) take turns in one-by-one, simultaneous or summariser communication; final verdict by aggregation. Sees only the output text; no tools, no execution.

## Evaluated on
Open-ended QA (FairEval pairs) and dialogue response generation (Topical-Chat); reported higher accuracy and correlation with human judgements than single-agent GPT-3.5/GPT-4 judges (numbers not re-verified this session).

## Limitations admitted by the authors
- Diverse role prompts are essential: the same role for all agents degrades performance (authors' ablation).
- Cost grows with agents and turns.
- Cost scales with agents and rounds; diversity of personas matters.

## Limitations found by others
- Choi et al. 2025 (arXiv 2508.17536): in multi-agent debate generally, majority voting explains most of the gain; debate alone is a martingale and does not raise expected correctness.
- JudgeBench (arXiv 2410.12784) included multi-agent judges and found them near random on hard objective pairs, like single judges.
- JudgeBench (2410.12784): ChatEval 34.0% on hard objective pairs, below single GPT-4o (50.9-56.6%).

## What it leaves untried
- Agents that can execute or retrieve during the debate; application to agent trajectories.
