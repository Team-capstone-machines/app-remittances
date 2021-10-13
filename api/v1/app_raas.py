#!/usr/bin/python3

from api.v1.views import app_views
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
