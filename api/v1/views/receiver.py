#!/usr/bin/python3

from api.v1.views import app_views
from flask import request, jsonify
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
        new_inst = Receiver(**data_json)
        storage.new(new_inst)
        storage.save()
        if '_sa_instance_state' in new_inst.__dict__:
            del new_inst.__dict__['_sa_instance_state']
        return jsonify(new_inst.__dict__), 201

@app_views.route("/receiver/<phone_id>", methods=['GET'], strict_slashes=False)
def receiver_id(phone_id=None):
    _receiver = storage.all('Receiver').values()
    for receiver in _receiver:
        if '_sa_instance_state' in receiver.__dict__:
            del receiver.__dict__['_sa_instance_state']
        if phone_id == receiver.phone:
            return jsonify(receiver.__dict__)
