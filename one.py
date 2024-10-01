# one.py

def get_message():
    return "Hello from Flask!"

def chatbot_response(user_input):
    user_input = user_input.lower()  # Normalize to lowercase
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm functioning as expected! How about you?"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created to assist you."
    else:
        return "Sorry, I don't understand that."