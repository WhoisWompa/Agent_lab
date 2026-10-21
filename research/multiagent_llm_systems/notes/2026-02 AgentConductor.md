---
title: AgentConductor: Topology Evolution for Multi-Agent Competition-Level Code Generation
authors: Siyu Wang et al.
date: 2026-02
arxiv: 2602.17100
url: https://arxiv.org/abs/2602.17100
venue: arXiv (preprint)
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2602.17100.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "automated pipeline and topology search", "communication topology and channels"]
---
# AgentConductor: Topology Evolution for Multi-Agent Competition-Level Code Generation

## One line
A small RL-trained orchestrator writes, for each code problem, a layered agent graph sized to the problem's difficulty, then rewrites it after seeing execution failures.

## Method
Problem: multi-agent code systems either use one fixed topology (costly on easy problems) or prune or generate a topology once per task (G-Designer, AgentPrune). None of these scales density with difficulty, and none revises the graph within one problem using test feedback.

Idea: a 3B orchestrator (Qwen-2.5-Instruct) reads the problem, infers a difficulty level (easy, medium, hard) and picks roles from a fixed pool: planner, searcher, algorithmer, coder, tester, debugger. It emits the topology as YAML: each `step` is a layer, each `ref` an edge to earlier agents, so the graph allows parallel agents within a layer and edges across layers. The agents run in a sandbox. If the code fails, the failure output and history go back to the orchestrator, which generates a new topology for the same problem (two turns in training).

Training has two stages. SFT on GPT-4o-generated topologies (4,500 examples) teaches the YAML format and the density bands. GRPO then optimises a rule-based reward with two parts:
- Execution reward: fixed penalties for malformed YAML (-2.0 to -0.5) and graded scores for code outcomes (passed 1.5, wrong answer 1.0, down to compile error 0.6).
- Density reward: a score `Scomplex` built from node count, edge count relative to a complete graph, and depth. Each difficulty level has a node cap (4, 7 or 10 per turn); going over the cap is penalised. The caps come from statistics of the SFT samples that solved problems, so density follows difficulty instead of collapsing to one sparse shape.

At inference the orchestrator is frozen.

## Evaluated on
- Beats every topology and workflow baseline on pass@1 across five code benchmarks: APPS 58.8 (the text claims a 14.6-point margin, but its own table lists MetaGPT at 51.3, a 7.5-point gap), LiveCodeBench 46.3 (+3.1), CodeContests 38.8 (+1.1), HumanEval 97.5 (+1.0), MBPP 95.1 (+0.7). Gains are large on APPS and small on the others.
- Cheaper on APPS than the cost-comparable baselines: 277,600 prompt and 79,800 completion tokens, against 334,650 and 134,250 for Chain-of-Agents (32B), the best baseline on accuracy among the workflow methods. It also has the sparsest average graph (Scomplex 5.2 vs 4.1 for the next).
- Density tracks difficulty: sparser graphs on easy problems, denser on hard ones. The paper says competing methods show little or no such adaptation (shown in a figure, no numbers in the text).
- SFT is needed for valid output: without it only 15% of APPS topologies are valid. Without RL, valid topologies are 56.5% and pass@1 is 29.8, against 100% and 58.8 for the full model.
- The density reward helps accuracy as well as cost: removing it drops APPS to 52.6, and the validity rate falls from 100% to 83.2%.
- Zero-shot transfer is weak evidence: 15.8% success on 50 text-only GAIA samples with two new roles added and no retraining.

## Limitations admitted by the authors
- The method targets competition-level code. Other domains need retraining with a different validator and a binary reward; the zero-shot GAIA result (15.8% on 50 samples) is small and has no baseline in the text read.
- Difficulty caps (4/7/10 nodes) were set from statistics of the SFT samples. They are hand-chosen per level and fixed for two turns, so the density control inherits that data's bias.
- Valid topologies are not guaranteed without training. Skipping SFT or RL leaves 15% or 56.5% valid, so the format and density rules are learned, not enforced.

## Limitations found by others

## What it leaves untried
- It does not test which part of the gain comes from the layered DAG shape and which from the learned difficulty adaptation, for example by running a fixed layered graph with the same roles and feedback loop.
- Training and evaluation use two turns of revision; more turns and the point where extra rounds stop helping are not studied.
- The model behind the worker agents and the cost of the orchestrator itself are not broken out in the text read, so the token comparison to baselines may not be like for like (unsupported).

## Topics
[[Topic - orchestration and delegation]] · [[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]
