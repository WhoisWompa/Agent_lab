---
title: Teaching Language Models to Critique via Reinforcement Learning
authors: Zhihui Xie et al.
date: 2025-02
arxiv: 2502.03492
url: https://arxiv.org/abs/2502.03492
venue: ICML 2025
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2502.03492.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "trained judges and reward models"]
---
# Teaching Language Models to Critique via Reinforcement Learning

## One line
CTRL trains a separate critic LLM with reinforcement learning to write feedback that makes a fixed, black-box generator's revised code pass more tests, with no human critique labels.

## Method
The problem is the feedback bottleneck. Self-critique gives almost nothing (Pass@1 7.88% to 8.36% on CodeContests). Reward models squeeze quality into one number. Raw execution traces are low-level and do not tell the model what to change (8.97%).

The paper splits the loop into two abilities and models it as a Markov chain on solution correctness. Discrimination is judging whether a solution is right. Critiquing is the chance of fixing a wrong solution (p_cw) while not breaking a right one (p_cc). In simulation, strong critiquing (p_cc 0.9, p_cw 0.3) can make up for weak discrimination, and the gain compounds with more rounds. Best-of-n without critiquing plateaus. This is a simulation with chosen parameters, not a measured result.

The critic is a separate model that sees the problem and the solution and writes three parts: an analysis, improvement suggestions and a correct/incorrect verdict. The loop stops when the verdict says correct. It is trained in two stages.
- **Stage I, execution-guided synthesis.** A sandbox runs the initial solution. The result (pass, total failure, or a failing test with its error message) becomes a hint, and the model reasons over it to write a critique. The hint is then removed and the model is fine-tuned on the critique, which makes the critic learn the execution-based strategy without needing the sandbox. This stage mainly improves discrimination (macro F1 61.19 to 68.55), but the revisions it produces break correct code often (regression rate 3.03%).
- **Stage II, RL with GRPO.** The reward is whether the generator's revision, written from the critique, passes all tests. A critique's value depends on a sampled solution, so the policy gradient has a large variance. PPO's value network gave unstable estimates. GRPO instead samples 8 critiques per problem and normalises rewards within the group, so problems that are too easy or too hard give no gradient. The sandbox is used only in training. At test time the critic works alone.

The critic is trained against Qwen2.5-Coder-32B as generator and then paired with other generators.

## Evaluated on
- RL cuts regressions while raising the pass rate. On CodeContests, CTRL gets 11.76% Pass@1 against 7.88% zero-shot, and the regression rate is 0.85% against 3.03% for the SFT-only critic.
- It scales with iterations although it was trained on single-turn critiques. Three rounds reach 15.15% Pass@1 with regression still at 0.85%. Five rounds with Qwen2.5-Coder as generator average 42.77% across three benchmarks, against 38.30% for self-critique and 39.98% for a GPT-4o critic.
- A weak critic helps a stronger generator. With GPT-4o as generator, CTRL moves CodeContests from 20.61% to 25.45% after five rounds. The paper reports up to 106.1% relative gain with its own base model and 23.5% with GPT-4o.
- Errors compound less. Self-critique and GPT-4o critics have rising regression rates over rounds, and CTRL stays lower (Figure 4, no exact figures in the text).
- It transfers to judging. On JudgeBench (general-domain pairs of GPT-4o answers) it reaches 64.3% overall, comparable to Claude-3.5-Sonnet, although it was trained on code only. Accuracy rises with the number of majority votes (22.6% at the smallest count shown, 64.3% at the largest).

## Limitations admitted by the authors
- The critic must be at least as capable as the generator. In inference-only tests, a 7B critic lowers results for every generator size (average -14.14%), while a 32B critic gains 15.99% on average.
- Accuracy costs execution time. On LiveCodeBench the timeout rate is 16.61%, against 10.54% zero-shot and 8.93% with a GPT-4o critic. The authors read this as "more comprehensive" solutions without testing that reading.
- Gains are small or absent where the base is already strong. On MBPP+ with GPT-4o, the best case is 77.94% against 77.67% zero-shot.
- Training uses single-turn critique-revision only. The multi-turn gains are incidental, and multi-turn training is listed as future work, as are efficiency and safety.
- The method needs unit tests and a sandbox for training, so it is shown only on code.

## Limitations found by others

## What it leaves untried
- It does not train against a stronger generator. The critic is trained only on Qwen2.5-Coder-32B, and the "weak-to-strong" claim rests on transfer to GPT-4o (+4.84 points on CodeContests, +1.79 on LiveCodeBench, +0.27 on MBPP+ after five rounds). There is no comparison with training on the strong generator itself.
- Non-code domains with a verifier are untested. The JudgeBench result shows the verdict transfers, but the feedback quality outside code is not measured.
- It does not train a critic and generator together. The generator is frozen, so any gain from the generator learning to use critiques is left out.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - trained judges and reward models]]
