# ADR 2: Selection of Language Model API

## Decision
We will integrate GPT-4 Turbo API for text summarization and note generation, with the flexibility to switch to other APIs like Google Gemini or Meta Llama as needed.

## Rationale
GPT-4 Turbo is chosen for its advanced capabilities in generating coherent and contextually accurate text summaries. The decision to allow swapping between APIs provides flexibility in managing costs and adapting to changes in technology or service levels. GPT-4 Turbo's balance of cost and performance makes it suitable for our initial setup.

## Status
Proposed

## Consequences
This flexibility allows for scalability and adaptability of services based on performance evaluations and cost considerations. It may, however, introduce complexity in API management and integration.
