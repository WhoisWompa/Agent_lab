---
title: From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents
authors: Laksh Advani et al.
date: 2026-06
arxiv: 2606.09863
url: https://arxiv.org/abs/2606.09863
venue: ICML 2026 Workshop on Failure Modes in Agentic AI (FAGEN)
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2606.09863.pdf
folder: ["multiagent_llm_systems"]
topics: ["judge and decision-model audits", "LLM and agent judges", "agent system failure analysis"]
---
# From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents

## One line
Agents often claim a task is done when the environment state says it is not, LLM judges cannot catch this (AUROC at most 0.65), and a TF-IDF classifier catches it far better.

## Method
The problem is "false success": the agent's own claim of completion contradicts the programmatic environment state. It is silent, because unlike a crash or hand-off nobody is alerted.

The paper does two things. First, it measures how common the failure is. On tau2-bench (customer service) a failed trajectory counts as false success if its closing message matches completion phrases ("successfully", "refund of $N") and no hand-off phrases. Honest failures are the reverse. On AppWorld (coding agents) the label is text-independent: the agent wrote status=success to a supervisor database while the unit tests failed.

Second, it compares monitors. LLM judges read the trajectory and say whether the task was completed. Lightweight detectors (bigram TF-IDF with logistic regression or XGBoost, and a fine-tuned DeBERTa) are trained against the ground-truth labels. On AppWorld the detector sees only the API-call sequence.

The central claim is a mechanism. Judges read surface completion proxies as evidence of success, and false success produces exactly those proxies. On tau2-bench the proxy is confident closing language. On AppWorld it is the sheer number of actions. A detector trained against ground truth learns the opposite signal. On AppWorld, false success looks like repeated read-only calls with no write, while honest failure looks like write retries and checking state after claiming done.

## Evaluated on
- **False success is common and varies by setting.** It is 45% and 48% of failures in tau2-bench airline and retail, 3% in the dual-control telecom domain, and 75.8% among AppWorld self-assessing trajectories. Per-model rates run from 13% (GPT-5.2) to 79% (Qwen3-Max-Thinking), so a reasoning model is no safer; its traces rationalize completion rather than verify it.
- **Judges fail.** No configuration reaches AUROC 0.65 on tau2-bench across 5 judges and 5 prompt styles. Giving the judge the full ground-truth task spec moves the best judge from 0.640 to 0.632. On AppWorld the best is 0.537 (GPT-4o), and Sonnet gets worse with more context (0.368 to 0.274).
- **The judge mechanism is anchoring.** Against honest failures, judges score assertion-language trajectories as more "completed" by 0.27 to 0.36, whatever the outcome.
- **Simple detectors win.** Task-disjoint AUROC is 0.83 to 0.85 on tau2-bench and 0.95 on AppWorld. A linear model is within 0.03 AUROC of DeBERTa.
- **Better triage and lower latency.** At a 10% human-review flag rate the detector finds 72% of false successes versus 13% for the best judge. Inference takes 1.19 ms versus about 4,000 ms.
- **The labels are not circular.** Dropping the closing message costs only 0.008 AUROC, and AppWorld labels share no text with its features.

## Limitations admitted by the authors
- Only structured-API benchmarks were tested. Whether this holds for web navigation, open-ended code or scientific reasoning is unknown.
- The AppWorld rate (75.8%) covers only two of four architectures. The other two always write status=success, so their status carries no information, and the rate does not describe the whole benchmark.
- The detector does not transfer across domains zero-shot: airline to retail gives AUROC 0.69. Fifty to 100 labeled examples per class raise it to 0.79 to 0.83, so each deployment needs a calibration set. Transfer from tau-v1 to tau2 is 0.73.
- It is a triage signal, not an autonomous monitor. At a 10% flag rate precision is 50%, so half the flags are false alarms.
- It is weak against adversarial wording. Rewriting honest-failure closings in confident style flips the detector on 20% of cases (10 of 50) and judges on about 24%.
- The environment-structure effect rests on one dual-control domain with 15 false-success cases. It is a hypothesis, not a causal result.

## Limitations found by others

## What it leaves untried
- Direct checks of trajectory against environment state (did a write call actually succeed?). The authors say these are needed for high-stakes use but do not build or test them.
- Dual-control or independent-verifier setups in more than one domain. This would show whether verification suppresses false success, which they only conjecture.
- A judge given tool access to inspect state, instead of reading text. Their judges only read transcripts, so the failure may be a limit of reading rather than of judging.

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - LLM and agent judges]] · [[Topic - agent system failure analysis]]
