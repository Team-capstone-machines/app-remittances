#!/usr/bin/python3

from api.v1.views import app_views
from flask import Flask, jsonify, request
from flask.helpers import make_response

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(400)
def show_error(error):
    list_errror = str(error).split(': ')
    if list_errror[1] == 'Not a JSON':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing name':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing phone':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing cash':
        return make_response(jsonify({"error": list_errror[1]}), 400)
    if list_errror[1] == 'Missing sign positive(+) or negative(-)':
        return make_response(jsonify({"error": list_errror[1]}), 400)

@app.errorhandler(404)
def show_error(error):
    list_errror = str(error).split(': ')
    if list_errror[1] == 'Phone id. Not found':
        return make_response(jsonify({"error": list_errror[1]}), 404)
    if list_errror[1] == 'Amount invalido. Can not be processed':
        return make_response(jsonify({"error": list_errror[1]}), 404)

@app.errorhandler(413)
def show_error(error):
    list_errror = str(error).split(': ')
    return make_response(jsonify({"error": list_errror[1]}), 413)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
