#!/usr/bin/python3
""" Status of the API.

"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ This function checks the status of the API.
    Return: The status OK.

    """
    return jsonify({"Status": "Ok"})
