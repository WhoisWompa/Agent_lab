---
title: When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs
authors: Ryo Kamoi et al.
date: 2024-06
arxiv: 2406.01297
url: https://arxiv.org/abs/2406.01297
venue: arXiv (v3, Dec 2024)
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2406.01297.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs

## One line
A critical survey that splits "can LLMs self-correct?" into three precise research questions, shows that many positive results come from unfair or unrealistic setups, and concludes that the bottleneck is feedback quality.

## Method
The survey starts from a conflict: Self-Refine, RCI and Reflexion report gains from self-correction, while other studies find no gain or a loss on arithmetic, closed-book QA, code, planning and graph colouring. The authors argue the conflict exists because papers never say which question they test.

They define three questions:
- RQ1: can a model fix its best-possible initial response using only its own abilities?
- RQ2: can it do so with external information such as code interpreters, search or fine-tuning?
- RQ3: is the corrected output better than other uses of the same compute?

Each question has its own requirements. RQ1 and RQ2 need a best-effort initial response, no oracle information, and a comparison against that initial response. RQ3 needs strong baselines at comparable cost.

Frameworks are then sorted along two axes. Realistic versus unrealistic: unrealistic ones use ground-truth answers, so they can answer no question. Fair versus unfair: unfair ones weaken the first draft, or use a tool (such as search) only in the correction step although it could also have improved the first draft. "Intrinsic" correction is the fair case with no extra information. Using this sorting, they re-read the literature and give a checklist (Tables 7 and 8) for designing and for reporting negative results.

The central claim is that verifying is not generally easier than generating. Reliable correction needs reliable feedback, so the weak point is the feedback step, not the revision step.

## Evaluated on
This is a literature analysis. There are no new experiments. The claims rest on re-reading prior papers.
- No prior work shows fair intrinsic self-correction with prompted feedback on general tasks. The reason is that the positive results use unfair settings. RCI uses ground-truth answers as the stop condition and never touches correct answers, so it ignores correct answers being wrongly changed. Reflexion's HotpotQA feedback is exact match against the gold answer. Self-Refine and Constitutional AI revisions start from weak initial prompts, such as wrong few-shot labels used only for the first draft.
- Intrinsic correction does work on tasks where verification is much easier than generation. CoVe is the example: a list answer decomposes into per-item checks. Constrained generation and Game of 24 are similar, since the check is trivial.
- With reliable external feedback, correction works. Code interpreters, symbolic reasoners and proof assistants are the cases named, and the literature broadly agrees on this. Tools used only at correction time (RARR, search-based methods) are classed as unfair for RQ2, though fine for RQ3.
- Fine-tuning enables correction, but most feedback-training methods use more than 100K training instances (SelFee 178K, Volcano 274K, Self-Critique 100K). Behaviour with little data is unexplored.
- RQ3 is open: many studies skip self-consistency or generate-and-rank baselines, although self-correction costs several extra LLM calls. The survey names this gap but gives no head-to-head number.

## Limitations admitted by the authors
- Coverage stops at May 2024. Later work, including RL-trained reasoners such as o1, gets only a brief section, so the conclusions may be dated. The paper does not test whether they still hold.
- The framework taxonomy covers same-model correction. Cross-model correction and multi-agent debate are set aside for RQ1 and RQ2, because a different model is not the model fixing its own mistake.
- The finding that prompted feedback fails rests on mostly simple feedback prompts (Self-Refine, Huang et al.). The authors say better prompts, such as reference-free LLM metrics or confidence signals, may change this.
- The task base is skewed towards math and code. Open-ended generation, where model-based feedback is common, is under-studied, so "intrinsic correction is hard" may not hold there.
- No quantitative measure of feedback quality is pooled. The authors recommend direct measures such as error-detection accuracy, but prior papers rarely report them, so the bottleneck claim is inferred from downstream accuracy.

## Limitations found by others

## What it leaves untried
- Direct measurement of feedback quality across the studied methods, for example error-detection accuracy. This is the claimed bottleneck, yet no cross-paper evidence on it is given.
- Fair intrinsic correction with stronger feedback (human-written criteria, decomposition, confidence) on open-ended tasks, where verification may be easier.
- Fine-tuning for self-correction with small data, and pre-training changes that would give the ability without large annotation. The paper only flags these as future work.

## Topics
[[Topic - self-refinement and critique loops]]
