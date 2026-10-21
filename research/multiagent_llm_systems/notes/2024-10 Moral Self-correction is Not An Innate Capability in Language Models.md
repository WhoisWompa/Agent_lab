---
title: Moral Self-correction is Not An Innate Capability in Language Models
authors: Guangliang Liu et al.
date: 2024-10
arxiv: 2410.20513
url: https://arxiv.org/abs/2410.20513
venue: arXiv (cs.CL, v8, Jan 2026)
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2410.20513.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Moral Self-correction is Not An Innate Capability in Language Models

## One line
Behavioral and hidden-state analyses of 7-8B models show that moral self-correction (fewer stereotyped answers, less toxic text) works through shallow heuristics: the models cannot tell their better output from their worse one, and they underuse external feedback when they also reason in chain of thought (CoT).

## Method
The problem: intrinsic self-correction (an instruction such as "do not rely on stereotypes") is known to help on moral tasks, but extrinsic self-correction is little studied. In extrinsic self-correction a second LLM critiques the answer. Nobody had asked how internal reasoning (CoT) and outside feedback interact. The authors ask whether the ability is innate, meaning real moral sensitivity. Their reasoning is that a model with such sensitivity should recognise the moral signal in its own outputs and weight it above the immoral one.

The paper tests this in two ways.

1. **Behavioral test, the "self-distinguishing task".** The model sees its own self-correction rounds as context and must (a) name the stereotyped group in a BBQ question, or (b) pick the less toxic of two of its own responses from the same trajectory. If correction came from real sensitivity, accuracy here should match or beat the share of samples the correction actually detoxified.

2. **Mechanistic test.** The paper builds "warrants" for each case: the correct label, evidence for why the other choices are biased, or a far less toxic completion. It measures layer-wise cosine similarity (layer 15 onward) between hidden states of the CoT or feedback text and these warrants. Controls remove feedback or CoT from the input and compare. An instruction-following-difficulty (IFD) score measures which part of the context the output actually follows (lower means more influence).

Six strategies are compared: intrinsic, extrinsic (DeepSeek-chat gives feedback only, never an answer), and both combined, each with and without CoT, over 5 rounds. Models are Mistral-7B, Gemma-7B and DeepSeek-R1-Distill-Llama-8B.

## Evaluated on
BBQ (ambiguous contexts, 11 bias types) and RealToxicity.
- Feedback and CoT do help. Mistral-7B on Age bias goes from .586 baseline to .870 intrinsic, .993 intrinsic with CoT, and .991 extrinsic. Extrinsic beats intrinsic on all 12 tasks. No single strategy wins everywhere.
- Stacking strategies is unreliable. Combining intrinsic and extrinsic correction is best on Age only and worse than either alone on Religion (.943 vs .973 and .980).
- Models correct themselves without recognising it. On BBQ, self-correction context lowers the model's ability to name the stereotyped group below its no-context baseline in 4 of 6 biases. On RealToxicity, accuracy at picking the less toxic response stays below the share of samples actually detoxified in four of the six methods. Feedback-free intrinsic runs were slightly better at distinguishing, which the authors attribute to conflict between internal knowledge and external feedback (their interpretation, not tested).
- Feedback is informative but barely used. On RealToxicity the feedback text alone activates many warrants, yet removing it from the input leaves warrant activation unchanged (ext vs ext without feedback). The model is not reading it.
- With both CoT and feedback, the model follows its CoT. IFD shows outputs track the CoT rather than the feedback even though feedback activates more warrants. On BBQ-Age, feedback also lowers the warrants the CoT activates. On RealToxicity (Mistral) it leaves them unchanged, which explains why extrinsic with CoT is worse than extrinsic alone. DeepSeek shows clear conflict instead.

## Limitations admitted by the authors
- Only the moral domain (stereotypes, toxicity) is studied. Whether the finding holds for reasoning or code self-correction is untested, so "not innate" is shown for morality only.
- The conflict between external feedback and internal knowledge is named as the cause, but the authors say it is a hard question they did not explore well. The generator-evaluator capability gap is offered as the bottleneck without a test.
- Differences between bias types are attributed to uneven pretraining corpora with no evidence given. The proposed fix (reinforcement learning for the generator plus a rational-speech-act-style listener-friendly evaluator) is a sketch, and the authors list open obstacles: defining communicative goals, generalisation, and abstract moral language.

## Limitations found by others

## What it leaves untried
- Training the generator to use feedback, or the evaluator to write feedback matched to the generator's ability. This is the paper's own proposal, but no run is reported, and the claimed bottleneck stays unconfirmed.
- Pairing the evaluator with a stronger generator or varying their gap. Only one external evaluator (DeepSeek-chat) is used, so the capability-gap explanation is never varied.
- Models above 8B or with safety tuning. Prior work cited in the paper finds scale and alignment matter, so the "not innate" claim may not extend to them.

## Topics
[[Topic - self-refinement and critique loops]]
