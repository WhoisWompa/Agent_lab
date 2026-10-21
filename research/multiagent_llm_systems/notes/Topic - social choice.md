---
type: topic
group: Game theory
---
# Topic - social choice

Aggregating outputs, votes, rankings and judge scores from several agents: Arrow, Gibbard-Satterthwaite, voting rules, judgment aggregation, fair division, computational social choice.

Group: Game theory. See [[Topics]]. Same group: [[Topic - contract theory]], [[Topic - cooperative game theory]], [[Topic - information design]], [[Topic - inverse reinforcement learning]], [[Topic - mechanism design]], [[Topic - preference learning]], [[Topic - stackelberg games]], [[Topic - team theory and distributed decision making]].

## Papers (4)
- [[2023-09 ReConcile]] — Several different LLMs (ChatGPT, Bard, Claude2) discuss a reasoning question over up to three rounds, seeing each other's answers, explanations and stated confidence, and the team answer is a confidence-weighted vote. (also: [[Topic - multi-agent debate and consensus]])
- [[2024-03 Are More LM Calls All You Need]] — Shows that majority voting over many LM calls (with or without an LM filter) can get worse as calls increase, explains this by the mix of easy and hard queries, and gives a fitted model that predicts the best number of calls. (also: [[Topic - reasoning prompting]])
- [[2025-02 Voting or Consensus]] — Holding everything else fixed, it compares seven ways a debating LLM team picks its final answer (four voting rules, three consensus thresholds) and proposes two drafting schemes that raise answer diversity. (also: [[Topic - multi-agent debate and consensus]])
- [[2026-04 From Debate to Decision]] — A post-hoc layer pools the verbalized probabilities of debating LLM agents and applies split conformal prediction, so a singleton answer is acted on and a larger candidate set goes to a human. (also: [[Topic - multi-agent debate and consensus]], [[Topic - confidence-gated escalation]], [[Topic - calibration]])
