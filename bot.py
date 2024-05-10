import nltk
import random
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you', ['I am good, thank you!', 'Feeling great, thanks!', 'I am doing well!']),
    (r'what is your name', ['I am just a chatbot.', 'You can call me Chatbot.', 'I am your friendly chatbot.']),
    (r'what can you do', ['I can chat with you and answer your questions.', 'I am here to assist you with any queries you have.', 'I can engage in conversation and provide information.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'.*', [" That's interesting.", 'Tell me more!', "I'm not sure I understand."]),
]


chatbot = Chat(patterns, reflections)


def start_chat():
    print("Welcome to the Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:", chatbot.respond(user_input))


start_chat()

