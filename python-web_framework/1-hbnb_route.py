#!/usr/bin/python3

"""
This module starts a web aplication using Flask
It defines routes and handlers for different URLs to demonstrate
the basic usage of the Flask web framework.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    A route handler for the root URL '/'. It returns a greeting message.

    Returns:
        str: Greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """
    A route handler for the URL '/hbnb'. It returns a message "HBNB".

    Returns:
        str: Message "HBNB".
    """
    return "HBNB"


if __name__ == '__main__':
    """
    Main entry point of the script. Starts the Flask app.
    """
    app.run(host='0.0.0.0', port=5000)
