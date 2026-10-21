---
title: Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models
authors: Andy Zhou et al.
date: 2023-10
arxiv: 2310.04406
url: https://arxiv.org/abs/2310.04406
venue: ICML 2024
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2310.04406.pdf
folder: ["multiagent_llm_systems"]
topics: ["reasoning prompting", "self-refinement and critique loops"]
---
# Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models

## One line
LATS wraps a single LLM agent in Monte Carlo Tree Search, using environment feedback, an LLM-scored value function and verbal reflections on failures, so it explores several trajectories instead of committing to one.

## Method
The problem: prompting methods are either reflexive or isolated. ReAct and Reflexion refine one trajectory and never weigh alternatives at a step. Tree-of-thought and RAP search over alternatives, but only inside the model's own knowledge, so they cannot use feedback from the environment (a compiler, a website, a retrieval API).

The idea: language tasks can be rewound by pasting the earlier context back in. That removes the usual obstacle to MCTS, an environment model for undoing steps. One model plays three roles: agent, state evaluator and reflection writer. No training is involved.

Each iteration runs six operations:
- Selection descends the tree by UCT, which balances a node's value against how rarely it has been visited.
- Expansion samples n candidate actions, executes each in the environment, and stores the observations as child nodes in an external tree memory.
- Evaluation scores each child with V(s) = lambda * LM score + (1 - lambda) * self-consistency score. The LM is prompted to reason about the state after seeing the environment's response and to end with a score. Self-consistency rewards actions that were sampled repeatedly at the same state.
- Simulation continues from the node to a terminal state, which gives an objective success signal.
- Backpropagation updates the values on the path.
- Reflection: when a terminal node fails, the model writes a verbal summary of what went wrong. The failed trajectory and the reflection go into the context of later attempts, for both the agent and the value function. The authors call this a "semantic gradient", richer than a scalar reward.

The search stops on success or when the trajectory budget is spent. For pure reasoning tasks with no environment feedback, CoT is the base prompt. The paper's claim is that a naive bolt-on of search to ReAct fails: ToT and RAP built on ReAct score 0.39 and 0.54 on HotPotQA, and the ToT version is worse than the reasoning-only setting.

## Evaluated on
- Large gains over ReAct and Reflexion with GPT-3.5. HotPotQA exact match is 0.63 for LATS vs 0.32 for ReAct and 0.51 for Reflexion, and 0.71 when the base prompt starts with CoT and falls back to ReAct. This uses an oracle setup in which the environment reports whether an answer is correct.
- Programming is the strongest case. HumanEval pass@1 is 92.7 with GPT-4 (Reflexion 91.0, base model 80.1). With GPT-3.5 it is 83.8 vs 68.1 for Reflexion. MBPP is 81.1 vs 70.0.
- WebShop score is 75.9 vs 64.2 for Reflexion and 62.4 for RL-based training. Success rate is 38.0, which stays below the 45.0 of a fine-tuned model and the 59.6 of human experts.
- Each component carries weight, in HotPotQA ablations. Dropping the LM value heuristic costs 0.26, swapping MCTS for DFS costs 0.21, and dropping reflection costs 0.05.
- LATS also beats search baselines on a pure reasoning task. Game of 24 success is 0.44 vs 0.40 for RAP, which the authors credit to the self-consistency term in the value function.
- Cost at equal k: the same asymptotic sample complexity as ToT and RAP, and fewer nodes to reach success (66.65 vs 70.60 for RAP and 84.05 for ToT at k=50). The token counts are 173,290 vs 176,500 for RAP and 210,215 for ToT. The authors say failed runs would widen the gap, but do not measure it.

## Limitations admitted by the authors
- Compute cost is higher than ReAct or Reflexion, since many nodes are expanded. Accuracy rises with n (HotPotQA 0.58 at n=3, 0.63 at n=5, 0.65 at n=10) at more inference cost. Setting n=1 brings the cost to ReAct-with-retries level.
- It requires reverting to earlier states, which not every environment allows. The paper names programming, WebShop, ALFWorld and tool use as feasible, and concedes that some environments cannot be rolled back.
- Reflections on WebShop are often generic and leave the agent stuck in local minima. ReAct and Reflexion with k=30 score about the same there.
- Benchmarks are simple and decision-focused compared with real interactive settings.
- Part of the HotPotQA advantage comes from the oracle correctness signal. Without it, the value function is the only guide.

## Limitations found by others

## What it leaves untried
- Environments with no rollback, or with irreversible side effects. Only a general remark that the design can be adjusted is offered.
- Complex open-ended settings such as Minecraft, and multi-agent use. Both are named as future work and neither is tested.
- Settings without a reliable terminal success signal. HotPotQA uses the oracle one and the code tasks use LM-generated tests, but the paper does not measure how much noise in that signal costs.

## Topics
[[Topic - reasoning prompting]] · [[Topic - self-refinement and critique loops]]
