from flask import Flask, render_template  # Import render_template to render HTML files
import os
from one import get_message  # Importing get_message() from one.py

app = Flask(__name__)

port = int(os.getenv('PORT', 4000))

@app.route('/')
def hello():
    message = get_message()  # Calling the function from one.py
    return render_template('index.html', message=message)  # Render index.html and pass the message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)  # Enable debug mode