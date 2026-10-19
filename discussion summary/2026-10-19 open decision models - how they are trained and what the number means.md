# Open decision models: how they are trained and what the number means

Discussion of 2026-10-19. Source material: the 43 model papers and 27 evaluation papers in
`agent as a judge papers/decision models/open models/`. The long write-up with every number and
citation is `open models/HOW THEY ARE TRAINED.md`; the six per-batch reader notes are in
`open models/notes/`. This file is the plain-language version of what was discussed.

---

## 1. What these models are

Jev, and every open copy of it, does one job. You give it a situation, a question and a fixed list
of possible answers. It returns one probability per answer, in a single forward pass, no text
written.

Underneath they are ordinary chat models with the last step changed. A chat model ends by scoring
every possible next token. Put the options in the prompt labelled A, B, C, read the scores for the
tokens "A", "B", "C", softmax over just those. The model was about to answer with a letter anyway;
you take its leaning instead of letting it speak.

The 43 open models differ only in where that probability is read from:

| Readout | Examples | Buys | Costs |
|---|---|---|---|
| Letter logits at one position, no new parameters | Jeff, Intern-Decision, Nimble, StartLux, SII-Decision; untrained: AnyJev, SemIf | Works untrained on a chat backbone; many questions per pass | Option order moves the answer |
| Small head over each option's hidden state | Kev, Open-Jev, Drex, OmniMed-Jev, VideoJev, FunDM, Laya | Any option count; head fits in seconds | Order effects depend on whether options see each other |
| Each option scored alone, then combined | Prism-1, Verdict, Jeva | Zero order flips, no steering by injected options | Cannot say "none of the above" |
| Separate encoders, late interaction | MetaEncoder, CLM, ASOM, bekko | Caching, millions of candidates | Single-vector bottleneck |
| Small encoder (BERT-size) with trained head | Laya, THX-01, Chinese-Jev, Verdict, BERT-as-a-Judge | 6 to 30 ms | Collapses out of distribution |

On top: looped (SanSi), reason-then-read (StartLux, Dyad, OpenJev-RLCD), multi-question packing.

## 2. How to build one, as a story

1. **Get a model that already talks.** Download the instruction-tuned (chat) version of Qwen or
   Gemma, not the base version. The chat version already knows that a question with options A to E
   is answered with a letter, so its letter scores mean something before any training. Same recipe
   on base Gemma scored 70.3 after training; chat Gemma scored 79.6 before training.
2. **Collect questions with known answers.** Mostly old human-labelled datasets reshaped into
   state / question / options / answer: sentiment, exams, NLI, ratings. Thousands exist. Nobody
   generated these; they picked them. Inner Jev: 79 tasks, ~300k items. Chinese Decision: 20 sources,
   10M items.
3. **Optional: ask a bigger model how sure it is.** The old datasets only say "the answer is B".
   A teacher adds shading: "B, 75 percent sure". It grades, it does not invent. It runs once, before
   training. Leaving it out cost under two points, within noise.
4. **Teach the chat model to lean instead of talk.** Show the question with options, read its letter
   scores, nudge with cross-entropy toward the target. Shuffle option order every time an example is
   shown (one random order per visit, not all permutations). LoRA rank 16 to 64, a few hundred
   steps, a few GPU-hours. Training longer makes calibration worse, not better.
5. **Fix the overconfidence.** Fit one temperature per question type on a few hundred held-out
   items so that "70 percent" comes out right 70 percent of the time. Nearly always above one.

RL adds nothing for a single-pass model: the output is a differentiable softmax, so any proper
scoring rule can be minimised directly, and the expected gradient of REINFORCE on Brier is just the
Brier gradient with noise. After temperature scaling no objective beats plain cross-entropy. RL only
earns its place when the trained thing is sampled text: a rationale (OpenJev-RLCD, StartLux) or a
verbalised confidence (MIT RLCR, Rewarding Doubt). "RLCD" in the open literature is four different
methods; Jev's own is undisclosed in every paper.

## 3. Where the data comes from

Mostly converted human datasets. The synthetic part is a minority, made five specific ways, none
random:

- **Relabel existing questions with a teacher.** Question exists; a big model answers it, its
  distribution becomes a soft target.
- **Generate documents in hand-picked domains, then label them.** Inner Jev: ~30k business
  documents across ~40 domains. Teacher prompts are not published.
- **Compute the answer by program.** Rule plus case, code decides. SecJev: 37k items, zero label
  errors. Chess and grid worlds use an engine or simulator.
- **Have many models answer, then judge.** BERT-as-a-Judge: 36 models answer a million exam
  questions, one teacher marks each right or wrong.
- **Break good examples on purpose.** Luna-2 injects hallucinations; Nimble edits one sentence by
  at most eight words so the answer flips.

Domains are chosen by hand: deployment target, benchmark error analysis, or a decision-type
taxonomy. Quality control: keep only where two verifiers agree (StartLux), human spot checks
(BERT-as-a-Judge, 97.5 percent agreement), certificates (Nimble).

## 4. The teacher, worked example

Item from an old sentiment dataset:

```
State:    "The battery lasts forever but the screen scratched within a week."
Question: What is the sentiment of this review?
Options:  A) positive   B) negative   C) mixed
```

The teacher reads it **once**, no sampling. Read its scores for the next token "A", "B", "C",
softmax. One pass gives a full distribution.

| | A positive | B negative | C mixed |
|---|---|---|---|
| Human hard label | 0 | 1.00 | 0 |
| Teacher 1 (27B) | 0.05 | 0.18 | 0.77 |
| Teacher 2 (122B) | 0.03 | 0.40 | 0.57 |
| Average of teachers | 0.04 | 0.29 | 0.67 |

Averaging is per column: (0.05 + 0.03) / 2 = 0.04, and so on. The row still sums to 1. Where the
teachers agree the average is sharp; where they disagree it sits in between and the student learns
the item is a close call.

The student reads the same prompt, its own letter scores are softmaxed, cross-entropy measures the
gap to the target row, the gradient moves the student's weights. Repeat over ~50k items.

Cost: one or two passes per item on an open model you run yourself, once. With Jev as teacher,
126k labels cost a few dollars. Fifteen samples per item would buy precision the student cannot
use: noisy labels cancel across many items, and hard labels instead of soft changed nothing
measurable. The expensive input is human labels, which is why old datasets are reused.

Caveats: the teacher's raw distribution carries the teacher's own overconfidence (the student's
temperature fit corrects the level anyway). Letting the teacher reason first sharpens the readout
to near certainty, which is why Inner Jev averages two reasoning runs per teacher.

## 5. The MIT formula (RLCR), untangled

Reward = correctness − (q − correctness)².

- **correctness**: 1 if the model's own answer was right, 0 if wrong. Checked against the key.
- **q**: the confidence the model itself stated. The model controls this.
- No teacher anywhere in it.

| Model says | Right? | correctness | q | (q − correctness)² | reward |
|---|---|---|---|---|---|
| "B, 90% sure" | yes | 1 | 0.9 | 0.01 | 0.99 |
| "B, 90% sure" | no | 0 | 0.9 | 0.81 | −0.81 |
| "B, 50% sure" | yes | 1 | 0.5 | 0.25 | 0.75 |
| "B, 50% sure" | no | 0 | 0.5 | 0.25 | −0.25 |

Being right still pays most, so accuracy is kept. Saying 90 and being wrong costs far more than
saying 50 and being wrong. The honest number is the profitable number. Brier is bounded, so it
cannot be hacked; log-loss is unbounded and can be.

Cousin to the supervised recipe: both compare the student's confidence to something true and push
them together. MIT compares to the hard outcome of its own answer; the supervised recipe compares to
a label. For a single-pass model these give the same gradient.

## 6. What the number means (the core of the discussion)

The MIT paper proves that training on a proper scoring rule makes the model's best move to report
its true probability, and the open recipe is a proper scoring rule. So the number is honest **on
average, on data like what it was calibrated on**. Not honest about any single decision. Not honest
when the task changes: the same Jev has calibration error 0.03 on one task and 0.29 on another. Even
after RLCR, out-of-domain calibration error is "often high in an absolute sense" (their words).

| What the number tracks well | What it tracks badly |
|---|---|
| How settled the model is: would the answer survive a rephrasing (flip AUROC 0.82 to 0.93) | Whether the answer is right (error AUROC ~0.59) |

About a fifth of decisions are settled, confident and wrong. These are the systematic errors:
following the option's name instead of its definition, trusting a reference answer, following a
planted cue. They appear in every judge tested, open or closed, decision model or chat model.

A stronger backbone does not fix this. Bigger models are more accurate, not more honest, and they
hold their mistakes more firmly. Raw overconfidence barely moves with size; in one family the 27B was
worse calibrated than the 4B. These models do not reason: the number is a reflex. Where reasoning
was added first, the answer token afterwards sat above 0.99 on nearly every rollout, and swapping in
a rationale for the opposite label flipped the answer 92 to 100 percent of the time, still at near
certainty.

So the signal is asymmetric. **Low confidence means "look harder". High confidence means nothing
extra.**

Selection inflation: when a model's confidence is used to pick the best of several trajectories, the
picked one is over-rated (92 percent correct at 80 to 90 confidence individually, 78 percent after
best-of-32 selection). A judge that both scores and chooses must be calibrated on what it chose.

## 7. Per domain: recalibrate, do not retrain

Two separate failures: bad at the task (fix by retraining weights) or fine at the task but the
probabilities mean the wrong thing (fix by refitting temperature and threshold on a small labelled
set). For ordinary English agent-trajectory judging, the first mostly does not arise; the second
always does.

- Temperature: roughly 100 to 500 labelled decisions.
- Certified threshold ("at most 5 percent of what I accept is wrong"): 22 to 45 hand-checked
  accepted examples, via Learn-Then-Test.
- Redo when the rubric changes, the judged agent changes, or the model is swapped or quantised.
- Weight retraining paid off only for domains with their own language: security, medical,
  Indonesian, agriculture. Tuning on a narrow domain buys that domain and costs the rest.
- There is no general calibration in any paper. What survives domain shift is the ranking within a
  task, not the absolute number. A fixed gate is domain-specific whether intended or not.

## 8. Multiple models, consensus, weighting

Evidence from the chess paper (Sadoun 2026, "From Probabilities to Decisions: Search and
Multi-Teacher Distillation with Jev"), which trained a chess evaluator from judge labels and
measured Lichess rating:

- Jev plus Qwen averaged beat either alone, and beat asking Jev twice. Two different models beat
  two reads of one.
- All four teachers together did worse than the best pair. More judges did not keep helping.
- In the retrieval half, more data from one judge beat adding a second judge.
- On items where judges disagreed, Jev alone was right more often than the average, yet the average
  trained the stronger student. Label accuracy and downstream usefulness are not the same.

Why the count does not help: the models share their mistakes ("cheaper, faster, and wrong in the
same places"). Consensus only cancels what the models disagree on.

Bias comes from three places, and a different base model fixes only the first:

1. **Base weights.** Two LoRA tunes of the same Qwen are one judge wearing two hats.
2. **Training labels.** Most open models are labelled by a bigger Qwen. Different bases tuned on the
   same teacher's labels learn the same mistakes. "Shared errors are possible and undetectable."
3. **Question framing.** Option-name bias, reference trust, planted cues. In every judge, across
   bases. Fixed by changing the input, not the model.

In the chess paper Qwen's best partner was Jev, not OLMo or DiffusionGemma, though those are
different base families. Different lineage (labels, objective) mattered more than different base.

Cheapest diversity: pose the same question differently to the same model (both option orders,
different wordings). Agreement between reads beat any confidence threshold as a stop signal in the
agent-loop papers, and needs no labels.

Weighting: never by raw confidence (the most overconfident model wins every vote; Qwen needed a
temperature near 18 where Jev was near honest). Temperature-scale each model on your data first,
then plain-average. Weighting by measured reliability is a small model trained on your labels and
must be refit when the rubric changes.

Mixed teachers at training time work the same way: averaging removes the mistakes teachers make
separately and keeps the ones they make together. Random sampling of a teacher per example is
mathematically the same as averaging under cross-entropy, only noisier (ChaosNLI result: sampled
annotator equals CE on averaged votes). Two teachers that fail differently beat one; four that
overlap beat nothing; a weak teacher drags the mixture down.

Consensus does not touch the case where every model is confidently wrong together.

## 9. What it means for the judge

- Yes/no per rubric item, both option orders, averaged.
- Temperature fitted on 100 to 500 judged trajectories from the lab's own runs.
- Threshold picked on a separate split by an upper confidence bound, refit per rubric.
- Read low confidence as "test from another angle", high confidence as "will not change under
  rephrasing", never as "correct".
- Something in the stop loop that is not a model's opinion: run the code, check the output against
  the task. Jev as a stop guard accepted 40.7 percent of an agent's wrong "finished" claims.
- If an open model replaces Jev: isolated-option or sorted-option letter readout on a 27B to 31B
  instruct backbone, tuned briefly on the lab's own trajectories. Pair with a second judge of a
  different training lineage, not just a different base.
