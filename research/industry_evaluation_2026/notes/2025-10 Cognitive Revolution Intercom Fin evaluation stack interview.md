---
title: The Customer Service Revolution: Building Fin, with Eoghan McCabe & Fergal Reid of Intercom
org: Intercom (Eoghan McCabe, Fergal Reid) on Cognitive Revolution podcast
date: 2025-10
url: https://www.cognitiverevolution.ai/the-customer-service-revolution-building-fin-with-eoghan-mccabe-fergal-reid-of-intercom/
kind: production-practice
category: production-practice
---
# The Customer Service Revolution: Building Fin, with Eoghan McCabe & Fergal Reid of Intercom

## One line
Podcast (4 Oct 2025) where Intercom's CEO and Chief AI Officer describe Fin's evaluation stack: offline backtests as a first filter, production A/B tests as the arbiter, sensitive to ~0.1 pp resolution-rate shifts.

## What they do
- Mature backtesting framework for hallucination rate, answer rate, and retrieval against known-good answers; new models backtested within hours to a day.
- "Always test in production"; "Don't fall in love with your offline stuff" - you "can't build a perfect eval" for messy human conversations.
- Large-scale production A/B tests detect resolution-rate changes of about a tenth of a percentage point; resolution judged by the customer.
- Would A/B test any move to a more agentic architecture; Reid says agentic architectures would currently "reduce the quality of Fin" on Q&A.

## Evidence
- Backtests that looked good sometimes underperformed in production.
- Model upgrades contributed only a few points of the >30 pp resolution-rate increase since launch (rest from system engineering). Honeycomb case study: resolution rate rose ~1 pp per month (https://honeycomb.io/resources/case-studies/how-honeycomb-helped-intercom-observe-and-operate-fin-ai).
- Haiku gave poor summarisation; replaced by a self-trained encoder-decoder and fine-tuned Qwen-3.
- Asked about LLM judges, guests did not address them directly.

## Limitations and criticisms
Interview claims, not a written methodology. Third-party note: Intercom changed the resolution-rate denominator (excluding "Fin Constrained" conversations), which can raise the headline rate (https://myaskai.com/blog/how-to-improve-intercom-fin-resolution-rate; secondary).

## Relevance to agent evaluation
A strong practitioner statement that online A/B on a user-judged outcome beats offline evals for customer-facing agents at scale; offline evals filter, production decides.
