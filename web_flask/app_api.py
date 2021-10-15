#!/usr/bin/python3

from flask import Flask, request, render_template
from function_help import Convert_int
import requests

app = Flask(__name__)

URL_RECEIVER = 'http://0.0.0.0:5001/api/v1/receiver/'
URL_HISTORY = 'http://0.0.0.0:5001/api/v1/history/'


@app.route('/sender', methods=['GET', 'POST'], strict_slashes=False)
def sender():
    """  """
    if request.method == 'GET':
        return render_template('sender.html')
    if request.method == 'POST':
        name = request.form['nm']
        phone = request.form['pho']
        cash = Convert_int(request.form['csh'])
        headers = {"Content-Type": "application/json"}
        dict_post = "{\
            \"name\":\"" + name + "\",\
            \"phone\": \"" + phone + "\",\
            \"cash\": \"" + str(cash) + "\"\
        }"
        user_get = requests.get(URL_RECEIVER + phone)
        if not user_get:
            requests.post(URL_RECEIVER, data=dict_post, headers=headers)
            return render_template('sended.html')
        else:
            dict_put = "{\
                \"cash\": \"" + '+ ' + str(cash) + "\"}"
            requests.put(
                URL_RECEIVER + request.form['pho'],
                data=dict_put, headers=headers)
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
        phone = request.args.get('pho')
        user_history = requests.get(URL_HISTORY + phone)
        user_receiver = requests.get(URL_RECEIVER + phone)
        if user_receiver.status_code == 200:
            cash = user_receiver.json()['cash']
            return render_template(
                'history.html', list_history=user_history.json(),
                cash=cash, phone=phone)
        else:
            return render_template('failed.html')
    if request.method == 'POST':
        cash = Convert_int(request.form['cash'])
        headers = {"Content-Type": "application/json"}
        dict_put = "{\"cash\": \"" + '- ' + str(cash) + "\"}"
        user_update = requests.put(
            URL_RECEIVER + receiver_id, data=dict_put, headers=headers)
        if user_update.status_code == 200:
            user_receiver = requests.get(URL_RECEIVER + receiver_id)
            return render_template(
                'success.html', cash=cash,
                cash_total=user_receiver.json()['cash'])
        else:
            return render_template('exceeded.html')


@app.route('/receiver/get', strict_slashes=False)
def home_page():
    return render_template('receiver.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
