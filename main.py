from flask import Flask, request, jsonify
from one import chatbot  # Adjust as necessary to import your chatbot function

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chat():
    user_input = request.json.get('query')
    response = chatbot(user_input)  # Call the chatbot function with user input
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)