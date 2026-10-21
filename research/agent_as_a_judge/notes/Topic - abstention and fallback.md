---
type: topic
group: Mechanisms
---
# Topic - abstention and fallback

None-of-the-above, defer, other, ask a clarifying question, null gates: whether a model can decline to pick from the menu, and how reliably.

Group: Mechanisms. See [[Topics]]. Same group: [[Topic - confidence-gated escalation]], [[Topic - calibration]], [[Topic - presentation sensitivity]], [[Topic - adaptive reasoning depth]], [[Topic - reasoning prompting]].

## Papers (7)
- [[2024-07 Trust or escalate]] — Selective evaluation: the judge abstains when unconfident, with a calibrated threshold giving a provable lower bound on human agreement; Cascaded Selective Evaluation escalates from cheap to strong judges. (also: [[Topic - LLM and agent judges]], [[Topic - confidence-gated escalation]])
- [[2026-02 SCOPE selective conformal optimized pairwise LLM judging]] — Selective conformal risk control for pairwise judges; Bidirectional Preference Entropy (query both orders) as the uncertainty score. (also: [[Topic - LLM and agent judges]], [[Topic - presentation sensitivity]])
- [[2026-09 LAVOIR]] — Extends the open "System One" decision encoder Laya so that one forward pass returns both the decision distribution and, for each missing piece of information, how much asking about it would raise the probability of the correct answer, which lets the model decide whether to ask a clarifying question, decide, or hand off. (also: [[Topic - decision models]], [[Topic - open decision models]])
- [[2026-09 When the Right Answer Is Missing]] — Shows that the typed decision model Jev picks the right numeric answer from a menu 99% of the time but rejects a menu with no right answer only 7% of the time, even with an explicit NONE option, and repairs most of the gap with a rejection-probability threshold. (also: [[Topic - decision models]], [[Topic - judge and decision-model audits]])
- [[2026-10 Benchmarking Candidate Coverage and Rejection Policy Transfer]] — A benchmark showing that the "none of these" rejection thresholds of typed decision models (Laya, Jev, against Qwen2.5-7B) often stop working when moved to another task or candidate setup, and that different sources of missing answers give different tradeoffs. (also: [[Topic - decision models]], [[Topic - judge and decision-model audits]])
- [[2026-10 Jeva]] — A decision-native architecture for fast choose/yes-no/score judgments that encodes request and options separately, making decisions order-invariant, null-aware, scalable to thousands of options and cacheable across requests. (also: [[Topic - decision models]], [[Topic - open decision models]], [[Topic - presentation sensitivity]])
- [[2026-10 Lost in the Fallback]] — Introduces the Paired Fallback Robustness (PFR) Test and shows that open typed decision models (Jev-style choosers) often fail to pick a supplied fallback option ("Other", "Defer") even when they recognise the input's category, and flip decisions under logically equivalent wordings of the fallback rule. (also: [[Topic - decision models]], [[Topic - judge and decision-model audits]], [[Topic - presentation sensitivity]])
