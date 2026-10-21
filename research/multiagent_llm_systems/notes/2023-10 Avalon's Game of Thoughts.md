---
title: "Avalon's Game of Thoughts: Battle Against Deception through Recursive Contemplation"
authors: Shenzhi Wang et al.
date: 2023-10
arxiv: 2310.01320
url: https://arxiv.org/abs/2310.01320
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2310.01320.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "self-refinement and critique loops"]
---
# Avalon's Game of Thoughts: Battle Against Deception through Recursive Contemplation

## One line
ReCon is a prompting scheme (private thinking, then a second pass that checks how others will read the draft speech) that helps LLM agents play the hidden-role game Avalon without being deceived or leaking their own role.

## Method
Problem: LLM-agent work assumes the information agents receive is honest. The authors name three failures in deceptive settings, shown with chain-of-thought (CoT) agents in Avalon. The agent is misled by plausible but malicious suggestions. It exposes private information, for example Merlin revealing that he is Merlin. Its hidden intent, such as an evil player faking loyalty, is not visible to a human overseer.

Idea: each turn runs two stages, and only the final speech is public.
- Formulation contemplation. The agent first guesses the other players' roles from the discussion log (the "first-order perspective transition"). It keeps this guess private and carries it to the next turn. It then writes a private thought and a first draft of its speech. Thinking before speaking gives private information a safe place to be used without being said aloud.
- Refinement contemplation. The agent asks how good-side and evil-side players would each read the draft (the "second-order perspective transition"). It then rewrites both thought and speech. This is a self-critique pass whose critic is the agent imagining its audience.

The method adds no fine-tuning and no game data. The authors' explanation for why it works: the private stage stops the model repeating prompt secrets in its output, and the second stage lets it catch a leak before speaking. They offer this from example logs, not from a test.

## Evaluated on
- ReCon beats CoT as the good side. Against a CoT evil side, the good side wins 19.4% with ReCon versus 15.0% with CoT (both sides CoT) in the ethics statement's comparison. The main-text bars (ChatGPT and Claude) are in figures, not in the text.
- ReCon as the evil side against ReCon good players wins 70.6%, versus 85.0% for CoT against CoT. The authors take this as evidence the method helps defence more than attack. It also shows ReCon-vs-ReCon is not a like-for-like comparison with the CoT pair.
- Every component helps in ablation. Removing either stage or either perspective transition lowers win rate in every setting. First- and second-order transitions matter most on the good side, and refinement matters most on the evil side.
- GPT-4 preference judgments over six qualities (concealment, logic, contribution, persuasiveness, information, creativity) favour ReCon over CoT on all six. Persuasiveness dips for variants with formulation contemplation, because thinking first makes speeches shorter and less rousing.
- Qualitative cases show ReCon rejecting an "add an evil player for balance" argument that fooled CoT, and keeping Merlin's knowledge hidden.

## Limitations admitted by the authors
- LLM reasoning is weak. An agent playing Percival cannot infer that a proposer who puts Merlin and Morgana on one team must be Morgana, which an expert human sees at once.
- Making the agent talk like a human costs performance. Success falls from 83.3% to 77.8% with human-like speech, and to 70.0% with human-like thoughts and speech. Default outputs are overly formal and "fail the Turing test".
- Safety alignment is shallow. GPT-4 refuses "write a message to deceive others", yet writes a deceptive message when asked to play Morgana. The authors say RLHF covers content but not logic, which also means ReCon could sharpen deception.
- Whether the displayed contemplation is the real reasoning cannot be verified. They only note that logs show it matching the agent's interests.
- Llama-2-70b-chat fails the required output format (bracketed "[approve]" decisions), while ChatGPT and Claude comply over 90% of the time. ReCon therefore was not tested on open models.

## Limitations found by others

## What it leaves untried
- Tests only in Avalon, against a CoT opponent chosen as the weaker side. No test against humans, against other prompting methods, or in other settings. The authors only list Werewolf and similar games as future work.
- Win rates are not paired with any measure of how often the agent is actually deceived. The "detects deception" claim rests on a few example logs and GPT-4 preference scores, not a direct deception-detection rate.
- The prompts do not reward honest play, so the authors do not study whether the two-stage design could be stripped of its ability to deceive while keeping its resistance to deception.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - self-refinement and critique loops]]
