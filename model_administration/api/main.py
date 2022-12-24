from flask import Flask
from flask_restful import Api

from model_administration import LOCALHOST
from model_administration.api.ModelAdministration import ModelAdministration

app = Flask(__name__)
api = Api(app)

LOCALHOST = "http://127.0.0.1"
ENDPOINT = "/admin"
PORT = 5000

api.add_resource(ModelAdministration, ENDPOINT)

if __name__ == "__main__":
    app.run(host=LOCALHOST, port=PORT, debug=True)
