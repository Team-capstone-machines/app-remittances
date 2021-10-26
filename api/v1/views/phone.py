#!/usr/bin/python3
""" ResFul API to phones.

"""

from api.v1.views import app_views
from flask import jsonify
from function_help import Encrypt
from models import storage


@app_views.route("/phones", strict_slashes=False)
def phones():
    """ This function do the action when requests the GET method of phones.
    Return: The list with the phones and your encrypted phone.

    """
    list_phones = []
    # Request the information of the phones table.
    _phones = storage.all('Phones').values()
    # For loop to add the phone in a list.
    for phone in _phones:
        if '_sa_instance_state' in phone.__dict__:
            del phone.__dict__['_sa_instance_state']
        list_phones.append(phone.__dict__)
    return jsonify(list_phones)


@app_views.route(
    "/phones/<phone_id>", strict_slashes=False)
def phones_id(phone_id=None):
    """ This function do the action when requests the GET method and
    an ID of cell number of history.
    Return: The list with the phone of that ID.

    """
    dict_phone = {}
    # Request the information of the phones table.
    _phones = storage.all('Phones').values()
    # For loop to add the phones in a list.
    for phone in _phones:
        if '_sa_instance_state' in phone.__dict__:
            del phone.__dict__['_sa_instance_state']
        if Encrypt(phone_id) == phone.phone:
            dict_phone = phone.__dict__
    return jsonify(dict_phone)
