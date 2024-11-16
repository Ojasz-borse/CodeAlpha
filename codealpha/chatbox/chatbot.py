import random
import nltk
from transformers import pipeline
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary data for NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Rule-based chatbot function
def simple_chatbot(user_input):
    greetings = ["hello", "hi", "hey", "howdy"]
    farewells = ["bye", "goodbye", "see you", "later"]
    general_responses = [
        "I'm here to help!",
        "Tell me more.",
        "I'm listening.",
        "That's interesting!",
    ]

    user_input = user_input.lower()

    if any(greeting in user_input for greeting in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey!"])
    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Take care."
    else:
        return random.choice(general_responses)

# NLP-enhanced chatbot function with NLTK
def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    return tokens

def nlp_chatbot(user_input):
    tokens = preprocess_text(user_input)
    if "weather" in tokens:
        return "I can’t provide weather updates right now, but you can check your local forecast!"
    elif "name" in tokens:
        return "I’m a chatbot created to help you!"
    else:
        return "I'm here to assist with your questions."

# Transformer-based conversational chatbot using transformers
def conversational_chatbot(user_input):
    chatbot_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")
    response = chatbot_pipeline(user_input)
    return response[0]['generated_text']

# Main program to interact with the chatbot
if __name__ == "__main__":
    print("Select chatbot type:")
    print("1 - Simple rule-based chatbot")
    print("2 - NLP-enhanced chatbot")
    print("3 - Conversational chatbot with transformers")
    
    chatbot_type = input("Enter your choice (1/2/3): ")

    if chatbot_type == '1':
        print("Chatbot: Hi! This is the simple rule-based chatbot. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye! Take care.")
                break
            response = simple_chatbot(user_input)
            print("Chatbot:", response)

    elif chatbot_type == '2':
        print("Chatbot: Hi! This is the NLP-enhanced chatbot. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye! Take care.")
                break
            response = nlp_chatbot(user_input)
            print("Chatbot:", response)

    elif chatbot_type == '3':
        print("Chatbot: Hi! This is the conversational chatbot with transformers. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye! Take care.")
                break
            response = conversational_chatbot(user_input)
            print("Chatbot:", response)

    else:
        print("Invalid choice. Please restart the program and select a valid option.")
