---
title: Debating Truth: Debate-driven Claim Verification with Multiple Large Language Model Agents
authors: Haorui He et al.
date: 2025-07
arxiv: 2507.19090
url: https://arxiv.org/abs/2507.19090
venue: WWW 2026
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2507.19090.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "role-based agent teams"]
---
# Debating Truth: Debate-driven Claim Verification with Multiple Large Language Model Agents

## One line
DebateCV has two opposed debater agents argue a claim over shared evidence while a moderator, fine-tuned on synthetic debates, issues the verdict and justification, beating single-agent and other multi-agent verifiers on AVeriTeC.

## Method
Problem: a single LLM that reads retrieved web evidence in one chain of thought can miss the decisive item. The paper's example is a refutation based on 2008 urbanisation figures, although newer evidence supporting the claim had been retrieved. Majority voting and CAMEL-style cooperation add agents but no adversarial scrutiny, so they can reinforce a shared error.

Idea: copy the "star chamber" sessions of professional fact-checkers. An Affirmative and a Negative Debater see the same evidence set and alternate opening, rebuttal and counter-argument. After each round a Moderator writes a summary and checks convergence, meaning the new summary is highly similar to the last. It stops early on convergence or at a round cap. It then weighs both sides and gives one of four verdicts (Supported, Refuted, Not Enough Evidence, Conflicting Evidence/Cherry-picking) with a justification. The roles and fixed turn order are prompt-enforced.

Second problem: zero-shot LLMs debate well but moderate badly. The Moderator defaults to neutral verdicts even when the evidence decides the claim, which the authors attribute to conformity bias (their explanation, not tested directly). No debate-with-verdict dataset exists. Debate-SFT builds one:
- Run zero-shot DebateCV over an existing labelled claim set.
- Where the Moderator disagrees with the human label, an LLM Corrector (GPT-4o) writes a justification that reaches the ground-truth verdict from the debate transcript.
- Fine-tune the Moderator on all debates, the originally correct ones plus the corrected errors.

The resulting dataset, SynDeC, holds 3,068 debates, of which 936 needed correction.

## Evaluated on
AVeriTeC dev set (500 claims) with golden evidence and two retrieval pipelines. The Moderator is an 8B open model, the Debaters are GPT-4o-Mini.
- Beats the strongest baseline (HerO, a fine-tuned single agent) by at least 2.0 points on golden evidence and 2.6 to 5.8 points on retrieved evidence. With Llama-3.1-8B: 83.4 golden, 72.8 and 73.6 on the two retrieved settings. HerO gets 80.4, 70.2 and 67.8.
- Other multi-agent setups barely help. Majority voting gains 0.6 points over CoT with GPT-4o under retrieved evidence, and CAMEL-style cooperation falls below CoT for small models (Qwen-2.5-7B: 62.6 to 60.8 under Retrieved (H)).
- Fine-tuning the Moderator is where the gain comes from. Without Debate-SFT, Llama-3.1-8B drops from 72.8 to 53.8 under Retrieved (H). False Not Enough Evidence verdicts fall from 25.0% to 0.4%, and false Conflicting Evidence verdicts from 6.3% to 1.1%.
- The corrected-error samples carry robustness to noisy evidence. Removing them costs 9.8 points under Retrieved (H) (72.8 to 63.0). Removing the originally correct samples costs only 2.4 points there, but 6.6 under golden evidence (83.4 to 76.8).
- Justifications are rated higher by 36 journalism and communications postgraduates on 50 claims both systems got right. MOS gains are 1.07 (evidence used), 0.85 (uncertainty) and 1.10 (reasoning), and DebateCV is preferred in 50.5 to 57.6% of comparisons.
- The Debater model hardly matters: accuracy moves from 72.8 to 71.8 across three Debater LLMs.

## Limitations admitted by the authors
- Inference cost is high, because several agents run several rounds per claim. The paper names this as future work and gives no cost figures.
- Performance under extremely noisy or heavily polluted evidence is untested. Retrieved-evidence accuracy (about 73%) is still 10 points below golden evidence (83.4%).
- The zero-shot Moderator's error rate rises in later debate rounds, which the authors attribute to multi-turn degradation. Fine-tuning mitigates it but the cause is not isolated.

## Limitations found by others

## What it leaves untried
- Cost-matched comparison. The baselines use one call or three, DebateCV uses many, and the paper never gives an equal-compute baseline such as a larger self-consistency vote. The accuracy gain therefore cannot be separated from extra compute.
- Training the Debaters. Only the Moderator is tuned, and the Debater model barely matters (72.8 vs 71.8), so any benefit of stronger or trained advocates is unknown.
- Using the Corrector's labels beyond one benchmark. The authors say Debate-SFT should transfer to other debate settings, but only AVeriTeC was used and the claim is unsupported.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - role-based agent teams]]
