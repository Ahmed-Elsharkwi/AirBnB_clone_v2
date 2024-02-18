#!/usr/bin/python3
"""
Web server
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():

    """ print Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show():
    """ print HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """ print C <text> """
    return "C {}".format(text.replace('_', " "))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text):
    """ print python <text> """
    return "Python {}".format(text.replace('_', " "))


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """ print n """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def show_number_html(n):
    """ print html template """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def show_number_html_odd_or_even(n):
    """ print html template """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)