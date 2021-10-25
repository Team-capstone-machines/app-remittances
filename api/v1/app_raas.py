#!/usr/bin/python3
""" Flask application.

"""

from api.v1.views import app_views
from flask import Flask, jsonify
from flask.helpers import make_response

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(400)
def show_error(error):
    """ This function process the errors with the code 400.

    """
    list_errror = str(error).split(': ')
    # Conditions to handle the description of the errors.
    if list_errror[1] == 'Not a JSON':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing name':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing phone':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing cash':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing positive(+) or negative(-) sign':
        return make_response(jsonify({"error": list_errror[1]}), 400)


@app.errorhandler(404)
def show_error(error):
    """ This function process the errors with the code 404.

    """
    list_errror = str(error).split(': ')
    # Conditions to handle the description of the errors.
    if list_errror[1] == 'Phone id. Not found':
        return make_response(jsonify({"error": list_errror[1]}), 404)
    if list_errror[1] == 'Invalid amount. Cannot be processed':
        return make_response(jsonify({"error": list_errror[1]}), 404)


@app.errorhandler(413)
def show_error(error):
    """ This function process the errors with the code 413.

    """
    list_errror = str(error).split(': ')
    return make_response(jsonify({"error": list_errror[1]}), 413)


@app.errorhandler(422)
def show_error(error):
    """ This function process the errors with the code 422.

    """
    list_errror = str(error).split(': ')
    return make_response(jsonify({"error": list_errror[1]}), 422)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
