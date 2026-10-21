---
title: "ScoreFlow: Mastering LLM Agent Workflows via Score-based Preference Optimization"
authors: Yinjie Wang et al.
date: 2025-02
arxiv: 2502.04306
url: https://arxiv.org/abs/2502.04306
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2502.04306.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "judges as reward signals"]
---
# ScoreFlow: Mastering LLM Agent Workflows via Score-based Preference Optimization

## One line
Trains a small open-weight LLM to write a task-specific multi-agent workflow as code for each input, using a DPO variant (Score-DPO) that learns from the numeric scores of executed workflows.

## Method
The problem: automated workflow search (ADAS, AFlow) optimizes one workflow for a whole task set with discrete search driven by a paid API model. The authors say this limits adaptivity (easy and hard problems get the same structure), scalability to mixed datasets, and cost. AFlow also converges too fast on a structure, which restricts exploration (a claim made without a measurement).

ScoreFlow replaces the search with a trained generator G. G (Llama-3.1-8B-Instruct) reads a task plus a description of the allowed operators (programmer, reviewer, ensemble, test, a custom operator whose prompt G can rewrite) and emits a Python workflow with loops and conditionals. A separate executor model (GPT-4o-mini) runs it, and a third-party score in [0,1] (solve rate or F1 against a dataset) comes back. G never grades itself, which avoids a self-referential loop.

Each round, 8 workflows are sampled per problem and ranked by score into preference pairs. Plain DPO converged slowly because scores are noisy: a pair with a small score gap may be mis-ordered. Score-DPO changes two things:
- Pairs are sampled in proportion to a cubic of the score gap, so confidently ordered pairs dominate.
- The implicit reward of the winner is scaled by its score and the loser's by one minus its score, so the loss uses the score values and not only the ordering.

A theorem shows each sample's gradient influence then rises with its score, provided the implicit reward |r| is at most 1. The authors measure that this holds 91.1% of the time on average during training (82.2% on DROP).

## Evaluated on
- Beats every static and automated baseline on six benchmarks: 85.3 average vs 80.6 for AFlow and 76.0 for plain prompting (8.2 points over the best baseline as the paper counts it). The generator is an 8B model, while AFlow and ADAS use GPT-4o-mini to design workflows.
- Score-DPO beats other training rules inside the same pipeline: MATH test 64.4 vs 60.4 for DPO, 55.2 for PPO and 54.8 for SFT. The paper's reason for PPO's weakness (diluted gradient over long sequences) is asserted, not tested.
- The gain over AFlow widens on a mixed GSM8K, MBPP and DROP set (ScoreFlow 88.1% on the combined task). This is the only evidence for the scalability claim, and it uses one mix of three datasets.
- Weaker executors with ScoreFlow workflows beat GPT-4o with chain-of-thought on HumanEval, which the paper presents as cost-efficiency.
- Optimization is cheaper than AFlow: $2.26 vs $4.61 with GPT-4o-mini as executor. Convergence comes as early as the second of three iterations.
- Exponent ablation on the gap weight: cubic gives 64.4 on MATH vs 60.4 for DPO (exponent 0), and an exponent of 100 drops to 59.2, below DPO.

## Limitations admitted by the authors
- Too much emphasis on high-gap pairs hurts. At exponent 100 MATH falls to 59.2 (below plain DPO) because most pairs are discarded and DPO leans toward unseen data.
- The theory holds only when |r| is at most 1, true 82% to 99.8% of the time depending on the dataset, so the guarantee is partial.
- Workflows must be generated until they run without error and finish within a time limit. The paper does not report how often this rejection loop retries.

## Limitations found by others

## What it leaves untried
- Inference cost is higher than AFlow's, since adaptive workflows are larger. With GPT-4o-mini the cost is $0.228 vs $0.202, and with GPT-4o $5.15 vs $3.95. The paper stresses the savings only against GPT-4o chain-of-thought and does not address this.
- No test on tasks without a cheap numeric score (open-ended or agentic tasks). The method depends on a third-party score, and the paper does not say how noisy human or judge scores would behave.
- Executor transfer is only partly checked. GPT-4o is used at test time after optimizing with GPT-4o-mini, but the generator is never trained against a different executor family.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - judges as reward signals]]
