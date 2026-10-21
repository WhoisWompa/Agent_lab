---
title: Self-collaboration Code Generation via ChatGPT
authors: Yihong Dong et al.
date: 2023-04
arxiv: 2304.07590
url: https://arxiv.org/abs/2304.07590
venue: ACM Transactions on Software Engineering and Methodology (arXiv preprint)
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2304.07590.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# Self-collaboration Code Generation via ChatGPT

## One line
Three ChatGPT instances, told through role instructions to act as analyst, coder and tester in a waterfall workflow, generate code better than one ChatGPT instance (29.9% to 47.1% relative Pass@1 gain).

## Method
The problem: one LLM call struggles with complex code requirements, and training separate specialised models into a team is costly and short of data. The paper instead has the same LLM collaborate with itself. The framework has two parts. Division of labour: the task is split into stages, and each stage gets an LLM agent initialised once with a role instruction (team description, role description, the user requirement). The claim is that role-playing does not add ability; it narrows the generation space and evokes latent skill. Collaboration: agents exchange natural-language messages through a shared blackboard that holds the earlier stages' outputs.

The instance copies a simplified waterfall model. The analyst decomposes the requirement and writes a high-level plan. The coder writes code from the plan, and later repairs it from the tester's report. The tester does not run code. It is another LLM call that writes a report on functionality, readability and maintainability, and ends with a fixed pass phrase when satisfied. The loop ends when the tester passes the code or after at most 4 interactions. The output is updated only in the coding stage. Role messages are fixed by prompt; the harness only enforces the interaction cap and the pass phrase.

## Evaluated on
- Beats a single ChatGPT and prompting baselines with the same base model. On HumanEval, ChatGPT gets 57.3 and the team 74.4. That is above GPT-4 alone (67.6) and above CodeX+CodeT (65.8). On MBPP the team gets 68.2 against 52.2.
- Gains are larger on the stricter edge-case versions, +31.4% on HumanEval-ET and +34.6% on MBPP-ET. The authors suggest the team covers more boundary conditions. This is a hypothesis; the paper does not test it.
- Harder and more realistic tasks: APPS Competition 1.2 to 3.4 and Interview 6.8 to 10.7. CoderEval average 19.82 to 29.14, with the largest gains on standalone and Plib-dependent code (35.87 to 47.63, 21.43 to 38.1).
- Both added roles help. Coder alone gets 45.1 on HumanEval, +analyst 54.9, +tester 56.8, both 63.5. Role instructions beat plain zero-shot instructions (64.4 vs 60.0) and 4-shot prompting (58.1).
- Not just repeated editing: a baseline that repeatedly asks "improve this code" scores 55.5 on HumanEval, below plain ChatGPT's 57.3.
- Most of the gain comes in the first round. Moving from no interaction to one round lifts HumanEval from 45.1 to 60.4; rounds up to 4 add only to 63.5.
- Applying it to GPT-4 lifts HumanEval from 67.7 to 90.2. Open models gain only from about 7B parameters up. Llama2-7B gains less than CodeLlama-7B, which the authors read as needing domain knowledge, instruction following and reasoning.

## Limitations admitted by the authors
- Benchmarks do not match real software work, and no benchmark exists that does. The repository-level and game or website demos are single case studies with no numbers.
- Fully autonomous teams still need a little human guidance. The error analysis shows analyst errors mostly come from ambiguous or incomplete requirements.
- The three-role structure is specific to code. Other problems may need a different team, and the paper does not show one.
- Remaining errors are mostly the coder's, tied to the base model: after the team, 36.5% of HumanEval tasks stay unsolved while 18.4% are rescued. Tester suggestions about exception handling can turn a correct return value into a raised error and fail a test.
- Interaction depth was capped at 4 rounds by ChatGPT's token limit, so the benefit of longer collaboration is unknown.

## Limitations found by others

## What it leaves untried
- The tester only simulates testing. Adding a compiler gave 64.6 against 63.5 without it, but the case for real execution feedback is tested only on HumanEval's public use cases and the paper calls the gain comparable.
- Cost is reported only as a plot, with the coder normalised to 1 and the team "moderate" among prompting methods. No token or dollar figures, and no comparison against sampling more candidates with the same budget.
- Team shapes beyond the one waterfall chain (parallel roles, other domains) are named as possible but not run.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]
