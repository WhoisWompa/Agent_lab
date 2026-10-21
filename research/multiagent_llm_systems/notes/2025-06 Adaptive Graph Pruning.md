---
title: Adaptive Graph Pruning for Multi-Agent Communication
authors: Boyi Li et al.
date: 2025-06
arxiv: 2506.02951
url: https://arxiv.org/abs/2506.02951
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2506.02951.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "automated pipeline and topology search"]
---
# Adaptive Graph Pruning for Multi-Agent Communication

## One line
A small graph network, trained once, picks for each incoming task both which agents from a pool take part and how strongly they talk to each other, cutting prompt tokens while raising accuracy.

## Method
Problem: multi-agent systems use hand-made topologies (chain, tree, star, complete graph) or learn only edge weights over a fixed agent set (GPTSwarm, G-Designer). The authors' own reproductions found that accuracy peaks at a narrow team size on GSM8K, HumanEval and MMLU, and that adding "irrelevant" agents hurts both accuracy and cost. So who participates matters as much as how loudly they speak.

Idea: prune two things at once. Soft-pruning gives every directed edge a weight in [0,1] that throttles its bandwidth. Hard-pruning is a binary node mask that removes an agent entirely. Both heads sit on a shared two-layer graph-convolution encoder that embeds the agent profiles and the task text, so edge and node decisions stay consistent. The network is supervised, not searched per task.

Stage I builds the supervision. Random sub-teams of a 15-agent pool (roles such as Math Solver, Programming Expert, Critic, Doctor, Lawyer) are sampled, scored on a task, and the top two graphs per task are kept as labels, 460 in all. Stage II trains the network to reproduce them. Two losses are coupled because each alone fails: edge supervision cannot shrink a graph (all nodes stay active), and node-only sparsification collapses to a clique with no edge weighting. A Gumbel-sigmoid relaxation with annealed temperature lets gradients pass through the discrete choices. At inference one forward pass outputs the graph, with nodes kept if their mask score is at least 0.5. A decision agent aggregates a three-round dialogue.

Assumes a fixed heterogeneous pool, and that the labels mined from sampled teams are near-optimal for the task family.

## Evaluated on
- Best average accuracy, 91.04 on six benchmarks (MMLU, GSM8K, MultiArith, SVAMP, AQuA, HumanEval) with gpt-4o-mini, against 89.56 for G-Designer and 85.42 for the strongest single-agent baseline (self-consistency). It ranks first on five of six; on HumanEval it trails MetaGPT (90.93 vs 90.62).
- Fewer tokens at higher accuracy: on MMLU about 2.5e5 prompt tokens, 90% fewer than GPTSwarm, with 87.65 vs 82.8 accuracy. On GSM8K -65% tokens and +1.04; on HumanEval -22% tokens and +3.12. Against the architecture-search method MaAS it uses over half fewer tokens on GSM8K but is slightly behind on HumanEval, because MaAS keeps compile-and-test agents.
- Both levers matter: removing soft-pruning costs 4.16 / 4.88 / 4.99 points (MMLU / GSM8K / HumanEval); removing hard-pruning costs 2.45 / 3.45 / 2.21 and lengthens prompts by 22 to 30%.
- Trains quickly: MMLU accuracy rises from 80% to 88% in 10 updates; G-Designer peaks at 87% at step 34.
- Hand design is often not the optimum: of the 460 labels, 54% match what a human would wire, 43% are a subset of it, and 3% need an apparently unrelated agent (for example a Doctor and Programming Expert on a social-science question, outperforming every hand-picked team). The 3% figure is a count of labels, not a tested effect.

## Limitations admitted by the authors
- Only gpt-4o-mini is used in the main results, plus gpt-3.5-turbo on MMLU and GSM8K only (average 81.94, 0.29 above single-agent gpt-4). Transfer to other model families or scales is open.
- Efficiency analysis is thin; the authors say richer quantitative analysis is still needed.
- Text-only. Multimodal, embodied or tool-heavy tasks may expose asymmetric bandwidth and other problems.
- Beyond the stated limits, the supervision labels come from the same three task families as the test sets (200 + 100 + 160 pairs), and evaluation sets are small (153 MMLU questions, 164 HumanEval). The paper does not test unseen task types or give variance beyond averaging two runs.

## Limitations found by others

## What it leaves untried
- A pool or task family not seen in Stage I: the policy copies labels from three families, so whether it adapts to new tasks without re-mining labels is unmeasured.
- Per-query rather than per-task-family pruning is claimed, but no test shows the graph varying within one benchmark by difficulty.
- Training-cost accounting: Stage I fine-tunes and scores many sampled graphs, yet the training-efficiency claim counts only Stage II steps.

## Topics
[[Topic - communication topology and channels]] · [[Topic - automated pipeline and topology search]]
