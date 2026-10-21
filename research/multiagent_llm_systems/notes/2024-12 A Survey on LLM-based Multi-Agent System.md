---
title: A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application
authors: Shuaihang Chen et al.
date: 2024-12
arxiv: 2412.17481
url: https://arxiv.org/abs/2412.17481
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2412.17481.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "multi-agent debate and consensus", "communication topology and channels"]
---
# A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application

## One line
A survey of 125 LLM multi-agent papers from 2023 and 2024 that sorts them by what the system is for (solving tasks, simulating scenarios, evaluating or training agents) and lists open challenges.

## Method
The paper attacks a coverage problem: earlier surveys (Guo et al. 2024 and others) built a framework, but new work has fallen outside it. The authors define an LLM-based multi-agent system (LLM-MAS) as a set of generative agents interacting in a shared environment. A generative agent has four parts: a profile (role written in natural language), memory (long-term, short-term, sensory), planning, and action. The environment has three parts: tools that turn an action into an outcome, rules that fix how agents may communicate, and an intervention interface for humans, a supervisor model or another agent.

The new contribution is a taxonomy by application purpose, not by architecture:
- **Solving complex tasks.** Reasoning frameworks come in three forms: multi-stage (agents as serial solvers, as in ChatDev), collective decision-making (voting or debate) and self-refine. A second group optimizes communication, because full connection causes combinatorial explosion and privacy disclosure. It splits into speed (non-verbal communication, shorter generation) and distributed discussion (agents each hold part of the information).
- **Simulating scenarios.** Social (Stanford Town's 25 agents, social media, markets, games like Werewolf and Avalon), and physical (wireless networks, mobility). Simulation is judged by consistency with the real world and by whether information spreads over time as it does in reality.
- **Evaluating and training agents.** The system acts as a dynamic environment that gives rewards, used for assessment, supervised fine-tuning, RL, or synthesized training data.

The survey also tabulates open-source code, datasets and benchmarks per sub-field, and distinguishes two communication channels. Natural language is readable but hard to optimize, so it suits consensus. Vectors or discrete signals can be trained with policy gradients, so they suit cooperation.

## Evaluated on
There are no experiments. The claims are descriptive.
- Coverage: 125 papers from *ACL, NeurIPS, AAAI, ICLR plus some arXiv preprints (2023-2024), with a public paper list.
- Scaling in agent count: it cites Qian et al. 2024c as finding "no significant pattern", but gives no figures.
- Cost: one cited system uses real runtime as its metric. The survey offers no comparison of cost or accuracy across systems, so "LLM-MAS achieves better results than a single agent" is asserted from Du et al. 2023 and not tested.

## Limitations admitted by the authors
- Each method gets only a brief summary because of page limits, so technical detail is missing.
- Sources are mostly *ACL, NeurIPS, ICLR, AAAI and arXiv, so important work from other venues may be missed.
- Tables 1-3 list only representative systems with open code, not all papers.
- Challenges named for the field: agents inherit LLM alignment gaps (agents cannot be aligned to mock objects), hallucination, and weak long-text ability. Cost explodes because every agent action needs several LLM calls, and one cited fix, swapping edge agents for rule-based ones, does not work for complex action spaces. Errors accumulate round to round; a rule-based corrector exists but "there is still a lot of room for improvement".
- No benchmark compares LLM-MAS of the same kind, and no objective metric exists for group behavior; current practice compares only the distribution of the system with reality.

## Limitations found by others

## What it leaves untried
- No cross-system comparison of single-agent versus multi-agent on the same task. The central premise that multi-agent collaboration improves performance is taken from the literature.
- It does not analyze failure modes (role drift, loops, conformity) or topology choices. Communication is covered only as speed and distribution of information, so there is no guidance on picking a structure.
- It proposes the need for a common benchmark but does not design one.

## Topics
[[Topic - role-based agent teams]] · [[Topic - multi-agent debate and consensus]] · [[Topic - communication topology and channels]]
