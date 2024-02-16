#!/usr/bin/python3
""" Flask app that return hello HBNB"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ say hello hbnb """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """ desplay hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C_(text):
    """ desplay ur text """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python_(text=""):
    """ desplay python is $"""
    if text == "":
        return "Python is cool"
    else:
        return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    """ desplay only numbers """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_num_template(n):
    """ rednder numbers on html """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_num_template_even_odd(n):
    """ show if the number is even or odd """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
