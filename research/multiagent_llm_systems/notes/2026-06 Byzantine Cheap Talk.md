---
title: Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games
authors: Aya El Mir et al.
date: 2026-06
arxiv: 2606.07790
url: https://arxiv.org/abs/2606.07790
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2606.07790.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "communication topology and channels"]
---
# Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games

## One line
Shows that the cooperation which one-word cheap talk buys LLM agents in a 4-player Stag Hunt breaks under a single lying agent and under announced visibility limits, and that models split into two stable response types.

## Method
Prior work (the authors' own) found that a one-word broadcast before acting lifts 4-player Stag Hunt cooperation from 0% to 96.7%. That result assumes honest signals and everyone seeing everything. This paper tests both assumptions in the same game: 5 rounds, payoff 10 if all four hunt stag, 3 for hare, 0 for a lone stag hunter.

Two attacks are tried. First, a Byzantine agent bypasses the LLM, always broadcasts "stag" and always plays hare. A soft version defects with probability 0.5. Second, message visibility is restricted to a ring (two neighbours) or a star (hub sees all, spokes see only the hub). Each restriction is run in two forms: explicit, where agents are told what they cannot see, and silent, where the same filtering is applied but the prompt says nothing and drops the player count.

The explanatory claim is meta-reasoning. Telling an agent that some messages are hidden makes it reason about unseen players with unknown intent, and it then plays safe. The authors call this a conjecture; they have no direct test of it. Agents are also sorted by behaviour after the first betrayal. Defection-Prone (DP) agents switch permanently to hare in more than half their trials. Cooperation-Persistent (CP) agents do not.

## Evaluated on
- One hard Byzantine agent ends group cooperation (0% versus 77% at baseline), though unanimity makes that structurally certain. Honest agents detect the betrayal within a round: their cooperation falls from 98% to 43% by round 2. About half still choose stag (50% over the trial).
- A second Byzantine agent deepens the collapse. Honest cooperation drops from 100% to 23% by round 2.
- The soft adversary earns 2.64 per round against 2.37 for honest agents, an 11% premium. Intermittent honesty keeps others hopeful (honest cooperation decays from 97% to 48%).
- Explicit topology collapses cooperation with no adversary present: group cooperation is 5% in a ring and 0% in a star, against 70% for explicit broadcast. Silent topology with the same filtering keeps 100% in ring and broadcast and 80% in star. Silent-ring agents miss one of three peers yet cooperate perfectly, so lost information does not explain the explicit collapse.
- Combining the attacks compounds the harm. With a star and one adversary, honest cooperation is 13% when the hub is the adversary and 28% when the hub is honest, against 50% for broadcast with one adversary.
- The DP/CP split holds across three model cohorts and group sizes of 2 to 6. Mixtral and DeepSeek are DP, Qwen and Llama are CP, and DP agents earn 2.42 per round against 0.45 for CP (5.4x). The split vanishes under silent topology, which the authors read as prompt-elicited rather than intrinsic.

## Limitations admitted by the authors
- Only one game, 4 players, 20 trials per condition. Unanimity makes a single defector fatal, which may exaggerate the damage compared with graded payoffs.
- The cause of DP versus CP cannot be identified. RLHF data, scale and instruction style are all confounded with model family. The "alignment tax" reading (cooperative models are exploitable) is therefore only suggestive.
- Some models are unstable. GPT-4o is DP in the first cohorts but CP in the 5- and 6-player groups, and also defects pre-emptively from round 1 (8 of 13 instances in one cohort). Claude Sonnet shows non-extreme defection rates at larger sizes. The two-type picture is cleanest for Mixtral and Qwen.
- Meta-reasoning is conjectured, not isolated. A reasoning-trace analysis is offered as support, but the traces are model-written text.
- No randomness seeds are set, and the 5-round horizon is short.

## Limitations found by others

## What it leaves untried
- No defence is tested, for example signal verification, reputation tracking or reciprocity prompts. The paper only shows that no mechanism exists in current frameworks. Whether any fix helps non-Byzantine agents recover is unknown.
- Games with graded or partial-credit payoffs, longer horizons, or unfixed model-to-seat assignments are not run. These would show whether the 0%-cooperation result comes from the model or from the unanimity payoff.
- The claim that disclosing topology hurts is tested in one prompt wording. A neutral disclosure was not compared, so how much is framing and how much is information remains open.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - communication topology and channels]]
