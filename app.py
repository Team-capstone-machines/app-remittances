#!/usr/bin/python3
"""  """

from flask import Flask, render_template, request

app = Flask(__name__)


app.route('/', strict_slashes=False)
def root():
    """  """
    return "Success"


@app.route('/sender', methods=['GET', 'POST'], strict_slashes=False)
def sender():
    """  """
    """ This function takes the methods GET and POST
    sent from an HTML page of the sender.
    """
    # This condition is to display an HTML page of the sender.
    if request.method == 'GET':
        return render_template('sender.html')


@app.route('/receiver', strict_slashes=False)
def receiver():
    """ This function display an HTML page of the receiver.
    Return: the HTML file.
    """
    return render_template('receiver.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
