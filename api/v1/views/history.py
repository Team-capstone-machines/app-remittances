#!/usr/bin/python3
""" ResFul API to history.

"""

from api.v1.views import app_views
from flask import jsonify
from function_help import Encrypt
from models import storage


@app_views.route("/history", strict_slashes=False)
def history():
    """ This function do the action when requests the GET method of history.
    Return: The list with the history.

    """
    list_history = []
    # Request the information of the history table.
    _history = storage.all('History').values()
    # For loop to add the history in a list.
    for history in _history:
        if '_sa_instance_state' in history.__dict__:
            del history.__dict__['_sa_instance_state']
        list_history.append(history.__dict__)
    return jsonify(list_history)


@app_views.route(
    "/history/<phone_id>", strict_slashes=False)
def history_id(phone_id=None):
    """ This function do the action when requests the GET method and
    an ID of cell number of history.
    Return: The list with the history of that ID.

    """
    list_history = []
    # Request the information of the history table.
    _history = storage.all('History').values()
    # For loop to add the history in a list.
    for history in _history:
        if '_sa_instance_state' in history.__dict__:
            del history.__dict__['_sa_instance_state']
        if Encrypt(phone_id) == history.phone:
            list_history.append(history.__dict__)
    return jsonify(list_history)
