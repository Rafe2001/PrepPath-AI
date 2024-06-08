import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


llm = ChatGroq(temperature=0,groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")

prompt = ChatPromptTemplate.from_template(
    """
    You are an intelligent and highly knowledgeable assistant. 
    Your task is to provide accurate and concise answers to questions based on the given context. 
    Ensure your responses are directly relevant to the questions asked.
       
    <context>
    {context}
    </context>
    Questions: {input}
    
    """
)


embedd_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


def load_documents():
    loader = PyPDFDirectoryLoader("data")
    return loader.load()


# Function to generate vector embeddings from documents
def generate_vector_embeddings(docs, embedd_model):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    documents = text_splitter.split_documents(docs)
    vectors = Chroma.from_documents(documents, embedd_model)
    return vectors


# Function to generate a response based on user input
def generate_response(llm, prompt, user_input, vectors):
    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    retriever = vectors.as_retriever(search_kwargs={"k": 3})
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": user_input})
    return response['answer']



def main():
    docs = load_documents()
    vectors = generate_vector_embeddings(docs, embedd_model)
    user_input = input("Enter your question: ")
    response = generate_response(llm, prompt, user_input, vectors)
    print(response)


if __name__ == "__main__":
    main()
