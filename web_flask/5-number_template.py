""" Flask app that return hello HBNB"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "“Hello HBNB!”"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return "“HBNB”"

@app.route("/c/<text>", strict_slashes=False)
def display_C_(text):
    return "C {}".format(text.replace("_", " "))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python_(text=""):
    if text == "":
        return "Python is cool"
    else:
        return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def display_num_template(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")