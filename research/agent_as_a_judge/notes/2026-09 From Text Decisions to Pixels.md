---
title: "From Text Decisions to Pixels: A Study of Jev-Style Visual Choice Model (PixelJev)"
authors: Xunlan Zhou et al.
date: 2026-09
arxiv: 2609.29283
url: https://arxiv.org/abs/2609.29283
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/From Text Decisions to Pixels - A Study of Jev-Style Visual Choice Model (Zhou 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models"]
---
# From Text Decisions to Pixels: A Study of Jev-Style Visual Choice Model (PixelJev)

## One line
PixelJev puts a Jev-style decision contract on small open vision-language models (Qwen3.5 2B/4B): an image, an instruction and a candidate list supplied at runtime go in, a valid candidate ID with probabilities over those candidates comes out, and the paper measures how far few-shot LoRA adaptation of that interface carries across recognition and multiple-choice VQA.

## Method
- **Problem**: software often needs a vision model to pick from caller-supplied options, not describe the image. Fixed classifiers hard-wire one label set; chat VLMs return free text that must be parsed and can be invalid.
- **Contract**: F(image, instruction, C) = (chosen ID, p, provenance), where C is an ordered list of (stable ID, description) pairs mapped to single-token letter slots (2 to 52). p is a softmax over only those slots' logits at the first assistant position, with thinking off. Nothing is generated, so output is valid by construction. p is conditional on C, not a probability of correctness, and there is no reject option.
- **What is new**: by the authors' own account, little mechanically. The readout is ordinary multiple-choice scoring (logits match constrained one-token generation exactly), and Visual Jev already combines native images with adaptation. The contribution is an explicit contract plus a study of what each optional add-on buys.
- **Three separate regimes**: frozen inference (no labels); one shared LoRA on language-attention projections only, vision tower frozen, trained with candidate-conditioned cross-entropy and shuffled candidates on 64 images per class from three recognition tasks; and a held-out scalar temperature. The bet: the backbone already knows the concepts, and the adapter only teaches it to put mass on the right slot.

## Evaluated on
- **Adaptation lifts fine-grained recognition**: Pets 60.13% to 92.40±0.26%, EuroSAT 49.63% to 88.31±1.57%. A prompt-only control credits the adapter, not the readout: both paths go 56.36% to 91.63%.
- **A specialist still wins on source tasks**: a 64-shot DINOv2 probe gets 95.67 / 97.62 / 92.13 on Pets / CIFAR-10 / EuroSAT, above adapted 2B on all three.
- **Transfer is real but does not replace scale**: on DTD (47 unseen texture labels) adapted 2B reaches 58.28% vs 45.85% frozen 2B, but frozen 4B gets 64.79%.
- **Per-question options work without VQA training**: frozen 2B scores 80.61% on A-OKVQA and 81.51% on ScienceQA. The adapter adds +2.71 pp on A-OKVQA but only +0.84 pp [-2.14, 3.33] on ScienceQA, where frozen 4B leads it by 6.99 pp.
- **Direct readout only buys validity**: on adapted ScienceQA it beats free generation by +1.88 pp, all from 55 invalid generations (52 out-of-range letters), 38 of which readout gets right. Generation takes 1.32-1.44x the time, constrained one-token 1.03-1.04x, so the saving is avoided decoding, not cheaper decisions.

## Limitations admitted by the authors
- **Accuracy gains do not bring calibration**: on DTD adaptation cuts NLL from 2.6985 to 1.9253 while ECE worsens from 0.1905 to 0.2040. Temperature scaling also worsened ECE for frozen CIFAR-10, adapted EuroSAT and the Pets DINOv2 probe.
- **Probabilities are relative to the list given**: an omitted correct answer still yields a confident pick, and scores are not comparable across candidate sets.
- **Image use is unproven**: VQA questions may be answerable from text or world knowledge, so VQA accuracy does not show visual evidence was used.
- **Narrow evidence**: one adaptation split, three seeds, one VQA adapter seed, one model family; pretraining overlap unknown.
- **Unmatched baselines**: supervision, parameters, compute and preprocessing differ, and there is no matched run against Visual Jev.
- **Partial order sensitivity**: reversing candidate order changed some decisions (97.30% agreement on 74 images); only finite diagnostics were run.

## Limitations found by others

## What it leaves untried
- **Candidate-conditioned training vs ordinary answer fine-tuning at matched budget**: without it the benefit may be convenience, not a better method, as the authors concede.
- **A reject or evidence-sufficiency output**: the model cannot say "none of these" or "need a better image", the gap that matters most for trusting its confidence.
- **Holding out whole task families** (counting, spatial relations): only that tests the "general-purpose" claim beyond three recognition tasks.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]]
