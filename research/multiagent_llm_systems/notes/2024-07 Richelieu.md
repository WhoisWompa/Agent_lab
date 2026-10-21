---
title: Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy
authors: Zhenyu Guan et al.
date: 2024-07
arxiv: 2407.06813
url: https://arxiv.org/abs/2407.06813
venue: NeurIPS 2024
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2407.06813.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "self-refinement and critique loops"]
---
# Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy

## One line
A single LLM agent for the seven-player game Diplomacy that models others' intentions, plans sub-goals, checks whether negotiating partners are lying, and improves by storing self-play experience in memory, with no human game data.

## Method
The problem: the previous best Diplomacy agent, Cicero, pairs a language model for negotiation with a separately trained RL planner, and both are trained on human game data. The authors say this makes the system hard to evolve and tied to one domain. They ask whether one LLM agent can do both planning and negotiation and still improve without human data.

Each turn runs a fixed chain of prompted modules on one LLM:
- **Social reasoning.** The agent infers each rival's intentions and labels players as ally or enemy. This "social belief" feeds every later step.
- **Sub-goal planner with reflection.** The authors observe that LLMs favour short-term gains (for example, letting a non-neighbour grow too strong). So the planner proposes intermediate sub-goals toward the long-term goal. It then retrieves similar past experiences from memory, matched on goal and state similarity, and revises the sub-goals against the scores those experiences received.
- **Negotiator.** Before replying, the agent estimates whether each counterpart is telling the truth. It uses three signals: consistency between the partner's inferred sub-goals and what they say, similar past experiences, and a running honesty score for that player. It then chooses whether to cooperate, feign cooperation, or try to change the partner's intent.
- **Actor.** Picks the unit orders after negotiation.
- **Memory.** Stores state, messages, actions and sub-goals per turn. Each sub-goal is later scored against the outcome that followed. Each player's honesty score is kept only as short-term memory.
- **Self-evolution.** The agent controls all seven countries in self-play games and fills the memory. The only learning is a growing memory the planner and negotiator read. No weights are updated.

Why it should work: a bigger pool of scored experiences gives the reflection step more comparable cases. The explicit lie-check turns non-binding promises into a belief that can be updated.

## Evaluated on
- Beats RL and human-data baselines in no-press play. Richelieu scores higher than SL-DipNet, RL-DipNet, BRPI, SearchBot, DORA and Cicero, shown only as a relative-score figure with no numbers in the text.
- Edges out Cicero with negotiation on, by small margins. Win rate is 6.83% vs 6.03%, Most-SC 8.63% vs 6.90%, defeated 44.60% vs 45.20%, and the authors report a score about 10% higher. Cicero survives more often (41.87% vs 39.95%).
- Clearly beats an AutoGPT-style LLM agent, with win rate 9.1% vs 1.63% and defeated 34.3% vs 61.4%.
- Each module adds value. A vanilla LLM wins 0.4% of games and is defeated in 94.6%. With all modules plus self-play it wins 6.7% and is defeated in 44.4%.
- Self-play memory moves every backbone toward Cicero. GPT-4 goes from 1.5 points below Cicero's win rate to 0.7 above. Llama 3 goes from 2.3 points below to about level. ERNIE Bot and Spark Desk close most of the gap but stay below Cicero (0.7 and 1.6 points under).
- Social reasoning is only partly accurate. Relationship labels are correct 85.7% of the time (GPT-4) and intention labels 74.7%. The ground truth is not independent of the agent, because every seat runs the same agent.

## Limitations admitted by the authors
- Diplomacy is a constrained testbed. Its action space is small next to real diplomacy, and apart from messages all information is public and certain, whereas real diplomacy has incomplete information.
- Self-play gains saturate. New experiences get less novel, so the agent does not improve indefinitely. A larger memory also retrieves near-duplicate experiences, which lowers the useful information the planner sees. The win-rate curve plateaus.
- The win-rate gain over Cicero is small, 0.7 points. The authors attribute this to three or four Richelieu seats per game, which often end in draws.

## Limitations found by others

## What it leaves untried
- No significance testing for the Cicero margin. Win-rate gaps under one point are given without confidence intervals, so the headline "beats Cicero" is not shown to be outside noise. The NeurIPS checklist says error bars are reported, but none appear in the tables.
- No measurement of deception itself. The paper shows two anecdotes of avoiding a lie and none on how often the lie-check is right or what happens when it is wrong. Honesty is scored per player but never checked against ground truth.
- Memory is never pruned or deduplicated, though the authors name retrieval of near-identical experiences as a problem. Diversity-aware selection is left open.
- The werewolf test (59.2% win, versus 65% for the strongest purpose-built LLM agent) was run without self-play, so the self-evolution claim is untested outside Diplomacy.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - self-refinement and critique loops]]
