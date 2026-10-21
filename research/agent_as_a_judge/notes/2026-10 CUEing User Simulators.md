---
title: "CUEing User Simulators: Calibrated User Embeddings for Multi-Turn Benchmarking"
authors: Anjali Kantharuban et al.
date: 2026-10
arxiv: 2610.02460
url: https://arxiv.org/abs/2610.02460
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/CUEing User Simulators - Calibrated User Embeddings for Multi-Turn Benchmarking (2026).pdf
folder: ["agent as a judge"]
topics: ["user simulation", "agent evaluation benchmarks"]
---
# CUEing User Simulators: Calibrated User Embeddings for Multi-Turn Benchmarking

## One line
Steers any LLM to play a benchmark user from a continuous user embedding decoded into persona commands, and argues simulators should be judged by whether agents fail with them as they do with real users.

## Method
- **Problem.** Multi-turn agent benchmarks use an LLM as the user. Simulators are usually scored on *fidelity*, meaning human-looking dialogue. The paper argues benchmarks need *outcome calibration*: the same success rates and failure causes as with real users. A fluent simulator can over-cooperate or never trigger the agent errors that humans trigger, and the two criteria rank methods differently.
- **Idea.** Encode each session into one continuous vector (a CUE). A small LM decoder turns the vector into natural-language commands (general, user-specific, style). These commands, plus eight retrieved example turns, are added to the benchmark's normal simulator prompt. The text interface lets any black-box LLM be the simulator without retraining.
- **Supervision.** For each of roughly 170k training sessions, an LLM writes commands by contrasting the real user with generic simulators' replies (this removes simulator artifacts) and with other humans (this keeps individual variation). Benchmark rewards and failure labels are never used, so any calibration gain is a by-product of modelling behaviour.
- **Two uses.** *Replay* encodes a recorded human session to re-run the task as that user, so costly human studies can be reused on new agents. *Sampling* uses a latent diffusion model over the CUE space to generate new users, giving more variety than resampling the stored bank.
- **Assumption.** Losses suppress task and outcome content in the vector, but the authors say this "cannot guarantee removal".

## Evaluated on
- **A persona is not automatically better.** The no-persona simulator is closest to the human success rate of 0.61 on Llama 3.1 8B (error 0.21 vs CUE 0.35). Some persona methods distort outcomes badly: RealUserSim's user-share gap on Gemini is 0.62 vs 0.12 for no persona.
- **CUE aligns best on stronger base models.** Success-rate error is 0.12 vs 0.21 for no persona on Gemini 3.5 Flash Lite. Replay outcome F1 is the best among persona methods on all three base models (0.62 on Gemini), but on Llama it is below no persona (0.46 vs 0.50).
- **CUE has the lowest user-share gap among persona methods on every base model** (0.06 on Gemini vs 0.67 for PPol). It also has the best failure-mode F1 on GPT and Gemini, though the paper says failure-composition differences are small except for USP.
- **It transfers to writing.** SimulatorArena document-quality error is 2.21 vs RealUserSim's 5.80, but still above the 0.85-1.48 gap between two humans.
- **Fidelity stays competitive.** Coverage is best or tied-best (S2R-C 0.83 vs 0.64 for no persona on GPT). Shuffling CUEs between sessions drops mimicry (PT3 0.38 to 0.21), so the vector is user-specific.

## Limitations admitted by the authors
- The paper uses two human studies and one evaluated agent (GPT 5.2). It never tests whether agent *rankings* are preserved, which is the purpose of a benchmark.
- The gains are not attributed to components. Comparisons are end-to-end without matched supervision, retrieval is part of CUE's treatment, and the ablations show only that diffusion improves coverage over the bank (0.83 vs 0.77). They do not show that the embedding or the sampler causes the calibration gains.
- Replay is retrospective. It does not show prediction of a user's future behaviour.
- Failure attribution and failure modes are labelled by an LLM, so the failure metrics inherit that labeller's errors.
- Results on the weak base model are mixed: on Llama it loses to no persona. The authors say CUE "remains imperfectly calibrated".

## Limitations found by others

## What it leaves untried
- Rank several agents with humans and with CUE users and check that the leaderboards match. The paper names this as untested, and it is the property a benchmark needs.
- Train directly on outcome or failure signals, to see whether that closes the remaining gap or only overfits one human study.
- Run a matched control: same retrieval and data, discrete profiles vs continuous CUE. This would isolate whether the continuous representation is what helps.

## Topics
[[Topic - user simulation]] · [[Topic - agent evaluation benchmarks]]
