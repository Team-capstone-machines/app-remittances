#!/usr/bin/python3

from api.v1.views import app_views
from flask import request, jsonify
from function_help import Encrypt
from models import storage
from models.receiver import Receiver


@app_views.route("/receiver", methods=['GET', 'POST'], strict_slashes=False)
def receiver():
    if request.method == 'GET':
        list_receiver = []
        _receiver = storage.all('Receiver').values()
        for receiver in _receiver:
            if '_sa_instance_state' in receiver.__dict__:
                del receiver.__dict__['_sa_instance_state']
            list_receiver.append(receiver.__dict__)
        return jsonify(list_receiver)
    if request.method == 'POST':
        data_json = request.get_json()
        encrypted_phone = Encrypt(data_json['phone'])
        data_json['phone'] = encrypted_phone
        new_inst = Receiver(**data_json)
        storage.new(new_inst)
        storage.save()
        if '_sa_instance_state' in new_inst.__dict__:
            del new_inst.__dict__['_sa_instance_state']
        return jsonify(new_inst.__dict__), 201


@app_views.route(
    "/receiver/<phone_id>", methods=['GET', 'PUT'], strict_slashes=False)
def receiver_id(phone_id=None):
    if request.method == 'GET':
        _receiver = storage.all('Receiver').values()
        for receiver in _receiver:
            if '_sa_instance_state' in receiver.__dict__:
                del receiver.__dict__['_sa_instance_state']
            if Encrypt(phone_id) == receiver.phone:
                return jsonify(receiver.__dict__)
    if request.method == 'PUT':
        data_json = request.get_json()
        encrypted_phone = Encrypt(data_json['phone'])
        user_receiver = storage.get('Receiver', encrypted_phone)
        cash_total = int(data_json['cash']) +\
            int(user_receiver[0].__dict__['cash'])
        storage.update('Receiver', encrypted_phone, cash_total)
        if '_sa_instance_state' in user_receiver[0].__dict__:
            del user_receiver[0].__dict__['_sa_instance_state']
        return jsonify(user_receiver[0].__dict__)
