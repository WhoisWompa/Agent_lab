---
title: A Survey on Agent-as-a-Judge
authors: Runyang You, Hongru Cai et al. (PolyU, Cambridge, Huawei)
date: 2026-01
arxiv: 2601.05111
url: https://arxiv.org/abs/2601.05111
venue: arXiv
category: agent-as-judge
---
# A Survey on Agent-as-a-Judge

## One line
First dedicated survey of agentic evaluators; organises them into three stages of agency (procedural, reactive, self-evolving) and five capability dimensions, and lists open problems.

## Method
- Stages: **Procedural** (fixed workflows / fixed sub-agent roles, e.g. ChatEval, M-MAD, GEMA-Score 2503.05347, CAFES 2505.13965); **Reactive** (route and call tools/sub-agents conditionally on intermediate feedback, e.g. Evaluation Agent 2412.09645, AGENT-X 2505.15261, MAJ-Eval 2507.21028, Agentic Reward Modeling 2502.19328); **Self-evolving** (synthesise rubrics and update memory online, e.g. EvalAgent 2504.15219).
- Capability dimensions: multi-agent collaboration (consensus vs task decomposition), planning (workflow orchestration, rubric discovery), tool integration (evidence collection: Agent-as-a-Judge, CodeVisionary, ARM-Thinker; correctness verification: HERMES, VerifiAgent, Agentic Reward Modeling), memory & personalisation, optimisation (training-time: TIR-Judge 2510.23038, ARM-Thinker; inference-time).
- Companion list: github.com/ModalityDance/Awesome-Agent-as-a-Judge.

## Evaluated on
Survey, no experiments.

## Limitations admitted by the authors
- No consensus on what counts as an evaluation agent; many included "agents" are prompt-based role-play that may not meet stricter autonomy criteria.
- Open challenges: cost (RL training over long tool trajectories, multi-step inference), latency (conflicts with RL reward loops), safety (prompt injection and tool misuse widen attack surface; judge biases reinforced when judge is the reward), privacy (memory/personalisation leaks).
- Future directions: proactive personalisation, on-the-fly rubric generation, adaptive multi-granularity scoring, judges that probe the environment / escalate to edge cases, human-agent collaborative calibration, RL to internalise planning and tool use, jointly trained multi-agent judges.

## Limitations found by others
- Placement is inconsistent (MAJ-Eval reactive in one section, near self-evolving in another) (own reading).
- Does not discuss non-determinism / run-to-run variance or gaming by the judged agent (own reading; cf. Gaming the Judge 2601.14691).

## What it leaves untried
- An empirical comparison across the taxonomy on a common testbed.
- Treatment of adversarial agents under test.
