from groq import Groq
from typing import List, Dict
import logging
from config import MODEL

logger = logging.getLogger('ChatBot')

class ChatBot:

    """
    This class will give you the experinece of Encapsulation (_model) using this
    we hide the implementation details
    """

    def __init__(self, api_key: str, model: str):

        self._client = Groq(api_key=api_key) # this is protected variable _
        self._model = model
        self.messages:  List[Dict[str,str]] = []
        logger.info(f"Chatbot initialized with mode {MODEL}")

    def add_system_message(self, content: str):
        self.messages.append({'role':"sytem", 'content':content})
        logger.debug('Sytem message added')
    
    def add_assistant_message(self, content: str):
        self.messages.append({'role':"assistant", 'content':content})
        logger.debug('Assistant message added')

    def get_streaming_response(self, user_input: str):
        """ Send user message and yield responsed through the chunks"""
        logger.info("User Question: %s", user_input)

        self.messages.append({'role': 'user', 'content': user_input})

        stream = self._client.chat.completions.create(
            model = self._model,
            messages=self.messages,
            stream=True,
            temperature=0.7
        )

        response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                response += content
                yield content

        self.messages.append({'role':"assistant", 'content':response})
