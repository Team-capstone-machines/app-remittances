#!/usr/bin/python3
""" ResFul API to receiver.

"""

from os import PRIO_PGRP
from api.v1.views import app_views
from flask import request, jsonify, abort
from function_help import Encrypt, Convert_int, Verify_number
from models import storage
from models.history import History
from models.phones import Phones
from models.receiver import Receiver

# Variables for error cases.
PETITION_NAME = "The petition 'name' exceeds the limits defined by the server"
PETITION_PHONE = "\
    The petition 'phone' exceeds the limits defined by the server"
PETITION_CASH = "The petition 'cash' exceeds the limits defined by the server"
AMOUNT_INVALIDO = "Invalid amount. Cannot be processed"
SIGN = "Missing positive(+) or negative(-) sign"

@app_views.route(
    "/receiver", methods=['GET', 'POST'], strict_slashes=False)
def receiver():
    """ This function do the action when requests the
    GET and POST methods to the receiver API.

    """
    # This condition is to returns all the information
    # of the receiver table.
    if request.method == 'GET':
        list_receiver = []
        # Request the information of the receiver table.
        _receiver = storage.all('Receiver').values()
        # For loop to add the receiver in a list.
        for receiver in _receiver:
            if '_sa_instance_state' in receiver.__dict__:
                del receiver.__dict__['_sa_instance_state']
            list_receiver.append(receiver.__dict__)
        return jsonify(list_receiver)
    # This condition is to create information in the receiver table.
    if request.method == 'POST':
        # Conditions to handle the API errors.
        data_json = request.get_json()
        if not data_json:
            abort(400, description="Not a JSON")
        if 'name' not in data_json:
            abort(400, description="Missing name")
        if len(data_json['name']) > 120:
            abort(413, description=PETITION_NAME)
        if 'phone' not in data_json:
            abort(400, description="Missing phone")
        if len(data_json['phone']) > 40:
            abort(413, description=PETITION_PHONE)
        verified_number = Verify_number(data_json['phone'])
        if verified_number == data_json['name']:
            if 'cash' not in data_json:
                abort(400, description="Missing cash")
            if len(data_json['cash']) > 100:
                abort(413, description=PETITION_CASH)
            # Encrypt the phone
            encrypted_phone = Encrypt(data_json['phone'])
            # Request the information of the receiver table.
            user_receiver = storage.get('Receiver', encrypted_phone)
            # This condition checks if the phone is registered.
            # Otherwise, failed.
            if user_receiver == []:
                data_json['phone'] = encrypted_phone
                # Create the new data in the receiver table.
                new_inst = Receiver(**data_json)
                storage.new(new_inst)
                storage.save()
                # Create the new data in the history table.
                new_inst_2 = History(
                    phone=data_json['phone'], balance='+ ' + data_json['cash'])
                storage.new(new_inst_2)
                storage.save()
                # Create the new data in the phone table.
                new_inst_3 = Phones(
                    phone=encrypted_phone, phone_desencrypt=data_json['phone'])
                storage.new(new_inst_3)
                storage.save()
                if '_sa_instance_state' in new_inst.__dict__:
                    del new_inst.__dict__['_sa_instance_state']
                if '_sa_instance_state' in new_inst_2.__dict__:
                    del new_inst_2.__dict__['_sa_instance_state']
                return jsonify(new_inst.__dict__, new_inst_2.__dict__), 201
            else:
                abort(422, description='The record exists. POST not possible ')
        else:
            return jsonify({"name": "Invalid name"})


@app_views.route(
    "/receiver/<phone_id>", methods=['GET', 'PUT'], strict_slashes=False)
def receiver_id(phone_id=None):
    """ This function do the action when requests the
    GET and PUT methods to the receiver API with ID.

    """
    # This condition is to returns all the information
    # of the receiver table with that ID.
    if request.method == 'GET':
        # Request the information of the receiver table.
        _receiver = storage.get('Receiver', Encrypt(phone_id))
        if _receiver == []:
            abort(404, description="Phone id. Not found")
        if '_sa_instance_state' in _receiver[0].__dict__:
            del _receiver[0].__dict__['_sa_instance_state']
        return jsonify(_receiver[0].__dict__)
    # This condition is to create information in the receiver table.
    if request.method == 'PUT':
        data_json = request.get_json()
        # Conditions to handle the API errors.
        if not data_json:
            abort(400, description="Not a JSON")
        if 'cash' not in data_json:
            abort(400, description="Missing cash")
        if len(data_json['cash']) > 100:
            abort(413, description=PETITION_CASH)
        # Request the information of the receiver table.
        _receiver = storage.get('Receiver', Encrypt(phone_id))
        if _receiver == []:
            abort(404, description="Phone id. Not found")
        encrypted_phone = _receiver[0].__dict__['phone']
        # This condition is to check if the cash is to sum or
        # subtraction. Otherwise, failed.
        if data_json['cash'].find('+') != -1:
            cash_total = Convert_int(data_json['cash']) + int(
                _receiver[0].__dict__['cash'])
            # Update the information in the receiver table.
            storage.update('Receiver', encrypted_phone, cash_total)
            # Create the new data in the history table.
            new_inst = History(
                phone=encrypted_phone, balance=data_json['cash'])
            storage.new(new_inst)
            storage.save()
            if '_sa_instance_state' in _receiver[0].__dict__:
                del _receiver[0].__dict__['_sa_instance_state']
            if '_sa_instance_state' in new_inst.__dict__:
                del new_inst.__dict__['_sa_instance_state']
            return jsonify(_receiver[0].__dict__, new_inst.__dict__)
        if data_json['cash'].find('-') != -1:
            cash_total = int(
                _receiver[0].__dict__['cash']) - Convert_int(data_json['cash'])
            if cash_total < 0:
                abort(404, description=AMOUNT_INVALIDO)
            # Update the information in the receiver table.
            storage.update('Receiver', encrypted_phone, cash_total)
            # Create the new data in the receiver table.
            new_inst = History(
                phone=encrypted_phone, balance=data_json['cash'])
            storage.new(new_inst)
            storage.save()
            if '_sa_instance_state' in _receiver[0].__dict__:
                del _receiver[0].__dict__['_sa_instance_state']
            if '_sa_instance_state' in new_inst.__dict__:
                del new_inst.__dict__['_sa_instance_state']
            return jsonify(_receiver[0].__dict__, new_inst.__dict__)
        abort(400, description=SIGN)
