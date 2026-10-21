---
title: "Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling"
authors: Tong Zhu et al.
date: 2026-10
arxiv: 2610.22131
url: https://arxiv.org/abs/2610.22131
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Intern-Decision - Efficient Multimodal Decision Making with Autoregressive Masked LM (Zhu 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling

## One line
A family of 0.8B/2B/4B multimodal Jev-style decision models that answer several typed questions (choice, yes/no, score) over text and images in one causal forward pass, returning labels plus candidate probabilities instead of generated text.

## Method
The problem: agents keep making closed-set decisions (which tool, which action, which label) but get them by generating free text, which costs decoding time and needs parsing. Existing System-1 decision models (Jev and its open clones) are text-only.

The idea is "autoregressive masked language modeling". The request (state, optional images, ordered questions with ordered options) goes in the user turn, then an assistant JSON skeleton is appended with one `<decision>` placeholder per field. Each option is mapped to a single-token symbol (A, B, C...; Boolean is A=no, B=yes). The model reads the native LM-head logits at the position just before each placeholder, so supervision is the ordinary next-token shift: the correct symbol is the target at that position and is never inserted into the input. Only those positions are trained. At inference, logits are restricted to the legal symbols for each field and softmaxed with a fitted temperature T, which changes spread but not the argmax.

Why it should work: it keeps the pretrained causal backbone and LM head intact (Qwen3.5, vision tower and projector frozen), so the model's existing token knowledge does the scoring; all fields share one pass; and output is schema-valid by construction because nothing is decoded.

## Evaluated on
- Higher average accuracy than the text-only open and hosted baselines: 4B gets 90.02% unweighted mean over seven suites vs 88.74% for Jev, leading or tying on five of seven. Jev still wins WildJailBreak (96.29 vs 89.86), and the 4B ties JevK5 on Jevbench-Hard at 73.87%.
- Faster than Jev on a short request: 44.16 ms mean for the 4B on a 289-token, three-field request on one RTX 4090, vs 109.70 ms for Jev (2.48x); 0.8B and 2B are about 33-34 ms.
- Temperature scaling repairs calibration without touching accuracy: on Hard, ECE drops from 0.133 to 0.065 with 82/111 correct unchanged; 4B Hard Brier 0.347 is the lowest, though JevK5 has the lowest ECE (0.047).
- Better full distributions on exact-probability puzzles: on a 96-case pilot, calibrated 4B pooled Brier/ECE is 0.550/0.089 vs 0.595/0.130 for Jev; uncalibrated 4B (0.628/0.213) was worse than Jev.
- Confidence handoff recovers most of a big model's accuracy: routing 42/111 Hard items to Atria-Dawn-Preview gives 87.39% vs 73.87% local and 89.19% Atria-only, at an estimated 53% less time than Atria-only.

## Limitations admitted by the authors
- No ablations: without matched-data experiments, neither the gain from joint field scoring nor the 79.38% to 90.02% climb across sizes can be attributed to the method or to parameter count.
- Public Jevbench informed development, so the three Jevbench suites are a diagnostic, not held-out evidence; the synthetic training data also follows Jevbench ability types.
- Calibration comparison is uneven: Intern-Decision temperatures were fitted, baselines used default settings, so the Brier/ECE lead is partly a tuning advantage.
- The 96-case pilot is really 48 paired settings (each in two option orders), and temperature scaling does not help every case: on Monty Hall the uncalibrated output was closer to the reference.
- Latency is one fixed short text request; Jev's serving and transport conditions are undocumented, so the 2.48x ratio is not a controlled speedup.
- Handoff time is estimated, not measured, and one operating point is reported, not an optimized policy.
- Game, CAPTCHA and browser demonstrations are selected successful trajectories with no episode counts, returns or baselines.
- Fields see different causal prefixes, so no permutation invariance or cross-field consistency is guaranteed.

## Limitations found by others

## What it leaves untried
- A matched-data ablation of joint one-pass scoring vs field-by-field scoring, the central architectural claim.
- A quantitative multimodal benchmark: the visual contribution is the paper's distinguishing feature, yet every image-based result is qualitative.
- Testing field-order sensitivity: since later fields attend to earlier placeholders, permuting fields could change answers, and the paper never measures by how much.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
