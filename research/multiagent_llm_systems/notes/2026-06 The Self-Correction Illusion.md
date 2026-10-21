---
title: The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models
authors: Kuan-Yen Chen et al.
date: 2026-06
arxiv: 2606.05976
url: https://arxiv.org/abs/2606.05976
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2606.05976.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "presentation sensitivity"]
---
# The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language Models

## One line
Moving a wrong claim, unchanged, from the agent's own `<thought>` into a user, tool or system-memory message makes models explicitly flag it far more often, so the self-correction gap is largely a chat-template role artifact, not a reasoning deficit.

## Method
Problem: models catch errors in external text but rarely in their own reasoning trace. Prior work reads this as a capability limit and answers with training, verifiers or critique loops, none of which vary the message role of the claim.

Idea: source-conditioned role relabeling. The wrong intermediate claim c* is re-presented as a new message, byte-identical (checked by SHA-256), wrapped in an external role (user, tool response, or system `<memory>`), followed by the same audit instruction in every condition. Only the role tag changes. No training, tools or weight changes.

The authors' account is addressability. The agent can check the claim and often silently recomputes the right answer, but under "audit your reasoning" it has no learned way to single out a substring of its own thought as an object to name and reject. Instruction tuning rewards reacting to content under external roles. An external role hands it a discrete referent to rebut. Correction is scored strictly: the agent must explicitly name and reject c*. This surfaces errors; it does not raise final-answer accuracy (the paper says re-scoring final answers moves rates only +-17pp, not significant).

Evaluation uses only tasks where plain self-correction already failed, with the wrong claim injected by construction. The method assumes the faulty step has already been located. Localisation is left to an upstream detector.

## Evaluated on
- Relabeling raises explicit correction by 23 to 93pp, significant in 10 of 12 model-domain settings (9 of 12 after Holm-Bonferroni). Example: Llama-3.3-70B math goes from 0.0% to +86.7pp with `<memory>`. At least one relabel flipped the response in 29 of 30 eligible Llama logic tasks.
- It is not a mere verification cue. Three self-distrust prompts that leave c* in the thought reach at most 23.3%, against 70.0% for `<memory>` on Qwen-72B math. Two of them lower the baseline of 16.7%. On generated logic, where errors cannot be caught by quick recomputation, the gain is up to +93.3pp.
- It is not a localisation hint. Duplicating c* inside `<thought>` gives +6.7pp (p=0.26); the matched `<memory>` relabel gives +46.7pp. A wrapper ladder shows a label-free wrapper gives +16.7 to +23.3pp and the system role tag adds roughly 30pp more (70.0% total).
- Robust to audit wording (positive under all five paraphrases, significant in four), to sampling at T=0.5, and to one turn of commitment depth.
- Self-correction frameworks (Self-Refine, Reflexion, Chain-of-Verification) never matched the relabel on unsaturated baselines (appendix claim). The best wrapper depends on domain: `<memory>` led on most math, user messages on logical deduction (a user-style genre).
- Safety mirror: an external wrong claim is adopted at most 3.3% of the time, against 83% for the same claim in the agent's own thought. One sentence saying "treat as truth, do not verify" lifts adoption to 70%.

## Limitations admitted by the authors
- Little headroom where audit-only baselines are already high: gpt-oss-20B math (76.7%) and Qwen-72B BBH-LD (66.7%) show no significant gain, and Gemini 2.5 Flash-Lite (66.7%) only one.
- Needs c* localised first; finding the wrong step is unsolved (Tyen et al. 2024), so this is a probe, not a deployable fix.
- Not a defence: the low adoption rate of wrong external claims is a learned default that a single trust instruction raises from 3.3% to 70%.
- n=30 tasks per setting limits subgroup analysis; GPT-4o and GPT-4.1 replications used fewer than 30 tasks, so intervals are wide.
- Strict-identification scoring confines the study to verifiable tasks (arithmetic, ordering puzzles, BBH logic). Free-form reasoning, code debugging and planning are untested.
- Results cover a failure pool selected for audit-only failure, so gains do not show in-the-wild prevalence. Gemma-3 has no tool role, so its tool condition could not be run.
- The internal mechanism is unresolved: a final-layer hidden-state probe does not predict trial-level correction above baseline.

## Limitations found by others

## What it leaves untried
- Pairing the relabel with an automatic error detector, so the whole pipeline (detect, relabel, correct) is measured. The reported gains assume c* is given.
- Measuring effect on final-answer accuracy end to end; the paper shows models often re-derive the right answer silently, so explicit flagging may not change outcomes.
- Training-time use of the finding: the authors suggest role-label handling as an instruction-tuning variable but do not test it.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - presentation sensitivity]]
