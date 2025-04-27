# chatbot.py

import nltk
from nltk.chat.util import Chat, reflections

# You can skip this if already downloaded
nltk.download('punkt')

# Define chatbot conversation patterns
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["I'm an AI chatbot created using NLTK."]
    ],
    [
        r"what is AI ?",
        ["AI stands for Artificial Intelligence. It enables machines to mimic human intelligence."]
    ],
    [
        r"what is NLP ?",
        ["NLP stands for Natural Language Processing. It allows computers to understand human language."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How can I assist you today?"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help. Please tell me your issue."]
    ],
    [
        r"(.*) your creator ?",
        ["I was created by a Python developer using NLTK."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day."]
    ],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot
print("Hi! I'm your AI Chatbot. Type 'bye' or 'exit' to end the chat.\n")
chatbot.converse()
