---
title: "From Probabilities to Decisions: Search and Multi-Teacher Distillation with Jev"
authors: Mohamad Yazan Sadoun et al.
date: 2026-10
arxiv: 2610.09188
url: https://arxiv.org/abs/2610.09188
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/From Probabilities to Decisions - Search and Multi-Teacher Distillation with Jev (Sadoun 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "preference learning", "social choice"]
---
# From Probabilities to Decisions: Search and Multi-Teacher Distillation with Jev

## One line
Distils the pairwise probabilities of a probability-only judge (Jev), alone or averaged with an LLM judge (Qwen3-32B), into a small evaluator that a search engine or reranker uses without any live judge calls, and asks when a second judge is worth its share of the labelling budget.

## Method
Problem: a probability-only "System One" model like Jev returns calibrated probabilities over fixed choices but no lookahead, and at 177 ms median per call it is too slow to consult inside a search tree. Calling it live only to break exact ties among search's best moves already costs 28.7 Elo.

Idea: move the judgment offline. Each judge answers "which of these two moves (or passages) is better?" in both orders, giving p(a≻b). Those probabilities become soft targets for a Bradley-Terry fit: a linear evaluator w·x(s) over 443 hand-defined chess features (piece-square, mobility, king safety, pawn structure, threats) is trained by cross-entropy so that σ(w·Δx) matches the judge's probability. The weights replace Stockfish's neural evaluation, so search supplies lookahead and the distilled judgment scores every leaf at no call cost. For retrieval the same soft labels train a MiniLM reranker.

Multi-teacher step: instead of spending the whole budget on one judge, average two judges' probabilities per pair before fitting. The bet is that two judges with different errors give better-shaped targets than more pairs or repeated answers from one judge. The right test of a label source is decision quality after search, not label agreement, since the two can disagree.

## Evaluated on
- Averaging Jev and Qwen beats spending the same 252,540 responses on Qwen alone over twice the pairs: +9.6 Elo [4.3, 14.9] over 4,000 games, replicated at +8.4 [2.9, 14.1] on fresh openings; over Jev on twice the pairs, +27.0.
- The gain comes from Jev's position-specific judgments, not just softening Qwen: replacing Jev with a constant 0.5 still leaves the combination ahead by +9.6, shuffling Jev's probabilities freely by +10.9, recalibrating Qwen by +14.3.
- Label agreement does not predict playing strength: all judges agree with Stockfish only 52.9 to 54.5% of the time, and on Jev-Qwen disagreements the averaged labels match Stockfish 48.2% versus Jev's 53.6%, yet they train the stronger player.
- In reranking, Jev alone matches Qwen: NDCG@10 0.637 vs 0.630, from about 21 minutes of API calls instead of 5.1 GPU-hours; adding Qwen gains at most +0.004 [−0.003, 0.011].

## Limitations admitted by the authors
- Distilled judgment is task-dependent and can be harmful: the Jev-trained score cuts strength by 619.4 Elo in Othello and 157.7 in Connect-4, because Jev prefers corner moves in only 14.4% of corner pairs and learns a corner weight of −838 against the baseline's +858.
- The partnership gain is fragile to tuning: when each training subset picks its own regularisation, Jev+Qwen over Qwen on twice the pairs falls to +2.2 Elo [−2.4, 6.8], not significant.
- More judges do not help in any simple way: across all 15 judge combinations, Jev+OLMo scores −5.9 and all four judges +13.2, below Jev+Qwen's +25.8 and roughly level with Qwen alone at +24.0.
- The stricter shuffle (Jev's values moved only within Qwen's probability groups) leaves a +5.3 lead [−0.5, 11.0] that does not exclude zero, so how much Jev adds beyond what Qwen's confidence already encodes is not settled.
- The headline deployment (1753 to 2268 Lichess bullet rating) has the opening book, tablebases and live Jev calls on and is played against bots, so it does not isolate the judge's contribution.

## Limitations found by others

## What it leaves untried
- Combining judges by weighting them by estimated reliability (Dawid-Skene, Snorkel-style) instead of a plain mean; the mixed 15-combination results suggest equal weighting is a weak link.
- A richer evaluator than a 443-weight linear model; the student's capacity may cap what any judge's labels can convey, and Stockfish-labelled versions of the same features still add over 200 Elo, far more than Jev's +38.9.
- A cheap pre-distillation check that a judge's labels suit the task, since label agreement does not predict play and the Othello failure only surfaced in games.

## Topics
[[Topic - decision models]] · [[Topic - preference learning]] · [[Topic - social choice]]
