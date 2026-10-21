---
title: Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement
authors: Jaehun Jung, Faeze Brahman, Yejin Choi
date: 2024-07
arxiv: 2407.18370
url: https://arxiv.org/abs/2407.18370
venue: ICLR 2025
category: alternative-paradigms
topics: ["LLM and agent judges", "confidence-gated escalation", "abstention and fallback"]
---
# Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement

## One line
Selective evaluation: the judge abstains when unconfident, with a calibrated threshold giving a provable lower bound on human agreement; Cascaded Selective Evaluation escalates from cheap to strong judges.

## Method
Confidence via Simulated Annotators (in-context simulation of several annotator personas; agreement ratio as confidence). Threshold calibrated on a small human-labelled set with a fixed-sequence testing bound. Cascade: e.g. Mistral-7B -> GPT-3.5 -> GPT-4, each abstaining below its threshold. Pairwise outputs only.

## Evaluated on
On a Chatbot Arena subset where GPT-4 alone almost never reaches 80% human agreement, the method guarantees over 80% agreement with almost 80% test coverage (from abstract); also TL;DR summarisation and other pairwise sets; cheaper than GPT-4-only.
- (llm-judge-foundations) On a Chatbot Arena subset where GPT-4 almost never reaches 80% human agreement, the cascade with Mistral-7B first guarantees >80% agreement at ~80% coverage.

## Limitations admitted by the authors
- Guarantee holds under exchangeability between calibration and test data.
- Coverage cost: some instances are never judged (left to humans).
- Pairwise preference only.
- Guarantee needs a calibration set exchangeable with test data; abstained items still need humans.

## Limitations found by others
- Badshah et al. 2026 SCOPE (arXiv 2602.13110) report up to 2.4x more accepted judgments than vanilla baselines under the same risk level, using bidirectional entropy to handle position bias.

## What it leaves untried
- Selective evaluation of agent trajectories with escalation to an agentic judge, then to a human.
- Applying guarantees under distribution shift or adversarial candidates.

## Topics
[[Topic - LLM and agent judges]] · [[Topic - confidence-gated escalation]] · [[Topic - abstention and fallback]]
