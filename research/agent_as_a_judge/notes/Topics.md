---
type: topic-index
---
# Topics

Every topic in `research/topics.md`, with how many notes carry it. 384 notes in all.

## Judging and evaluation
- [[Topic - LLM and agent judges]] (121) — Using an LLM or an agent to evaluate agents or model outputs. Judge designs and prompting, agentic judges that inspect trajectories or run code, reference-based and reference-free judging, methods that make a judge more accurate or less biased. The paper's subject is the judge or the act of judging.
- [[Topic - judge and decision-model audits]] (113) — Empirical studies of how judges or decision models behave: biases, adversarial cues, calibration measurement, probabilistic coherence, robustness, cost, failures inside agent loops, meta-evaluation benchmarks of judges. Measurement is the contribution.
- [[Topic - trained judges and reward models]] (62) — Fine-tuned judges, reward models, process reward models, critics, reasoning judges, small-encoder judges, and how they are trained.
- [[Topic - agent evaluation benchmarks]] (66) — Benchmarks and harnesses for agents: task suites, environments, trajectory and step-level scoring, verifier failures, deployment-aware evaluation.
- [[Topic - user simulation]] (18) — Simulated users for multi-turn agent evaluation: building and steering them, measuring their fidelity to real users, benchmarks for simulators.
- [[Topic - alternative evaluation paradigms]] (70) — Debate, arenas and pairwise tournaments, consistency checks, execution-based verification, cross-examination, judge-the-judge. Ways to evaluate that are not a single judge scoring an output.
- [[Topic - self-evolving tests]] (57) — Generated or adversarial test sets, self-improving judges, evaluator loops that refine their own tests from where they missed.
- [[Topic - judges as reward signals]] (28) — Using a judge, verifier, rubric or other automatic check as the reward that trains a policy (RLVR, RLAIF, judge-in-the-loop), and what that reward does to the policy: what it learns, reward hacking, spurious or noisy rewards, whether the reward is what drives the gain. The subject is the training signal and its effect, not the judge's own accuracy.
- [[Topic - stopping rules]] (8) — When to stop sampling, testing or evaluating: sequential tests (SPRT, group sequential), adaptive testing, Bayesian optimal stopping, sample-size reduction with valid error control. A confidence gate that routes cases to a bigger model is not a stopping rule unless framed as sequential testing.

## Decision models
- [[Topic - decision models]] (67) — Typed, System One, single-pass decision models (Jev and its kin: Laya, Kev, Clef, Decider, Bongard): architecture, theory, interface, properties, and their use inside agents or pipelines. Any paper whose subject is such a model.
- [[Topic - open decision models]] (37) — Building, training, distilling, adapting, reproducing or releasing an open-weight decision model, or a recipe for getting one from an existing LLM or encoder. The contribution includes a model or a recipe, not only measurements of a hosted one.

## Mechanisms
- [[Topic - confidence-gated escalation]] (13) — A cheap model or judge answers first and its low-confidence cases go to a stronger model, a judge or a human. Cascades, deferral, how the threshold is chosen, whether it transfers to new data, whether the stages make the same errors.
- [[Topic - calibration]] (31) — Making reported probabilities mean what they say: proper-scoring-rule training (Brier, log score), post-hoc recalibration (temperature, Platt, isotonic), probabilistic coherence, and when a fix transfers.
- [[Topic - presentation sensitivity]] (36) — Decisions that change with option order, option names or labels, the set of listed options, question form or request serialisation, though the content is logically the same; and methods that remove the sensitivity.
- [[Topic - abstention and fallback]] (7) — None-of-the-above, defer, other, ask a clarifying question, null gates: whether a model can decline to pick from the menu, and how reliably.
- [[Topic - adaptive reasoning depth]] (6) — Spending extra compute (looping, partial chain of thought, handing off to a slow reasoner) only on inputs where the fast decision is unsure, and how the switch is decided.
- [[Topic - reasoning prompting]] (1) — Prompt-level techniques that elicit better single-model reasoning: chain-of-thought triggers, plan-then-solve, decomposition prompts, self-consistency voting, program-of-thought. The subject is the prompt wording and the reasoning text it produces, not a multi-agent structure or a critique loop.

## Game theory
- [[Topic - contract theory]] (0) — Hidden action and hidden type: principal-agent models, moral hazard, adverse selection, multi-agent contracting, relational and incomplete contracts, algorithmic contract design, principal-agent with a learning agent.
- [[Topic - cooperative game theory]] (0) — Coalitions and credit assignment: core, Shapley value, nucleolus, coalition formation, hedonic games, cost sharing.
- [[Topic - information design]] (0) — Controlling what agents know: Bayesian persuasion, information disclosure, Bayes correlated equilibrium, multi-receiver design, algorithmic persuasion.
- [[Topic - inverse reinforcement learning]] (0) — Recovering a reward function from observed behaviour or corrections: maximum-entropy IRL, cooperative IRL, assistance games.
- [[Topic - mechanism design]] (0) — Controlling what agents are paid: revelation principle, incentive compatibility, VCG, auctions, implementation theory, mechanism design without money, dynamic and robust mechanism design.
- [[Topic - preference learning]] (21) — Learning what a person wants from binary or pairwise feedback: Bradley-Terry models, RLHF-style reward models, active preference elicitation.
- [[Topic - social choice]] (17) — Aggregating outputs, votes, rankings and judge scores from several agents: Arrow, Gibbard-Satterthwaite, voting rules, judgment aggregation, fair division, computational social choice.
- [[Topic - stackelberg games]] (1) — Leader commits, follower best-responds: the orchestrator-worker relationship, Stackelberg equilibrium, security games, commitment computation.
- [[Topic - team theory and distributed decision making]] (1) — Agents that share an objective but not information: common-payoff games, Dec-POMDPs, information structures, consensus and coordination, decentralised control, credit assignment.

## Agent systems
- [[Topic - self-refinement and critique loops]] (2) — A model critiques and revises its own output, or is critiqued by a second model, over one or more rounds (Self-Refine, Reflexion, RCI, generator-critic loops). The subject is what the loop changes, when it helps or hurts, and what stops it. The critique is a step in producing the answer, not a judgment of someone else's output.
- [[Topic - orchestration and delegation]] (0) — A controller LLM decomposes a request, routes sub-tasks to tools, models or sub-agents, and composes their outputs: planner-executor, orchestrator-worker, hierarchical delegation, hand-offs. The subject is the architecture: planning, selection, what the controller sees of the workers' results and how it accepts them.
- [[Topic - role-based agent teams]] (0) — Two or more LLM agents given complementary roles (instructor and assistant, analyst, coder and tester, a software company) work through a task by turn-taking dialogue or a fixed workflow. The subject is how role assignment, standard procedures, what each role sees and the termination rule keep the team on task, including role flipping, loops, hollow completion and drift.
- [[Topic - strategic play among LLM agents]] (0) — LLM agents in games with hidden information, hidden roles, or opposed or partly aligned goals: negotiation and bargaining, social deduction, cheap talk between agents, and the trust, deception and coordination that emerge in play. The subject is how the agents play and what the communication channel does, not a shared-task team.
- [[Topic - multi-agent debate and consensus]] (6) — Several LLM agents, often from different models, exchange answers and explanations over rounds, revise their positions after seeing each other's, and settle on a team answer by vote, judge or convergence. The subject is what the exchange adds over one model or a plain ensemble: agent diversity, conformity and echo chambers, convergence, and when rounds stop helping. Debate as a way of producing an answer, not as a way of evaluating one.
- [[Topic - automated pipeline and topology search]] (0) — Searching for or learning the prompts, demonstrations, workflow, agent roles or communication graph of an LM pipeline or multi-agent system against a metric, instead of hand-writing them: compiled prompt programs, bootstrapped demonstrations, workflow search, learned or pruned agent topologies. The subject is the optimizer and what it finds, not the wording of any one prompt.
- [[Topic - communication topology and channels]] (0) — How the shape and size of the communication structure among LLM agents (chain, tree, star, mesh, layered, random, agent count) and what passes over an edge (text, summaries, artifacts only, embeddings or hidden states, protocol envelopes) determine task quality, cost and context load, including scaling in the number of agents. The subject is the structure and the channel, not the roles in it and not a search for it.
- [[Topic - agent system failure analysis]] (2) — Empirical studies of how LLM agents and multi-agent systems fail in operation or in traces: failure taxonomies built from incidents or runs, silent and plausible-looking failures, how failures are discovered, and the defences that follow. The subject is the failure record and what it implies for building the system, not a benchmark score or a judge's accuracy.
