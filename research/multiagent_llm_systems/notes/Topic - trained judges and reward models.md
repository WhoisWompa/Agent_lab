---
type: topic
group: Judging and evaluation
---
# Topic - trained judges and reward models

Fine-tuned judges, reward models, process reward models, critics, reasoning judges, small-encoder judges, and how they are trained.

Group: Judging and evaluation. See [[Topics]]. Same group: [[Topic - LLM and agent judges]], [[Topic - judge and decision-model audits]], [[Topic - agent evaluation benchmarks]], [[Topic - user simulation]], [[Topic - alternative evaluation paradigms]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]], [[Topic - stopping rules]].

## Papers (6)
- [[2022-12 Constitutional AI]] — Trains a harmless but non-evasive assistant with no human harmlessness labels, using a short list of written principles that a model applies to critique its own answers and to judge answer pairs, then distilling those judgments into a reward for RL. (also: [[Topic - judges as reward signals]], [[Topic - LLM and agent judges]], [[Topic - self-refinement and critique loops]])
- [[2023-11 LLMs cannot find reasoning errors, but can correct them given the error location]] — Splits self-correction into finding the mistake and fixing it, and shows that the finding step is the bottleneck: LLMs fix a reasoning step well when told where it is wrong, but cannot locate it themselves. (also: [[Topic - self-refinement and critique loops]], [[Topic - judge and decision-model audits]])
- [[2024-04 Small Language Models Need Strong Verifiers to Self-Correct Reasoning]] — SCORE has a 7B to 13B model write its own critique-correction training data and fine-tune on it, and the paper finds the gain depends on a strong verifier (GPT-4 or oracle labels), not on the refiner. (also: [[Topic - self-refinement and critique loops]])
- [[2024-08 Critic-CoT]] — Fine-tunes one LLM to critique its own solutions step by step in chain-of-thought and to repair them from the first wrong step, using training data labelled only by whether the final answer is right. (also: [[Topic - self-refinement and critique loops]])
- [[2025-02 Self-rewarding correction for mathematical reasoning]] — Trains one LLM to solve a math problem, judge its own answer with a "[VERIFY] correct/wrong" token, and revise only when it judged itself wrong, so no external reward model is needed at inference. (also: [[Topic - self-refinement and critique loops]], [[Topic - judges as reward signals]])
- [[2025-02 Teaching Language Models to Critique via Reinforcement Learning]] — CTRL trains a separate critic LLM with reinforcement learning to write feedback that makes a fixed, black-box generator's revised code pass more tests, with no human critique labels. (also: [[Topic - self-refinement and critique loops]])
