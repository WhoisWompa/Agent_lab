---
title: "Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments"
authors: Linhai Ma et al.
date: 2026-10
arxiv: 2610.18497
url: https://arxiv.org/abs/2610.18497
venue: arXiv
category: llm-judge-foundations
pdf: agent as a judge papers/decision models/open models/evaluations/Judges Follow the Reference - The Derivation Gap in Verifying Tool-Call Arguments (Ma 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["LLM and agent judges", "judge and decision-model audits"]
---
# Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments

## One line
Shows that tool-call argument judges reject correct values their input does not state outright, and fixes it with DeRef, a separate model that reads the full history without the candidate and writes the expected value for the judge.

## Method
Problem: an argument judge sees a truncated context and one proposed value. A correct value can arrive by different *derivation paths*: copied from visible text, taken from a tool return cut from the judge's input, reformatted, filled from a schema default, or inferred. The *derivation gap* is how much less often correct out-of-view values are accepted than correct visible ones, at a per-judge threshold accepting 80% of correct values.

Diagnosis: judges do not derive the right value; they match the candidate against an explicit reference in their input. Missing information is only part of it: on FC-RewardBench nothing is cut and the default is printed in the schema, yet correct defaults carry the largest gap.

Fix, DeRef: a deriver (Qwen3.8-27B, thinking on) reads the uncut history and schema, never the candidate, and writes each argument's expected value and source, or says the context does not fix it. The text goes into the judge's usual truncated input; the judge is unchanged. Hiding the candidate stops the reference echoing the value under test and lets candidates share one reference. It works because it supplies exactly what judges rely on, built from history the judge never saw.

## Evaluated on
- The gap is universal and survives scale: all seven judges (System One models CLM and Jev, five open LLMs) show 22.67-36.13 points on ComplexFuncBench and FinTrace, and 14.40-50.51 on FCRB defaults; the 27B judge still has 12.29-29.76. Base rates do not explain it (FCRB defaults 77% correct vs 75% visible).
- Judges follow what they see: with the correct source buried past the cut and a wrong distractor visible, AUROC falls from 91.89-99.88 to 39.80-49.03, and to 26.71-39.88 against the distractor alone.
- Restating a default moves acceptance by at most 6.18 points; the DeRef reference lifts it to 73.02-88.06%.
- DeRef improves every judge: AUROC up 1.44-22.14 points in all 12 judge-benchmark pairs, and from chance to 98.40-99.59 on the buried set. It beats RevisEval in 10 of 12 pairs (8 significantly); the two losses (0.32, 0.27) are not significant.
- The gain is the reference, not reasoning or context: the 27B judge thinking stays 2.82-10.92 points below itself reading the reference without thinking; full history instead is 11.58 points worse on CFB.
- Swapping a wrong value into the reference drops AUROC from 92.16-99.91 to 42.63-77.92 on CFB and FCRB.

## Limitations admitted by the authors
- One gold value per argument: a reference naming it can make judges reject another correct value, which also flatters DeRef; worst-case removal of the 3-4% unconfirmed wrong labels keeps every gain significant, but Jev's FinTrace gain shrinks to 0.89 points.
- DeRef does not shrink the FinTrace no-source gap for three of four judges, so values matching nothing stay unsolved (only 45% of these are correct, which may explain part of it).
- One deriver, Qwen3.8-27B, throughout; a Qwen3-8B deriver loses 6.53 points on CFB, and other families are untested.
- No frontier LLM is tested as judge, so the gap at that scale is unknown.
- Since a wrong reference overturns judgments, an erring deriver or a misleading tool return can make the judge approve a wrong argument; the authors call DeRef support for review, not a replacement.

## Limitations found by others

## What it leaves untried
- No injected tool return is tested against the deriver itself, though the swap test shows a poisoned reference flips verdicts; that is the realistic attack on a guard.
- The judge follows the reference blindly; using judge-deriver disagreement as an escalation signal would address both the single-gold and poisoning problems.

## Topics
[[Topic - LLM and agent judges]] · [[Topic - judge and decision-model audits]]
