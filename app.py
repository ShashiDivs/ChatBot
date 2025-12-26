import streamlit as st
from config import MODEL
from tutors.base_tutor import PythonnClassBot
from tutors.java_tutor import JavaClassBot
from chatbot.engine import ChatBot
from dotenv import load_dotenv
import os
import logging

api_key = st.secrets.get('GROQ_API_KEY') or os.getenv('GROQ_API_KEY')

logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('Bot Logging')

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


tutor_choice = st.sidebar.selectbox(
    "Select the Programming Language",
    options = ["Python", "Java"],
    index=0
)

# create objects
#tutor = PythonnClassBot()


if tutor_choice == "Python":
    tutor = PythonnClassBot()
    logger.info("Python has been chosen")
else:
    tutor = JavaClassBot()
    logger.info("Python has been chosen")

st.sidebar.success(f"Active Tutor is: {tutor_choice}")

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



