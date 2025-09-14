import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load PDF
pdf_path = "data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf"
doc_text = ""

with fitz.open(pdf_path) as pdf:
    for page in pdf:
        doc_text += page.get_text()

# Split text into chunks for embeddings
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=50
)
chunks = text_splitter.split_text(doc_text)

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store in FAISS
db = FAISS.from_texts(chunks, embeddings)
db.save_local("faiss_index")

print("✅ PDF processed and FAISS index created!")
