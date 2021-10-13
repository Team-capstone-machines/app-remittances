#!/usr/bin/python3
"""  """

from flask import Flask, render_template, request
from function_help import Convert_int, Encrypt
from models import storage
from models.history import History
from models.receiver import Receiver

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
        if user_data == None:
            new_inst = Receiver(**dict_post)
            storage.new(new_inst)
            storage.save()
            new_inst_2 = History(phone=phone, balance='+ ' + str(cash))
            storage.new(new_inst_2)
            storage.save()
            return render_template('sended.html')
        else:
            cash_total = cash + int(user_data.__dict__['cash'])
            storage.update('Receiver', phone, cash_total)
            new_inst_2 = History(phone=phone, balance='+ ' + str(cash_total))
            storage.new(new_inst_2)
            storage.save()
            return render_template('sended.html')

@app.route('/receiver', methods=['POST', 'GET'], strict_slashes=False)
def receiver():
    """ This function gets, updates the information of the receiver.
    """
    if request.method == 'GET':
        return render_template('receiver.html')

@app.route('/receiver/receiver_id', strict_slashes=False)
def receiver_id():
    name = request.args.get('nm')
    phone = Encrypt(request.args.get('pho'))
    user_history  = storage.get("History", phone)
    user_receiver = storage.get('Receiver', phone)
    if user_history != [] and user_receiver != []:
        return render_template(
            'success.html', history=user_history)
    else:
        return render_template('failed.html')

@app.route('/receiver/get', methods=['POST'])
def receiver_put():
    if request.method == 'POST':
        phone = Encrypt(request.args.get('phone'))
        storage.update("Sender", phone)
        return render_template('payout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
