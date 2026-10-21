---
title: Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems
authors: Junze Zhu et al.
date: 2026-06
arxiv: 2606.01351
url: https://arxiv.org/abs/2606.01351
venue: ICML 2026
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2606.01351.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "agent evaluation benchmarks"]
---
# Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems

## One line
Models the entropy of an orchestrator's executor-scheduling distribution as a damped oscillation plus a logarithmic context-load term, fits it to 6 LLM orchestrators on a synthesized checkpoint benchmark, and finds that reasoning-heavy models make worse orchestrators.

## Method
The problem: in centralized multi-agent systems the orchestrator (the LLM that decomposes the query and picks which executor runs next) is the weak point. A manual failure attribution over four systems (deep research, coder, web browser, agentic RAG; GPT-4o orchestrator) puts a mean 67.7% of failures on the orchestrator and 32.3% on executors. The paper wants a way to say why, and a measurable signature per model.

The idea: at each step the orchestrator emits a probability vector over executors; its entropy is the "scheduling entropy". The authors posit two competing forces. A focusing term (task resolution) behaves like momentum optimization, so entropy rings down as a damped oscillation A·e^(-γt)·sin(ωt+φ). A dispersion term (context accumulation) acts like diffusion, so entropy grows as β·ln(t+1). The fitted curve H(t) = A·e^(-γt)·sin(ωt+φ) + β·ln(t+1) + H0 gives readable parameters: A is task complexity, γ solving efficiency, ω exploration pace, β context sensitivity, H0 intrinsic noise. The derivation rests on analogies (Nesterov momentum to a heavy-ball ODE; diffusion to log entropy) and an assumption that LLM inertia comes from attention over history. The paper does not test these assumptions directly.

To observe entropy at every step, standard benchmarks (GAIA, AssistantBench) are too opaque. Inverse Workflow Generation (IWG) starts from a QA pair, has a Scout agent derive the needed sub-tasks backward, and has a Wrapper agent synthesize the tool outputs and exact-match checkpoints. A three-tier validation (a small open model, a second model, human experts) keeps only solvable instances. The orchestrator then runs live in that synthetic environment, so trajectories are real.

## Evaluated on
- Two orchestrator archetypes. Oscillatory-aggressive models (DeepSeek-V3.1, Qwen-3-Max) have high A and ω, plan well structurally (DeepSeek LCS-F1 80.12) but finish few tasks (task success 29.69); DeepSeek's step accuracy drops from 92% to 22% at step 2. Smooth-conservative models (Claude-4.5-Sonnet, Gemini-2.5-Pro) have low ω; Claude has the highest step success (60.83) and the lowest β (0.87 vs 1.37 for DeepSeek).
- Fit quality: the equation fits the entropy traces of the six models, with regression p < 0.005 each. The paper offers no goodness-of-fit measure beyond that, and fits use a 6-step window.
- Parameters shift sensibly when conditions change. Replacing executor outputs with ground-truth evidence cuts A from 3.16 to 0.49 and γ from 1.56 to 0.10. Injecting noise raises A to 9.85. API-call tasks drop β to 0.01.
- "Reasoning Trap": within a model family, the low-thinking variant orchestrates better. GPT-5-Low uses about 69% fewer tokens than GPT-5-High and lifts step success from 0.251 to 0.302. Qwen3-Max-NoThink reaches 0.413 step success. In the main table, GPT-5 scores 11.71 task success and DeepSeek-R1 7.43, below most non-reasoning models. The authors attribute this to self-generated chain of thought squeezing the attention left for executor outputs. That mechanism is inferred, not isolated by an experiment.
- Real-world tasks (no synthetic observations) give A = 6.42 and β = 0.68 against the baseline's 3.16 and 0.47, which the authors call the same order of magnitude.

## Limitations admitted by the authors
- The orchestrator's 67.7% failure share is probably inflated: the orchestrator absorbs executor glitches as extra reasoning load, so some executor errors surface as orchestrator failures. The split rests on manual annotation.
- Real-world parameters differ from the IWG baseline (A 6.42 vs 3.16, β 0.68 vs 0.47, ω 1.03 vs 1.72), so synthetic difficulty only approximates real orchestration.
- Many models, especially with short contexts or weak instruction following, fail delegation so badly that their task success is too low to analyze; only six models were fitted.

## Limitations found by others

## What it leaves untried
- Using the parameters as a runtime signal, for example to cut or summarize context when β-driven entropy rises, or to pick a thinking budget; the paper only diagnoses.
- Causal tests of the physics: no ablation shows the oscillation reflects momentum rather than being a flexible curve with five free parameters fitted to short traces.
- Orchestrator designs that keep context small (summaries, task ledgers) were not tested against the context-squeezing explanation.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - agent evaluation benchmarks]]
