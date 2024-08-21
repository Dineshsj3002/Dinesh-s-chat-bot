import streamlit as st
import google.generativeai as genai

st.title("Welcome to Dinesh's Chat")

genai.configure(api_key = "AIzaSyD4-b8tfOmAj72fxTEGBA9uizXFufmzqSQ")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message(text)

if st.button("Click Me")
st.write(response.text)
