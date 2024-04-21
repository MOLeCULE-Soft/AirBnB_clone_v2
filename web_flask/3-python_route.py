#!/usr/bin/python3
"""Hello Flask"""
from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return 'Python {}'.format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
