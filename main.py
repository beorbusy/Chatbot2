# main.py

from flask import Flask, render_template
from one import chatbot  # Importing the chatbot function from one.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render index.html

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode