# PrepPath AI Interview Assistant

PrepPath AI is an intelligent interview assistant designed to help users prepare for job interviews. It leverages open source Mixtral-8x7b-32768 LLM through Groq API, to provide accurate and relevant answers to a wide range of interview questions.

![image](https://github.com/Rafe2001/PrepPath-AI/assets/108533597/3c5e5b19-974a-4123-b422-0bd9ecf57b16)
![image](https://github.com/Rafe2001/PrepPath-AI/assets/108533597/3a07b5c8-db8a-49c3-a0e7-4c4307c8b56c)


## Features

- **Intelligent Question-Answering**: PrepPath AI uses state-of-the-art LLM mixtral-8x7b-32768, to understand and answer user questions with precision.
- **User-Friendly Interface**: The web-based interface makes it easy for users to interact with the assistant and receive instant responses.
- **Wide Range of Topics**: Whether it's technical questions, behavioral scenarios, or industry-specific inquiries, PrepPath AI can handle them all.
- **Customizable Prompt Templates**: Users can customize the prompts to tailor the responses to their specific needs and contexts.
- **Scalable Architecture**: The application is built using Flask and LangChain, ensuring scalability and robust performance.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- LangChain
- GoogleGenerativeAIEmbeddings
- Groq API
- Chroma

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rafe2001/PrepPath-AI.git
   cd PrepPath-AI
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   ```bash
   export GROQ_API_KEY=your_groq_api_key
   export GOOGLE_API_KEY=your_google_api_key
   ```

### Usage

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter your interview questions in the input field and click "Ask" to receive responses from PrepPath AI.

## Contributing

Contributions are welcome! If you'd like to contribute to PrepPath AI, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/yourusername/langchain) - A powerful natural language processing library.
- [Google Generative AI Embeddings](https://github.com/yourusername/google-generative-ai-embeddings) - State-of-the-art embeddings for semantic analysis.
- [Chroma](https://github.com/yourusername/chroma) - Efficient document embedding generation.
- [Groq API](https://github.com/yourusername/groq-api) - An API for accessing the Groq knowledge base.
