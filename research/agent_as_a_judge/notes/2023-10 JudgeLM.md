---
title: JudgeLM: Fine-tuned Large Language Models are Scalable Judges
authors: Lianghui Zhu et al.
date: 2023-10
arxiv: 2310.17631
url: https://arxiv.org/abs/2310.17631
venue: ICLR 2025
category: trained-judges-reward-models
---
# JudgeLM: Fine-tuned Large Language Models are Scalable Judges

## One line
Vicuna-based 7B/13B/33B pairwise judges fine-tuned on 100K GPT-4 judgments, with augmentations against position, knowledge and format bias.

## Method
- Data: about 100K seed tasks with answer pairs from 11 LLMs, judged by GPT-4 (scores plus reasons). Synthetic teacher labels.
- Format: pairwise; outputs two scores then a rationale.
- Swap augmentation (position bias), reference support (knowledge bias), reference drop (format bias).

## Evaluated on
- Agreement with the GPT-4 teacher above 90% on its own benchmark, higher than the reported human-to-human agreement of about 82% (paper abstract). Also extended to multimodal, multi-turn, single-answer grading.

## Limitations admitted by the authors
- Agreement is measured against GPT-4, the same teacher, so it measures imitation, not correctness.
- Biases reduced, not removed.

## Limitations found by others
- Huang et al. (arXiv:2403.02839) found JudgeLM-style fine-tuned judges score high in-domain but drop on other formats and benchmarks.
- JudgeBench (arXiv:2410.12784) lists JudgeLM among fine-tuned judges that perform poorly on hard pairs.

## What it leaves untried
- Agreement with ground-truth correctness rather than with the teacher judge.
