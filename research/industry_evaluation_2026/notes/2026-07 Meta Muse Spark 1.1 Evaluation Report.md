---
title: Muse Spark 1.1 Evaluation Report
org: Meta (Meta Superintelligence Labs)
date: 2026-07
url: https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report/
kind: lab-practice
category: frontier-labs
---
# Muse Spark 1.1 Evaluation Report

## One line
Meta's 9 Jul 2026, 112-page evaluation report for Muse Spark 1.1 (the model behind Meta AI and its API) covering Advanced AI Scaling Framework risk domains, adversarial robustness, a broad model-behaviour section incl. evaluation awareness and Petri audits, and capability benchmarks.

## What they do
- Three configurations evaluated: unmitigated model, 'System' (deployed with system-level safeguards), and 'Helpful' (no refusal training) as a capability upper bound.
- Catastrophic risk domains: Chem & Bio (SecureBio, WMDP, LAB-Bench, agentic science), Cybersecurity (CTFs, CyberGym 1,507 tasks, ExploitGym 869 tasks, social-engineering eval with judge-LLM ratings, insecure-code propensity, static and adaptive refusal on private and public benchmarks, false refusals), Loss of Control (reliability of pre-deployment assessment incl. sandbagging, AI R&D acceleration, monitorability, misaligned propensities).
- Adversarial robustness: StrongREJECT v2, FORTRESS (third party), AgentHarm Verified, AgentDojo, SWE-PI, Gray Swan ART (third-party red teaming). In an agentic attack benchmark, generation categories are scored by an LLM judge and the execution category "by verifiable container state (docker exec, no LLM)".
- Model behaviour: hallucination/calibration, risk escalation in coding agents, honesty (MASK, Deception Bench), sycophancy, scheming, evaluation awareness; automated alignment assessment with Petri 3.0 (auditor + target + judge; judge grades 38 dimensions, 12 reported, 1-10 scale); holistic principle-adherence eval; open-ended exploration (personality, self-description interviews, situational awareness: distinguishing training/eval/deployment, action-belief coherence, in-situ deployment interviews).
- Capabilities methodology: compares against Gemini 3.1 Pro, Claude Opus 4.8, GPT-5.5 at highest effort; for coding/agentic benchmarks uses competitors' self-reported results; for other benchmarks reports "the most favorable result between self-reported scores or our internal reproductions". OSWorld-Verified (361 tasks, execution-based checkers, 200 steps) and OSWorld 2.0 (108 workflows, median ~1.6 human hours / ~318 tool calls, mid-task goal changes) described in detail.

## Evidence
- Evaluation awareness (LLM classifier over CoT, lower bound): suspicion in 27.9% of samples on average, explicit safety-eval recognition 15.3%, definitive certainty 9.6%; awareness influenced behaviour in 14.3%, primary driver 1.6%. Agentic Misalignment eval: 75.0% suspicion, 53.4% awareness-influenced.
- Sandbagging: instructed-sandbagging monitor AUC 0.99 (oblivious) / 0.98 (monitor-aware); covert-sandbagging quadrant empty; strategic reasoning under evaluation pressure 12.6% / 17.9% / 30.1% (low/medium/high) with small performance deltas.
- Cyber: CyberGym 59.0% pass@1 (vs 43.5% for 1.0).
- Pre-mitigation, cannot rule out 'high risk' threshold in Chem/Bio and Cyber; mitigated to 'moderate or lower'.

## Limitations and criticisms
- Meta admits higher false-refusal rates than peers on cyber.
- Awareness analysis is "preliminary" and correlational; competitors cannot be compared since their full reasoning is not available.
- Choosing "the most favorable result" between self-reported and internal reproductions inflates competitor scores (conservative for Meta) but mixes methods.

## Relevance to agent evaluation
Meta adopted Anthropic's open-source Petri as its alignment auditing harness, showing cross-lab convergence on agent-auditor + judge pipelines. The report separates LLM-judged from state-verified outcomes in the same agentic benchmark, a useful pattern for agent judges.
