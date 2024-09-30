from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define the text for all four yatras
yatra_data = {
    'kailash_manasarovar': {
        'overview': ["The Kailash Manasasarovar."],
        'faqs': ["Participants should be carried throughout the trip."]
    },
    'himalayas': {
        'overview': ["The Himalayas experience the sacred energies of the Himalayas."],
        'inquiries_and_registration': ["To learn more about reserving their place."]
    },
    'southern_sojourn': {
        'overview': ["The Southern Sojourn explores India's sacred spaces."],
        'spiritual_practices': ["The journey includes daily meditation at sacred sites."],
        'accommodations': ["Accommodation is provided during the yatra."],
        'cost': ["Cost details vary. Contact the Isha Sacred Walks team."],
        'itinerary': ["The itinerary includes places of spiritual significance."]
    },
    'kashi_krama': {
        'overview': ["Kashi Krama by Isha Sacred Walks offers a spiritual experience."],
        'spiritual_practices': ["The sojourn involves meditations."],
        'cost': ["Cost details vary depending on the package and year."],
        'itinerary': ["The itinerary covers spiritual places in the ancient city."]
    },
    'common': {
        'registration': ["Participants can register on the official website."],
        'cost': ["Cost details vary depending on the package and year."]
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
    index, segments = index_data[yatra]
    query_vector = model.encode([query])  # Encode the query
    distances, indices = index.search(np.array(query_vector), k)  # Search for top-k results
    combined_answer = " ".join([segments[idx] for idx in indices[0]])
    return combined_answer

# Function to determine which yatra the user is asking about
def identify_yatra(query):
    if 'himalayas' in query.lower():
        return 'himalayas'
    elif 'kailash' in query.lower():
        return 'kailash_manasarovar'
    elif 'southern' in query.lower():
        return 'southern_sojourn'
    elif 'kashi' in query.lower():
        return 'kashi_krama'
    else:
        return None  # If no yatra is identified

# Define the chatbot route and logic
@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        query = request.form["query"]
        identified_yatra = identify_yatra(query)
        
        if not identified_yatra:
            response = "Please specify which yatra you are asking about: Himalayas, Kailash Manasarovar, Southern Sojourn, or Kashi Krama."
        else:
            response = search_yatra(query, identified_yatra)
            if not response:
                response = "Sorry, I couldn't find an answer to your question."
        return render_template("index.html", query=query, response=response)
    return render_template("index.html", query="", response="")


#html template
"""
<html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot - Isha Sacred Walks</title>
</head>
<body>
    <div style="
    margin: auto;
    padding: 30px;
    width: 50%;
    border: 2px solid black;
    border-radius: 35px;
">
    <h1 style="
    text-align: center;
">Isha Sacred Walks Chatbot</h1><label for="query">Type your question</label><br><textarea id="query" name="query" rows="4" cols="50" style="
    width: 95%;
    border: 2px solid black;
    border-radius: 10px;
    padding: 10px;
    height: auto;
">{{ query }}</textarea><br><br><input type="submit" value="Submit"><h2>Response:</h2><p>{{ response }}</p><table>
    
    <form method="POST"></form>
        
        
        
    
    
    
</table>
        </div></body></html>

        """









# Run the app on port 8000
if __name__ == "__main__":
    app.run(port=8000)
