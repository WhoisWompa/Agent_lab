---
title: Cheap Talk Stabilizes Strategic Interaction in LLM Agents
authors: Lorè et al.
date: 2026-09
arxiv: 2609.16270
url: https://arxiv.org/abs/2609.16270
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2609.16270.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents"]
---
# Cheap Talk Stabilizes Strategic Interaction in LLM Agents

## One line
One sentence of non-binding pre-play messages cuts round-to-round action flipping of 7-9B LLM agents in repeated 2x2 games from 63.8% to 18.9%, and probes show the effect depends on model, framing and the partner's last move.

## Method
The problem: LLM agents in repeated games often flip their action every round, even when one action strictly dominates. A stable aggregate share of an action can hide every individual agent alternating, so the paper measures trajectory persistence directly, as the share of adjacent-round transitions where an agent's action changes. Memoryless random play cannot exceed 50% switching (2p(1-p) is at most 1/2), so a rate above 50% implies negative first-order autocorrelation, that is systematic alternation.

The intervention is cheap talk: before each action, both agents write a short message that costs nothing, binds nothing and leaves payoffs unchanged. The comparison is the same game with no messages. Four open-weight models play Prisoner's Dilemma, Snowdrift, Stag Hunt and Harmony in six framings (neutral, business, environmental, social, team, international relations).

Three probes ask why messages help:
- **Current-message replay.** Hold the realized history fixed and swap only the current message (real, dummy text, re-attributed). Expected switching is split exactly into probability drift (movement in P(A) between rounds) and action uncertainty (Bernoulli variance).
- **History-by-message crossing.** A standardized mutual-benefit or self-prioritizing message is crossed with the partner's last action.
- **Late-layer projection.** In Qwen and Falcon (Prisoner's Dilemma) a "policy-content direction" is found from the residual difference between the two message types, balanced over partner histories. It is projected out at every action during regenerated play.

## Evaluated on
- Communication lowers mean switching from 63.8% to 18.9% (-44.9 points, 95% CI [44.1, 45.6]). 71 of 96 model-game-framing cells stay significant after false-discovery correction.
- The no-message baseline is period-two alternation. 91.5% of Qwen agents and 83.2% of Granite agents switch on all nine transitions. In Harmony, 73.4% of perfectly alternating Qwen dyads cycle in phase (AA to BB), which tit-for-tat cannot produce.
- The effect varies by model. Qwen and Granite stabilize in all 24 cells (-83.2 and -73.5 points). Gemma and Falcon move only 14.5 and 8.3 points, with 5 corrected reversals, all in social or team framings.
- Stabilization is not arbitrary. Action A rises 18.5 to 23.5 points, AA outcomes 25.9 to 30.1 points, and payoff 0.40 to 1.04 per agent per round.
- In Qwen, a real partner message beats partner-formatted dummy text by 21.1 points. Own text shown as partner speech gives 13.1 points against 4.4 for partner text shown as the agent's own. Generic text mostly cuts uncertainty (6.4 points) rather than drift (0.95).
- The history-by-message interaction is significant in all four models. Gemma's self-prioritizing-minus-mutual-benefit contrast is +11.9 after partner A and -24.3 after B.
- Projecting out the direction at layers 20-24 raises switching. In Qwen at layer 22 it rises from 6.0% to 70.0%, with action entropy only 0.125 nats against a 0.693 maximum, so the model alternates confidently rather than randomly.

## Limitations admitted by the authors
- Only four 7-9B models, ten rounds, fixed payoffs, temperature 0.8. Larger, reasoning-tuned models and longer horizons are untested.
- The switch metric measures first-order persistence, not strategic quality. A perfect period-two cycle scores 1 yet is fully predictable, and nine transitions per agent cannot separate a settled cycle from a transient.
- Whether baseline alternation is "avoid repeating my last action" or strategic instability is undecided. Telling them apart needs different history presentations, which were not tried.
- The projection has no random-direction control, so it shows sensitivity to removing that component, not specificity or unique mediation. The two message types also differ in favored action, so "policy-content" names a construction, not a meaning.
- The activation tests cover only Qwen and Falcon in Prisoner's Dilemma, with ten trajectories per context.
- Cheap talk does not help everywhere. In social and team framings it can destabilize.

## Limitations found by others

## What it leaves untried
- Varying how past rounds are shown to the agent. This would test whether the 64% baseline switching comes from the history format rather than strategy.
- Other protocols: sequential messages, longer or open-ended dialogue, or messages that might be used deceptively. The study fixes one sentence, simultaneous and unverified.
- Mixed-model dyads and larger agent counts. Each dyad uses the same model for both players, though the history-by-message results suggest partner behavior drives interpretation.

## Topics
[[Topic - strategic play among LLM agents]]
