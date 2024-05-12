# dependencies
import streamlit as st 
from openai import OpenAI

# Sidebar setup
with st.sidebar:
    # Title displayed on the side bar
    st.title('Enter your model parameters here')
    # Request OpenAI API key
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    # Check that the key provided starts with sk and has 40 characters
    if not ((openai_api_key.startswith('sk')) and len(openai_api_key) == 51):
        st.warning('Enter a valid API key', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')
