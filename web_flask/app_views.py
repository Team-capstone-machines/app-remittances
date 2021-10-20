#!/usr/bin/python3
"""  """

from flask import Flask, render_template, request
from function_help import Convert_int, Encrypt
from models import storage
from models.history import History
from models.receiver import Receiver
from models.phones import Phones

app = Flask(__name__)


@app.route('/sender', methods=['GET', 'POST'], strict_slashes=False)
def sender():
    """  """
    if request.method == 'GET':
        return render_template('sender.html')
    if request.method == 'POST':
        name = request.form['nm']
        phone = Encrypt(request.form['pho'])
        cash = Convert_int(request.form['csh'])
        dict_post = {
            'name': name,
            'phone': phone,
            'cash': cash
        }
        user_data = storage.get('Receiver', phone)
        if user_data == []:
            new_inst = Receiver(**dict_post)
            storage.new(new_inst)
            storage.save()
            new_inst_2 = History(phone=phone, balance='+ ' + str(cash))
            storage.new(new_inst_2)
            storage.save()
            new_inst_3 = Phones(phone=phone, phone_desencrypt=request.form['pho'])
            storage.new(new_inst_3)
            storage.save()
            return render_template('sended.html')
        else:
            cash_total = cash + int(user_data[0].__dict__['cash'])
            storage.update('Receiver', phone, cash_total)
            new_inst_2 = History(phone=phone, balance='+ ' + str(cash_total))
            storage.new(new_inst_2)
            storage.save()
            return render_template('sended.html')


@app.route('/receiver', strict_slashes=False)
def receiver():
    """ This function gets, updates the information of the receiver.
    """
    return render_template('receiver.html')


@app.route(
    '/receiver/<receiver_id>', methods=['POST', 'GET'], strict_slashes=False)
def receiver_id(receiver_id):
    if request.method == 'GET':
        phone = Encrypt(request.args.get('pho'))
        user_history = storage.get("History", phone)
        user_receiver = storage.get('Receiver', phone)
        if user_history != [] and user_receiver != []:
            cash = user_receiver[0].__dict__['cash']
            return render_template(
                'history.html', list_history=user_history, cash=cash,
                phone=request.args.get('pho'))
        else:
            return render_template('failed.html')
    if request.method == 'POST':
        cash = Convert_int(request.form['cash'])
        phone = Encrypt(receiver_id)
        user_receiver = storage.get('Receiver', phone)
        cash_total = int(user_receiver[0].__dict__['cash']) - cash
        if cash > int(user_receiver[0].__dict__['cash']):
            return render_template('exceeded.html')
        if cash_total > 0:
            storage.update('Receiver', phone, str(cash_total))
            new_inst = History(phone=phone, balance='- ' + str(cash))
            storage.new(new_inst)
            storage.save()
            return render_template(
                'success.html', name=user_receiver[0].__dict__['name'],
                phone=receiver_id, cash=cash, cash_total=cash_total)
        else:
            return render_template('success.html', cash=cash_total)


@app.route('/receiver/get', strict_slashes=False)
def home_page():
    return render_template('receiver.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
