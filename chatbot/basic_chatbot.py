# chatbot/basic_chatbot.py
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"Hi|Hello", ["Hello!", "Hi there!"]),
    (r"What is your name?", ["I am a chatbot."]),
    # Add more patterns and responses as needed
]

def chatbot():
    print("Chatbot is running...")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
 
