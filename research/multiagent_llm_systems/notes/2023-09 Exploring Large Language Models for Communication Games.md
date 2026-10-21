---
title: Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf
authors: Yuzhuang Xu et al.
date: 2023-09
arxiv: 2309.04658
url: https://arxiv.org/abs/2309.04658
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2309.04658.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents"]
---
# Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf

## One line
Seven frozen gpt-3.5 agents play the social-deduction game Werewolf, using retrieved history, self-reflection and a pool of past-game experience instead of fine-tuning.

## Method
The problem: in a communication game (incomplete information, played in free natural language) an agent must decide from a history far longer than its context window, must infer other players' hidden roles, and ideally improves across games. Fine-tuning is ruled out as slow and data-hungry.

Each of the seven players (two werewolves, two villagers, witch, guard, seer) is one prompted LLM that knows only its own role. Its prompt has four parts: rules, role and some simple human strategy hints; a compact history; suggestions from past games; and a chain-of-thought request.

Compact history has three sources. Freshness: the last 15 messages. Informativeness: messages caught by rules (role reveals, deaths), ranked by a heuristic. Completeness: "reflect by answering questions". The LLM picks 5 questions from a hand-written, role-specific list and asks 2 of its own. Sentence-BERT retrieves the matching messages for each, the LLM answers them, and a reflection summarises the answers. The authors say free-form questions come out generic ("Has any player revealed their role?"), so the hand-written human prior is what makes the questions useful.

Learning from experience is non-parametric. After each game every (reflection, response) pair is scored: 1000 minus game length for winners, game length for losers, so fast wins and slow losses rank high. In a new game the agent retrieves pool entries whose reflection is similar to its own (cosine above 0.85), takes only the lowest-scored entry (likely bad) and entries near the median score (likely good), and has the LLM extract a suggestion from the contrast. Using the whole retrieved set hurt in preliminary tests, because "winners' moves are good" is a weak assumption.

The paper contrasts itself with Reflexion (experience only within one game) and a negotiation self-play work (two players only): this one carries experience across games and across seven players.

## Evaluated on
- Experience helps, but unstably. Only the villager side gets the pool; werewolves serve as a fixed reference. With pools of 10 or 20 games, villager win rate and game length both rise. With 30 games length rises but win rate does not move clearly; with 40 win rate is slightly up but games get shorter. Gains are read from plots over 50 rounds; no significance is reported.
- The fixed-opponent assumption fails. Average camouflage acts rise for werewolves too once villagers have experience (about 4.02 without experience, a dashed baseline, higher in the plots), so the reference opponent moves. The authors use this to explain the erratic win-rate trend.
- Every component matters. In a human check of 50 responses per variant, dropping informative messages, questions, reflection or chain of thought each lowers the share of "reasonable" outputs (read from a bar chart, no exact figures). Without reflection the witch's reasoning turns ambivalent.
- Four behaviours appear without being programmed: trust (builds up over the days, and is dissolved when evidence contradicts it), confrontation, camouflage (werewolves and special roles claim to be villagers) and leadership. Renaming roles ("werewolf" to "pretty girl") still gives similar behaviour, offered as evidence it is not recalled training text. No numbers back this; only examples.

## Limitations admitted by the authors
- Hallucination hurts factuality and reasoning. The seer once claims to have heard others at night, which cannot happen. The authors argue most such fabrications are rational camouflage, but the paper gives no rate.
- Experience use is crude: a sparse win/lose score and prompting give an indirect signal, and the effect is unstable as the pool grows (win rate flat or erratic from 30 games on). Noise handling and cross-game general experience are untried.
- No experience from human players, and no comparison with human performance. The human strategy hints in the prompt serve as bootstrap, so how much comes from the framework is unclear.
- Evaluating multi-LLM play lacks an invariant baseline, since opponents' ability shifts with the agent's own (the camouflage result above).

## Limitations found by others

## What it leaves untried
- Seeding the pool with human game records, though preliminary results already show human priors help.
- A denser or learned score in place of the win/lose-and-length heuristic, which gives the instability above.
- A fixed, non-adaptive opponent, which would make win-rate changes attributable to the agent.

## Topics
[[Topic - strategic play among LLM agents]]
