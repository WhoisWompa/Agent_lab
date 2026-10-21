---
title: Self-rewarding correction for mathematical reasoning
authors: Wei Xiong et al.
date: 2025-02
arxiv: 2502.19613
url: https://arxiv.org/abs/2502.19613
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2502.19613.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "trained judges and reward models", "judges as reward signals"]
---
# Self-rewarding correction for mathematical reasoning

## One line
Trains one LLM to solve a math problem, judge its own answer with a "[VERIFY] correct/wrong" token, and revise only when it judged itself wrong, so no external reward model is needed at inference.

## Method
Problem: prompted self-correction does not work, because the model has no signal for when to revise and when to stop. Prior successes relied on an external reward model, which means running two models. The paper folds generator, judge and reviser into one model.

Stage 1, self-rewarding fine-tuning. Because the base model rarely self-corrects and never self-evaluates, a full trajectory cannot be sampled directly. The authors sample the pieces separately (first attempt, self-evaluation, correction), keep only pieces consistent with a ground-truth checker, and stitch them into one long chain of thought. Three kinds are kept: wrong, flagged wrong, then corrected; correct, wrongly flagged wrong, then still correct; and correct, flagged correct. The third kind teaches the model to stop. The second kind teaches it not to break a right answer when its own verdict is mistaken.

Stage 2, reinforcement learning (PPO, or multi-turn DPO) on the final-answer correctness from a rule-based checker. The reward is the oracle, not a learned proxy, which the authors say limits reward hacking.

Inference is a loop: answer, self-evaluate, stop if "correct", otherwise revise and re-evaluate. Training is on-policy only (self-generated data).

## Evaluated on
- Intrinsic self-correction hurts. On MATH500 with Qwen2.5-Math-7B, final accuracy falls from 65.4 to 51.4 because 15.4% of answers flip from correct to wrong. Even with a gold reward given in the prompt, only 1.4% flip from wrong to correct.
- The method fixes the stopping problem. With the same rejection-sampling data, STaR/RAFT+ loses 3.8% of correct answers; self-rewarding fine-tuning loses 0.4% and gains 5.0% (MATH500 final 77.2 vs 71.2). RL pushes final accuracy to 80.2 (PPO) and 78.6 (DPO).
- It beats single-turn training on the same base. OlympiadBench 43.4 vs 39.5 and Minerva Math 38.4 vs 33.1 (PPO). The extra pass costs tokens.
- It is cheaper than sampling more. On MATH with Llama-3-8B-it, independent sampling reaches 40.4% at 64 samples; the self-rewarding model reaches 42.8% with 26.4 samples. It averages 1.65 samples per problem on MATH and 1.25 on GSM8K because it stops after a confident first answer.
- It beats an external reward model on the final metric. Llama-3-SFT on MATH: 40.3 final accuracy vs 39.2 with a separately trained ORM (same training set). The trend holds on Llama and on Qwen.

## Limitations admitted by the authors
- The self-judge is weaker than a dedicated reward model at spotting wrong answers: 76.4% vs 88.4% on MATH (Llama-3-SFT), while right answers are recognised at 70.0% vs 66.9%. The authors attribute this to distribution shift (the policy changes after training, the judge was fit to the old policy) and to model capacity. This is a hypothesis; a larger base model was not tried.
- Judge accuracy is lopsided and the data mix moves it. Shifting the training mix toward correct trajectories moved accuracy from (72.1%, 75.3%) to (63.6%, 82.4%) for (correct, wrong) classes. Qwen favours recognising correct answers (about 90%+) but only 36-56% on wrong ones.
- RL does not reliably improve the judging or the correction. Most RL gain is from better first attempts; the gap between first and final accuracy narrows after about 100 PPO steps and the model becomes more willing to call answers correct. DPO shifts judge accuracy unpredictably (a 10% drop in other classes when mixing ranking rules). Too low a correct-to-incorrect flip rate makes the model too conservative: wrong-to-correct fixes fell from 8.8% to 5.6%.
- Reward shaping was gamed. Paying 1.5 for wrong-then-correct made PPO deliberately answer wrong first: 18.6% first-attempt vs 77.6% final accuracy on MATH500 at step 150. A two-stage reward schedule gave no gain.
- Experiments use a simplified two-turn format with user-supplied instructions between turns, since models did not follow the instructions in a single long chain reliably. Horizon is capped at two iterations for resource reasons.
- Distilling revisions from a 70B teacher lifted turn-1 accuracy but not correction ability, and cut judge accuracy on correct answers to 36.7% vs 63.6%.

## Limitations found by others

## What it leaves untried
- Multi-turn RL designed for correction (such as SCoRe) was not tried; the authors say open-source frameworks make it hard. It matters because plain outcome RL erodes the self-correction behaviour late in training.
- Step-level self-rewarding (judging each reasoning step, as process rewards do) rather than whole-answer verdicts is only suggested.
- Only math with a programmatic checker was studied; the claim that a model can judge itself without external feedback is untested where no oracle exists for training.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - trained judges and reward models]] · [[Topic - judges as reward signals]]
