---
title: "AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation"
authors: Dong Huang et al.
date: 2023-12
arxiv: 2312.13010
url: https://arxiv.org/abs/2312.13010
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2312.13010.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation

## One line
A three-agent code generator in which a test designer writes tests without seeing the code, a script runs them, and the failures drive the programmer's rewrites, beating larger multi-agent systems at about a third of their token cost.

## Method
The problem: earlier multi-agent coders (MetaGPT with 5 agents, ChatDev with 7) spend many tokens on coordination, and their feedback is weak because the tests are poor (MetaGPT's generated tests are correct only 79.3% of the time on HumanEval). Single-agent loops that write code and then tests in one conversation have the same weakness: the tests inherit the code's blind spots.

The fix is a small team with a strict separation of jobs.
- **Programmer** (LLM): prompted to follow four steps (understand the task, pick an algorithm, write pseudocode, write code). In later rounds it rewrites the code from error feedback.
- **Test designer** (LLM): sees only the task description, never the code. The prompt asks for basic, edge-case and large-scale tests. The paper's argument is that tests written after the code are biased by it, and that one model optimising both jobs does both worse. Both reasons are stated, not isolated: the ablation shows a gap but does not separate "distraction" from "bias".
- **Test executor** (a Python script, not an LLM): runs the code against the tests in a local terminal and checks for errors. If all tests pass it returns the code. Otherwise it sends the error text back to the programmer, up to an iteration budget (5 in the reported runs).

Measurable work (does it run, does it pass) is done by the executor; judgment (what to test, how to fix) is done by the two LLM roles. The harness enforces that the test designer is blind to the code and that termination is "all tests pass or budget spent". Output format is fixed with code-block markers so the script can parse it.

## Evaluated on
- Beats all 16 baselines on HumanEval, MBPP and their stricter "-ET" versions. With GPT-4: 96.3% and 91.8% pass@1 on HumanEval and MBPP, against 90.2% and 78.9% for the best multi-agent baseline cited. With GPT-3.5-turbo: mean 84.1% against 75.3% for CodeCoT. Baseline numbers are copied from their papers, not rerun.
- Holds up on the harder test versions: GPT-3.5-turbo scores 89.1% on MBPP-ET versus 63.0% for CodeCoT, so the gain is not just from passing weak tests.
- Cheaper: GPT-4 uses 56.9K and 66.3K tokens on HumanEval and MBPP, against 138.2K / 206.5K (MetaGPT), 183.7K / 259.3K (ChatDev) and 149.2K / 193.6K (AgentVerse).
- Both extra agents are needed. Programmer alone with GPT-3.5-turbo: 61.0 on HumanEval and 47.9 on MBPP. Adding only the designer or only the executor gives 64.0 / 62.3 and 64.6 / 69.3. All three: 79.9 / 89.9. The executor-only variant uses the 2-3 tests in the prompt.
- Independent tests are better tests: accuracy 87.8% / 89.9% on HumanEval / MBPP (GPT-3.5-turbo) against 47.0% / 57.2% for the same model writing tests alongside code. Line coverage is 87.5% / 89.5% against 70.2% / 61.3%.
- One agent doing both jobs reaches 71.3 / 79.4 pass@1 versus 79.9 / 89.9 for separate agents; its tests are 61.0% / 51.8% accurate.
- More rounds help but flatten: HumanEval rises from 74.4 (1 iteration) to 79.9 (5).

## Limitations admitted by the authors
- The main text points to an appendix for limitations and broader impact, but the extracted text contains no such section. Nothing is admitted in the text I could read.

## Limitations found by others

## What it leaves untried
- Tests are still wrong about 10% of the time (87.8-91.4% accuracy). The paper argues bad tests mislead the programmer but never measures how often a wrong test pulls a correct program into a wrong rewrite, or adds a check on the tests.
- Only function-level, self-contained Python tasks (HumanEval, MBPP). Whether a blind test designer works when the spec is long, multi-file or ambiguous is not tried.
- The comparison to MetaGPT, ChatDev and AgentVerse is on numbers from their papers, so differences in model version and iteration budget are not controlled. The "separate agents" ablation also does not test the same two roles in one agent with the code hidden from the tests, which would separate bias from distraction.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]
