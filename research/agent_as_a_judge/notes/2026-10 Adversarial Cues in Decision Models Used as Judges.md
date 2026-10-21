---
title: "Adversarial Cues in Decision Models Used as Judges: The Role of Request Presentation"
authors: Hongliang Liu
date: 2026-10
arxiv: 2610.11436
url: https://arxiv.org/abs/2610.11436
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Adversarial Cues in Decision Models Used as Judges - Request Presentation (Liu 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "presentation sensitivity"]
---
# Adversarial Cues in Decision Models Used as Judges: The Role of Request Presentation

## One line
Shows that one colon added to a wrong candidate answer makes the Jev decision model accept it, but only when the same judging request is sent with sorted JSON keys, so a judge that passes every competence control can still be exploitable under one logically equivalent presentation.

## Method
The problem: a judge told to grade only the *final* committed answer should reject a reply whose final value is wrong. Prior work showed short strings flip judges and that meaning-preserving formats shift outputs; this paper crosses the two and asks whether a candidate edit's effect depends on how the integration serialises the request.

The idea is a *certified* attack. The candidate is `X`, a bridge line, then `Final answer: Y.`, where X matches the trusted reference and Y differs from every reference. A parser can read the final value, so the required label is "incorrect" whatever the bridge says, and any acceptance is a provable error. The edit is minimal: the bridge is six random letters R, the cue is the same letters plus a colon (R:). The second factor belongs to the integration, not the attacker: "insertion" keeps field order (question, reference, reply), "sorted" sorts keys recursively (reply first), with identical decoded content. The hypothesis arose after a 200-source insertion-order study found nothing and a 28-source diagnosis pointed at key order; it was then tested on a fresh, source-disjoint bank. The attacker is assumed to know the reference-matching value X.

## Evaluated on
- **The colon only works under sorting.** Jev three-label: 2/200 to 52/200 false acceptance; published four-label instruction: 6/200 to 53/200. Under insertion every cell was 0/200. Interactions +25.0 pp [19.0, 31.0] and +23.5 pp [18.0, 29.5], Holm p = .00006.
- **Controls do not reveal it.** Jev passed every competence gate (at least 190/200 on bare-correct, bare-wrong, wrong-final-only; 180/200 on valid revision) under both presentations.
- **Concentrated in large errors.** Near mutations (Y = X+1) gave +2 pp; far mutations +48 and +45 pp. Similar in DROP and GSM8K.
- **A strong generative judge was immune.** GPT-6 Sol had zero observed false acceptances; with six missing responses the planned-panel interaction is bounded to [-0.5, +1.5] pp.
- **Earlier recurrence.** On the original certified subset R: was accepted 10/54 vs R 0/54; three repeat passes gave 10, 9, 10 vs zero.

## Limitations admitted by the authors
- **Sorting is a compound change.** It reorders state fields, outer request, criteria and (for Sol) embedded JSON together, so the responsible component is unmeasured.
- **Narrow, reference-aware construction.** The attacker must know a reference-matching value; natural prevalence is unmeasured, and a reference-blind generation study accepted 0/29 strict numeric wrong cases.
- **Mutation size is confounded.** Near and far mutations went to different questions, so magnitude, digit length and plausibility are not separated.
- **Presentation-dependent, not universal.** The first 200-source insertion-order study found no corrected colon effect, so many integrations may never see it.
- **Unstable service.** Byte-identical duplicates gave similar totals (48/200, 59/200) but different accepted sources, and the jev-1.13.0 identifier does not guarantee fixed weights.
- **No transfer to open models.** All five open decision implementations failed the competence gate (CLM NF4 got 0/80 on bare-wrong), and results flipped with precision: SemIf's colon effect went from +6.25 pp (NF4) to -18.75 pp (int8).
- **In-house verification.** The cue search was adaptive with no programme-wide correction; replay was author-run, with no outside audit.

## Limitations found by others

## What it leaves untried
- **Split the sort.** Varying state-field order alone would show whether "reply first" is the trigger, which is what integrators need to know.
- **A reference-blind attacker.** Whether an attacker without the reference value can exploit the presentation effect decides whether this matters in deployment.
- **Near and far on the same questions.** That would show whether error size really drives the effect or the split is an artefact of question assignment.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - presentation sensitivity]]
