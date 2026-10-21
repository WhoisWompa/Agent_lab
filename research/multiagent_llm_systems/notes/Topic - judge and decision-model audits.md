---
type: topic
group: Judging and evaluation
---
# Topic - judge and decision-model audits

Empirical studies of how judges or decision models behave: biases, adversarial cues, calibration measurement, probabilistic coherence, robustness, cost, failures inside agent loops, meta-evaluation benchmarks of judges. Measurement is the contribution.

Group: Judging and evaluation. See [[Topics]]. Same group: [[Topic - LLM and agent judges]], [[Topic - trained judges and reward models]], [[Topic - agent evaluation benchmarks]], [[Topic - user simulation]], [[Topic - alternative evaluation paradigms]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]], [[Topic - stopping rules]].

## Papers (8)
- [[2023-10 Can Large Language Models Really Improve by Self-critiquing Their Own Plans]] — Tests whether GPT-4 can verify its own plans in a generate-and-critique loop on Blocksworld planning, and finds its verifier accepts most invalid plans, so the loop gains little over a sound external checker. (also: [[Topic - self-refinement and critique loops]])
- [[2023-10 GPT-4 Doesn't Know It's Wrong]] — On graph coloring, GPT-4 self-critique loops do worse than a single answer, and the gains seen with an external verifier come from extra tries, not from the content of the feedback. (also: [[Topic - self-refinement and critique loops]])
- [[2023-11 LLMs cannot find reasoning errors, but can correct them given the error location]] — Splits self-correction into finding the mistake and fixing it, and shows that the finding step is the bottleneck: LLMs fix a reasoning step well when told where it is wrong, but cannot locate it themselves. (also: [[Topic - self-refinement and critique loops]], [[Topic - trained judges and reward models]])
- [[2024-02 On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks]] — GPT-4 critiquing its own answers makes results worse on Game of 24, graph coloring and planning, and the gains from an external sound verifier come mostly from having many guesses and a reliable check, not from the critique text. (also: [[Topic - self-refinement and critique loops]])
- [[2025-09 Peacemaker or Troublemaker]] — Defines and measures inter-agent sycophancy in multi-agent debate, then shows with persona-controlled agents that it drives debates to wrong consensus and that a mix of agreeable and contrarian debaters works best. (also: [[Topic - multi-agent debate and consensus]])
- [[2026-05 MUSE]] — MUSE splits an LLM's tendency to give in to user pushback into "pure sycophancy" (yielding while fully certain) and "uncertainty-driven conformity" (yielding more as the model's own uncertainty rises), by measuring the answer entropy before the pushback.
- [[2026-06 From Confident Closing to Silent Failure]] — Agents often claim a task is done when the environment state says it is not, LLM judges cannot catch this (AUROC at most 0.65), and a TF-IDF classifier catches it far better. (also: [[Topic - LLM and agent judges]], [[Topic - agent system failure analysis]])
- [[2026-08 Does a Tool Result Carry More Authority Than Plain Text]] — Three preregistered studies on one model ask whether an unsupported claim is adopted more often when it arrives as a native tool result than as plain text, and find the apparent tool-result advantage disappears once the text comparator is made active. (also: [[Topic - presentation sensitivity]], [[Topic - abstention and fallback]])
