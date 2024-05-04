# ADR 3: Data Processing Framework

## Decision
We will use Apache Spark for preprocessing and structuring the text data obtained from lectures.

## Rationale
Apache Spark is chosen for its ability to handle large datasets efficiently due to its distributed nature. It excels in tasks that require fast processing speeds and can scale easily as data volume grows. The decision against using Python dataframes directly (e.g., via pandas) is based on their limitations in handling large-scale data efficiently.

## Status
Proposed

## Consequences
Apache Spark will enhance the system's capability to process data quickly and at scale. However, it requires a setup for distributed computing, which might increase the complexity of deployment and maintenance.
