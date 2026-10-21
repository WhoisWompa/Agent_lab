---
title: "Decision Models vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places"
authors: Delip Rao et al.
date: 2026-09
arxiv: 2609.29769
url: https://arxiv.org/abs/2609.29769
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/evaluations/Decision Models vs LLMs as Rubric Judges - Cheaper, Faster, and Wrong in the Same Places (Rao 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "confidence-gated escalation"]
---
# Decision Models vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places

## One line
Tests whether typed "decision models" (Jev and Perplexity's open Decider), which return only probabilities over the permitted answers, can replace or front-run flash-tier LLM rubric judges. They mostly can replace them at a small fraction of the cost, but they make the same errors, so a cascade adds almost no accuracy.

## Method
The problem is that LLM rubric judges are slow and expensive, and they score every (submission, criterion) pair with free-text reasoning. A decision model is a classifier-like model. It reads one request holding all of a unit's criteria and returns a probability distribution over the allowed answers, with no text. The authors test it in three ways: through argmax over the option labels (Choice), through the expected level over ordered descriptions (Score), and through P(yes) thresholded at 0.5 (Noul). The bet behind the paper is that a model built this differently should err in different places from a reasoning LLM. If it does, a confidence-gated cascade becomes possible: the decision model keeps its confident verdicts and sends the uncertain ones to an LLM judge. The paper's central argument is structural. A cascade can beat its fallback only on kept pairs that the first stage gets right and the fallback gets wrong. So it needs two things: (1) confidence that ranks the first stage's own errors, and (2) a fallback that is wrong somewhere else. To measure (2), the paper counts how often an LLM judge repeats the decision model's wrong answer. It compares that rate with an independence baseline: the rate at which the LLM gives that same wrong answer on other pairs with the same criterion and label. The baseline matters because judges that share an offset would agree often anyway.

## Evaluated on
- **Often a substitute, at a small fraction of the cost.** Jev trails the per-criterion LLM judges significantly in only 4 of 27 paired comparisons, and the Decider trails them in 5. The LLM judges cost 16 to 357 times as much and take 5 to 350 times as long.
- **Judges agree with each other more than with humans.** On all 7 ordinal panels, mean QWK between judges beats QWK between judges and labels (for example 0.66 vs 0.31 on HelpSteer2). On 6 of 7, Jev and every LLM judge rate below the raters. On ELLIPSE the labels put 36.3% of pairs at levels 4 to 5, and no Jev-set judge goes above 4.2%.
- **Errors are correlated.** On Jev's 12 most confident errors per ordinal panel, 96.0% of the LLM verdicts repeat Jev's answer, where independence predicts 50.3%. For the Decider it is 86.5% vs 47.9%. This holds at high effort and with higher-tier models (94.8%).
- **Confidence ranks errors, but cascades add little.** Jev's AUROC for correctness is 0.57 to 0.70 on 6 ordinal panels (0.49, flat, on ELLIPSE). Even with oracle thresholds, Jev-first cascades beat the best single judge by at most 2.7 points, and Decider-first cascades by at most 1.7. With higher-tier fallbacks, no cascade gains more than 1.7 points over either tier's best single judge. Cascades do save money: on most panels, the cascade that matches the best LLM judge costs under half as much.
- **Juries do not help.** A median jury's interval never lies above the best matched judge. It repeats Jev's wrong answer on 82 of 84 confident errors.

## Limitations admitted by the authors
- **The explanation for the shortfall is post hoc.** The idea that raters followed conventions missing from the criterion texts was inferred from the judges' errors and never tested by intervention: no exemplars, no rewritten levels. So the shared low ratings could equally come from shared training priors or literal reading.
- **Shared training data cannot be ruled out.** The Decider's training data include HelpSteer2 attribute labels, and synthetic rows were labelled by gpt-5.6-sol, a sibling of the Luna judge. Jev's and the LLMs' training data are undisclosed. Shared training signal is one route to correlated errors.
- **The LLM judges are not tuned.** They are flash-tier and zero-shot with default prompts. No flagship tier, no few-shot prompting and no no-reasoning run was tried, so the comparison is against a default LLM judge, not the best one obtainable.
- **Only two decision models were tested.** Nothing is shown for the class as a whole, and the Decider's ELLIPSE result (51.0% vs the rater reference's 51.4%, against Jev's 13.4%) is unexplained.
- **The statistics are lenient in places.** The 5-point parity margin was chosen post hoc and is absolute, so it is lenient where accuracy is low. Oracle cascade gains are optimistic, and the cross-fitted halves can hold as few as 12 units.
- **Labels are fragile.** Nearly half of the ELLIPSE labels depend on the rounding rule: the Decider's offset is −0.46 levels with half-up rounding and +0.004 with round-down. HelpSteer2 correctness tracks overall helpfulness at r = 0.94, and on LFQA no judge differs significantly from a baseline that only sees who wrote the answer.

## Limitations found by others

## What it leaves untried
- Deferral used only the decision model's own confidence. The LLM judges' token probabilities and verbalized confidence were never elicited, and a disagreement-based router might catch errors that confidence misses.
- No decision model was trained to be complementary to LLM judges. The authors call for this but do not attempt it, for example by training on the pairs where LLM judges fail.
- The conventions hypothesis was never tested directly, for example by rerunning ELLIPSE with exemplar essays, or giving the judges the raters' own instructions. That test would show whether the shared errors can be fixed through the rubric text or are baked into the models.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - confidence-gated escalation]]
