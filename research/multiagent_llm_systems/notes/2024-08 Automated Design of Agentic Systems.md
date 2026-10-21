---
title: Automated Design of Agentic Systems
authors: Shengran Hu et al.
date: 2024-08
arxiv: 2408.08435
url: https://arxiv.org/abs/2408.08435
venue: ICLR 2025
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2408.08435.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "self-refinement and critique loops"]
---
# Automated Design of Agentic Systems

## One line
A meta agent (an LLM) writes new agents as Python code, scores them on a task, and keeps an archive of past designs to inspire the next ones (Meta Agent Search), finding agents that beat hand-designed ones.

## Method
The problem: agent building blocks (chain-of-thought, self-reflection, tools, roles) and the ways to combine them are designed by hand, with domain-specific tuning. The paper names the research area ADAS (Automated Design of Agentic Systems) and splits it into a search space, a search algorithm and an evaluation function.

The new idea is the search space: the whole agent is code, a single `forward` function over a small ~100-line framework that supplies model calls and prompt formatting. Code is Turing complete, so prompts, workflows, tools and their combinations are all reachable. Earlier work searched prompts only (PromptBreeder, OPRO), or graphs and networks (DyLAN, GPT-Swarm), where tools or other parts stay fixed. The authors argue code also reads well (easier to debug and audit) and plays to LLMs' coding skill. The last point is an argument; the paper does not test code against graph spaces.

The algorithm is deliberately simple. The archive starts with baselines (CoT, Self-Refine and others). The meta agent, conditioned on the archive, writes a description and the code of a new agent, and reflects twice to make it novel. The agent is run on validation data. On errors the meta agent reflects and fixes it, up to five times. The agent and its score are added to the archive. The only selection pressure is a prompt asking for "interestingly new" agents. There is no explicit population, fitness-based parent selection or diversity metric.

Why it should work: the archive supplies stepping stones that later designs recombine. On ARC, "multiple CoTs, refine, ensemble" appeared at iteration 3 and was reused. The best agent combined three earlier ideas (diverse feedback at iteration 5, expert critics for efficiency and simplicity at 11, human-like critic at 12). The discovered agents are largely critique-and-ensemble loops: this is a search over the same refine, debate and ensemble patterns that hand designers use.

## Evaluated on
- Discovered agents beat seven hand-designed baselines and prompt optimization (OPRO) in all four domains, with GPT-4 as meta agent and GPT-3.5 as the agent. Reading comprehension F1 is 79.4 vs 69.1 for OPRO and 65.8 for the best hand-designed baseline. Math (MGSM) is 53.4% vs 39.0% (LLM Debate).
- The gain is small where the model lacks the knowledge: 34.6 vs 31.6 on science (GPQA) and 69.6 vs 65.9 on MMLU. The confidence intervals are about ±3.2 to 3.3, so these gaps are within noise. The authors hypothesise that agent design cannot supply missing knowledge. They do not test this.
- On ARC (60 test questions of grid size 5x5 or smaller, 25 iterations), the best agent reaches 13.7% with GPT-3.5 vs 8.0% for the best baseline (COT-SC).
- Agents found on MGSM transfer. The top agent gets 69.5% on GSM8K vs 43.6% for the best baseline. It reaches 70.4 F1 on DROP, above every baseline (65.8 best), though below the 79.4 of the DROP-searched agent.
- Agents found with GPT-3.5 transfer across models on ARC. With Claude-Sonnet the best reaches 48.3% vs 39.3% for Self-Refine. With Claude-Haiku the margin is smaller: 9.7% vs 6.3%, and one of the three found agents (5.0%) falls below it.
- Cost: about $500 for one ARC search and about $300 for one run in the other domains (OpenAI API, appendix).

## Limitations admitted by the authors
- Only single-step question answering is tested. Multi-step interaction with environments is left as future work, so the claim of designing general agents is not shown.
- The evaluation function is the validation score only. It is expensive and discards the information in failure logs. Tasks without ground-truth answers are not covered.
- Only one objective (accuracy) is optimized. Cost, latency and robustness are ignored, though the ~$300 to $500 search cost shows they matter.
- The search algorithm is plain "ask for something interesting". The authors say better novelty or quality-diversity search is open.
- Agents need the basic framework functions in order to be efficient. Building everything from scratch is possible in theory but impractical.
- Model-written code could be destructive. The authors ran it in containers and inspected it by hand, and they note that the same method could speed up self-improving AI.
- The best GPT-3.5 agent used a complex feedback mechanism, but stronger models did better with simpler feedback and more refinement. So a design is tied to the model it was found on, even though the average ranking transfers.

## Limitations found by others

## What it leaves untried
- Comparison to the same search run over a graph or prompt-only space with equal budget. Without it the benefit of code as search space, versus simply running a search, is argued but not isolated.
- Searching for agents that do well across several domains at once, or a meta agent that is itself improved (higher-order ADAS). Both are listed as future work.
- Using failure logs, not just the score, to guide the next design. This would cut the evaluation cost.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - self-refinement and critique loops]]
