#!/usr/bin/python3

from api.v1.views import app_views
from flask import request, jsonify
from function_help import Encrypt
from models import storage
from models.history import History

@app_views.route("/history", methods=['GET', 'POST'], strict_slashes=False)
def history():
    if request.method == 'GET':
        list_history = []
        _history = storage.all('History').values()
        for history in _history:
            if '_sa_instance_state' in history.__dict__:
                del history.__dict__['_sa_instance_state']
            list_history.append(history.__dict__)
        return jsonify(list_history)
    if request.method == 'POST':
        data_json = request.get_json()
        encrypted_phone = Encrypt(data_json['phone'])
        data_json['phone'] = encrypted_phone
        new_inst = History(**data_json)
        storage.new(new_inst)
        storage.save()
        if '_sa_instance_state' in new_inst.__dict__:
            del new_inst.__dict__['_sa_instance_state']
        return jsonify(new_inst.__dict__), 201

@app_views.route(
    "/history/<phone_id>", methods=['GET', 'PUT'], strict_slashes=False)
def history_id(phone_id=None):
    if request.method == 'GET':
        list_history = []
        _history = storage.all('History').values()
        for history in _history:
            if '_sa_instance_state' in history.__dict__:
                del history.__dict__['_sa_instance_state']
            if Encrypt(phone_id) == history.phone:
                list_history.append(history.__dict__)
        return jsonify(list_history)