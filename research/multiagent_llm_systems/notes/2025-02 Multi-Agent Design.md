---
title: Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies
authors: Han Zhou et al.
date: 2025-02
arxiv: 2502.02533
url: https://arxiv.org/abs/2502.02533
venue: ICLR 2026
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2502.02533.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search"]
---
# Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies

## One line
MASS searches for a multi-agent system by optimizing prompts and topology in three interleaved stages (per-block prompts, pruned topology search, whole-workflow prompts), and beats hand-built and auto-designed systems.

## Method
The problem: a multi-agent system (MAS) has two coupled design spaces, the prompt of each agent and the topology that wires agents together. Searching both jointly is combinatorial. Cascaded agents have no ground truth for intermediate outputs, and the reward gets sparser as agents are added. Prior automatic designers (ADAS, AFlow) search topologies and leave prompts hand-written.

Two analyses motivate the design. First, prompt optimization on a single agent buys more accuracy per token than scaling agents with self-consistency, self-refine or debate; those saturate earlier. Self-consistency on top of a prompt-optimized agent keeps scaling. Second, most topology blocks do not help. On HotpotQA only debate helps (+3%); the others add nothing or hurt. On LiveCodeBench test-output prediction, one block costs 15%. The search space is therefore mostly dead weight.

MASS turns this into three stages, local to global:
1. **Block-level prompt optimization.** Warm up a single predictor, then optimize each building block (aggregate, reflect, debate, plus task-specific summarize and tool-use) at its minimum size, for example two predictors and one debator. Each block's validation gain over the base agent is recorded as its "influence".
2. **Workflow topology search.** Influence is softmaxed into a selection probability per block. Low-influence blocks are randomly rejected, which prunes the space. Workflows are sampled under an agent budget, blocks are placed in a fixed order (summarize, reflect, debate, aggregate), and the best of 10 sampled topologies is kept.
3. **Workflow-level prompt optimization.** Prompts are tuned jointly on the winning topology, so agents adapt to each other's outputs.

The prompt optimizer (MIPRO, instructions plus bootstrapped demonstrations) is swappable. Stages 1 and 2 can run in parallel, which iterative ADAS and AFlow cannot.

## Evaluated on
- Beats the baselines across 8 tasks (math, DROP, three multi-hop QA sets, three coding sets). Average 78.8 against 70.3 for the best baseline (multi-agent debate) on Gemini 1.5 Pro, and 74.3 against 65.9 on Flash. Cost is matched at a maximum of 10 agents. Gains reported as consistent on Claude 3.5 Sonnet and Mistral Nemo.
- Each stage adds something. Averaged over the 8 tasks on Pro: single-agent prompt optimization 68.0, block-level 74.2, plus topology 77.3, plus workflow prompts 78.8. Block-level is about 6 points above single-agent optimization.
- Both design choices matter. On HotpotQA, topology search without prior prompt optimization or without pruning is worse than the full pipeline (shown in a figure only; no numbers in the text).
- The auto-design baselines are weaker. ADAS gives subtle gains and drifts toward over-complex topologies. AFlow has high MCTS variance and does not optimize its operators' prompts. AFlow is close on 2WikiMQA and HumanEval. AFlow's meta-prompt only worked with Claude as optimizer, so its numbers are "for reference".
- Prompt optimization is the larger lever. On MATH with Flash, swapping the optimizer moves the result: 73.3 (APE), 78.2 (DSPy), 81.0 (MIPRO) against 66.7 for CoT. Against GPTSwarm graph optimization, MASS gains 8 points on MATH and 6 on HumanEval, as the authors read it because graph pruning improves efficiency more than accuracy.
- Training cost is called comparable to ADAS and AFlow (details in an appendix table).
- Design principles drawn from found systems: optimize agents before composing them; compose only influential topologies; tune prompts jointly afterward. On MATH the search found that debate won at block level, but more parallel aggregating agents beat it once composed.

## Limitations admitted by the authors
- The topology space is limited to serial, parallel and fully-connected mixtures. Other topologies could help. The fully-connected debate block is wasteful, since sparse communication is known to work, but sparsification is not tried.
- Topology search is random rejection sampling over 10 candidates. A Bayesian optimizer might be more sample-efficient in a richer space, but this is not tested.
- The prompt optimizer ignores textual error feedback. The authors expect feedback-based optimizers (ProTeGi, TextGrad) to be more sample-efficient; this is untested.

## Limitations found by others

## What it leaves untried
- Influence is measured per block in isolation and then used as an independent selection weight. Interactions between blocks (debate plus aggregate) are not modeled, although the MATH trajectory shows block-level rank can reverse after composition.
- One searched system per task, fixed by the validation set. A system chosen per query is not tried, and the paper itself cites MaAS as concurrent work doing that.
- Ordering of blocks is fixed by hand. Reordering is not searched, so the fixed order caps the topologies reachable.

## Topics
[[Topic - automated pipeline and topology search]]
