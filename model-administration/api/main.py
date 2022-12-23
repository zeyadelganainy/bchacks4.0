from api import LOCALHOST
from api.ModelAdministration import ModelAdministration

from flask import Flask
from flask_restful import Api

from Model import MODEL_TO_ENDPOINT, MODEL_TO_PORT

app = Flask(__name__)
api = Api(app)

LOCALHOST = "http://127.0.0.1"
ENDPOINT = "/admin"
PORT = 5000

api.add_resource(ModelAdministration, ENDPOINT)

if __name__ == "__main__":
    app.run(host=LOCALHOST, port=PORT, debug=True)
