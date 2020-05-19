import os
from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "Response from flask on " + os.environ.get('PORT')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=8000)