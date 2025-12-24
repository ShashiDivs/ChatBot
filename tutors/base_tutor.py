from abc import ABC, abstractmethod

class Tutor(ABC):
    """ Abstract base class"""

    @abstractmethod
    def get_system_prompt(self) -> str:
        pass

    @abstractmethod
    def greet(self) -> str:
        pass



class PythonnClassBot(Tutor):
    """ This will give you Inheritence and even further Polymorphism"""

    def get_system_prompt(self) -> str:

        return """
You are friendly and patient Python Class Tutor and teaching the pillars of OOP:
- Inheritence
- Encapsulation
- Abstraction
- Polymorphism

Explain concpets simplistic way for beginners.
Always include short, clear, and runnable Python code examples.
Use even real-life analogies when possible.
Keep responses concise and focused
If asked about other topics, response politely and redirect to OOP concepts.
"""


    def greet(self) -> str:
        return (
            "Hi, I'm your Python Class Bot \n"
            "I can help you understand - **Inheritence**, **Encapsulation**, **Abstraction**, and **Polymorphism** with simple examples \n"
            "What You want learn out of these??"
        )