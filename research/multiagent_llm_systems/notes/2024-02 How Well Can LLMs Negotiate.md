---
title: How Well Can LLMs Negotiate? NegotiationArena Platform and Analysis
authors: Bianchi et al.
date: 2024-02
arxiv: 2402.05863
url: https://arxiv.org/abs/2402.05863
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2402.05863.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "agent evaluation benchmarks"]
---
# How Well Can LLMs Negotiate? NegotiationArena Platform and Analysis

## One line
An open-source platform of three two-player negotiation games is used to rank four LLMs against each other and to show that persona prompts raise payoffs while anchoring and other irrational habits leave the agents exploitable.

## Method
Static benchmarks ask fixed questions; negotiation changes with every counter-offer yet still ends in a measurable outcome (a price, a split), so it can test theory of mind, strategy and rationality at scale. NegotiationArena runs two agents (Red and Blue) through turn-taking games: resource exchange (trade to maximise total holdings), a multi-turn ultimatum game (split $100; the classical game has one round, here counter-offers are allowed), and seller versus buyer (seller cost 40, buyer value 60, each side's value private, so incomplete information).

The harness forces each message into XML-like tags: the agent restates its name, resources and goal every turn (to curb forgetting), gives private reasoning, a public message, an accept/reject answer and a structured trade. The partner sees only message and trade, so reasoning stays secret. Whole games are saved and can be reloaded, edited and replayed for counterfactuals. Because the ultimatum game has a known rational solution, deviations can be named and measured.

Three analyses follow. First, a round-robin between GPT-4, GPT-3.5, Claude 2 and Claude 2.1 in both seat orders. Second, GPT-4 given a "cunning" persona (insult and humiliate) or a "desperate" persona (fake desperation, beg) in the second seat. Third, rationality probes on GPT-4: anchoring, split-the-difference, over-valued buyers, stakes and number of turns.

## Evaluated on
- Seat and role decide outcomes as much as model quality. In the ultimatum game Player 1 almost always wins (win rates 0.77 to 1.00 in the table). In resource exchange the second player tends to beat the first (e.g. GPT-4 second beats Claude-2.1 first 76% of decisive games; Claude-2.1 second beats GPT-4 first 72%).
- Winning is not the same as earning. As Player 2, GPT-4 wins more often than Claude-2.1 but averages a lower payoff (1.38 vs 2.45). Claude opens about $10 lower than GPT in the ultimatum game and gets payoffs above 60 as Player 1. GPT-4 is the best buyer, averaging a sale price of $41; all models reach similar prices as sellers, with prices mostly under the midpoint 50.
- Personas pay. A desperate or cunning second GPT-4 raises win rate and payoff in all three games; the abstract quotes a 20% payoff gain against standard GPT-4. Cunning is high risk: in the ultimatum game it wins 82% but its average payoff (about 49) matches the default, because failed deals pay 0.
- A weak partner drags a strong one down. GPT-3.5 made an impossible offer and GPT-4, correcting it twice, ended up giving away most of its money. About 20% of GPT-3.5's seller/buyer games misread the goal as "sell for exactly 40".
- Human-like biases. Final price correlates with the opening price (Spearman 0.716, anchoring). Agents "split the difference". An over-valued buyer counter-offers a higher price than the seller asked in 41% of games against 11% for the default buyer, and a "self-interested" prompt did not change this.
- Weak generalisation. GPT-4 accepts every positive offer in the classical ultimatum game, but in the 3-turn version acceptance falls as the offer gets less fair, though the rational rule is identical. Scaling the amount to split to $10 billion gave Player 1 nearly 79%.

## Limitations admitted by the authors
- The classical ultimatum result may be memorisation: the model sometimes names the game in its reasoning, so the "rational" behaviour may not be understood and does not carry over to the 3-turn variant.
- GPT-4's seller/buyer behaviour is explained by hypothesis only ("believes it must meet in the middle"); no test separates that from other causes.
- Human parallels (anchoring, stakes effects) are cited from other work, not tested against human players here.
- The paper notes game theory cannot model every real interaction, so the games are only one reference point for rationality.

## Limitations found by others

## What it leaves untried
- Defences. The paper shows desperation, insults and a faulty partner can exploit an agent but tests no prompt or training fix, so how to harden agents is open.
- Mixed pairings for the persona tests. Personas are tested only with GPT-4 on both sides, so whether weaker or Claude models are as easily exploited is unknown.
- No negotiation against humans or on tasks with real stakes; transfer from these three toy games is unsupported.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - agent evaluation benchmarks]]
