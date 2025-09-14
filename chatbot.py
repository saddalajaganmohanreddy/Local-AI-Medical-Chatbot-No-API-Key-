from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

# Load FAISS index
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Load local LLM
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def medical_chatbot(query):
    docs = db.similarity_search(query, k=3)  # top 3 related chunks
    context = " ".join([d.page_content for d in docs])
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    result = generator(prompt, max_length=200, do_sample=True)
    return result[0]['generated_text']
