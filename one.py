# one.py

# Import the necessary libraries
from sentence_transformers import SentenceTransformer
import faiss  # For vector similarity search
import numpy as np

# Load the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define the text for all four yatras in a more structured format
yatra_data = {
    'kailash_manasarovar': {
        'overview': [
            "The Kailash Manasasarovar is a sacred pilgrimage site, highly revered in Hindu culture."
        ],
        'faqs': [
            "Participants should be prepared for the physical challenges of the trip."
        ]
    },
    'himalayas': {
        'overview': [
            "The Himalayas offer a unique opportunity to experience the sacred energies of the mountains."
        ],
        'inquiries_and_registration': [
            "To learn more about registration, please visit our official website."
        ]
    },
    'southern_sojourn': {
        'overview': [
            "The Southern Sojourn takes you through India's sacred spaces."
        ],
        'spiritual_practices': [
            "The journey includes daily meditations and visits to sacred sites."
        ],
        'accommodations': [
            "Accommodation is provided in guesthouses during the yatra."
        ],
        'cost': [
            "Cost details vary and can be obtained from the Isha Sacred Walks team."
        ],
        'itinerary': [
            "The itinerary includes various sites of spiritual significance."
        ]
    },
    'kashi_krama': {
        'overview': [
            "Kashi Krama by Isha Sacred Walks offers a profound spiritual experience."
        ],
        'spiritual_practices': [
            "The sojourn involves meditations and rituals in the ancient city."
        ],
        'cost': [
            "Cost details vary depending on the package and year."
        ],
        'itinerary': [
            "The itinerary covers significant spiritual sites in the ancient city."
        ]
    },
    'common': {
        'registration': [
            "Participants can register on the official website."
        ],
        'cost': [
            "Cost details vary depending on the package and year."
        ]
    }
}

# Creating indices based on the new structure
index_data = {}
for yatra, sections in yatra_data.items():
    segments = []
    for section, texts in sections.items():
        segments.extend(texts)
    vectors = model.encode(segments)
    index = faiss.IndexFlatL2(vectors.shape[1])  # L2 distance
    index.add(np.array(vectors))  # Add vectors to the index
    index_data[yatra] = (index, segments)  # Store index and segments

# Modify the search function to handle structured data
def search_yatra(query, yatra, k=3):
    # Flatten the sections and concatenate them for the search
    index, segments = index_data[yatra]
    query_vector = model.encode([query])  # Encode the query
    distances, indices = index.search(np.array(query_vector), k)  # Search for top-k results

    # Combine top results
    combined_answer = " ".join([segments[idx] for idx in indices[0]])
    return combined_answer

# Function to determine which yatra the user is asking about
def identify_yatra(query):
    if 'himalayas' in query.lower() or 'himalaya' in query.lower():
        return 'himalayas'
    elif 'kailash' in query.lower() or 'kailas' in query.lower() or 'manasarovar' in query.lower():
        return 'kailash_manasarovar'
    elif 'southern' in query.lower():
        return 'southern_sojourn'
    elif 'kashi' in query.lower():
        return 'kashi_krama'
    else:
        return None  # If no yatra is identified

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
                    common_response = " ".join(yatra_data['common']['registration'])
                elif 'cancel' in query.lower() or 'cancellation' in query.lower():
                    common_response = "To cancel your registration, please contact customer service."
                elif 'enquiry' in query.lower() or 'contact' in query.lower():
                    common_response = "For inquiries, please reach out to support@ishasacredwalks.com."
                elif 'cost' in query.lower() or 'price' in query.lower():
                    common_response = " ".join(yatra_data['common']['cost'])
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