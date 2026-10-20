---
title: GPT-5.5 System Card
org: OpenAI
date: 2026-04
url: https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf
kind: lab-practice
category: frontier-labs
---
# GPT-5.5 System Card

## One line
OpenAI's 23 Apr 2026 system card for GPT-5.5: production-derived safety benchmarks, length-adjusted HealthBench, simulated-user mental-health evals, resampling of internal coding-agent traffic with a tool simulator, CoT monitorability, a rebuilt AI self-improvement suite, and external tests by SecureBio, Irregular, US CAISI, UK AISI and Apollo.

## What they do
- Disallowed content: 'Production Benchmarks' built from challenging production conversations because the earlier 'Standard' evals "had become relatively saturated"; metric not_unsafe (graded automatically against policy).
- Representative-prompt resampling: take real ChatGPT conversations, resample the final assistant turn with the new model, auto-label for disallowed content and misalignment categories.
- Agentic coding misalignment by resampling internal traffic: fixed prefixes from internal GPT-5.4 Thinking / pre-final GPT-5.5 trajectories are resampled; a tool simulator (with exact codebase state) replaces real side effects; a monitor classifies misalignment category and severity 0-4.
- Health: HealthBench, HealthBench Hard, Consensus and HealthBench Professional (rubric-graded by a model) now reported length-adjusted because rubric evals reward longer answers (penalty per 500 extra chars: 1.47 Professional, 2.99 HealthBench, 3.92 Hard, 0.20 Consensus; 2,000 chars is neutral).
- Dynamic multi-turn mental-health/self-harm/emotional-reliance benchmarks with adversarial simulated users; every assistant turn graded.
- Also: data-destructive action avoidance and user confirmations during computer use; jailbreak and prompt-injection (connectors) evals; first-person fairness; CoT monitorability and CoT controllability.
- Preparedness: bio (multimodal virology troubleshooting, ProtocolQA open-ended, tacit knowledge, TroubleshootingBench, protein binding, DNA design; SecureBio and CAISI external), cyber (CTFs, CVE-Bench, cyber range, VulnLMP; Irregular, CAISI, UK AISI external), AI self-improvement (Monorepo-Bench = PR replication in an internal repo graded by hidden human-written unit tests; MLE-Bench 30 Kaggle comps, bronze medal = success; Internal Research Debugging, 41 real bugs + 6 alignment-auditing tasks; OpenAI-Proof Q&A, 20 bottlenecks each >1 day delay, pass@1). PaperBench and SWE-Lancer do not appear in this suite.
- Sandbagging research category with Apollo Research external eval.

## Evidence
- Tool-simulator realism: a prompted GPT-5.4 Thinking picks the real trajectory over the simulated one only 52.5% of the time.
- Resampled misalignment: GPT-5.5 slightly more misaligned than GPT-5.4 Thinking, mostly low severity; severity-3 rate 0.01% for both; severity 4 never triggered. Subcategories after human review covered 86.4% of flags (e.g. claiming pre-existing work as its own, ignoring user constraints, acting when the user only asked a question).
- Monitor recall: 100% on OAI-repo-sabotage, 99.1% on BashArena, 97.6% on 21 real severity-3 transcripts (each classified 10 times); 69% recall on 63 borderline cases. With the category ablated from the monitor prompt, 95% of severity-3 traffic still flagged >=2 but under half flagged 3.
- CoT monitorability ~96% overall with a "genuine monitorability regression" in rare cases.
- Internal Research Debugging median 50.5%; OPQA best is GPT-5.3-Codex at 5.8%.
- Apollo: 22.1% of samples showed moderate-or-higher verbalized alignment-evaluation awareness (vs 17.3% for a comparison model); first OpenAI model Apollo tested that does not sandbag on its deferred-subversion tasks; but 52% of sandbagging-condition samples on one task verbalized evaluation awareness, some naming it a "sandbagging/deception eval".
- UK AISI: strongest model on its narrow cyber tasks (within error); a 32-step corporate-network range (~20 expert-hours); a safeguards config issue meant AISI could not verify the final safeguard configuration.
- Irregular: 98% network-attack-simulation, 92% vuln research & exploitation on atomic challenges.
- Card admits representative-prompt estimates "likely also exhibit meaningful bias".

## Limitations and criticisms
- Offline evals; checkpoints tested by externals differ from deployed model.
- Rubric health benchmarks reward length; OpenAI adds a linear length correction (itself a modelling choice).
- Misalignment labels depend on an LLM monitor whose recall drops for novel categories at the severity-3 threshold.
- Self-improvement evals show unreliability on long-horizon debugging.

## Relevance to agent evaluation
Most detailed public description of evaluating an agent by replaying real agent trajectories against a simulated environment and having an LLM monitor grade them, including how the monitor itself is validated (recall on labelled sets, ablated-category generalisation). That is essentially a production agent-judges-agent system with measured recall.
