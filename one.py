# one.py

# Function to simulate getting a message (replace this with your actual logic)
def get_message():
    return "Hello from one.py! How can I assist you today?"

# Chatbot function
def chatbot():
    print("Namaskaram,\nThis is an automated system to answer your questions regarding Isha Sacred Walks sojourns.\n"
          "Kailash Manasarovar?\nHimalayas?\nSouthern Sojourn?\nKashi Krama?\n")
    current_yatra = None

    while True:
        query = input("\nYour question (type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break

        # First check for common questions like registration, cancellation, etc.
        common_topics = ['register', 'registration', 'cancel', 'cancellation', 'enquiry', 'contact', 'cost', 'price']

        common_response = None
        for topic in common_topics:
            if topic in query.lower():
                # Match the query to the correct common topic and return the corresponding response
                if 'register' in query.lower() or 'registration' in query.lower():
                    common_response = "You can register by visiting our website."
                elif 'cancel' in query.lower() or 'cancellation' in query.lower():
                    common_response = "To cancel your registration, please contact customer service."
                elif 'enquiry' in query.lower() or 'contact' in query.lower():
                    common_response = "For inquiries, please reach out to support@ishasacredwalks.com."
                elif 'sadhguru' in query.lower() or 'guru' in query.lower():
                    common_response = "Sadhguru is a guiding force in our sojourns."
                elif 'cost' in query.lower() or 'price' in query.lower():
                    common_response = "The cost varies depending on the yatra you choose."
                break  # Exit the loop once a match is found

        # If a common response is found, return it and skip the yatra-specific search
        if common_response:
            print("\nAnswer:")
            print(common_response)
            continue  # Skip to the next query

        # Try to identify the yatra from the query
        identified_yatra = identify_yatra(query)
        if identified_yatra:
            current_yatra = identified_yatra

        # If no specific yatra is mentioned, ask the user
        if not current_yatra:
            print("Please specify which yatra you are asking about: Himalayas, Kailash Manasarovar, Southern Sojourn, or Kashi Krama.")
            continue

        # Search for an answer within the identified or current yatra
        response = search_yatra(query, current_yatra)
        if response:
            print("\nAnswer:")
            print(response)
        else:
            print("Sorry, I couldn't find an answer to your question.")

# Start the chatbot (this is for command line use, not for Flask)
# chatbot()  # Uncomment this line if you want to run the chatbot in the terminal