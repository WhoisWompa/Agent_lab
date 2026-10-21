---
title: Communication Enables Cooperation in LLM Agents: A Comparison with Curriculum-Based Approaches
authors: Hachem Madmoun et al.
date: 2025-10
arxiv: 2510.05748
url: https://arxiv.org/abs/2510.05748
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2510.05748.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents"]
---
# Communication Enables Cooperation in LLM Agents: A Comparison with Curriculum-Based Approaches

## One line
Compares two ways of getting LLM agents to cooperate in social dilemmas, a one-word cheap-talk channel (works almost perfectly) and an in-context curriculum of games (makes agents worse).

## Method
LLMs default to individually rational play in social dilemmas, which is bad for multi-agent safety. The paper tests two interventions on four-player games played by mixed groups of open models (Mixtral, Qwen, Llama, DeepSeek).

**Cheap talk.** Before acting in a four-player Stag Hunt, each agent broadcasts one non-binding word. Stag Hunt has two equilibria: everyone hunts stag (10 points each), or the safe hare (3 points). The channel costs nothing and binds no one. It should work because it lets agents settle on a shared signal and trust it, and the paper says current models do this without training.

**Curriculum.** The target task is a 10-round Public Goods Game with costly punishment. Agents first play easier games in sequence (2-player Prisoner's Dilemma, then 4-player, then a short Public Goods Game). After each stage a stronger model (Claude Opus 4.1) writes a strategic lesson from the game logs, and it is prepended to the next stage's prompt. This is in-context learning only, with no weight updates. Three conditions are compared with a no-lesson control: full curriculum, the same games scrambled, and only the direct precursor game.

The authors then read the agents' reasoning traces to explain the curriculum result. A neutral-lesson ablation (generic text such as "Consider your options carefully", same games) separates the game sequence from the lesson content.

## Evaluated on
- Cheap talk fixes coordination among mixed models: Stag Hunt cooperation rises from 0% to 96.7%. Same-family pairs go from 52.2% to 100%, and payoff variance disappears (17.9 ± 11.8 to 30.0 ± 0.0). The word "stag" appeared in 73% of messages in cooperative rounds.
- The curriculum lowers payoffs, and the loss grows with curriculum length. Against the control (211.7), the direct precursor gets 199.0 (-6.0%), the scrambled order 182.0 (-14.0%) and the full curriculum 153.6 (-27.4%). The control sustains contributions longer; trained groups collapse to defection faster.
- The lesson content, not the game sequence, causes the damage. The same games with neutral lessons score 251.1, 63.5% above the AI-lesson condition (153.6) and above the control (211.7). In traces, "learned pessimism" appears in 62% of full-curriculum traces and under 5% of neutral ones. Early 3-round games taught "defect from round 1", which agents over-applied to a 10-round game with punishment.
- Cheap talk helps welfare only when cooperation pays. With a 1.6x pot multiplier, communication raises contribution from 48% to 71% but cuts average payoff from 184.4 to 127.5, because cooperative signallers got exploited and punished. With a 4.0x multiplier, contribution goes from 55% to 100% and payoff from 457.9 to 480.0.
- Frontier models (GPT-4o, o1-preview) in the 4.0x game show the same pattern: 0% cooperation without cheap talk, 100% with it (payoff 192.1 to 480.0). The appendix reports this; the main text does not detail the setup.

## Limitations admitted by the authors
- The full curriculum opened with defection-equilibrium games, so the failure may come from this design and not from curricula in general. Cooperation-first sequences were not tried.
- Lessons were written by one model (Claude Opus 4.1). Its framing cannot be fully separated from the curriculum structure, and no human-written lessons were tested.
- Only four models were used (plus the frontier replication), so the results may not carry to other architectures.
- In-context learning only; fine-tuning might embed cooperation more robustly and was not explored.
- All games are four-player and perfect-information. Real deployments have partial observability, mixed incentives and other group sizes.

## Limitations found by others

## What it leaves untried
- A cooperation-first curriculum, or human-written lessons. Without them the headline claim that curricula are fragile is not separated from this one bad design, as the authors concede.
- Fine-tuning on the game sequence instead of prompt lessons, which is the usual meaning of curriculum learning.
- Cheap talk with deception or conflicting goals. The Stag Hunt is a pure coordination game, and the 1.6x result already shows signalled intent can be exploited. How robust the channel is to a liar is unmeasured.

## Topics
[[Topic - strategic play among LLM agents]]
