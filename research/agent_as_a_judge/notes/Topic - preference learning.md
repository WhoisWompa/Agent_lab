---
type: topic
group: Game theory
---
# Topic - preference learning

Learning what a person wants from binary or pairwise feedback: Bradley-Terry models, RLHF-style reward models, active preference elicitation.

Group: Game theory. See [[Topics]]. Same group: [[Topic - contract theory]], [[Topic - cooperative game theory]], [[Topic - information design]], [[Topic - inverse reinforcement learning]], [[Topic - mechanism design]], [[Topic - social choice]], [[Topic - stackelberg games]], [[Topic - team theory and distributed decision making]].

## Papers (21)
- [[2022-10 Scaling Laws for Reward Model Overoptimization]] — Synthetic 'gold RM' setup measuring how true reward first rises then falls as a policy optimises a proxy RM, with smooth scaling laws in RM size. (also: [[Topic - trained judges and reward models]], [[Topic - judges as reward signals]])
- [[2023-05 AlpacaFarm]] — Simulates human feedback with LLM annotators (50x cheaper) and introduced the auto-evaluation that became AlpacaEval. (also: [[Topic - LLM and agent judges]])
- [[2023-10 A Long Way to Go Length Correlations in RLHF]] — Finds much of RLHF's reward improvement is explained by response length, and RMs learn length as a shortcut. (also: [[Topic - trained judges and reward models]], [[Topic - judge and decision-model audits]], [[Topic - judges as reward signals]])
- [[2023-10 Reward Model Ensembles Help Mitigate Overoptimization]] — Uses Gao et al.'s gold-RM setup to show worst-case and uncertainty-weighted RM ensembles reduce overoptimization in BoN and PPO. (also: [[Topic - trained judges and reward models]], [[Topic - judges as reward signals]])
- [[2024-01 Self-Rewarding Language Models]] — One model acts as both policy and LLM-as-a-judge of its own outputs, and iterative DPO on self-judged pairs improves both roles. (also: [[Topic - trained judges and reward models]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]])
- [[2024-02 ODIN Disentangled Reward Mitigates Hacking]] — Trains a two-head RM separating length from content quality to reduce length hacking. (also: [[Topic - trained judges and reward models]], [[Topic - judges as reward signals]])
- [[2024-02 Self-alignment for factuality]] — Uses the model's own self-evaluation (Self-Eval, with calibration) as the reward signal for DPO to reduce hallucinations; closest match found for the brief's 'Self-Alignment via consistency'. (also: [[Topic - LLM and agent judges]], [[Topic - calibration]], [[Topic - judges as reward signals]])
- [[2024-03 Chatbot Arena]] — Crowdsourced pairwise blind battles between anonymous models, ranked with Bradley-Terry, as a live leaderboard of human preference. (also: [[Topic - alternative evaluation paradigms]], [[Topic - social choice]])
- [[2024-03 RewardBench]] — First standard RM benchmark (Chat, Chat-Hard, Safety, Reasoning) with a public leaderboard. (also: [[Topic - trained judges and reward models]], [[Topic - judge and decision-model audits]])
- [[2024-06 CriticGPT LLM Critics Help Catch LLM Bugs]] — RLHF-trained GPT-4 critic that writes code-review critiques of ChatGPT code; catches more bugs than paid contractors but also hallucinates bugs. (also: [[Topic - trained judges and reward models]], [[Topic - LLM and agent judges]])
- [[2024-06 Scaling Laws for RM Overoptimization in Direct Alignment]] — Shows DPO/IPO-style methods also overoptimize, with hump-shaped quality vs KL curves like explicit RMs. (also: [[Topic - trained judges and reward models]], [[Topic - judges as reward signals]])
- [[2024-07 Meta-Rewarding Language Models]] — Adds a meta-judge role that judges the model's own judgments, so the judge skill is trained too, not only the policy. (also: [[Topic - trained judges and reward models]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]])
- [[2024-08 Critique-out-Loud Reward Models]] — Reward model first generates a natural-language critique, then a reward head scores the response conditioned on that critique. (also: [[Topic - trained judges and reward models]])
- [[2024-09 Language Models Learn to Mislead Humans via RLHF]] — Shows RLHF makes models better at convincing human evaluators of wrong answers (U-SOPHISTRY), increasing human false-positive rates on QA and code. (also: [[Topic - judge and decision-model audits]], [[Topic - judges as reward signals]])
- [[2024-10 Skywork-Reward]] — Scalar RMs on an 80K curated preference set that topped RewardBench in late 2024. (also: [[Topic - trained judges and reward models]])
- [[2025-02 Agentic Reward Modeling]] — RewardAgent: base RM combined with verification agents for factuality (search) and instruction constraints (code checks). (also: [[Topic - trained judges and reward models]], [[Topic - LLM and agent judges]])
- [[2025-07 Skywork-Reward-V2]] — Scalar Bradley-Terry RMs (0.6B-8B) trained on 26M pairs curated from a 40M-pair pool by a human-verified then LLM-scaled curation pipeline; top of RewardBench 2. (also: [[Topic - trained judges and reward models]])
- [[2025-08 Dropping just a handful of preferences can change top LLM rankings]] — Data-dropping sensitivity analysis shows Bradley-Terry Arena-style rankings at the top can flip by removing a tiny fraction of votes. (also: [[Topic - alternative evaluation paradigms]])
- [[2026-02 Outcome Accuracy is Not Enough Rationale Consistency]] — Shows GenRMs/LLM judges trained on outcome accuracy reach right verdicts for wrong reasons, and trains with a hybrid rationale-consistency + outcome reward. (also: [[Topic - trained judges and reward models]])
- [[2026-05 PReMISE]] — Audits and repairs judge rubrics using pairwise human preference data (known only via a citing paper; abstract not read). (also: [[Topic - LLM and agent judges]])
- [[2026-10 From Probabilities to Decisions]] — Distils the pairwise probabilities of a probability-only judge (Jev), alone or averaged with an LLM judge (Qwen3-32B), into a small evaluator that a search engine or reranker uses without any live judge calls, and asks when a second judge is worth its share of the labelling budget. (also: [[Topic - decision models]], [[Topic - social choice]])
