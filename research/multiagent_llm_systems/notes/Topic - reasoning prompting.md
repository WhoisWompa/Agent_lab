---
type: topic
group: Mechanisms
---
# Topic - reasoning prompting

Prompt-level techniques that elicit better single-model reasoning: chain-of-thought triggers, plan-then-solve, decomposition prompts, self-consistency voting, program-of-thought. The subject is the prompt wording and the reasoning text it produces, not a multi-agent structure or a critique loop.

Group: Mechanisms. See [[Topics]]. Same group: [[Topic - confidence-gated escalation]], [[Topic - calibration]], [[Topic - presentation sensitivity]], [[Topic - abstention and fallback]], [[Topic - adaptive reasoning depth]].

## Papers (9)
- [[2023-05 Plan-and-Solve Prompting]] — Replaces "Let's think step by step" with a trigger sentence that asks the model to first devise a plan and then carry it out (PS), and adds detailed instructions about variables and calculation (PS+), raising zero-shot reasoning accuracy with no demonstrations.
- [[2023-09 Cooperation, Competition, and Maliciousness]] — A scorable six-party, five-issue negotiation game that measures how well LLM agents cooperate, compete and resist a greedy or sabotaging teammate. (also: [[Topic - agent evaluation benchmarks]], [[Topic - strategic play among LLM agents]])
- [[2023-10 Avalon's Game of Thoughts]] — ReCon is a prompting scheme (private thinking, then a second pass that checks how others will read the draft speech) that helps LLM agents play the hidden-role game Avalon without being deceived or leaking their own role. (also: [[Topic - strategic play among LLM agents]], [[Topic - self-refinement and critique loops]])
- [[2023-10 Language Agent Tree Search]] — LATS wraps a single LLM agent in Monte Carlo Tree Search, using environment feedback, an LLM-scored value function and verbal reflections on failures, so it explores several trajectories instead of committing to one. (also: [[Topic - self-refinement and critique loops]])
- [[2024-02 More Agents Is All You Need]] — Sampling the same LLM many times and taking a majority vote (Agent Forest) raises accuracy steadily with the number of samples, often matching or beating more elaborate prompting and multi-agent frameworks. (also: [[Topic - multi-agent debate and consensus]], [[Topic - communication topology and channels]])
- [[2024-02 Rethinking the Bounds of LLM Reasoning]] — Re-tests the claim that multi-agent discussion beats a single LLM on reasoning, and finds that a single agent with a strong prompt (a worked demonstration) matches it, while discussion helps mainly when no demonstration is given. (also: [[Topic - multi-agent debate and consensus]])
- [[2024-03 Are More LM Calls All You Need]] — Shows that majority voting over many LM calls (with or without an LM filter) can get worse as calls increase, explains this by the mix of easy and hard queries, and gives a fitted model that predicts the best number of calls. (also: [[Topic - social choice]])
- [[2025-07 Self-Correction Bench]] — Shows that non-reasoning LLMs fix an error when it is attributed to the user but not when the identical error sits in their own turn (a 64.5% "blind spot"), traces this to missing error-correction data in post-training, and shows that fine-tuning or appending "Wait" removes most of it. (also: [[Topic - self-refinement and critique loops]])
- [[2026-08 Refining Over Resampling]] — Spends test-time compute on N independent reasoning rollouts, each repaired by D rounds of self-critique and self-correction, then majority-votes the refined answers, with no verifier and no training. (also: [[Topic - self-refinement and critique loops]])
