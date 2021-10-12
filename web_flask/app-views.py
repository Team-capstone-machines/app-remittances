#!/usr/bin/python3
"""  """

from flask import Flask, render_template, make_response
from flask.json import jsonify


app = Flask(__name__)


@app.route('/sender', strict_slashes=False)
def sender():
    """  """
    return render_template('sender.html')


@app.errorhandler(404)
def not_found(error):
    """  """
    return render_template('not_found.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
