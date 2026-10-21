---
type: topic
group: Judging and evaluation
---
# Topic - stopping rules

When to stop sampling, testing or evaluating: sequential tests (SPRT, group sequential), adaptive testing, Bayesian optimal stopping, sample-size reduction with valid error control. A confidence gate that routes cases to a bigger model is not a stopping rule unless framed as sequential testing.

Group: Judging and evaluation. See [[Topics]]. Same group: [[Topic - LLM and agent judges]], [[Topic - judge and decision-model audits]], [[Topic - trained judges and reward models]], [[Topic - agent evaluation benchmarks]], [[Topic - user simulation]], [[Topic - alternative evaluation paradigms]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]].

## Papers (2)
- [[2026-05 Sequential Consensus for Multi-Agent LLM Debates]] — Wraps a multi-agent debate in Wald's sequential probability ratio test on a judge's per-round consensus score, so the debate stops when the score is informative enough, and the calibration of that score tells you whether stopping can be trusted at all. (also: [[Topic - multi-agent debate and consensus]])
- [[2026-07 Verify, Repair, Repeat, or Stop]] — VRR-Stop decides when to stop a noisy verifier/repairer loop by estimating the probability the current plan is valid and stopping once one more repair is expected to do more damage than good, with a conservative keep-best fallback when the verifier cannot tell valid from invalid plans. (also: [[Topic - self-refinement and critique loops]])
