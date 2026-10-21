---
type: topic
group: Judging and evaluation
---
# Topic - user simulation

Simulated users for multi-turn agent evaluation: building and steering them, measuring their fidelity to real users, benchmarks for simulators.

Group: Judging and evaluation. See [[Topics]]. Same group: [[Topic - LLM and agent judges]], [[Topic - judge and decision-model audits]], [[Topic - trained judges and reward models]], [[Topic - agent evaluation benchmarks]], [[Topic - alternative evaluation paradigms]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]], [[Topic - stopping rules]].

## Papers (18)
- [[2023-09 MINT]] — Evaluates multi-turn problem solving with code execution and GPT-4-simulated natural-language feedback. (also: [[Topic - agent evaluation benchmarks]])
- [[2024-03 The misleading success of simulating social interactions with LLMs]] — Shows omniscient single-LLM simulation of both sides succeeds far more than non-omniscient agent-agent interaction, so simulation-based social evaluation overestimates ability. (also: [[Topic - agent evaluation benchmarks]])
- [[2024-06 tau-bench]] — Customer-service agent (retail, airline) talks to an LLM-simulated user and calls APIs under a policy; graded by comparing final database state to the goal state, with pass^k for reliability. (also: [[Topic - agent evaluation benchmarks]])
- [[2025-01 IntellAgent]] — Generates synthetic, policy-grounded multi-turn scenarios from a policy graph and runs simulated users against a conversational agent, with a critic grading. (also: [[Topic - agent evaluation benchmarks]], [[Topic - self-evolving tests]])
- [[2025-05 LLMs get lost in multi-turn conversation]] — Sharded simulation of underspecified multi-turn instructions shows average performance drops of about 39% vs single-turn, mainly from unreliability (as recalled). (also: [[Topic - presentation sensitivity]])
- [[2025-05 Sentient Agent as a Judge]] — Simulated human-like agent with an emotional state converses with the tested model and judges its social cognition - a judge that interacts with the model under test. (also: [[Topic - LLM and agent judges]])
- [[2025-06 tau2-bench]] — Extends tau-bench with a telecom domain where the user also has tools and acts on a shared state, plus a compositional task generator. (also: [[Topic - agent evaluation benchmarks]])
- [[2025-07 UserBench]] — Gym where simulated users reveal underspecified, evolving preferences gradually; agents must elicit them while using tools (travel planning). (also: [[Topic - agent evaluation benchmarks]])
- [[2025-08 Agent-Testing Agent]] — A meta-agent that reads a target conversational agent's code, interviews its designer, mines literature, then runs persona-driven adversarial dialogues whose difficulty adapts to judge feedback to hunt the target's weakest capabilities. (also: [[Topic - self-evolving tests]])
- [[2025-10 SimulatorArena]] — A benchmark of 909 real human-LLM conversations that scores LLM user simulators on how human their messages look and whether their assistant ratings match real users', and shows that a user profile lifts that match from about 0.6 to 0.7-0.77 Spearman. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-01 Lost in Simulation]] — User study (US, India, Kenya, Nigeria) on tau-bench retail showing simulated users are unstable and miscalibrated proxies. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-03 Mind the Sim2Real Gap in User Simulation]] — Runs the tau-bench protocol with 451 real people and 31 LLM user simulators and defines a User-Sim Index of simulator realism. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-06 Simulated Customers Never Walk Away]] — Measures whether LLM user simulators decide like real customers; notes tau-bench's simulator is built to always reach its goal and cannot decline. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-06 VISTA]] — A user-simulation toolkit that tests customer-facing agents with a simulated user who can both click through the real web UI and call user-side APIs, plus six metrics that score how realistic and how thorough the simulated conversations were. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-07 Enjoy Your Talk EYT-Bench]] — A multi-turn chat benchmark that splits user simulator, target model and LLM judge into separate roles, and adds trajectory metrics (intent drift, final-intent completion) next to rubric scores for empathy, persona fit and human-likeness. (also: [[Topic - LLM and agent judges]])
- [[2026-09 GAUGE]] — Offline protocol checking whether judge rankings of 25 agents in user-simulated conversations (tau2-bench, SimulatorArena) track grounded task success. (also: [[Topic - judge and decision-model audits]])
- [[2026-09 UserProxyBench]] — Scores the simulated user (User Fidelity Score, rubric-based) separately from agent success on tau-bench-family tasks. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-10 CUEing User Simulators]] — Steers any LLM to play a benchmark user from a continuous user embedding decoded into persona commands, and argues simulators should be judged by whether agents fail with them as they do with real users. (also: [[Topic - agent evaluation benchmarks]])
