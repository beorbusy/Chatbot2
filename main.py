import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import math

# Sentence transformers and FAISS imports
from sentence_transformers import SentenceTransformer
import faiss  # For vector similarity search
import numpy as np

# Load the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define the port for the server (Render will dynamically assign the port)
PORT = int(os.environ.get("PORT", 8000))

# Define the text for all four yatras
yatra_data = {
    'kailash_manasarovar': {
        'overview': [
            "The Kailash Manasarovar Sojourn is a 13/14-day profound spiritual journey starting and ending in Kathmandu, Nepal. It offers a unique pilgrimage to the sacred Mount Kailash and Lake Manasarovar."
        ],
        'fitness_and_health': [
            "Physical and mental fitness is crucial. Participants should start an exercise regime at least one month before the journey, including daily brisk walking or jogging for 5 km, and practicing Isha programs like Shambhavi Mahamudra Kriya, Isha Kriya, Hatha Yoga, or Shakthi Chalana Kriya."
        ],
    },
    'himalayas': {
        'overview': [
            "The Himalayas Sojourn is a profound spiritual journey organized by Isha Sacred Walks, offering powerful spiritual processes, satsangs, and the opportunity to experience the sacred energies of the Himalayas."
        ],
        'cost': [
            "Cost details vary depending on the package and year. For the most accurate and up-to-date pricing, visit the Isha Sacred Walks website or contact the Isha Sacred Walks team."
        ],
        'eligibility': [
            "Participants must have completed the Isha Inner Engineering program, including initiation into Shambhavi Mahamudra Kriya."
        ],
        'fitness_and_health': [
            "Participants should start a fitness regimen at least one month prior to the trip, including 5 km of daily brisk walking or jogging to prepare for high-altitude conditions (up to 13,000 feet)."
        ]
    },
    # Additional Yatras (same as your original structure)
}

# Function to handle search and chatbot interaction
def search_yatra(query, yatra, k=3):
    index, segments = index_data[yatra]
    query_vector = model.encode([query])  # Encode the query
    distances, indices = index.search(np.array(query_vector), k)  # Search for top-k results
    combined_answer = " ".join([segments[idx] for idx in indices[0]])
    return combined_answer

def chatbot():
    print("Namaskaram,\nThis is an automated system to answer your questions regarding Isha Sacred Walks sojourns.")
    current_yatra = None

    while True:
        query = input("\nYour question (type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break

        identified_yatra = identify_yatra(query)
        if identified_yatra:
            current_yatra = identified_yatra

        if not current_yatra:
            print("Please specify which yatra you are asking about.")
            continue

        response = search_yatra(query, current_yatra)
        if response:
            print("\nAnswer:")
            print(response)
        else:
            print("Sorry, I couldn't find an answer to your question.")

# HTTP Handler
class CalculatorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Chatbot Server is running")

if __name__ == "__main__":
    with HTTPServer(('0.0.0.0', PORT), CalculatorHandler) as httpd:
        print(f"Calculator server listening on port {PORT}")
        httpd.serve_forever()
