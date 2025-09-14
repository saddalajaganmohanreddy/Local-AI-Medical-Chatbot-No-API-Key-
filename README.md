# Local-AI-Medical-Chatbot-No-API-Key-
This project is a fully local AI-powered medical chatbot designed to answer medical questions based on a custom PDF knowledge base. Unlike typical chatbots, this system does not rely on external APIs or internet-based models, making it ideal for academic projects, offline usage, and privacy-sensitive environments.

# Local AI Medical Chatbot (No API Key)

## Overview
This project is a **Local AI Medical Chatbot** that allows users to ask medical questions and get answers based on a PDF knowledge base.  
✅ **Fully local** — no API keys or external cloud services are required.  
✅ **Retrieval-based** — uses FAISS for indexing and HuggingFace models for embeddings and language generation.  

## Features
- Ask medical questions based on your uploaded PDF knowledge base.  
- Uses **FAISS** for fast similarity search on the text chunks.  
- Uses **HuggingFace Transformers** for generating natural language answers.  
- Runs **entirely locally** without depending on any paid APIs.  
- Streamlit interface for easy web-based interaction.  

## Project Structure
medical-chatbot/
│
├── app.py # Streamlit web interface
├── chatbot.py # Chatbot logic and LLM integration
├── ingest.py # Process PDF and create FAISS index
├── requirements.txt # Required Python packages
├── commands.txt # Helpful terminal commands
├── faiss_index/ # Folder containing FAISS index (created after running ingest.py)
└── README.md # Project documentation
