#!/usr/bin/python3
""" Flask app that return hello HBNB"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ say hello hbnb """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """ desplay hbnb"""
    return "“HBNB”"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
