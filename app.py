import os
from flask import Flask, render_template, redirect, request, jsonify
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from main import generate_vector_embeddings, generate_response, load_documents


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


app = Flask(__name__)



llm = ChatGroq(temperature=0,
               groq_api_key=groq_api_key, 
               model_name="mixtral-8x7b-32768")


prompt = ChatPromptTemplate.from_template(
    """
    You are an intelligent and highly knowledgeable interview preparation assistant. 
    Your task is to provide accurate and concise answers to questions based on the given context. 
    Ensure your responses are directly relevant to the questions asked.
       
    <context>
    {context}
    </context>
    Questions: {input}
    
    """
)

embedd_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


docs = load_documents()
vectors = generate_vector_embeddings(docs, embedd_model)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Generate response
    answer = generate_response(llm, prompt, question, vectors)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)