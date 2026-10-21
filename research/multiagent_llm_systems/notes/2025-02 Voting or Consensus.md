---
title: Voting or Consensus? Decision-Making in Multi-Agent Debate
authors: Lars Benedikt Kaesberg et al.
date: 2025-02
arxiv: 2502.19130
url: https://arxiv.org/abs/2502.19130
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2502.19130.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "social choice"]
---
# Voting or Consensus? Decision-Making in Multi-Agent Debate

## One line
Holding everything else fixed, it compares seven ways a debating LLM team picks its final answer (four voting rules, three consensus thresholds) and proposes two drafting schemes that raise answer diversity.

## Method
Earlier debate papers changed the decision protocol together with other settings (turn order, prompts, agent count), so no one knew what the protocol itself contributed. Here three expert-persona agents (same base model) discuss a question and only the rule that ends the discussion changes.

- Consensus protocols: agents say whether they agree with the previous message, and the debate ends when more than 50% (majority), more than 66% (supermajority) or all (unanimity) agree.
- Voting protocols: several candidate solutions stay alive, and from the third turn the agents vote. Rules are simple, ranked, approval (unlimited votes) and cumulative (25 points to split). A tie triggers another round.
- The authors' explanation for the split: voting keeps several reasoning paths alive, which suits reasoning. Consensus makes several agents confirm the same statement, which catches small factual errors that a vote can miss. They saw voting fooled by answers that look right but contain wrong statements.
- Two new methods target answer diversity, because agents tend to be agreeable and only polish the first agent's draft. All-Agents Drafting (AAD) makes every agent write its own solution before any exchange. Collective Improvement (CI) also starts from independent drafts, but agents never talk to each other: each round they only see the previous round's solutions. CI works only with voting, since it removes turn order.
- Two extra response styles were tried: a critical one and one that shares only reasoning, not final answers.

## Evaluated on
Llama 3 8B (and 70B in the appendix) on three knowledge tasks (MMLU, MMLU-Pro, GPQA) and three reasoning tasks (SQuAD 2.0, StrategyQA, MuSR).
- Task type decides the better protocol: voting beats consensus by 13.2% on reasoning (SQuAD 2.0 F1 56.7 vs 43.6), consensus beats voting by 2.8% on knowledge. On StrategyQA the gap is only 0.2%, so that dataset does not separate them.
- Consensus is cheaper in rounds: 1.42 rounds on average against 3.38 for voting. Against a CoT baseline the debate costs about 5 times the compute (consensus) and 10 times (voting).
- On SQuAD 2.0, stricter consensus (unanimity) does better on unanswerable questions, while voting is better on answerable ones.
- Approval voting fails to reach a decision in 59% of cases, because agents vote for almost every answer and create ties.
- More agents helps slightly, more rounds before voting hurts slightly on StrategyQA (linear trends only, with a jump at round ten). When agents are asked to challenge a final answer, the extra round does not improve it, and made reasoning answers worse in 3% of cases. This is read as problem drift and as doubt about self-refinement.
- AAD gives +3.3% and CI +7.4% over the debate baseline on StrategyQA (62.8% and 65.7% against 58.3%). The critical style gives +1.1% and the reasoning-only style -6.4%. Answer similarity (SBERT cosine) is lowest for CI (0.845) and highest for reasoning-only (0.916), which the authors read as diversity driving accuracy.

## Limitations admitted by the authors
- Debate is very costly (hundreds of forward passes), so every dataset is a sampled subset with three runs. The authors say the gaps exceed the standard deviation, but variance remains.
- Agents still converge on similar answers even with AAD and CI, so diversity is only partly achieved.
- Prompt design and persona choice were not ablated; the persona ablation was skipped for cost, citing outside evidence that personas matter little.
- Gains must be weighed against the compute (5 to 10 times a CoT baseline), and may not scale with it.
- With Llama 3 70B the debate rarely beats the CoT baseline, so the benefit depends on the base model's weakness (appendix explanation: small models hallucinate more and a second agent rarely repeats the same hallucination). The weaker 8B and 70B comparison is explained, not tested.

## Limitations found by others

## What it leaves untried
- AAD, CI and the round and agent scaling are tested on StrategyQA only, so it is unknown if the diversity-accuracy link holds on knowledge tasks; the diversity-accuracy link itself is a correlation over five settings, with no causal test.
- Only one model family and persona count (three) are used; mixing different models, which would raise diversity more directly, is not tried.
- Power structure between agents (a leader or a manager persona) is named as future work but not explored.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - social choice]]
