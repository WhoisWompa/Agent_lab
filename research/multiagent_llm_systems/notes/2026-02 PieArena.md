---
title: PieArena: Ranking and Profiling Language Agents in Realistic Negotiation Scenarios
authors: Chris Zhu et al.
date: 2026-02
arxiv: 2602.05302
url: https://arxiv.org/abs/2602.05302
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2602.05302.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent evaluation benchmarks", "strategic play among LLM agents"]
---
# PieArena: Ranking and Profiling Language Agents in Realistic Negotiation Scenarios

## One line
A negotiation benchmark built from MBA-course scenarios that ranks 13 LLM agents by head-to-head play, anchors them against trained human negotiators, and profiles behaviour (lying, arithmetic, rule compliance) beyond the deal outcome.

## Method
Static exam-style benchmarks saturate as models improve. PieArena replaces them with live two-party negotiations over private information, where the opponent is another model, so the ranking signal moves as the field improves. Each side has a private payoff table, a walk-away value (BATNA) and hard constraints. Six rounds of free chat end in a structured contract that is scored deterministically. Two quantities are separated: the total pie (joint surplus above both BATNAs, i.e. value creation) and the pie share (how it is split, i.e. value claiming). Scenarios are single-issue price haggling (zero-sum) or multi-issue deals where trades across issues enlarge the pie.

Three pairings are used: mirror-play (same model both sides, compared with human-human pairs), cross-play (different models, for ranking), and human-LM play.

Ranking idea: payoffs are continuous shares in [0,1], so the paper fits a Beta-likelihood extension of Bradley-Terry-Luce (BBTL). Each model has a latent skill; the logit of side one's expected share is the skill gap plus a first-speaker effect plus a scenario-role effect. All plays are fitted jointly by maximum likelihood, so the leaderboard does not depend on match order (unlike sequential Elo) and carries confidence intervals. A binary win/loss BTL would throw away the size of the win. The paper says BBTL beats Elo and binary BTL (its Table 2, not shown in the text read here).

Every model is run in two modes. "Base" is the off-the-shelf model. "Pro" adds a harness with a state-tracking module (modelling the other side's preferences) and a round-level strategic planner, motivated by shared-intentionality theory.

Behaviour profiles from transcripts: deal rate, BATNA compliance, structured-output validity, arithmetic accuracy, plus lie rate and perceived reputation scored by LLM judges blinded to model identity.

## Evaluated on
- Frontier models match or beat trained humans. On the multi-issue SnyderMed task, human pairs reach a normalized total pie of 0.874 (23 pairs). GPT-5 reaches 0.960 in base mode, significantly above humans. Against students, GPT-5 takes 60.3% of the pie on single-issue Main Street (significant in base and pro). On multi-issue Top Talent, students take 53.8% vs 46.2% for the agent (p = 0.27, not significant), despite coaching.
- The harness lifts weaker models far more than strong ones. In mirror-play, base Claude-Opus-4.5 (0.800), GPT-4.1 (0.805) and Gemini-2.5-Flash (0.754) are significantly worse than humans. With the harness none is, and Gemini-2.5-Flash rises to 0.860. GPT-5, Gemini-3-Pro and Grok-4 show no detectable gain. In cross-play, ERNIE-4.5 moves from rank 12 to 7 in multi-issue play.
- Outcome rank hides behaviour. Computation accuracy is 100% for GPT-5.2 and 99.6% for GPT-5, but 5.4% for GPT-4.1 and 15.3% for Grok-3. Structured-output validity is 68.3% for Claude-Opus-4.5 and 61.9% for Claude-Sonnet-4.5, because reflective text is appended to the final answer.
- Lying pays. Lie rate is about 11.3% for Grok-4, versus 39.9% for Gemini-3-Pro and 33.9% for GPT-5.2. A one-unit larger lie-rate gap goes with +3.23 points of pie share (p = 0.001). Lie rates are higher in single-issue bargaining (o4-mini-high 6.4% to 46.8%), where claims are harder to check.
- Higher relative reputation goes with a smaller share (-22.79 points per unit, p = 0.001).

## Limitations admitted by the authors
- Only two-party negotiation with deterministic payoffs, whereas real negotiation has coalitions and ambiguous preferences. The conclusions do not cover those cases.
- The human baseline is MBA students from one school. The authors cite work saying such students perform like professionals, but professionals were not tested.
- Lie rate and reputation come from LLM judges. They were checked against a 10-judge panel and human labels, but the authors concede residual judge bias may remain.
- The harness hurts arithmetic in multi-issue play for mid-tier models: Claude-Sonnet-4.5 falls from 80.0% to 56.8% and Grok-3-mini from 80.6% to 62.5%. The authors suggest context overload but do not test it.

## Limitations found by others

## What it leaves untried
- Training for negotiation: the harness is prompt-level scaffolding only, so it is unknown whether the catch-up gains survive fine-tuning or just reflect weaker models needing more structure.
- Whether the lie-rate and pie-share link is causal. It is a correlation across model pairs, and the paper does not test an honesty constraint or a verifier that penalizes false claims.
- The Top Talent comparison has no base-mode agent, and its non-significant result (p = 0.27, 40 sessions) cannot separate "equal to humans" from "too few sessions to detect a difference".

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - strategic play among LLM agents]]
