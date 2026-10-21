---
title: Detecting Multi-Agent Collusion Through Multi-Agent Interpretability
authors: Aaron Rose, Carissa Cullen et al.
date: 2026-04
arxiv: 2604.01151
url: https://arxiv.org/abs/2604.01151
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2604.01151.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "agent evaluation benchmarks"]
---
# Detecting Multi-Agent Collusion Through Multi-Agent Interpretability

## One line
Frames collusion detection as a composite hypothesis test over per-agent activation probes (HELIOS) and tests it on a new benchmark, NarcBench, where probes catch collusion that transcript monitors miss but transfer poorly to emergent collusion.

## Method
Problem: agents can coordinate covertly, for example by steganography, so that nothing shows in the transcript. Monitors that read text are blind to this. The authors add a second monitoring surface, the agents' internal activations.

The idea is that detecting collusion is a joint test over all agents with an unknown colluding subgroup. The null is "no subgroup colludes". The alternative is "some subgroup does", and the monitor does not have to say which. Collusion is defined operationally: a group communicates (directly or indirectly) and then takes a harmful action. The causality requirement is dropped because counterfactual runs are usually unavailable.

Each agent gets one sensor, a linear "deception probe" (logistic regression on mid-layer activations). It is trained on instructed-collusion runs in one environment and gives each agent a scalar score. Five group-level statistics fuse the scores:
- **Peak Suspicion** is the maximum score. It is a generalised likelihood-ratio test (GLRT) when one colluder shifts a Gaussian score.
- **Deception Split** is the mean of the top two scores minus the mean of the rest, with colluder count known (2 of 4). It is also a GLRT, under Gaussian scores with a shifted mean.
- Three heuristics: **Sorted Concatenation** (activations sorted by score, then a classifier), **Activation Alignment** (mean pairwise cosine similarity of activations), and **Asymmetry Probe** (a classifier on score variance, range, split and mean).

The theory says that no uniformly most powerful test is known for an unknown subgroup, because the best test depends on how many agents collude and how strong the signal is. So no single statistic should win everywhere. The two GLRT results assume independent Gaussian scores, which the authors say will not hold in general.

## Evaluated on
- **Probes transfer zero-shot to out-of-distribution tasks.** Trained only on committee-vote deliberations (CORE, 50 scenarios, 17 domains), the best method on every one of four open-weight models reaches 0.99 to 1.00 AUROC on STEGO. STEGO is blackjack card counting with an agent-invented signalling code in table talk. Transcript judges, including strong Claude models, could not separate STEGO without a few examples of the protocol.
- **Structurally different tasks are harder.** On TRANSFER (code-review sabotage, pump-and-dump, RAG poisoning and others) results vary by model and family. For Qwen3-32B, family-level AUROC ranges from 0.28 to 1.00 depending on method. At a 1% false-positive rate, the best method (Deception Split) recovers only 0.38 of collusive runs, so AUROC overstates deployability.
- **No statistic dominates.** The best method changes with model and task, as the theory predicts. Activation Alignment is the best on STEGO for GPT-OSS-20B but near chance on TRANSFER for Qwen3-32B (0.48).
- **Detection tracks model capability.** The authors report that out-of-distribution AUROC rises roughly monotonically with parameter count across four models. GPT-OSS-20B, the smallest, is lowest, with an OOD mean of 0.59 to 0.79 by method.
- **Emergent collusion barely transfers.** On a third-party peer-review environment, 229 of 480 rounds had colluding agents, and only 2 of those 229 verbalised it. Zero-shot AUROC was 0.73 for Sorted Concat and 0.49 to 0.64 for the other four, so three of five methods were near chance.

## Limitations admitted by the authors
- Probes may fit spurious cues such as prompt wording rather than collusion. A null probe on honest agents scored near chance, but the authors give no proof that this rules out confounds.
- Labels are strict. Only runs where both colluders coordinated and executed were kept, so looser collusion is excluded. Labelling collusion is called inherently difficult.
- Colluders that know they are monitored may suppress the signal. A small evaluation-awareness test was run (Appendix H) but the authors call it far from comprehensive. A follow-up paper they cite finds fixed-threshold recall can drop sharply.
- Main results use only 4 agents with 2 colluders. A test with 8 agents shows weaker TRANSFER scores, for example 0.45 to 0.74 AUROC, and method rankings shift with group size. Real systems may have hundreds of agents.
- The method needs white-box access to every agent's activations, which the authors call a strong assumption.
- Probes trained on instructed collusion may miss emergent collusion, shown by the near-chance results above. Only one third-party environment is reported in the main text.

## Limitations found by others

## What it leaves untried
- Sequential detection that accumulates evidence over interactions, with formal stopping guarantees. One-shot detection at 1% false-positive rate recovers only 0.38 of structural collusion, and the authors name this as the next step.
- Training probes on emergent collusion, or methods that adapt to unknown group size. The paper shows the gap but not a fix.
- Counterfactual tests of the dropped causality criterion. CORE allows counterfactual runs, but none are run.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - agent evaluation benchmarks]]
