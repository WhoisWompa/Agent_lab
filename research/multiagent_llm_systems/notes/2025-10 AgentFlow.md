---
title: In-the-Flow Agentic System Optimization for Effective Planning and Tool Use
authors: Zhuofeng Li et al.
date: 2025-10
arxiv: 2510.05592
url: https://arxiv.org/abs/2510.05592
venue: ICLR 2026
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2510.05592.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "judges as reward signals"]
---
# In-the-Flow Agentic System Optimization for Effective Planning and Tool Use

## One line
AgentFlow trains only the planner of a four-module tool-using system with on-policy RL inside the live multi-turn loop, using one final-answer reward copied to every turn (Flow-GRPO), and a 7B backbone beats GPT-4o on ten benchmarks.

## Method
Two existing designs both fall short. A single monolithic tool-integrated RL policy reasons and calls tools under full context. The paper says its training grows unstable as horizons lengthen and tools multiply, and that it generalizes brittlely to new tasks or tools. Multi-module agentic systems (AutoGen, MetaGPT) decompose the work but are mostly training-free, so coordination is handcrafted. Where they are trained, it is offline (SFT or preference tuning on stored traces), detached from the live loop.

AgentFlow has four modules sharing an explicit memory. The planner picks a sub-goal, a tool and the context for it. The executor runs the tool. The verifier returns a binary "enough evidence?" signal. The generator writes the final answer once the verifier says stop or the turn budget runs out. The memory is a deterministic structured record updated by a fixed function, not a latent thought, so context growth is bounded and the state is inspectable. Only the planner is trained; the other three stay frozen Qwen2.5-7B-Instruct.

Flow-GRPO handles sparse, long-horizon credit assignment. The system is rolled out under the current policy, one 0/1 outcome reward is given to the whole trajectory, and that same reward is broadcast to every turn's planner action. Each turn then becomes an ordinary single-turn GRPO update, conditioned on the full memory state. Advantages are normalized within a group of rollouts of the same query, which cuts variance. The authors say they prove this multi-turn-to-single-turn equivalence and its convergence in an appendix (not in the body text). The reward comes from a GPT-4o judge rubric that checks semantic, numeric and option-level equivalence with the ground truth.

The bet is that training the planner on the exact states it meets at inference, including its own tool errors, beats imitating good traces offline.

## Evaluated on
- Beats the best baseline in each domain with a 7B backbone: average gains of 14.9% on search, 14.0% on agentic (GAIA), 14.5% on math and 4.1% on science, and it exceeds GPT-4o in every domain by 8.2 to 18.0 points.
- The training is what matters. Untrained AgentFlow averages 47.2 on search; with Flow-GRPO it reaches 57.3. On math the average goes from 31.7 to 51.5. Training lifted GAIA from 17.2 to 33.1.
- A frozen GPT-4o planner adds only 5.8% on average over the frozen 7B planner. Flow-GRPO adds 17.2%. Offline SFT on GPT-4o trajectories drops the average by 19.0%, which the authors attribute to token imitation misaligned with trajectory success.
- The planner learns to pick tools by task. On MedQA, Google Search calls fall from 66.2% to 10.9% while Wikipedia Search rises from 0 to 59.8%. On 2Wiki, Google Search use grows by 42.0%. The case study shows it escaping a repeated "variable not defined" error loop that the untrained system never left.
- Gains hold at 3B and 7B. Raising the turn cap from 3 to 10 improves all four tasks tested with no degenerate loops. Against the monolithic ToRL baseline on AIME24, validation accuracy keeps rising, while ToRL's stagnates and then declines.

## Limitations admitted by the authors
- The paper has no limitations section. The one caveat it states is that a stronger but static planner helps only modestly (5.8% from GPT-4o), so planner quality alone is not the lever.

## Limitations found by others

## What it leaves untried
- Training the executor, verifier or generator. Only the planner learns, so the verifier's binary stop signal (which ends the loop) stays a frozen 7B prompt. Its quality is never measured.
- Reward design beyond one 0/1 final answer. The paper says broadcasting avoids brittle heuristics but does not compare it with turn-level rewards inside this system. The reward also depends on a GPT-4o judge, and no check of that judge's errors is reported.
- Settings beyond a 7B backbone, short-answer reasoning tasks and five fixed tools. The scale evidence is 3B and 7B only. The claim of better generalization to new tools than monolithic policies is not tested with held-out tools.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - judges as reward signals]]
