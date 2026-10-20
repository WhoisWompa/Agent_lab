---
title: General-Purpose AI Code of Practice, Safety and Security chapter (and AI Act Art. 55)
org: EU AI Office / European Commission
date: 2025-07
url: https://code-of-practice.ai/
kind: standard-or-regulation
category: third-party-and-benchmarks
---
# EU GPAI Code of Practice: Safety and Security chapter

## One line
The voluntary code, published 10 Jul 2025, through which providers of GPAI models with systemic risk show compliance with AI Act Art. 55. It requires state-of-the-art evaluations, adversarial testing, access for independent external evaluators, and a Safety and Security Model Report before a model is placed on the market.

## What they do
Commitments and measures, from an unofficial mirror of the final text ([code-of-practice.ai](https://code-of-practice.ai/)):
- **Measure 3.2**: "conduct at least state-of-the-art model evaluations" in the modalities relevant to systemic risk, including open-ended testing for unexpected behaviours. Example methods include "red-teaming and other methods of adversarial testing".
- **Measure 1.2**: lighter-touch evaluations, such as automated ones, at defined trigger points across the lifecycle, plus a full systemic-risk assessment "at least before placing the model on the market".
- **Measure 1.1**: the Framework must be confirmed "no later than two weeks before placing the model on the market".
- **Measure 3.5**: providers must give "an adequate number of independent external evaluators" adequate free access to:
  - the most capable model version;
  - its chains of thought, where available;
  - the version with the fewest safety mitigations.

  Further conditions:
  - Providers must publish criteria for evaluator applications.
  - Evaluators are protected from retaliation.
  - Providers "cannot delay or block publication for more than 30 business days".
  - There is an exception for models judged similarly safe or safer. Another exception applies if no qualified evaluators can be found, for example after a public call open for 20 business days ([CASRAI crosswalk](https://casrai.org/guides/mapping-ai-safety-program-to-eu-ai-act-gpai-code)).
- **Measure 5.1**: mitigations must be "sufficiently robust under adversarial pressure (e.g. fine-tuning attacks or jailbreaking)".
- **Commitment 7**: a Safety and Security Model Report to the AI Office before market placement. Measure 7.3 requires at least five random input/output samples from each relevant evaluation.
- **Thresholds**: systemic risk is presumed above 10^25 training FLOPs, and the Scientific Panel can designate models below it ([AI Act summary](https://artificialintelligenceact.eu/high-level-summary/)).

## Evidence
- **Timeline**: GPAI obligations applied from 2 Aug 2025. The Commission's enforcement powers, including fines, apply from 2 Aug 2026 ([CSA note](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-gpai-enforcement-20260509-csa-st/)).
- **Signatories**, per secondary sources ([Wikipedia](https://en.wikipedia.org/wiki/General-Purpose_AI_Code_of_Practice); CASRAI):
  - Amazon, Anthropic, Google, IBM, Microsoft, OpenAI, Mistral and Aleph Alpha signed in full.
  - xAI signed the Safety and Security chapter only.
  - Meta declined. Joel Kaplan said the code goes "far beyond the scope of the AI Act".
  - One source says more than 20 providers signed by August 2026.
- **Threshold review**: the Chairs' statement warns the 10^25 threshold may soon capture hundreds of models and asks the Commission to review it.

## Limitations and criticisms
- The code is voluntary; providers that do not sign must show compliance by other means.
- "State of the art" is not defined by a benchmark list.
- Sources differ on deadlines for serious-incident reporting.
- The text was read from an unofficial mirror, truncated after Measure 7.3.
- No public enforcement action against a GPAI provider was found as of October 2026.

## Relevance to agent evaluation
This is the first binding-backed requirement for independent external evaluator access, including chain of thought and minimally mitigated versions, and for evaluation samples in regulator reports. It creates demand for third-party evaluators (METR, Apollo, AISIs) and for evidence about agentic capability.
