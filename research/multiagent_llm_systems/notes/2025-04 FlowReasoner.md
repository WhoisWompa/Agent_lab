---
title: FlowReasoner: Reinforcing Query-Level Meta-Agents
authors: Hongcheng Gao et al.
date: 2025-04
arxiv: 2504.15257
url: https://arxiv.org/abs/2504.15257
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2504.15257.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "judges as reward signals"]
---
# FlowReasoner: Reinforcing Query-Level Meta-Agents

## One line
A 7B or 14B reasoning model is trained with reinforcement learning on code-execution feedback to write a separate multi-agent workflow for each user query, instead of searching for one workflow per task.

## Method
Earlier automatic design methods (ADAS, AFlow, MaAS) are task-level. A meta-agent searches a candidate set of workflows against a held-out search set and returns one fixed system for the whole task. The authors object that this is one-size-fits-all: it cannot give an easy query a small system and a hard query a larger one, and a single incoming query has no search set to search over.

FlowReasoner replaces the search algorithm with a trained reasoner. A system is code: agents plus a workflow built from a few operators taken from AFlow (code generate, ensemble, review, revise, code test). The meta-agent reads the query, reasons, and emits a system for that query. It then sees the execution result of the system it wrote and revises it, for 10 rounds.

Training has two stages:
- **Distillation warm-up.** DeepSeek R1-671B plays the meta-agent, producing multi-round reasoning plus workflows. About 1,400 such samples fine-tune DeepSeek-R1-Distill-Qwen-7B (and a 14B variant) so it can reason about workflow construction at all.
- **RL with GRPO.** Each round gets its own reward, so credit is assigned per round (process-style supervision) rather than at the end of the trajectory. The reward combines the test pass rate of the generated solution, a complexity score from the workflow's abstract syntax tree, and a diversity score for the workflow.

The assumption is that execution feedback, here unit-test pass rate, is a trustworthy signal. That is why the paper is limited to code. The intended payoff is that workflow structure adapts to the query and no search set is needed.

## Evaluated on
- Beats the best automatic baseline and its own worker. Overall accuracy on BigCodeBench, HumanEval and MBPP is 81.89 for the 14B model, against 76.81 for MaAS, 75.63 for AFlow and 71.37 for o1-mini used alone. That is the paper's "+10.52% over o1-mini".
- It beats hand-built workflows run on the same worker. Self-Refine, LLM-Debate and LLM-Blender with o1-mini score 70.63, 71.33 and 74.22 overall. Gains are largest on MBPP (92.15 vs 84.16 for MaAS).
- RL adds little over distillation, and the gain shrinks with size. At 7B, overall goes 78.89 to 80.53; at 14B, 81.50 to 81.89. Most of the gain therefore comes from the R1 distillation, not from RL. The paper does not discuss this.
- Scale matters: 14B beats 7B on all three benchmarks (81.89 vs 80.53 overall).
- The meta-agent trained with o1-mini workers transfers to other workers. With Claude 3.5 on BigCodeBench it scores 61.12, and with GPT-4o-mini 59.75, against 63.53 with o1-mini. Qwen2.5-Coder-32B drops to 52.67 on BigCodeBench.
- Case studies show a longer retry-and-ensemble workflow for a BigCodeBench task and a short generate-review-improve workflow for a HumanEval task. This is illustrative only, with no measure of how well structure tracks difficulty.

## Limitations admitted by the authors
- Scope is code generation only, because only code gives test cases to use as execution feedback. Whether the method works on tasks without a cheap executable check is untested.
- Untrained open-source models do badly as meta-agents without a predefined starting workflow, and produce error-prone workflows. For example, Qwen2.5-14B scores 15.26 and Qwen2.5-7B 12.68 on BigCodeBench, against about 57 to 63 for API models. This is the weakness the training is meant to fix.
- The model is trained against one worker (o1-mini) and is best with it. The Qwen2.5-Coder-32B worker costs about 11 points on BigCodeBench.
- Larger meta-agents work better, so the benefit depends on model scale.

## Limitations found by others

## What it leaves untried
- The reward includes complexity, but no cost or latency comparison is given against the search baselines. The efficiency claim for per-query systems, and for dropping the search algorithm, is therefore unsupported by numbers.
- No ablation of the reward terms (performance, complexity, diversity), so which term matters is unknown. The abstract and conclusion also say "efficiency" where the method section says "diversity".
- Inference-time feedback uses test cases or ground truth, which a real single user query may not have. How the meta-agent behaves with no tests is not tested.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - judges as reward signals]]
