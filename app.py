import streamlit as st
from config import MODEL
from tutors.base_tutor import PythonnClassBot
from chatbot.engine import ChatBot
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

st.set_page_config(page_title="Python Class Tutor")
st.title('Python Class Bot')
st.markdown("""
This app is built using python OOP concpets
            
Will teach these concepts 
- Inheritence
- Encapsulation
- Abstraction
- Polymorphism
""")

if not api_key:
    st.info("Please upddate your apikey in .env")
    st.stop()

# create objects
tutor = PythonnClassBot()
chat_engine = ChatBot(api_key=api_key, model=MODEL)


# Initialize chat history

if "messages" not in st.session_state:
    chat_engine.add_system_message(tutor.get_system_prompt())
    chat_engine.add_assistant_message(tutor.greet())
    st.session_state.messages = chat_engine.messages

# Display chat messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# user input
if prompt := st.chat_input("Ask about Inheritence, Encapsulation, Abstraction and Polymorphism...."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # streaming
    with st.chat_message('assistant'):
        response = st.write_stream(chat_engine.get_streaming_response(prompt))



