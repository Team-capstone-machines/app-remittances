#!/usr/bin/python3
""" The flask application consuming an API.
"""

from flask import Flask, request, render_template
from function_help import Convert_int, Verify_number, Delete_GMT
import requests

app = Flask(__name__)

# The API URLs
URL_RECEIVER = 'http://0.0.0.0:5001/api/v1/receiver/'
URL_HISTORY = 'http://0.0.0.0:5001/api/v1/history/'


@app.route('/sender', methods=['GET', 'POST'], strict_slashes=False)
def sender():
    """ This function takes the methods GET and POST
    sent from an HTML page of the sender.

    """
    # This condition is to display an HTML page of the sender.
    if request.method == 'GET':
        return render_template('sender.html')
    # This condition is to process the data sent from the
    # HTML page of the sender.
    if request.method == 'POST':
        # Takes the data sent.
        name = request.form['nm']
        phone = request.form['pho']
        cash = Convert_int(request.form['csh'])
        headers = {"Content-Type": "application/json"}
        # This dictionary is constructed with the data.
        dict_post = "{\
            \"name\":\"" + name + "\",\
            \"phone\": \"" + phone + "\",\
            \"cash\": \"" + str(cash) + "\"\
        }"
        verified_number = Verify_number(phone)
        # Condition to check if the name is equal at sent from
        # the HTML page of the sender. Otherwise, failed.
        if verified_number == name:
            # The request to API.
            user_get = requests.get(URL_RECEIVER + phone)
            # Condition to check if the user is registered. Otherwise, update.
            if not user_get:
                requests.post(URL_RECEIVER, data=dict_post, headers=headers)
                return render_template('sended.html')
            else:
                # The body of the API to do the query
                dict_put = "{\
                    \"cash\": \"" + '+ ' + str(cash) + "\"}"
                requests.put(
                    URL_RECEIVER + request.form['pho'],
                    data=dict_put, headers=headers)
                return render_template('sended.html')
        else:
            return 'Invalid name'


@app.route('/receiver', strict_slashes=False)
def receiver():
    """ This function display an HTML page of the receiver.
    Return: the HTML file.

    """
    return render_template('receiver.html')


@app.route(
    '/receiver/<receiver_id>', methods=['POST', 'GET'], strict_slashes=False)
def receiver_id(receiver_id=None):
    """ This function takes the methods GET and POST
    sent from an HTML page of the receiver.

    """
    # This condition is to display an HTML page of the history.
    if request.method == 'GET':
        # Takes the data sent.
        if request.args.get('pho') and receiver_id == 'receiver_id':
            phone = request.args.get('pho')
            name = request.args.get('nm')
        else:
            phone = receiver_id.split('&')[0]
            name = receiver_id.split('&')[1]
        # The request to API.
        verified_number = Verify_number(phone)
        if verified_number == name:
            user_history = requests.get(URL_HISTORY + phone)
            user_history = Delete_GMT(user_history.json())
            user_receiver = requests.get(URL_RECEIVER + phone)
            # The condition to check the status code, if is 200, displays an
            # HTML page of history. Otherwise, failed.
            if user_receiver.status_code == 200:
                cash = user_receiver.json()['cash']
                return render_template(
                    'history.html', list_history=user_history,
                    cash=cash, phone=phone, name=name)
            else:
                return render_template('failed.html')
        else:
            return 'Invalid name'
    # This condition is to process the data sent from
    # the HTML page of the receiver.
    if request.method == 'POST':
        # Takes the data sent.
        name = request.args.get('nm')
        print(name)
        cash = Convert_int(request.form['cash'])
        headers = {"Content-Type": "application/json"}
        # The body of the API to do the query
        dict_put = "{\"cash\": \"" + '- ' + str(cash) + "\"}"
        # The request to API.
        user_update = requests.put(
            URL_RECEIVER + receiver_id, data=dict_put, headers=headers)
        # The condition to check the status code, if is 200, displays an
        # HTML page of history. Otherwise, failed.
        if user_update.status_code == 200:
            user_receiver = requests.get(URL_RECEIVER + receiver_id)
            return render_template(
                'success.html', cash=cash,
                cash_total=user_receiver.json()['cash'])
        else:
            return render_template(
                'exceeded.html', phone=receiver_id, name=name)


@app.route('/receiver/get', strict_slashes=False)
def home_page():
    """ This function display an HTML page of the receiver.
    Return: the HTML file.

    """
    return render_template('receiver.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
