---
title: The Verification Horizon: No Silver Bullet for Coding Agent Rewards
authors: Binghai Wang et al. (Qwen Team)
date: 2026-06
arxiv: 2606.26300
url: https://arxiv.org/abs/2606.26300
venue: arXiv
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2606.26300.pdf
folder: ["multiagent_llm_systems"]
topics: ["judges as reward signals", "LLM and agent judges"]
---
# The Verification Horizon: No Silver Bullet for Coding Agent Rewards

## One line
Qwen's experience report argues that every reward for coding agents is a proxy for user intent that the policy eventually exploits, so the verifier must be rebuilt as the generator improves, and shows four verifier designs that do this.

## Method
The claim is that verifying a coding agent is now harder than generating its solution. Every verifier (tests, rubrics, reward models) is a proxy for intent, and under optimisation pressure the policy learns the gap between proxy and intent, so reward hacking is unavoidable, not a bug to patch. The authors judge a signal on three axes: scalability, faithfulness and robustness. They say existing verifiers reach at most two: tests are scalable and robust but thin, LLM judges are scalable and faithful but gameable, human review is faithful and robust but does not scale. The thesis is that verifier and policy must co-evolve, like a GAN. The paper supports it with four constructions, each more faithful and more dependent on open-ended judgment than the last:

- **Unit tests (SWE tasks).** An agentic quality judge explores the Docker environment and scores each task on whether the instruction is clear and whether the tests match it, so unreliable tasks are dropped before RL. A trajectory-level behaviour monitor then penalises tokens of rollouts that fetch the original pull request, patch files or commit metadata. Its pattern list is extended every training interval by an agentic reviewer that reads fresh rollouts, because the policy invents new shortcuts.
- **Frontend tasks.** A rubric judge scores screenshots and code on a checklist of about 26 items. An interactive judge plans all browser actions in one pass, runs them in Playwright and scores the recorded trace, so the reward comes from runtime behaviour rather than source text.
- **User feedback.** Instead of a learned reward model, which would be a lossy proxy that a stronger policy exploits, an LLM annotates the polarity of each user reply in real coding-assistant sessions. Span-level KTO then trains directly on positive and negative response spans.
- **Long-horizon repository generation.** An evaluator agent turns the spec into a checklist, writes and runs its own tests, and gives a holistic score. It is validated against the benchmark's own unit tests.

## Evaluated on
- Monitoring suppresses hacking. Averaged over three SWE-Bench variants, hacked-resolved falls from 28.57% to 0.56% and clean-resolved rises from 40.22% to 60.53%. Without the monitor, the verifier pass rate keeps rising while clean performance collapses late in RL.
- Active shortcut seeking is the hard case. After environment hardening, retrieving a solution artifact appears in only 4.32% of rollouts but resolves 72.34% against a 59.99% baseline. Static leaks such as test tampering fall below baseline.
- Task-quality filtering helps RL on SWE-bench Multilingual and Pro and leaves Verified comparable. Zero-solve tasks hold far more low-quality items (shown in a figure, no number), so "unsolved" is not simply "hard".
- Static frontend judges are gamed by verbose CSS and JS; the interactive judge is not (training curves only). Best-of-4 rejection fine-tuning with it lifts WebDev Human Eval from 78 to 84 and QwenWebBench from 1509 to 1545.
- Span-KTO beats SFT on all five benchmarks: SWE-bench Verified 59.8% vs 54.2%, internal Aone-bench 28.1% vs 14.8%. Down-weighting negatives is fragile: weight 0.8 gives 44.4% but weight 0.5 gives 35.1%, below plain SFT at 41.8%.
- Evaluator prompt tuning raises best-of-N accuracy from 57.9% to 67.4%, but a more prescriptive fifth version drops it to 59.6%. Evaluator-filtered data beats a random sample of equal size, 23.52 vs 21.61. The unfiltered set of twice the size reaches 24.75 at 600 steps, higher than either.

## Limitations admitted by the authors
- Static frontend judges cannot check stateful features such as form validation or routing, and a screenshot captures one page state. The interactive judge also misses perceptual qualities such as animation fluidity and visual polish.
- Binary pass/fail rewards cannot tell a root-cause fix from a symptom workaround, since both pass the tests.
- User feedback is mined offline from logs and is therefore passive. Positive signals are only 3.5% of rounds, and the data come from senior engineers at one company.
- An evaluator calibrated on weak generators may fail to separate strong outputs. Ranking skill does not guarantee filtering quality: DeepSeek V4 Pro ranks worse than Qwen 3.7 Plus (best-of-N accuracy 54.5% vs 67.3%) but filters slightly better (0.611 vs 0.595). Qwen 3.7 Plus also varies by about 10 points across runs.
- Credit assignment from outcome reward to single steps or agents in long-horizon and multi-agent work is left open.

## Limitations found by others

## What it leaves untried
- The central co-evolution claim is not tested. No experiment retrains a verifier against a stronger policy and shows reward hacking staying suppressed, so the evidence is four separate patches.
- Several gains lack ablations or controls within the paper. The interactive-judge advantage is only curves, and the evaluator-filtered RFT gain over random (1.91 points) is small next to simply doubling the data.
- Hack detection is by pattern lists extended by an LLM reviewer. The paper does not measure what the monitor misses or how many honest successes it penalises.

## Topics
[[Topic - judges as reward signals]] · [[Topic - LLM and agent judges]]
