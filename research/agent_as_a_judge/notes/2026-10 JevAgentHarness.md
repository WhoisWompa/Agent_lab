---
title: "JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs"
authors: Kunlun Zhu et al.
date: 2026-10
arxiv: 2610.21412
url: https://arxiv.org/abs/2610.21412
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/JevAgentHarness - Benchmarking, Deploying and Training Decision Models That Share Control with LLMs (Zhu 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "confidence-gated escalation"]
---
# JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs

## One line
Hands an agent's routine multiple-choice steps (which tool, which argument, whether to reflect) to a cheap decision model such as JEV, accepting its answer only above a per-choice confidence threshold fitted on the agent's own runs, and trains a 4B decision model on the states the agent actually visits.

## Method
Harnesses call a large LLM at every step, yet most steps are a choice from a list. A decision model scores the listed options directly: one JEV call took 28% of an LLM call's time and 2.6% of its price. But decision models are tested on fixed questions. Inside an agent their errors carry forward, and they face states that follow the agent's own mistakes.

- **Delegation rule.** Eight decision points (tool, arguments, action, memory read/write, reflect, stop, routing) and five modes (REPLACE, CASCADE, ASSIST, GUARD, TRIGGER). In the main mode, the cascade, the model's answer is used when c ≥ τ, otherwise the LLM decides. Accepting pays when the model's accuracy at c minus the LLM's accuracy is ≥ −ΔC/V, where ΔC is the saved call's price and V the success lost to one wrong choice. So the model may be slightly worse than the LLM if the saving covers the risk. τ is fitted from silent "shadow" runs and refitted whenever the LLM, the model or the rules change.
- **AgentDecisionBench.** Scores models on isolated questions (L1), recorded agent states (L2) and live control (L3). It runs on DecisionGym, a simulated shop that knows the acceptable next steps at every reachable state.
- **AgentDecision-4B.** Qwen3-4B trained on 15,694 visited states, 30.9% of them after scripted mistakes. Labels mix gold with JEV's probabilities, plus a Brier calibration term. GRPO follows.

## Evaluated on
- **Isolated scores misrank models.** StartLux-9B led BFCL tool choice (92.2%) but solved 69.5% of agent tasks. AgentDecision-4B (89.3%) solved 91.5% and JEV 82.0%. The spread was 5.1 points on L1 and 57.5 on L3.
- **The fitted threshold protects success.** JEV's tool-and-argument cascade cut cost 14.2% without changing any of 500 outcomes. Thresholds came out at 1.00 and 0.99. A fixed 0.5 threshold lost 21.5 points.
- **The trained model is what makes delegation pay.** The chosen combination with JEV lost 2.2 points and failed non-inferiority. With AgentDecision-4B it was +0.6 points at 81.1% lower cost. Agents ran 81.1–89.0% cheaper and up to 2.5× faster.
- **SFT on agent states does the work.** It raised shifted-task step accuracy from 52.9% to 98.4%. GRPO added nothing measurable.
- **Coding agents gain little:** 7.0–10.5% savings, and SWE-agent lost 6.0 points.

## Limitations admitted by the authors
- **Thresholds and model are tied to one agent.** Given a new cancel-or-ship rule, AgentDecision-4B stayed confident but was only 81.6% right. The agent solved 3.0% of tasks against 88.0% for the LLM alone.
- **The gate does not notice shift.** On shifted tasks the 4B models kept taking nearly all tool choices and lost 6.0–7.5 points.
- **Confident irreversible errors.** All 34 of JEV's failed tasks began with an irreversible wrong tool choice, usually cancelling where it should have asked.
- **The benchmark is saturated and templated.** The LLM alone solves 99.4%. A one-tool-per-template lookup gets almost every common state right, so most of the trained models' lead reflects the generator's conventions.
- **Transfer failed.** The refitted delegation lost 8.1 points on τ²-bench. On ALFWorld the DecisionGym-trained model scored 64.7%, against 61.1% for its untrained base.
- **Guards are not safety controls.** The stop guard accepted 40.7% of Flash-Lite's wrong finishes. Injection attacks were untested.
- English only, mostly Gemini, and no comparison to learned routers.

## Limitations found by others

## What it leaves untried
- **A drift monitor that hands control back.** The authors propose tracking the share of answers above the threshold but do not build it. Under shift the gate stayed confident while success fell.
- **Per-option costs for irreversible actions.** V is one number per decision point, yet every failure observed was a confident irreversible write.
- **A realistic, non-saturated environment** to show the training gain is more than learning DecisionGym's templates.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - confidence-gated escalation]]
