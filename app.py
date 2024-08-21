import streamlit as st
import google.generativeai as genai

st.title("Welcome to Dinesh's Chat")

api_key = "AIzaSyD4-b8tfOmAj72fxTEGBA9uizXFufmzqSQ" 
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

text = st.text_input("Enter your question")

if text:
    try:
        response = chat.send_message(text)
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a question to get a response.")
