---
type: topic
group: Mechanisms
---
# Topic - adaptive reasoning depth

Spending extra compute (looping, partial chain of thought, handing off to a slow reasoner) only on inputs where the fast decision is unsure, and how the switch is decided.

Group: Mechanisms. See [[Topics]]. Same group: [[Topic - confidence-gated escalation]], [[Topic - calibration]], [[Topic - presentation sensitivity]], [[Topic - abstention and fallback]].

## Papers (6)
- [[2026-01 VAGEN GUI Agentic Reward Modeling]] — VAGEN: a tool-augmented verifier agent that first extracts evidence from a GUI agent's trajectory and, only when needed, actively probes the live environment for latent state (cheap-to-expensive progressive verification); OSWorld-Verified, AndroidWorld. (also: [[Topic - LLM and agent judges]])
- [[2026-05 Reasoning Is Not Free RACER]] — Reasoning judges help on structured-verification tasks (math, code) but give little or negative gain on simpler evaluations; RACER routes between reasoning and non-reasoning judges under budget and distribution shift. (also: [[Topic - LLM and agent judges]], [[Topic - judge and decision-model audits]])
- [[2026-10 SanSi]] — Turns a language model pre-trained to loop (Ouro-1.4B) into a typed decision model that reads option probabilities after every pass of the same layers, so one small model buys accuracy and reasoning depth with extra compute instead of extra parameters or generated text. (also: [[Topic - decision models]], [[Topic - open decision models]])
- [[2026-10 Selective Reasoning for Typed Decision Models]] — A single trained candidate-answer head on a frozen Qwen3.5-4B returns a typed choice either at once or from a partial chain of thought, with three small controllers deciding whether to start reasoning, when to query an answer, and when to accept it and cancel generation. (also: [[Topic - decision models]], [[Topic - open decision models]])
- [[2026-10 StartLux-Decision]] — A family of open decision models (0.8B to 27B) that answer typed questions in one forward pass and stop to reason only when unsure. Reasoning is trained with RLCD 2, which rewards the gain in proper-score quality of the decision probability and penalizes overlong traces. (also: [[Topic - decision models]], [[Topic - open decision models]], [[Topic - calibration]])
- [[2026-10 System Switch]] — A fast one-pass "System One" decision model takes every decision in real-time Doom and hands control to a slow vision reasoner only when a gate on its confidence or on lack of progress opens, and the paper measures what that deferral buys offline and in closed loop. (also: [[Topic - decision models]], [[Topic - confidence-gated escalation]])
