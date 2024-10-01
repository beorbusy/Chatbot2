# main.py

from flask import Flask, render_template  # Import render_template to render HTML files
import os
from one import chatbot  # Importing the chatbot function from one.py

app = Flask(__name__)

# Get the port from environment variables, defaulting to 4000
port = int(os.getenv('PORT', 4000))

@app.route('/')
def home():
    return render_template('index.html')  # Render index.html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)  # Enable debug mode