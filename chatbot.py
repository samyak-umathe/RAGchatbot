import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter         
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS    

st.set_page_config(page_title="RAG Chatbot", page_icon=":robot_face:")
st.title("C++ RAG Chatbot")
st.write("This chatbot uses Retrieval-Augmented Generation (RAG) to answer questions about C++ programming language based on the provided document.")

@st.cache_resource
def load_vectorstore():
    loader = TextLoader('C++_Introduction.txt', encoding='utf-8')
    documents = loader.load() 
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    finalDocuments = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(finalDocuments, embeddings)
    
    return db

db = load_vectorstore()

query = st.text_input("Ask a question about C++:")

if query:
    docs = db.similarity_search(query, k=3)
    st.subheader("Relevant Documents:")
    for i, doc in enumerate(docs):
        st.markdown(f"**Document {i+1}:**")
        st.write(doc.page_content)

        
        