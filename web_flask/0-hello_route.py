#!/usr/bin/python3
"""
    Starts a Flash web application
"""
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """
        Prints `Hello HBNB!` when accessing root of website
    """
    return 'Hello HBNB!'

app.run(host='0.0.0.0', port='5000')
