---
type: topic
group: Game theory
---
# Topic - social choice

Aggregating outputs, votes, rankings and judge scores from several agents: Arrow, Gibbard-Satterthwaite, voting rules, judgment aggregation, fair division, computational social choice.

Group: Game theory. See [[Topics]]. Same group: [[Topic - contract theory]], [[Topic - cooperative game theory]], [[Topic - information design]], [[Topic - inverse reinforcement learning]], [[Topic - mechanism design]], [[Topic - preference learning]], [[Topic - stackelberg games]], [[Topic - team theory and distributed decision making]].

## Papers (17)
- [[2022-02 Jury learning]] — Models individual annotators and lets practitioners specify a 'jury' composition whose simulated verdict replaces a single majority label.
- [[2022-03 Self-consistency improves chain of thought reasoning]] — Sample many reasoning paths and take the majority answer; agreement rate doubles as a confidence signal. (also: [[Topic - alternative evaluation paradigms]])
- [[2023-08 ChatEval]] — Multi-agent referee team: several LLM agents with different personas debate the quality of a response before giving a verdict. (also: [[Topic - LLM and agent judges]], [[Topic - alternative evaluation paradigms]])
- [[2023-11 Should we be going MAD]] — Benchmarks multi-agent debate strategies and finds they do not reliably beat self-consistency or ensembling at matched cost, and are sensitive to hyperparameters. (also: [[Topic - alternative evaluation paradigms]])
- [[2024-01 PRE peer review evaluation]] — Peer-review evaluation: candidate LLMs act as reviewers after passing a qualification exam, and their weighted reviews rank all models. (also: [[Topic - LLM and agent judges]], [[Topic - alternative evaluation paradigms]])
- [[2024-02 PiCO peer review consistency optimization]] — Unsupervised peer evaluation: models answer unlabeled questions and score each other; per-model capability weights are optimised so stronger models' votes count more. (also: [[Topic - alternative evaluation paradigms]], [[Topic - LLM and agent judges]])
- [[2024-03 Chatbot Arena]] — Crowdsourced pairwise blind battles between anonymous models, ranked with Bradley-Terry, as a live leaderboard of human preference. (also: [[Topic - alternative evaluation paradigms]], [[Topic - preference learning]])
- [[2024-04 Replacing judges with juries PoLL]] — Panel of LLM evaluators (PoLL) from disjoint model families, aggregated by voting, beats a single large judge and is over seven times cheaper. (also: [[Topic - LLM and agent judges]], [[Topic - alternative evaluation paradigms]])
- [[2024-05 Auto-Arena]] — Fully LLM-driven arena: an examiner LLM writes questions, two candidate LLMs battle over multiple rounds, and a committee of LLM judges discusses and votes. (also: [[Topic - alternative evaluation paradigms]], [[Topic - LLM and agent judges]])
- [[2024-06 Language model council]] — A council of 20 LLMs writes test prompts, answers them and judges one another, producing rankings that match humans better than any single judge on emotional-intelligence dilemmas. (also: [[Topic - alternative evaluation paradigms]], [[Topic - LLM and agent judges]])
- [[2025-01 Exploring and mitigating adversarial manipulation of voting-based leaderboards]] — Shows an attacker can identify which model wrote a reply with >95% accuracy and then vote to move a target model on Chatbot Arena; worked with Arena on mitigations. (also: [[Topic - alternative evaluation paradigms]])
- [[2025-01 Improving your model ranking on Chatbot Arena by vote rigging]] — Omnipresent vote-rigging strategies that vote on battles not involving the target model can lift its rank with a few hundred new votes. (also: [[Topic - alternative evaluation paradigms]])
- [[2025-08 Debate or vote]] — Decomposes multi-agent debate into majority voting and inter-agent debate and shows voting accounts for most of the reported gains. (also: [[Topic - alternative evaluation paradigms]])
- [[2025-08 Overconfidence in LLM-as-a-Judge]] — Shows that pairwise LLM judges state far more confidence than their accuracy earns, proposes TH-Score to measure calibration only in the high- and low-confidence bands where routing decisions are made, and proposes LLM-as-a-Fuser, where one LLM reads several judges' verdicts and rationales and issues a final verdict with a confidence. (also: [[Topic - calibration]], [[Topic - judge and decision-model audits]], [[Topic - LLM and agent judges]])
- [[2026-06 Minority sentinel]] — Argues an LLM judge reading debate logs shares the debaters' blind spots; reports an LLM judge gave negative net gain versus no intervention (from search snippet). (also: [[Topic - alternative evaluation paradigms]])
- [[2026-10 From Probabilities to Decisions]] — Distils the pairwise probabilities of a probability-only judge (Jev), alone or averaged with an LLM judge (Qwen3-32B), into a small evaluator that a search engine or reranker uses without any live judge calls, and asks when a second judge is worth its share of the labelling budget. (also: [[Topic - decision models]], [[Topic - preference learning]])
- [[2026-10 Judging the Judges Rubrics as Rewards]] — RaRE ensembles five rubric judges with logprob-weighted soft-Likert rewards and drops high-disagreement rollouts from GRPO updates. (also: [[Topic - judges as reward signals]], [[Topic - LLM and agent judges]])
