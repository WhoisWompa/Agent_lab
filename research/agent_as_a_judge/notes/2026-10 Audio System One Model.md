---
title: "Audio System One Model: Typed Probabilistic Perception of Emotion in Speech"
authors: Jaime Bellver-Soler et al.
date: 2026-10
arxiv: 2610.22401
url: https://arxiv.org/abs/2610.22401
venue: arXiv (submitted to ICASSP)
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/papers/Audio System One Model - Typed Probabilistic Perception of Emotion in Speech (Bellver-Soler 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "calibration"]
---
# Audio System One Model: Typed Probabilistic Perception of Emotion in Speech

## One line
ASOM is a System One model for speech: a 6.2M-parameter reader over frozen Whisper and Qwen encoders that answers typed choice, score and yes/no questions written at request time about a clip, in one pass, each with a calibrated distribution trained on listener votes.

## Method
Problem: speech classifiers are fast and calibrated but locked to one label set; audio LLMs take any question but pay a generation pass per question and give poorly calibrated probabilities. ASOM brings the Jev-style typed request (choice, ordinal score, yes/no) to audio.

Mechanism: every option becomes a text "criterion" (question + option name + short description), encoded by a frozen Qwen2.5-1.5B (token mean). Because the criterion never sees the audio, its vector is cached. The clip goes through a frozen Whisper-large-v3, pooled from four blocks and 64 time segments. Two small heads project both sides to unit vectors in R^256; option j scores s_j = 8 * cos(c_j, a) + b(c_j), with b a linear function of the criterion alone that learns each option's base rate, and a softmax runs over the options of each question. All criteria are scored in one matrix product, so cost barely depends on the number of questions. With no per-class parameters, new wordings or labels need no retraining.

Training target is the distribution of listener votes, under cross-entropy (a strictly proper scoring rule), so the model learns disagreement, not only the majority. Because few listeners make votes noisy, a second, smoother target is distilled from cross-fitted auxiliary readers, each predicting only clips it never saw. Half the steps paraphrase questions and options. Assumes frozen encoders carry the paralinguistic signal and listener votes are the right ground truth.

## Evaluated on
- Matches a classifier while taking labels as text: a class-table variant on the same features and data gets F1 0.379 vs 0.382 for ASOM; MSP-Podcast macro-F1 0.383, above every audio-only classifier.
- More accurate and better calibrated than audio LLMs: leads the best zero-shot ALM (Qwen2.5-Omni-7B) by 0.072 F1 and a LoRA-fine-tuned Omni-3B on the same 169k clips by 0.026; every zero-shot ALM has log loss above the constant class prior (2.097+ vs 1.863), ASOM is at 1.507.
- Cheap: 20 questions in 13.1 ms, 17 to 41 times faster than ALMs (230 to 545 ms), mostly the Whisper encoder.
- Survives rewording: synonyms plus paraphrased descriptions cost 0.038 F1, a new question 0.035; eight unseen emotion words as yes/no reach AUC 0.714 vs 0.762 on trained ones.
- Hears rather than reads: on 17 unseen corpora where the transcript is at chance, 0.419 vs 0.281 for the best zero-shot ALM; Omni-7B keeps 84% of its MSP-Podcast F1 from the transcript alone.

## Limitations admitted by the authors
- Closed tests on affect only; speaker identity or recording content, which ALMs can answer, were not tested.
- Unseen labels are ranked well (AUC 0.721) but almost never chosen (F1 0.018), because the learned bias b favours trained labels: the open-label claim holds for ranking, not for picking.
- Gender, asked in an unseen wording, trails Omni-7B (0.873 vs 0.927 accuracy).
- Where the words carry the emotion, the best ALM leads (0.550 vs 0.494 on 4 such corpora), so a transcript still matters.
- Data is the bottleneck: only three corpora release per-listener votes; dropping CREMA-D and Emozionalmente cuts the unseen-corpus mean from 0.440 to 0.362.
- Vote-based training trades transfer for calibration: a CLIP-style contrastive loss raises the unseen mean by 0.067 but worsens log loss by 0.369 and yes/no AUC from 0.763 to 0.596.

## Limitations found by others

## What it leaves untried
- Using ASOM as a judge or gate over spoken agent output (e.g., scoring a voice agent's tone) is not tried; calibration is shown against votes, not as a decision threshold.
- No fix for the base-rate bias that suppresses unseen labels, such as dropping or recalibrating b for new criteria, even though the paper names b as the cause of F1 0.018.
- No test beyond affect: the claim that "nothing in the reader is tied to emotion" is unsupported until a non-affect attribute set with votes is trained and compared to ALMs.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - calibration]]
