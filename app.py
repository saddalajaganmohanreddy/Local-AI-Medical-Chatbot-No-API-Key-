import streamlit as st
from chatbot import medical_chatbot

st.set_page_config(page_title="Medical AI Chatbot", page_icon="💊")

st.title("💊 AI Medical Chatbot")
st.write("Enter a medical question to receive AI-powered answers from the local knowledge base.")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input.strip() != "":
        # Get answer from chatbot
        answer = medical_chatbot(user_input)
        # Append to history
        st.session_state.history.append({"user": user_input, "bot": answer})
    else:
        st.warning("Please type a question first!")

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")
