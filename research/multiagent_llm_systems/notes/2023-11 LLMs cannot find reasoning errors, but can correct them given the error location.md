---
title: LLMs cannot find reasoning errors, but can correct them given the error location
authors: Gladys Tyen et al.
date: 2023-11
arxiv: 2311.08516
url: https://arxiv.org/abs/2311.08516
venue: arXiv (v3, June 2024)
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2311.08516.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "judge and decision-model audits", "trained judges and reward models"]
---
# LLMs cannot find reasoning errors, but can correct them given the error location

## One line
Splits self-correction into finding the mistake and fixing it, and shows that the finding step is the bottleneck: LLMs fix a reasoning step well when told where it is wrong, but cannot locate it themselves.

## Method
Prior work found that prompting an LLM to self-correct reasoning often turns correct answers into wrong ones. The authors hypothesise the cause is not poor correction but poor mistake finding, and test the two parts separately.

- **Mistake finding.** They release BIG-Bench Mistake, chain-of-thought traces from PaLM 2 Unicorn on five tasks, each labelled with the first wrong step (or "no mistake"). Human annotators agree almost perfectly (Krippendorff's alpha 0.979 to 0.998 on the four human-labelled tasks), so the errors are objective. Five LLMs are asked, with three-shot prompts, to name the first wrong step, either from the whole trace or step by step.
- **Correction.** A simple backtracking baseline: keep the trace up to the step before the mistake, resample that step at temperature 1 until it differs from the original (up to 8 tries), then regenerate the rest at temperature 0. The mistake location is given by oracle labels, so correction is tested without any finding error. A random-location baseline checks that the gain is not just resampling.
- **Closing the gap.** Because oracle labels are unavailable in practice, they simulate classifiers of varying accuracy to find how good a finder must be, and fine-tune a small model (PaLM 2 Otter) as a step-correctness classifier on four tasks, testing on the fifth.

## Evaluated on
- LLMs cannot find mistakes: the best model, GPT-4, reaches 52.87 overall accuracy at the best prompting method. GPT-3.5-Turbo reaches 14.78 and PaLM 2 Unicorn 23.67 with direct step-level prompting.
- More output means more false alarms: accuracy on mistake-free traces falls from direct trace-level to chain-of-thought step-level prompting (for example GPT-3.5-Turbo on tracking shuffled objects: 67.50 to 0.00 on mistake-free traces). The authors' explanation is that each extra call is another chance to flag something. This is a hypothesis; the paper does not test it.
- Mistake finding is a poor proxy for answer correctness: weighted F1 is mostly below the 78 obtained by always predicting "wrong answer" (for example GPT-3.5-Turbo direct trace-level scores 6.58 on word sorting).
- Correction works given the location: oracle backtracking raises accuracy on originally incorrect traces by +18.04 to +43.92 points per task, against losses of 0 to 11.43 points on originally correct ones. A random location gains only +5.16 to +21.57 and loses more (up to 15.91).
- Finding does not need to be perfect: losses on correct traces plateau around 65% finder accuracy, and for most tasks gains exceed losses at about 60 to 70%.
- A small classifier trained out of domain beats three-shot Unicorn on 4 of 5 tasks (for example +22.59 on Dyck languages, +19.67 on tracking shuffled objects), but is still below the 60 to 70% needed.

## Limitations admitted by the authors
- The tasks are artificial (word sorting, Dyck languages), chosen to make errors unambiguous, so it is unknown whether backtracking works on realistic reasoning.
- Only a skewed sample was tested (85% incorrect-answer traces, 45 correct-answer traces per task), not the full BIG-Bench sets. Net gain depends on starting accuracy: on tracking shuffled objects, a 50% start would rise to 68.6%, while a 99% start would fall to 92.8%.
- The trained classifier does not reach the accuracy backtracking needs; the authors think more data is needed, with no evidence given.
- Traces come from PaLM 2 Unicorn, so using Unicorn as its own finder is likely biased; the self- versus cross-model difference is left unexamined.
- The claim that weak finding is a main cause of failed self-correction is a hypothesis, not a tested result.

## Limitations found by others

## What it leaves untried
- Closing the loop: using a trained finder, not oracle labels, to drive backtracking end to end and repeating it when the new step is also wrong.
- Scaling the classifier: more training data and a size-versus-accuracy study, since the current one falls short of the 60 to 70% threshold.
- Realistic tasks, and the number of regeneration tries (fixed at 8) as a variable.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - judge and decision-model audits]] · [[Topic - trained judges and reward models]]
