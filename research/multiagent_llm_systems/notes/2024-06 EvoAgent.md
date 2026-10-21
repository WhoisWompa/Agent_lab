---
title: EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms
authors: Siyu Yuan et al.
date: 2024-06
arxiv: 2406.14228
url: https://arxiv.org/abs/2406.14228
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2406.14228.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "role-based agent teams"]
---
# EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms

## One line
Turns a single hand-built agent into a multi-agent team by having an LLM play the evolutionary operators (crossover, mutation, selection) on the agent's role and settings text.

## Method
The problem: multi-agent frameworks (MetaGPT, AutoGen, Camel, AgentVerse, AutoAgents) depend on hand-written roles, task scopes and prompts, which costs human labor and caps how many agents can be added. The AutoAgents and AgentVerse automations still impose a fixed pipeline ("Planner - Agent Observer - Plan Observer", "Expert Recruitment - Decision - Action - Evaluation").

EvoAgent treats an existing agent as the first individual and its settings (role, skills, prompts), written in language, as the genome. Each iteration runs four steps, all done by LLM calls:
- Crossover: parent agents produce results; an LLM reads them, decides which skills need improving and rewrites the settings to give child agents.
- Mutation: an LLM compares children with parents and edits the children to be distinct while keeping task ability, so the population does not collapse into copies.
- Selection: an LLM quality check keeps N children that both inherit the parent's character and differ from earlier agents; duplicates (for example a second accommodation agent) are discarded.
- Result update: every kept agent drafts a result, and an LLM merges these with the previous iteration's result.

Agents from earlier generations are carried into the next. Because it only edits text, it is framework-agnostic and needs no extra human design. It is written EvoAgent(N, T): N agents per iteration, T iterations.

## Evaluated on
- Beats single-agent prompting and hand-built multi-agent baselines on three reasoning and writing tasks: with GPT-4, Logic Grid Puzzle 77.00 vs 69.00 for the best baseline (AutoAgents), Trivia Writing 84.40 vs 82.00, Codenames 84.53 vs 83.56. With GPT-3.5 Codenames it is 79.38 vs 76.29 for direct prompting, where Self-Refine drops to 46.39.
- Works on weaker models where persona prompting fails: on Llama2-13B, SPP scores 0.00 on Logic while EvoAgent (1,3) scores 35.50.
- Improves long-horizon interactive tasks: ScienceWorld with GPT-4 rises from 27.97 to 30.42 overall, but gains are largest on short trajectories (42.41 to 48.67) and small on long ones (10.58 to 11.38).
- On TravelPlanner with GPT-4, final pass rate is 7.2 vs 2.2 for direct prompting; GPT-3.5 reaches 1.1 against 0.0. Most baselines stay at or near 0.
- The quality check matters once N > 1: with GPT-3.5 and Gemini-Pro averaged, N=2 without it scores 62.8 commonsense pass rate vs 67.0 with it. Variants that skip new agents (Overgen, PromptRefine) score below EvoAgent (1,3) at 68.9 commonsense.
- Time cost with Llama-3.1-70B is about that of AgentVerse and AutoAgents (for example 1060.8 s vs 1056.0 s and 988.8 s on Logic) and above a single agent (318.0 s direct), for the best accuracy (67.00 vs 61.50 best baseline).

## Limitations admitted by the authors
- More tokens and time than one agent, since several agents are generated and each drafts a result; the time table shows roughly 3x the direct-prompting time on Logic.
- Compared against only two other multi-agent frameworks (AgentVerse, AutoAgents), because designing the others per benchmark was out of scope, so the advantage over hand-built teams rests on a narrow set.
- Generated agents were not manually checked, so the claim that they are specialized and useful is supported only by task scores.
- Gains shrink on long trajectories, which the authors tie to longer context hurting multi-agent systems; this is a hypothesis, not tested.
- More agents or iterations pull plans toward user preferences and away from commonsense rules, which the authors attribute to the initial agent's bias when it merges results; untested. Beyond about three iterations on Trivia Writing, generated agents converge and gains plateau.
- Without the quality check, bad agents can hurt: a mistakenly generated nutritionist produced plans so long they overflowed the context window and cut the delivery rate (93.3 for GPT-3.5 All-in, N=3).

## Limitations found by others

## What it leaves untried
- Comparing generated agents with a well-designed human-written team on the same task, which would show whether automation matches expert design rather than only beating prompting baselines.
- Counting what the extra agents cost relative to gain (tokens, cost) across settings, and whether a stopping rule beyond a fixed T could cut it.
- A selection signal beyond an LLM self-check, for example an executable or ground-truth check; the selection here is judged by the same model family that generates the agents.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - role-based agent teams]]
