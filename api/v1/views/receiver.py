#!/usr/bin/python3

from api.v1.views import app_views
from flask import request, jsonify, abort
from function_help import Encrypt, Convert_int
from models import storage
from models.history import History
from models.receiver import Receiver

PETITION_NAME = "The petition 'name' exceeds the limits defined by the server"
PETITION_PHONE = "\
    The petition 'phone' exceeds the limits defined by the server"
PETITION_CASH = "The petition 'cash' exceeds the limits defined by the server"
AMOUNT_INVALIDO = "Invalid amount. Cannot be processed"
SIGN = "Missing positive(+) or negative(-) sign"

@app_views.route(
    "/receiver", methods=['GET', 'POST'], strict_slashes=False)
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
        if 'cash' not in data_json:
            abort(400, description="Missing cash")
        if len(data_json['cash']) > 100:
            abort(413, description=PETITION_CASH)
        encrypted_phone = Encrypt(data_json['phone'])
        data_json['phone'] = encrypted_phone
        new_inst = Receiver(**data_json)
        storage.new(new_inst)
        storage.save()
        new_inst_2 = History(
            phone=data_json['phone'], balance='+ ' + data_json['cash'])
        storage.new(new_inst_2)
        storage.save()
        if '_sa_instance_state' in new_inst.__dict__:
            del new_inst.__dict__['_sa_instance_state']
        if '_sa_instance_state' in new_inst_2.__dict__:
            del new_inst_2.__dict__['_sa_instance_state']
        return jsonify(new_inst.__dict__, new_inst_2.__dict__), 201


@app_views.route(
    "/receiver/<phone_id>", methods=['GET', 'PUT'], strict_slashes=False)
def receiver_id(phone_id=None):
    if request.method == 'GET':
        _receiver = storage.get('Receiver', Encrypt(phone_id))
        if _receiver == []:
            abort(404, description="Phone id. Not found")
        if '_sa_instance_state' in _receiver[0].__dict__:
            del _receiver[0].__dict__['_sa_instance_state']
        return jsonify(_receiver[0].__dict__)
    if request.method == 'PUT':
        data_json = request.get_json()
        if not data_json:
            abort(400, description="Not a JSON")
        if 'cash' not in data_json:
            abort(400, description="Missing cash")
        if len(data_json['cash']) > 100:
            abort(413, description=PETITION_CASH)
        _receiver = storage.get('Receiver', Encrypt(phone_id))
        if _receiver == []:
            abort(404, description="Phone id. Not found")
        encrypted_phone = _receiver[0].__dict__['phone']
        if data_json['cash'].find('+') != -1:
            cash_total = Convert_int(data_json['cash']) + int(
                _receiver[0].__dict__['cash'])
            storage.update('Receiver', encrypted_phone, cash_total)
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
            storage.update('Receiver', encrypted_phone, cash_total)
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
