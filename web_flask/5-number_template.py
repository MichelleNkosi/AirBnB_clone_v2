#!/usr/bin/python3
"""Starts a Flask web application with multiple routes"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns 'Hello HBNB!' when accessing the root route"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB' when accessing the /hbnb route"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Returns 'C ' followed by the text (replacing _ with space)"""
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Returns 'Python ' followed by the text (replacing _ with space)"""
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Returns '<n> is a number' only if n is an integer"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns an HTML page with the number if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

