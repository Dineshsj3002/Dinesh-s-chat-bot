import requests
import streamlit as st
import base64
import io
from PIL import Image
import os

def get_img_as_base64(file_path):
    if not os.path.isfile(file_path):
        st.error(f"File {file_path} not found.")
        return None
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set the background image
img = get_img_as_base64("download.jpg")
if img:
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/jpeg;base64,{img}");
        background-size: cover;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Define API URL and headers
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {os.getenv('HF_dhrGuqmARKBXWJqWtxxMfIbTLyoRokstJI')}"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return None

# User input
prompt = st.text_input('Enter prompt:')

# Generate image on button click
if st.button('Generate'):
    if prompt:
        image_bytes = query({"inputs": prompt})
        if image_bytes:
            try:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image)
            except Exception as e:
                st.error(f"Error displaying image: {e}")
    else:
        st.warning("Please enter a prompt.")
