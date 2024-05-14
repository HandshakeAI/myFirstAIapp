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
    if not ((openai_api_key.startswith('sk')) and len(openai_api_key) == 56):
        st.warning('Enter a valid API key', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')

    # Sidebar toggles setup
    chosen_model = ""
    selected_model = st.sidebar.selectbox('Choose an OpenAI model', ['GPT-3.5', 'GPT-4'])
    if selected_model == 'GPT-3.5':
        chosen_model = "gpt-3.5-turbo"
    elif selected_model == 'GPT-4':
        chosen_model = "gpt-4"
    chosen_temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=1.0, step=0.01)
    chosen_max_length = st.sidebar.slider('max_length', min_value=32, max_value=10000, value=2000, step=8)
    chosen_number_of_samples = st.sidebar.slider('Number of samples', min_value=1, max_value=3, value=1, step=1)

    st.sidebar.button('Clear Chat History', on_click = clear_chat_history)

# main window title and description
st.subheader('Future Forecast Generator')
st.text('Enter an innovation in the window below and receive a future forecast')
st.text('which lists the opportunities and dangers related to that innovation as')
st.text('well as a story illustrating how this innovation can impact the')
st.text('life of a student in Nigeria 10 years from now.')

if "messages" not in st.session_state.keys():
    st.session_state["messages"] = [{"role": "assistant", "content": "Provive a subject matter to generate a future forecast on."}]

# Show the relevant content from the database on the frontend
for messages in st.session_state.messages[2:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Make a button which clears teh converation and starts a new chat
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Provive a subject matter to generate a future forecast on."}]
