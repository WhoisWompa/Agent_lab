---
title: From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation
authors: Mengdie Flora Wang et al.
date: 2026-04
arxiv: 2604.07667
url: https://arxiv.org/abs/2604.07667
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2604.07667.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "confidence-gated escalation", "calibration", "social choice"]
---
# From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation

## One line
A post-hoc layer pools the verbalized probabilities of debating LLM agents and applies split conformal prediction, so a singleton answer is acted on and a larger candidate set goes to a human.

## Method
The problem: debate pipelines stop when agents agree, but agreement is not correctness. Social reinforcement can lead agents to unanimous wrong answers, and consensus stopping then commits the error with no recourse (0% escalation).

The fix reframes debate as a decision problem, "is any answer safe to act on?", in four stages.
- Three heterogeneous agents debate for four rounds. Each round every agent sees a summary of the previous round and outputs a full probability distribution over the options, elicited verbally because token log-probabilities are often unavailable.
- The distributions are combined by a linear opinion pool with uniform weights. This keeps the intensity of each agent's belief, which a majority vote throws away (0.6 versus 0.99 on the same option).
- Split conformal calibration on held-out labelled data sets a threshold on the score 1 minus pooled probability, separately for each pre-specified round. Under exchangeability, the true answer is then in the set with probability at least 1-alpha. This needs no assumption that any agent is calibrated; bad verbalized probabilities only make sets larger.
- Action policy: a singleton set means act autonomously, two or more options mean escalate to a human with the pruned candidates, and an empty set means full manual review. A set has more than one option exactly when the runner-up's pooled probability reaches the threshold.

The authors say they add no new conformal theory. The contribution is the contract between debate and deployment, plus the finding about what it catches.

## Evaluated on
Eight MMLU-Pro domains, LogiQA and GPQA, with Claude Haiku 4.5, DeepSeek-R1 and Qwen-3 32B.
- Coverage holds at each fixed round. At alpha 0.05 it runs 93.0 to 97.6%, and at 0.10 it runs 87.6 to 93.2%. Twenty repeated splits stay within 1.3 points of target.
- Wrong consensus is common. Of 1,963 initially disputed MMLU-Pro questions, 23.9% end in unanimous wrong agreement (Law 34.8%, Math 12.1%). Overall 14.1% of final answers are wrong consensus.
- The conformal layer flags them. 81.9% of the 586 final-round wrong-consensus cases get a non-singleton set. Only 31.9% of correct-consensus cases are also escalated, so the cost is real.
- Accuracy among cases resolved before the final round is 90.0 to 96.8%, up to 22.1 points above consensus stopping (Law: 90.0 vs 67.9%). The authors call this a selection effect, not better reasoning. It costs automation: on Law only 6.2% of cases are resolved automatically.
- Simple scalar rules do about as well. Top-probability and entropy thresholds flag 79.4 to 80.0% of wrong consensus versus 81.9%. The authors concede conformal does not give a better interception curve.

## Limitations admitted by the authors
- The guarantee is marginal, not per instance or per difficulty level. A singleton can still be wrong, and the paper reports no conditional guarantee.
- It holds only at a fixed pre-specified round. Stopping at the first singleton depends on the data, so those accuracy gains are empirical and carry no coverage claim.
- It needs exchangeable calibration and test data. A distribution shift, such as a different exam year, breaks it, and the authors only mitigate this by random splitting.
- Verbalized probabilities are noisy and prompt-sensitive. Parsing failures (0.77%) fall back to a uniform distribution. This affects set size but not validity.
- Cost: 12 LLM calls per question (3 agents, 4 rounds). Savings from early singletons range from over 98% of Math cases resolved to 6.2% of Law cases.
- Only closed-set multiple choice with 4 or 10 options was tested. Open-ended generation is left out. With binary labels, a non-singleton set would say little.

## Limitations found by others

## What it leaves untried
- Anytime-valid or simultaneous-correction conformal methods for adaptive stopping. The practical policy, stopping at the first singleton, has no guarantee today.
- Conditional coverage, for example by difficulty or domain (conformal risk control, group-balanced calibration). Law and Engineering show that the average hides large differences between domains.
- Learned or accuracy-based agent weights. Only uniform weights and one entropy variant (mean coverage change 0.6%) were tried. A cheaper single-agent baseline with the same conformal layer is also not tested, so the value added by the debate itself is unmeasured.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - confidence-gated escalation]] · [[Topic - calibration]] · [[Topic - social choice]]
