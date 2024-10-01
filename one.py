# one.py

# Sample data structure to hold responses (this should be defined according to your actual data)
yatra_data = {
    'common': {
        'registration': ["To register for a sojourn, please visit our website or contact customer service."],
        'cancellation': ["To cancel your registration, please contact our support team at least 48 hours in advance."],
        'enquiries': ["For enquiries, you can reach us at info@ishasacredwalks.org."],
        'sadhguru': ["Sadhguru is the founder of Isha Foundation and is known for his wisdom and teachings."],
        'cost': ["The cost varies depending on the sojourn. Please check our website for detailed pricing."],
    }
}

# Dummy function to identify yatra from the query
def identify_yatra(query):
    yatra_keywords = {
        'Kailash Manasarovar': ['kailash', 'manasarovar'],
        'Himalayas': ['himalayas'],
        'Southern Sojourn': ['southern', 'sojourn'],
        'Kashi Krama': ['kashi', 'krama']
    }
    
    for yatra, keywords in yatra_keywords.items():
        if any(keyword in query.lower() for keyword in keywords):
            return yatra
    return None

# Dummy function to search for yatra-specific answers
def search_yatra(query, current_yatra):
    responses = {
        'Kailash Manasarovar': ["Kailash Manasarovar is a sacred pilgrimage and usually takes about 12 days."],
        'Himalayas': ["The Himalayas sojourn offers breathtaking views and is usually 6 days long."],
        'Southern Sojourn': ["The Southern Sojourn takes you through beautiful temples and culture over 6 days."],
        'Kashi Krama': ["Kashi Krama includes a visit to the holy city of Varanasi and lasts for 4 days."]
    }
    
    return responses.get(current_yatra, [])

# Chatbot function to process user input
def chatbot(query):
    # Check for common questions first
    common_topics = ['register', 'registration', 'cancel', 'cancellation', 'enquiry', 'contact', 'cost', 'price']
    current_yatra = None

    # Check for common responses
    for topic in common_topics:
        if topic in query.lower():
            if 'register' in query.lower() or 'registration' in query.lower():
                return " ".join(yatra_data['common']['registration'])
            elif 'cancel' in query.lower() or 'cancellation' in query.lower():
                return " ".join(yatra_data['common']['cancellation'])
            elif 'enquiry' in query.lower() or 'contact' in query.lower():
                return " ".join(yatra_data['common']['enquiries'])
            elif 'sadhguru' in query.lower() or 'guru' in query.lower():
                return " ".join(yatra_data['common']['sadhguru'])
            elif 'cost' in query.lower() or 'price' in query.lower():
                return " ".join(yatra_data['common']['cost'])

    # Try to identify the yatra from the query
    identified_yatra = identify_yatra(query)
    if identified_yatra:
        current_yatra = identified_yatra

    # If no specific yatra is mentioned, prompt the user
    if not current_yatra:
        return "Please specify which yatra you are asking about: Himalayas, Kailash Manasarovar, Southern Sojourn, or Kashi Krama."

    # Search for an answer within the identified or current yatra
    response = search_yatra(query, current_yatra)
    if response:
        return response[0]  # Return the first response
    else:
        return "Sorry, I couldn't find an answer to your question."