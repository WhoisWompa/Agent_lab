---
title: No Free Labels: Limitations of LLM-as-a-Judge Without Human Grounding
authors: Michael Krumdick et al.
date: 2025-03
arxiv: 2503.05061
url: https://arxiv.org/abs/2503.05061
venue: arXiv
category: llm-judge-foundations
---
# No Free Labels: Limitations of LLM-as-a-Judge Without Human Grounding

## One line
On expert-graded finance questions, LLM judges agree with experts mainly on the questions they could answer themselves; expert-written references largely fix this.

## Method
BFF-Bench: 160 business/finance questions with professional-written answers; experts grade 1,200 LLM responses (VERDICTS) on BFF-Bench and a hard MT-Bench subset. Compare graders with and without references.

## Evaluated on
LLM judges beat other automatic graders, but without a correct reference agreement with experts is high only where the judge itself answers correctly; providing expert references largely mitigates the gap.

## Limitations admitted by the authors
- Single domain (business/finance) and 160 questions.

## Limitations found by others


## What it leaves untried
- Tool-augmented judges that verify instead of relying on their own knowledge.
