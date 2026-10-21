---
title: Is Self-Repair a Silver Bullet for Code Generation?
authors: Theo X. Olausson et al.
date: 2023-06
arxiv: 2306.09896
url: https://arxiv.org/abs/2306.09896
venue: ICLR 2024
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2306.09896.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Is Self-Repair a Silver Bullet for Code Generation?

## One line
Measures whether letting a model debug its own code beats simply sampling more programs at equal cost, and finds the gain is modest and capped by the quality of the model's own feedback.

## Method
Self-repair is split into four stages: sample programs, run them against unit tests, have a feedback model explain the failure in text, then have the code model repair the program using that explanation. Separating the feedback stage lets the authors swap it out and study it alone. The sampled programs, feedback strings and repairs form a "repair tree".

The paper's central move is a fair cost comparison. A repair tree is charged for every program it samples (initial plus repairs) and compared with plain i.i.d. sampling, pass@k, with the same k. The question is whether the same budget spent on fresh samples would have worked better. Feedback tokens are not charged in the main metric. An appendix adds token-count versions (batched and sequential) and says the trends hold.

The hypothesis is that self-repair is bottlenecked by the model's ability to critique its own code. Two interventions test it. A stronger model writes the feedback while the weaker one repairs. A human programmer writes the feedback for GPT-4's failing programs.

## Evaluated on
Code Llama-13b-instruct, GPT-3.5 and GPT-4 on HumanEval and APPS (300 sampled APPS tasks), with full unit tests available.
- Self-repair is not reliably better than resampling. On APPS only GPT-4 gains clearly (up to 8% over baseline). GPT-3.5 gains marginally, and only at the largest budgets. Gains at small budgets are marginal or absent, and many cells fall below 1.0 (GPT-3.5 on APPS at np=1 with 10 repairs scores 0.83 of baseline).
- Spend the budget on diverse first drafts, not repeated repair. For GPT-4 on APPS, 10 initial samples plus 1 repair each gives 1.05x the pass@20 baseline. 2 initial samples plus 10 repairs each gives 0.97x the pass@22 baseline.
- Gains are larger on harder problems. GPT-3.5 gains up to 34% on APPS competition-level tasks. The pattern is not simply tied to baseline strength: GPT-3.5 on APPS-introductory scores about like GPT-3.5 on HumanEval, yet only HumanEval benefits.
- A stronger feedback model fixes the bottleneck. On APPS, Code Llama and GPT-3.5 with GPT-3.5 or GPT-4 feedback beat both their own baseline and their own self-repair at all budgets.
- Human feedback beats GPT-4's own. Repairs pass 52.6% of the time with human feedback and 33.3% with GPT-4 feedback (1.58x). The gap widens with difficulty: 14.67% vs 3.67% on competition tasks.
- GPT-4's feedback is inaccurate in 32 of 80 cases against 7 of 80 for humans. Humans voiced uncertainty in 7 of 80 and GPT-4 in none, and humans suggested large-scale changes slightly more often (23 vs 18 of 80).

## Limitations admitted by the authors
- Results come from sub-sampling one large pre-generated repair tree (50 initial programs, 25 feedbacks) rather than independent trees. This could introduce statistical artefacts. The authors keep n well below the pool size, and the standard deviations are very small.
- Only self-contained Python tasks with complete executable tests. Real software work has incomplete specifications, long context dependencies and few tests per snippet, so the findings may not transfer.
- The human study did not record debugging time, so it shows feedback quality matters but not whether human-in-the-loop repair is worth the effort. It is also small: 16 participants, 40 failing programs.
- The main metric ignores feedback tokens and so risks overstating the benefit of self-repair. The appendix shows sequential (chat-style) use is somewhat less beneficial, especially when the baseline pass rate is already high.
- Why repair helps in some settings and not others is conjecture: generation and repair success rates rise together, and "many subtle factors" decide which wins. The paper does not isolate them.

## Limitations found by others

## What it leaves untried
- Training or prompting the model to give more accurate and more uncertainty-aware feedback. The paper identifies feedback quality as the bottleneck and the human gap (7 vs 32 inaccurate of 80) but does not try to close it.
- Settings without full tests, such as ambiguous specifications or synthesised tests, where repair might matter more than resampling.
- A predictor for when to repair versus resample. The paper says efficacy is hard to predict but offers none.

## Topics
[[Topic - self-refinement and critique loops]]
