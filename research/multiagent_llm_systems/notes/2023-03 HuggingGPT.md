---
title: "HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face"
authors: Yongliang Shen et al.
date: 2023-03
arxiv: 2303.17580
url: https://arxiv.org/abs/2303.17580
venue: NeurIPS 2023
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2303.17580.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation"]
---
# HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

## One line
An LLM acts as controller that plans a request into a dependency graph of sub-tasks, picks a Hugging Face expert model for each from its text description, runs them, and writes the answer from their outputs.

## Method
The problem: LLMs only handle text, cannot schedule several models for a compound request, and are weaker than fine-tuned experts on specialised tasks. The paper's idea is that language is the generic interface. Every expert model already has a text description on the Hugging Face hub, so the LLM can manage the experts by reading those descriptions, with no per-model prompt engineering and no retraining. A new model joins by adding its description.

There is one controller LLM (ChatGPT, GPT-4) and many non-LLM expert models as workers. The controller runs four stages:
1. **Task planning.** The request is parsed into a JSON list. Each task has a type, an id, a `dep` list of prerequisite tasks and arguments. The prompt gives the slot format and a few demonstrations. Chat history is included so multi-turn references resolve.
2. **Model selection.** Choosing a model is framed as a single-choice question. Context length rules out listing every model, so candidates are filtered by task type, ranked by Hugging Face download count (the authors' proxy for quality and popularity, not verified), and cut to the top K. The LLM picks one and gives a reason.
3. **Task execution.** The harness, not the LLM, runs the models. Outputs of earlier tasks are substituted for `<resource>-id` placeholders in later tasks' arguments. Tasks with no unmet dependency run in parallel. Local endpoints are preferred over cloud ones.
4. **Response generation.** The LLM gets the request, plan, model choices and raw outputs (boxes, scores) and answers in plain language, with a confidence level.

The planning is global: the whole task graph comes from one query. The paper contrasts this with the step-by-step planners of AutoGPT and BabyAGI. It argues, without measuring it, that those need many LLM calls and can loop forever after one bad step, while global planning gives one answer but cannot guarantee the plan is correct or optimal.

## Evaluated on
- **The controller's ability limits the system.** Human evaluation on 130 requests: GPT-3.5 reaches 63.08% end-to-end success, Vicuna-13b 15.64% and Alpaca-13b 6.92%. Planning passing rate is 91.22% for GPT-3.5 against 79.41% and 51.04%.
- **Selection is not the bottleneck.** GPT-3.5 model selection passes 93.89% of cases (84.29% rationality). Most failures therefore come from planning or execution.
- **Even strong controllers plan complex requests poorly.** On 46 expert-annotated complex requests, GPT-4 scores 41.36% accuracy on sequential tasks and 58.33% on graph tasks. GPT-3.5 gets 18.18% and 20.83%, and Vicuna-7b 7.45% and 10.12%. The authors say a substantial gap to human plans remains.
- **Demonstrations help, with diminishing returns.** Raising demo variety from 2 to 10 task types lifts GPT-3.5 graph-task F1 from 43.42 to 64.24. More than 4 demonstrations adds little.
- **Qualitative cases** (about 24 supported task types across language, vision, audio, video) show correct ordering, parallel runs and resource passing, e.g. pose detection feeding pose-conditioned image generation. These are hand-picked examples with no failure rate attached.

## Limitations admitted by the authors
- Plan quality rests entirely on the LLM. A feasible, optimal plan is not guaranteed, and the results above show the gap.
- Latency: every request needs several LLM calls (plan, select, respond), so response time grows. The paper gives no timing numbers.
- Context length: the model descriptions that can be listed are bounded, which is why candidates are cut to top-K by downloads. A better model outside the top K is never seen.
- Instability: the LLM sometimes ignores the format or gives wrong answers, which breaks the workflow. No recovery or retry mechanism is described.
- The GPT-4-as-critic plan score is "not always correct" despite high correlation. The paper reports no correlation number. The main planning labels are themselves GPT-4-generated, and only 46 requests are human-annotated.

## Limitations found by others

## What it leaves untried
- No check or repair step between stages. A bad plan or a failed model call just propagates, and the 63% end-to-end success suggests that is costly.
- No comparison against iterative planners on cost or success. The argument for global planning stays qualitative.
- Model selection by download count is never tested against alternatives such as learned or description-quality-based ranking, so how much quality is lost is unknown.

## Topics
[[Topic - orchestration and delegation]]
