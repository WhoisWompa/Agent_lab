---
title: "Verdict: Encode Once, Decide Many"
authors: Avdhesh Singh Chouhan et al.
date: 2026-10
arxiv: 2610.20778
url: https://arxiv.org/abs/2610.20778
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/Verdict - Encode Once, Decide Many (Chouhan 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "presentation sensitivity"]
---
# Verdict: Encode Once, Decide Many

## One line
An open ModernBERT encoder (Verdict-MQ) that reads one piece of state once and returns a distribution for every typed question about it, with option-order and question-grouping invariance built into the attention mask.

## Method
- **Problem.** Automation asks several typed questions about one state (an email, an invoice, an agent trace), each needing a probability good enough to auto-act on. Decision models like Laya re-encode the state once per question.
- **Idea.** Pack the state and all question blocks (instructions plus options with criterion text, each option opened by a marker token) into one pass. One attention mask enforces four rules:
  1. The state sees only itself, so it is question-independent and cacheable.
  2. Each question block sees the state and itself, starting at the same position, so other questions cannot change its answer.
  3. Options see the state, their question and themselves, never each other.
  4. All options share position ids, so reordering them only reorders the outputs.
  Each marker's hidden state goes through an MLP to a logit, then a softmax over the options. Training uses soft labels.
- **Why it works.** The invariances hold by construction, not by training. A packed answer equals a single-question answer whenever truncation keeps the same state tokens. K passes become one.
- **A failure mode it found.** If options attend to each other, the identical markers collapse into one representation. The model then outputs uniform distributions and still passes invariance tests.
- **Split depth k.** Optionally, the top k layers give each question its own copy of the state, trading speed for accuracy.
- The claimed novelty is packing several questions per pass and measuring what sharing costs. The invariance mechanism itself predates the paper (Set-LLM, UniMC).

## Evaluated on
- **Fits soft labels better than Laya's 421M specialist.** KL 0.080 vs 0.117 and Brier 0.045 vs 0.061, with p ≤ 0.0002 on all five seeds. It survives temperature fitting (KL 0.074–0.077 vs 0.105).
- **Accuracy 0.801 vs 0.767, past the benchmark's ~0.75 saturation point.** The authors read this as closer agreement with the labelling teacher, not as better decisions.
- **Automates more at a fixed target.** At 90% it auto-handles 62–71% of decisions vs Laya's 56%, with 32–39% lower AURC. Raw ECE is worse (0.156), so the gain is in ranking, not calibration.
- **Faster.** 2.7–2.8× faster per case than one pass per question at batch 8.
- **Sharing has a small cost.** Per-question state copies gain 0.9–3.5 points on RACE and MultiRC at 1.4–2.5× the latency, and nothing on typed decisions (0.804 vs 0.801, p = 0.24).
- **Mixed against a matched fine-tuned baseline.** Wins on MultiRC (80.6 vs 71.6), loses on RACE (77.4 vs 78.9) and BoolQ (76.2 vs 81.0). Zero-shot closed Jev beats all (90–93%).

## Limitations admitted by the authors
- **The gain is the initialization, not the architecture.** From Laya's own encoder the two architectures tie (0.763 vs 0.771). From raw ModernBERT, KL is worse than Laya's (0.191).
- **The benchmark is weak.** It has 400 synthetic test cases, labelled by a ~4B teacher, and is not peer-reviewed, so scores partly measure agreement with that teacher.
- **Only specialists work.** Generalists trained on synthetic workflows score 0.25–0.34 zero-shot, below the input-ignoring prior (0.470).
- **Training is unstable.** BoolQ seeds span 72.3–79.4%, so it is unreliable for BoolQ-like tasks. The large model stalled on 2 of 6 seeds until warmup was raised, and warmup is confounded with a lower peak learning rate.
- **Per-decision coverage overstates automation.** Requiring all five decisions to clear the threshold qualifies 19–27% of cases, and those are only 69.8–81.6% correct against a 90% target.
- **The process was adaptive.** Live test accuracy was visible during training, and p-values are unadjusted for the configurations tried.

## Limitations found by others

## What it leaves untried
- **No head-to-head with Set-LLM, UniMC or DuplexJev**, the methods sharing its mechanism. Whether packing beats them is open.
- **Options never compare directly.** The add-on mixer did not help (0.764 vs 0.766). Whether close calls between similar options suffer is untested.
- **No human labels or live corpus.** Whether autonomy thresholds transfer to real deployments, the property operators rely on, is unmeasured.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - presentation sensitivity]]
