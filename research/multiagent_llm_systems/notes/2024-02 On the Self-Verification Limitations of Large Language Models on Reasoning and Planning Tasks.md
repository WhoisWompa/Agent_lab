---
title: On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks
authors: Kaya Stechly et al.
date: 2024-02
arxiv: 2402.08115
url: https://arxiv.org/abs/2402.08115
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2402.08115.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "judge and decision-model audits"]
---
# On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks

## One line
GPT-4 critiquing its own answers makes results worse on Game of 24, graph coloring and planning, and the gains from an external sound verifier come mostly from having many guesses and a reliable check, not from the critique text.

## Method
The problem: self-critique loops (Reflexion, Self-Refine, Self-Debug) are widely believed to help because verifying is assumed to be easier than generating. The authors doubt this for an LLM, whose behaviour may be closer to approximate retrieval than to complexity-class reasoning. They also argue that earlier tests used benchmarks that were too easy, multiple choice (so n-1 critiques solve any n-way question by just not repeating an answer), memorisable, or without ground truth.

They pick three tasks with machine-checkable answers and unlimited fresh instances: Game of 24, graph coloring, and Blocksworld / Mystery Blocksworld planning. One loop is built: GPT-4 proposes an answer, the same GPT-4 verifies it, and if it says "wrong", its critique is added to a prompt holding the full history of attempts and the model retries until it accepts or times out.

The loop is split into three roles and each is ablated separately:
- Verification: the LLM verifier's false positive and false negative rates are measured.
- Critique generation: the quality of the free-form critique is scored against ground truth.
- Critique consideration: the LLM verifier is replaced by a sound external checker (SymPy, an edge check, VAL). Feedback is then cut from every error, to the first error, to "wrong" only, to nothing: the same base prompt is re-sampled until the checker accepts.

The reasoning for the design: if the critique content matters, performance should track feedback richness; if only the verifier matters, a no-feedback resampling loop should match it.

## Evaluated on
- Self-critique lowers accuracy against one-shot prompting in most domains (100 instances each): Game of 24 5% to 3%, graph coloring 16% to 2%, Mystery Blocksworld 4% to 0%. Blocksworld alone improves, 40% to 55%. Accuracy falls as backprompts accumulate.
- The cause is verifier false negatives: graph coloring 95.8% (113/118) and Mystery Blocksworld 97.1% (100/103) of correct answers are rejected, so the loop discards correct answers and times out on worse later ones.
- Critique text is unreliable: in graph coloring it cites non-existent edges and wrong colours, and in planning it invents precondition states. In Game of 24 the LLM scores 81.6% of correct expressions as equalling 24 but marks only 79.1% as correct, so it sometimes computes right and judges wrong.
- A sound verifier gives large gains: Game of 24 5% to 36-38%, graph coloring 16% to about 37%, Blocksworld 40% to 87%.
- Feedback richness barely matters: binary, first-error and all-error feedback land close together, and in two domains more feedback does worse. Plain resampling with no critique at k=15 gets 28%, 40%, 68% and 9% (Game of 24, coloring, Blocksworld, Mystery), close to the feedback runs. At k=25 these rise to 42%, 44%, 72% and 14%. Self-consistency voting over 15 samples gives no gain (6%, 14%, 42%, 4%), so the gain is verified selection, not majority voting.
- Appendix: chain-of-thought verification lifts Game of 24 verifier accuracy from 87% to 98.8%, but a 6-point gap to the sound verifier remains, at 17 times the output tokens. In graph coloring, CoT verification gets the full pipeline to 0%. With 150 direct queries plus a sound verifier, Game of 24 reaches 70%, close to Tree of Thoughts' reported 74%.

## Limitations admitted by the authors
- Only GPT-4 and three formal domains are tested, so the result may not carry to qualitative tasks (writing, style) where no sound verifier exists. The authors choose formal tasks deliberately, and the paper leaves open how far they generalise.
- Chain-of-thought verification helps in some domains, but the gain is uneven and costly (17 times the output tokens in Game of 24), so the negative result is not shown to hold under every verification prompt.
- Sound verifiers exist only for tasks with formal correctness. For real-world use the authors only expect "a menagerie of partial critics" whose consensus counts as verification, and they do not test this.
- The Tree of Thoughts contradiction is explained as a difference in setup, which the authors check only through a cost-matched rerun (70% vs 74%).

## Limitations found by others

## What it leaves untried
- Other models. Whether stronger or fine-tuned verifiers cut the 95%+ false negative rates is not tested, though that rate decides whether the loop helps.
- Partial or approximate external critics (the LLM-Modulo suggestion). The paper's conclusion depends on them, but only sound verifiers are tested.
- Cost-matched comparison of resampling against critique loops on tasks where a sound check is unavailable. This would show whether critique ever beats plain guessing there.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - judge and decision-model audits]]
