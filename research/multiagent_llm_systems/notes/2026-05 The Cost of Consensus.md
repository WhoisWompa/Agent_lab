---
title: The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate
authors: Blaž Bertalanič et al.
date: 2026-05
arxiv: 2605.00914
url: https://arxiv.org/abs/2605.00914
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2605.00914.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "self-refinement and critique loops", "communication topology and channels"]
---
# The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate

## One line
Teams of ten identical 7-8B models that debate and plurality-vote do no better than the same models revising their own answers alone, while using 2.1 to 3.4 times the tokens.

## Method
The problem: debate is deployed on the assumption that peers filter each other's hallucinations, but nobody had compared its cost and accuracy against simpler alternatives. The paper tests the bare debate primitive: N=10 identical agents, 3 rounds, no personas or roles, plurality vote with a confidence tie-break. In rounds 2 and 3 each agent reads the answers and shortened rationales of the other 9 peers.

The idea is the control design. The same revision prompt is given under three conditions: peer debate; isolated self-correction (the agent sees only its own previous answer); and a noise control (the agent sees rationales from unrelated problems). If debate beats both, peer content helps. If it does not, the gain comes from the revision structure, not the exchange.

The authors split debate failure into three model-dependent pathways:
- **Sycophantic conformity.** Agents drop their own answer for the most common peer answer. Measured as modal adoption rate.
- **Contextual fragility.** The longer peer context knocks over reasoning that was correct. Measured as vulnerability rate, the share of correct agents who turn wrong.
- **Consensus collapse.** The correct answer exists somewhere in the pool, but the vote discards it. Measured as the oracle gap, which is pool-has-correct accuracy minus team accuracy.

Cost is analysed separately: reading K peers costs O(N×K) prompt tokens, while output tokens stay roughly flat.

## Evaluated on
Qwen2.5-7B, Ministral-3-8B and Llama-3.1-8B on GSM-Hard and MMLU-Hard.
- **Revision itself accounts for the gain, not debate.** Qwen on GSM-Hard goes from 25.6% single-pass to 58.8% (debate), 63.2% (noise) and 61.0% (self-correction). Debate adds nothing over the controls.
- **Debate is equal or worse than self-correction.** Ministral on GSM-Hard: 20.7% debate vs 48.3% self-correction (p<0.001). Debate falls below its own single-pass 24.7%. Qwen on MMLU-Hard: 60.7% vs 66.7% (p<0.001). Llama gaps (39.3 vs 41.0, 45.0 vs 47.7) are not significant (p=0.155, 0.131).
- **Unrelated rationales beat relevant ones.** Qwen on GSM-Hard: noise 63.2% vs debate 58.8% (p<0.001). The paper says the noise traces may carry useful arithmetic, so this is not a pure non-semantic control.
- **Conformity is high and inflates agreement.** Modal adoption reaches 85.5% (Qwen, MMLU-Hard). Qwen's consensus is 90.1% under debate vs 81.7% under self-correction, with lower accuracy.
- **Correct answers are discarded.** Oracle gaps are 32.3 points (Ministral, GSM-Hard) and 24.3 points (Llama, MMLU-Hard, where the pool held the correct answer in 69.3% of cases and the team scored 45.0%). Agent-level recovery exceeded vulnerability for Qwen (18.8% vs 6.9% on GSM-Hard), yet the team still lost to self-correction, so the vote is blamed.
- **Cost.** Debate costs 17,401 to 28,631 tokens per problem against 5,335 to 12,831 for self-correction. A single agent given a 10x output budget matched or beat debate (+6.0 points for Qwen on MMLU-Hard, per the appendix).
- **Few peers are enough to cause it.** With K=2 peers, conformity is already 69.4% (GSM-Hard) and 77.2% (MMLU-Hard). Accuracy never exceeds self-correction at any K.

## Limitations admitted by the authors
- Only 7-8B instruction-tuned models were tested. Frontier and reasoning models (Qwen3, DeepSeek-R1) are untested. A 32B pilot showed more sycophancy (95.4%), but that is preliminary.
- Only unguided, homogeneous debate was tested. The claim that personas, adversarial roles or structured debate would not fix it is speculative, and the authors say it needs structured-debate baselines.
- The noise control uses coherent reasoning on other problems, not random tokens. It cannot cleanly separate context perturbation from transferred skill.
- Llama was run on only 100 items (margin of error about ±9.8%), and its two debate-vs-self-correction gaps are not significant. After Holm-Bonferroni correction those would stay non-significant, and the authors call them directional.
- Ministral's weak GSM-Hard debate result is partly a token-budget artifact. At 350 tokens, 82.2% of MMLU-Hard answers were invalid (an effective team of 1.8 agents). At a 1,024-token budget, modal adoption rose from 19.5% to 80.5%.
- Single team size (N=10) and a single revision prompt. Peers are shown in confidence-descending order, which may add a bias toward the most confident peer. Self-reported confidence is poorly calibrated.

## Limitations found by others

## What it leaves untried
- Smaller teams (N of 3 or 5) and structured debate with heterogeneous models or roles. These are the setups practitioners actually use, so the headline claim does not yet cover them.
- A prompt that explicitly encourages dissent, or a replacement for plurality vote. The oracle gap suggests the vote is a major source of loss, but no aggregator is tried.
- A pure random-token noise control, to give a clean non-semantic lower bound.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - self-refinement and critique loops]] · [[Topic - communication topology and channels]]
