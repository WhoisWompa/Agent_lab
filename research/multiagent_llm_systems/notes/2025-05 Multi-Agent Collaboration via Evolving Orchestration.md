---
title: Multi-Agent Collaboration via Evolving Orchestration
authors: Yufan Dang et al.
date: 2025-05
arxiv: 2505.19591
url: https://arxiv.org/abs/2505.19591
venue: NeurIPS 2025
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2505.19591.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "automated pipeline and topology search", "communication topology and channels"]
---
# Multi-Agent Collaboration via Evolving Orchestration

## One line
A small RL-trained "puppeteer" policy picks which LLM agent speaks next from the current task state, and learns to reach correct answers with fewer agents and tokens.

## Method
Problem: most multi-agent LLM systems use a fixed or hand-designed topology (chain, tree, mesh). The paper says this adds coordination overhead and does not scale as tasks and agent counts grow. Its motivating footnote: a 50-node mesh can take up to 10 hours to write a few hundred lines of code.

Idea: replace the fixed structure with one central policy. An agent is a triple (model, reasoning pattern, tools). The pool holds reasoning agents (plan, reason, critique, reflect, question, summarize, conclude, modify) and tool agents (file, arXiv, Bing, website, Python), plus a Terminator. At each step the policy sees the task and the shared state and picks the next agent (or a few in parallel). The agent's output updates the state, and the next choice depends only on the new state (a Markov process). The final answer is a majority vote over outputs. Seen afterwards, the sequence of calls is a directed graph, so the topology is built during reasoning, not searched in advance. Agents can be called repeatedly, so loops are possible.

Learning: the policy (initialised from a Llama-3.1 reward-model variant) is trained online with REINFORCE. Reward is final correctness or quality minus lambda times a step-wise cost that grows with step count, with lambda = 0.1 and discount 0.99. The cost is why the policy learns to prune weak or expensive agents and call the Terminator early. Setting lambda to zero would, the authors say, collapse the system into an ordinary large collaboration, possibly with higher accuracy.

## Evaluated on
- Beats fixed-structure and workflow-search baselines on average, with the same base model. Titan (large models), averaged over GSM-Hard, MMLU-Pro, SRDD and CommonGen-Hard: 0.7731 evolved, against 0.6899 for AFlow and 0.6157 for Self-Refine. Mimas (small models): 0.6324 against 0.5364 for AFlow. AFlow, though, wins some single tasks (e.g. MMLU-Pro, 0.75 against 0.70 for Puppeteer in Titan).
- Training helps: Titan average rises from 0.6893 (early) to 0.7731 (evolved). The comparison is early vs late inside one online run, not separate runs.
- Cost falls while quality rises: token use drops over training on almost all tasks. In Titan the number of active agents falls too, meaning earlier stopping. In Mimas the agent count stays roughly constant and savings come from choosing cheaper agents.
- Structure changes in a measurable way: average graph density goes from 1.08 to 1.45, and cycles of every length from 1 to 4 become more frequent (length-2 cycles 1.17 to 1.40, length-3 0.17 to 0.38). The authors credit the gains to this "compact, cyclic" structure, but only show correlation.
- Depth and width limits matter: the default (width 4, depth 2) gives the best accuracy/cost trade-off; larger values add cost and can lower accuracy.
- Mixed-model pools beat the single-model variant (Puppeteer-Mono) on average in both subspaces. The authors attribute this to complementary models, without testing the explanation.

## Limitations admitted by the authors
- Reward is coarse (final answer plus token count only). With no step-level feedback, credit assignment over a long agent chain is weak. On some tasks the performance/cost score shows no upward trend.
- Training used only 200 optimisation samples, and the authors say this may be too few to find good configurations on harder tasks. The fixed length cap may also be unsuited to weaker base models.
- The set of agents and tools is fixed, so the system cannot adapt to task variations by creating or changing agents at inference time.
- Agents sometimes mis-coordinate or reach "deceptive agreement", and the paper says better interaction protocols and incentives are needed. It gives no rate.
- Training cost cannot be compared with baselines. The orchestrator is trained online alongside inference, and AFlow-style methods spend a different kind of compute.

## Limitations found by others

## What it leaves untried
- No ablation separates the effects of centralisation, the RL training, and the cost term, so the claim that cycles cause the gains is unsupported.
- Only four task types are tested, plus a single ALFWorld case study. There is no test of whether a trained policy transfers to unseen tasks or new agent pools.
- It does not tackle the deceptive-agreement problem it names, for instance with incentive design among the agents.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]
