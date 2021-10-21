#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/sender', strict_slashes=False)
def sender():
    return "Test"

if __name__ == '__main__':
    app.run(debug=True)