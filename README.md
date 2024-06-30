# Voc-Notes: A Free-to-use AI Notebook Tool

## Project Overview

This project aims to transform live lecture audio into structured, insightful educational content using state-of-the-art technology. The system captures live audio, converts it into text, preprocesses the data, summarizes it into concise class notes, stores the processed data, and finally visualizes the information for insights. The project leverages various technologies such as Google Cloud Speech-to-Text, Apache Spark, Groq LLMs, MongoDB, and Tableau to ensure efficiency and scalability.

## Architecture Decision Records (ADRs)

We have documented several key architectural decisions in our ADRs. These decisions are crucial for the development and future scalability of our project. You can find more details about each decision in the following ADRs:

- [ADR 1: Choice of Speech-to-Text Service](ADR/ADR001.md)
- [ADR 2: Selection of Language Model API](ADR/ADR002.md)
- [ADR 3: Data Processing Framework](ADR/ADR003.md)
- [ADR 4: Database Selection for Storing Processed Data](ADR/ADR004.md)
- [ADR 5: Data Visualization Tool](ADR/ADR005.md)

## System Components and Technologies Used

- **Streamlit** for UI (front-end)
- **Whisper AI** for high-quality audio capture
- **Google Cloud Speech-to-Text** for accurate transcription
- **PySpark** for efficient data preprocessing
- **Groq** for managing large language models
- **LLMs**: Mixtral-8x7b (32768 token size) & Llama3-70b (8192 token size) for advanced summarization
- **PyMongo** for data storage
- **Tableau** for data visualization

## Workflow Summary

1. **Audio Capture/Upload**: Users can either capture live lecture audio or upload an existing audio file using Streamlit for the front-end interface.
2. **Audio-to-Text Conversion**: The audio is converted into text using Google Cloud Speech-to-Text, chosen for its scalability and efficiency.
3. **Data Preprocessing**: The text data is cleaned and preprocessed using PySpark, removing stop words and tokenizing the text to prepare it for summarization.
4. **Text Summarization**: Using Mixtral-8x7b and Llama3-70b models through groq inference, the preprocessed text is summarized into concise class notes. Mixtral-8x7b handles large context chunks, while Llama3-70b combines the chunked results into coherent summaries.
5. **Data Storage**: The processed and summarized data is stored in MongoDB for efficient retrieval and scalability.
6. **Data Visualization**: Finally, the information is visualized using Tableau, providing insightful and structured educational content.

## Future Work

To enhance the Voc-Notes solution, several future improvements and expansions can be considered:

- **Multi-Language Support**: Extend support to multiple languages to cater to a diverse user base.
- **Real-Time Transcription**: Develop real-time transcription capabilities for live lecture note-taking.
- **AI Model Optimization**: Continuously update and optimize AI models for better performance and lower resource consumption.

## Contributing

We welcome contributions from developers and researchers interested in educational technology and data processing. If you would like to contribute to the project, please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
