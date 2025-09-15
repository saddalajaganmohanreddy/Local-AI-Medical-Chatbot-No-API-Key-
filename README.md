# 🏥 Local AI Medical Chatbot (No API Key)

A **fully local AI-powered medical chatbot** that answers medical questions using a **custom PDF knowledge base**.
Unlike typical chatbots, this system **does not rely on external APIs** or internet-based models — making it ideal for **academic projects, offline usage, and privacy-sensitive environments**.

---

## 🚀 Overview

* ✅ **Fully local** — no API keys or cloud services required
* ✅ **Retrieval-based** — FAISS indexing + HuggingFace embeddings
* ✅ **Privacy-friendly** — all processing stays on your machine
* ✅ **User-friendly** — simple Streamlit interface

---

## ⚡ Features

* Upload **medical PDFs** as knowledge sources
* Ask **medical questions** and receive AI-generated answers
* Uses **FAISS** for fast similarity search across document chunks
* **HuggingFace Transformers** for embeddings & answer generation
* Runs **entirely offline**

---

## 📂 Project Structure

```
medical-chatbot/
│── app.py            # Streamlit web interface
│── chatbot.py        # Chatbot logic & LLM integration
│── ingest.py         # Process PDF and create FAISS index
│── requirements.txt  # Required Python packages
│── commands.txt      # Helpful terminal commands
│── faiss_index/      # Folder for FAISS index (created after running ingest.py)
└── README.md         # Project documentation
```

---

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/local-ai-medical-chatbot.git
   cd local-ai-medical-chatbot
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📘 Usage

1. **Ingest your PDF knowledge base**
   Place your medical PDFs in the project folder and run:

   ```bash
   python ingest.py
   ```

2. **Start the chatbot (Streamlit app):**

   ```bash
   streamlit run app.py
   ```

3. **Ask your questions!**
   Open the Streamlit link (default: `http://localhost:8501`) and chat with your AI doctor 🤖💬

---

## 🛠 Tech Stack

* **Python**
* **Streamlit** (web interface)
* **FAISS** (vector database for retrieval)
* **HuggingFace Transformers** (embeddings + text generation)

---

## 📌 Example Use Cases

* Academic projects
* Offline medical Q\&A systems
* Privacy-focused chatbot demos
* AI + NLP learning projects

---

## ⚠️ Disclaimer

This chatbot is intended for **educational purposes only**.
It should **not** be used for real medical diagnosis or treatment. Always consult a licensed medical professional.

---

