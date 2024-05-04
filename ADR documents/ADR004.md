# ADR 4: Database Selection for Storing Processed Data

## Decision
We will use MongoDB, accessed through PyMongo, for storing and managing the lecture content and metadata.

## Rationale
MongoDB is chosen for its schema-less nature, which provides flexibility in storing diverse data types that our application will handle, such as text, metadata, and summaries. PyMongo facilitates easy and efficient interaction with the MongoDB database from Python applications. This decision supports rapid development and iteration of database schemas as project requirements evolve.

## Status
Proposed

## Consequences
The schema-less nature of MongoDB offers flexibility but may lead to less data consistency and could complicate data integrity checks. It also requires careful design to optimize performance and manage data effectively.
