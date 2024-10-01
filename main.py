from flask import Flask, render_template, request, jsonify
import os
from one import get_message, chatbot_response  # Import the chatbot response function

app = Flask(__name__)

port = int(os.getenv('PORT', 4000))

@app.route('/')
def hello():
    message = get_message()
    return render_template('index.html', message=message)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('user_message')  # Get user message from form data
    response = chatbot_response(user_message)  # Get response from the chatbot
    return jsonify({'response': response})  # Return response as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)