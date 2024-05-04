# ADR 1: Choice of Speech-to-Text Service

## Decision
We will utilize Google Cloud Speech-to-Text for converting live audio to text over a local Python library.

## Rationale
Google Cloud Speech-to-Text offers high accuracy, supports multiple languages and dialects, and handles noisy environments well. It operates in real-time, which is crucial for the project's need to process live lectures. Using a cloud service also alleviates the load on local systems, avoiding the need for extensive local processing capabilities. The decision against a local library stems from the potential limitations in speech recognition accuracy and the intensive resources required for running speech recognition locally.

## Status
Proposed

## Consequences
By choosing a cloud-based service, we reduce the complexity of local setups and avoid demanding hardware requirements on the client side. However, this decision incurs ongoing operational costs and introduces a dependency on internet connectivity and external service availability.
