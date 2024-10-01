# one.py

def get_message():
    return "Hello from Flask!"

def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")  # Get user input
        user_input = user_input.lower()  # Normalize to lowercase

        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break  # Exit the loop
        elif "hello" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")
        elif "what is your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Uncomment the following line to run the chatbot in the console directly
# chatbot()